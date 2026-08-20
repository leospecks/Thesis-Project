Annals of Operations Research (2021) 299:1317–1356
https://doi.org/10.1007/s10479-020-03515-w
S.I.: RECENT DEVELOPMENTS IN FINANCIAL MODELING AND RISK
MANAGEMENT
Forecasting commodity futures returns with stepwise
regressions: Do commodity‑specific factors help?
Massimo Guidolin1 · Manuela Pedio1
Published online: 6 February 2020
© Springer Science+Business Media, LLC, part of Springer Nature 2020
Abstract
The aim of this paper is to assess whether three well-known commodity-specific variables
(basis, hedging pressure, and momentum) may improve the predictive power for commod-
ity futures returns of models otherwise based on macroeconomic factors. We compute
recursive, out-of-sample forecasts for the monthly returns of fifteen commodity futures,
when estimation is based on a stepwise model selection approach under a probability-
weighted regime-switching regression that identifies different volatility regimes. We sys-
tematically compare these forecasts with those produced by a simple AR(1) model that
we use as a benchmark and we find that the inclusion of commodity-specific factors does
not improve the forecasting power. We perform a back-testing exercise of a mean–vari-
ance investment strategy that exploits any predictability of the conditional risk premium
of commodities, stocks, and bond returns, also consider transaction costs caused by port-
folio rebalancing. The risk-adjusted performance of this strategy does not allow us to con-
clude that any forecasting approach outperforms the others. However, there is evidence that
investment strategies based on commodity-specific predictors outperform the remaining
strategies in the high-volatility state.
Keywords Stepwise regression · Commodity returns · Predictability · Portfolio back-
testing
1 Introduction
Recently, in the academic literature a debate has raged on the role played and the alleged
distortions induced by speculative investors in commodity markets. For instance, Tang
and Xiong (2012) have reported a surge from $15 to $200 billion of capital flows in
commodity futures markets from institutional investors between 2003 and 2008. Irwin
and Sanders (2011), Tang and Xiong (2012), and Hamilton and Wu (2015) have traced
*
Manuela Pedio
Manuela.pedio@unibocconi.it
1 Finance Department, Bocconi University and Baffi-CAREFIN Centre, via Roetgen 1, 20136 Milan,
Italy
1 3
Vol.:(0123456789)

1318 Annals of Operations Research (2021) 299:1317–1356
the start of the process of financialization of commodity markets back to 2004. Follow-
ing this increasing interest in commodities as an asset class, a literature has emerged
that investigates the risk sources driving commodity futures returns. In this paper we
formally test—both using standard statistical criteria and resorting to economically
grounded loss functions—whether variables that describe the dynamics and state of
(dis-)equilibrium in the very commodity markets are needed to model and forecast com-
modity returns or this information is already captured by traditional macroeconomic
variables (as conjectured, for instance, by Bessembinder and Chan 1992).
Our paper builds on two different strands in the literature on commodities. The first
strand argues that the expected return of any given commodity futures is driven by fac-
tors that are specific to each market. This group of papers is based on two main classical
theories, which posit that the level of inventories and the relative positions of short ver-
sus long hedgers in the futures markets (hedging pressure) are the key determinants of
futures returns. First, the theory of storage (Kaldor 1939; Brennan 1958) hypothesizes
that producers and inventory holders receive implicit benefits from inventories deriv-
ing from the possibility to manage any temporary shortages (the “convenience yield”).
However, due to the presence of costs of carrying such inventories, these benefits
decline as inventories increase. Given that the level of inventories plays a role in deter-
mining the relative movements of spot and futures prices, the convenience yield turns
out to be related to the basis, i.e., the difference between spot and futures prices. Sec-
ond, the theory of normal backwardation in Keynes (1930) and Hicks (1939) is based
on the intuition that, to induce risk-averse speculators to take long positions, current
futures prices must be set at a discount versus expected future spot prices at maturity,
i.e., in ordinary times, the market would be in backwardation. The size of the discount
is the future risk premium and it depends on the interplay between hedgers and specula-
tors. Many papers have provided empirical evidence on the forecasting power of com-
modity-specific factors related to these classical theories (basis and hedging pressure,
besides momentum that may be associated to speculative herding behavior). For exam-
ple, Gorton et al. (2012), exploiting the Theory of Storage, identify a linkage between
the basis and individual commodity futures returns. Building on the theory of hedging
pressure, Stoll (1979), Hirshleifer (1988) and de Roon et al. (2000) found that hedging
pressure affects individual commodity futures premiums.
A second strand of literature has tested the relationship between macroeconomic vari-
ables and commodities. These papers are mainly based on the assumption that storage costs
and convenience yields are expected to be influenced by the general state of the economy
through short-term mismatches between the demand and supply of commodities (see e.g.,
Bessembinder and Chan 1992). However, only a small portion of the literature studies the
predictive power of macroeconomic variables that have been proven to carry a relation
with commodity futures returns. For instance, Gargano and Timmermann (2014) examine
the predictability of commodity returns from some macroeconomic variables and find that
bond spreads, the growth rate of money supply, and industrial production are better predic-
tors for raw industrials and metals index returns, than for foods and textiles commodities.
They also observe that the predictability of commodity futures returns based on inflation,
industrial production, and money supply is stronger during economic recessions than dur-
ing expansions. Giampietro et al. (2018) test whether flexible specifications of pricing ker-
nels that jointly price the cross-section of commodities, equities, and government bonds
reflect standard macroeconomic variables or, alternatively, the stochastic discount factor
should include commodity-specific variables as well; they find evidence that commodity
market information would be required.
1 3

Annals of Operations Research (2021) 299:1317–1356 1319
With these two competing strands of literatures in mind, in this paper we investigate
whether models extended to include three commonly used aggregate commodity-specific
factors (i.e., basis, hedging pressure, and momentum) display stronger predictive power
than models based on the lagged values of 128 macroeconomic-based factors, as in Lud-
vigson and Ng (2009) and Welch and Goyal (2008). Our question is of considerable impor-
tance to both practitioners (arguably, investors, including both hedgers and speculators)
and academics: a rejection of the null hypothesis that commodity returns can be forecast
by a restricted model that only contains macroeconomic factors would represent robust
evidence in favor of the segmentation of commodities from the rest of the asset classes.
Indeed, if accurate and economically valuable predictions could be derived only from an
extended model that includes the information in commodity-specific variables, this would
confirm that commodities constitute a source of diversification to a portfolio manager, as
they would offer exposures to factors that are specific to this asset class.
We conduct our analysis on 15 commodity futures series, i.e., Brent Crude Oil, Gaso-
line, Corn, Soybeans, Wheat, Coffee, Cocoa, Sugar, Cotton, Gold, Silver, Platinum, Orange
Juice, Lumber, and Live Cattle. We examine the sample period January 1989–December
2012. As You and Daigler (2013), we focus on individual futures contracts. To assess out-
of-sample (henceforth, OOS) predictability, we split our data and use information for the
period January 1989–December 2003 for in-sample estimation of the models, and data
for the period January 2004–December 2012 to test the recursive OOS forecasting per-
formance of a range of alternative models. In addition, we consider different regimes of
market volatility (proxied by either the VIX or by the variance of the unexplained returns
from the very predictive models) and investigate whether the predictive power of differ-
ent models may depend on such regimes. To test the conjecture of a strong dependence,
we split both the in-sample and OOS windows in high- and low-volatility periods (differ-
ently from Jensen et al. 2000, who have instead emphasized monetary policy regimes).
To reduce the number of macroeconomic variables that need to be considered, we adopt
a principal components analysis, as suggested by Stock and Watson (2006): we therefore
identify ten linearly uncorrelated variables, which effectively summarize 60% of the vari-
ance of the initial information set. In addition, to decide whether all these ten variables that
we have constructed should be actually included in predictive regression for the returns
of each of the commodities, we exploit the flexibility offered by forward and backward
stepwise regressions, a tool that allows some (or all) of the variables to be chosen auto-
matically, using various statistical criteria (see, e.g., Sharma and Yu 2015). This approach
allows us to obtain the “best” subset of variables for each commodity series, thus avoiding
statistically irrelevant predictors, which would just add noise to the forecasting exercises,
uselessly reducing the degrees of freedom. Because our main goal is to assess whether
commodity-specific variables improve the OOS predictive ability of such flexible, macro-
based models, we also estimate predictive regressions where these factors are added to the
models previously specified. We compare OOS forecasts from a model based on the princi-
pal components of macroeconomic variables only versus forecasts produced using also the
commodity-specific factors. To evaluate the forecasting accuracy of the alternative models,
we adopt two measures: the mean absolute error (MAE) and the root mean square forecast
error (RMSFE). Both criteria lead to the conclusion that neither the models that include
only macroeconomic variables nor the extended models that contain also commodity-spe-
cific factors yield better OOS performances than a simple, naïve first-order autoregressive
benchmark.
Finally, we turn to the assessment of the economic value of alternative predictions (i.e.,
those based on macroeconomic variables only versus those that include commodity-specific
1 3

1320 Annals of Operations Research (2021) 299:1317–1356
factor as well) using a mean–variance framework (similar to Jensen et al. 2000; Erb and
Harvey 2006; Fuertes et al. 2010), in which the asset menu includes both commodities
and traditional assets (equities and bonds). Although such a OOS portfolio back-testing
may seem not justified by the in-sample and statistical OOS results, a recent literature in
portfolio management (see, e.g., Dal Pra et al. 2018) has shown that—because the typical
loss functions employed are deeply different—it is possible for statistical back-testing to
reveal a distorted, downward-biased picture of the amount of economic value that instead
a OOS portfolio back-test may disclose. In fact, our results suggest that portfolios resulting
from the joint use of macroeconomic and commodity-specific factors perform better (in the
case of models built by forward selection) than models driven by macroeconomic variables
only also when transaction costs are considered. However, this result appears to be reversed
when regressions are built using backward selection stepwise methods. Interestingly, the
asset allocations are dominated by long exposures to bonds and the residual is structured
as a long/short strategy with an almost perfect zero net exposure to commodities and equi-
ties. This empirical result is in line with a recent literature that has showed that, even going
beyond standard mean–variance analysis, it may be difficult to obtain evidence in favour of
multi-asset portfolios including long positions in individual commodities (see, e.g., Hen-
riksen et al. 2019; Lean et al. 2018). Finally, it is interesting to notice that when these
analyses are performed separately with reference to low- versus high-volatility regimes,
we find that in the high-volatility regime models that include commodity-specific factors
imply more accurate forecasts, higher realized Sharpe ratios, and higher mean–variance
realized utility values than the low-volatility regime portfolios. These results appear novel:
You and Daigler (2013) have examined the diversification benefits of using individual
futures contracts in a Markowitz framework and investigated the differences between ex-
ante, in-sample results and ex-post, realized performances. However, our focus is distinc-
tively devoted to the differential predictability of commodity-specific versus variables that
capture the state of the business cycle.
The rest of the paper is organized as follows: Sect. 2 describes the methodology. Sec-
tion 3 contains a description of the data. Section 4 reports the results of the estimation of
the models and their OOS performances. Section 5 reports the back-testing results from the
mean–variance exercises. Section 6 concludes.
2 Research design
2.1 Definition of volatility regimes
It is nowadays well-known in the literature that different regimes of market volatility
should be featured in factor models, based on the evidence that financial markets may
change dramatically (see, e.g., Rapach and Zhou 2013). Portfolio managers, risk arbitra-
geurs, and corporate treasurers closely monitor volatility trends, because changes in prices
could have a major impact on their investment and risk management decisions. We adopt
the VIX index provided by the Chicago Board Options Exchange (CBOE) from January
1989 to December 2012 as a proxy of market volatility. Given that the VIX index is char-
acterized by the presence of different states (or regimes), we introduce a regime switching
framework in order to disentangle the different levels of market volatility. In particular, we
1 3

Annals of Operations Research (2021) 299:1317–1356  1321
Fig. 1  VIX index series and estimated filtered probability of being in the low-volatility state
adopt the following two-state regime switching model to feature the existence of a high-
volatility and a low-volatility state1:
|     |     | VIX | =c +𝜙VIX |     | +𝜀, |     |     |     |
| --- | --- | --- | -------- | --- | --- | --- | --- | --- |
|     |     |     | t s      | t−1 | t   |     |     | (1) |
t
∼N 0,σ2
with ε  . The variable s t is a Markov state variable, so that the mean, c, of the
t
VIX process  takes  different values (say, c high and c low) in the two different regimes and the
( )
transition between the two regimes is governed by a Markov process:
|     | P s =0 | s   | =0 P s | =1 s | =0  | p    | p    |     |
| --- | ------ | --- | ------ | ---- | --- | ---- | ---- | --- |
| P=  | t      | t−1 | t      | t−1  |     | = 00 | 10 , |     |
|     | P s =0 | s   | =1 P s | =1 s | =1  | p    | p    | (2) |
|     | t      | t−1 | t      | t−1  |     | 01   | 11   |     |
|     | [ (    |     | ) (    |      | )]  | [    | ]    |     |
|     |        | |   |        | |    |     |      |      |     |
|     | (      |     | ) (    |      | =)  |      |      |     |
where p ij (i, j = 0,1) den otes the  transitio n p robabil ity of s j , given s t−1 =i and the transi-
|     |     | |   |     | |   | t   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
tion probabilities satisfy p +p =1  . The transition matrix governing the behaviour of the
i0 i1
state variable, contains only two parameters p  and p
. Hence, we assume that the vari-
|     |     |     |     | 00  | 11  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
able s t is not directly observable, but that it can be inferred from the past behaviour of VIX t.
Figure 1 plots the estimated filtered probabilities that the VIX was in a low-volatility
regime (clearly the plot for high-volatility state is just specular). From an inspection of the
figure, it seems that the entire sample period could be divided into four different sub-peri-
ods. In particular, January 1989-December 1997 and January 2004-December 2007 can
be considered as low-volatility periods, while January 1998–December 2003 and January
2008-December 2012, as high-volatility periods.
1 Jensen et al. (2000) provide evidence on the role of commodity futures in mean–variance portfolios. They
find that in periods of restrictive monetary policy, commodity futures carry an important weight and yield
a considerable performance enhancement. However, since their paper, it has become common to classify
financial market regimes on the basis of the level of volatility.
1 3

