# Literature Map and Gap Analysis

**Thesis:** Transfer Learning for Cross-Market Commodity Return Forecasting: Leveraging Data-Rich Markets to Improve Predictions in Data-Sparse Economies
**Prepared:** August 2026 | **Corpus reviewed:** 19 papers currently in the project library

---

## 1. How the corpus maps onto Chapter 2

Chapter 2 of the thesis structure has six sections. The table below assigns each of the 19 papers to its primary section(s) (●) and secondary relevance (○).

| Paper | 2.1 Classical forecasting | 2.2 ML/DL in commodities | 2.3 Transfer learning / domain adaptation | 2.4 Cross-market co-movement | 2.5 Data scarcity, EM | 2.6 Research gap |
|---|---|---|---|---|---|---|
| Pan & Yang (2010) — TL survey | | | ● | | | ○ |
| Mashetty et al. (2025) — TL equities, EM | | | ● | ○ | ● | ● |
| Hao et al. (2025) — CNN images, US→China | | ● | ● | ○ | ● | ● |
| Merello et al. (2019) — TL cross-stock | | ○ | ● | | ○ | |
| Alquist et al. (2020) — comovement factor model | ○ | | | ● | | |
| Byrne et al. (2020) — heterogeneous comovement | ○ | | | ● | | |
| Cerqueti et al. (2024) — attention network spillover | | ● | | ○ | | |
| Hao & Pham (2024) — clean energy/oil connectedness | | ○ | | ● | | |
| Tissaoui & Azibi (2026) — sentiment momentum, oil | | ○ | | ● | | |
| Yang et al. (2026) — climate vulnerability, ag | | ○ | | ● | ○ | |
| Gargano & Timmermann (2014) — macro predictors | ● | | | | | ○ |
| Guidolin & Pedio (2021) — stepwise regressions | ● | | | ○ | | ○ |
| Guidolin & Ionta (2026) — climate predictors | ● | | | | | ○ |
| Nguyen & Walther (2018) — GARCH-MIDAS volatility | ● | | | ○ | | ○ |
| Giampietro et al. (2018) — regime-switching SDF | ● | | | ○ | | |
| Moghadam (2025) — sentiment FIGARCH | ○ | ● | | | | ○ |
| Sun et al. (2023) — ag price forecasting review | ● | ● | | | ○ | |
| Auer (2021) — trend-following reliability | ● | | | | | |
| Masteika et al. (2012) — continuous futures series | (data methodology only) | | | | | |

Three papers do the real load-bearing work for the thesis's core argument: **Pan & Yang (2010)** for TL vocabulary, **Mashetty et al. (2025)** as the direct predecessor being extended, and **Hao et al. (2025)** as the only paper that actually runs a cross-market commodity transfer-learning experiment (and finds it fails naively). Everything else supplies the surrounding economic and econometric scaffolding.

---

## 2. Connecting the papers

**The TL spine.** Pan & Yang (2010) supplies the taxonomy — domain vs. task, inductive/transductive/unsupervised TL, instance/feature/parameter/relational transfer, and the concept of negative transfer, which it flags in 2010 as understudied. Mashetty et al. (2025) operationalizes a subset of this taxonomy for finance: source pre-training → MMD-based domain adaptation → fine-tuning, applied to S&P 500 → NIFTY 50/BOVESPA equity indices. Merello et al. (2019) is a useful worked example one level down: pooled pre-training across ten NASDAQ stocks, fine-tuning only the last layer per stock, with an explicit finding that some stocks needed zero fine-tuning epochs while others needed the maximum — evidence that transfer benefit is heterogeneous even within a single, developed, liquid market. Hao et al. (2025) is the paper that closes the loop for the thesis's actual asset class: it runs the equivalent experiment for commodities (CNN trained on US futures, applied directly to Chinese futures) and finds naïve transfer *underperforms* retraining from scratch, attributing this to commodity returns being driven by localized supply/demand/policy factors rather than the global macro forces that make equity-index transfer more forgiving. Read together, these four papers frame the thesis's central bet precisely: Mashetty shows the pipeline works for equities, Hao et al. shows a cruder version of the same idea fails for commodities without proper domain adaptation, and Pan & Yang supplies the language (negative transfer, domain shift, transductive TL) for explaining why. The thesis's job is to show whether a properly adapted (MMD/DANN, staged fine-tuning) version of the pipeline can succeed where Hao et al.'s naïve version failed.

