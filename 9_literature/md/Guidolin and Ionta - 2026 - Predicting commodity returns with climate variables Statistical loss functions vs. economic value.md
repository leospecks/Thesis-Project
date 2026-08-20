Economics Letters 265 (2026) 113028
Contents lists available at ScienceDirect
EconomicsLetters
journal homepage: www.elsevier.com/locate/ecolet
Predictingcommodityreturnswithclimatevariables:Statisticalloss
(cid:73)
functionsvs.economicvalue
Massimo Guidolin ∗, Serena Ionta
Finance Department, Bocconi University,Italy
A R T I C L E I N F O A B S T R A C T
JEL classification: We test whether large-scale climate indicators contribute to the predictability of commodity futures returns
G11 and generate economic value for investors. Using monthly data on fourteen commodities, we conduct a pseudo
G17 out-of-sample forecasting exercise based on a range of models that include automatic variable selection and
Q54 nonlinear regime-switching specifications. Climate-related predictors rarely outperform standard benchmarks
C53
in terms of statistical forecast accuracy. Yet, when embedded in a portfolio choice problem, they deliver
C58
economically meaningful gains. These results illustrate a disconnect between statistical predictability and
Keywords: economic relevance.
Commodity futures
Climate risk
Hidden Markov models
Loss functions
Certainty equivalent returns
1. Introduction 2017). Recent work in finance further shows that physical climate risk
can be priced in asset markets, although most contributions focus on
Commodity futures represent a major asset class, offering diversi- equities rather than commodities (Choi et al., 2020; Kruttli et al., 2025).
fication benefits, inflation hedging, and equity-like long-run returns Nonetheless, it is unclear whether large-scale climate indicators pro-
(Gorton and Rouwenhorst, 2006). Despite their relevance, evidence vide information beyond macroeconomic factors that can be exploited
on short-horizon return predictability in commodity futures remains to improve short-horizon forecasts of commodity futures returns and,
mixed, and the nature of the underlying priced risks is debated. It crucially, whether they generate economically meaningful gains when
is unclear whether commodity futures returns are primarily driven embedded in portfolio problems and, more generally, in actual financial
by a common stochastic discount factor or by specific sources of decisions (Tedeschi et al., 2024). Our paper addresses this gap by
risk (De Roon et al., 2000).
jointly evaluating whether climate information adds to macroeconomic
Climate shocks are a natural candidate for such commodity risks
predictors in terms of predictive performance and/or whether, even
because they impact directly production, inventories, and transporta-
when statistical predictability is weak, this translates into risk-adjusted
tion constraints, thereby shifting marginal costs and convenience yields
gains to investors.
(Yang et al., 2026). A prominent example is represented by telecon-
We use monthly data on futures returns for a cross-section of four-
nections, i.e., persistent atmospheric oscillations linking geographically
teen commodities over the period January 1989 to May 2018, collected
distant regions. Heino et al. (2018) document that teleconnections
from Thomson Reuters Eikon. Climate information is summarized using
affect global cropland areas and discuss their relevance for commodity
PCs extracted from a broad set of large-scale atmospheric and climate
markets. Among large-scale climate phenomena, the El Niño–Southern
indicators, which are included alongside macroeconomic factors in the
Oscillation represents a salient source of persistent and geographically
heterogeneous climate shocks, with documented effects on both spot
information set.
and futures prices, particularly for agricultural commodities. More
Our design relies on three classes of forecasting models. First, we es-
broadly, climate-driven shocks propagate beyond commodity markets, timate predictive regressions in which predictors are chosen recursively
affecting global inflation dynamics and economic activity (Cashin et al., from a large set using stepwise selection guided by information criteria,
(cid:73)
We thank an anonymous associate editor and one anonymous referee for constructive comments and encouragement.
∗ Corresponding author.
E-mail addresses: massimo.guidolin@unibocconi.it (M. Guidolin), serena.ionta2@unibocconi.it (S. Ionta).
https://doi.org/10.1016/j.econlet.2026.113028
Received 6 February 2026; Received in revised form 22 April 2026; Accepted 5 May 2026
Available online 11 May 2026
0165-1765/© 2026 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/) .