1322 Annals of Operations Research (2021) 299:1317–1356
2.2 Forecasting with many macroeconomic predictors: principal components
Stock and Watson (2006) surveyed the literature concerning methods to forecast eco-
nomic time series variables using many predictors. Among all the methodological solu-
tions analysed, the authors showed that forecasts based on principal components of a
large number of predictors are first-order asymptotically efficient given that both the
number of predictors and the number of observations are very large, and this is par-
ticularly true when we consider a large set of macroeconomic variables (Stock and
Watson 2002). The core idea of principal component analysis (PCA) is to identify a
limited number of linearly uncorrelated variables, the so-called principal components
(PCs), which summarize the largest part of the variation of a sample set of potentially
correlated variables. The PCA approach is based on a well-known result, the singular
value decomposition theorem, that states that any symmetric matrix, and therefore also
a variance–covariance matrix Σ , can be decomposed through the symmetric eigenvalue
decomposition as
Σ=U ΛU�,
(3)
where U is a square n × n matrix whose ith column is the eigenvector u i of Σ and Λ is
a diagonal matrix whose diagonal elements are the corresponding eigenvalues, Λ ii =𝜆 i .
Notably, U is an orthogonal matrix, so that UU� =U�U =I n . After obtaining the decompo-
sition of the variance–covariance matrix of our n starting variables, we compute the princi-
pal components:
n
PC = u y,
k ki i (4)
i=1
∑
where y 1 , y 2 , …, y n represent the vectors of the original variables (in our case the 128
macro-based factors that we will describe in details in Sect. 3) and u k is the kth eigenvector
of Σ and u k1 ,u k2 ,…,u kn are its n elements.
Using principal component analysis to summarize a large set of macroeconomic fac-
tors, we estimate the following model for the returns of each commodity j, R t+1,j:
N K
R =𝛼 + 𝛽 PC +D 𝛾 C +𝜀 ,
t+1,j j ij t,ij t,j kj t,kj t,j (5)
i=1 (k=1 )
∑ ∑
where 𝛼 j is the model’s intercept, 𝛽 ij is the factor loading of the ith principal component for
commodity j, 𝛾 kj represents the regression coefficients of the kth commodity-specific factor
C t,kj , and D t,j is a dummy variable, which is equal to 1 when the model also contains com-
modity-specific factors, and 0 otherwise. 𝜀 t,j represents the error term, assumed to be white
noise and such that Corr 𝜀 j ,𝜀 i =0 , for all pairs i and j. Figure 2 reports the graph of the
cumulative variance explained by principal components. To reduce the number of param-
( )
eters to be estimated, we decided to include only the first ten components resulting from
the PCA performed, which explain 60% of the total variance of the initial informational
set (the dotted line in the Fig. 2 represents the tenth principal component). In addition,
Table 1 provides a representation of the scale of the factor loadings. They range from − 1 to
1; loadings close to − 1 or 1 indicate that the factor is strongly correlated with the variable,
while loadings close to zero indicate that the link is weak.
1 3

Annals of Operations Research (2021) 299:1317–1356 1323
Fig. 2 Cumulative proportion of explained variance by principal components
2.3 Variables selection method: stepwise regressions
Starting from the set of principal components computed previously, we apply a vari-
able selection methodology to decide the variables to be included as regressors to esti-
mate futures returns of each commodity in the sample. To this purpose we rely on step-
wise regression, an automatic variable selection procedure, which chooses from a set of
candidates the explanatory variables that are, jointly, the most relevant. Different stepwise
regression procedures are available, but we decided to use the unidirectional forward and
backward methods. Forward selection starts with no variables in the model, testing the
inclusion of each variable with a chosen model-fit criterion, adding the variable (if any)
whose inclusion gives the most statistically significant improvement of the fit, and repeat-
ing this process until none of the remaining variables improves the model to a statistically
significant extent. Backward elimination starts with all candidate variables, testing the
deletion of each variable using a chosen model-fit criterion, deleting the variable (if any)
whose exclusion gives the least statistically significant deterioration of the model fit, and
repeating this process until no further variables can be deleted without a statistically sig-
nificant loss of fit.
Stepwise regression procedures admit different selection criteria for variables to be
included or excluded from the models; for instance, it may rely on a sequence of F-tests or
on an information criterion, which is a measure that trades-off in-sample fit with parsimony
of the model, such as the Akaike information criterion (henceforth, AIC). In line with the
recent literature, we adopt the AIC as a selection criterion,
AIC=2k−2ln L̂
, where
L̂
is
the maximum value of the likelihood function of the model and k is the number of param-
( )
eters to be estimated. Given a set of models, the preferred one is that with the smallest AIC
value.2
2 Yamashita et al. (2007) compare the stepwise AIC selection method with other stepwise methods for vari-
able selection and show that this practical criterion leads to the same results as partial F tests.
1 3

1324 Annals of Operations Research (2021) 299:1317–1356
Table 1 Principal components factor loadings
1 3

Annals of Operations Research (2021) 299:1317–1356 1325
Table 1 (continued)
In total, we estimated four different models for each commodity using backward proce-
dures and four using forward procedures: a model that regresses futures returns on the prin-
cipal components only (potentially a subset of the initial set, according to the selection pro-
cedure) in periods of low volatility and in periods of high volatility; a model that regresses
futures returns on principal components and on commodity-specific factors, both in time
of high and low volatility.3 We then compute OSS forecasts for models that include and
exclude commodity-specific factors using the weighted average of low-volatility and high-
volatility estimates, where weights are represented by the filtered probabilities obtained
from the application of the Markov switching (MS) model described earlier.
3 The data
3.1 Commodity futures returns
We consider time series of monthly returns computed using settlement prices of futures
contracts on 15 commodities, collected from Thomson Reuters Datastream, for a period
spanning from January 1989 to December 2012. The dataset contains two energy commod-
ities (Brent Crude Oil and Gasoline), seven agricultural commodities (Corn, Soybeans,
3 As a robustness check, instead of running two separate regressions according to a classification of the
regime based on the state of the VIX, we also estimate Markov-switching predictive regressions. The results
are discussed in detail in Sects. 4.3 and 5.2.
1 3

1326 Annals of Operations Research (2021) 299:1317–1356
Wheat, Coffee C, Cocoa, Sugar No. 11, and Cotton No. 2), three metals commodities
(Gold 100 Oz, Silver 5000 Oz, and Platinum), two general commodities (Orange Juice and
Lumber), and one livestock commodity (Live Cattle).4
Following a common practice of both practitioners and academics, we consider inves-
tors to take fully collateralised positions in commodity futures. This implies two conse-
quences. First, investors are not allowed to operate on margin, thus using leverage; while
this approach limits the size of the return that could be reached, it has the advantage to
make investments in commodities directly comparable with the investments in other asset
classes, which usually require an initial money outflow. Second, the lack of a margin sys-
tem limits the possibility of any unintentional liquidation (due to insufficient collateral) of
the position before the end of the investor’s holding period.
We compute the return on a future position on commodity j at time t as:
F(1)
R = j,t+1 −1+Rf,
j,t+1 F(1) t (6)
j,t
where
Rf
t is the risk-free rate between time t and t + 1, here proxied by the 1-month T-bill
rate. Naturally, the computation of the time series of futures returns is complicated by the
fact that the front-end contract (typically the most liquid and used by the traders) has to be
rolled over before expiry in order to maintain a long-term position (while at the same time
avoiding taking a delivery). In case of physically settled contracts, to avoid the delivery,
traders shall close their position before the “First Notice Day”, which is the first day from
which the exchange may assign the delivery of the underlying asset, before the “Last Trad-
ing Day”. In order to identify the First Notice Day for each contract, we have considered
the official trading calendar of the relevant exchange. In addition, to forecast when actually
(before the First Notice Day) the majority of the investors are likely to roll over their posi-
tions, we adopted a methodology proposed by Bakshi, et al. (2019) and widely consistent
with the intuition of Gorton et al. (2012) and Hong and Yogo (2012). Because the investor
wants to avoid delivery, we consider that she takes position in the futures contract with the
second closest maturity on the last business day of each month t, when the contract’s First
Notice Day occurs after the end of month t + 1.
In Table 2 we report the summary statistics of the commodity futures returns. We notice
that the commodities in the sample have similar volatility, except for Corn, Cotton, Live
Cattle, Gold 100 Oz, and Soybeans. Query ID="Q2" Text="Please check the layout of
Table(s) 4, 5, 7, 8, 9, and correct if necessary." We also find that the time series of com-
modities futures returns have platykurtic tails (kurtosis lower than 3) and positive skew-
ness, except for Corn, Live Cattle and Soybeans, which display a negative skewness. We
also notice that Brent Crude Oil and Gasoline have a higher average return during the sam-
ple period than the other commodities.
3.2 Macroeconomic‑based factors
Since we want to represent broad categories of economic activity, we consider the 125
macroeconomic-based factors by Ludvigson and Ng (2009), adding some series by Welch
and Goyal (2008). We obtain a set of 139 variables, spanning from January 1989 to
4 As recently shown by Aslan et al. (2018), with reference to commodity returns, it may be possible to
group different commodity returns series on the basis of commonalities in the estimated linear autoregres-
sive and non-linear threshold autoregressive features to further reduce the dimension of the cross-section.
1 3

Annals of Operations Research (2021) 299:1317–1356  1327
Table 2  Summary statistics for
|     | Variable | Mean Median | SD Skewness | Kurtosis |
| --- | -------- | ----------- | ----------- | -------- |
commodity futures returns
|     | Brent crude oil | 0.015 0.014     | 0.095 0.516   | 3.568 |
| --- | --------------- | --------------- | ------------- | ----- |
|     | Corn            | − 0.003 − 0.007 | 0.074 − 0.098 | 0.499 |
|     | Lumber          | − 0.006 − 0.008 | 0.095 0.575   | 1.684 |
|     | Live Cattle     | 0.002 0.001     | 0.039 − 0.481 | 2.720 |
|     | Soybeans        | 0.004 0.000     | 0.067 − 0.083 | 0.952 |
|     | Wheat           | − 0.005 − 0.007 | 0.081 0.499   | 2.097 |
|     | Cocoa           | − 0.002 − 0.010 | 0.086 0.580   | 1.127 |
|     | Cotton No. 2    | 0.000 − 0.004   | 0.076 0.375   | 0.863 |
|     | Gold 100 Oz     | 0.003 − 0.003   | 0.045 0.204   | 1.481 |
|     | Gasoline        | 0.016 0.015     | 0.099 0.414   | 2.563 |
|     | Orange Juice    | − 0.002 − 0.008 | 0.088 0.621   | 1.602 |
|     | Coffee C        | 0.001 − 0.010   | 0.111 1.020   | 2.729 |
|     | Platinum        | 0.009 0.006     | 0.098 0.487   | 3.302 |
|     | Sugar No. 11    | 0.008 0.009     | 0.092 0.253   | 0.740 |
|     | Silver 5000 Oz  | 0.005 − 0.002   | 0.081 0.031   | 1.081 |
December 2012, and we group the variables into nine main categories: output and income,
labour market, housing, consumption, orders and inventories, money and credit, stock mar-
ket, bond and exchange rate, and prices series. A reader may find a detailed description of
the variables and of the sources from which they were collected in “Appendix”.
Since previous literature has highlighted that most macroeconomic series are not sta-
tionary, in the sense that they contain one (or more) unit roots, we perform the Augmented
Dickey-Fuller (ADF) test on the series. The null hypothesis of this test is that the series
contains a unit root; consistently, we maintain the original values of the variables if the null
hypothesis is rejected at a significance level of 5%. Otherwise, we take the first difference
of the variables and test them again. Again, we maintain the first difference of the variables
if the null hypothesis is rejected at a significance level of 10%. By contrast, we exclude the
variables if the null hypothesis cannot be rejected in the second application of the Dickey
Fuller test. At the end of this process, we obtain a set of 128 macroeconomic variables.
3.3   Commodity‑specific factors
The commodity-specific factors that we consider are the hedging pressure factor (HP), the
basis factor, and the momentum factor, defined exactly as in Daskalaki et al. (2014). More
precisely, the hedging pressure factor is represented by the difference between positive and
negative hedging pressure positions. The hedging pressure of a commodity j at time t is
calculated as the ratio between the number of short hedging positions minus the number of
long hedging positions, divided by the total number of hedgers in the commodity market:
|     | #shorthedgeposition | −#longhedgeposition |      |     |
| --- | ------------------- | ------------------- | ---- | --- |
|     |                     | j,t                 | j,t. |     |
HP =
| j,t | Total#hedgeposition |     |     | (7) |
| --- | ------------------- | --- | --- | --- |
j,t
1 3