**The cross-market/co-movement layer.** Alquist et al. (2020) and Byrne et al. (2020) both decompose commodity price co-movement into common and idiosyncratic factors, and both find that co-movement is heterogeneous across commodity sectors and increasingly driven by emerging-market (especially Chinese) demand since 2000 — this is useful indirect evidence for *why* a developed-market source domain might carry transferable signal about developing-market-relevant commodities. Cerqueti et al. (2024), Hao & Pham (2024), Tissaoui & Azibi (2026), and Yang et al. (2026) each demonstrate a different spillover/connectedness mechanism (investor attention, higher-moment volatility, sentiment-derivative regime dependence, climate-shock vulnerability) — collectively they establish that commodity markets are richly interconnected through several channels beyond simple price correlation, which supports the economic plausibility of transfer but does not itself test transferability of forecasting *models*. None of these six papers involve a developing-market target series; the "cross-market" story in this literature is cross-*commodity* or cross-*asset-class* (oil vs. clean-energy equities, oil vs. VIX/MOVE), not cross-*country*.

**The classical/econometric benchmark layer.** Gargano & Timmermann (2014), Guidolin & Pedio (2021), Guidolin & Ionta (2026), Nguyen & Walther (2018), Giampietro et al. (2018), and Auer (2021) collectively establish what "good" classical forecasting performance looks like for developed-market commodity benchmarks (mostly US-listed futures/indices, 1970s–2010s samples): modest and horizon-dependent predictability from macro/financial variables, frequent failure to beat a random-walk or AR(1) benchmark on pure statistical loss even when economic-value gains (Sharpe ratio, CER) are positive, and no single model dominating across commodities. This is directly useful as the thesis's baseline-model justification (Chapter 4.5 already lists ARIMA-GARCH and target-only models) and as a recurring cautionary theme: statistical accuracy and economic value diverge, so the thesis's evaluation section (5.6, economic significance) is well precedented by this cluster. Sun et al. (2023) and Moghadam (2025) extend this into ML/hybrid territory (SVM, LSTM, decomposition-ensemble methods for Sun; Random Forest + FinBERT + FIGARCH for Moghadam) but both remain single-market, no-transfer exercises — reinforcing, by their absence of any TL component, the same gap Mashetty and Hao et al. address directly.

**The odd one out.** Masteika et al. (2012) is not conceptually connected to the others — it is a practitioner note on continuous futures series construction (roll-adjustment methods). Its only role is methodological: if the thesis builds its own continuous futures price series from raw contract data, this paper documents the standard adjustment choices and their distortions.

---

## 3. Gaps by section

**2.1 Classical approaches — well covered, one omission.** The corpus has strong US/developed-market coverage (Gargano & Timmermann, Guidolin & Pedio, Guidolin & Ionta, Nguyen & Walther, Auer) across regression, stepwise-selection, GARCH-MIDAS, and technical-signal approaches. Missing: a dedicated ARIMA/VAR/GARCH benchmark study for **metals or energy** written outside the Guidolin/Pedio cluster (all four of those papers share overlapping authorship and similar US-exchange data, which narrows independence of the "classical benchmark" evidence base). Sun et al. (2023) covers classical methods but is agriculture- and China-specific.

**2.2 ML/DL in commodity markets — thin.** Only Cerqueti et al. (2024, network/factor model), Hao et al. (2025, CNN images), Moghadam (2025, RF + FinBERT), and Sun et al. (2023, review) touch this section, and none benchmark the specific architectures the thesis methodology chapter commits to (LSTM, TCN). There is no paper in the corpus that trains and evaluates an **LSTM or TCN specifically on commodity return/price forecasting** with a proper walk-forward design — this is a direct hole against Chapter 4.2's architecture choice and should be filled before writing 2.2.