M. Guidolin and S. Ionta Economics Letters 265 (2026) 113028
allowing the specification to adapt to evolving predictor relevance and We retain the first 𝐾 = 5 principal components (PCs), which jointly
parameter instability. Second, we extend these baseline models with explain over 50% of the total variance of the climate information set.
regime-dependent features indexed to market volatility, so that both The selected climate PCs enter the regressions as candidate predictors
the set of included predictors and their predictive content may differ and are subject to the same recursive variable selection procedure as
across states (DeMiguel et al., 2009; Cederburg et al., 2023). Third, we the other regressors. For consistency, macroeconomic information is
employ nonlinear models based on hidden Markov dynamics, which summarized using the first eight principal extracted from a large panel
allow regression coefficients to vary across latent regimes and capture of U.S. macroeconomic and financial variables.
state dependence in the relationship between climate conditions and
commodity returns (Ang and Timmermann, 2012).
2.2. Nonlinear models and regime dependence
Forecasts are generated at a one-month horizon within a recursive
pseudo-out-of-sample design and evaluated relative to an AR(1) bench-
To allow for potential state dependence in return predictability, we
mark. To assess economic relevance, the same forecasts are embedded
in a portfolio allocation exercise for a power-utility investor, follow-
consider two complementary classes of models. First, stepwise predic-
ing DeMiguel et al. (2009). Performance is measured using certainty-
tive regressions are estimated allowing for regime dependence based
equivalent returns, i.e., the constant return that delivers the same
on market volatility, distinguishing between high- and low-volatility
average utility as the realized of portfolio returns. Our results convey
periods.2 Second, we estimate nonlinear predictive models based on
a clear message. When forecast accuracy is assessed solely by statisti-
hidden Markov dynamics (Ang and Timmermann, 2012), in which
cal loss, climate-based predictors rarely outperform the benchmarks. coefficients vary across latent regimes:
However, when forecasts are mapped into portfolio decisions, cli- 𝑅𝑗 =𝛼𝑗 +𝐙′𝜷𝑗 +𝜀𝑗 , 𝑠 ∈{1,…,𝑆}, (4)
mate signals generate meaningful gains, even when their improvements 𝑡+1 𝑠𝑡 𝑡 𝑠𝑡 𝑡+1 𝑡
under conventional loss functions are modest. This evidence high- where the latent state 𝑠 follows a first-order Markov process. Markov
𝑡
lights a wedge between statistical predictability and economic value switching models capture abrupt changes in the conditional mean dy-
in commodity markets when climate information is used, consistent namics and provide a flexible representation of nonlinear predictability.
with the literature on forecast evaluation and economic performance
(Cenesizoglu and Timmermann (2012)).
2.3. Economic value and portfolio allocation
2. Research design
To assess the economic relevance of the forecasts, we embed the
predictive signals into a recursive portfolio allocation problem for a
We study the predictability of commodity futures returns using a
myopic investor with power utility in which, at each time 𝑡, the investor
recursive framework. For each commodity 𝑗, we consider the one–
chooses portfolio weights 𝝎 to solve
month–ahead predictive regression 𝑡
[ ]
𝑅𝑗 𝑡+1 =𝛼 𝑡 𝑗+𝐙′ 𝑡 𝜷𝑗 𝑡 +𝜀𝑗 𝑡+1 , (1) m 𝝎 a 𝑡 x E 𝑡 (1+𝝎 1 ′ 𝑡 − 𝐑 𝑡 𝛾 +1 )1−𝛾 s.t. 𝝎′ 𝑡 𝟏=1, 𝜔 𝑖,𝑡 ≥0, (5)
where 𝑅𝑗 denotes excess return between 𝑡 and 𝑡 + 1 and 𝐙 is a
vector of
𝑡 +
l
1
agged predictors observed at time 𝑡. Model parameter
𝑡
s are
where 𝛾 is the coefficient of relative risk aversion, 𝐑
𝑡+1
collects the
estimated using an expanding window. Following, e.g., Dal Pra et al.
returns on commodities, equities, bonds, and cash. The climate-based
(2018), forecasts are generated using a recursive, pseudo out-of-sample
predictive signals are employed exclusively for commodities, while
design. At each forecast origin, the estimation sample is expanded by
forecasts for equities and bonds are obtained using the benchmark
one observation and the model is re-estimated using only information models.
available up to time 𝑡. The pseudo out-of-sample evaluation period Following DeMiguel et al. (2009), portfolio performance is evalu-
spans from December 2003 to April 2018. ated using the certainty equivalent return (CER). Let 𝑟 𝑝,𝑡 denote the
Forecast accuracy is evaluated relative to a benchmark AR(1) model, realized return of strategy 𝑝 and 𝑟 𝑏,𝑡 the return of the AR(1) benchmark.
The out-of-sample certaintyequivalent return 𝛥𝐶𝐸𝑅 is defined as:
𝑝
𝑅𝑗 𝑡+1 =𝛼 𝑡 𝑗+𝜃 𝑡 𝑗𝑅𝑗 𝑡 +𝑣𝑗 𝑡+1 , (2) 1 ∑ 𝑇 (1+𝑟 )1−𝛾 = 1 ∑ 𝑇 [ (1+𝛥𝐶𝐸𝑅 )(1+𝑟 ) ]1−𝛾 . (6)
𝑇 𝑝,𝑡 𝑇 𝑝 𝑏,𝑡
which captures the (weak) autocorrelation structure typically observed 𝑡=1 𝑡=1
in commodity futures returns. Statistical forecasting performance is We also consider an alternative specification incorporating transaction
assessed using the root mean squared forecast error (RMSFE).1 costs proportional to portfolio rebalancing.
2.1. Principal component analysis
2.4. Data
The predictor set includes macroeconomic variables and climate-
based indicators. Given the potentially large dimensionality of such a
We consider monthly excess returns on fully collateralized futures
set, we adopt a sparse forecasting approach in which relevant predictors
contracts for a cross-section of 14 commodities over the period January
are selected recursively using stepwise regression procedures based on
1989 to May 2018.3 Data are obtained from Thomson Reuters Eikon.
the Akaike Information Criterion, implemented through both forward The commodity universe includes agricultural commodities (corn, soy-
and backward selection. beans, wheat, cocoa, coffee, cotton, and sugar), soft commodities
Climate information is summarized using principal component anal- (frozen orange juice, lumber, and live cattle), energy (light crude oil),
ysis applied to a vector 𝐂 ∈R𝑛 collecting 𝑛 large-scale atmospheric and
𝑡
climate indicators. The 𝑘th climate principal component is defined as
2 Market volatility regimes are identified using the VIX index as a proxy for
𝑃𝐶
𝑘,𝑡
=𝐮′
𝑘
𝐂
𝑡
, 𝑘=1,…,𝐾. (3)
aggregate uncertainty. Specifically, we estimate a two-state Markov-switching
model for the VIX and classify each period as belonging to a high- or
low-volatility regime based on the filtered regime probabilities.
1 We also test forecast accuracy using mean absolute error. The results are 3 Details on data sources and summary statistics are provided in Online
qualitatively similar to those reported and are available upon request. Appendix A.
2