1328 Annals of Operations Research (2021) 299:1317–1356
Table 3 Summary statistics for
Variable Mean Median SD Skewness Kurtosis
commodity-specific factors
Hedging pressure 0.004 0.005 0.044 − 0.125 1.012
Basis 0.010 0.011 0.045 − 0.009 1.393
Momentum 0.009 0.009 0.050 0.353 3.329
The basis factor is defined as the difference of the return of a portfolio of commodity
futures with positive basis and a portfolio with negative basis. For a commodity j at time t,
basis is calculated as
F −F
Basis =
j,t j,t+1
,
j,t F (8)
j,t
where F j,t is the price of the nearest available futures contract on j, while F j,t+1 is the price
of the next nearest available futures contract on j.
Finally, the momentum factor is the difference between the return of a portfolio of com-
modity futures with highest prior 12-month return and the return of a portfolio of commod-
ity futures with lowest prior 12-month return.5 Gorton et al. (2012), Shen et al. (2007) and
Narayan et al. (2015) have documented robust momentum effects in commodity futures
returns. Table 3 reports summary statistics for the commodity-specific factors from Janu-
ary 1989 to December 2012.
4 Empirical results
In this Section we discuss the model estimated. Then, we provide a detailed analysis of
the OOS predictability power of the models, using the MAE and the RMSFE and compar-
ing the forecast performances of the models that include only macroeconomic variables to
models based on both macroeconomic and commodity-specific factors.
4.1 Results from in‑sample estimation
First, we report results of the linear regression models for the commodity futures returns.
We also estimate a first order autoregressive model for each commodity futures return
series, to be used as a benchmark to assess the forecast performances of the other models.
In Table 4 we report the regression coefficients, the R2 and adjusted R2 for the models that
were selected by the stepwise procedure; the regression results for low- and high-volatility
states are reported separately. Low-volatility models are estimated on the period starting
from January 1989 and ending in December 1997; the high-volatility models, instead, are
estimated on the period from January 1998 to December 2003. The estimation periods fail
to exhaust the sample because they simply form the basis for the subsequent back-testing
exercise. Panels A and B of Table 4 are dedicated to backward and forward stepwise regres-
sions that include macroeconomic variables only. Panel C and D, instead, show results for
5 More precisely, the procedure is as follows: at any time, t, we sort the commodities according to their past
12‐month performances and create an equally‐weighted portfolio that is long on the first 5 commodities in
the ranking and short on the last 5 commodities in the ranking.
1 3

Annals of Operations Research (2021) 299:1317–1356 1329
1 3
sledom
noisserger
drawrof
dna
drawkcab
fo
noitamitsE
4
elbaT