**2.3 Transfer learning — foundations present, technical core missing.** This is the most consequential gap. The thesis structure explicitly commits to Maximum Mean Discrepancy and DANN as the two domain-adaptation mechanisms (Section 4.3), and its own "Key Methodological Papers to Read First" list names **Long et al. (2015)** on MMD-based Deep Adaptation Networks and **Ganin et al. (2016)** on Domain-Adversarial Neural Networks — neither is in the library. Right now, MMD and DANN are only known to this project through Mashetty et al.'s secondary (and under-specified — no hyperparameters, no sample period, thin methodological detail) description. Citing the original technical papers is not optional here: without them, Chapter 4's formal loss functions (L_DA, the gradient-reversal layer) have no primary source. Also referenced by Hao et al. (2025) but absent from the library: **Jiang et al. (2023)**, who reportedly found that image-based equity patterns *do* transfer successfully across international stock markets — this is the natural counter-case to Hao et al.'s negative commodity result and would sharpen the equities-vs-commodities contrast the thesis wants to draw in Section 6.2. A general modern survey of domain adaptation for time series (post-2010, since Pan & Yang predates deep-learning-era TL entirely) would also help bridge the 15-year gap between the foundational taxonomy and current practice.

**2.4 Cross-market commodity dynamics — well covered but wrong axis.** Six papers address spillover/co-movement richly, but every one of them operates *within* developed markets or *across commodities/asset-classes*, never across a developed-market benchmark and a developing-country local commodity price. The thesis structure explicitly asks this section to cover the **law of one price**, **price transmission to local/domestic markets**, and **country-specific wedges** (exchange-rate risk, storage infrastructure, political risk) — none of the 19 papers address this. This is a real gap: the literature the thesis needs here is the agricultural/development-economics price-transmission literature (e.g., studies of world-price pass-through to local grain or oil markets in African, South/Southeast Asian, or Latin American economies), plus the "commodity currencies" literature (Chen & Rogoff-style work linking exporter exchange rates to commodity prices — touched on only as a predictor-variable footnote in Gargano & Timmermann, not as its own literature stream).

**2.5 Data scarcity in emerging economies — the thinnest section.** Only Mashetty et al. (asserted, not evidenced — no sample details given) and Hao et al. (2025, the strongest evidence: explicit description of the Chinese commodity market's shorter history, retail-dominated trading, position limits) substantively address this theme. The thesis structure asks for coverage of short time series, missing observations, reporting lags, and currency-denomination issues, and for a critical discussion of *why* imputation/oversampling is inferior to transfer learning for this problem — nothing in the corpus makes that comparison. This section needs dedicated sourcing: empirical finance papers on data quality/availability in frontier or emerging commodity exchanges, and ideally something on synthetic-data or imputation approaches in low-data financial forecasting to serve as the "straw man" the thesis argues transfer learning improves upon.

**2.6 Research gap — adequately supported by synthesis, not by any single paper.** No paper does this work for you (nor should one); the gap argument has to be assembled from the pieces above. The corpus currently supports the "commodities differ from equities" plank (via Hao et al.) and the "existing commodity forecasting is single-market" plank (via the whole classical/ML cluster) reasonably well. It does not yet support the "developing-market data-transmission" plank (2.4 gap) or the "data-scarcity mechanics" plank (2.5 gap) described above.

**Also absent but needed for Chapter 4/5 methodology, not the literature review per se:** Diebold & Mariano (1995), also named in the thesis's own reading list, is not in the corpus and is required to justify the forecast-comparison tests specified in Section 4.6/Appendix D. Foundational architecture papers (Hochreiter & Schmidhuber on LSTM; Bai, Kolter & Koltun on TCN) are likewise absent and would normally be cited alongside the Chapter 4 model specification rather than the literature review.

---

## 4. Priority list to close the gaps

1. Long et al. (2015), *Learning Transferable Features with Deep Adaptation Networks* — MMD mechanism, primary source.
2. Ganin et al. (2016), *Domain-Adversarial Training of Neural Networks* — DANN mechanism, primary source.
3. Diebold & Mariano (1995) — forecast-comparison test, needed for Chapter 4/5 and 2.1.
4. One or two papers on price transmission from global benchmark to local commodity markets in developing economies (law-of-one-price / exchange-rate pass-through literature) — fills 2.4's actual gap.
5. One or two papers specifically on financial data scarcity/quality in emerging or frontier markets — fills 2.5.
6. Jiang et al. (2023) (the positive-transfer equity counter-case cited inside Hao et al.) — sharpens the 2.6 contrast.
7. A benchmark LSTM/TCN-for-commodities paper — fills 2.2 and directly supports the Chapter 4 architecture choice.

Items 1–3 are the most urgent: they are already committed to in the thesis's own methodology chapter and reading list, so their absence is the sharpest inconsistency between what the thesis promises to build on and what the library currently contains.