M. Guidolin and S. Ionta Economics Letters 265 (2026) 113028
and precious metals (gold, silver, and platinum). For each commodity Table 1
𝑗, returns are computed at a monthly frequency as Classification of commodities by climate exposure.
𝐹𝑗 Climate-Exposed Commodities (CE) Less Climate-Exposed Commodities (LCE)
𝑅𝑗 = 𝑡+1 −1, (7) Corn Light (Crude Oil)
𝑡+1 𝐹𝑗
Soybeans Gold
𝑡
Wheat Silver
where 𝐹 𝑡 𝑗 denotes the end-of-month futures price. Positions are sys- Coffee Platinum
tematically rolled into the second-nearest contract to avoid delivery Cocoa
effects. Sugar
Cotton
Climate information is based on a set of 13 large-scale atmospheric
FOJ
and climate indicators capturing persistent global climate variability. Lumber
The set includes major teleconnection indices describing large-scale Live Cattle
atmospheric circulation patterns (such as ENSO-related measures and Commodities are classified based on their exposure to climate-related shocks, following
Pacific and Atlantic oscillations), together with global indicators of Heino et al. (2018) and Yang et al. (2026). Climate-exposed commodities include
drought conditions and temperature anomalies. These variables are agricultural, soft, and livestock commodities, as well as lumber, whose production is
common across commodities and observed at a monthly frequency. Cli-
d
in
ir
c
e
lu
c
d
tl
e
y a
e
f
n
f
e
e
r
c
g
te
y
d
a
b
n
y
d
w
p
e
r
a
e
t
c
h
io
er
u s
a n
m
d
e
c
ta
li
l
m
s,
at
w
e
h
c
i
o
ch
n d
a
it
r
i
e
o n
e
s
i
.
t h
L
e
e
r
s s
i
c
n
l
d
im
ire
a
c
te
tl
-
y
e x
a
p
f
o
f
s
e
e
c
d
te d
co m
or
m
l
o
a
d
rg
it
e
ie
ly
s
mate data are obtained from standard sources, including the National
insensitive to climate variability in the short run.
Oceanic and Atmospheric Administration and its Climate Prediction
Center, as well as the National Centers for Environmental Information.
All series are transformed to ensure stationarity prior to analysis. All se-
display greater dispersion across models and specifications. Nonethe-
ries are transformed to ensure stationarity prior to analysis. Appendix A
less, a directionally consistent pattern emerges in the HMM results
provides a detailed description of the climate variables and their data
(Table 3): augmenting the macro-only HMM with climate factors re-
sources.
duces average RMSFE for climate-exposed commodities (from 0.0942
Macroeconomic information is summarized using PCs extracted
to 0.0933) while increasing it for less climate-exposed ones (from
from a large monthly dataset compiled by Ludvigson and Ng (2009),
0.0949 to 0.1014), suggesting that climate information is at least not
which includes 132 U.S. macroeconomic and financial time series span-
detrimental — and marginally useful — for the group whose returns
ning real activity, labor markets, prices, interest rates, and financial
are more directly tied to weather conditions.
market indicators.
3.2. Economic value
3. Results
Table 4 reports annualized 𝛥𝐶𝐸𝑅 relative to the AR(1) benchmark.4
3.1. Baseline out-of-sample forecasting performance
In the absence of transaction costs, the Hidden Markov Model aug-
mented with macroeconomic and climate factors delivers the highest
As regards the stepwise linear predictive regressions, out-of-sample
economic value across all levels of risk aversion, with 𝛥𝐶𝐸𝑅 equal to
RMSFE are reported in Table 6 of Online Appendix B. While stepwise
0.56%, 0.68%, and 0.86% for 𝛾=2,5, and 10, respectively. By contrast,
variable selection reduces forecast errors relative to the kitchen-sink
the macro-only HMM generates smaller gains, while stepwise strategies
specification, which suffers from severe overfitting, none of the models
yield negative 𝛥𝐶𝐸𝑅 throughout.
outperform the AR(1) benchmark. Moreover, the inclusion of climate
These gains arise despite the lack of systematic improvements in
factors does not yield systematic gains in forecast accuracy.
forecast accuracy: as shown earlier, climate-based models rarely out-
To investigate heterogeneity across commodities, Table 1 classi-
perform the AR(1) benchmark in terms of RMSFE. This evidence is
fies assets into climate-exposed (CE) and less climate-exposed (LCE)
in line with the literature documenting a disconnect between predic-
groups. Climate-exposed commodities include agricultural, soft, and
tive performance and economic value, whereby models with weak or
livestock commodities, as well as lumber, whose returns are more di-
modest forecast accuracy can generate economically meaningful gains
rectly affected by weather and climate conditions. Less climate-exposed
when evaluated in a portfolio context (Dal Pra et al., 2018). Although
commodities include energy and precious metals, whose exposure to
stepwise strategies remain unprofitable, the inclusion of climate in-
climate variability is less direct. This classification allows us to as-
formation consistently mitigates their losses relative to macro-only
sess whether climate variables provide stronger predictive gains for
specifications.
commodities that are more directly exposed to weather conditions.
Table 2 reports out-of-sample RMSFE by periods classified by
Panel B shows that these conclusions are robust to the inclusion
volatility regimes, using the filtered probabilities of a regime switching
of transaction costs. Overall, climate risk appears to affect optimal
model applied to the VIX. In low-volatility periods, stepwise regres-
portfolio allocation and risk exposures to deliver higher realized risk-
sions outperform the AR(1) benchmark for most commodities (12 out
adjusted performance rather than short-horizon return statistical pre-
of 14), with gains largely driven by macroeconomic specifications
dictability.5 We report bootstrap confidence intervals for CER differ-
(10 out of 12 cases). Climate variables provide additional improve-
ences in Table 7 (Appendix B). While these intervals are generally wide
ments over macro-only models in only three cases. In high-volatility
and often include zero, in several cases the confidence intervals for
periods, forecast improvements largely vanish: stepwise regressions
climate-augmented HMM specifications do not overlap with those of
rarely outperform AR(1), and climate-augmented models do not deliver
the corresponding benchmarks.6
systematic gains.
Table 3 reports RMSFE for the HMM specifications. Except for
live cattle, where the macro-based HMM marginally improves upon
4 Additional portfolio diagnostics, including mean returns, volatility, Sharpe
ratios, and downside for the benchmark and climate-augmented strategies, are
the benchmark, HMMs fail to outperform the AR(1) model in nearly
reported in Online Appendix B (Table 6).
all cases. Importantly, as before, augmenting the HMM with climate
5 These conclusions are robust to the inclusion of commodity-specific
variables does not lead to lower RMSFE relative to the macro-only
(e.g., basis, momentum, illiquidity, hedging intensity) and aggregate
specification. commodity factors. Detailed results are available upon request.
Climate-exposed commodities do not exhibit systematically better 6 In addition, the HMM with macro and climate factors yields p-values that
forecast accuracy than less exposed assets; rather, their forecast errors are in some cases close to conventional significance levels.
3