1330 Annals of Operations Research (2021) 299:1317–1356
1 3
)deunitnoc(
4
elbaT

Annals of Operations Research (2021) 299:1317–1356 1331
1 3
)deunitnoc(
4
elbaT

1332 Annals of Operations Research (2021) 299:1317–1356
1 3
)deunitnoc(
4
elbaT

Annals of Operations Research (2021) 299:1317–1356 1333
1 3
)deunitnoc(
4
elbaT

1334 Annals of Operations Research (2021) 299:1317–1356
backward and forward algorithms that employ both macroeconomic and commodity-spe-
cific factors as predictors in a stepwise algorithm. Finally, Panel E reports the regression
coefficients for the first-order autoregressive benchmark.
First, in panels A and B, backward and forward stepwise algorithms lead to the specifi-
cation of rather similar models. In general, for most commodities, there is evidence of con-
siderably more macroeconomic predictors being selected in the high-volatility regime than
in the low-volatility one, consistently with our brief literature review. For instance, silver
futures returns are predicted by PC3 and PC7 under both backward and forward variable
inclusion algorithms in the low volatility state, and by PC1, PC2, PC5, and PC10 under
both stepwise rules in the high volatility regime. The resulting adjusted R2 coefficients are
included between an approximate 2% (for gold) and 15% (platinum) in the low-volatility
regime, and 2% (for coffee) and a remarkable 26% (for gasoline) in the high-VIX one.6
In panels C and D of Table 4, when commodity-specific predictors are added, the gen-
eral insights on when and which macroeconomic factors are included as predictors remain
intact. This is already an indication that the predictive power of the latter is approximately
independent of the power of the former set of variables. In fact, the improvement in in-
sample forecasting accuracy brought about by the basis, hedging pressure, and momen-
tum is limited: in both panels, they are hardly ever significant in terms of t-tests, while the
resulting adjusted R2 generally declines! For instance, comparing panels A and C, we find
that in the latter the adjusted R2 coefficients now range between − 2 and 12% (down from
a range + 2 to 15%) in the low-volatility regime, and between − 4 and 20% (down from a
range + 2 to 26%) in the high-volatility regime. Finally, in panel E of Table 4, we report
on the performance of the AR(1) benchmark, finding that the autoregressive coefficient
is hardly ever significant independently of the volatility regime. Therefore, this appears to
be a weak benchmark. Yet, the adjusted R2, which we do not report because they would be
hardly meaningful being based on an autoregressive structure, tended to generally exceed
(although by a modest spread) those in panels A-D of the table.
4.2 Comparison of out‑of‑sample performances
The existing literature abounds with results in which relatively rich predictive models
offer a rather accurate in-sample fit that however fails to be met by a similarly accurate
OOS performance, presumably due to over-fitting problems (see, for instance, Rapach and
Wohar 2006). In addition, empiricists have been aware at least since Bossaerts and Hil-
lion’s (1999) work on equity return predictability, that even predictive regressions speci-
fied on the basis of information criteria that penalize over-fitting (such as the AIC that we
employ), may in any case lead to poor OOS performance. Therefore, the goal of this sec-
tion is to investigate the OOS predictive power of the models estimated in Sect. 4.1, when
parameter estimates are held fixed to those in Table 4 and therefore are obtained with refer-
ence to data for a 1989–2003 sample. As a result, the OOS period is Jan. 2004–Dec. 2012
and appears to be long in terms of number of observations spanned and to also include two
different volatility “cycles/regimes”: 2004–2007 and then 2011–2012 characterized by low
volatility, and 2008–2010 characterized by a high volatility regime.
6 The fact that the number and nature of the principal components included in the “optimized” predictive
regressions is highly sensitive to whether the data are drawn from a low- versus a high-volatility regime
provides indirect confirmation of the presence of regime switching dynamics in the data.
1 3

Annals of Operations Research (2021) 299:1317–1356 1335
In particular, we compute the one-month ahead forecasts of futures commodity returns
under both low- and high-volatility predictive regressions (specified using either backward
or forward stepwise methods). This is performed for models that include macroeconomic
predictors only (using the parameter estimates in panels A and B of Table 4) but also mod-
els extended to include commodity factors (using the estimates in panels C and D). At each
point in time of the OOS period, the forecasts are also (i.e., in addition to forecasts that
simply classify the t + 1 regime as either low- or high-volatility, according to whether the
time t filtered probability of a low-volatility regime exceeds or not 0.5) obtained as (fil-
tered, one-step forward-iterated, real-time) probability-weighted averages of the forecasts
that refer to the low- versus the high-volatility state. Under a RMSFE loss function, such
weighting by predicted regime probabilities of regime-specific forecasts can be shown to
be optimal under the assumption that the Markov states are independent of all other shocks
in the model.
As discussed, to evaluate the accuracy of the different combinations between stepwise
predictor selection techniques and whether the selection set includes or not the commodity-
specific factors, we use two standard summary measures, the MAE and the RMSFE. The
MAE is the average of the absolute forecast errors of the models over the OOS period, say
between t = 1 and T,
T T
1 1
MAE= ŷ −y = ê ,
T t t T t (9)
t=1 t=1
∑ ∑
| | | |
where ê t is the the absolute error, ŷ t i|s the p|rediction |fro|m a given model/selection
method, and y t is the true value of a variable. Clearly, the smallest the MAE, the highest
is the f|ore|casting power of a model. Panel A of Table 5 reports the realized OOS values
| |
of MAE for the backward and forward stepwise methodologies. The upper portion of the
table shows the values of MAE for backward and forward stepwise regressions that only
include macroeconomic factors, when we do not average-weight the low- and high-volatil-
ity regime forecasts; next, we report similar, unweighted forecasts when the set of predic-
tors also includes the basis, hedging pressure, and momentum; the last two sections of the
Table report, in the same order, similar information when we weight-average the forecasts
from different regimes on the basis of their one-step ahead predicted probability of being in
either a low- or in a high-volatility regime.7 The very bottom of the table reports the MAE
of the AR(1) benchmark. We prefer to comment on MAE first because this forecast accu-
racy measure is obviously less sensitive to outliers and is therefore more robust.
In Table 5, there is no stark result, apart from the fact the grand averages of MAE values
with and without commodity-specific factors are approximately the same. However, this
just applies to the average of the MAEs (both unweighted and probability-weighted), as for
some commodities there is evidence that the inclusion of the basis, hedging pressure, and
momentum lowers MAE (this happens for crude oil, lumber, soybeans, gold, and platinum),
while for some others it increases MAE (wheat, gasoline, orange juice, coffee, and sugar).
7 While the upper portion of the Table relies only on whether the state probability of a low regime exceed
0.5 or not, the bottom parts of the Table also rely on the predictions from the estimated two-state MS model
for the VIX. Although one may argue that this way of proceeding is more elegant and consistent with the
framework of our paper, note that at this point we find ourselves jointly assessing the forecasting power of
the predictive regressions that include or not commodity-specific factors and the forecasting accuracy of a
simple MS model for the VIX. The latter model, as simple and compelling as it may appear, does not repre-
sent the main object of our analysis.
1 3

|  1336 |     |     | Annals of Operations Research (2021) 299:1317–1356 |     |
| ----- | --- | --- | -------------------------------------------------- | --- |
zO 0005
|     | 8170.0 9711.0 | 8170.0 9711.0 | 5070.0 8811.0 | 5070.0 8811.0 |
| --- | ------------- | ------------- | ------------- | ------------- |
 revliS
 raguS 11 .oN 2060.0 4871.0 2060.0 4221.0 4260.0 0081.0 4260.0 9021.0
munitalP
|     | 3760.0 9521.0 | 3760.0 9521.0 | 5660.0 6421.0 | 5660.0 6421.0 |
| --- | ------------- | ------------- | ------------- | ------------- |
C eeffoC
|     | 5270.0 3470.0 | 2670.0 3470.0 | 5970.0 7670.0 | 3080.0 7670.0 |
| --- | ------------- | ------------- | ------------- | ------------- |
 egnarO
|     | 6960.0 2001.0 | 6960.0 1190.0 | 9170.0 7501.0 | 9170.0 3290.0 |
| --- | ------------- | ------------- | ------------- | ------------- |
eciuJ
enilosaG
|     | 5780.0 5691.0 | 5780.0 7831.0 | 2090.0 4891.0 | 2090.0 1531.0 |
| --- | ------------- | ------------- | ------------- | ------------- |
 001 dloG
|                                                                                             | 6630.0 9250.0                                                                                    | 6630.0 9250.0 | 7630.0 4050.0                                                                                    | 7630.0 4050.0 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------- | ------------------------------------------------------------------------------------------------ | ------------- |
| serusaem ycarucca SOO )EFSMR( rorre erauqs-naem-toor dna )EAM( rorre etulosba naeM  5 elbaT | dedulcxe srotcaf cfiiceps-ytidommoc-ytilitalov hgih/wol detarapes-noitceles drawrof/drawkcaB-EAM |               | dedulcni srotcaf cfiiceps-ytidommoc-ytilitalov hgih/wol detarapes-noitceles drawrof/drawkcaB-EAM |               |
zO
 nottoC
|     | 3160.0 2361.0 | 8360.0 2121.0 | 0360.0 6351.0 | 2560.0 7711.0 |
| --- | ------------- | ------------- | ------------- | ------------- |
2 .oN
|     | 9450.0 4522.0 | 9450.0 0811.0 | 0060.0 4222.0 | 0060.0 3711.0 |
| --- | ------------- | ------------- | ------------- | ------------- |
aocoC
taehW 6660.0 4311.0 6660.0 1431.0 0760.0 6211.0 0760.0 0431.0
snaebyoS
|     | 1260.0 7721.0 | 5360.0 8701.0 | 3260.0 5021.0 | 2360.0 5790.0 |
| --- | ------------- | ------------- | ------------- | ------------- |
elttaC 6330.0 8130.0 6330.0 8130.0 7330.0 2230.0 7330.0 2230.0
 eviL
rebmuL
|     | 0660.0 4121.0 | 5660.0 4121.0 | 5660.0 1311.0 | 6560.0 1311.0 |
| --- | ------------- | ------------- | ------------- | ------------- |
|     | 4460.0 8490.0 | 4460.0 8490.0 | 9660.0 3490.0 | 9660.0 3490.0 |
nroC
rorre etulosba naeM :A lenaP
 edurC 9470.0 8701.0 0280.0 8701.0 1470.0 4301.0 8180.0 4301.0
 tnerB
liO
-drawkcaB ytilitalov -drawkcaB ytilitalov ytilitalov ytilitalov -drawkcaB ytilitalov -drawkcaB ytilitalov ytilitalov ytilitalov
|     |            | -drawroF -drawroF |                  | -drawroF -drawroF |
| --- | ---------- | ----------------- | ---------------- | ----------------- |
|     |  wol  hgih |  wol              |  hgih  wol  hgih |  wol  hgih        |
1 3

Annals of Operations Research (2021) 299:1317–1356  1337
zO 0005
| 9811.0 9811.0 | 2811.0 2811.0 | 2090.0 8880.0 | 2641.0 8880.0 | 2641.0 |
| ------------- | ------------- | ------------- | ------------- | ------ |
 revliS
 raguS 11 .oN 8511.0 7190.0 6711.0 9190.0 8870.0 2770.0 9422.0 2770.0 1741.0
munitalP
| 7990.0 7990.0 | 9790.0 9790.0 | 5570.0 2880.0 | 9561.0 2880.0 | 9561.0 |
| ------------- | ------------- | ------------- | ------------- | ------ |
C eeffoC
| 5770.0 1970.0 | 3080.0 5080.0 | 4170.0 1690.0 | 3301.0 5790.0 | 3301.0 |
| ------------- | ------------- | ------------- | ------------- | ------ |
 egnarO
| 2580.0 5080.0                                                                                                                   | 2090.0 8280.0                                                                                                             | 3470.0 8580.0 | 9621.0 8580.0 | 4111.0 |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------- | ------ |
| eciuJ dedulcxe srotcaf cfiiceps-ytidommoc-seitilibaborp deretlfi yb dethgiew ytilitalov hgih/wol-noitceles drawrof/drawkcaB-EAM | dedulcni srotcaf cfiiceps-ytidommoc-seitilibaborp deretlfi yb dethgiew ytilitalov hgih/wol-noitceles drawrof/drawkcaB-EAM |               |               |        |
enilosaG
| 6831.0 5211.0 | 4041.0 7111.0 | 5480.0 6901.0 | 1752.0 6901.0 | 6091.0 |
| ------------- | ------------- | ------------- | ------------- | ------ |
 001 dloG
| 0540.0 0540.0 | 6340.0 6340.0 | 5540.0 9440.0 | 7360.0 9440.0 | 7360.0 |
| ------------- | ------------- | ------------- | ------------- | ------ |
dedulcxe srotcaf cfiiceps-ytidommoc-ytilitalov hgih/wol detarapes-noitceles drawrof/drawkcaB-ESMR
zO
 nottoC
| 4901.0 2190.0 | 0501.0 1980.0 | 6370.0 2180.0 | 3422.0 9280.0 | 4061.0 |
| ------------- | ------------- | ------------- | ------------- | ------ |
2 .oN
| 5431.0 5380.0 | 8431.0 5580.0 | 3960.0 6170.0 | 2492.0 6170.0 | 0341.0 |
| ------------- | ------------- | ------------- | ------------- | ------ |
aocoC
taehW 1190.0 3990.0 3190.0 0001.0 9870.0 1380.0 8241.0 1380.0 3961.0
sledom )1(RA-seitilibaborp deretlfi yb dethgiew ytilitalov hgih/woL-EAM
snaebyoS
| 5290.0 4280.0 | 4980.0 1870.0 | 1860.0 1180.0 | 7871.0 1280.0 | 9931.0 |
| ------------- | ------------- | ------------- | ------------- | ------ |
elttaC 7230.0 7230.0 7230.0 7230.0 5230.0 4140.0 5930.0 4140.0 5930.0
 eviL
rebmuL
| 3980.0 0880.0 | 9580.0 1480.0 | 0470.0 9080.0 | 7161.0 0480.0 | 7161.0 |
| ------------- | ------------- | ------------- | ------------- | ------ |
rorre-erauqs-naem-tooR :B lenaP
| 5770.0 5770.0 | 8870.0 8870.0 | 9770.0 3380.0 | 1511.0 3380.0 | 1511.0 |
| ------------- | ------------- | ------------- | ------------- | ------ |
nroC
 edurC 0501.0 8001.0 6201.0 3890.0 7270.0 5090.0 6041.0 2001.0 6041.0
)deunitnoc(  5 elbaT  tnerB
liO
| dethgiew dethgiew | dethgiew dethgiew |     |     |     |
| ----------------- | ----------------- | --- | --- | --- |
-drawkcaB -drawkcaB -drawkcaB ytilitalov -drawkcaB ytilitalov ytilitalov ytilitalov
| -drawroF | -drawroF |            | -drawroF   | -drawroF |
| -------- | -------- | ---------- | ---------- | -------- |
|          |          | )1(RA  wol |  hgih  wol |  hgih    |
1 3

1338 Annals of Operations Research (2021) 299:1317–1356
1 3
)deunitnoc(
5 elbaT
revliS
raguS
munitalP
C
eeffoC
egnarO
enilosaG
001
dloG
nottoC
aocoC
taehW
snaebyoS
eviL
rebmuL
nroC
tnerB
zO
0005
11
.oN
eciuJ
zO
2
.oN
elttaC
edurC
liO
dedulcni
srotcaf
cfiiceps-ytidommoc-ytilitalov
hgih/wol
detarapes-noitceles
drawrof/drawkcaB-ESMR
3780.0
4080.0
3780.0
7101.0
2090.0
1111.0
1540.0
4280.0
7670.0
6380.0
5180.0
5140.0
2180.0
0580.0
1780.0
-drawkcaB
wol
ytilitalov
6641.0
9622.0
0361.0
4301.0
2631.0
9752.0
4160.0
9302.0
1882.0
6141.0
8861.0
6930.0
5351.0
5511.0
7531.0
-drawkcaB
hgih
ytilitalov
3780.0
4080.0
3780.0
5101.0
2090.0
1111.0
1540.0
8480.0
7670.0
6380.0
4280.0
5140.0
2380.0
0580.0
6790.0
-drawroF
wol
ytilitalov
6641.0
6541.0
0361.0
4301.0
0111.0
1681.0
4160.0
2651.0
8241.0
2071.0
6421.0
6930.0
5351.0
5511.0
7531.0
-drawroF
hgih
ytilitalov
dedulcxe
srotcaf
cfiiceps-ytidommoc-seitilibaborp
deretlfi
yb
dethgiew
ytilitalov
hgih/wol-noitceles
drawrof/drawkcaB-ESMR
9811.0
1561.0
4431.0
2601.0
4801.0
4391.0
3550.0
4561.0
8502.0
2611.0
0731.0
5040.0
1321.0
8890.0
6831.0
-drawkcaB dethgiew
9811.0
1711.0
4431.0
3601.0
2990.0
0451.0
3550.0
6521.0
7801.0
2131.0
0211.0
5040.0
4121.0
8890.0
4921.0
-drawroF
dethgieW
dedulcni
srotcaf
cfiiceps-ytidommoc-seitilibaborp
deretlfi
yb
dethgiew
ytilitalov
hgiH/woL-noitceles
drawrof/drawkcaB-ESMR
2811.0
9661.0
4131.0
1701.0
8511.0
8391.0
0450.0
7151.0
3202.0
0611.0
2131.0
3040.0
1811.0
4990.0
9331.0
-drawkcaB dethgiew
2811.0
4711.0
4131.0
5601.0
5101.0
5151.0
0450.0
5221.0
1011.0
4231.0
7301.0
3040.0
3611.0
4990.0
3421.0
-drawroF
dethgiew
sledom
)1(RA-seitilibaborp
deretlfi
yb
dethgiew
ytilitalov
hgih/woL-ESMR
7311.0
2201.0
5501.0
5490.0
1090.0
6111.0
6850.0
2790.0
0880.0
9101.0
9680.0
3040.0
6390.0
5690.0
6190.0
)1(RA

Annals of Operations Research (2021) 299:1317–1356 1339
For the remaining five commodity futures returns series, the evidence is indeed mixed.
In any event, all such differences are modest. For instance, the largest reduction occurs in
the case of the Brent crude oil futures returns series, when the state probability-weighted
MAE declines from 0.105 to 0.103 when commodity-specific predictors are included and
a backward stepwise selection is applied (instead, in the case of the forward algorithm, the
decline is from 0.101 to 0.098). However, for all series, the reported MAEs are structurally
lower for the low-volatility regime, even though this regime implies stronger predictability,
as one would expect from the much lower variation in realized returns of this state of the
world. Finally, and crucially, for most series we observe a difficulty by predictive regres-
sions of all types at outperforming the AR(1) benchmark, that in fact implies lower MAEs
for 12 series out of 15 (the only ties are obtained for corn, live cattle, and gold, but also in
these cases, the solid OOS performance is attributable to commodity factors only in the
case of gold).
Panel B of Table 5 reports the OOS values for the second measure of predictive accu-
racy, the RMSFE, defined as
T ŷ −y 2
RMSFE= t=1 t t , (10)
� T
∑ � �
where the notation is the same as in Eq. (9). Panel B is then structured like Panel A. Also
the key qualitative remarks expressed with reference to Panel A apply in this case. First,
the grand average of the OOS RMSFE values with and without commodity-specific factors
are approximately the same. Only in a few cases (namely, Brent crude, lumber, soybeans,
especially in the high-volatility regime, and platinum), the inclusion of basis, hedging
pressure, and momentum as predictors lowers the RMSFE. By contrast, for the remaining
series, including commodity factors does not help. In panel B, there is some tendency for
the forward stepwise algorithm to lead to lower RMSFEs than the backwards algorithm, a
difference that did not appear in panel A and therefore indicates that backward-type fore-
casts produce larger outliers than forward-type do. Second, also in this case and for all the
series, the reported RMSFEs are structurally lower for the low-volatility regime. Third, for
all series but gold and live cattle futures returns, all stepwise methods and selections of
predictors lead to higher RMSFEs than the AR(1) benchmark does.
4.3 Robustness checks
The analysis presented in the previous section relies on the estimation of two separate pre-
dictive regressions based on the prevailing VIX regime. One may be concerned that the use
of a two-step procedure may decrease the predictive accuracy of the model because of the
lower efficiency versus a one-step estimation approach. To check for this possibility, we
also estimate MS predictive regressions (with and without commodity-specific factors) in
which the definition of and the inferences on the state ( S t,j =1,2, where j indexes different
commodities) are also affected by the second moment of the prediction errors, to retain a
connection with second moments that so far has been captured by the VIX mean state.
The results concerning the predictive accuracy of the MS regressions are reported in
Table 6. The switching predictive regressions generally lead to lower RMSFE than their
probability-weighted counterparts, which is expected, as MS models are well-known to
1 3

1340 Annals of Operations Research (2021) 299:1317–1356
1 3
ledom
gnihctiws
vokraM
evitanretla
na
fo
ycarucca
evitciderp
SOO
eht—kcehc
ssentsuboR
6
elbaT
0005
revliS
.oN
raguS
munitalP
C
eeffoC
egnarO
enilosaG
001
dloG
nottoC
aocoC
taehW
snaebyoS
eviL
rebmuL
nroC
tnerB
zO
11
eciuJ
zO
2
.oN
elttaC
liO
edurC
ylno
stnenopmoc
lapicnirp
-
ledom
gnihctiws
vokraM
8880.0
7280.0
5450.0
4670.0
6970.0
8980.0
8640.0
9370.0
4370.0
7580.0
2070.0
1430.0
3470.0
5970.0
4470.0
EAM
2880.0
0380.0
1450.0
1870.0
0970.0
3190.0
6540.0
1370.0
3670.0
0580.0
5070.0
9330.0
1670.0
2180.0
4370.0
ESMR
srotcaf
cfiiceps-ytidommoc
&
stnenopmoc
lapicnirp
-
ledom
gnihctiws
vokraM
3011.0
4501.0
0080.0
7101.0
6990.0
8611.0
2950.0
9590.0
0290.0
8011.0
8090.0
0240.0
0790.0
7790.0
3190.0
EAM
7111.0
8401.0
9870.0
2301.0
3001.0
2911.0
4750.0
2690.0
2590.0
5211.0
7090.0
5140.0
6890.0
8001.0
9090.0
ESMR

Annals of Operations Research (2021) 299:1317–1356 1341
produce forecast errors that are less volatile than those of competing models (see, e.g.,
Guidolin and Timmermann 2007). Indeed, MS models that only include macroeconomic
variables are often able to outperform the AR(1) benchmark, which was not the case for
most of the probability-weighted predictions. By contrast, when we turn to analyze MAE,
the results are qualitatively very similar to those reported in Sect. 4.2. In particular, the
MS predictive regressions based on macroeconomic variables outperforms their weighted
counterparts in the case of Crude Oil, Lumber, Soybeans, Wheat, Cocoa, Cotton, Gasoline,
Coffee, Platinum, Sugar, and Silver, while the reverse applies to Corn, Live Cattle, Gold,
and Orange Juice. However, the differences are never as stark as in the case of RMSFE.
Interestingly, the adoption of MS models confirms (or even strengthens) our previous con-
clusion that commodity-specific factors do little to increase the predictive accuracy of the
models. Instead, their inclusion always lowers both MAE and RMSFE when switching
regressions are considered.
A second robustness check concerns the benchmarks used in our analysis. Indeed, as the
AR(1) model turns out to be rather strong especially for some commodities such as crude
oil, one may wonder whether it would be appropriate to add an AR component also to
the model that includes macroeconomic predictors only, before comparing it to the model
augmented with commodity-specific factors. Therefore, in a set of unreported results (that
remain available upon request), we compare the RMSFE of three alternative models: (i) the
simple AR(1) benchmark; (ii) a macro-PC model; (iii) a macro-PC model augmented with
an AR(1) term. First, the model under (iii) hardly outperforms the macro-PC model when
its OOS performance is considered: indeed, this happens only in the case of corn, cocoa,
cotton, and coffee. Second, the model under (iii) never outperforms the AR(1) model.
Therefore, because a model augmented with the commodity-specific factors is always able
to outperform the AR(1) model, this evidence is re-assuring that it would also outperform
an augmented macro model. In conclusion, this additional robustness check shows that we
using a AR(1) benchmark is a conservative choice, as this is a benchmark represents a
rather tall hurdle in terms of OOS performance.
5 P ortfolio allocation tests
Even though the OOS statistical evidence in Sect. 4 on the predictive power of the basis,
hedging pressure, and momentum as well as on all models (even those just based on mac-
roeconomic variables) are quite grim, an investor would be more interested in the pos-
sibility to exploit the forecasts from the various models than in their MAEs or RMSFEs
compared to a AR(1) benchmark. Therefore, in this Section, we conduct an additional OOS
recursive asset allocation exercise based on the forecasts of the expected futures commod-
ity returns estimated under different combinations of model selection criteria and of types
of predictors included. This exercise is particularly relevant given the increasing interest of
investors in including commodities in their portfolios, as they would offer diversification
opportunities with respect to other asset classes with which they tend to show modest or
even negative correlations (see Daskalaki and Skiadopoulos 2011; Giampietro et al. 2018).
Recent literature, see e.g., Dal Pra et al. (2018) has shown a few cases in which a statistical
model fails to outperform simple benchmarks in terms of realized OOS predictive accuracy
and yet leads to a solid increase in risk-adjusted portfolio performance relative to the same
benchmark.
1 3

1342 Annals of Operations Research (2021) 299:1317–1356
5.1 Optimal portfolios in a mean–variance framework
Our aim is to compare the realized (risk-adjusted) OOS performance of portfolios that exploit
forecasts of futures returns estimated with macroeconomic variables-based models with those
that rely on forecasts produced expanding the set of predictors to include “local” asset class-
specific variables. To use a robust framework—that over short investment intervals is known
to well approximate many other types of utility modes—we compute optimal portfolios in a
mean–variance set up. Among the tradable assets we include the S&P 500 total return index
(as a proxy for the equity market), the US 10-Year Treasuries (to proxy the default risk-free
bond market), and 30-day T-bills (to proxy cash investments). We include equity, bonds, and
cash on the top of our 15 commodity futures strategies not only for realism, to simulate the
strategic asset allocation decisions of a US investor over time, but also because the literature
has strongly emphasized how the low correlation of commodities with the other asset classes
may make them considerably more appealing than what their Sharpe ratios reveal (see, e.g.,
Chong and Miffre 2010; Daskalaki and Skiadopoulos 2011; Henriksen et al. 2019). To retain
symmetry and obtain a fair “playing field” across assets, we apply to stock and bond returns
the same predictive models (for instance, in terms of whether only macro variables are to be
included, as well as in terms of the backward or forward stepwise approaches implemented)
applied to commodity futures returns. For simplicity, we assume instead that the 1-month
T-bill rate is a constant and known in advance.
In more detail, let 𝜇 i,t+1 be the predicted return with 𝜎 i 2 ,t+1 the variance on the asset i. Sup-
pose that an investor allocates her wealth at time t according to a set of weights 𝝎 t , for which
n i=1 𝜔 i,t =1 holds (n is the number of assets available to the investor) and that she cares (at
least locally, i.e., for a one-period investment horizon) only about the conditional mean and
∑
variance of her portfolio returns, so that she wants to maximize the functional
𝛾
max𝜇 − 𝜎2 ,
𝜔 p,t+1 2 P,t+1 (11)
t
where 𝛾 represents her risk aversion coefficient. If we indicate the risk-free rate as r t f +1 , we
have that, at any point in time, the portfolio expected return is
�
𝜇 =rf + 𝝁 −rf ′1 𝝎
p,t+1 t+1 t+1 t+1 t (12)
( )
and the portfolio variance is
n
𝜎2 = 𝜔 𝜔 Cov(r ,r )=𝝎�𝚺 𝝎,
P,t+1 i,t j,t i,t+1 j,t+1 t t+1 t (13)
i,j=1
∑
where 𝝎 t+1 represents the vector of weights and 𝚺 t+1 the variance–covariance matrix of
asset returns predicted at time t for time t + 1. This leads to classical, unconstrained
program
� 𝛾
maxrf + 𝝁 −rf ′1 𝝎 − 𝝎�𝚺 𝝎
𝝎 t+1 t+1 t+1 t 2 t t+1 t (14)
t
( )
𝝎 ′1=1.
t+1
From its first order condition, the problem in (14) implies the formulas for the optimal
vector of weights:
1 3

Annals of Operations Research (2021) 299:1317–1356 1343
−1
1
𝝎̂ = 𝝁 −rf ′1 .
t 𝛾 t+1 t+1 (15)
t+1
∑( )
No short sale constraints are imposed. Following DeMiguel et al. 2007, we build static
one-period optimal portfolios over time, considering expanding windows of data, starting
from the beginning of our sample and including all the data until the time of the forecast;
then, we calculate the corresponding portfolio expected return, realized mean–variance
utility and Sharpe ratio for each time t. The recursive exercise is initialized with reference
to January 1989–December 2003 to produce a January 2004 portfolio and then iterated
107 times until the last estimation sample, January 1989-November 2012, to produce an
optimal portfolio for December 2012. Because in this paper we do not compute forecasts
of second-order moments, we use historical data on the same expanding window described
above to estimate the sample covariance matrix.8
For the sake of robustness, we use three different values of the risk aversion coefficient 𝛾
(0.10, 0.25, and 0.5). To make our portfolio exercise realistic, we also consider the transac-
tion costs of rebalancing the portfolio at any time t. Additionally, we consider that an investor
may want to rebalance her portfolio only if she can get an advantage in terms of the expected
return of the portfolio. This means that she will decide to rebalance her portfolio at time t
only if the transaction costs of rebalancing do not exceed the portfolio expected returns at
t + 1. Therefore, we solve the portfolio problem under the following, additional condition
n n
Δ𝜔 ×tc ≤ 𝜇 𝜔̃
i,t i i,t+1 i,t (16)
i=1 i=1
∑ ∑
| |
where tc is some proportional tra|nsacti|on cost, Δ𝜔 i,t represents a hypothetical change in
weights in case of rebalancing and 𝜔̃ i,t ≡𝜔 i,t−1 +Δ𝜔 i,t represents the hypothetical weights
at t in case of rebalancing. If (16) does not hold, then an investor would not rebalance
between t and t + 1, as the implied costs are higher than the resulting expected benefits.
Otherwise, we consider that the investor will rebalance her portfolio at t and take the
resulting transaction costs into account when computing realized portfolio performance at
time t + 1. As for the imputed level of the cost tc, we face a need to introduce some sim-
plification because an investor willing to rebalance her portfolio would pay two types of
transaction costs: costs to access the market (or infrastructure costs) and liquidity costs.
While it is quite difficult to make assumptions on the first type of costs, as they are likely
to depend on the exact nature of an investor (e.g., whether she is an institutional investor
and of what size), we can reasonably assume the liquidity costs being close to the bid-ask
spread as a percentage of the mid-price and therefore being proportional to the amount
transacted. Therefore, to estimate the parameter tc, we have collected daily best ask and
best bid prices for commodity futures contracts, for the period Jan. 1996–Dec. 2016. For
each commodity, we estimate a daily time series for tc as the bid-ask spread as a percent-
age of the mid-price. Next, we compute the average tc as the grand average of all such
daily values. We get an average value of the transaction costs across all commodities equal
to approximately 0.09%. Therefore, also because such estimates are considerably variable
over time and across different commodities, to simplify we set tc = 0.1%. When the con-
straint (16) is added to the general mean–variance program in (14), the solution must be
performed numerically using a non-linear optimization algorithm.
8 We have also experimented with 5-year rolling estimation windows, obtaining qualitatively similar
results.
1 3

 1344 Annals of Operations Research (2021) 299:1317–1356
 ni tessa hcae rof sthgiew egareva eht sniatnoc noitrop mottob ehT .selbairav cimonoceorcam ylno edulcni snruter serutuf ytidommoc rof sledom evitciderp eht nehw secnam  ehT :C lenaP .unem tessa eht ni tessa hcae rof sthgiew egareva eht sniatnoc noitrop mottob ehT .selbairav cfiiceps-rotcaf dna cimonoceorcam htob edulcni snruter serutuf yti  egareva eht sniatnoc noitrop mottob ehT .ledom )1(RA kramhcneb a rednu secnamrofrep oiloftrop lamitpo ,dezilaer rof scitsitats yrammus stroper elbat eht fo noitrop reppu
-rofrep oiloftrop lamitpo ,dezilaer rof scitsitats yrammus eht stroper elbat siht fo noitrop reppu ehT :A lenaP .secnamrofrep dezilaer dna snoitacolla oiloftrop lamitpO  7 elbaT -dommoc rof sledom evitciderp eht nehw secnamrofrep oiloftrop lamitpo ,dezilaer rof scitsitats yrammus eht stroper elbat siht fo noitrop reppu ehT :B lenaP .unem tessa eht
noitceles drawroF
80100.0 84010.0 96753.0 50100.0
| %534.3 %817.2 %286.0 − %355.2 − | %532.1 − %298.1 − %575.0 − %760.0 %360.1 | %273.2 − %354.0 − %121.1 %790.0 %406.0 | %250.0 − %708.1 %209.89 |
| ------------------------------- | ---------------------------------------- | -------------------------------------- | ----------------------- |
5.0 = γ
noitceles drawkcaB
00000.0 10410.0 19000.0 − 50000.0 −
| %185.5 %611.1 %675.0 %055.0 − | %024.1 %344.1 − %720.0 − %547.2 − %982.3 | %353.4 − %954.0 − %020.0 − %481.0 − %237.0 | %145.1 − %299.2 %616.59 |
| ----------------------------- | ---------------------------------------- | ------------------------------------------ | ----------------------- |
5.0 = γ
noitceles drawroF
80100.0 84010.0 77753.0 70100.0
| %534.3 %817.2 %286.0 − %255.2 − | %532.1 − %298.1 − %575.0 − %760.0 %360.1 | %273.2 − %354.0 − %121.1 %790.0 %406.0 | %250.0 − %708.1 %209.89 |
| ------------------------------- | ---------------------------------------- | -------------------------------------- | ----------------------- |
52.0 = γ
noitceles drawkcaB
00000.0 10410.0 60100.0 − 30000.0 −
| %185.5 %611.1 %675.0 %055.0 − | %024.1 %344.1 − %620.0 − %547.2 − %982.3 | %353.4 − %954.0 − %020.0 − %481.0 − %337.0 | %145.1 − %299.2 %616.59 |
| ----------------------------- | ---------------------------------------- | ------------------------------------------ | ----------------------- |
52.0 = γ
noitceles drawroF
sledom selbairav cimonoceorcam - snoitacolla oiloftrop lamitpO :A lenaP
80100.0 84010.0 36753.0 80100.0
| %434.3 %817.2 %286.0 − %255.2 − | %532.1 − %198.1 − %575.0 − %760.0 %360.1 | %273.2 − %354.0 − %121.1 %790.0 %406.0 | %250.0 − %708.1 %209.89 |
| ------------------------------- | ---------------------------------------- | -------------------------------------- | ----------------------- |
1.0 = γ
noitceles drawkcaB
30000.0 − 71410.0 02600.0 − 40000.0 − %585.5 %911.1 %875.0 %055.0 − %414.1 %144.1 − %820.0 − %947.2 − %492.3 %953.4 − %754.0 − %020.0 − %481.0 − %137.0 %245.1 − %399.2 %616.59
unem tessa eht ni tessa hcae rof sthgiew
1.0 = γ
noitaived dradnats ylhtnoM
nruter ylhtnom egarevA
| oitar eprahS ylraeY                           |                          |                           | dnoB yrusaerT Y01 |
| --------------------------------------------- | ------------------------ | ------------------------- | ----------------- |
| ecnairav–naeM sthgiew egarevA lio edurc tnerB |                          |                           | zO 0005 revliS    |
|                                               | 2 .oN nottoC zO 001 dloG | eciuJ egnarO 11 .oN raguS |                   |
elttaC eviL
|     | snaebyoS | enilosaG C eeffoC munitalP | 005 P&S |
| --- | -------- | -------------------------- | ------- |
rebmuL
| nroC | taehW aocoC |     |     |
| ---- | ----------- | --- | --- |
1 3

| Annals of Operations Research (2021) 299:1317–1356  |     |     |     |     | 1345 |
| --------------------------------------------------- | --- | --- | --- | --- | ---- |
noitceles drawroF
87100.0 15900.0 67746.0 57100.0 %558.3 %696.0 %685.0 − %374.0 %171.0 %601.1 − %490.0 − %602.0 − %600.3 %471.3 − %322.0 %525.0 %164.0 − %692.0 %122.0 %838.1 %123.49
5.0 = γ
noitceles drawkcaB
30000.0 − 53510.0 17500.0 − 80000.0 − %151.2 %254.0 − %046.0 %874.0 %663.1 %754.0 − %221.0 − %065.1 − %034.3 %320.2 − %862.0 %681.0 %353.0 − %270.0 − %932.0 − %524.1 %633.59
5.0 = γ
noitceles drawroF
|          | 87100.0 05900.0 28746.0 77100.0 | %558.3 %696.0 %685.0 − %374.0 | %171.0 %601.1 − %490.0 − %602.0 − | %600.3 %471.3 − %322.0 %525.0 %164.0 − |                       |
| -------- | ------------------------------- | ----------------------------- | --------------------------------- | -------------------------------------- | --------------------- |
| 52.0 = γ |                                 |                               |                                   | %692.0                                 | %122.0 %838.1 %123.49 |
sledom srotcaf cfiiceps-ytidommoc dna selbairav cimonoceorcam - snoitacolla oiloftrop lamitpO :B lenaP
noitceles drawkcaB
|     | 30000.0 − 63510.0 78500.0 − 60000.0 − | %254.0 − | %754.0 − %221.0 − %065.1 − | %420.2 − %353.0 − %270.0 − | %932.0 − |
| --- | ------------------------------------- | -------- | -------------------------- | -------------------------- | -------- |
52.0 = γ %151.2 %146.0 %874.0 %563.1 %034.3 %862.0 %681.0 %524.1 %633.59
noitceles drawroF
|     | 87100.0 05900.0 28746.0 77100.0 | %685.0 −             | %601.1 − %490.0 − |                                               |                       |
| --- | ------------------------------- | -------------------- | ----------------- | --------------------------------------------- | --------------------- |
|     |                                 | %558.3 %596.0 %474.0 | %171.0 %602.0 −   | %600.3 %471.3 − %422.0 %525.0 %164.0 − %692.0 | %122.0 %838.1 %123.49 |
1.0 = γ
noitceles drawkcaB
50000.0 − 45510.0 35010.0 − 60000.0 −
|     |     | %651.2 %944.0 − %246.0 %874.0 | %063.1 %554.0 − %421.0 − %365.1 − | %534.3 %030.2 − %962.0 %681.0 %353.0 − %470.0 − | %142.0 − %624.1 %633.59 |
| --- | --- | ----------------------------- | --------------------------------- | ----------------------------------------------- | ----------------------- |
1.0 = γ
noitaived dradnats ylhtnoM
nruter ylhtnom egarevA
| )deunitnoc(  7 elbaT | oitar eprahS ylraeY |     |     |     | dnoB yrusaerT Y01 |
| -------------------- | ------------------- | --- | --- | --- | ----------------- |
sthgiew egarevA liO edurC tnerB
|     | ecnairav–naeM |     |              |                                       | zO 0005 revliS |
| --- | ------------- | --- | ------------ | ------------------------------------- | -------------- |
|     |               |     | 2 .oN nottoC | zO 001 dloG eciuJ egnarO 11 .oN raguS |                |
elttaC eviL
snaebyoS
|     |     | rebmuL |     | enilosaG C eeffoC munitalP | 005 P&S |
| --- | --- | ------ | --- | -------------------------- | ------- |
taehW aocoC
nroC
1 3

|  1346 |     | Annals of Operations Research (2021) 299:1317–1356 |     |     |
| ----- | --- | -------------------------------------------------- | --- | --- |
5.0 = γ )1(RA
05000.0 23310.0 18031.0 64000.0
|     | %257.3 | %703.1 − %376.0 − %721.3 %345.0 %771.2 − %900.2 − %890.0 − | %183.62 − %223.3 %000.1 − %277.0 %243.0 %964.1 | %440.7 %068.2 %837.801 |
| --- | ------ | ---------------------------------------------------------- | ---------------------------------------------- | ---------------------- |
52.0 = γ )1(RA
05000.0 23310.0 18031.0 84000.0
|     | %257.3 | %703.1 − %376.0 − %721.3 %345.0 %381.2 − %900.2 − %890.0 − | %183.62 − %223.3 %000.1 − %277.0 %923.0 %964.1 | %440.7 %068.2 %837.801 |
| --- | ------ | ---------------------------------------------------------- | ---------------------------------------------- | ---------------------- |
1.0 = γ )1(RA
05000.0 23310.0 08031.0 94000.0
sledom )1(RA - snoitacolla oiloftrop lamitpO :C lenaP %437.3 %503.1 − %676.0 − %051.3 %325.0 %394.0 − %810.2 − %580.0 − %864.62 − %733.3 %000.1 − %877.0 %813.0 %974.1 %061.7 %638.2 %968.111
noitaived dradnats ylhtnoM
nruter ylhtnom egarevA
| )deunitnoc(  7 elbaT | oitar eprahS ylraeY |     |     | dnoB yrusaerT Y01 |
| -------------------- | ------------------- | --- | --- | ----------------- |
sthgiew egarevA
|     | ecnairav–naeM lio edurc tnerB |              |                                       | zO 0005 revliS |
| --- | ----------------------------- | ------------ | ------------------------------------- | -------------- |
|     |                               | 2 .oN nottoC | zO 001 dloG eciuJ egnarO 11 .oN raguS |                |
elttaC eviL
snaebyoS
|     |     | rebmuL      | enilosaG C eeffoC munitalP | 005 P&S |
| --- | --- | ----------- | -------------------------- | ------- |
|     |     | taehW aocoC |                            |         |
nroC
1 3

Annals of Operations Research (2021) 299:1317–1356 1347
Panel A of Table 7 reports summary statistics for realized performances and recursive
optimal portfolio weights obtained considering the three alternative risk aversion coeffi-
cients (0.1, 0.25, and 0.5), when the forecasts for commodity futures returns are computed
from stepwise predictive regressions based on macro principal components only. Panel B
reports the corresponding results when the basis, hedging pressure, and momentum are
used as additional predictors. Interestingly, and almost independently of the assumed
parameter 𝛾 , the largest fraction of all portfolios is allocated to 10-year Treasuries. This
result seems to be plausible, given the high 10-year bond returns recorded during the
2004–2012 sample, which is in fact largely dominated by the Great Financial Crisis and the
ensuing deep recession in the US, when interest rates plummeted and long-term govern-
ment bonds gave extraordinarily high average returns; the demand for stocks is small but
always positive. Interestingly, when commodity-specific factors are included, the share of
bonds slightly declines (from 96–98% to 94–95%), the one of stocks modestly increases
(from 1–2 to 2–3%), and residually the overall weight to commodities goes from 1–3% to
2–4%. In particular, crude oil, gold, and corn (when only macro factors are used) are the
commodities in relatively high positive demand, and gasoline, wheat, cotton, and live cattle
are the commodities in the largest negative demand.
The most striking results in Table 7, panel A, emerge from the upper portion devoted
realized performances, especially when compared to panel C, that concerns portfolio
weights under the benchmark model.9 First, there is now a massive difference between
the OOS realized performances of forward versus backward stepwise regression meth-
ods; in particular, while predictions based on forward stepwise regressions lead to high
and appealing annualized Sharpe ratios (essentially of 0.36 independently of the selected
value of 𝛾 ), forecasts based on backward stepwise regressions yield essentially zero or even
slightly negative risk-adjusted performances. Second, such annualized Sharpe ratios are
more than double versus those obtainable under the benchmark AR(1) model (0.13 inde-
pendently of 𝛾 ), and this derives from both the higher realized mean returns and from lower
realized portfolio standard deviations. Therefore investing in predictive technologies based
on macro variables that may be thought to affect the fundamental pricing kernel does pay
out in an OOS back-testing exercise, but only when the selected loss function is based on
the (risk-adjusted) portfolio performance, while it does not under more classical, statistical
loss functions, such as the MAE and the RMSFE covered in Table 5.
Panel B of Table 7 answers instead the question as to whether commodity-specific
factors generate economic value in a portfolio problem. Although the averages for the
weights for the different asset classes and commodities are generally similar (though not
exactly identical) versus those in panel A, unreported plots (that remain available from the
Authors upon request) reveal that their dynamics is positively correlated but not identi-
cal. As a result, the maximum realized risk-adjusted performance in the top portion of the
Table differs and it is in fact considerably higher, almost double (0.65 vs. 0.36, indepen-
dently of 𝛾 ), than that in panel B. This implies that access to the predictive power of the
basis, hedging pressure, and momentum massively increases the economic value of pre-
dictive systems applied to portfolio management that includes commodity futures among
9 In panel C, the average allocations implied by the benchmark are even more biased towards long posi-
tions in government bonds, now exceeding 100%. The long positions in commodities are modest and now
concentrated in silver, Brent crude oil, and gasoline; gold is instead massively shorted, which represents the
most visible difference versus the allocations in panels A and B.
1 3

1348 Annals of Operations Research (2021) 299:1317–1356
the asset classes.10 This is consistent with a recent literature that has stressed that such
“local” factors may come to play a key role in making sense of the cross-section of com-
modity returns, e.g., de Roon et al. (2000) and Daskalaki et al. (2014). In fact, such outper-
formance seems to derive more from a further improvement in the mean realized portfolio
returns than from a reduction of realized risk.
Table 8 repeats the comparisons performed in Table 7, but considering the transaction
costs, which in our experiment turns out to be important also because the predictive system
that we propose implies a considerable degree of turnover and portfolio re-shuffling over
time. Panel A is comparable to Table 7 and shows that—because an investor is allowed not
to trade to rebalance her portfolio when the expected cost exceeds the expected benefit—
taking realistic transaction costs into account slightly improves realized portfolio perfor-
mance, in risk adjusted terms. However, this remains true only for the forward predictor
selection algorithm, while for very high values of 𝛾 , some instability in the ratio appears in
the case of the benchmark.11 Moreover, our earlier conclusions concerning the economic
value of the commodity-specific predictors remain intact and can be quantified in a differ-
ence between annualized Sharpe ratios of 0.65 when commodity predictors are exploited
versus 0.36 when they are not, a spread of approximately 0.29.
Panels B and C of Table 8 proceed to disentangle the results under transaction costs
in panel A between the periods of low- versus high-volatility.12 Interestingly, all realized
annual Sharpe ratios move up now, and the difference between the predictability regres-
sions and the benchmark becomes massive. For instance, in periods of high volatility and
for 𝛾 =1 , the benchmark achieves a ratio of 0.13 to be contrasted to a stunning 2.63 from
forward stepwise regressions based on macro PCs only and 2.70 from models that also
include the basis, hedging pressure, and momentum; these estimates are 0.13, 0.60, and
1.08 with reference to the low-volatility period. The finding that models of predictabil-
ity generate more economic value in times of distress is fully consistent with the OOS
measures of forecasting accuracy commented in Sect. 4. However, one implicit finding is
that, under transaction costs, the commodity-specific factors add more risk-adjusted perfor-
mance in tranquil times (the increase in Sharpe ratio is approximately 0.48 and it exceeds
the probability-weighted estimate reported above) versus times of distress (the improve-
ment is only 0.07), which implies that macroeconomic factors play a leading role espe-
cially during the less frequent crisis periods.
5.2 Robustness checks
As a robustness check, we also examine the economic value of forecasts based on the MS
models introduced in Sect. 4.3. The results are reported in Table 9, where the left-portion
concerns predictive regressions that exclude commodity-specific factors and the right-
portion those that include them. Interestingly, the MS regressions lead to realized risk-
adjusted performances that are considerably lower than those obtained from the probabil-
ity-weighted model, disregarding whether commodity-specific factors are included or not.
10 Also in this case, the effect can be noted only when the predictions are computed using a forward step-
wise algorithm that starts out with a null model without any predictability, and progressively expands the
set of predictors if and when these lower the AIC of the resulting model.
11 In Table 8 and also as a way to check the robustness of our results, we have extended the exercise to
include more values of the risk aversion coefficient 𝛾 , also exceeding 1.
12 We have also performed this robustness check for the case without transaction costs and it gave insights
qualitatively similar to those reported in the main text.
1 3

Annals of Operations Research (2021) 299:1317–1356 1349
1 3
stsoc
noitcasnart
rof
gnitnuocca
secnamrofrep
oiloftrop
dezilaeR
8
elbaT
)1(RA
sledom
srotcaf
cfiiceps-ytidommoc
dna
selbairav
cimonoceorcaM
sledom
selbairav
cimonoceorcaM
-irav–naeM
detcepxE
ylraeY
noitceles
drawroF
noitceles
drawkcaB
noitceles
drawroF
noitceles
drawkcaB
ecna
nruter
eprahS
oitar
-naeM
detcepxE
ylraeY
-naeM
detcepxE
ylraeY
–naeM
detcepxE
ylraeY
–naeM
detcepxE
ylraeY
γ
ecnairav
nruter
eprahS
ecnairav
nruter
eprahS
ecnairav
nruter
eprahS
ecnairav
nruter
eprahS
oitar
oitar
oitar
oitar
ygetarts
dethgiew-ytilibaborP
:A
lenaP
94000.0
40600.0
08031.0
77100.0
33120.0
28746.0
60000.0
−
75000.0
−
35010.0
−
80100.0
89210.0
36753.0
40000.0
−
03000.0
−
02600.0
−
01.0
84000.0
40600.0
18031.0
77100.0
33120.0
28746.0
60000.0
−
13000.0
−
78500.0
−
70100.0
99210.0
77753.0
30000.0
−
50000.0
−
60100.0
−
52.0
64000.0
40600.0
18031.0
57100.0
33120.0
67746.0
80000.0
−
03000.0
−
17500.0
−
50100.0
89210.0
96753.0
50000.0
−
40000.0
−
19000.0
−
05.0
44000.0
40600.0
38031.0
47100.0
33120.0
48746.0
11000.0
−
92000.0
−
55500.0
−
40100.0
89210.0
47753.0
80000.0
−
60000.0
−
12100.0
−
57.0
14000.0
40600.0
28031.0
37100.0
33120.0
87746.0
41000.0
−
03000.0
−
46500.0
−
30100.0
89210.0
47753.0
01000.0
−
60000.0
−
71100.0
−
00.1
24100.0
42710.0
09242.1
17100.0
33120.0
08746.0
02000.0
−
03000.0
−
46500.0
−
00100.0
89210.0
47753.0
51000.0
−
60000.0
−
32100.0
−
05.1
94420.0
−
14340.0
−
31180.0
−
87100.0
33120.0
18746.0
30000.0
−
03000.0
−
76500.0
−
99000.0
99210.0
97753.0
81000.0
−
60000.0
−
52100.0
−
57.1
56720.0
−
61340.0
−
33080.0
−
87100.0
33120.0
88746.0
30000.0
−
03000.0
−
86500.0
−
79000.0
99210.0
08753.0
02000.0
−
60000.0
−
61100.0
−
00.2
02030.0
−
01240.0
−
69970.0
−
22100.0
96410.0
65635.0
30000.0
−
03000.0
−
17500.0
−
55100.0
97910.0
02556.0
52000.0
−
60000.0
−
71100.0
−
05.2
emiger
ytilitalov-woL
:B
lenaP
94000.0
40600.0
08031.0
34300.0
02140.0
24870.1
76200.0
11230.0
14746.1
03200.0
74520.0
68006.0
41200.0
16720.0
04528.0
01.0
84000.0
40600.0
18031.0
24300.0
02140.0
44870.1
76200.0
11230.0
44746.1
92200.0
35803.0
09006.0
31200.0
85233.0
54528.0
52.0
64000.0
40600.0
18031.0
04300.0
02140.0
34870.1
76200.0
11230.0
54746.1
72200.0
27720.0
88006.0
21200.0
17520.0
54528.0
05.0
44000.0
40600.0
38031.0
93300.0
02140.0
44870.1
66200.0
11230.0
74746.1
42200.0
27720.0
88006.0
11200.0
17520.0
44528.0
57.0
14000.0
40600.0
28031.0
73300.0
02140.0
34870.1
66200.0
11230.0
14746.1
22200.0
27720.0
68006.0
01200.0
17520.0
44528.0
00.1
24100.0
42710.0
09242.1
43300.0
02140.0
43870.1
56200.0
11230.0
44746.1
81200.0
27720.0
58006.0
80200.0
27520.0
65528.0
05.1
94420.0
−
14340.0
−
31180.0
−
33300.0
02140.0
44870.1
56200.0
11230.0
34746.1
51200.0
27720.0
78006.0
70200.0
27520.0
55528.0
57.1
56720.0
−
61340.0
−
33080.0
−
13300.0
02140.0
54870.1
46200.0
11230.0
34746.1
31200.0
26503.0
68006.0
60200.0
17520.0
93528.0
00.2
02030.0
−
01240.0
−
69970.0
−
42200.0
98720.0
57879.0
46200.0
11230.0
34746.1
90200.0
27720.0
68006.0
20200.0
94520.0
56028.0
05.2
emiger
ytilitalov-hgiH
:C
lenaP
94000.0
40600.0
08031.0
72300.0
82930.0
74307.2
65200.0
77030.0
22783.1
83300.0
35040.0
74726.2
17200.0
94230.0
51745.1
01.0
84000.0
40600.0
18031.0
72300.0
82930.0
82307.2
65200.0
57030.0
58583.1
83300.0
35040.0
43826.2
07200.0
84230.0
01745.1
52.0
64000.0
40600.0
18031.0
72300.0
82930.0
44307.2
55200.0
47030.0
10583.1
73300.0
35040.0
67826.2
07200.0
15230.0
23055.1
05.0

1350 Annals of Operations Research (2021) 299:1317–1356
1 3
)deunitnoc(
8
elbaT
)1(RA
sledom
srotcaf
cfiiceps-ytidommoc
dna
selbairav
cimonoceorcaM
sledom
selbairav
cimonoceorcaM
-irav–naeM
detcepxE
ylraeY
noitceles
drawroF
noitceles
drawkcaB
noitceles
drawroF
noitceles
drawkcaB
ecna
nruter
eprahS
oitar
-naeM
detcepxE
ylraeY
-naeM
detcepxE
ylraeY
–naeM
detcepxE
ylraeY
–naeM
detcepxE
ylraeY
γ
ecnairav
nruter
eprahS
ecnairav
nruter
eprahS
ecnairav
nruter
eprahS
ecnairav
nruter
eprahS
oitar
oitar
oitar
oitar
44000.0
40600.0
38031.0
72300.0
82930.0
05307.2
55200.0
57030.0
91683.1
73300.0
35040.0
65826.2
07200.0
05230.0
23055.1
57.0
14000.0
40600.0
28031.0
62300.0
82930.0
25307.2
45200.0
57030.0
32683.1
73300.0
35040.0
55826.2
96200.0
15230.0
24055.1
00.1
24100.0
42710.0
09242.1
62300.0
82930.0
26307.2
35200.0
57030.0
03683.1
63300.0
35040.0
95826.2
86200.0
15230.0
05055.1
05.1
94420.0
−
14340.0
−
31180.0
−
62300.0
82930.0
46307.2
35200.0
57030.0
82683.1
63300.0
35040.0
65826.2
86200.0
15230.0
84055.1
57.1
56720.0
−
61340.0
−
33080.0
−
62300.0
82930.0
76307.2
25200.0
57030.0
99583.1
63300.0
35040.0
75826.2
76200.0
15230.0
24055.1
00.2
02030.0
−
01240.0
−
69970.0
−
52300.0
92930.0
69307.2
15200.0
57030.0
82683.1
53300.0
35040.0
74826.2
66200.0
15230.0
44055.1
05.2

Annals of Operations Research (2021) 299:1317–1356  1351
Table 9  Robustness check—optimal portfolio allocations under an alternative Markov switching model.
The upper portion of the table reports the summary statistics for realized, optimal portfolio performances
when the predictive models for commodity futures returns include only macroeconomic variables (on the
left side) and when it includes both macroeconomic and factor-specific variables (on the right side). The
bottom portion contains the average weights for each asset in the asset menu
Principal components only Principal components & commodity-
specific factors
|     | γ = 0.1 γ = 0.25 | γ = 0.5 γ = 0.1 | γ = 0.25 γ = 0.5 |
| --- | ---------------- | --------------- | ---------------- |
Average monthly return 0.0014 − 0.0004 0.0087 − 0.0062 − 0.0064 − 0.0119
Monthly standard deviation 0.0437 0.0423 0.0552 0.0720 0.0713 0.0512
Yearly Sharpe ratio 0.1100 − 0.0306 0.5429 − 0.2971 − 0.3132 − 0.8032
Mean–Variance 0.0013 − 0.0006 0.0079 − 0.0064 − 0.0071 − 0.0125
Average weights
| Brent crude oil | 4.638% 3.384%     | 1.904% 2.854%     | − 1.732% 3.900%   |
| --------------- | ----------------- | ----------------- | ----------------- |
| Corn            | 1.490% 1.851%     | 5.879% 5.430%     | 4.287% 8.732%     |
| Lumber          | 0.576% 0.699%     | 0.088% 2.640%     | 0.895% 1.257%     |
| Gasoline        | − 0.678% 0.245%   | 3.406% 3.735%     | 10.098% 7.046%    |
| Soybeans        | − 1.623% − 2.344% | − 4.384% − 1.254% | 0.199% − 6.914%   |
| Wheat           | 1.500% 1.931%     | − 0.635% 1.918%   | − 0.111% 1.242%   |
| Cocoa           | − 1.183% − 1.345% | − 0.512% − 1.304% | − 2.624% − 3.373% |
Cotton No. 2 − 2.686% − 1.663% − 2.254% − 2.912% − 0.018% 0.229%
| Gold 100 Oz  | 1.424% 3.654%   | − 3.241% 2.446%   | 2.911% 2.194%   |
| ------------ | --------------- | ----------------- | --------------- |
| Gasoline     | − 0.678% 0.245% | 3.406% 2.423%     | 6.503% − 1.450% |
| Orange Juice | 0.238% − 0.005% | − 0.040% − 1.232% | 0.525% 0.238%   |
| Coffee C     | 2.093% 2.304%   | 1.992% 0.442%     | 3.365% 2.527%   |
Platinum − 3.946% − 5.398% − 5.757% − 3.779% − 10.129% − 3.402%
| Sugar No. 11   | 1.391% 1.825%   | 2.516% 2.576%   | 2.241% 0.843% |
| -------------- | --------------- | --------------- | ------------- |
| Silver 5000 Oz | 4.353% 3.483%   | 6.526% 4.850%   | 6.434% 6.236% |
| S&P500         | 12.820% 10.749% | 13.653% 14.471% | 4.338% 5.012% |
10Y Treasury Bond 72.047% 73.515% 73.901% 66.695% 72.817% 75.683%
Indeed, the highest Sharpe ratio that we obtain from the switching predictive regressions is
0.11 (for an investor with a modest risk aversion coefficient of 0.1 and when only macro-
economic variables are included). This is one sixth of the best Sharpe ratio that we achieve
under the weighted-regressions, which equals 0.65 (for all the investors and when the
commodity-specific factors are included). This seems to confirm our intuition that models
that outperform when statistical loss functions are applied may fail to deliver superior risk-
adjusted performances when used to produce optimal portfolio allocations.13
13 We also performed the exercises accounting for transaction costs, similarly to Sect. 5.1. The results,
which are not reported for the sake of brevity, are comparable to those discussed for the case of no transac-
tion costs.
1 3

1352 Annals of Operations Research (2021) 299:1317–1356
6 Conclusions
In this paper, we have compared the predictive power for commodity futures returns of
models based on macroeconomic variables with models augmented to include three com-
modity-specific factors that have received considerable attention in earlier work. Differ-
ently from previous papers, we concentrate almost entirely on the genuine OOS forecasting
power of a range of regressions (compared to a simple AR benchmark). Finally, we have
assessed the relative performance of the models when they are used to produce forecasts to
be employed in a mean–variance framework.
In particular, the primary objective of this paper was to assess whether commodity‐spe-
cific predictors are needed to accurately forecast commodity returns (thus supporting the
idea that commodities are an “alternative”, per‐se asset class) or instead macroeconomic
variables are sufficient (and hence commodities are similar to the rest of the asset classes).
Our analysis leads us to conclude that the relevance of commodity‐specific factors depends
on whether we use statistical or economic loss functions. Indeed, while commodity‐specific
factors do not seem to be relevant when OOS predictive accuracy measures are considered,
they become of paramount importance when we use the predictions to build recursive,
static, one‐period mean‐variance portfolios. More specifically, from the in-sample estima-
tion exercises, we conclude that neither models based on macroeconomic variables alone,
nor models which also include commodity-specific factors outperform the others. Both
types of predictive regressions lead to small adjusted R2; furthermore, all models imply the
widespread appearance of non-significant coefficients for most commodity-specific factors
as well as a majority of the macro principal components. Probably as a result of this, when
we investigate the OOS predictive accuracy of the models over the 2004–2012 period, we
find that the MAE and the RMSFE scores fail to show any marked differences across mod-
els. In fact, all types of models perform worse than the benchmarks, with exception of the
predictions generated in the low-volatility regime.
Against this background, the OOS results from the recursive portfolio allocations and
the resulting risk-adjusted performances are instead sharp: exploiting predictive regres-
sions—remarkably those from stepwise forward algorithms that go “simple to general”—
tends to generate large increases in realized Sharpe ratios. Consistently with the idea that
commodities represent a peculiar asset class, the ability to create economic value is further
enhanced when the basis, hedging pressure, and momentum are used as predictors, espe-
cially in times of quiet financial markets and low volatility. The results are even starker
when transaction costs are taken into account (and the investor has the possibility to choose
to trade only when the expected benefit exceed the rebalancing cost).
Even though they can generate economic value (and this is a notable finding that should
be of interest for money and risk managers), it remains the case that in statistical terms,
both the macroeconomic and commodity-specific factors carry limited predictive power for
commodity futures returns. A potential explanation for this empirical finding is that com-
modities are extremely heterogeneous in terms of their economic determinants, and there-
fore a unique, even if detailed, set of variables may be insufficient to capture and predict
futures contract returns. In future research, it may prove useful to investigate whether the
inclusion of commodity factors specific to each underlying, individual commodity (e.g.,
oil inventory for oil futures, temperature levels in specific areas for orange juice output,
rainfall levels in specific regions for soybean crops, etc.) may deliver further, substantial
increases in forecasting power.
1 3

Annals of Operations Research (2021) 299:1317–1356 1353
In this paper, we have adopted a pseudo-out of sample approach in that the predictor
selection methodology implemented through stepwise regressions is only performed in the
full sample and again with reference to the first date of our recursive back-testing sample
(December 2003). It would be interesting to adopt online algorithms stemming from the
theory of attribute distributed learning (a particular class of machine learning algorithms,
see Zheng et al. 2013) that sequentially takes new observations and incorporates them
immediately, simultaneously adjusting the way that the individual predictors are combined
and providing feedback to the individual predictors for them to be retrained in order to
achieve a better ensemble predictor in real time. Zheng et al. (2013) have proven that such
algorithms are particularly useful when applied to financial market prediction.
Finally, although our results show that there may exist a payoff from modelling com-
modity futures returns (selecting the corresponding linear regressions by stepwise meth-
ods), it would seem natural to explore whether other aggregate variables (possibly also
related to commodity markets) may improve the overall forecasting performance. Our set
merging Ludvigson and Ng’s (2009) with Welch and Goyal (2008) variables appears to be
rich, but richer is always possible. Moreover, while in this paper we have classified sample
dates as belonging to good and bad times and then, conditioning on that, distinguished
between regimes of low- and high-volatility, it may prove interesting to develop an inte-
grated regime switching predictive framework in which regimes and forecasting models are
specified and estimated jointly, as in Giampietro et al. (2018).
Acknowledgements We would like to thank the editors of the special issue on “Recent Developments in
Financial Modeling and Risk Management” and three anonymous referees for insightful comments and
encouragement to improve this paper.
Appendix
The first group of macroeconomic variables includes output and income series, such as
personal income, retail sales, and real consumption, taken from The Conference Board’s
Indicator (TCB), and total industrial production, extrapolated from the Global Insights
Basic Economics Database (GIBED). The second group contains labour market series.
The series of average weekly hours of production or non-support workers on private non-
farm payrolls, total employees in civilian labour force, and unemployment average duration
in weeks are taken from the database GIBED, while the source of average weekly initial
claims for unemployment insurance is TCB. The third group contains housing series. The
series of total new private housing units are taken from GIBED, while the manufacturing
and trade inventories are taken from TCB. The fourth group includes consumption, orders,
and inventories series, such as manufacturers’ new orders series and National Association
Of Purchasing Managers (NAPM) new orders index, National Association Of Purchasing
Managers (NAPM) vendor deliveries index, and National Association Of Purchasing Man-
agers (NAPM) inventories index. The fifth group includes money and credit variables. The
series of monetary base, S&P 500, commercial and industrial loans, and average effective
exchange rates of this group are taken from GIBED. To this series, we add the historical
news-based policy index and the economic policy uncertainty index. The historical news-
based policy index is a proxy of the economic policy uncertainty for the US, based on
three types of underlying components: the newspaper coverage of policy-related economic
uncertainty, the number of federal tax code provisions set to expire in future years, and
the disagreement among economic forecasters. The economic policy uncertainty index
1 3

1354 Annals of Operations Research (2021) 299:1317–1356
represents the US movements in policy-related economic uncertainty. This index indicates
that when the uncertainty increases, stock prices rise and the level of investment, employ-
ment, and country’s outcome go down.
The sixth group includes stock market series. They are S&P 500 Index and S&P 500
industrials series. We also include dividend yield (DY), earning price ratio (EP), and divi-
dend pay-out ratio (DP) of S&P 500 index. The dividends used here are the 12-month mov-
ing sums of dividends paid on the S&P 500 Index. Earning price ratio is obtained as the
log of earnings minus the log of stock prices where the earnings are the 12-month moving
sums on the S&P 500 Index. The dividend pay-out ratio is computed as the log of divi-
dends minus the log of earnings. We also consider stock return volatility (SVOL), which
is the monthly sum of the squared daily stock returns on the S&P 500 index, and book-to-
market ratio (BM), that is the ratio of the book value to market value for the Dow Jones
Industrial Average. We also take into account the net equity expansion (NTIS), which is
the ratio of the 12-month moving sums of net issues by New York Stock Exchange (NYSE)
listed stocks to the total market capitalization of NYSE stocks.
The seventh group includes bond and exchange rate series. We additionally consider
Treasury Bill Rate (TBL), which relates to the interest rate on a three-month Treasury bill,
the long-term government bond yield (LTY), the long-term return government bond (LTR)
returns, the term spread (TMS), the default yield spread (DFY), calculated as the difference
between Moody’s BAA- and AAA-rated bond yields, and the default return spread (DFR),
calculated as the difference between long-term corporate and government bond returns.
The eighth group includes prices series. They represent producer price index series,
National Association of Purchasing Managers (NAPM) commodity price index, consumer
of price index series, personal consumption expenditures series, and average hourly earn-
ings of production and nonsupervisory employees series. To these, we add the crude oil
price (COP), computed using the logarithmic changes in the nominal price of West Texas
Intermediate crude oil, provided by the Federal Reserve Bank of St. Louis.
References
Aslan, S., Yozgatligil, C., & Iyigun, C. (2018). Temporal clustering of time series via threshold autore-
gressive models: Application to commodity prices. Annals of Operations Research, 260, 51–77.
Bakshi, G., Gao, X., & Rossi, A. G. (2019). Understanding the sources of risk underlying the cross sec-
tion of commodity returns. Management Science, 65(2), 619–641.
Bessembinder, H., & Chan, K. (1992). Time-varying risk premia and forecastable returns in futures mar-
kets. Journal of Financial Economics, 32, 169–193.
Bossaerts, P., & Hillion, P. (1999). Implementing statistical criteria to select return forecasting models:
What do we learn? Review of Financial Studies, 12, 405–428.
Brennan, M. J. (1958). The supply of storage. American Economic Review, 48, 50–72.
Chong, J., & Miffre, J. (2010). Conditional correlation and volatility in commodity futures and tradi-
tional asset markets. Journal of Alternative Investments, 12, 61–75.
Dal Pra, G., Guidolin, M., Pedio, M., & Vasile, F. (2018). Regime shifts in excess stock return predict-
ability: An out-of-sample portfolio analysis. Journal of Portfolio Management, 40, 10–24.
Daskalaki, C., Kostakis, A., & Skiadopoulos, G. (2014). Are there common factors in individual com-
modity futures returns? Journal of Banking & Finance, 40, 346–363.
Daskalaki, C., & Skiadopoulos, G. (2011). Should investors include commodities in their portfolios after
all? New evidence. Journal of Banking & Finance, 35, 2606–2626.
de Roon, F. A., Nijman, T. E., & Veld, C. (2000). Hedging pressure effects in futures markets. Journal of
Finance, 55, 1437–1456.
1 3

Annals of Operations Research (2021) 299:1317–1356 1355
DeMiguel, V., Garlappi, L., & Uppal, R. (2007). Optimal versus naive diversification: How inefficient is
the 1/N portfolio strategy? Review of Financial studies, 22, 1915–1953.
Erb, C. B., & Harvey, C. R. (2006). The tactical and strategic value of commodity futures. Financial
Analysts Journal, 62, 69–97.
Fuertes, A. M., Miffre, J., & Rallis, G. (2010). Tactical allocation in commodity futures markets. Jour-
nal of Banking & Finance, 34, 2530–2540.
Gargano, A., & Timmermann, A. (2014). Forecasting commodity price indexes using macroeconomic
and financial predictors. International Journal of Forecasting, 30, 825–843.
Giampietro, M., Guidolin, M., & Pedio, M. (2018). Estimating stochastic discount factor models with
hidden regimes: Applications to commodity pricing. European Journal of Operational Research,
265, 685–702.
Gorton, G. B., Hayashi, F., & Rouwenhorst, K. G. (2012). The fundamentals of commodity futures
returns. Review of Finance, 17, 35–105.
Guidolin, M., & Timmermann, A. (2007). Asset allocation under multivariate regime switching. Journal
of Economic Dynamics and Control, 31(11), 3503–3544.
Hamilton, J. D., & Wu, J. C. (2015). Effects of index-fund investing on commodity futures prices. Inter-
national Economic Review, 56, 187–205.
Henriksen, T. E. S., Pichler, A., Westgaard, S., & Frydenberg, S. (2019). Can commodities dominate
stock and bond portfolios? Annals of Operations Research, 282(1–2), 155–177.
Hicks, J. R. (1939). Value and capital. London: Oxford Clarendon Press.
Hirshleifer, D. (1988). Residual risk, trading costs, and commodity futures risk premia. Review of Finan-
cial Studies, 1, 173–193.
Hong, H., & Yogo, M. (2012). What does futures market interest tell us about the macroeconomy and
asset prices? Journal of Financial Economics, 105, 473–490.
Irwin, S. H., & Sanders, D. R. (2011). Index funds, financialization, and commodity futures markets.
Applied Economic Perspectives and Policy, 33, 1–31.
Jensen, G., Johnson, R., & Mercer, J. (2000). Efficient use of commodity futures in diversified portfolios.
Journal of Futures Markets, 20, 489–506.
Kaldor, N. (1939). Speculation and economic stability. Review of Economic Studies, 7, 1–27.
Keynes, J. M. (1930). A Treatise on Money. London: Macmillan Press.
Lean, H., H., Nguyen, D., K., & Uddin, G. (2018). On the Role of Commodity Futures in Portfolio Diver-
sification, Working paper, Indiana University.
Ludvigson, S. C., & Ng, S. (2009). Macro factors in bond risk premia. Review of Financial Studies, 22,
5027–5067.
Narayan, P. K., Ahmed, H. A., & Narayan, S. (2015). Do momentum-based trading strategies work in the
commodity futures markets? Journal of Futures Markets, 35, 868–891.
Rapach, D. E., & Wohar, M. E. (2006). In-sample vs. out-of-sample tests of stock return predictability in
the context of data mining. Journal of Empirical Finance, 13, 231–247.
Rapach, D., E., & Zhou, G. (2013). Forecasting stock returns. In Handbook of Economic Forecasting
Vol. 2, Part A, pp. 328–383.
Sharma, M. J., & Yu, S. J. (2015). Stepwise regression data envelopment analysis for variable reduction.
Applied Mathematics and Computation, 253, 126–134.
Shen, Q., Szakmary, A. C., & Sharma, S. C. (2007). An examination of momentum strategies in com-
modity futures markets. Journal of Futures Markets, 27, 227–256.
Stock, J. H., & Watson, M. W. (2002). Forecasting using principal components from a large number of
predictors. Journal of the American Statistical Association, 97, 1167–1179.
Stock, J. H., & Watson, M. W. (2006). Forecasting with many predictors. In G. Elliott, C. Granger,
& A. Timmermann (Eds.), Handbook of economic forecasting (Vol. 1, pp. 515–554). Amsterdam:
Elsevier.
Stoll, H. R. (1979). Commodity futures and spot price determination and hedging in capital market equi-
librium. Journal of Financial and Quantitative Analysis, 14, 873–894.
Tang, K., & Xiong, W. (2012). Index investment and the financialization of commodities. Financial Ana-
lysts Journal, 68, 54–74.
Welch, I., & Goyal, A. (2008). A comprehensive look at the empirical performance of equity premium
prediction. Review of Financial Studies, 21, 1455–1508.
Yamashita, T., Yamashita, K., & Kamimura, R. (2007). A stepwise AIC method for variable selection in
linear regression. Communications in Statistics-Theory and Methods, 36(13), 2395–2403.
You, L., & Daigler, R. T. (2013). A Markowitz optimization of commodity futures portfolios. Journal of
Futures Markets, 33, 343–368.
1 3

1356 Annals of Operations Research (2021) 299:1317–1356
Zheng, H., Kulkarni, S. R., & Poor, H. V. (2013). A sequential predictor retraining algorithm and its appli-
cation to market prediction. Annals of Operations Research, 208, 209–225.
Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.
1 3