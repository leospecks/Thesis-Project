"""
Download CBOT Rough Rice futures (Yahoo Finance ticker: ZR=F) daily history.

Note on what this series actually is: ZR=F is Yahoo's continuous/generic
front-month quote for Rough Rice futures, not one fixed-expiry contract.
The "Nov-2026" label on Yahoo's page just names whichever contract currently
happens to be quoted as the front month; Yahoo does not publish its roll or
price-adjustment convention for this generic series (unlike the DCE panel,
which was built here from each contract's own fields, so the roll rule is
fully under our control). Treat this as a given external input, and note
that limitation if it is used as source-domain data in the thesis.
"""

from pathlib import Path
import yfinance as yf

TICKER = "ZR=F"
OUT_DIR = Path("2_data/2.1_raw/yahoo")  # adjust to match your project layout
OUT_PATH = OUT_DIR / "ZR=F_rough_rice_daily.csv"

df = yf.download(TICKER, period="max", interval="1d", auto_adjust=False)
df.index.name = "date"

OUT_DIR.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT_PATH)

print(f"{len(df):,} rows | {df.index.min().date()} to {df.index.max().date()}")
print(f"Saved to {OUT_PATH.resolve()}")