M. Guidolin and S. Ionta Economics Letters 265 (2026) 113028
Table 2
RMSFE — Stepwise regressions by volatility regimes.
Light Corn Soyb. Wheat Coffee Cocoa Sugar Cotton Gold Silver Plat. FOJ Lumber Cattle Avg CE Avg LCE
Low volatility
Kitchen Sink 0.1012 0.0750 0.0766 0.0925 0.1177 0.0841 0.0834 0.0766 0.0519 0.1719 0.0631 0.1118 0.0964 0.0537 0.0868 0.0970
Stepwise Macro (Backward) 0.0767 0.0729 0.0751 0.0818 0.0899 0.0706 0.0709 0.0709 0.0452 0.0818 0.0539 0.0854 0.0756 0.0497 0.0743 0.0644
Stepwise Macro (Forward) 0.0762 0.0730 0.0751 0.0818 0.0914 0.0706 0.0709 0.0688 0.0453 0.0803 0.0538 0.0756 0.0756 0.0493 0.0732 0.0639
Stepwise Macro + Climate (Backward) 0.0779 0.0731 0.0760 0.0814 0.0896 0.0708 0.0723 0.0717 0.0460 0.0835 0.0546 0.0862 0.0756 0.0500 0.0747 0.0655
Stepwise Macro + Climate (Forward) 0.0787 0.0724 0.0751 0.0820 0.0915 0.0708 0.0723 0.0694 0.0462 0.0821 0.0545 0.0853 0.0756 0.0497 0.0744 0.0654
High volatility
Kitchen Sink 0.1737 0.1624 0.1909 0.2907 0.2175 0.2531 0.2350 0.1502 0.1301 0.1853 0.2252 0.1403 0.1409 0.0840 0.1865 0.1786
Stepwise Macro (Backward) 0.1667 0.1600 0.1468 0.1347 0.0971 0.1434 0.1187 0.1080 0.0868 0.1506 0.1129 0.1125 0.0960 0.0436 0.1161 0.1293
Stepwise Macro (Forward) 0.1172 0.1555 0.1468 0.1323 0.0956 0.1444 0.1127 0.1029 0.0687 0.1242 0.1147 0.1088 0.0961 0.0424 0.1138 0.1062
Stepwise Macro + Climate (Backward) 0.1682 0.1546 0.1484 0.1749 0.0950 0.1458 0.1169 0.1081 0.0871 0.1534 0.1150 0.1146 0.0986 0.0465 0.1203 0.1309
Stepwise Macro + Climate (Forward) 0.1180 0.1523 0.1485 0.1395 0.0956 0.1469 0.1148 0.1033 0.0691 0.1248 0.1159 0.1156 0.1004 0.0429 0.1150 0.1070
AR(1) 0.0844 0.0869 0.0798 0.0948 0.0877 0.0784 0.0844 0.0809 0.0521 0.0961 0.0728 0.0915 0.0804 0.0465 0.0811 0.0764
The table reports RMSFE obtained for low- and high-volatility regimes. Boldfaced (underlined) entries indicate the lowest RMSFE within the low- (high-) volatility regime across stepwise
specifications. The low-volatility periods correspond to January 2004–December 2007 and January 2013–May 2018, while the high periods span January 2008–December 2012. The columns
‘‘Avg CE’’ and ‘‘Avg LCE’’ report the average RMSFE for climate-exposed (Corn, Soybeans, Wheat, Coffee, Cocoa, Sugar, Cotton, Frozen Orange Juice, Lumber, and Live Cattle) and less
climate-exposed commodities (Light Crude Oil, Gold, Silver, and Platinum), respectively.
Table 3
Root mean square forecast error — Hidden Markov models.
Light Corn Soyb. Wheat Coffee Cocoa Sugar Cotton Gold Silver Plat. FOJ Lumber Cattle Avg CE Avg LCE
HMM — Macro Factors 0.0911 0.0934 0.0870 0.1038 0.1441 0.0934 0.0959 0.0972 0.0960 0.1078 0.0848 0.0937 0.0867 0.0465 0.0942 0.0949
HMM — Macro and Climate Factors 0.1448 0.0928 0.0976 0.1035 0.1092 0.0965 0.0907 0.1022 0.0627 0.1104 0.0875 0.1015 0.0910 0.0480 0.0933 0.1014
AR(1) 0.0844 0.0869 0.0798 0.0948 0.0877 0.0784 0.0844 0.0809 0.0521 0.0961 0.0728 0.0915 0.0804 0.0465 0.0811 0.0764
The table reports RMSFE from a recursive pseudo out-of-sample exercise for HMM. Boldfaced entries indicate the lowest RMSFE for each commodity. The columns ‘‘Avg CE’’
and ‘‘Avg LCE’’ report the average RMSFE for climate-exposed (Corn, Soybeans, Wheat, Coffee, Cocoa, Sugar, Cotton, Frozen Orange Juice, Lumber, and Live Cattle) and less
climate-exposed commodities (Light Crude Oil, Gold, Silver, and Platinum), respectively.
The emerging divergence between statistical and economic per- Table 4
formance reflects a fundamental difference between statistical loss Economic value.
functions and economic evaluation criteria. Standard measures such 𝛾=2 𝛾=5 𝛾=10
as RMSFE assess forecast accuracy in terms of the conditional mean Panel A: No transaction costs
and penalize forecast errors symmetrically, without accounting for their HMM — Macro Factors 0.0023 0.0026 0.0041
implications for decision-making. By contrast, portfolio choice depends HMM — Macro and Climate Factors 0.0056 0.0068 0.0086
Stepwise Macro (Forward) −0.0071 −0.0099 −0.0190
on how predictive signals affect time-varying portfolio weights and the
Stepwise Macro and Climate (Forward) −0.0067 −0.0096 −0.0184
associated risk exposures, and therefore on the economic relevance— AR(1) Benchmark 0.0000 0.0000 0.0000
rather than the statistical magnitude—of forecast errors. Even modest Panel B: With transaction costs
improvements in predictive signals may have a limited impact on
HMM — Macro Factors 0.0025 0.0052 0.0053
average forecast accuracy, while still affecting the investor’s optimal HMM — Macro and Climate Factors 0.0079 0.0045 0.0128
allocation through changes in expected returns, higher-order moments, Stepwise Macro (Forward) −0.0031 −0.0052 −0.0153
or the covariance structure of returns. As a result, relatively small or
S
A
t
R
e
(
p
1
w
)
is
B
e
e n
M
c
a
h
c
m
ro
a r
a
k
nd Climate (Forward) −
0.
0
0
.
0
0
0
0
0
09 −
0.
0
0
.
0
0
0
0
0
14 −
0.
0
0
.
0
0
0
0
0
90
noisy signals can generate economically meaningful gains if they help
The table reports annualized CERs relative to an AR(1) benchmark for different levels
investors adjust portfolio tilts or manage risk exposures more effectively
of relative risk aversion. Panel A reports results without transaction costs, while Panel
over time. B accounts for proportional costs. Boldfaced entries indicate the highest 𝛥𝐶𝐸𝑅 for each
A formal quantitative bridge between these two perspectives is level of risk aversion.
provided by Campbell and Thompson (2008), who show that, for a
mean–variance investor, even an out-of-sample 𝑅2 as small as 0.5%
at a monthly horizon is sufficient to generate economically meaning-
4. Robustness
ful improvements in portfolio performance. The intuition is that the
We test the robustness of results to alternative constructions of
achievable gain in certainty-equivalent return scales with the signal-to-
climate-based predictors, with detailed results in online Appendix C.
noise ratio of the predictive model rather than with its contribution to
While recursive and orthogonalized climate factors do not improve
average squared forecast error. Our results are broadly consistent with
forecast accuracy, the HMM with orthogonalized macro-climate factors
this logic: the climate-augmented HMM delivers annualized 𝛥CER in
delivers higher certainty equivalent returns than the macro-only model.
the range of 56–86 basis points (Panel A of Table 4) despite near-zero
or negative out-of-sample 𝑅2 values across most commodities.7 5. Conclusion
We study the role of climate in forecasting commodity futures
returns and in generating economic value. Climate predictors fail to
7 The magnitude of these gains appears to exceed what a linear 𝑅2-to-
Sharpe mapping would imply under the Campbell and Thompson (2008)
materially improve short-horizon prediction accuracy relative to bench-
framework, pointing to the regime-switching structure as an additional source
marks. However, when incorporated into portfolio choice, climate in-
of economic value: climate signals that carry limited information about the formation delivers economically significant gains, consistent with prior
unconditional mean forecast error can nonetheless shift optimal portfolio evidence that economic value need not coincide with improvements
weights across latent states, reducing exposure in adverse regimes and raising in statistical accuracy. These findings suggest that climate risk affects
it when expected returns are more favorable. optimal portfolios rather than short-horizon predictability, highlighting
4

