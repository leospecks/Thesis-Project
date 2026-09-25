"""SQLite-backed shared results store for cross-pair analysis.

Two tables, deliberately kept separate:

  run_log  -- one row per pipeline stage completed for one pair/run, for
              provenance and debugging ("did corn_china's Stage B actually
              run, and with what config?"). Not itself an evaluation result.
  results  -- long-format forecasting-evaluation metrics: one row per
              (pair_id, tier, seed, horizon_h, metric_name), ready to feed the
              random-effects meta-analytic framework logged in
              decision_log.md (2026-09-16 pivot entry, sub-decision (b)).

Long format (one metric per row) rather than wide (one column per metric) so
that adding a new metric or a new tier never requires a schema migration --
only new rows.

config_hash is a short hash of the resolved PairConfig (plus any run-time
hyperparameters passed in), so two runs of the same pair/tier with different
settings do not silently collide, and a stale result can be identified.
"""
from __future__ import annotations

import hashlib
import json
import sqlite3
from contextlib import contextmanager
from dataclasses import asdict, is_dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Optional

RUN_LOG_SCHEMA = """
CREATE TABLE IF NOT EXISTS run_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pair_id TEXT NOT NULL,
    stage TEXT NOT NULL,
    status TEXT NOT NULL,          -- "completed" | "failed" | "skipped_not_implemented"
    config_hash TEXT,
    detail TEXT,
    run_timestamp TEXT NOT NULL
);
"""

RESULTS_SCHEMA = """
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pair_id TEXT NOT NULL,
    tier TEXT NOT NULL,            -- e.g. "A_family", "B_restricted", "B_full",
                                    -- "C_zero_shot", "D_fine_tuned", "E_domain_adapted", "RF"
    seed INTEGER,
    horizon_h INTEGER,
    metric_name TEXT NOT NULL,     -- e.g. "RMSE", "MAE", "R2_OOS", "directional_accuracy", "DM_stat"
    metric_value REAL NOT NULL,
    config_hash TEXT,
    run_timestamp TEXT NOT NULL,
    notes TEXT,
    UNIQUE(pair_id, tier, seed, horizon_h, metric_name, config_hash)
);
"""


def _utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def config_hash(config_obj) -> str:
    """Short, stable hash of a config (dataclass, dict, or anything json-able).

    Path objects are stringified so the same logical config hashes identically
    regardless of which machine resolved the absolute paths.
    """
    payload = asdict(config_obj) if is_dataclass(config_obj) else config_obj
    normalized = json.loads(json.dumps(payload, default=str, sort_keys=True))
    blob = json.dumps(normalized, sort_keys=True).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()[:12]


@contextmanager
def _connect(db_path: Path):
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    try:
        conn.execute(RUN_LOG_SCHEMA)
        conn.execute(RESULTS_SCHEMA)
        yield conn
        conn.commit()
    finally:
        conn.close()


def log_run(db_path: Path, pair_id: str, stage: str, status: str,
            config_hash_val: Optional[str] = None, detail: str = "") -> None:
    with _connect(db_path) as conn:
        conn.execute(
            "INSERT INTO run_log (pair_id, stage, status, config_hash, detail, run_timestamp) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (pair_id, stage, status, config_hash_val, detail, _utcnow()),
        )


def upsert_result(db_path: Path, pair_id: str, tier: str, metric_name: str, metric_value: float,
                   seed: Optional[int] = None, horizon_h: Optional[int] = None,
                   config_hash_val: Optional[str] = None, notes: str = "") -> None:
    """Insert one metric row, replacing any prior row with the same identifying key.

    The UNIQUE constraint on (pair_id, tier, seed, horizon_h, metric_name,
    config_hash) means a rerun with an IDENTICAL config overwrites its own
    prior result (idempotent reruns); a rerun with a CHANGED config
    (different config_hash) adds a new row rather than overwriting, so a
    result is never silently lost when a setting changes.
    """
    with _connect(db_path) as conn:
        conn.execute(
            """
            INSERT INTO results
                (pair_id, tier, seed, horizon_h, metric_name, metric_value, config_hash, run_timestamp, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(pair_id, tier, seed, horizon_h, metric_name, config_hash)
            DO UPDATE SET metric_value = excluded.metric_value,
                          run_timestamp = excluded.run_timestamp,
                          notes = excluded.notes
            """,
            (pair_id, tier, seed, horizon_h, metric_name, metric_value,
             config_hash_val, _utcnow(), notes),
        )


def upsert_results_batch(db_path: Path, rows: Iterable[dict]) -> None:
    for row in rows:
        upsert_result(db_path, **row)


def query_results(db_path: Path, pair_ids: Optional[Iterable[str]] = None,
                   tiers: Optional[Iterable[str]] = None,
                   metric_name: Optional[str] = None):
    """Return matching rows from `results` as a pandas DataFrame."""
    import pandas as pd

    clauses, params = [], []
    if pair_ids is not None:
        pair_ids = list(pair_ids)
        clauses.append(f"pair_id IN ({','.join('?' * len(pair_ids))})")
        params += pair_ids
    if tiers is not None:
        tiers = list(tiers)
        clauses.append(f"tier IN ({','.join('?' * len(tiers))})")
        params += tiers
    if metric_name is not None:
        clauses.append("metric_name = ?")
        params.append(metric_name)
    where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
    with _connect(db_path) as conn:
        return pd.read_sql_query(f"SELECT * FROM results {where}", conn, params=params)