M. Guidolin and S. Ionta
Economics Letters 265 (2026) 113028
Table 5
Climate variables: Definition and data sources.
|  Variable |     | Climate phenomenon |     |     | Sample Data source |     |     |     |
| --------- | --- | ------------------ | --- | --- | ------------------ | --- | --- | --- |
 Pacific North American (PNA) Atmospheric circulation over the North Pacific and North  NOAA Climate Prediction Center
1989–2018
America
 Arctic Oscillation (AO) Strength of the polar vortex (Northern Hemisphere) 1989–2018 NOAA Climate Prediction Center
 North Atlantic Oscillation (NAO) Sea-level pressure gradient over the North Atlantic NOAA Climate Prediction Center
1989–2018
 Scandinavian Pattern (SCA) Geopotential height anomalies over Scandinavia and  1989–2018 NOAA Climate Prediction Center
Europe
 Pacific Decadal Oscillation (PDO) Low-frequency North Pacific sea surface temperature  NOAA National Centers for Environmental
1989–2018
|     |     | variability |     |     | Information |     |     |     |
| --- | --- | ----------- | --- | --- | ----------- | --- | --- | --- |
 Atlantic Multidecadal Oscillation (AMO) Multidecadal North Atlantic sea surface temperature  1989–2018 NOAA Physical Sciences Laboratory
anomalies
 Multivariate ENSO Index (MEI) Coupled ocean–atmosphere ENSO indicator NOAA Physical Sciences Laboratory
1989–2018
 Dipole Mode Index (DMI) Indian Ocean Dipole sea surface temperature gradient 1989–2018 NOAA Physical Sciences Laboratory
 Madden–Julian Oscillation (MJO, phase 1) Intra-seasonal tropical convection pattern 1989–2018 World Meteorological Organization
 Quasi-Biennial Oscillation (QBO proxy) Stratospheric circulation variability (temperature-based  NOAA Physical Sciences Laboratory
1989–2018
proxy)
 Palmer Drought Severity Index (global, 36 m  Global drought conditions (soil moisture balance) 1989–2018 National Center for Atmospheric Research
MA)
 Northern Hemisphere Snow Cover Anomaly Cryosphere variability (snow extent deviations) NOAA National Centers for Environmental
1989–2018
Information
 Global Temperature Anomaly (detrended) Global surface temperature anomalies (land and ocean) 1989–2018 NOAA Physical Sciences Laboratory
All variables are observed at monthly frequency and standardized prior to analysis. The Palmer Drought Severity Index is averaged globally and smoothed using a 36-month
moving average. Global temperature anomalies are spatially averaged and detrended to remove the deterministic warming component.
Table 6
Portfolio diagnostics.
|     |     | 𝛾=2 |     | 𝛾=5 | 𝛾=10 |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- |
  Mean Vol Sharpe Downside Mean Vol Sharpe Downside Mean Vol Sharpe Downside
 Panel A: No transaction costs
 HMM — Macro Factors 0.0159 0.0851 0.1755 0.0590 0.0159 0.0851 0.1755 0.0590 0.0159 0.0851 0.1759 0.0590
|  HMM — Macro and Climate Factors |     |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
0.0183 0.0775 0.2239 0.0518 0.0183 0.0775 0.2237 0.0518 0.0183 0.0775 0.2236 0.0518
|  Stepwise Macro (Forward) |     |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
0.0080 0.0915 0.0766 0.0680 0.0080 0.0915 0.0766 0.0680 0.0080 0.0915 0.0765 0.0680
 Stepwise Macro and Climate (Forward) 0.0085 0.0915 0.0824 0.0678 0.0085 0.0915 0.0824 0.0678 0.0085 0.0915 0.0824 0.0678
 AR(1) Benchmark 0.0137 0.0844 0.1509 0.0595 0.0137 0.0844 0.1509 0.0595 0.0137 0.0844 0.1509 0.0595
 Panel B: With transaction costs
|  HMM – Macro Factors |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
0.0140 0.0809 0.1617 0.0567 0.0161 0.0802 0.1882 0.0550 0.0135 0.0772 0.1629 0.0540
 HMM – Macro and Climate Factors 0.0181 0.0711 0.2413 0.0470 0.0150 0.0758 0.1849 0.0520 0.0168 0.0688 0.2303 0.0455
 Stepwise Macro (Forward) 0.0099 0.0882 0.1013 0.0645 0.0110 0.0885 0.1137 0.0642 0.0081 0.0807 0.0878 0.0595
|  Stepwise Macro and Climate (Forward) |     |     |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
0.0119 0.0867 0.1265 0.0620 0.0147 0.0880 0.1557 0.0619 0.0133 0.0808 0.1529 0.0568
|  AR(1) Benchmark |     |     |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
0.0115 0.0794 0.1323 0.0567 0.0115 0.0798 0.1317 0.0570 0.0112 0.0784 0.1306 0.0562
The table reports standard portfolio diagnostics for the main strategies, including mean returns, volatility, Sharpe ratios, and downside risk. Panel A reports
results without transaction costs, while Panel B accounts for costs.
Table 7
Statistical inference on economic value: Parametric bootstrap.
|     |     | 𝛾=2  |        | 𝛾=5    | 𝛾=10 |        |     |     |
| --- | --- | ---- | ------ | ------ | ---- | ------ | --- | --- |
|     |     |      | 95% CI | 95% CI |      | 95% CI |     |     |
|     |     | 𝛥CER |        | 𝛥CER   | 𝛥CER |        |     |     |
 Panel A: No transaction costs
 HMM — Macro +0.0023 [−0.1234,+0.1712] +0.0026 [−0.1374,+0.1814] +0.0041 [−0.1859,+0.2233]
 HMM — Macro & Climate +0.0056 [−0.0747,+0.2119] +0.0068 [−0.0662,+0.2463] +0.0086 [−0.0861,+0.3314]
 Stepwise Macro (Fwd) −0.0071 [−0.2454,+0.0671] −0.0099 [−0.2864,+0.0622] −0.0190 [−0.4427,+0.0957]
|     |  Stepwise Macro & Climate (Fwd) |         |                   |                           |         | [−0.3923,+0.0953]  |     |     |
| --- | ------------------------------- | ------- | ----------------- | ------------------------- | ------- | ------------------ | --- | --- |
|     |                                 | −0.0067 | [−0.2380,+0.0774] | −0.0096 [−0.2875,+0.0744] | −0.0184 |                    |     |     |
 Panel B: With transaction costs
 HMM — Macro +0.0025 [−0.1089,+0.1658] +0.0052 [−0.0999,+0.2004] +0.0053 [−0.1955,+0.2357]
 HMM — Macro & Climate +0.0079 [−0.0373,+0.2265] +0.0045 [−0.0878,+0.2084] +0.0128 [−0.0318,+0.3343]
|     |  Stepwise Macro (Fwd)           |         |                   |                           |         | [−0.3034,+0.1448]  |     |     |
| --- | ------------------------------- | ------- | ----------------- | ------------------------- | ------- | ------------------ | --- | --- |
|     |                                 | −0.0031 | [−0.1903,+0.1062] | −0.0052 [−0.2210,+0.1091] | −0.0153 |                    |     |     |
|     |  Stepwise Macro & Climate (Fwd) |         |                   |                           |         | [−0.1968,+0.1969]  |     |     |
|     |                                 | −0.0009 | [−0.1577,+0.1387] | −0.0014 [−0.1909,+0.1686] | −0.0090 |                    |     |     |
The table reports annualized 𝛥CER relative to the AR(1) benchmark and 95% bootstrap confidence intervals based on a parametric bootstrap
with 𝐵=10,000 simulations. The DGP is AR(0)–GJR-GARCH(1,1), calibrated separately for each specification.
the importance of complementing statistical forecast evaluation with  Appendix B. Portfolio diagnostics
economic loss function-driven analyses.
See Table  6.
| Appendix A. Climate variables |     |     |     | Appendix C. Supplementary data |     |     |     |     |
| ----------------------------- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- |
Supplementary material related to this article can be found online
See Table  5. at https://doi.org/10.1016/j.econlet.2026.113028.
5

M. Guidolin and S. Ionta Economics Letters 265 (2026) 113028
Data availability Dal Pra, Giulia, Guidolin, Massimo, Pedio, Manuela, Vasile, Fabiola, 2018. Regime shifts
in excess stock return predictability: an out-of-sample portfolio analysis. J. Portf.
Data will be made available on request. Manag. 44 (3), 10.
De Roon, Frans A., Nijman, Theo E., Veld, Chris, 2000. Hedging pressure effects in
futures markets. J. Financ. 55 (3), 1437–1456.
DeMiguel, Victor, Garlappi, Lorenzo, Uppal, Raman, 2009. Optimal versus naive
References
diversification: How inefficient is the 1/N portfolio strategy? Rev. Financ. Stud.
22 (5), 1915–1953.
Ang, Andrew, Timmermann, Allan, 2012. Regime changes and financial markets. Annu. Gorton, Gary, Rouwenhorst, K. Geert, 2006. Facts and fantasies about commodity
Rev. Financ. Econ. 4 (1), 313–337. futures. Financ. Anal. J. 62 (2), 47–68.
Campbell, John Y., Thompson, Samuel B., 2008. Predicting excess stock returns out Heino, Matias, Puma, Michael J, Ward, Philip J, Gerten, Dieter, Heck, Vera, Siebert, Ste-
of sample: Can anything beat the historical average? Rev. Financ. Stud. 21 (4), fan, Kummu, Matti, 2018. Two-thirds of global cropland area impacted by climate
1509–1531. oscillations. Nat. Commun. 9 (1), 1257.
Cashin, Paul, Mohaddes, Kamiar, Raissi, Mehdi, 2017. Fair weather or foul? The Kruttli, Mathias S., Roth Tran, Brigitte, Watugala, Sumudu W., 2025. Pricing poseidon:
macroeconomic effects of El Niño. J. Int. Econ. 106, 37–54. extreme weather uncertainty and firm return dynamics. J. Financ. 80 (2), 783–832.
Cederburg, Scott, Johnson, Travis L., O’Doherty, Michael S., 2023. On the economic Ludvigson, Sydney C., Ng, Serena, 2009. Macro factors in bond risk premia. Rev. Financ.
significance of stock return predictability. Rev. Financ. 27 (2), 619–657. Stud. 22 (12), 5027–5067.
Cenesizoglu, Tolga, Timmermann, Allan, 2012. Do return prediction models add Tedeschi, Marco, Foglia, Matteo, Bouri, Elie, Dai, Peng-Fei, 2024. How does climate
economic value? J. Bank. Financ. 36 (11), 2974–2987. policy uncertainty affect financial markets? Evidence from europe. Econom. Lett.
Choi, Darwin, Gao, Zhenyu, Jiang, Wenxi, 2020. Attention to global warming. Rev. 234, 111443.
Financ. Stud. 33 (3), 1112–1145. Yang, Hao, Yang, Jie, Feng, Yun, 2026. Climate physical risks and the vulnerability of
global agricultural commodities. Econom. Lett. 258, 112748.
6