MODELING AND FORECASTING COMMODITY MARKET
VOLATILITY WITH LONG-TERM ECONOMIC AND
FINANCIAL VARIABLES
DUC KHUONG NGUYEN
THOMAS WALTHER
WORKING PAPERS ON FINANCE NO. 2018/24
INSTITUTE FOR OPERATION RESEARCH AND COMPUTATIONAL FINANCE (IOR/CF – HSG)
DECEMBER 3, 2018
Electronic copy available at: https://ssrn.com/abstract=3294967

Modeling and Forecasting Commodity Market Volatility with
(cid:73)
Long-term Economic and Financial Variables
DucKhuongNguyena,b,ThomasWaltherc,d,∗
aIPAGLab,IPAGBusinessSchool,184BoulevardSaint-Germain,75006Paris,France
bSchoolofPublicandEnvironmentalAffairs,IndianaUniversity,107SIndianaAve,Bloomington,IN47405,USA
cInstituteforOperationsResearchandComputationalFinance,UniversityofSt. Gallen,9000St.Gallen,Switzerland
dFacultyofBusinessandEconomics,TechnischeUniversita¨tDresden,01062Dresden,Germany
Abstract
This paper investigates the time-varying volatility patterns of some major commodities as well as
thepotentialfactorsthatdrivetheirlong-termvolatilitycomponent. Forthispurpose,wemakeuse
ofarecentlyproposedGARCH-MIDASapproachwhichtypicallyallowsustoexaminetheroleof
economic and financial variables of different frequencies. Using commodity futures for Crude Oil
(WTI and Brent), Gold, Silver and Platinum as well as a commodity index, our results show the
necessity of disentangling the short-term and long-term components in modeling and forecasting
commodityvolatility. Theyalsoindicatethatthelong-termvolatilityofmostcommodityfuturesis
significantly driven by the level of the global real economic activity as well as the changes in con-
sumersentiment,industrialproduction,andeconomicpolicyuncertainty. However,theforecasting
resultsarenotalikeacrosscommodityfuturesasnosinglemodelfitsallcommodities.
Keywords: Commodityfutures,GARCH,Long-termvolatility,Macroeconomiceffects,Mixed
datasampling.
JEL:C58,G17,Q02
(cid:73)Thispaperhasbeencirculatedwiththetitle“IdentifyingtheLong-termVolatilityDriversofCommodityMarkets”.
We appreciate the comments of two anonymous reviewers and the special issue editor Hans-Jo¨rg von Mettenheim
which led to an significant improvement of a previous version of this paper. We thank Paul Bui Quang, Christian
Conrad, SteffiHo¨se, StefanHuschens, LutzKilian, TonyKlein, ChristophKoser, RobinsonKruse-Becher, Hermann
Locarek-Junge, Marcel Prokopczuk, Anne Sumpf, and the participants of the 2nd Joint Seminar on Finance (2016,
TUDresden),HVBdoctoralseminar(2017,FUBerlin),the5thInternationalSymposiumonEnvironmentandEnergy
FinanceIssues(2017,Paris),the6thInternationalRuhrEnergyConference(2017,Essen),thePhDinFinanceSeminar
(2018, University of St. Gallen), the Energy Finance Workshop (2018, Stolberg), the 16th INFINITI Conference on
InternationalFinance(2018,Poznan),andthe12thRiskSymposium(2018,Dresden)foradvice,remarks,andhints.
This publication is part of SCCER CREST (Swiss Competence Center for Energy Research), which is supported
by Innosuisse (Swiss Innovation Agency). Thomas Walther is grateful for the funding received for conducting this
research.
∗Mail: thomas.walther@unisg.ch,Phone: +41(0)712242088.
WorkingPaperVersion2-December3,2018
Electronic copy available at: https://ssrn.com/abstract=3294967

1. Introduction
Earlier studies on commodity markets have shown that commodity futures can be a valuable
source of diversification benefits for investors and portfolio managers, given their distinct risk-
return characteristics as compared to traditional assets like bonds and stocks. Bodie & Rosansky
(1980) note, for example, that their benchmark portfolio of commodity futures performs as well
as the portfolio of common stocks in terms of average returns over the period 1950-1976. More
importantly, a diversified portfolio of 60% stocks and 40% commodity futures leads to a return
variabilityreductionofaboutone-thirdrelativetothe100%stockportfolio,whilehavingthesame
levelofreturn. Thehedgingabilityagainstinflationisanotherinterestingfeatureofcommodityfu-
tures(Luceyetal.,2017). Similarly,Lintner(1983)findsthatthevariabilityofportfoliosofstocks
and bonds is consistently lower when they are combined with managed commodity futures. More
recent studies such as Gorton & Rouwenhorst (2006), Arouri et al. (2011), Narayan et al. (2013),
and Klein (2017) also find evidence to confirm this diversifying potential of commodity futures
through the use of various datasets and evaluation methods. The specific drivers of commodity
returnsaswellastheirlowcorrelationswithstocksandbondscanthusbeviewedasthekeyfactors
that explain the increasing role of commodity futures in portfolio investments and diversification
strategies(Domanski&Heath,2007,Dwyeretal.,2011,Bekirosetal.,2017).
Withtheintensificationoftheirfinancializationsince2004,commoditymarketsareexposedto
some structural changes in the distributional characteristics of returns and dependence with other
assetclasses. Commodityfuturesreturnsnowbehavemorelikestockreturns,andtheircorrelation
with stocks has become positive and increased in recent years, particularly after the collapse of
Lehman Brothers (Bu¨yu¨ks¸ahin & Robe, 2011, Daskalaki & Skiadopoulos, 2011, Tang & Xiong,
2012,Bu¨yu¨ks¸ahin&Robe,2014,Adams&Glu¨ck,2015). Asaresultofthisincreasingequity-like
behavior, researchers find evidence of lower diversification benefits associated with the inclusion
of commodity futures in diversified portfolios and a higher level of their shock transmission and
volatility spillovers with stocks (Baur & McDermott, 2010, Filis et al., 2011, Narayan & Sharma,
2011,Daskalaki&Skiadopoulos,2011,Silvennoinen&Thorp,2013).
The large fluctuations of commodity prices over recent years have also generated concerns for
macroeconomicstabilityandoveralleconomicperformance. ThestandarddeviationoftheIMFall
commodity price index over the 2005M1-2017M6 is 36.45%. The same price index also reached
the highest value of 220.03 index points in July 2008 (base index of 100 points in 2005), or an
increaseof120%. Sincetheinformationaboutvolatilityisacriticalinputforportfoliodesign,risk
managementandpolicydecisions(i.e.,thevolatilitydirectlyaffectsthecross-assetcorrelationand
portfolio’srisklevel),animportantstrandofthecommodityfinanceliteraturehasdevotedattention
to commodity volatility modeling and the identification of its determinants. A general consensus
fromthemajorityofpaststudiesisthatmainvolatilitydriverstendtodifferacrossdifferentclasses
2
Electronic copy available at: https://ssrn.com/abstract=3294967

ofcommodities.
For instance, Daskalaki et al. (2014) attempt to identify common factors for the pricing of
commodities. They conclude that neither macroeconomic, equity-related, nor commodity-specific
factorscanexplainthepricingoverallcommodityclasses. Battenetal.(2010)analyzethemacroe-
conomic drivers of monthly precious metal volatility and document that monetary (e.g., inflation)
andfinancial(e.g.,S&P500returns)variablescanexplainthevolatilityblockwise,buttheirresults
do not hold for Silver. Moreover, the drivers of volatility within the group of precious metals are
not alike. Silvennoinen & Thorp (2013) analyze the correlation of commodities and find lagged
VIXtohavepositiveimpactonweeklyenergyvolatility,butnoimpactonpreciousmetals.
Regarding the energy market volatility, Pindyck (2004) document that macroeconomic vari-
ables such as treasury bill yields or effective exchange-weighted dollar rate do not affect oil price
volatilityusingweeklydata. Kilian&Vega(2011)findevidencethatWTIoilpricereturnsarenot
sensitive to macroeconomic news. Karali & Ramirez (2014) use macroeconomic variables, polit-
icalandweathereventstoidentifydriversofcrudeoil,heatingoil,andnaturalgasfuturesvolatility.
Theirresultsindicatethatonlycrudeoil’svolatilityincreasesfollowingpolitical,financial,andnat-
ural events, whereas macroeconomic variables have no significant impact on oil price volatility. A
recentstudybyYin(2016)showsthateconomicpolicyuncertaintyspillsovertooilpricespotand
futuresvolatility.
Nevertheless, several studies empirically uncover common volatility links among commodity
classes. The work of Verma (2012) shows, for example, negative influence of sentiment on the
volatility of energy and precious metal futures. Considering a sample of agricultural, energy, and
metal commodities, Karali & Power (2013) find evidence of significant influences of inflation and
industrial production on commodity markets long-term volatility. Smales (2017) documents that
the volatility of commodity markets, represented by the Commodity Research Bureau Index and
the S&P Goldman Sachs Commodity Index, react to both the U.S. and Chinese macroeconomic
news including the U.S. employment and economic output as well as the purchasing intentions of
Chinesemanufacturers. Lastly,Prokopczuketal.(2017)investigatetheco-movementofcommod-
ity market volatility and economic uncertainty via regression with realized volatility and find that
certain macroeconomic and financial variables (i.e., the inflation volatility, the VIX, the default
return spread and the TED spread) drive the monthly commodity volatility. The authors suggest to
scrutinizetheissuefurtherthroughtheframeworkproposedbyEngleetal.(2013)whichcombines
Generalized Autoregressive Heteroskedasticity (GARCH, Engle, 1982, Bollerslev, 1986) models
with the Mixed Data Sampling (MIDAS, Ghysels et al., 2004, 2007) technique. This combination
particularly allows one to use macroeconomic variables, usually available at monthly or quarterly
frequency,asexplanatoryvariablesofdailyvolatility.
The GARCH-MIDAS model has been mostly used to examine the macroeconomic effects of
3
Electronic copy available at: https://ssrn.com/abstract=3294967

equity (Asgharian et al., 2013, Conrad & Loch, 2015, Opschoor et al., 2014) and bond markets
(Nietoetal.,2015). Somestudieshavealsoemployedthismethodologytoexaminethevolatilityin
commoditymarkets. Do¨nmez&Magrini(2013)investigatepossibledriversoflong-termvolatility
ofagriculturalcommodities(wheat,corn,andsoybean). Foroilprices,Yin&Zhou(2016)andPan
etal.(2017)useGARCH-MIDASwithdemandandsupplyshocksasexplanatoryvariablesforthe
volatility. Conradetal.(2014)usemacroeconomicvariablestoexplainthedynamiccorrelationsof
stockmarketsandoilprices. Regardingcommodities,Weietal.(2017)andFangetal.(2018)show
thattheeconomicpolicyuncertaintyispositivelyassociatedwithWTIspotreturnsandGoldfutures
variance and improves forecasts. Moreover, Liu et al. (2018) use news implied volatility indices
to explain the long-term volatility of commodities. The authors present evidence that stock market
relatednewsaffectenergyandnon-energycommodities. However,newsonfinancialintermediaries
areonlyassociatedwithnon-energycommodities.
Our paper contributes to the literature on modeling and forecasting the volatility of commod-
ity markets for portfolio and risk management purposes to the extent that investors and portfolio
managers would need accurate volatility to construct diversified portfolio including commodity
assets. Going a step further, we particularly focus on the modeling and predictive ability of the
GARCH-MIDAS model, while taking into account the potential macro-economic drivers of com-
modityvolatility.
Using data of four economically-important commodity futures (Crude Oil, Gold, Silver, and
Platinum) as well as a rich set of economic and financial variables (e.g., industrial production,
consumer sentiment, economic uncertainty, implied volatility, and global real economic activity),
wefindthatthegrowthrateofindustrialproductionandconsumersentimentdecreasesvolatilityof
commodity futures. Moreover, our analysis suggests that rising economic policy uncertainty and
global real economic activity increase the long-term commodity volatility. When examining the
usefulness of GARCH-MIDAS to forecast the volatility of commodity futures, we reveal that the
inclusion of macroeconomic and financial variables in the volatility models improve the volatility
forecast, especially on longer time horizons such as 5- or 20-days ahead prediction. However,
no single model appears to be the best-suited specification for all commodity futures we consider.
Hence,inthelightofourempiricalfindings,investorswouldhavetopayaclosewatchonthetrends
in industrial production, consumer sentiment, economic policy uncertainty, and global economic
activitiesbeforemakinganytacticalportfoliorebalancingrelatedtocommodityfutures.
Theremainderofthepaperisstructuredasfollows. InSection2,weintroduceoureconometric
framework. Section 3 presents our dataset. Section 4 reports and discusses the empirical results.
Section5concludesthepaper.
4
Electronic copy available at: https://ssrn.com/abstract=3294967

2. Methodology
2.1. Spline-GARCH
The Spline-GARCH by Engle & Rangel (2008) is a multiplicative alternative to the additive
Component GARCH (Engle & Lee, 1999). The model allows one to disentangle the high and
√
low frequency parts of conditional volatility. The long-term volatility τ is described by a non-
t
parametricspline. Engle&Rangel(2008)suggesttodividethesampleinequidistantknotsk. The
Spline-GARCHcanbeformulatedasfollows:
√
|     |     | r = µ+z | τ g withz |     | ∼ t (0,1)i.i.d., |     |     | (1) |
| --- | --- | ------- | --------- | --- | ---------------- | --- | --- | --- |
|     |     | t       | t t t     | t   | ν                |     |     |     |
(cid:18) (cid:19)
ε2
t−1
|     |     | g = (1−α−β)+α |     |     | +βg | ,   |     | (2) |
| --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
|     |     | t             |     | τ   |     | t−1 |     |     |
t−1
|     |     |          | (cid:32) |          |          | (cid:33)      |     |     |
| --- | --- | -------- | -------- | -------- | -------- | ------------- | --- | --- |
|     |     |          | t        | k        | (cid:18) | t−t (cid:19)2 |     |     |
|     |     |          |          | (cid:88) |          | i             |     |     |
|     |     | τ = cexp | ω +      | ω        | max      | ,0 ,          |     | (3) |
|     |     | t        | 0        | i        |          |               |     |     |
|     |     |          | T        |          |          | T             |     |     |
i=1
V[r
where |Ω ] = τ g with Ω as the information set at time t−1 containing all past returns
| t t−1 |     | t t t−1 |     |     |     |     |     |     |
| ----- | --- | ------- | --- | --- | --- | --- | --- | --- |
r and residuals ε = (r −µ). The innovation z is an i.i.d. random variable from a Student’s t
| t   | t   | t   |     | t   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
distribution with ν degrees of freedom. The parameter µ describes the unconditional mean of the
√
return series. The process g describes the high frequency part of the conditional volatility with
t
the well known GARCH dynamics. To maintain non-negativity and weakly stationarity α,β ≥ 0
and α + β < 1. Engle & Rangel (2008) suggest to identify the optimal choice of knots by using
an information criterion such as Bayesian Information Criterion (BIC). However, we follow the
approach of Walther et al. (2017), who choose the number and positions of knots by means of the
IterativeCumulativeSumsofSquares(ICSS)variantofSanso´ etal.(2004).
2.2. GARCH-MIDAS
BasedontheSpline-GARCH,theGARCH-MIDASmodelisintroducedbyEngleetal.(2013).
It incorporates a long-term volatility component τ to a simple GARCH model (Bollerslev, 1986).
q
Thus,theconditionalvolatilityofr partlydependsonamacroeconomicvariableX withK lags.
t
√
|     |     | r = µ+z | τ g   | withz      |          | ∼ t (0,1)i.i.d., |     |     |
| --- | --- | ------- | ----- | ---------- | -------- | ---------------- | --- | --- |
|     |     | t,q     | t,q q | t,q        | t,q      | ν                |     | (4) |
|     |     |         |       | (cid:18)ε2 | (cid:19) |                  |     |     |
t−1,q
|     |     | g = (1−α−β)+α |     |     |     | +βg , |     | (5) |
| --- | --- | ------------- | --- | --- | --- | ----- | --- | --- |
|     |     | t,q           |     |     |     | t−1,q |     |     |
τ
q
|     |     |     | (cid:32) |     |     | (cid:33) |     |     |
| --- | --- | --- | -------- | --- | --- | -------- | --- | --- |
K
(cid:88)
|     |     | τ = exp | m+θ | ϕ   | (ω ,ω | )X , |     | (6) |
| --- | --- | ------- | --- | --- | ----- | ---- | --- | --- |
|     |     | q       |     | k   | 1 2   | q−k  |     |     |
k=1
|     |     |     | +1))ω1−1(1−k/(K |     |     | +1))ω2−1 |     |     |
| --- | --- | --- | --------------- | --- | --- | -------- | --- | --- |
(k/(K
|     | ϕ   | (ω ,ω ) =     |       |                 |     |          | .   | (7) |
| --- | --- | ------------- | ----- | --------------- | --- | -------- | --- | --- |
|     | k   | 1 2 (cid:80)K |       |                 |     |          |     |     |
|     |     |               | (j/(K | +1))ω1−1(1−j/(K |     | +1))ω2−1 |     |     |
j=1
5
Electronic copy available at: https://ssrn.com/abstract=3294967

The constraints α,β ≥ 0 and α +β < 1 have to hold in order to maintain the non-negativity and
stationarity of the high-frequency part g . For a further discussion on stationarity and ergodicity,
t
see Wang & Ghysels (2015). The Beta-weighting scheme ϕ (ω ,ω ) is introduced to MIDAS
k 1 2
by Ghysels et al. (2007). Dependent on the parameters ω ,ω > 1, the Beta scheme can depict
1 2
increasing, decreasing, or hump-shaped weights, which sum up to unity.1 Engle et al. (2013) also
offer the possibility to use an exponential scheme, which is not as flexible as the Beta-function
based scheme. Furthermore, Baumeister et al. (2014) consider unrestricted and equally-weighted
schemes. Due to the exponential character of the low-frequency part τ , no additional restrictions
q
for non-negativity are required. In our specification, τ stays constant for a quarter of a year q,
q
which is associated with time t. Note that if we do not include a macroeconomic variable X, the
long-termvarianceisτ = exp(m)andthemodeldegeneratestoasimpleGARCHrepresentation.
q
For the T +1 prediction of GARCH-MIDAS, we estimate the parameters from the in-sample
perioduptoT andthelastquarterQandcalculatetheforecastasfollows:
h ˆ = E[τ g |Ω ] = τ E[g |Ω ] (8)
T+1 Q T+1,Q T Q T+1,Q T
(cid:18) (cid:18)ε2 (cid:19) (cid:19)
T,Q
= τ (1−α−β)+α +βg . (9)
Q T,Q
τ
Q
The multi-step prediction T + h is conducted by recursively substituting the unknown variance
forecastuntiltimeT:
(cid:32) (cid:33)
h
(cid:88)
h ˆ = τ (1−α−β) (α+β)i +(α+β)hg . (10)
T+h Q T,Q
i=0
This technique of recursive substitution is criticized by Ederington & Guan (2010) for keeping the
same weights for all forecast horizons. Admittedly, the short-term component of the GARCH-
MIDAS model is prone to this critique. However, the long-term component is the estimate for
longer horizons. Thus, the dissipating weights of the short-term component can be neglected for
longer horizons. Another possible critique may that we apply quarterly macroeconomic variables
for short-term forecast of 1-day or 5-days ahead. Nonetheless, the latest observation of a macro-
economicvariablewillinfluencetheoverallvolatilitylevelandthusalsoaffectnear-termforecasts.
At the empirical level, we first estimate the three baseline models (i.e., the simple GARCH,
the Spline-GARCH, and the GARCH-MIDAS accommodating each of the financial and macroe-
conomic variables) over different sub-samples corresponding to different dynamics of commod-
ity prices. We then compare the forecasting performance of these models over an out-of-sample
1Here,weusetheschemepresentedinConrad&Loch(2015).
6
Electronic copy available at: https://ssrn.com/abstract=3294967

period.2
3. Data
Weconsider,inthispaper,themostimportantcommodityfuturesintherealeconomy,whichare
tradedintheNewYorkMercantileExchange(NYMEX)andtheCommodityExchange(COMEX)
and are commonly investigated in commodity finance literature. We include the WTI crude oil
index(RCLC1)3,theBrentcrudeoilindex(LLCCS00),Gold(NGCCS00),Silver(NSLCS00),and
Platinum (NPDCS00).4 In addition, we take the S&P Goldman Sachs Commodity Index (GSCI)
into consideration, which collected from Datastream as well. For all price and index series we use
the daily prices over the period from 1 January 1996 to 31 December 2015, and calculate the daily
logarithmicreturnsasr = 100·(log(P /P )).
t t t−1
Forthesetofmacroeconomicvariableswhichwillbeusedaspotentialdriversofthelong-term
commodityvolatility,weconsidertheProductPriceIndex(PPI),theIndustrialProduction(IP),the
University of Michigan Consumer Sentiment (SENTI), the overall Economic Policy Uncertainty
Index (EPUI)5, the Effective Exchange Rate for the United States (EERUS) from the Bank of
International Settlement, the bond market volatility index (MOVE), the S&P500 volatility index
(VIX),the3-monthTreasuryBillrate(TB3M),theTEDspread(TED),andtheglobalrealeconomic
activity (GREA) from Kilian (2009)6. The latter is constructed by adjusting the prices of dry bulk
cargo rates for various commodities. Given the data availability from 1 January 1992 to 1 October
2015, we calculate 95 quarterly growth rates as XM = 100·(P /P −1) for each series, except
q q q−1
the GREA, for Apr 1st 1992-Oct 1st 2015.7 For the GREA, we choose to use the variable in levels,
since it is already deflated and linearly detrended by construction. We subdivided the full sample
into three periods: (I) 1996-2005, (II) 2006-2015, and the full sample (III) 1996-2015. Table 1
reportsthedescriptivestatisticsandsomepreliminarytestsonalltimeseries.
[includeTable1abouthere]
2AllcalculationsareexercisedinMatLabR2017b. Inaddition, wearethankfultoKevinSheppardforproviding
his MFE MatLab toolbox from which we used some functions including the Model Confidence Set. The toolbox is
availablefromhttps://www.kevinsheppard.com/MFE_Toolbox.
3Thepriceseriesisretrievedfromhttps://www.eia.gov/dnav/pet/pet_pri_fut_s1_d.htm.
4ExceptforWTI,allpriceseriesareretrievedfromThompsonReutersDatastream. Thepriceseriesarecontinuous
futuresserieswhichrollovertothenearestcontractatthefirstdayofthemonth(RollmethodType0).
5Thedataisobtainedfromhttp://www.policyuncertainty.com/.
6We are grateful to Lutz Kilian for kindly providing the data for the global real economic activity with recent
updatesonhispersonalwebpagehttp://www-personal.umich.edu/˜lkilian/paperlinks.html.
7Wechoosethistimewindow, becausetheVIXisonlyavailablestarting1990. Choosing1992asastartingyear
allowsus1)havethenecessaryK =16quarterslag,i.e.fouryears,fortheGARCH-MIDASmodeland2)tocalculate
proxiesforthevarianceofallmacroeconomicvariableswhichincludesayearoftimelag.
7
Electronic copy available at: https://ssrn.com/abstract=3294967

We find that all time series are stationary, given the results of the Augmented Dickey-Fuller
(ADF)test. OnlyforGREAinthefirstsample,theADFtestdoesnotrejectthehypothesisofaunit
rootinthesample. Moreover,thedailylog-returnsofthecommoditiesexhibithighauto-correlation
ofsquaredreturnsat12lags(ARCHtest),whichsuggeststheuseofGARCHmodels.
In addition to the growth rates of the macroeconomic variables, we also include the quarterly
realizedvarianceofthecommodities,definedas
66
(cid:88)
|     | XRV = | r2    | .   | (11) |
| --- | ----- | ----- | --- | ---- |
|     | q     | t−i,q |     |      |
i=1
Moreover,weusethequarterlyvarianceofthegrowthratesofthemacroeconomicvariablesXMV
q
as explanatory variable for the long-term volatility. We estimate the variance of the quarterly mac-
roeconomicvariablesinasimilarfashionasinSchwert(1989). Inafirststep,wefilterthequarterly
growthrateswithafourth-orderAuto-Regressivemodelandfourquarterlydummyvariablestoac-
countforseasonaleffectsofthegrowthseries:
|     | 4        |          | 4        |      |
| --- | -------- | -------- | -------- | ---- |
|     | (cid:88) | (cid:88) |          |      |
| XM  | XM       |          |          |      |
|     | = φ      | +        | η D +ε . | (12) |
| q   | i        | q−i      | i i q    |      |
|     | i=1      | i=1      |          |      |
Inasecondstep,thefilteredquarterlyobservations,ε ,aresquaredandusedasanestimatorfor
q
thequarterlyvarianceofthemacroeconomicvariables:
|     | XMV | ε2. |     |      |
| --- | --- | --- | --- | ---- |
|     |     | =   |     | (13) |
|     | q   | q   |     |      |
4. ResultsandDiscussions
We now turn to our results. We divide this section into three parts. In the first subsection,
we estimate three GARCH models: the simple GARCH, the Spline-GARCH, and the GARCH-
MIDAS-RV toexaminewhetherincludingatime-varyinglong-termcomponentcanbetterexplain
thecommodityvolatility.
In the subsequent subsection, we estimate a total of 20 different models for each commodity,
i.e.weuseseparatelythequarterlygrowthratesandthequarterlyvariancesofallexplanatorymac-
roeconomicandfinancialvariablesinoursampleincombinationwithGARCH-MIDAS.Focusing
onasinglevariableintheGARCH-MIDASmodelallowsustoconcludesignificanceanddirection
ofimpactoftheexplanatoryvariables.
Lastly, we employ the GARCH-MIDAS models with quarterly growth rates of the macroeco-
nomic and financial drivers, the simple GARCH model, as well as the GARCH-MIDAS-RV and
the Spline-GARCH to forecast the volatility of our five commodities under investigation. Thus, a
8
Electronic copy available at: https://ssrn.com/abstract=3294967

totalof13modelsisincorporatedtopredictthe1-day,1-week,and1-monthaheadvolatility.
4.1. Long-termVolatilityPatterns
WestartouranalysisbyexaminingtheparameterestimationsofthesimpleGARCH,theSpline-
GARCH, and the GARCH-MIDAS-RV models with Student’s t distribution for the period from 2
January 1996 to 31 December 2015. The estimation of these models allows to straightforwardly
assess whether it is economically meaningful to decompose the commodity return volatility into
high and low frequencies. Note that the GARCH-MIDAS-RV has the quarterly realized variance
ofeachcommodityreturnasanexplanatoryvariableofitslong-termvolatility.
[includeTable2abouthere]
TheestimationresultsaregiveninTab.2. Asexpected,theGARCH-MIDAS-RV model,which
incorporates the quarterly realized variance of commodity returns, yields the best goodness-of-fit
(i.e., lowest BIC) for all commodities under consideration, except for Platinum where the Spline-
GARCH is the best-suited model. In all cases, the simple GARCH model has the worst fit, given
its low Log-Likelihood (LL). For the Spline-GARCH model, the knots are identified by means of
the ICSS approach and the results show five structural breakpoints for WTI and Brent oil indices,
sixforGold,SilverandGSCI,andonlyonebreakpointforPlatinum.
1996 1998 2000 2002 2004 2006 2008 2010 2012 2014 2016
ytilitaloV
ITW
12
√h
t
√τ t (GARCH)
10 √τ t (Spline)
√τ t (RV)
8
6
4
2
0
√ √
Figure1: Volatility( h )andlong-termvolatility( τ )ofWTIoilpricereturnswithGARCH,Spline-GARCH,and
t t
GARCH-MIDAS-RV fortheperiod1996-2015.
9
Electronic copy available at: https://ssrn.com/abstract=3294967

Tab. 2 also indicates that the short-term dynamics (i.e. α and β) of the three models are highly
significant and very similar with relatively close values. This finding thus suggests that the dif-
ferences in statistical fit (LL) and goodness-of-fit (BIC) rather arise from the long-term volatility
component. Engleetal.(2013)useavarianceratiotodeterminetheexplanatoryvalueofthelong-
term volatility. The measure VR =
V(logτt)
describes the proportion of variance of the logarithmic
V(loght)
long-term volatility and the variance of the logarithmic conditional volatility. For each GARCH-
based specification, we use the estimated conditional variance (cid:98)h of the simple GARCH model as
t
base.8 For the remaining models, we see that the long-term component of the Spline-GARCH and
theGARCH-MIDAS-RV explainsthefluctuationofthevarianceinarangebetween21%and96%.
Asanillustration,wedepict,inFig.1,thelong-termcomponentsofeachmodelfortheWTIcrude
oilvolatility. Thelong-termvolatilitypatternprovidedbytheGARCH-MIDAS-RV followsclosely
theconditionalvolatilitydynamics.
4.2. DriversofLong-termVolatility
We now turn to present and discuss the results from the GARCH-MIDAS regressions over the
three different sample periods for each commodity, whereby the long-term volatility component is
modeledasafunctionofeachofthefinancialandmacroeconomicvariables.
Beforewepresenttheregressionanalysis,wefurthertestthelegitimacyofatime-varyinglong-
termcomponentbymeansofarecentlyproposedregression-basedmisspecificationtest. Totestthe
null hypothesis of a constant long-term component (simple GARCH), Conrad & Schienle (2018)
suggesttorunthefollowinglinearregressionmodel:
logRV = a +a X +ρlogRV +ξ , (14)
q 0 1 q−1 q−1 q
where RV is the quarterly realized variance based on the daily, standardized residuals from the
q
simple GARCH model. X is the lagged, quarterly macroeconomic variable. The idea behind
q−1
the test is that the realized variance should not be predictable. Hence, if a is statistically different
1
from zero, we can reject the null hypothesis of a constant long-term component. Our results show,
that for all five commodities at least two variables are able to predict the realized variance. Thus,
some variables might not be appropriate to predict RV, but it appears the simple GARCH model
withconstantlong-termcomponentisnotcorrectlyspecified.9
Since a time-varying long-term component seems reasonable, we procede with the GARCH-
MIDAS insample regression. This analysis allows us to identify the drivers of shocks or swings
in the long-term volatility component. Without loss of generality, we solely concentrate on the
8NotethatthesimpleGARCHhasanVRofzero.Sinceitslong-termcomponentisconstantovertime,thevariance
oftheconstantlogarithmiclong-termcomponentiszero.
9ThecompleteregressionresultsaregivenintheAppendixinTable6.
10
Electronic copy available at: https://ssrn.com/abstract=3294967

interpretation of the MIDAS parameters θ, ω , and ω . The results are given in Tab. 3, where we
1 2
summarizethesignofthestatisticallysignificantparameterθ.10
[includeTable3abouthere]
TheresultsfortheWTIcrudeoilindicatethatthequarterlygrowthratesofallmacroeconomic
variableshavesignificanteffectsontheWTIlong-termvolatilityinatleastoneoutofthethreeperi-
odsweconsider,exceptPPI andTB3M.Inparticular,theconsumersentiment(SENTI)consistently
has a negative and significant impact in all three periods. Hence, when consumer sentiment rises
the oil price volatility tends to decrease, which may suggest that the economy is in its stable state.
As expected, the economic policy uncertainty (EPUI), the effective exchange rate for the United
States (EERUS), and the global real economic activity (GREA) drive up the long-term oil price
volatility. The effect of the quarterly variance of the growth rates of macroeconomic variables is
howevernotexactlysimilarasthePPI andTB3M variableshavenowsignificantimpacts. Also,the
impact of the variance of the SENTI variable on long-term oil price volatility over the full period
ispositive. AcloselookattheSENTI variableshowsthatforthefullperiod,weestimatethepara-
meters θ(cid:98) = −0.2359, ω = 1.7843, and ω = 2.8450. Hence, for a 1% increase of SENTI one
(cid:99)1 (cid:99)2
quarter before, the long-term WTI volatility decreases by exp(−0.2359·0.0549)−1 = −0.0129
or -1.29%. The highest impact is due to changes in the consumer sentiment five quarters before,
i.e. a 1% increase in consumer sentiment decreases the long-term volatility in five quarters by
exp(−0.2359·0.1094) − 1 = −0.0258 or −2.58%. Figure 2 shows the full lag structure for all
three sample periods and how it changed from the first to the second decade of the whole sample.
Inthesecondsampleperiod,theimpactofSENTI isevenbiggerthanforthefullsample. Astothe
variance of the 3-month treasury bill rate, it negatively influences the long-term WTI volatility for
allthreesampleperiods. Thus,theU.S.oilpricevolatilitydecreasesduetointerestratevariability.
ThisfindingcomplementstheobservationsofBarsky&Kilian(2002),whodocumentthatoilprice
increases(decreases)wereprecededbylow(high)interestrates.
The European Brent oil volatility shows similar patterns like its U.S. counterpart. Especially
for the second period and the full sample, we observe that the GREA level is positively associated
with the long-term oil price volatility. Hence, positive values in the global real economic activity
index lead to higher oil price fluctuations. Kilian (2009) builds the index based on dry bulk ship
cargorates. Theseratesincreaseintimesofhigheconomicactivityduetothefactthathighdemand
meets an relatively inelastic supply curve. Thus, a positive index points towards a demand shock
and an increased trading volume of commodities in general, which leads to their higher volatility.
Analogously, if the GREA has a negative index, the markets cool down given the lower demand,
10ThecompleteregressionresultsaregivenintheAppendixinTables7-24.
11
Electronic copy available at: https://ssrn.com/abstract=3294967

0
-0.005
-0.01
-0.015
-0.02
-0.025
-0.03
-0.035
2 4 6 8 10 12 14 16
Lag
egnahC
I: 1996-2005
II: 2006-2015
III: 1996-2015
Figure2: ChangeoftheconditionalvarianceofWTIduetotheimpactofconsumersentiment(SENTI)forquarterly
lagsuptoK =16.
and oil prices stabilize (less volatility). We find the GREA to be significant for all commodities
in the second sub-sample. Figure 3 shows the effects of the lagged GREA levels on the long-term
volatilityofthetwooilindicesandthethreemetals. Whilethelong-termvolatilityoftheWTIand
Brent is influenced by the GREA index from its first lag onwards, the metal volatility only reacts
five quarters after and their highest reaction is observed at the seventh lag. Interestingly, we find
thatBrentreactsonequarterquickertodemandshocksthanWTI,whichcouldbeexplainedbythe
factthattheBrentoilpriceisusedasthebenchmarkfortwo-thirdsoftheworld’soiltrades.
For the long-term volatility of Gold and Silver, we find a negative effect of the IP variable.
Industrial production generally reflects the state of the U.S. economy. Thus, an increase in the IP
growthrateswilldecreasethelong-termmetalvolatility. ThisisbecauseGoldandSilverareoften
used for hedge and/or safe-haven purposes during turbulent periods (Baur & Lucey, 2010) and are
notinvestedextensivelywhentheeconomyperformswell. WealsofindthattheEPUI growthrates
positively affect Gold’s and Platinum’s volatility whatever the sub-samples, but it is not the case
forSilver. Thisfindingsuggeststhatincreasesintheeconomicpolicyuncertaintyleadstodifferent
expectations by investors. Hence, we can support the results of Fang et al. (2018) and Wei et al.
12
Electronic copy available at: https://ssrn.com/abstract=3294967

0.012
0.01
0.008
0.006
0.004
0.002
0
2 4 6 8 10 12 14 16
Lag
egnahC
WTI
Brent
Gold
Silver
Platinum
Figure3: Changeofthelong-termconditionalvolatilityofWTI,Brent,Gold,Silver,andPlatinumduetotheimpact
ofglobalrealeconomicactivity(GREA)indexforquarterlylagsuptoK =16. Theperiodspansfrom2006-2015.
(2017),whichshowtheimportanceofEPUIforGoldandWTI,respectively.
To summarize, our findings show that the growth rates of the industrial production (IP) and
consumer sentiment (SENTI) negatively influence the long-term commodity volatility regardless
of subsample periods and commodities, whenever the associated coefficients are statistically sig-
nificant. The same result is reported in Karali & Power (2013) where changes in the industrial
productionarenegativelyassociatedwithcrudeoilandGold. Thereisalsoapositivelinkbetween
the growth rate of EPUI and the level of GREA with the long-term commodity volatility. Except
forEPUI,wecanconfirmtheseresultsfortheGSCI.Theimpactofthevarianceofmacroeconomic
variables, albeit significant, is however not consistent across commodities or subsamples. We only
find the variance of SENTI (+) and PPI (+) to be consistent with only one exception each. Both
variables confirm the assumption, that uncertainty about sentiment and inflation impacts prices,
whichistheideabehindthestandardARCHmodel(Engle,1982).
13
Electronic copy available at: https://ssrn.com/abstract=3294967

4.3. ForecastingCommodityVolatility
Whether the GARCH-MIDAS specifications with financial and macroeconomic variables are
helpfulforforecastingcommodityvolatilityisofgreatinteresttoinvestorsandportfoliomanagers.
This subsection compares their predictive ability with the one of the simple GARCH, the Spline-
models.11
GARCH,andtheGARCH-MIDAS-RV Wechooseanout-of-sampleperiodoffouryears
from3January2012to30December2015(i.e.M = 1005observations),withanexpandingtrain-
ingwindowstartingfrom2January1996. Threelossfunctionsareusedtocomparetheforecasting
performanceofthedifferentmodelsandmodelspecifications. Theyaredescribedasfollows:
(cid:118)
(cid:117) M
|        | 1 (cid:117)(cid:88)(cid:16) |             | (cid:17) |
| ------ | --------------------------- | ----------- | -------- |
| RMSE = | (cid:116)                   | h ˆ −(r −µˆ | )2 ,     |
|        |                             | i i         | i        |
M
i=1
M
1
|       | (cid:88) ˆ |         | )2|, |
| ----- | ---------- | ------- | ---- |
| MAE = | |h         | −(r −µˆ |      |
|       | M i        | i       | i    |
i=1
|         | (cid:32) |     | (cid:33) |
| ------- | -------- | --- | -------- |
|         | 1 M      | (r  | −µˆ )2   |
|         | (cid:88) | ˆ   | i i      |
| QLIKE = | logh     | +   | ,        |
|         |          | i   | ˆ        |
|         | M        |     | h        |
|         | i=1      |     | i        |
where h ˆ is the forecasted conditional variance and the squared residual (r −µˆ )2 is the proxy for
i i i
theactualvarianceattimeiintheout-of-sampleseti = 1,...,M.
Moreover, following Hansen et al. (2011), we employ the Model Confidence Set (MCS) with
10% level of significance to identify the best forecasting models and to avoid the problem of data
snooping.
[includeTable4abouthere]
The results of the variance forecast are given in Tab. 4. For oil price returns (WTI and Brent),
the Spline-GARCH yields the best variance prediction performance and is present in the MCS
of almost all loss functions over all horizons. All GARCH-MIDAS models with macroeconomic
andfinancialvariableshaverelativelyequalperformanceinforecastingtheoilpricevolatilitywith
respect to the RMSE criterion over 1- or 5-days ahead. For the other loss functions, only the
GARCH-MIDAS-GREAmodeljoinstheSpline-GARCHintheMCS,whiletheGARCH-MIDAS-
VIXmodelfortheBrentoilisalsoincludedintheMCSwithrespecttotheQLIKE.Puttingtogether
with the findings in subsection 4.2, the GREA is not only suitable for explaining the in-sample
volatility,butalsoapromisingcandidatetoconductforecastsoflong-termoilpricevolatility.
11Duetothefactthatwedonotfindconsistentpatternsforthevarianceofthesevariables,weusethegrowthrates
ofthemacroeconomicandfinancialvariablesonly.
14
Electronic copy available at: https://ssrn.com/abstract=3294967

TheresultsforGoldshowthatallcompetingmodelsbelongtothesetofequallywell-performing
models at the 1-day ahead forecast horizon with respect to the RMSE and at the 5- and 20-days
aheadforecasthorizonwithrespecttoQLIKE.OnlytheGARCH-MIDAS-TB3M modelispresent
inallMCSregardlessoftimehorizonsandlossfunctions. Thisisalittlebitsurprisinginourstudy,
because (a) it is not significant in all in-sample estimations and (b) the direction of effects is not
consistent. Its predictive power seems to suggest that it contains information about the long-term
volatility which is used as a tendency for the short-term forecasts. For instance, a rising tendency
in the TB3M could signal stock market booms and thus more stable Gold prices in the long-run
becauseGoldwillbelessusedinhedginganddiversificationstrategies.
ForSilver,theRMSEandQLIKElossfunctionsindicatethatalmostallGARCH-MIDASmod-
els with financial and macroeconomic variables, the GARCH, and the GARCH-MIDAS-RV have
equal performance at the three forecasting horizons under consideration. The MAE, on the other
hand, only identifies four out of 13 models with superior performance. The inclusion of SENTI,
EPUI, and MOVE variables into the GARCH-MIDAS models results in lower MAE for 5- and
20-days than the other specifications. Having realized volatility as explanatory variable for the
long-termvolatilityshowsbetterperformancefor1-and5-daysaheadforecasts.
The long-term volatility of Platinum appears to be harder to predict. We find the same mac-
roeconomic variables as for Silver to be included in the MCS. While the GARCH-MIDAS-SENTI
and GARCH-MIDAS-MOVE models (also simple GARCH) show good performance for 5- and
20-days horizons, the GARCH-MIDAS-EPUI and GARCH-MIDAS-RV belong to the MCS for
1-dayaheadprediction.
ThevarianceofthecommodityindexGSCIisrelativelywellpredictedbyallexplanatoryvari-
ables. OnlytheMAEindicatesthattheSpline-GARCHmaybefavourable.
The results from the variance forecasting show that no single GARCH-MIDAS specification
is able to predict the volatility better than the others, and this result holds across all commodities.
Especially, the use of the TED to predict commodity volatility is not recommended. From 54 tests
(three horizons, three loss functions, and six commodities), it is only included in 15 MCS. On the
contrary,theGARCH-MIDASmodelusingtheGREAlevelappearstohave29inclusions.
Inadditiontothevolatilityforecast,weevaluatetheValue-at-Risk(VaR)forecastperformance
of the models. For this purpose, we use the multivariate unconditional coverage test of Pe´rignon
& Smith (2008) to jointly test the coverage of p = 95%, 97.5%, and 99% VaRs. The idea of the
test is based on the hit ratio test of Kupiec (1995), which compares the empirically observed VaR
exceedance with the theoretical one. Since the test by Kupiec (1995) only compares one coverage
ratio at a time, the extension of Pe´rignon & Smith (2008) allows us to scrutinize the performance
of a specific VaR forecast at three different coverage ratios jointly. We define the coverage as the
ratio of VaR violations to the number of out-of-sample observations. The backtest compares this
15
Electronic copy available at: https://ssrn.com/abstract=3294967

numbertothetheoreticalcoverage,e.g.fora95%VaRthetheoreticalcoverageis5%.
BasedontheGARCHmodels,weestimatetheVaRasfollows:
(cid:113)
V(cid:100)aR
t,p
= µˆ
t
+ h ˆ
t
F
1
−
−
1
p
(νˆ), (15)
where F−1 (ν) is the (1 − p)-quantile function of the Student-t distribution with ν degrees of
1−p
freedom.12
[includeTable5abouthere]
10
5
0
-5
WTI returns
99% VaR
97.5% VaR
-10
95% VaR
2012 2013 2014 2015 2016
Figure4: Value-at-RiskforecastforWTI2012-2015withGARCH-MIDAS-SENTI.
The results of the VaR backtest in Table 5 can be summarized as follows. First, for the WTI
and Brent crude oil as well as for GSCI, almost all models pass the VaR test from a long trading
12In addition, we calculate the Expected Shortfall (ES) for our commodities. The ES is the expected value of the
returnswhicharelowerthantheestimatedVaR.WeusetheESbacktestbyAcerbi&Szekely(2014),whichevaluates
thenumberandthesizeofexceedancesjointly. Weincorporatealevelofconfidenceof97.5%,whichistheusuallevel
undertheBaselrequirementsBaselCommitteeonBankingSupervision(2016). Forthesakeofbrevity,ourresultsare
presentedintheAppendixTab.25. Basically,theESresultsconfirmtheimpressionoftheVaRbacktest.
16
Electronic copy available at: https://ssrn.com/abstract=3294967

position, but fail when the short trading perspective is evaluated. For the GSCI, the result may
partly be explained due to the fact that a large share of the index includes crude oil. Second, the
testrejectsmoremodelsonthelongtradingpositionsforGoldandSilver. Finally,exceptforsome
modelsat5-daysaheadVaRforecastforlongtradingpositions,allforecastingmodelsforPlatinum
fail to obtain satisfactory results. Figure 4 demonstrates the VaR forecast for WTI with GARCH-
MIDAS-SENTI, which has the least rejections over all VaR tests conducted (17 out of 36). On the
short trading positions, i.e. traders being susceptible to earn positive returns, the GARCH-MIDAS
modelwiththesentimentindexasanexplanatoryvariableisrejectedbythebacktestduetothefact
that the predictions are too conservative. For example, the 95% VaR forecast which is supposed
to have a coverage of 5% only yields 2.69% (27 exceptions). The 97.5% VaR only has 0.90% (9
exceptions) and the 99% VaR only has a coverage of 0.02% (2 exceptions), where 2.5% and 1%
arerequired,respectively.13 SincethemodelfailstoprovideasufficientestimateoftheVaRatany
quantile,itisrejectedbythePe´rignon&Smith(2008)test. ModelsthatyieldtooconservativeVaR
estimatesarecostlyintermsofcapitalrequirementsofbanksorVaR-limitsoftraders. However,as
mentioned above, the VaR estimates for the long trading position pass the test. Here, the coverage
ofthe95%VaRis5.57%(56exceptions).
In order to check for robustness of our in-sample and out-of-sample results, we check for sev-
eral different settings of our models. First, we change the number of lags K, i.e. how many past
quartersinformationofmacroeconomicvariablesareused. Second,weuselogarithmicdifferences
of the macroeconomic variables instead of growth rates. Third, we attempt to incorporate the first
principal component of all macroeconomic and financial variables. Fourth, instead of using the
Student-t distribution for the innovations z , we evaluated our results assuming a Normal distribu-
t
tion. Finally, we change the frequency of our explanatory variable, which we use at a quarterly
rate,tomonthlygrowthratestoexplainthelong-termvolatilityofdailycommodityreturns. Forall
mentionedrobustnesschecks,theresultsremainqualitativelyintact.
5. Conclusion
The motivation of this paper was to identify the potential drivers of the long-term volatility
of commodity prices through the GARCH-MIDAS class model, at both modeling and forecasting
levels. We conduct our empirical investigation in three steps including the in-sample estimation,
the identification of the long-term commodity volatility drivers, and the out-of-sample volatility
forecasting. In the first step, we show that disentangling long-term and short-term volatility of
13TheexceptionscanbecountedbythedotsinFig.4. Forthe95%VaRthesumofallyellow,green,andreddots
isthenumberofexceptionsforeachtradingposition. Forthe97.5%VaR,onehastosumtheyellowandthereddots.
Forthe99%VaR,thenumberofexceptionsisgivenbythesumofthereddotsonly.
17
Electronic copy available at: https://ssrn.com/abstract=3294967

commodityfuturesleadstoabetterin-samplefitbymeansoftheSpline-GARCHandtheGARCH-
MIDASmodelswithcommodity’srealizedvolatility.
Inthesecondstep,weemploytheGARCH-MIDASframeworktoexaminewhethereachofthe
financialandmacroeconomicvariablesinourstudymattersforthelong-termcommodityvolatility.
Wefindthatthelong-termcommodityvolatilityisnegativelyinfluencedbythegrowthratesofthe
consumersentimentandtheindustrialproduction,butpositivelybythegrowthrateoftheeconomic
policy uncertainty and the level of the general real economic activity. We also investigate whether
the variance of these financial and macroeconomic variables inhibits any information for the long-
termcommodityvolatility,butwedonotfindanyconsistentresultsacrosscommodityfutures.
ThelastpartofthepaperusestheGARCH-MIDASwithfinancialandmacroeconomicvariables
toforecastthevolatilityofcommoditiesoverthe1-,5-,and20-daysaheadhorizons. Itisimportant
to stress that the consistent results for in-sample estimations are not translated into forecasting
performance. Thus, we find different best-suited models for each commodity. For example, the
oil price volatility is best predicted with either Spline-GARCH or the GARCH-MIDAS-GREA.
For Gold, the GARCH-MIDAS-TB3M is recommended for forecasting the volatility at the 1-, 5-
, and 20-days ahead forecasts. For Silver and Platinum, we find the GARCH-MIDAS-SENTI,
the GARCH-MIDAS-EPUI, the GARCH-MIDAS-MOVE, and the GARCH-MIDAS-RV to have
equally well results. At the same time, our forecasting results show, from a risk management
perspective, that the inclusion of financial and macroeconomic variables in the volatility models
doesnotleadtobetterValue-at-RiskpredictionsthanthesimpleGARCHmodel.
Thefindingsofourpapercanbeimprovedbypotentiallyconsideringtheasymmetriceffectsof
financial and macroeconomic variables. For instance, Verma (2012) and Bahloul & Bouri (2016)
reportvolatilityasymmetricresponsesintimesofbullishandbearishmarkets. Moreover,thefore-
castabilityofGARCH-MIDASmodelsmightbeimprovedbymodelaveraging.
18
Electronic copy available at: https://ssrn.com/abstract=3294967

References
Acerbi,C.,&Szekely,B.(2014). BacktestingExpectedShortfall. RiskMagazine,(pp.76–81).
Adams,Z.,&Glu¨ck,T.(2015). Financializationincommoditymarkets: Apassingtrendorthenew
normal? Journal of Banking & Finance, 60, 93–111. doi:10.1016/j.jbankfin.2015.
07.008.
Arouri, M. E. H., Jouini, J., & Nguyen, D. K. (2011). Volatility spillovers between oil prices and
stock sector returns: Implications for portfolio management. Journal of International Money
andFinance,30,1387–1405.doi:10.1016/j.jimonfin.2011.07.008.
Asgharian, H., Hou, A. J., & Javed, F. (2013). The importance of the macroeconomic variables
in forecasting stock return variance: A GARCH-MIDAS approach. Journal of Forecasting, 32,
600–612.doi:10.1002/for.2256.
Bahloul, W., & Bouri, A. (2016). The impact of investor sentiment on returns and conditional
volatilityinU.S.futuresmarkets. JournalofMultinationalFinancialManagement,36,89–102.
doi:10.1016/j.mulfin.2016.07.003.
Barsky, R., & Kilian, L. (2002). Do We Really Know that Oil Caused the Great Stagflation? A
Monetary Alternative. In B.S. Bernake, &K. S. Rogoff (Eds.),NBER MacroeconomicsAnnual
2001(pp.137–183). volume16.
Basel Committee on Banking Supervision (2016). Minimum capital requirements for market risk.
TechnicalReportJanuary2016. URL:www.bis.org/bcbs/publ/d352.pdf.
Batten, J. A., Ciner, C., & Lucey, B. M. (2010). The macroeconomic determinants of volatility in
preciousmetalsmarkets. ResourcesPolicy,35,65–71.doi:10.1016/j.resourpol.2009.
12.002.
Baumeister, C., Gue´rin, P., & Kilian, L. (2014). Do high-frequency financial data help forecast
oil prices? The MIDAS touch at work. International Journal of Forecasting, 31, 238–252.
doi:10.1016/j.ijforecast.2014.06.005.
Baur, D. G., & Lucey, B. M. (2010). Is Gold a Hedge or a Safe Haven? An Analysis of Stocks,
Bonds and Gold. Financial Review, 45, 217–229. doi:10.1111/j.1540-6288.2010.
00244.x.
Baur, D. G., & McDermott, T. K. (2010). Is gold a safe haven? International evidence. Journal of
Banking&Finance,34,1886–1898.doi:10.1016/j.jbankfin.2009.12.008.
19
Electronic copy available at: https://ssrn.com/abstract=3294967

Bekiros, S., Nguyen, D. K., Sandoval Junior, L., & Uddin, G. S. (2017). Information diffu-
sion, cluster formation and entropy-based network dynamics in equity and commodity markets.
European Journal of Operational Research, 256, 945–961. doi:10.1016/j.ejor.2016.
06.052.
Bodie, Z., & Rosansky, V. I. (1980). Risk and Return in Commodity Futures. Financial Analysts
Journal,36,27–39.doi:10.2469/faj.v36.n3.27.
Bollerslev, T. (1986). Generalized autoregressive conditional heteroskedasticity. Journal of Eco-
nometrics,31,307–327.doi:10.1016/0304-4076(86)90063-1.
Bu¨yu¨ks¸ahin, B., & Robe, M. A. (2011). Does ’Paper Oil’ Matter? Energy Markets’ Financializa-
tion and Equity-Commodity Co-Movements. URL: http://www.ssrn.com/abstract=
1855264.
Bu¨yu¨ks¸ahin, B., & Robe, M. A. (2014). Speculators, commodities and cross-market linkages.
JournalofInternationalMoneyandFinance,42,38–70.doi:10.1016/j.jimonfin.2013.
08.004.
Conrad, C., & Loch, K. (2015). Anticipating Long-Term Stock Market Volatility. Journal of
AppliedEconometrics,30,1090–1114.doi:10.1002/jae.2404.
Conrad, C., Loch, K., & Rittler, D. (2014). On the macroeconomic determinants of long-term
volatilities and correlations in U.S. stock and crude oil markets. Journal of Empirical Finance,
29,26–40.doi:10.1016/j.jempfin.2014.03.009.
Conrad, C., & Schienle, M. (2018). Testing for an Omitted Multiplicative Long-Term Component
in GARCH Models. Journal of Business & Economic Statistics, 0015, 1–14. doi:10.1080/
07350015.2018.1482759.
Daskalaki, C., Kostakis, A., & Skiadopoulos, G. (2014). Are there common factors in individual
commodity futures returns? Journal of Banking and Finance, 40, 346–363. doi:10.1016/j.
jbankfin.2013.11.034.
Daskalaki,C.,&Skiadopoulos,G.(2011). Shouldinvestorsincludecommoditiesintheirportfolios
after all? New evidence. Journal of Banking and Finance, 35, 2606–2626. doi:10.1016/j.
jbankfin.2011.02.022.
Domanski, D., & Heath, A. (2007). Financial investors and commodity markets. BIS Quarterly
Review,(pp.53–67).
20
Electronic copy available at: https://ssrn.com/abstract=3294967

Do¨nmez, A., & Magrini, E. (2013). Agricultural Commodity Price Volatility and Its Macroeco-
nomic Determinants. Technical Report EUR 26183 EN Joint Research Centre Luxembourg.
doi:10.2791/23669.
Dwyer, A., Gardner, G., & Williams, T. (2011). Global Commodity Markets – Price Volatility and
Financialisation. Bulletin,(pp.49–58).
Ederington, L. H., & Guan, W. (2010). Longer-term time-series volatility forecasts. Journal of
FinancialandQuantitativeAnalysis,45,1055–1076.doi:10.1017/S0022109010000372.
Engle,R. F.(1982). Autoregressive ConditionalHeteroscedasticitywith Estimatesof theVariance
ofUnitedKingdomInflation. Econometrica,50,987–1007.doi:10.2307/1912773.
Engle, R. F., Ghysels, E., & Sohn, B. (2013). Stock Market Volatility and Macroeconomic Funda-
mentals. ReviewofEconomicsandStatistics,95,776–797.
Engle,R.F.,&Lee,G.(1999). Along-runandshort-runcomponentmodelofstockreturnvolatil-
ity. In R. Engle, & H. White (Eds.), Cointegration, Causality, and Forecasting: A Festschrift in
HonourofCliveW.J.Granger (pp.475–497). Oxford: OxfordUniversityPress.
Engle, R. F., & Rangel, J. G. (2008). The spline-GARCH model for low-frequency volatility and
its global macroeconomic causes. Review of Financial Studies, 21, 1187–1222. doi:10.1093/
rfs/hhn004.
Fang, L., Chen, B., Yu, H., & Qian, Y. (2018). The importance of global economic policy un-
certainty in predicting gold futures market volatility: A GARCH-MIDAS approach. Journal of
FuturesMarkets,38,413–422.doi:10.1002/fut.21897.
Filis, G., Degiannakis, S., & Floros, C. (2011). Dynamic correlation between stock market and oil
prices: The caseofoil-importingandoil-exporting countries. InternationalReviewof Financial
Analysis,20,152–164.doi:10.1016/j.irfa.2011.02.014.
Ghysels, E., Santa-Clara, P., & Valkanov, R. (2004). The MIDAS Touch: Mixed Data Sampling
RegressionModels. CIRANOWorkingPapers,20,1–33.
Ghysels, E., Sinko, A., & Valkanov, R. (2007). MIDAS Regressions: Further Results and New
Directions. EconometricReviews,26,53–90.doi:10.1080/07474930600972467.
Gorton, G., & Rouwenhorst, K. G. (2006). Facts and Fantasies about Commodity Futures. Finan-
cialAnalystsJournal,62,47–68.doi:10.3386/w10595.
21
Electronic copy available at: https://ssrn.com/abstract=3294967

Hansen, P. R., Lunde, A., & Nason, J. M. (2011). The Model Confidence Set. Econometrica, 79,
453–497.doi:10.3982/ECTA5771.
Karali,B.,&Power,G.J.(2013). Short-andlong-rundeterminantsofcommoditypricevolatility.
AmericanJournalofAgriculturalEconomics,95,724–738.doi:10.1093/ajae/aas122.
Karali, B., & Ramirez, O. A. (2014). Macro determinants of volatility and volatility spillover in
energymarkets. EnergyEconomics,46,413–421.doi:10.1016/j.eneco.2014.06.004.
Kilian,L.(2009). NotAllOilPriceShocksAreAlike: DisentanglingDemandandSupplyShocks
in the Crude Oil Market. American Economic Review, 99, 1053–1069. doi:10.1257/aer.
99.3.1053.
Kilian, L., & Vega, C. (2011). Do Energy Prices Respond to U.S. Macroeconomic News? A Test
of the Hypothesis of Predetermined Energy Prices. Review of Economics and Statistics, 93,
660–671.doi:10.1162/REST{\_}a{\_}00086.
Klein, T. (2017). Dynamic Correlation of Precious Metals and Flight-to-Quality in Developed
Markets. FinanceResearchLetters,23,283–290.doi:10.1016/j.frl.2017.05.002.
Kupiec, P. H. (1995). Techniques for Verifying the Accuracy of Risk Measurement Models. The
JournalofDerivatives,3,73–84.doi:10.3905/jod.1995.407942.
Lintner, J. V. (1983). The potential role of managed commodity-financial futures accounts (and/or
funds) in portfolios of stocks and bonds. Division of Research, Graduate School of Business
Administration,HarvardUniversity.
Liu, Y., Han, L., & Yin, L. (2018). Does news uncertainty matter for commodity futures markets?
Heterogeneity in energy and non-energy sectors. Journal of Futures Markets, 38, 1246–1261.
doi:10.1002/fut.21916.
Lucey, B. M., Sharma, S. S., & Vigne, S. A. (2017). Gold and inflation(s) – A time-varying
relationship. EconomicModelling,67,88–101.doi:10.1016/j.econmod.2016.10.008.
Narayan,P.K.,Narayan,S.,&Sharma,S.S.(2013).Ananalysisofcommoditymarkets: Whatgain
for investors? Journal of Banking & Finance, 37, 3878–3889. doi:10.1016/j.jbankfin.
2013.07.009.
Narayan, P. K., & Sharma, S. S. (2011). New evidence on oil price and firm returns. Journal of
BankingandFinance,35,3253–3262.doi:10.1016/j.jbankfin.2011.05.010.
22
Electronic copy available at: https://ssrn.com/abstract=3294967

Nieto, B., Novales, A., & Rubio, G. (2015). Macroeconomic and Financial Determinants of the
Volatility of Corporate Bond Returns. Quarterly Journal of Finance, 05, 1550021. doi:10.
1142/S2010139215500214.
Opschoor, A., van Dijk, D., & van der Wel, M. (2014). Predicting volatility and correlations with
Financial Conditions Indexes. Journal of Empirical Finance, 29, 435–447. doi:10.1016/j.
jempfin.2014.10.003.
Pan, Z., Wang, Y., Wu, C., & Yin, L. (2017). Oil price volatility and macroeconomic fundament-
als: A regime switching GARCH-MIDAS model. Journal of Empirical Finance, 43, 130–142.
doi:10.1016/j.jempfin.2017.06.005.
Pe´rignon, C., & Smith, D. R. (2008). A New Approach to Comparing VaR Estimation Methods.
TheJournalofDerivatives,16,54–66.doi:10.3905/JOD.2008.16.2.054.
Pindyck, R. S. (2004). Volatility and commodity price dynamics. Journal of Futures Markets, 24,
1029–1047.doi:10.1002/fut.20120.
Prokopczuk, M., Stancu, A., & Symeonidis, L. (2017). The economic drivers of time-varying
commoditymarketvolatility. URL:https://papers.ssrn.com/sol3/papers.cfm?
abstract_id=2678883.
Sanso´, A., Arago´, V., & Carrion, J. (2004). Testing for changes in the unconditional variance of
financialtimeseries. RevistadeEconom´ıafinanciera,4,32–53.
Schwert, G. W. (1989). Why Does Stock Market Volatility Change Over Time? The Journal of
Finance,44,1115–1153.doi:10.1111/j.1540-6261.1989.tb02647.x.
Silvennoinen,A.,&Thorp,S.(2013).Financialization,crisisandcommoditycorrelationdynamics.
Journal of International Financial Markets, Institutions and Money, 24, 42–65. doi:10.1016/
j.intfin.2012.11.007.
Smales,L.A.(2017). CommoditymarketvolatilityinthepresenceofU.S.andChinesemacroeco-
nomicnews. JournalofCommodityMarkets,7,15–27.doi:10.1016/j.jcomm.2017.06.
002.
Tang,K.,&Xiong,W.(2012). IndexInvestmentandtheFinancializationofCommodities. Finan-
cialAnalystsJournal,68,54–74.doi:10.2469/faj.v68.n6.5.
Verma, R. (2012). Behavioral Finance and Pricing of Derivatives: Implications for Dodd-Frank
Act. ReviewofFuturesMarkets,20,21–67.
23
Electronic copy available at: https://ssrn.com/abstract=3294967

Walther, T., Klein, T., Pham Thu, H., & Piontek, K. (2017). True or spurious long memory in
European Non-EMU currencies. Research in International Business and Finance, 40C, 217–
230.doi:10.1016/j.ribaf.2017.01.003.
Wang, F., & Ghysels, E. (2015). Econometric Analysis of Volatility Component Models. Econo-
metricTheory,31,362–393.doi:10.1017/S0266466614000334.
Wei, Y., Liu, J., Lai, X., & Hu, Y. (2017). Which determinant is the most informative in fore-
casting crude oil market volatility: Fundamental, speculation, or uncertainty? Energy Eco-
nomics, 68, 141–150. URL: https://doi.org/10.1016/j.eneco.2017.09.016.
doi:10.1016/j.eneco.2017.09.016.
Yin, L. (2016). Does oil price respond to macroeconomic uncertainty? New evidence. Empirical
Economics,51,921–938.doi:10.1007/s00181-015-1027-7.
Yin, L., & Zhou, Y. (2016). What Drives Long-term Oil Market Volatility? Fundamentals versus
Speculation. Economics: The Open-Access, Open-Assessment E-Journal, 10, 1–26. doi:10.
5018/economics-ejournal.ja.2016-20.
24
Electronic copy available at: https://ssrn.com/abstract=3294967

T Mean Min. Max. Stand.Dev. Skewness Kurtosis LB(12) ARCH(12) ADF
Commodities(dailyreturns)
Jan1st1996-Dec30th2005
64.4502∗∗∗ -49.6648∗∗∗
| WTI 2501 | 0.0492 -12.1607 | 11.6594 | 1.9820 | -0.2029 5.2754 | 15.7446 |     |
| -------- | --------------- | ------- | ------ | -------------- | ------- | --- |
Brent 2610 0.0448 -14.4372 12.8982 2.2517 -0.2308 5.4517 9.7797 50.7701∗∗∗ -52.9709∗∗∗
|           |                |        |        |                |         | 112.6825∗∗∗ -51.0886∗∗∗ |
| --------- | -------------- | ------ | ------ | -------------- | ------- | ----------------------- |
| Gold 2610 | 0.0110 -5.1049 | 8.8872 | 0.8800 | 0.6539 12.7778 | 17.1831 |                         |
Silver 2610 0.0205 -11.8323 7.6612 1.4473 -0.4294 8.3490 23.0132∗∗ 175.5339∗∗∗ -51.0985∗∗∗
Platinum 2610 0.0342 -14.4173 18.6781 1.3806 1.1136 30.8952 30.6490∗∗∗ 12.0356 -52.0306∗∗∗
67.5175∗∗∗ -51.7882∗∗∗
| GSCI 2610 | 0.0350 -9.1695 | 6.5670 | 1.3058 | -0.1160 4.8398 | 9.4775 |     |
| --------- | -------------- | ------ | ------ | -------------- | ------ | --- |
Jan2nd2006-Dec31st2015
WTI 2514 -0.0199 -10.5782 12.1150 2.1369 -0.1592 6.2928 21.3814∗∗ 452.5556∗∗∗ -53.5608∗∗∗
Brent 2609 -0.0176 -10.9455 12.7066 2.0985 -0.0683 6.8232 51.0998∗∗∗ 592.7609∗∗∗ -54.3737∗∗∗
|           |                |        |        |                | 27.4426∗∗∗ | 130.4636∗∗∗ -51.0980∗∗∗ |
| --------- | -------------- | ------ | ------ | -------------- | ---------- | ----------------------- |
| Gold 2609 | 0.0275 -9.8206 | 8.6250 | 1.2635 | -0.3727 8.0461 |            |                         |
Silver 2609 0.0171 -19.5185 12.3585 2.2741 -0.8740 9.2652 14.8882 141.0550∗∗∗ -52.5413∗∗∗
Platinum 2609 -0.0033 -9.6033 16.0210 1.5176 -0.0922 11.2790 15.7196 164.1283∗∗∗ -48.1499∗∗∗
|           |                 |        |        |                | 20.0830∗ | 477.3502∗∗∗ -53.0929∗∗∗ |
| --------- | --------------- | ------ | ------ | -------------- | -------- | ----------------------- |
| GSCI 2609 | -0.0428 -8.6486 | 7.2159 | 1.4950 | -0.3046 6.3860 |          |                         |
Jan1st1996-Dec31st2015
WTI 5015 0.0146 -12.1607 12.1150 2.0612 -0.1826 5.8927 17.6758 527.7097∗∗∗ -73.1878∗∗∗
Brent 5219 0.0136 -14.4372 12.8982 2.1765 -0.1553 6.0644 32.4483∗∗∗ 535.3568∗∗∗ -75.8587∗∗∗
|           |                |        |        |                 | 33.3773∗∗∗ | 269.7001∗∗∗ -72.2897∗∗∗ |
| --------- | -------------- | ------ | ------ | --------------- | ---------- | ----------------------- |
| Gold 5219 | 0.0193 -9.8206 | 8.8872 | 1.0887 | -0.1107 10.0088 |            |                         |
Silver 5219 0.0188 -19.5185 12.3585 1.9058 -0.8372 10.7768 17.0178 341.2088∗∗∗ -73.7414∗∗∗
|               |                 |         |        |                | 19.3300∗ | 84.9298∗∗∗ -70.5618∗∗∗ |
| ------------- | --------------- | ------- | ------ | -------------- | -------- | ---------------------- |
| Platinum 5219 | 0.0154 -14.4173 | 18.6781 | 1.4507 | 0.4234 19.4480 |          |                        |
GSCI 5219 -0.0039 -9.1695 7.2159 1.4040 -0.2416 5.9329 16.2624 655.5203∗∗∗ -74.3136∗∗∗
MacroeconomicVariables(monthlygrowthrates)
Apr1st1992-Oct1st2005
|        |                |        |        |               | 318.2274∗∗∗ | 50.1899∗∗∗ -3.6043∗∗∗ |
| ------ | -------------- | ------ | ------ | ------------- | ----------- | --------------------- |
| PPI 55 | 0.6694 -0.3376 | 2.0451 | 0.4754 | 0.6912 3.7751 |             |                       |
IP 55 0.8200 -1.8292 2.8383 0.9645 -0.3809 3.1006 35.2119∗∗∗ 14.3579 -3.2424∗∗∗
SENTI 55 0.4590 -23.1088 21.8281 7.6340 0.0805 4.2131 41.7492∗∗∗ 32.1541∗∗∗ -9.3907∗∗∗
|         |                 |         |         |               | 39.2926∗∗∗ | -11.0963∗∗∗ |
| ------- | --------------- | ------- | ------- | ------------- | ---------- | ----------- |
| EPUI 55 | 1.7363 -38.8710 | 69.5293 | 22.3375 | 0.4208 3.1595 |            | 17.0294     |
EERUS 55 0.0478 -6.9507 6.1370 3.0024 -0.2221 2.6952 21.6967∗∗ 17.2949 -7.0971∗∗∗
|         |                 |         |         |               | 21.9241∗∗ | -10.0174∗∗∗ |
| ------- | --------------- | ------- | ------- | ------------- | --------- | ----------- |
| MOVE 55 | 1.3843 -29.3532 | 63.6364 | 18.5001 | 1.0442 4.1247 |           | 9.1196      |
VIX 55 2.3680 -40.3663 107.7626 28.2879 1.5510 5.8957 35.4489∗∗∗ 11.1852 -10.2729∗∗∗
TB3M 55 1.0094 -38.4615 41.4894 14.5236 0.1139 4.0666 87.7110∗∗∗ 33.2890∗∗∗ -3.5105∗∗∗
|        |                 |         |         |               | 31.6456∗∗∗ | 33.4887∗∗∗ -8.9898∗∗∗ |
| ------ | --------------- | ------- | ------- | ------------- | ---------- | --------------------- |
| TED 55 | 6.2467 -60.2941 | 86.1111 | 34.0892 | 0.4774 2.6466 |            |                       |
GREA 55 -0.4675 -31.9724 50.0013 20.8700 0.8223 3.0898 164.7693∗∗∗ 48.2137∗∗∗ -1.4067
Apr1st2002-Oct1st2015
PPI 55 0.5419 -2.5072 2.3931 0.9436 -0.5981 4.1356 40.2087∗∗∗ 15.1128 -5.9474∗∗∗
|       |                |        |        |                 | 45.8746∗∗∗ | 32.7200∗∗∗ -3.2404∗∗∗ |
| ----- | -------------- | ------ | ------ | --------------- | ---------- | --------------------- |
| IP 55 | 0.2587 -6.3991 | 2.2055 | 1.4753 | -2.5494 11.3393 |            |                       |
SENTI 55 0.3614 -23.1088 23.3553 9.2580 0.1338 3.3880 33.7638∗∗∗ 5.9681 -10.0613∗∗∗
EPUI -9.1542∗∗∗
| 55  | 2.6112 -45.3283 | 81.8613 | 25.4964 | 1.0549 4.3691 | 18.0936 | 11.2170 |
| --- | --------------- | ------- | ------- | ------------- | ------- | ------- |
EERUS 55 -0.2340 -7.9567 7.5602 3.5305 0.1185 2.6679 34.7111∗∗∗ 17.9774 -5.5318∗∗∗
MOVE 55 0.8816 -38.2632 74.1710 20.6668 1.4848 5.8719 8.3091 11.6003 -8.3127∗∗∗
30.7492∗∗∗ -8.8370∗∗∗
| VIX 55 | 4.4193 -45.5307 | 160.0484 | 34.2312 | 2.1021 9.7139 |     | 8.4924 |
| ------ | --------------- | -------- | ------- | ------------- | --- | ------ |
TB3M 55 0.8119 -80.5970 166.6667 43.9323 1.7308 8.3431 12.7389 18.4377 -6.4236∗∗∗
TED 55 10.6581 -63.4146 246.1538 52.2457 2.2308 10.1778 18.6416∗ 13.1449 -8.8564∗∗∗
GREA 55 14.6714 -52.8075 64.3385 30.4095 -0.3424 2.1175 155.1052∗∗∗ 49.8877∗∗∗ -2.1508∗∗
Apr1st1992-Oct1st2015
PPI 95 0.5767 -2.5072 2.3931 0.7532 -0.7862 6.0136 70.8559∗∗∗ 28.7945∗∗∗ -6.8992∗∗∗
IP 95 0.5351 -6.3991 2.8383 1.3503 -2.2119 11.4121 60.7998∗∗∗ 42.0781∗∗∗ -4.2607∗∗∗
|          |                 |         |        |               | 38.7771∗∗∗ | -12.9977∗∗∗ |
| -------- | --------------- | ------- | ------ | ------------- | ---------- | ----------- |
| SENTI 95 | 0.6426 -23.1088 | 23.3553 | 8.3201 | 0.2527 3.7418 |            | 8.6220      |
EPUI 95 2.7076 -45.3283 81.8613 24.7079 0.8304 3.8843 25.0137∗∗ 12.1545 -13.2026∗∗∗
23.7173∗∗ -8.0968∗∗∗
| EERUS 95 | 0.1405 -7.9567 | 7.5602 | 3.2155 | -0.0054 2.7492 |     | 15.9138 |
| -------- | -------------- | ------ | ------ | -------------- | --- | ------- |
MOVE 95 1.8373 -38.2632 74.1710 20.5543 1.1986 4.7469 14.3955 9.1704 -12.0629∗∗∗
VIX 95 4.2099 -45.5307 160.0484 32.1412 1.9710 8.8980 36.8007∗∗∗ 8.0812 -12.6911∗∗∗
30.7764∗∗∗ -8.4102∗∗∗
| TB3M 95 | -0.0771 -80.5970 | 166.6667 | 34.1781 | 2.1582 13.2354 | 18.4462 |     |
| ------- | ---------------- | -------- | ------- | -------------- | ------- | --- |
TED 95 7.8327 -63.4146 246.1538 45.9179 2.0660 10.5898 28.4977∗∗∗ 19.9667∗ -11.7807∗∗∗
|         |                 |         |         |               | 309.0392∗∗∗ | 81.8343∗∗∗ -2.8191∗∗∗ |
| ------- | --------------- | ------- | ------- | ------------- | ----------- | --------------------- |
| GREA 95 | 4.8672 -52.8075 | 64.3385 | 26.9702 | 0.3593 2.3448 |             |                       |
Table1: Descriptivestatisticsofcommodityreturnsandgrowthratesofmacroeconomicvariables.
Note: Rejectionoftherespectivehypothesisat1%,5%and10%ismarkedby∗∗∗,∗∗,and∗,respectively. LB(12)and
ARCH(12)aretheLjung-BoxandARCHtestat12lagsauto-correlationofreturnsandsquaredreturns. ADFisthe
AugmentedDickey-Fullertestforstationarity.
25
Electronic copy available at: https://ssrn.com/abstract=3294967

|           |       |       | µ      | α         | β         | ν         |              |     |
| --------- | ----- | ----- | ------ | --------- | --------- | --------- | ------------ | --- |
| Commodity | Model | knots |        |           |           |           | LL BIC       | VR  |
|           |       |       |        | 0.0396∗∗∗ | 0.9559∗∗∗ | 8.2406∗∗∗ |              |     |
|           | GARCH | –     | 0.0439 |           |           |           | -10251 20545 | –   |
WTI Spline 5 0.0455 0.0398∗∗∗ 0.9478∗∗∗ 8.0593∗∗∗ -10240 20573 0.4983
|       | RV     |     | 0.0434∗∗∗ | 0.0414∗∗∗ | 0.9338∗∗∗ | 8.9963∗∗∗ |              |        |
| ----- | ------ | --- | --------- | --------- | --------- | --------- | ------------ | ------ |
|       |        | –   |           |           |           |           | -10222 20513 | 0.7782 |
|       | GARCH  | –   | 0.0391∗   | 0.0413∗∗∗ | 0.9560∗∗∗ | 7.0635∗∗∗ | -10893 21828 | –      |
|       |        |     |           | 0.0432∗∗∗ | 0.9424∗∗∗ | 6.9465∗∗∗ |              |        |
| Brent | Spline | 5   | 0.0409    |           |           |           | -10878 21851 | 0.5524 |
RV – 0.0398∗ 0.0425∗∗∗ 0.9437∗∗∗ 7.3761∗∗∗ -10869 21806 0.6319
|     |       |     |        | 0.0399∗∗∗ | 0.9578∗∗∗ | 4.5391∗∗∗ |             |     |
| --- | ----- | --- | ------ | --------- | --------- | --------- | ----------- | --- |
|     | GARCH | –   | 0.0111 |           |           |           | -7000 14043 | –   |
Gold Spline 6 0.0092 0.0469∗∗∗ 0.9459∗∗∗ 3.9893∗∗∗ -6980 14063 0.7281
RV – 0.0126∗ 0.0467∗∗∗ 0.9443∗∗∗ 4.2017∗∗∗ -6973 14015 0.7653
GARCH – 0.0437∗∗∗ 0.0320∗∗∗ 0.9651∗∗∗ 4.0933∗∗∗ -9822 19686 –
Silver Spline 6 0.0400∗ 0.0349∗∗∗ 0.9595∗∗∗ 3.7689∗∗∗ -9806 19716 0.9574
|          |        |     | 0.0458∗∗∗ | 0.0408∗∗∗ | 0.9397∗∗∗ | 3.8973∗∗∗ |             |        |
| -------- | ------ | --- | --------- | --------- | --------- | --------- | ----------- | ------ |
|          | RV     | –   |           |           |           |           | -9798 19665 | 0.8059 |
|          | GARCH  | –   | 0.0330∗∗  | 0.0518∗∗∗ | 0.9388∗∗∗ | 4.7068∗∗∗ | -8460 16962 | –      |
|          |        |     | 0.0307∗∗  | 0.0535∗∗∗ | 0.9344∗∗∗ | 4.5654∗∗∗ |             |        |
| Platinum | Spline | 1   |           |           |           |           | -8450 16960 | 0.2618 |
RV – 0.0309∗∗ 0.0560∗∗∗ 0.9311∗∗∗ 4.6732∗∗∗ -8453 16975 0.2055
|     |       |     |        | 0.0355∗∗∗ | 0.9388∗∗∗ | 7.9946∗∗∗ |             |     |
| --- | ----- | --- | ------ | --------- | --------- | --------- | ----------- | --- |
|     | GARCH | –   | 0.0138 |           |           |           | -8633 17309 | –   |
GSCI Spline 6 0.0141 0.0351∗∗∗ 0.9542∗∗∗ 7.8838∗∗∗ -8621 17345 0.6525
|     | RV  | –   | 0.0138 | 0.0321∗∗ | 0.9612∗∗∗ | 8.3741∗∗∗ | -8616 17301 | 0.4904 |
| --- | --- | --- | ------ | -------- | --------- | --------- | ----------- | ------ |
Table2: ParameterestimationresultsoftheGARCH,Spline-GARCH,andGARCH-MIDAS-RV:2January1996-31
December2015.
Note:Theasterisks∗∗∗,∗∗,and∗indicatesignificanceat1%,5%,and10%,respectively.LListheLog-Likelihoodand
theBICistheBayesianInformationCriterion. Numbersinboldfaceindicatethemodelwiththebestgoodness-of-fit
(lowestBIC).ThevarianceratioVRrepresentstheproportionoflong-termvariancetototalvariance.
26
Electronic copy available at: https://ssrn.com/abstract=3294967

| Commodity | WTI  |     | Brent |     | Gold |     | Silver |     | Platinum |     | GSCI |     |
| --------- | ---- | --- | ----- | --- | ---- | --- | ------ | --- | -------- | --- | ---- | --- |
| Period    | I II | III | I II  | III | I II | III | I II   | III | I II     | III | I II | III |
quarterlygrowthrates
| PPI   |     |     |     | −   | − + | −   | −   |     | −   | −   | +   | +   |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IP    | −   |     | −   |     | − − | −   | − − | −   | −   | −   | −   |     |
| SENTI | − − | −   | − − | −   | − − |     | −   |     | − − |     | − − | −   |
| EPUI  | +   |     | +   | +   | + + | +   |     | +   | + + | +   |     |     |
| EERUS | − + |     | +   |     |     |     | − − |     | +   | +   | −   |     |
| MOVE  |     | +   | +   | +   | −   |     | −   | −   | +   |     | +   | +   |
| VIX   | −   | −   |     |     |     |     |     |     | +   | +   | −   |     |
| TB3M  | −   |     | +   | −   | − + |     | +   | −   | −   |     | −   | −   |
| TED   | −   | −   | + + | −   | −   |     | − + |     | − + |     |     |     |
| GREA  | +   | +   | +   | +   | + + | +   | + + | +   | + + | +   | + + | +   |
quarterlyvariance
| PPI   | + + |     | + + |     | + + | +   | + + | +   | −   |     | + + |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IP    | − + |     | +   |     | +   | +   | +   |     |     |     | −   |     |
| SENTI | − + |     |     |     | + + | +   | +   | +   | + + |     |     | +   |
| EPUI  |     |     | +   | −   | +   |     | + − | +   | +   | +   | + + |     |
| EERUS | +   |     |     | −   | +   | +   | +   | +   | − − | +   |     | +   |
| MOVE  | −   | −   |     |     | −   |     | − − |     | −   | +   |     |     |
| VIX   | −   | −   | + − | −   | +   |     | + − |     | −   | −   | −   | −   |
| TB3M  | − − | −   | + − | −   | − − | +   | −   |     | +   | +   | + − | −   |
| TED   | +   |     |     | −   | − + | +   | − + |     | +   | +   | + − |     |
| GREA  |     |     | +   |     |     |     | +   |     |     | +   |     |     |
Table3: RegressionresultsforGARCH-MIDASmodelusingmacroeconomicandfinancialvariables.
Note: Thesign(+or−)isgiveniftheparameterθisstatisticallysignificant,i.e.p-value<10%. Otherwisethefield
isleftblank. Theperiodsspanfrom(I)1996-2005,(II)2006-2015,and(III)1996-2015.
27
Electronic copy available at: https://ssrn.com/abstract=3294967

PPI IP SENTI EPUI EERUS MOVE VIX TB3M TED GREA GARCH RV Spline
WTI
1-day 3.4620 3.4717 3.4609 3.4717 3.4561 3.4647 3.4679 3.4636 3.4588 3.4633 3.4587 3.4366 3.4466
RMSE 5-days 3.6689 3.6779 3.6705 3.6582 3.6638 3.6692 3.6651 3.6967 3.6679 3.6604 3.6661 3.7518 3.6738
20-days 3.7608 3.7893 3.7525 3.7457 3.7605 3.7603 3.7426 3.8008 3.7671 3.7372 3.7550 3.9878 3.7846
1-day 0.7105 0.7173 0.6833 0.7054 0.7044 0.7090 0.7011 0.7157 0.7190 0.6906 0.7067 0.7220 0.6738
MAE 5-days 0.7670 0.7844 0.7410 0.7554 0.7631 0.7680 0.7546 0.7789 0.7789 0.7420 0.7628 0.8526 0.7293
20-days 0.8466 0.8864 0.8217 0.8271 0.8489 0.8539 0.8251 0.8629 0.8673 0.8093 0.8405 1.0394 0.7966
1-day 0.8807 0.8864 0.8304 0.8725 0.8753 0.8763 0.8637 0.8938 0.8943 0.8457 0.8745 0.9077 0.8461
QLIKE 5-days 0.9300 0.9475 0.8830 0.9165 0.9267 0.9294 0.9090 0.9465 0.9470 0.8894 0.9229 1.0410 0.8985
20-days 1.0081 1.0532 0.9651 0.9838 1.0099 1.0159 0.9793 1.0258 1.0353 0.9554 0.9988 1.2578 0.9600
Brent
1-day 3.0136 3.0106 3.0028 3.0022 3.0052 3.0112 3.0068 2.9924 2.9959 3.0038 3.0008 2.9952 3.0020
RMSE 5-days 3.2042 3.2030 3.1999 3.1934 3.1989 3.2002 3.2020 3.2011 3.1962 3.1834 3.1963 3.2741 3.2395
20-days 3.3086 3.3167 3.3050 3.2908 3.3114 3.3040 3.3033 3.3126 3.3044 3.2665 3.3017 3.5075 3.4219
1-day 0.6585 0.6670 0.6525 0.6620 0.6656 0.6656 0.6631 0.6599 0.6667 0.6430 0.6606 0.6830 0.6461
MAE 5-days 0.7072 0.7198 0.7036 0.7109 0.7182 0.7167 0.7150 0.7158 0.7210 0.6866 0.7115 0.7837 0.7043
20-days 0.7733 0.7960 0.7759 0.7751 0.7936 0.7852 0.7845 0.7886 0.7927 0.7442 0.7812 0.9387 0.7830
1-day 0.8238 0.8408 0.8134 0.8335 0.8417 0.8392 0.8340 0.8415 0.8484 0.8007 0.8330 0.8747 0.8492
QLIKE 5-days 0.8637 0.8842 0.8558 0.8721 0.8851 0.8795 0.8760 0.8865 0.8914 0.8362 0.8739 0.9720 0.9067
20-days 0.9217 0.9535 0.9200 0.9272 0.9534 0.9406 0.9386 0.9494 0.9578 0.8862 0.9356 1.1416 0.9776
Gold
1-day 1.6349 1.6345 1.6286 1.6315 1.6332 1.6363 1.6335 1.6324 1.6350 1.6340 1.6359 1.6154 1.6206
RMSE 5-days 1.7210 1.7189 1.7202 1.7187 1.7180 1.7207 1.7162 1.7149 1.7219 1.7183 1.7192 1.7351 1.7229
20-days 1.7288 1.7304 1.7294 1.7274 1.7252 1.7284 1.7219 1.7236 1.7300 1.7271 1.7266 1.7618 1.7384
1-day 0.2628 0.2593 0.2557 0.2566 0.2560 0.2597 0.2568 0.2519 0.2559 0.2576 0.2590 0.2640 0.2617
MAE 5-days 0.2775 0.2743 0.2702 0.2716 0.2693 0.2737 0.2701 0.2654 0.2712 0.2717 0.2725 0.2889 0.2837
20-days 0.2902 0.2907 0.2824 0.2851 0.2810 0.2850 0.2816 0.2769 0.2829 0.2840 0.2834 0.3249 0.3110
1-day 0.4122 0.4108 0.4093 0.4098 0.4087 0.4127 0.4061 0.4060 0.4105 0.4111 0.4113 0.4143 0.4079
QLIKE 5-days 0.4667 0.4639 0.4625 0.4628 0.4629 0.4680 0.4584 0.4598 0.4650 0.4661 0.4652 0.4719 0.4611
20-days 0.4756 0.4787 0.4745 0.4712 0.4694 0.4759 0.4612 0.4727 0.4760 0.4767 0.4744 0.4948 0.4754
Silver
1-day 3.4798 3.4808 3.4786 3.4844 3.4695 3.4722 3.4790 3.4746 3.4827 3.4593 3.4787 3.4671 3.4754
RMSE 5-days 3.6118 3.6079 3.5963 3.6027 3.6112 3.6053 3.6117 3.6080 3.6355 3.5970 3.6056 3.6028 3.6394
20-days 3.6370 3.6847 3.6231 3.6284 3.6349 3.6294 3.6414 3.6361 3.6705 3.6447 3.6312 3.6480 3.7435
1-day 0.7748 0.7733 0.7640 0.7675 0.7710 0.7672 0.7721 0.7704 0.7822 0.7656 0.7724 0.7571 0.8025
MAE 5-days 0.8113 0.8145 0.7972 0.8008 0.8134 0.8022 0.8091 0.8064 0.8205 0.8117 0.8068 0.7988 0.8636
20-days 0.8472 0.8769 0.8324 0.8327 0.8544 0.8369 0.8449 0.8437 0.8618 0.8800 0.8413 0.8531 0.9605
1-day 0.8651 0.8624 0.8474 0.8546 0.8627 0.8543 0.8629 0.8610 0.8812 0.8547 0.8615 0.8418 0.9129
QLIKE 5-days 0.9121 0.9178 0.8902 0.8987 0.9137 0.9027 0.9086 0.9074 0.9290 0.9135 0.9071 0.8942 0.9852
20-days 0.9499 0.9984 0.9299 0.9340 0.9569 0.9387 0.9469 0.9463 0.9720 0.9970 0.9461 0.9597 1.1089
Platinum
1-day 0.9786 0.9725 0.9751 0.9532 0.9836 0.9814 0.9907 0.9811 0.9838 0.9798 0.9822 0.9505 0.9954
RMSE 5-days 1.0680 1.0511 1.0461 1.0604 1.0520 1.0451 1.0671 1.0523 1.0509 1.0484 1.0457 1.0609 1.0931
20-days 1.1481 1.0992 1.0862 1.1429 1.0803 1.0706 1.1447 1.0889 1.0791 1.0842 1.0709 1.1617 1.2173
1-day 0.2944 0.2810 0.2740 0.2718 0.2861 0.2814 0.2906 0.2803 0.2836 0.2796 0.2816 0.2712 0.3101
MAE 5-days 0.3368 0.3162 0.3048 0.3225 0.3154 0.3078 0.3273 0.3112 0.3115 0.3094 0.3084 0.3285 0.3582
20-days 0.3976 0.3603 0.3394 0.3846 0.3482 0.3359 0.3828 0.3441 0.3412 0.3440 0.3373 0.4025 0.4368
1-day 0.4903 0.4751 0.4683 0.4679 0.4791 0.4760 0.4876 0.4753 0.4776 0.4760 0.4754 0.4663 0.5087
QLIKE 5-days 0.5327 0.5110 0.5013 0.5192 0.5098 0.5043 0.5264 0.5075 0.5070 0.5081 0.5038 0.5237 0.5564
20-days 0.6020 0.5583 0.5389 0.5906 0.5428 0.5317 0.5878 0.5422 0.5359 0.5433 0.5317 0.6092 0.6466
GSCI
1-day 1.1906 1.1889 1.1854 1.1918 1.1892 1.1878 1.1857 1.1867 1.1898 1.1863 1.1877 1.1871 1.1876
RMSE 5-days 1.2466 1.2481 1.2458 1.2478 1.2469 1.2466 1.2453 1.2512 1.2483 1.2430 1.2467 1.2619 1.2520
20-days 1.2660 1.2749 1.2673 1.2655 1.2714 1.2640 1.2635 1.2725 1.2680 1.2606 1.2652 1.3184 1.2765
1-day 0.2536 0.2578 0.2499 0.2565 0.2558 0.2560 0.2569 0.2592 0.2575 0.2505 0.2558 0.2593 0.2412
MAE 5-days 0.2695 0.2774 0.2680 0.2717 0.2742 0.2726 0.2741 0.2779 0.2737 0.2677 0.2724 0.2929 0.2606
20-days 0.2926 0.3085 0.2974 0.2932 0.3031 0.2958 0.2976 0.3025 0.2965 0.2951 0.2953 0.3513 0.2841
1-day 0.4201 0.4253 0.4158 0.4263 0.4215 0.4250 0.4242 0.4288 0.4260 0.4148 0.4240 0.4249 0.4277
QLIKE 5-days 0.4452 0.4525 0.4423 0.4508 0.4480 0.4504 0.4492 0.4562 0.4509 0.4398 0.4492 0.4634 0.4602
20-days 0.4601 0.4754 0.4602 0.4647 0.4684 0.4650 0.4643 0.4729 0.4659 0.4553 0.4638 0.5147 0.4740
Table4: Out-of-sampleforecastingresultstestedwithlossfunctions.
Note: We report RMSE, MAE, and QLIKE results from out-of-sample variance forecasting with 1-day, 5-day, and
20-daysaheadhorizons. BoldfacevaluesindicatemodelswhichareincludedintheModelConfidenceSetM with
90%
10%levelofsignificance. TheModelConfidenceSetisconstructedwith1000bootstrapswithblocklength2.
28
Electronic copy available at: https://ssrn.com/abstract=3294967

enilpS
VR
HCRAG
AERG
DET
M3BT
XIV
EVOM
SUREE
IUPE
ITNES
PI
IPP
ITW
∗∗∗8725.41
8971.6
1923.1
6156.0
6658.3
7837.0
1958.2
6970.1
5796.1
2980.0
1997.0
5451.1
1923.1
yad-1
∗∗1053.01
4869.2
6718.0
1250.1
1560.2
4550.1
2872.1
1586.1
1445.3
7546.1
3874.3
9767.0
6764.2
syad-5
gnol
1559.3
∗5223.7
4915.1
4059.3
1421.1
1305.1
7008.1
0425.0
5145.0
5648.0
4934.1
2488.4
4686.0
syad-02
∗∗∗0648.11
∗∗∗1148.62
∗∗∗0382.22
∗∗∗7691.61
∗∗∗0382.22
∗∗∗8815.52
∗∗∗5858.71
∗∗∗3345.02
∗∗∗0382.22
∗∗∗7325.91
∗∗∗5858.71
∗∗∗0382.22
∗∗∗0999.02
yad-1
2358.3
∗∗∗3795.42
∗∗∗0627.91
∗∗∗2434.41
∗∗∗8065.02
∗∗∗1532.81
∗∗∗4822.51
∗∗∗4656.22
∗∗∗0627.91
∗∗∗0529.71
∗∗∗4682.61
∗∗∗0627.91
∗∗∗0627.91
syad-5
trohs
∗∗2675.9
∗∗∗2500.73
∗∗∗2974.32
∗∗∗3324.51
∗∗∗3808.42
∗∗∗3482.52
∗∗∗9636.61
∗∗∗9039.71
∗∗∗9999.02
∗∗∗9636.61
∗∗∗7903.61
∗∗∗2974.32
∗∗∗3858.12
syad-02
tnerB
∗∗∗0722.31
8148.3
3109.2
2775.2
2784.3
9144.3
9144.3
7670.3
9144.3
6135.2
5722.3
2459.1
2123.1
yad-1
∗6259.6
3724.2
3304.0
6163.1
4863.0
7831.1
7441.0
3735.0
5343.2
1940.2
5268.0
7881.0
1805.0
syad-5
gnol
∗∗∗0576.31
∗∗4615.8
8439.1
2687.1
9107.0
3284.1
5915.1
7770.0
0394.2
3372.0
3372.0
0218.2
7281.0
syad-02
∗∗6474.8
∗∗∗0596.22
∗∗∗3184.71
∗∗∗0308.21
∗∗∗0692.71
∗∗∗5590.31
∗∗∗9690.02
∗∗∗8088.31
∗∗∗8900.81
∗∗∗3184.71
∗∗∗8117.61
∗∗∗2452.31
∗∗∗8939.41
yad-1
∗8985.7
∗∗∗3897.81
∗∗7575.8
∗9209.6
∗∗∗3455.11
∗∗8477.9
∗∗4235.9
∗∗6001.11
∗∗5516.9
∗6410.7
∗∗1423.8
∗∗7575.8
∗5987.7
syad-5
trohs
∗∗6591.8
∗∗∗6469.32
∗∗∗5688.11
∗1900.7
∗∗∗9917.41
∗∗∗5688.11
∗∗5677.8
∗∗∗8991.31
∗∗3475.01
∗∗4235.9
∗∗1423.8
∗∗∗5688.11
∗5560.7
syad-02
dloG
∗1676.7
∗1676.7
8058.5
2879.5
0941.5
∗∗6375.8
∗4081.7
0558.4
2138.5
∗∗∗7438.21
∗3635.6
∗7434.7
2124.5
yad-1
4142.4
0299.2
∗∗1420.01
∗∗1076.8
∗∗3988.8
∗∗∗8740.61
∗∗1358.8
∗∗8052.8
∗∗2849.01
∗∗1495.9
∗∗∗2022.21
∗8356.6
∗9274.7
syad-5
gnol
1196.4
7534.2
∗5390.7
∗2806.6
∗6082.7
∗∗0458.8
9794.3
8137.5
∗4376.6
8199.5
8137.5
∗3942.7
1211.3
syad-02
5501.6
0158.5
∗∗2291.9
∗∗8042.8
∗∗5595.8
∗∗1750.9
∗6026.7
∗∗0452.8
∗∗2660.9
∗∗9943.8
∗1108.7
∗3978.6
5236.5
yad-1
∗∗2291.9
∗∗7304.9
8470.3
7668.1
1282.3
4082.3
0408.3
3903.2
0408.3
3903.2
4900.4
∗1134.6
0691.5
syad-5
trohs
4128.1
2711.4
0024.4
7812.4
1766.2
9860.4
7528.4
4017.4
3226.4
4272.2
7159.2
8746.2
9576.1
syad-02
revliS
∗∗5840.01
7203.3
0856.5
∗0120.7
5062.4
∗5518.6
8573.5
∗8746.6
∗∗∗6429.11
∗∗0796.9
4444.3
∗∗7173.8
∗∗6053.8
yad-1
∗0427.7
6819.3
∗∗3968.7
∗∗3263.01
∗∗∗8540.21
∗∗6841.9
∗∗5327.01
∗0022.7
∗∗1949.8
∗∗∗7980.21
9568.5
∗∗7088.8
∗∗3071.01
syad-5
gnol
2694.4
7265.5
∗5357.7
4528.5
∗1093.6
∗1952.7
∗∗4334.8
∗5017.6
∗∗2583.8
∗3070.7
∗5357.7
9244.3
∗∗2809.8
syad-02
4072.5
6992.5
3794.4
6405.5
2549.4
∗5604.6
6801.3
4347.4
2800.6
5201.5
9688.3
∗6065.6
2800.6
yad-1
7083.2
5025.2
1356.2
4072.2
6674.3
6428.3
9144.3
1756.3
9894.2
8982.3
8081.2
8615.3
5364.3
syad-5
trohs
9919.5
3774.5
4128.1
1569.2
2597.2
4128.1
4128.1
3813.2
2821.1
4128.0
7414.3
5345.2
2482.2
syad-02
munitalP
∗∗∗0003.51
∗∗∗7234.42
∗∗∗1936.61
∗∗∗6913.31
∗∗∗9128.41
∗∗∗9115.51
∗∗3595.8
∗∗∗4629.31
∗∗∗5516.91
∗∗∗9628.72
∗∗∗0090.12
∗∗∗5516.91
∗∗∗4109.91
yad-1
∗7864.7
1378.1
3380.5
8995.5
0510.6
∗∗7034.8
6511.1
1137.4
1358.2
1009.1
∗2737.6
4054.3
1518.3
syad-5
gnol
∗∗∗0692.71
∗∗∗4844.31
2278.5
4133.4
8915.5
∗0075.6
∗∗8251.01
5077.5
∗3136.6
∗∗2202.9
5997.5
∗∗3380.8
∗∗∗3928.71
syad-02
∗∗∗5060.72
∗∗∗0725.42
∗∗∗5800.71
∗∗∗2177.61
∗∗∗9601.51
∗∗∗0015.71
∗∗∗3266.11
∗∗∗7081.51
∗∗∗9912.71
∗∗∗3266.22
∗∗∗4039.31
∗∗∗9665.32
∗∗∗2408.72
yad-1
∗∗∗1978.71
∗∗∗4144.21
∗∗4995.9
∗∗7042.8
∗∗8541.11
∗∗1656.01
∗∗1945.8
∗∗4995.9
∗∗∗6583.51
∗0442.7
5165.5
∗∗∗1064.21
∗∗∗3090.41
syad-5
trohs
∗∗∗3678.73
∗∗∗5881.43
∗∗∗2108.71
∗∗∗7081.51
∗∗∗8501.51
∗∗∗0015.71
∗∗∗2410.52
∗∗∗5845.51
∗∗∗4077.61
∗∗∗5373.22
∗∗∗1039.31
∗∗∗3818.02
∗∗∗9939.13
syad-02
ICSG
6236.2
8554.0
7256.1
3555.5
6427.0
0659.0
6810.2
2716.0
9142.0
6803.1
7846.2
5918.0
8514.1
yad-1
∗∗4757.9
6301.1
9497.3
0901.2
9694.3
2277.4
2407.3
2078.4
1390.1
4691.3
5058.2
0469.1
8152.3
yad-5
gnol
2110.4
∗∗5984.8
7884.5
8349.3
4262.4
6688.5
9277.2
6709.5
∗8273.6
4262.4
1838.4
∗6128.6
6751.2
yad-02
∗∗6235.9
∗∗∗6785.12
∗∗∗4307.71
∗∗∗0120.31
∗∗∗3669.61
∗∗∗4307.71
∗∗∗7042.81
∗∗∗3669.61
∗∗∗1094.51
∗∗∗3333.51
∗∗∗6363.21
∗∗∗4307.71
∗∗∗3333.51
yad-1
∗6444.6
∗∗∗8381.12
∗∗∗7967.51
∗∗1007.01
∗∗∗5742.41
∗∗∗9476.51
∗∗∗1540.71
∗∗∗7967.51
∗∗∗7062.51
∗∗∗4188.21
∗∗∗0205.21
∗∗∗0025.51
∗∗∗0205.21
yad-5
trohs
∗∗0329.8
∗∗∗6134.43
∗∗∗5213.71
∗∗∗0567.41
∗∗∗3595.71
∗∗∗7045.02
∗∗∗7665.02
∗∗∗8183.81
∗∗∗3595.71
∗∗∗8151.41
∗∗∗4740.71
∗∗∗4891.02
∗∗∗4740.71
yad-02
.ecnedfinoc%99.0dna,%579.0,%59.0tatsetegarevoclanoitidnocnuetairavitlumhtiwksiR-ta-eulaVehtrofstluseR
:5elbaT
29
Electronic copy available at: https://ssrn.com/abstract=3294967

| AppendixA | MisspecificationTestResults |               |        |             |          |        |        |     |
| --------- | --------------------------- | ------------- | ------ | ----------- | -------- | ------ | ------ | --- |
|           | Commodity                   | WTI Brent     |        | Gold Silver | Platinum |        | GSCI   |     |
|           | PPI                         | 0.0005 0.0233 | 0.9075 | 0.0925      |          | 0.9656 | 0.0602 |     |
|           | IP                          | 0.0166 0.0283 | 0.2160 | 0.5425      |          | 0.1646 | 0.0116 |     |
|           | SENTI                       |               |        |             |          | 0.0862 |        |     |
|           |                             | 0.8144 0.3272 | 0.0732 | 0.1922      |          |        | 0.1005 |     |
|           | EPUI                        | 0.0114 0.0370 | 0.6813 | 0.5567      |          | 0.7283 | 0.0056 |     |
|           | EERUS                       | 0.1311 0.0958 | 0.5110 | 0.7992      |          | 0.6556 | 0.4134 |     |
|           | MOVE                        | 0.1499 0.4188 | 0.0222 | 0.0092      |          | 0.1139 | 0.0905 |     |
|           | VIX                         | 0.0055 0.0543 | 0.0011 | 0.0004      |          | 0.0544 | 0.0010 |     |
|           | TB3M                        | 0.0316 0.0683 | 0.3664 | 0.3079      |          | 0.2420 | 0.0704 |     |
|           | TED                         | 0.5037 0.5975 | 0.0632 | 0.0131      |          | 0.0213 | 0.4535 |     |
|           | GREA                        | 0.9110 0.5901 | 0.5594 | 0.2826      |          | 0.6389 | 0.6366 |     |
Table6:Testresultsfromtheregression-basedmisspecificationtestofConrad&Schienle(2018).Thevaluespresented
arep-valuesforthecoefficienta intheregressionEq.14. Boldfacedfiguresareindicatingp-valuesof10%orless.
1
| AppendixB | EstimationResults |     |     |     |     |     |          |     |
| --------- | ----------------- | --- | --- | --- | --- | --- | -------- | --- |
|           | µ α               | β m | θ   | ω1  | ω2  | ν   | LogL BIC | VR  |
GARCH 0.0662∗ 0.0235∗∗∗ 0.9610∗∗∗ 1.3442∗∗∗ 7.3371∗∗∗ -5173.52 10386.16 –
GARCH-RV 0.0598∗∗ 0.0194 0.8188∗∗∗ 0.5098∗∗∗ 0.0030∗∗∗ 1.0081 84.7548∗∗∗ 8.5403∗∗∗ -5146.45 10355.50 2.0557
quarterlygrowthrates
PPI 0.0656 0.0209 0.9639∗∗∗ 1.8656 -0.8437 35.3324 6.7549 7.2906∗∗∗ -5170.66 10403.91 0.3950
IP 0.0648 0.0217∗∗∗ 0.9635∗∗∗ 1.4700 -0.1454 8.5688 1.0000∗∗ 7.2451∗∗∗ -5172.31 10407.21 0.2212
|       | 0.0688∗ 0.0217∗∗∗ | 0.9591∗∗∗ 1.3908∗∗∗ | -0.0790∗ |        | 1.0420∗∗∗ | 7.3093∗∗∗ |                   |        |
| ----- | ----------------- | ------------------- | -------- | ------ | --------- | --------- | ----------------- | ------ |
| SENTI |                   |                     |          | 8.6486 |           |           | -5168.06 10398.71 | 0.6124 |
EPUI 0.0661 0.0195∗∗∗ 0.9684∗∗∗ 1.3156∗∗∗ 0.0095 3.5530 29.4196 7.3811∗∗∗ -5172.11 10406.81 0.1431
|       | 0.0664∗ 0.0240∗∗∗ | 0.9582∗∗∗ 1.3543∗∗∗ | -0.0399∗ |         |          | 7.3247∗∗∗ |                   |        |
| ----- | ----------------- | ------------------- | -------- | ------- | -------- | --------- | ----------------- | ------ |
| EERUS |                   |                     |          | 29.8139 | 179.9190 |           | -5171.58 10405.76 | 0.1895 |
MOVE 0.0676∗ 0.0237∗∗∗ 0.9608∗∗∗ 1.3562∗∗∗ -0.0131 17.9453∗ 50.4967∗ 7.3290∗∗∗ -5171.77 10406.14 0.1723
VIX 0.0670∗ 0.0245∗∗∗ 0.9608∗∗∗ 1.3342∗∗∗ 0.0042 177.3029∗∗∗ 1.3560∗∗∗ 7.3441∗∗∗ -5172.47 10407.54 0.0851
|      | 0.0680∗ 0.0235∗∗∗ | 0.9620∗∗∗ 1.3472∗∗∗ |        | 275.1401∗ | 869.3456∗∗ | 7.2795∗∗∗ |                   |        |
| ---- | ----------------- | ------------------- | ------ | --------- | ---------- | --------- | ----------------- | ------ |
| TB3M |                   |                     | 0.0059 |           |            |           | -5172.39 10407.38 | 0.1360 |
TED 0.0662∗ 0.0229∗∗∗ 0.9627∗∗∗ 1.3544∗∗∗ -0.0024∗ 1.1083∗∗∗ 109.8121 7.3234∗∗∗ -5171.84 10406.27 0.1213
|      | 0.0662∗ 0.0234∗∗∗ | 0.9607∗∗∗ 1.3619∗∗∗ |        | 81.9892∗∗∗ |        | 7.3467∗∗∗ |                   |        |
| ---- | ----------------- | ------------------- | ------ | ---------- | ------ | --------- | ----------------- | ------ |
| GREA |                   |                     | 0.0020 |            | 1.6231 |           | -5173.46 10409.51 | 0.0103 |
quarterlyvariances
|     | 0.0628∗ 0.0205∗∗∗ | 0.9648∗∗∗ 0.9814∗∗∗ | 1.9056∗∗ |        | 1.0974∗∗∗ | 7.1587∗∗∗ |                   |        |
| --- | ----------------- | ------------------- | -------- | ------ | --------- | --------- | ----------------- | ------ |
| PPI |                   |                     |          | 3.1102 |           |           | -5169.76 10402.11 | 0.6266 |
IP 0.0672∗ 0.0223∗∗∗ 0.9633∗∗∗ 1.4308∗∗∗ -0.1676∗ 45.9446 139.8659 7.4050∗∗∗ -5171.01 10404.62 0.2246
|       | 0.0668∗ 0.0235∗∗∗ | 0.9605∗∗∗ 1.3846∗∗∗ | -0.0986∗ | 299.9747∗∗∗ | 15.4201∗ | 7.4282∗∗∗ |                   |        |
| ----- | ----------------- | ------------------- | -------- | ----------- | -------- | --------- | ----------------- | ------ |
| SENTI |                   |                     |          |             |          |           | -5172.26 10407.12 | 0.1032 |
EPUI 0.0675∗∗ 0.0234∗∗∗ 0.9615∗∗∗ 1.4068∗∗∗ -0.0744 425.8406 44.6619 7.3785∗∗∗ -5172.55 10407.70 0.0974
EERUS 0.0655∗ 0.0216∗∗∗ 0.9647∗∗∗ 1.4587∗∗∗ -0.1252 3.8376 34.3449 7.2796∗∗∗ -5172.33 10407.25 0.1277
|      | 0.0684∗ 0.0212∗∗∗ | 0.9629∗∗∗ 1.4320∗∗∗ | -0.1210∗∗ | 141.2469∗∗ | 488.3996∗∗ | 7.3892∗∗∗ |                   |        |
| ---- | ----------------- | ------------------- | --------- | ---------- | ---------- | --------- | ----------------- | ------ |
| MOVE |                   |                     |           |            |            |           | -5169.77 10402.14 | 0.3607 |
VIX 0.0702∗∗ 0.0251∗∗∗ 0.9579∗∗∗ 1.4392∗∗∗ -0.1219 79.4647 11.1845 7.5197∗∗∗ -5169.94 10402.47 0.3623
|      | 0.0685∗∗ 0.0220∗∗∗ | 0.9635∗∗∗ 1.4031∗∗∗ | -1.2953∗∗ |          |        | 7.4197∗∗∗ |                   |        |
| ---- | ------------------ | ------------------- | --------- | -------- | ------ | --------- | ----------------- | ------ |
| TB3M |                    |                     |           | 159.0463 | 2.6100 |           | -5171.10 10404.79 | 0.2092 |
TED 0.0657∗ 0.0226∗∗∗ 0.9635∗∗∗ 1.2421∗∗∗ 0.1478∗ 340.8063∗∗∗ 35.5891∗∗∗ 7.2947∗∗∗ -5171.88 10406.36 0.2044
GREA 0.0655 0.0236∗∗∗ 0.9587∗∗∗ 1.0938∗∗∗ 0.8111 4.8713 2.4795 7.2785∗∗∗ -5172.75 10408.09 0.1398
Table7: GARCH-MIDASestimationresultsforWTIlogreturns02Jan1996-30Dec2005withK = 16andBeta-
Theasterisks∗∗∗,∗∗,and∗indicatesignificanceat1%,5%,and10%,respectively.
weightingscheme.
| AppendixC | ExpectedShortfallResults |     |     |     |     |     |     |     |
| --------- | ------------------------ | --- | --- | --- | --- | --- | --- | --- |
30
Electronic copy available at: https://ssrn.com/abstract=3294967

|     | µ α | β m | θ   | ω1  | ω2  | ν   | LogL BIC | VR  |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- |
GARCH 0.0439∗ 0.0396∗∗∗ 0.9559∗∗∗ 1.4152∗∗∗ 8.2405∗∗∗ -10251.29 20545.18 –
|          | 0.0434∗ 0.0414∗∗∗ | 0.9339∗∗∗ 0.7312∗∗∗ | 0.0021∗∗∗ | 1.0090∗∗ | 83.9421∗∗∗ | 8.9921∗∗∗ |                    |        |
| -------- | ----------------- | ------------------- | --------- | -------- | ---------- | --------- | ------------------ | ------ |
| GARCH-RV |                   |                     |           |          |            |           | -10222.39 20512.94 | 0.7781 |
quarterlygrowthrates
PPI 0.0437∗ 0.0389∗∗∗ 0.9569∗∗∗ 1.8931∗∗∗ -0.7933 9.6178 4.9566 8.3242∗∗∗ -10250.16 20568.48 0.0776
IP 0.0435∗∗ 0.0375∗∗∗ 0.9579∗∗∗ 1.4301∗∗∗ -0.0708 4.1419 171.0336∗∗∗ 8.2199∗∗∗ -10250.13 20568.42 0.0317
|       | 0.0442∗∗ 0.0401∗∗∗ | 0.9516∗∗∗ 1.4563∗∗∗ | -0.2358∗∗∗ | 1.7845∗∗∗ |        | 8.0824∗∗∗ |                    |        |
| ----- | ------------------ | ------------------- | ---------- | --------- | ------ | --------- | ------------------ | ------ |
| SENTI |                    |                     |            |           | 2.8456 |           | -10246.60 20561.37 | 0.3746 |
EPUI 0.0435 0.0364∗∗∗ 0.9586∗∗∗ 1.2572∗∗∗ 0.0487 1.4480 3.1990 8.2006∗∗∗ -10248.33 20564.82 0.1442
EERUS 0.0447 0.0390∗∗∗ 0.9556∗∗∗ 1.4134∗∗∗ 0.2066 5.7845 1.8151 8.3647∗∗∗ -10247.79 20563.74 0.1930
MOVE 0.0444∗ 0.0383∗∗∗ 0.9560∗∗∗ 1.3136∗∗∗ 0.0671∗∗ 1.2579∗∗∗ 2.1798∗∗∗ 8.2353∗∗∗ -10247.82 20563.80 0.2052
VIX 0.0467∗∗ 0.0375∗∗∗ 0.9572∗∗∗ 1.4137∗∗∗ -0.0086∗ 65.2652∗ 28.8864∗ 8.2042∗∗∗ -10246.86 20561.89 0.0553
|      | 0.0438∗ 0.0393∗∗∗ | 0.9559∗∗∗ 1.4062∗∗∗ |        |         |         | 8.2363∗∗∗ |                    |        |
| ---- | ----------------- | ------------------- | ------ | ------- | ------- | --------- | ------------------ | ------ |
| TB3M |                   |                     | 0.0031 | 76.0193 | 15.7319 |           | -10250.24 20568.64 | 0.0190 |
TED 0.0456∗ 0.0395∗∗∗ 0.9551∗∗∗ 1.6324∗∗∗ -0.0265∗∗∗ 6.5371∗∗∗ 4.4292∗∗∗ 8.3307∗∗∗ -10247.50 20563.16 0.2421
GREA 0.0437 0.0379∗∗∗ 0.9559∗∗∗ 1.2659∗∗∗ 0.0143∗∗∗ 9.9051∗∗∗ 22.3021∗∗∗ 8.0910∗∗∗ -10246.79 20561.74 0.3782
quarterlyvariances
|     | 0.0451∗ 0.0394∗∗∗ | 0.9560∗∗∗ 1.4468∗∗∗ |         | 431.0154∗∗∗ | 472.4755∗∗∗ | 8.2833∗∗∗ |                    |        |
| --- | ----------------- | ------------------- | ------- | ----------- | ----------- | --------- | ------------------ | ------ |
| PPI |                   |                     | -0.0543 |             |             |           | -10249.59 20567.33 | 0.0389 |
IP 0.0440 0.0396∗∗∗ 0.9560∗∗∗ 1.4106∗∗∗ 0.0071 93.1714 1.4359 8.2432∗∗∗ -10251.24 20570.64 0.0007
SENTI 0.0445∗∗ 0.0393∗∗∗ 0.9549∗∗∗ 1.7079∗∗∗ -0.3954 4.5379∗ 5.3025∗ 8.3932∗∗∗ -10249.30 20566.77 0.1721
|      | 0.0443∗∗ 0.0396∗∗∗ | 0.9559∗∗∗ 1.3686∗∗∗ |        | 335.7813∗∗∗ | 87.5495∗∗∗ | 8.2424∗∗∗ |                    |        |
| ---- | ------------------ | ------------------- | ------ | ----------- | ---------- | --------- | ------------------ | ------ |
| EPUI |                    |                     | 0.0418 |             |            |           | -10249.84 20567.85 | 0.0147 |
EERUS 0.0443 0.0414∗∗∗ 0.9523∗∗∗ 1.1746∗∗∗ 0.1875 2.5551 10.9575∗∗ 8.2579∗∗∗ -10250.37 20568.90 0.0660
|      | 0.0452∗∗ 0.0393∗∗∗ | 0.9544∗∗∗ 1.6285∗∗∗ | -0.2314∗∗∗ | 7.5151∗∗∗ | 22.3919∗∗∗ | 8.2475∗∗∗ |                    |        |
| ---- | ------------------ | ------------------- | ---------- | --------- | ---------- | --------- | ------------------ | ------ |
| MOVE |                    |                     |            |           |            |           | -10246.80 20561.77 | 0.1758 |
VIX 0.0462∗∗ 0.0401∗∗∗ 0.9459∗∗∗ 1.7531∗∗∗ -0.3881∗∗∗ 10.6926 5.6186∗ 8.3157∗∗∗ -10239.45 20547.06 0.3613
TB3M 0.0458∗∗ 0.0392∗∗∗ 0.9487∗∗∗ 1.6150∗∗∗ -1.3559∗∗∗ 18.0971∗∗∗ 15.2119∗∗∗ 8.3524∗∗∗ -10240.50 20549.16 0.4255
|     | 0.0444∗∗ 0.0394∗∗∗ | 0.9564∗∗∗ 1.4066∗∗∗ |        |          |        | 8.2752∗∗∗ |                    |        |
| --- | ------------------ | ------------------- | ------ | -------- | ------ | --------- | ------------------ | ------ |
| TED |                    |                     | 0.0099 | 182.2665 | 1.8471 |           | -10250.62 20569.40 | 0.0050 |
GREA 0.0455∗∗ 0.0395∗∗∗ 0.9556∗∗∗ 1.4450∗∗∗ -0.0413 312.8666∗∗∗ 371.7751∗∗∗ 8.3227∗∗∗ -10248.85 20565.86 0.0532
Table8: GARCH-MIDASestimationresultsforWTIlogreturns02Jan1996-30Dec2015withK = 16andBeta-
Theasterisks∗∗∗,∗∗,and∗indicatesignificanceat1%,5%,and10%,respectively.
weightingscheme.
|     | µ α | β m | θ   | ω1  | ω2  | ν   | LogL BIC | VR  |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- |
GARCH 0.0286 0.0546∗∗∗ 0.9411∗∗∗ 1.4195∗∗∗ 10.0821∗∗∗ -5066.68 10172.52 –
|          | 0.0638∗∗∗ | 0.9143∗∗∗ 0.7061∗∗∗ | 0.0020∗∗∗ |        | 83.7974∗∗ | 11.1036∗∗∗ |                   |        |
| -------- | --------- | ------------------- | --------- | ------ | --------- | ---------- | ----------------- | ------ |
| GARCH-RV | 0.0279    |                     |           | 1.0091 |           |            | -5053.22 10169.08 | 0.7126 |
quarterlygrowthrates
PPI 0.0286 0.0533∗∗∗ 0.9429∗∗∗ 2.0460 -1.0944 8.8428 4.9528 10.4109∗∗∗ -5065.72 10194.09 0.1252
IP 0.0286 0.0504∗∗∗ 0.9456∗∗∗ 1.4944∗∗∗ -0.1145∗ 1.6841 163.7524 10.0182∗∗∗ -5065.10 10192.84 0.0642
|       | 0.0585∗∗∗ | 0.9293∗∗∗ 1.4222∗∗∗ | -0.2857∗∗∗ | 2.0030∗∗∗ | 3.5371∗∗ | 9.6653∗∗∗ |                   |        |
| ----- | --------- | ------------------- | ---------- | --------- | -------- | --------- | ----------------- | ------ |
| SENTI | 0.0297    |                     |            |           |          |           | -5063.88 10190.40 | 0.5146 |
EPUI 0.0314 0.0532∗∗∗ 0.9410∗∗∗ 1.3063∗∗∗ 0.0544∗∗∗ 9.8069∗∗∗ 19.1486∗∗∗ 10.0040∗∗∗ -5062.43 10187.51 0.2908
EERUS 0.0490∗∗∗ 0.9506∗∗∗ 3.0846∗∗∗ 0.8373∗ 3.2174∗∗∗ 1.6692∗∗∗ 9.5562∗∗∗
|     | 0.0316 |     |     |     |     |     | -5061.31 10185.25 | 0.7858 |
| --- | ------ | --- | --- | --- | --- | --- | ----------------- | ------ |
MOVE 0.0289 0.0537∗∗∗ 0.9417∗∗∗ 1.4559∗∗∗ 0.0775 1.1604∗∗ 1.9372∗∗ 9.7172∗∗∗ -5063.93 10190.49 0.2319
VIX 0.0333 0.0537∗∗∗ 0.9403∗∗∗ 1.3486∗∗∗ -0.0064∗∗ 406.7213∗∗∗ 163.0740∗∗∗ 10.1173∗∗∗ -5063.52 10189.68 0.0457
|      | 0.0572∗∗∗ | 0.9374∗∗∗ 1.5504∗∗∗ | -0.0247∗ | 2.6795∗ | 3.3784∗∗∗ | 9.9203∗∗∗ |                   |        |
| ---- | --------- | ------------------- | -------- | ------- | --------- | --------- | ----------------- | ------ |
| TB3M | 0.0294    |                     |          |         |           |           | -5065.39 10193.42 | 0.1533 |
TED 0.0287 0.0549∗∗∗ 0.9381∗∗∗ 1.1643∗∗∗ 0.0204 2.0699∗∗ 5.9154∗∗ 10.1046∗∗∗ -5065.11 10192.86 0.1243
GREA 0.0297 0.0558∗∗∗ 0.9307∗∗∗ 0.8570∗∗∗ 0.0211∗∗∗ 8.9299∗∗ 15.3925∗∗ 9.9207∗∗∗ -5061.06 10184.76 0.4400
quarterlyvariances
|     | 0.0550∗∗∗ | 0.9387∗∗∗ 0.8066∗ | 0.4461∗∗∗ |        |        | 9.8409∗∗∗ |                   |        |
| --- | --------- | ----------------- | --------- | ------ | ------ | --------- | ----------------- | ------ |
| PPI | 0.0289    |                   |           | 1.0000 | 1.4579 |           | -5063.89 10190.42 | 0.2504 |
IP 0.0289 0.0553∗∗∗ 0.9393∗∗∗ 1.0785∗∗∗ 0.3594∗ 1.0000 1.4348 9.9637∗∗∗ -5065.05 10192.73 0.1742
SENTI 0.0298 0.0510∗∗∗ 0.9437∗∗∗ 0.8463∗ 0.5304∗ 8.6925 2.1792 10.3900∗∗∗ -5062.38 10187.39 0.2961
|      | 0.0555∗∗∗ | 0.9400∗∗∗ 1.0562∗∗∗ |        |        | 1.0426∗∗∗ | 10.1742∗∗∗ |                   |        |
| ---- | --------- | ------------------- | ------ | ------ | --------- | ---------- | ----------------- | ------ |
| EPUI | 0.0302    |                     | 0.3597 | 2.9625 |           |            | -5064.87 10192.38 | 0.1219 |
EERUS 0.0290 0.0582∗∗∗ 0.9338∗∗∗ 0.9664∗∗∗ 0.3078∗∗ 1.8273 9.1927 10.0634∗∗∗ -5064.50 10191.63 0.1569
|      | 0.0565∗∗∗ | 0.9401∗∗∗ 1.1125∗∗ |        |        |        | 10.1875∗∗∗ |                   |        |
| ---- | --------- | ------------------ | ------ | ------ | ------ | ---------- | ----------------- | ------ |
| MOVE | 0.0296    |                    | 0.3966 | 3.2913 | 1.4248 |            | -5065.27 10193.18 | 0.1710 |
VIX 0.0317 0.0532∗∗∗ 0.9293∗∗∗ 1.8201∗∗∗ -0.4233∗∗∗ 14.3902∗∗ 7.4703∗∗∗ 9.9043∗∗∗ -5057.03 10176.69 0.4439
TB3M 0.0303 0.0526∗∗∗ 0.9347∗∗∗ 1.8269∗∗∗ -1.5398∗∗∗ 17.9972∗∗∗ 15.1325∗∗∗ 9.9078∗∗∗ -5059.93 10182.49 0.3916
|     | 0.0537∗∗∗ | 0.9423∗∗∗ 1.3991∗∗∗ |        |          | 2.1210∗∗ | 10.2009∗∗∗ |                   |        |
| --- | --------- | ------------------- | ------ | -------- | -------- | ---------- | ----------------- | ------ |
| TED | 0.0294    |                     | 0.0116 | 235.1124 |          |            | -5065.93 10194.50 | 0.0072 |
GREA 0.0309 0.0539∗∗∗ 0.9417∗∗∗ 1.4647 -0.0422 143.9873 193.0913 10.2171∗∗∗ -5065.09 10192.81 0.0539
Table9: GARCH-MIDASestimationresultsforWTIlogreturns03Jan2006-30Dec2015withK = 16andBeta-
Theasterisks∗∗∗,∗∗,and∗indicatesignificanceat1%,5%,and10%,respectively.
weightingscheme.
31
Electronic copy available at: https://ssrn.com/abstract=3294967

|     | µ   | α   | β   | m   | θ   | ω1  | ω2  | ν   | LogL BIC | VR  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
GARCH 0.0794∗ 0.0290∗∗∗ 0.9547∗∗∗ 1.6412∗∗∗ 5.8893∗∗∗ -5704.53 11448.40 –
|          | 0.0764∗ | 0.0257∗∗ | 0.8389∗∗∗ | 0.7362∗∗∗ | 0.0024∗∗∗ | 1.0081∗∗ | 84.8301∗∗∗ | 6.7592∗∗∗ |                   |        |
| -------- | ------- | -------- | --------- | --------- | --------- | -------- | ---------- | --------- | ----------------- | ------ |
| GARCH-RV |         |          |           |           |           |          |            |           | -5678.03 11418.99 | 1.6833 |
quarterlygrowthrates
PPI 0.0823∗∗ 0.0291∗∗∗ 0.9544∗∗∗ 1.5410∗∗∗ 0.1488 1.0865 111.0648 5.8706∗∗∗ -5703.08 11469.10 0.0821
IP 0.0789∗ 0.0287∗∗∗ 0.9538∗∗∗ 1.5615∗∗∗ 0.0899 431.7507∗∗ 290.0333∗∗ 5.9048∗∗∗ -5703.75 11470.44 0.0950
|       | 0.0776∗ | 0.0264∗∗∗ | 0.9567∗∗∗ | 1.6328∗∗∗ | -0.0472∗ |        |         | 5.8805∗∗∗ |                   |        |
| ----- | ------- | --------- | --------- | --------- | -------- | ------ | ------- | --------- | ----------------- | ------ |
| SENTI |         |           |           |           |          | 5.7097 | 33.4820 |           | -5702.44 11467.83 | 0.2150 |
EPUI 0.0793∗ 0.0250∗∗∗ 0.9577∗∗∗ 1.5930∗∗∗ 0.0169∗∗ 4.1082∗∗∗ 26.8004∗∗ 5.8842∗∗∗ -5702.42 11467.77 0.2226
EERUS 0.0769∗ 0.0275∗∗∗ 0.9495∗∗∗ 1.5939∗∗∗ 0.1017∗ 30.8319 13.5147 5.9490∗∗∗ -5702.11 11467.15 0.3033
MOVE 0.0787∗ 0.0277∗∗∗ 0.9544∗∗∗ 1.6232∗∗∗ 0.0180∗∗ 1.0000 6.2839 5.9642∗∗∗ -5702.91 11468.76 0.1469
VIX 0.0816∗∗ 0.0295∗∗∗ 0.9550∗∗∗ 1.6334∗∗∗ 0.0034 172.9569∗∗ 1.3710∗∗∗ 5.9087∗∗∗ -5703.49 11469.91 0.0642
|      | 0.0830∗∗∗ | 0.0290∗∗∗ | 0.9556∗∗∗ | 1.6500∗∗∗ | 0.0082∗∗∗ |          |           | 5.8352∗∗∗ |                   |        |
| ---- | --------- | --------- | --------- | --------- | --------- | -------- | --------- | --------- | ----------------- | ------ |
| TB3M |           |           |           |           |           | 326.7210 | 1001.1585 |           | -5702.49 11467.92 | 0.1980 |
TED 0.0823∗∗ 0.0250∗∗∗ 0.9632∗∗∗ 1.5989∗∗∗ 0.0056∗∗ 232.8204∗∗∗ 23.4961∗∗∗ 5.8945∗∗∗ -5701.97 11466.87 0.2099
GREA 0.0805∗∗ 0.0291∗∗∗ 0.9526∗∗∗ 1.7050∗∗∗ 0.0076 820.4496 125.4143 5.9403∗∗∗ -5703.69 11470.33 0.1165
quarterlyvariances
|     | 0.0788∗∗ | 0.0272∗∗∗ | 0.9573∗∗∗ | 1.4739∗∗∗ | 0.8336∗∗ | 365.3434∗∗∗ | 137.8913∗∗∗ | 5.9284∗∗∗ |                   |        |
| --- | -------- | --------- | --------- | --------- | -------- | ----------- | ----------- | --------- | ----------------- | ------ |
| PPI |          |           |           |           |          |             |             |           | -5701.29 11465.53 | 0.3273 |
IP 0.0798∗∗ 0.0283∗∗∗ 0.9519∗∗∗ 1.2452∗∗∗ 0.7040∗ 13.6770 13.4601 5.8683∗∗∗ -5701.06 11465.05 0.4925
SENTI 0.0793∗∗ 0.0281∗∗∗ 0.9568∗∗∗ 1.6112∗∗∗ 0.0658 566.1770 70.7841 5.9051∗∗∗ -5704.07 11471.08 0.0335
|      | 0.0765∗ | 0.0262∗∗∗ | 0.9624∗∗∗ | 1.5014∗∗∗ | 0.1761∗∗ |         |          | 5.9102∗∗∗ |                   |        |
| ---- | ------- | --------- | --------- | --------- | -------- | ------- | -------- | --------- | ----------------- | ------ |
| EPUI |         |           |           |           |          | 92.4390 | 170.0783 |           | -5700.65 11464.23 | 0.3451 |
EERUS 0.0810∗∗ 0.0285∗∗∗ 0.9519∗∗∗ 1.4590∗∗∗ 0.2068 20.9637 4.3382 5.9553∗∗∗ -5703.78 11470.50 0.1097
|      |        | 0.0286∗∗ | 0.9541∗∗∗ | 1.5589∗∗∗ |        |        |         | 5.9520∗∗∗ |                   |        |
| ---- | ------ | -------- | --------- | --------- | ------ | ------ | ------- | --------- | ----------------- | ------ |
| MOVE | 0.0793 |          |           |           | 0.1054 | 5.4162 | 45.0300 |           | -5703.67 11470.28 | 0.1062 |
VIX 0.0782∗∗ 0.0269∗∗∗ 0.9579∗∗∗ 1.4869∗∗∗ 0.1929∗∗ 4.3678∗∗ 31.0806∗∗∗ 5.8870∗∗∗ -5702.22 11467.38 0.2513
TB3M 0.0782∗∗ 0.0258∗∗∗ 0.9581∗∗∗ 1.4978∗∗∗ 1.9915∗∗∗ 35.2943 349.7361 5.9021∗∗∗ -5701.68 11466.30 0.2321
|     | 0.0786∗ | 0.0264∗∗∗ | 0.9576∗∗∗ | 1.5356∗∗∗ |        |        |         | 5.8816∗∗∗ |                   |        |
| --- | ------- | --------- | --------- | --------- | ------ | ------ | ------- | --------- | ----------------- | ------ |
| TED |         |           |           |           | 0.1668 | 7.5629 | 42.6644 |           | -5703.43 11469.80 | 0.1495 |
GREA 0.0788∗∗ 0.0268∗∗∗ 0.9583∗∗∗ 1.5421∗∗∗ 0.3049∗ 358.6663 95.7315 5.8934∗∗∗ -5702.12 11467.18 0.1758
Table 10: GARCH-MIDAS estimation results for Brent log returns 01 Jan 1996-30 Dec 2005 with K = 16 and
Theasterisks∗∗∗,∗∗,and∗indicatesignificanceat1%,5%,and10%,respectively.
Beta-weightingscheme.
|     | µ   | α   | β   | m   | θ   | ω1  | ω2  | ν   | LogL BIC | VR  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
GARCH 0.0391∗∗ 0.0413∗∗∗ 0.9560∗∗∗ 1.7228∗∗∗ 7.0635∗∗∗ -10892.81 21828.42 –
|          | 0.0398∗ | 0.0422∗∗∗ | 0.9442∗∗∗ | 0.9011∗∗∗ | 0.0019∗∗∗ | 1.0092∗∗∗ | 83.7747∗∗ | 7.3900∗∗∗ |                    |        |
| -------- | ------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | ------------------ | ------ |
| GARCH-RV |         |           |           |           |           |           |           |           | -10868.94 21806.36 | 0.6140 |
quarterlygrowthrates
PPI 0.0395∗ 0.0404∗∗∗ 0.9573∗∗∗ 1.9064∗∗∗ -0.2977∗∗ 52.6614∗∗∗ 37.3540∗∗∗ 7.0876∗∗∗ -10890.58 21849.64 0.0330
IP 0.0387 0.0400∗∗∗ 0.9573∗∗∗ 1.7284∗∗∗ -0.0501 1.0091 83.7762 7.0442∗∗∗ -10892.28 21853.04 0.0128
|       |        | 0.0417∗∗∗ | 0.9533∗∗∗ | 1.7244∗∗∗ | -0.2193∗∗∗ | 1.9143∗∗∗ | 3.1494∗∗ | 6.8354∗∗∗ |                    |        |
| ----- | ------ | --------- | --------- | --------- | ---------- | --------- | -------- | --------- | ------------------ | ------ |
| SENTI | 0.0397 |           |           |           |            |           |          |           | -10890.06 21848.60 | 0.2764 |
EPUI 0.0386 0.0397∗∗∗ 0.9581∗∗∗ 1.7547∗∗∗ 0.0037∗∗∗ 429.8582 87.3651 7.0649∗∗∗ -10889.90 21848.28 0.0173
| EERUS |        | 0.0397∗∗∗ | 0.9574∗∗∗ | 1.6975∗∗∗ |        |        |        | 7.2184∗∗∗ |                    |        |
| ----- | ------ | --------- | --------- | --------- | ------ | ------ | ------ | --------- | ------------------ | ------ |
|       | 0.0389 |           |           |           | 0.3520 | 4.3312 | 1.7986 |           | -10888.67 21845.82 | 0.3629 |
MOVE 0.0387∗ 0.0391∗∗∗ 0.9577∗∗∗ 1.5995∗∗∗ 0.0728∗ 1.2266∗∗∗ 2.4010∗∗∗ 7.0733∗∗∗ -10887.77 21844.02 0.2203
VIX 0.0393 0.0415∗∗∗ 0.9552∗∗∗ 1.8809∗∗∗ -0.0479 4.1850 2.9425 6.9516∗∗∗ -10890.68 21849.83 0.1487
|      |        | 0.0431∗∗∗ | 0.9531∗∗∗ | 1.7405∗∗∗ | -0.0222∗∗∗ | 4.6519∗∗∗ | 5.1642∗∗∗ | 6.9698∗∗∗ |                    |        |
| ---- | ------ | --------- | --------- | --------- | ---------- | --------- | --------- | --------- | ------------------ | ------ |
| TB3M | 0.0403 |           |           |           |            |           |           |           | -10890.11 21848.70 | 0.1616 |
TED 0.0412∗ 0.0416∗∗∗ 0.9551∗∗∗ 1.9759∗∗∗ -0.0322∗∗ 4.9531∗∗∗ 3.4181∗∗∗ 7.0685∗∗∗ -10889.68 21847.85 0.2324
GREA 0.0411 0.0392∗∗∗ 0.9569∗∗∗ 1.4976∗∗∗ 0.0137∗∗∗ 157.1200 423.7567∗ 7.0023∗∗∗ -10885.44 21839.36 0.3445
quarterlyvariances
|     | 0.0395∗ | 0.0412∗∗∗ | 0.9561∗∗∗ | 1.7307∗∗∗ |         | 363.0267∗∗ | 69.0795∗∗ | 7.0754∗∗∗ |                    |        |
| --- | ------- | --------- | --------- | --------- | ------- | ---------- | --------- | --------- | ------------------ | ------ |
| PPI |         |           |           |           | -0.0228 |            |           |           | -10892.54 21853.56 | 0.0048 |
IP 0.0394 0.0406∗∗∗ 0.9567∗∗∗ 1.7362∗∗∗ -0.0389 812.3569∗∗ 100.9616 7.0706∗∗∗ -10891.40 21851.28 0.0165
SENTI 0.0399 0.0414∗∗∗ 0.9543∗∗∗ 2.0201∗∗∗ -0.4870 5.2990 7.2992 7.1336∗∗∗ -10890.13 21848.73 0.2428
|      |        | 0.0399∗∗∗ | 0.9567∗∗∗ | 1.7612∗∗∗ | -0.1075∗∗∗ | 20.7665∗ |          | 7.0357∗∗∗ |                    |        |
| ---- | ------ | --------- | --------- | --------- | ---------- | -------- | -------- | --------- | ------------------ | ------ |
| EPUI | 0.0396 |           |           |           |            |          | 101.2644 |           | -10889.05 21846.59 | 0.0603 |
EERUS 0.0406∗ 0.0407∗∗∗ 0.9551∗∗∗ 1.9450∗∗∗ -0.2535∗ 18.4517 2.4228 6.9597∗∗∗ -10887.78 21844.03 0.1249
|      | 0.0391∗ | 0.0410∗∗∗ | 0.9552∗∗∗ | 1.9455∗∗∗ |         |        |         | 6.9623∗∗∗ |                    |        |
| ---- | ------- | --------- | --------- | --------- | ------- | ------ | ------- | --------- | ------------------ | ------ |
| MOVE |         |           |           |           | -0.2472 | 6.9609 | 22.4703 |           | -10888.27 21845.01 | 0.1640 |
VIX 0.0404 0.0430∗∗∗ 0.9440∗∗∗ 2.1546∗∗∗ -0.6247∗∗∗ 4.2526 2.6998 6.9803∗∗∗ -10878.25 21824.98 0.5306
TB3M 0.0411 0.0415∗∗∗ 0.9456∗∗∗ 1.8457∗∗∗ -1.7622∗∗∗ 14.5751∗∗ 14.3853∗ 7.0559∗∗∗ -10878.23 21824.94 0.5652
|     | 0.0401∗ | 0.0408∗∗∗ | 0.9564∗∗∗ | 1.7235∗∗∗ | -0.0136∗ |          |         | 7.0830∗∗∗ |                    |        |
| --- | ------- | --------- | --------- | --------- | -------- | -------- | ------- | --------- | ------------------ | ------ |
| TED |         |           |           |           |          | 465.3439 | 64.3570 |           | -10891.79 21852.05 | 0.0075 |
GREA 0.0386 0.0401∗∗∗ 0.9566∗∗∗ 1.8793∗∗∗ -0.2427 1.6053 4.0392 7.1536∗∗∗ -10890.22 21848.93 0.3248
Table 11: GARCH-MIDAS estimation results for Brent log returns 01 Jan 1996-31 Dec 2015 with K = 16 and
Theasterisks∗∗∗,∗∗,and∗indicatesignificanceat1%,5%,and10%,respectively.
Beta-weightingscheme.
32
Electronic copy available at: https://ssrn.com/abstract=3294967

|     | µ α | β m | θ   | ω1  | ω2  | ν   | LogL BIC | VR  |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- |
GARCH 0.0198 0.0546∗∗∗ 0.9423∗∗∗ 1.5212∗∗∗ 9.1887∗∗∗ -5174.70 10388.74 –
|          | 0.0623∗∗∗ | 0.9248∗∗∗ 0.8574∗∗∗ | 0.0017∗∗∗ |        |         | 9.4896∗∗∗ |                   |        |
| -------- | --------- | ------------------- | --------- | ------ | ------- | --------- | ----------------- | ------ |
| GARCH-RV | 0.0201    |                     |           | 1.0093 | 83.6529 |           | -5166.06 10395.05 | 0.5619 |
quarterlygrowthrates
PPI 0.0192 0.0512∗∗∗ 0.9450∗∗∗ 0.9825 0.7115 3.5710 9.0788 9.2305∗∗∗ -5174.03 10411.00 0.0629
IP 0.0190 0.0505∗∗∗ 0.9468∗∗∗ 1.6518∗∗∗ -0.1430∗∗ 1.1327 198.1292 9.0883∗∗∗ -5172.36 10407.65 0.0941
|       | 0.0573∗∗∗ | 0.9335∗∗∗ 1.4652∗∗∗ | -0.2954∗∗∗ | 1.9374∗∗∗ | 3.1332∗ | 8.7528∗∗∗ |                   |        |
| ----- | --------- | ------------------- | ---------- | --------- | ------- | --------- | ----------------- | ------ |
| SENTI | 0.0210    |                     |            |           |         |           | -5172.81 10408.55 | 0.4663 |
EPUI 0.0203 0.0549∗∗∗ 0.9409∗∗∗ 1.3770∗∗∗ 0.0793 2.0858 5.1262 8.9194∗∗∗ -5172.10 10407.14 0.3045
EERUS 0.0191 0.0515∗∗∗ 0.9446∗∗∗ 1.3705∗∗∗ -0.2905 3.3980 6.9437 9.2703∗∗∗ -5173.41 10409.75 0.1316
MOVE 0.0189 0.0521∗∗ 0.9451∗∗∗ 1.6082∗∗ 0.0644 1.0493 2.0981 9.0048∗∗∗ -5171.81 10406.56 0.1738
VIX 0.0203 0.0553∗∗∗ 0.9415∗∗∗ 1.5149∗∗∗ 0.0085 15.7627 48.6047 9.2185∗∗∗ -5173.43 10409.80 0.0290
|      | 0.0568∗∗∗ | 0.9396∗∗∗ 1.7014∗∗∗ |         |        |        | 8.9775∗∗∗ |                   |        |
| ---- | --------- | ------------------- | ------- | ------ | ------ | --------- | ----------------- | ------ |
| TB3M | 0.0211    |                     | -0.0229 | 4.6825 | 5.2851 |           | -5172.97 10408.88 | 0.1771 |
TED 0.0194 0.0529∗∗∗ 0.9438∗∗∗ 1.0947∗∗∗ 0.0404∗ 1.0000∗∗∗ 1.1141∗∗∗ 9.0427∗∗∗ -5171.64 10406.22 0.1233
GREA 0.0202 0.0542∗∗∗ 0.9340∗∗∗ 0.7799∗∗∗ 0.0256∗∗∗ 5.1782 11.0962 8.8998∗∗∗ -5168.27 10399.47 0.5997
quarterlyvariances
|     | 0.0549∗∗∗ | 0.9406∗∗∗ 0.9413∗ | 0.4341∗∗ |        |        | 8.9181∗∗∗ |                   |        |
| --- | --------- | ----------------- | -------- | ------ | ------ | --------- | ----------------- | ------ |
| PPI | 0.0200    |                   |          | 1.0000 | 1.7103 |           | -5172.44 10407.81 | 0.2427 |
IP 0.0202 0.0550∗∗∗ 0.9412∗∗∗ 1.2135∗∗ 0.3413 1.0000 1.7941 9.0087∗∗∗ -5173.49 10409.91 0.1689
SENTI 0.0221 0.0497∗∗∗ 0.9478∗∗∗ 0.8688 0.7251 7.0203 2.3635 8.9869∗∗∗ -5169.90 10402.73 0.3667
|      | 0.0534∗∗∗ | 0.9444∗∗∗ 1.0401∗ |        |        | 1.0475∗∗∗ | 9.1331∗∗∗ |                   |        |
| ---- | --------- | ----------------- | ------ | ------ | --------- | --------- | ----------------- | ------ |
| EPUI | 0.0208    |                   | 0.5672 | 1.0000 |           |           | -5173.50 10409.93 | 0.1255 |
EERUS 0.0203 0.0559∗∗∗ 0.9395∗∗∗ 1.2204∗∗∗ 0.2169 1.0000 8.5541 9.1091∗∗∗ -5172.53 10407.99 0.0938
|      | 0.0562∗∗∗ | 0.9417∗∗∗ 1.2691∗∗∗ |        | 3.3155∗∗ |        | 9.1800∗∗∗ |                   |        |
| ---- | --------- | ------------------- | ------ | -------- | ------ | --------- | ----------------- | ------ |
| MOVE | 0.0209    |                     | 0.4303 |          | 1.3649 |           | -5173.51 10409.95 | 0.1914 |
VIX 0.0210 0.0534∗∗∗ 0.9289∗∗∗ 1.9656∗∗∗ -0.5538∗∗∗ 9.0335∗ 5.6418∗∗ 8.9773∗∗∗ -5163.95 10390.83 0.5804
TB3M 0.0225 0.0540∗∗∗ 0.9341∗∗∗ 1.9235∗∗∗ -1.7958∗∗∗ 13.9763∗∗∗ 14.1407∗∗ 8.9573∗∗∗ -5167.32 10397.57 0.4755
|     | 0.0492∗∗∗ | 0.9479∗∗∗ 1.3852∗∗∗ |        |        |        | 9.0410∗∗∗ |                   |        |
| --- | --------- | ------------------- | ------ | ------ | ------ | --------- | ----------------- | ------ |
| TED | 0.0189    |                     | 0.1183 | 1.6790 | 9.9834 |           | -5171.31 10405.56 | 0.1476 |
GREA 0.0189 0.0509∗∗∗ 0.9462∗∗∗ 1.6695∗∗∗ -0.1678 1.7362 5.1397 9.3411∗∗∗ -5173.42 10409.78 0.1679
Table 12: GARCH-MIDAS estimation results for Brent log returns 02 Jan 2006-31 Dec 2015 with K = 16 and
Theasterisks∗∗∗,∗∗,and∗indicatesignificanceat1%,5%,and10%,respectively.
Beta-weightingscheme.
|     | µ α | β m | θ   | ω1  | ω2  | ν   | LogL BIC | VR  |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- |
GARCH -0.0063 0.0480∗∗∗ 0.9486∗∗∗ -0.0736 4.1517∗∗∗ -2986.31 6011.96 –
|     | 0.0642∗∗∗ | 0.9257∗∗∗ | 0.0212∗∗∗ |     |     | 3.7816∗∗∗ |     |     |
| --- | --------- | --------- | --------- | --- | --- | --------- | --- | --- |
GARCH-RV -0.0053 -0.7402 1.0000 8.4528 -2974.39 6011.72 0.6597
quarterlygrowthrates
PPI -0.0068 0.0565∗∗∗ 0.9392∗∗∗ 4.4361∗∗ -6.5927∗∗ 1.3087∗∗∗ 1.0258∗∗∗ 3.9631∗∗∗ -2982.97 6028.88 0.2795
IP -0.0067 0.0546∗∗∗ 0.9370∗∗∗ 0.6681 -0.6291∗∗∗ 50.8573 52.7204 3.7538∗∗∗ -2978.69 6020.31 0.6819
|       | 0.0555∗∗∗ | 0.9277∗∗∗ | -0.4198∗∗∗ | 4.1774∗∗∗ | 2.0004∗∗∗ | 3.6899∗∗∗ |                  |        |
| ----- | --------- | --------- | ---------- | --------- | --------- | --------- | ---------------- | ------ |
| SENTI | -0.0068   | 0.1701    |            |           |           |           | -2975.79 6014.51 | 0.7431 |
EPUI -0.0061 0.0544∗∗∗ 0.9265∗∗∗ -0.4683 0.1487∗∗∗ 7.4260 2.7882 3.7882∗∗∗ -2975.39 6013.72 0.7058
| EERUS | 0.0512∗ | 0.9421∗∗∗ |     |     |     | 4.0438∗∗∗ |     |     |
| ----- | ------- | --------- | --- | --- | --- | --------- | --- | --- |
-0.0077 -0.0965 -0.2263 7.6506 28.8344 -2984.45 6031.83 0.3597
MOVE -0.0066 0.0467∗∗∗ 0.9488∗∗∗ 0.3805 -0.2624∗∗ 1.8033∗∗∗ 2.1635∗ 3.9729∗∗∗ -2979.51 6021.95 0.5505
VIX -0.0072 0.0495 0.9466∗∗∗ 0.1976 -0.0295 16.5236 11.2721 4.0616∗ -2985.31 6033.56 0.0778
|      | 0.0553∗∗∗ | 0.9279∗∗∗ | -0.0786∗∗∗ | 7.4019∗∗ | 6.4276∗ | 3.7012∗∗∗ |                  |        |
| ---- | --------- | --------- | ---------- | -------- | ------- | --------- | ---------------- | ------ |
| TB3M | -0.0076   | -0.1367   |            |          |         |           | -2972.67 6008.27 | 0.7652 |
TED -0.0066 0.0507∗∗∗ 0.9279∗∗∗ 0.2775 -0.0911∗∗∗ 5.0520∗∗∗ 3.6726∗∗∗ 3.7270∗∗∗ -2970.56 6004.06 0.8130
GREA -0.0063 0.0489∗∗∗ 0.9459∗∗∗ -0.0779 0.0212∗∗∗ 1.2564 226.1724 4.0405∗∗∗ -2982.11 6027.15 0.5670
quarterlyvariances
|     | 0.0520∗∗∗ | 0.9359∗∗∗ -1.3397∗∗∗ | 7.0229∗∗∗ | 2.4532∗∗∗ | 3.1795∗∗∗ | 3.6833∗∗∗ |                  |        |
| --- | --------- | -------------------- | --------- | --------- | --------- | --------- | ---------------- | ------ |
| PPI | -0.0076   |                      |           |           |           |           | -2973.82 6010.57 | 0.9732 |
IP -0.0071 0.0496∗∗∗ 0.9442∗∗∗ 0.3769 -0.8283 2.5334 14.4310 4.0336∗∗∗ -2983.98 6030.90 0.2037
SENTI -0.0063 0.0536∗∗∗ 0.9390∗∗∗ -0.7613∗ 1.9547∗∗∗ 2.4203∗∗∗ 5.0475∗∗∗ 3.8622∗∗∗ -2981.53 6025.99 0.5366
|     | 0.0471∗∗∗ | 0.9497∗∗∗ |     |     |     | 4.1866∗∗∗ |     |     |
| --- | --------- | --------- | --- | --- | --- | --------- | --- | --- |
EPUI -0.0061 0.0317 -0.1113 157.9278 1.3253 -2985.62 6034.18 0.0269
EERUS -0.0073 0.0505∗∗∗ 0.9448∗∗∗ 0.2044 -0.2320 348.2565 35.3930 4.0838∗∗∗ -2985.14 6033.23 0.0482
|      | 0.0558∗∗∗ | 0.9280∗∗∗ 1.0713∗∗ | -1.4279∗∗∗ | 2.1832∗ |        | 3.7343∗∗∗ |                  |        |
| ---- | --------- | ------------------ | ---------- | ------- | ------ | --------- | ---------------- | ------ |
| MOVE | -0.0053   |                    |            |         | 4.7614 |           | -2975.47 6013.87 | 0.8051 |
VIX -0.0079 0.0562∗∗ 0.9371∗∗∗ 0.6181 -0.5239 17.7737 12.3365 3.9006∗∗∗ -2983.67 6030.27 0.1892
TB3M -0.0055 0.0406∗∗∗ 0.9561∗∗∗ -0.1366 -3.7329∗∗ 144.1225 509.3292 4.3050∗∗∗ -2982.12 6027.18 0.1558
|     | 0.0380∗∗∗ | 0.9607∗∗∗ | -2.6951∗∗ | 1.2195∗∗ | 2.0021∗∗ | 4.3669∗∗∗ |                  |        |
| --- | --------- | --------- | --------- | -------- | -------- | --------- | ---------------- | ------ |
| TED | -0.0080   | 0.5356    |           |          |          |           | -2981.92 6026.78 | 2.3908 |
GREA -0.0071 0.0460∗∗∗ 0.9501∗∗∗ -1.2550 3.9935 2.2698∗ 2.7228∗∗∗ 3.9230∗∗∗ -2977.82 6018.58 0.7409
Table13: GARCH-MIDASestimationresultsforGoldlogreturns01Jan1996-30Dec2005withK = 16andBeta-
Theasterisks∗∗∗,∗∗,and∗indicatesignificanceat1%,5%,and10%,respectively.
weightingscheme.
33
Electronic copy available at: https://ssrn.com/abstract=3294967

|     | µ   | α   | β   | m   | θ   | ω1  | ω2  | ν   | LogL BIC | VR  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
GARCH 0.0111 0.0399∗∗∗ 0.9578∗∗∗ -0.0064∗∗ 4.5391∗∗∗ -6999.85 14042.51 –
|          |        | 0.0467∗∗∗ | 0.9443∗∗∗ | -0.4543∗∗ | 0.0107∗∗∗ |        |         | 4.2019∗∗∗ |                   |        |
| -------- | ------ | --------- | --------- | --------- | --------- | ------ | ------- | --------- | ----------------- | ------ |
| GARCH-RV | 0.0126 |           |           |           |           | 1.0000 | 15.4420 |           | -6973.45 14015.37 | 0.7652 |
quarterlygrowthrates
PPI 0.0101 0.0415∗∗∗ 0.9563∗∗∗ 2.6572∗∗∗ -4.1571∗∗∗ 3.1520∗∗∗ 2.4573∗∗∗ 4.4335∗∗∗ -6994.06 14056.59 0.6663
IP 0.0106 0.0437∗∗∗ 0.9518∗∗∗ 0.7593∗∗∗ -0.8213∗∗∗ 1.1768 1.1548∗∗∗ 4.2259∗∗∗ -6992.84 14054.17 0.5417
|       |        | 0.0427∗∗∗ | 0.9537∗∗∗ | 0.4770∗ |         |        | 1.5160∗∗∗ | 4.2807∗∗∗ |                   |        |
| ----- | ------ | --------- | --------- | ------- | ------- | ------ | --------- | --------- | ----------------- | ------ |
| SENTI | 0.0107 |           |           |         | -0.2690 | 2.4985 |           |           | -6994.70 14057.88 | 0.2907 |
EPUI 0.0109 0.0405∗∗∗ 0.9559∗∗∗ -0.1940 0.1306∗∗∗ 1.3286∗∗∗ 1.0161∗∗∗ 4.4043∗∗∗ -6992.65 14053.79 0.3743
EERUS 0.0112 0.0398∗∗∗ 0.9577∗∗∗ -0.0078 -0.0146 298.5877 30.6834 4.5356∗∗∗ -6999.66 14067.81 0.0025
MOVE 0.0111 0.0397∗∗∗ 0.9582∗∗∗ -0.0023 0.0039 11.8956 81.3825 4.5484∗∗∗ -6998.95 14066.38 0.0064
VIX 0.0112 0.0395∗∗∗ 0.9578∗∗∗ -0.0079 0.0203 13.3564 18.9974 4.4888∗∗∗ -6997.82 14064.12 0.0601
|     |     | 0.0399∗ | 0.9578∗∗∗ |     |     |     |     | 4.5381∗∗∗ |     |     |
| --- | --- | ------- | --------- | --- | --- | --- | --- | --------- | --- | --- |
TB3M 0.0111 -0.0048 0.0002 81.8171 10.6749 -6999.85 14068.18 0.0000
TED 0.0108 0.0397∗∗∗ 0.9572∗∗∗ 0.4695 -0.0318 13.4047 10.1279 4.3877∗∗∗ -6991.57 14051.62 0.3690
GREA 0.0092 0.0404∗∗∗ 0.9571∗∗∗ 0.0906 0.0390∗∗ 2.3630 1.0000∗∗∗ 4.3121∗∗∗ -6987.87 14044.23 1.2407
quarterlyvariances
|     |        | 0.0420∗∗∗ | 0.9545∗∗∗ |         | 0.6714∗∗∗ | 1.0295∗∗∗ | 1.1398∗∗∗ | 4.2715∗∗∗ |                   |        |
| --- | ------ | --------- | --------- | ------- | --------- | --------- | --------- | --------- | ----------------- | ------ |
| PPI | 0.0102 |           |           | -0.1863 |           |           |           |           | -6989.63 14047.73 | 0.6539 |
IP 0.0099 0.0403∗∗∗ 0.9574∗∗∗ -0.2014 0.5305∗∗∗ 4.6840 2.3209 4.4440∗∗∗ -6993.48 14055.45 0.4093
SENTI 0.0117 0.0415∗∗∗ 0.9530∗∗∗ -0.9896∗∗∗ 1.5606∗∗∗ 1.1595∗∗∗ 1.3229∗∗∗ 4.2007∗∗∗ -6987.97 14044.43 1.0896
|     |     | 0.0398∗∗∗ | 0.9578∗∗∗ |     |     |     |     | 4.5362∗∗∗ |     |     |
| --- | --- | --------- | --------- | --- | --- | --- | --- | --------- | --- | --- |
EPUI 0.0110 -0.0140 0.0485 37.6192 346.9290 -6998.29 14065.06 0.0132
EERUS 0.0097 0.0397∗∗∗ 0.9574∗∗∗ -0.5081∗∗ 0.6944∗∗∗ 16.8067∗∗ 7.9749∗∗∗ 4.4111∗∗∗ -6989.58 14047.64 0.5018
|     |     | 0.0406∗∗∗ | 0.9566∗∗∗ |     |     |     |     | 4.5069∗∗∗ |     |     |
| --- | --- | --------- | --------- | --- | --- | --- | --- | --------- | --- | --- |
MOVE 0.0116 0.2243 -0.1517 9.3847 25.8016 -6998.76 14066.00 0.0488
VIX 0.0108 0.0403∗∗∗ 0.9572∗∗∗ -0.0269 0.0663 76.8542∗ 102.4869∗ 4.5406∗∗∗ -6997.60 14063.69 0.0261
TB3M 0.0104 0.0417∗∗∗ 0.9555∗∗∗ -0.1229 1.8944∗∗∗ 9.5790∗∗∗ 16.9602∗∗∗ 4.3972∗∗∗ -6994.09 14056.65 0.4953
|     |        | 0.0391∗∗∗ | 0.9585∗∗∗ |         | 0.0331∗ |         |          | 4.5425∗∗∗ |                   |        |
| --- | ------ | --------- | --------- | ------- | ------- | ------- | -------- | --------- | ----------------- | ------ |
| TED | 0.0114 |           |           | -0.0285 |         | 31.1878 | 290.8318 |           | -6997.10 14062.69 | 0.0197 |
GREA 0.0100 0.0401∗∗∗ 0.9574∗∗∗ -0.1692 0.2863 6.6844 3.6795 4.4617∗∗∗ -6993.68 14055.84 0.4009
Table14: GARCH-MIDASestimationresultsforGoldlogreturns01Jan1996-31Dec2015withK = 16andBeta-
Theasterisks∗∗∗,∗∗,and∗indicatesignificanceat1%,5%,and10%,respectively.
weightingscheme.
|     | µ   | α   | β   | m   | θ   | ω1  | ω2  |     | ν LogL | BIC VR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ |
GARCH 0.0533∗∗∗ 0.0378∗∗∗ 0.9586∗∗∗ 0.9930∗∗ 4.3351∗∗∗ -3998.31 8035.95 –
|          | 0.0561∗∗∗ | 0.0307∗∗∗ | 0.9215∗∗∗ | -0.3495∗∗∗ | 0.0066∗∗∗ | 1.0092∗ | 83.7635∗ | 4.8198∗∗∗ |                  |        |
| -------- | --------- | --------- | --------- | ---------- | --------- | ------- | -------- | --------- | ---------------- | ------ |
| GARCH-RV |           |           |           |            |           |         |          |           | -3978.81 8020.56 | 1.0031 |
quarterlygrowthrates
PPI 0.0527∗∗∗ 0.0321∗∗∗ 0.9650∗∗∗ 0.8799∗ 0.1722∗∗ 89.4027∗∗∗ 436.1480∗∗ 4.4236∗∗∗ -3993.15 8049.24 0.1009
IP 0.0537∗∗∗ 0.0357∗∗∗ 0.9604∗∗∗ 1.0935 -0.1511∗∗∗ 1.3349 179.6378 4.1842∗∗∗ -3994.74 8052.42 0.2178
|       | 0.0522∗∗∗ | 0.0292∗∗∗ | 0.9564∗∗∗ | 0.5629∗∗∗ | -0.1873∗∗∗ | 2.2877∗∗∗ | 7.0555∗∗ | 4.4506∗∗∗ |                  |        |
| ----- | --------- | --------- | --------- | --------- | ---------- | --------- | -------- | --------- | ---------------- | ------ |
| SENTI |           |           |           |           |            |           |          |           | -3989.78 8042.49 | 0.8206 |
EPUI 0.0536∗∗∗ 0.0370∗∗∗ 0.9588∗∗∗ 0.8557 0.0597∗∗ 2.1970∗∗∗ 6.4966∗∗∗ 4.1478∗∗∗ -3994.89 8052.71 0.4198
| EERUS | 0.0507∗∗ | 0.0337∗∗∗ | 0.9592∗∗∗ |        |         |        | 3.8472∗∗∗ | 4.4914∗∗∗ |                  |        |
| ----- | -------- | --------- | --------- | ------ | ------- | ------ | --------- | --------- | ---------------- | ------ |
|       |          |           |           | 0.5893 | -0.3873 | 2.4038 |           |           | -3996.03 8054.99 | 0.3168 |
MOVE 0.0534∗∗∗ 0.0374∗∗∗ 0.9578∗∗∗ 0.8820 0.0190 4.0866 25.3003 4.2914∗∗∗ -3995.45 8053.83 0.1418
VIX 0.0528∗∗∗ 0.0381∗∗∗ 0.9581∗∗∗ 0.9821∗∗ 0.0030 14.2641∗ 78.7089 4.3137∗∗∗ -3997.75 8058.43 0.0136
|      | 0.0531∗∗∗ | 0.0374∗∗∗ | 0.9594∗∗∗ | 1.0675∗∗ | 0.0039∗∗ | 465.8977∗∗∗ | 89.4272∗∗∗ | 4.3558∗∗∗ |                  |        |
| ---- | --------- | --------- | --------- | -------- | -------- | ----------- | ---------- | --------- | ---------------- | ------ |
| TB3M |           |           |           |          |          |             |            |           | -3995.46 8053.85 | 0.0870 |
TED 0.0518∗∗∗ 0.0373∗∗∗ 0.9587∗∗∗ 0.7173 0.0257 1.3768∗∗∗ 1.2248∗∗ 4.2911∗∗∗ -3997.00 8056.93 0.0863
GREA 0.0513∗∗∗ 0.0342∗∗∗ 0.9583∗∗∗ 0.3619 0.0146∗∗∗ 347.4642∗∗ 501.3855∗∗ 4.3382∗∗∗ -3991.69 8046.31 0.5259
quarterlyvariances
|     | 0.0539∗∗∗ | 0.0361∗∗∗ | 0.9589∗∗∗ |        | 0.0679∗∗ | 33.8917∗∗∗ | 332.4765∗∗∗ | 4.3598∗∗∗ |                  |        |
| --- | --------- | --------- | --------- | ------ | -------- | ---------- | ----------- | --------- | ---------------- | ------ |
| PPI |           |           |           | 0.7325 |          |            |             |           | -3996.31 8055.55 | 0.0970 |
IP 0.0546∗∗ 0.0348∗∗∗ 0.9600∗∗∗ 0.7194 0.0910∗∗ 33.6692 332.2703 4.3355∗∗∗ -3994.91 8052.75 0.1492
SENTI 0.0537∗∗∗ 0.0351∗∗∗ 0.9542∗∗∗ -1.0135 1.2936∗∗∗ 1.0558∗∗∗ 1.0443∗∗∗ 4.3795∗∗∗ -3994.91 8052.75 0.4641
|      | 0.0534∗∗∗ | 0.0371∗∗∗ | 0.9592∗∗∗ |        | 0.0735∗ | 36.8038∗ | 354.9241∗ | 4.3153∗∗∗ |                  |        |
| ---- | --------- | --------- | --------- | ------ | ------- | -------- | --------- | --------- | ---------------- | ------ |
| EPUI |           |           |           | 0.9208 |         |          |           |           | -3996.44 8055.81 | 0.0621 |
EERUS 0.0501∗∗∗ 0.0332∗∗∗ 0.9642∗∗∗ 0.6495 0.2513∗∗ 74.4816∗∗ 27.6554∗∗ 4.3852∗∗∗ -3993.72 8050.38 0.2685
|      | 0.0540∗∗∗ | 0.0377∗∗∗ | 0.9585∗∗∗ |        |        |        |         | 4.3105∗∗∗ |                  |        |
| ---- | --------- | --------- | --------- | ------ | ------ | ------ | ------- | --------- | ---------------- | ------ |
| MOVE |           |           |           | 0.9247 | 0.0567 | 7.6241 | 53.8093 |           | -3997.41 8057.75 | 0.0301 |
VIX 0.0519∗∗∗ 0.0372∗∗∗ 0.9594∗∗∗ 0.9492∗∗ 0.0627∗∗∗ 308.5964 357.9909 4.3818∗∗∗ -3995.93 8054.79 0.0862
TB3M 0.0518∗∗∗ 0.0344∗∗∗ 0.9576∗∗∗ 1.0640∗∗∗ -1.2912∗∗∗ 13.9594∗∗ 9.5808∗ 4.4049∗∗∗ -3994.24 8051.41 0.5110
|     | 0.0537∗∗∗ | 0.0348∗∗∗ | 0.9617∗∗∗ | 0.9349∗ | 0.0442∗∗∗ | 15.9730∗∗∗ | 142.1546∗∗∗ | 4.3178∗∗∗ |                  |        |
| --- | --------- | --------- | --------- | ------- | --------- | ---------- | ----------- | --------- | ---------------- | ------ |
| TED |           |           |           |         |           |            |             |           | -3994.20 8051.33 | 0.1027 |
GREA 0.0536∗∗∗ 0.0378∗∗∗ 0.9585∗∗∗ 0.9805∗∗ 0.0095 1.2144 195.9439 4.3257∗∗∗ -3998.13 8059.19 0.0063
Table15: GARCH-MIDASestimationresultsforGoldlogreturns02Jan2006-31Dec2015withK = 16andBeta-
Theasterisks∗∗∗,∗∗,and∗indicatesignificanceat1%,5%,and10%,respectively.
weightingscheme.
34
Electronic copy available at: https://ssrn.com/abstract=3294967

|     | µ   | α   | β   | m   | θ   | ω1  | ω2  | ν   | LogL BIC | VR  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
GARCH 0.0256 0.0267∗∗∗ 0.9693∗∗∗ 0.8990∗∗∗ 4.0100∗∗∗ -4328.07 8695.48 –
|          |        | 0.0260∗∗∗ | 0.9350∗∗∗ |         | 0.0052∗∗∗ |        | 83.3781∗∗ | 4.0128∗∗∗ |                  |        |
| -------- | ------ | --------- | --------- | ------- | --------- | ------ | --------- | --------- | ---------------- | ------ |
| GARCH-RV | 0.0293 |           |           | -0.0256 |           | 1.0096 |           |           | -4311.63 8686.19 | 1.0460 |
quarterlygrowthrates
PPI 0.0265 0.0236∗∗∗ 0.9718∗∗∗ 1.9031∗∗∗ -1.5942∗ 2.5646∗ 8.8017 3.9515∗∗∗ -4325.63 8714.19 0.1959
IP 0.0235 0.0217∗∗∗ 0.9726∗∗∗ 1.2240∗∗∗ -0.4997∗ 26.3244 8.3590 4.0081∗∗∗ -4323.26 8709.46 0.5734
|       |        | 0.0250∗∗∗ | 0.9709∗∗∗ | 1.0632∗∗∗ |         |        | 2.3737∗ | 3.8982∗∗∗ |                  |        |
| ----- | ------ | --------- | --------- | --------- | ------- | ------ | ------- | --------- | ---------------- | ------ |
| SENTI | 0.0248 |           |           |           | -0.1306 | 8.0119 |         |           | -4326.37 8715.68 | 0.1898 |
EPUI 0.0258 0.0255∗∗∗ 0.9711∗∗∗ 0.8139∗∗ 0.0440 1.8150 1.5926 4.0071∗∗∗ -4327.73 8718.40 0.0458
EERUS 0.0243 0.0251∗∗∗ 0.9703∗∗∗ 0.8453∗∗∗ -0.1283∗ 71.0667 31.5628 4.0634∗∗∗ -4323.69 8710.31 0.1850
MOVE 0.0248 0.0277∗∗∗ 0.9665∗∗∗ 1.1603∗∗∗ -0.1078∗∗∗ 5.2926∗∗ 6.0696∗∗∗ 3.8375∗∗∗ -4323.78 8710.50 0.3425
VIX 0.0251 0.0260∗∗∗ 0.9701∗∗∗ 0.9104∗∗∗ -0.0027 1.1029 103.0630 4.0076∗∗∗ -4326.71 8716.35 0.0243
|      |        | 0.0271∗∗∗ | 0.9688∗∗∗ | 0.9103∗∗∗ |        |        |         | 4.0003∗∗∗ |                  |        |
| ---- | ------ | --------- | --------- | --------- | ------ | ------ | ------- | --------- | ---------------- | ------ |
| TB3M | 0.0255 |           |           |           | 0.0023 | 1.0091 | 83.7994 |           | -4327.98 8718.90 | 0.0047 |
TED 0.0260 0.0210∗∗∗ 0.9750∗∗∗ 1.1719∗∗∗ -0.0577∗∗ 7.3549 3.2300∗∗ 3.9547∗∗∗ -4323.09 8709.13 0.7070
GREA 0.0258 0.0265∗∗∗ 0.9659∗∗∗ 1.3515∗∗∗ 0.0653∗∗∗ 2.5013∗∗∗ 1.0000∗∗∗ 3.9074∗∗∗ -4323.11 8709.15 0.5908
quarterlyvariances
|     |        | 0.0250∗∗∗ | 0.9709∗∗∗ | 0.5932∗ | 2.0331∗∗ |         |         | 3.9071∗∗∗ |                  |        |
| --- | ------ | --------- | --------- | ------- | -------- | ------- | ------- | --------- | ---------------- | ------ |
| PPI | 0.0255 |           |           |         |          | 23.6553 | 22.3869 |           | -4324.55 8712.04 | 0.3095 |
IP 0.0243 0.0248∗∗∗ 0.9698∗∗∗ 1.1851∗∗∗ -0.7281 9.5033 9.2858 4.0277∗∗∗ -4326.21 8715.36 0.1139
SENTI 0.0232 0.0252∗∗∗ 0.9707∗∗∗ 0.4672 0.9662 1.8210 3.6961 3.9573∗∗∗ -4325.41 8713.75 0.2096
|      |        | 0.0237∗∗∗ | 0.9711∗∗∗ |        | 0.5371∗ |         |        | 4.0525∗∗∗ |                  |        |
| ---- | ------ | --------- | --------- | ------ | ------- | ------- | ------ | --------- | ---------------- | ------ |
| EPUI | 0.0243 |           |           | 0.3670 |         | 11.3211 | 4.7761 |           | -4325.75 8714.43 | 0.3068 |
EERUS 0.0249 0.0251∗∗∗ 0.9672∗∗∗ 0.1209 0.6854 1.9638 7.5044 4.0094∗∗∗ -4324.44 8711.81 0.2996
|      |        | 0.0248∗∗∗ | 0.9699∗∗∗ | 1.5228∗∗∗ | -0.7865∗∗∗ | 6.0742∗∗ | 7.3216∗∗ | 3.8945∗∗∗ |                  |        |
| ---- | ------ | --------- | --------- | --------- | ---------- | -------- | -------- | --------- | ---------------- | ------ |
| MOVE | 0.0236 |           |           |           |            |          |          |           | -4323.23 8709.39 | 0.4685 |
VIX 0.0256 0.0276∗∗∗ 0.9680∗∗∗ 0.6562∗∗ 0.4084∗∗ 4.0166∗∗ 16.2990∗ 3.9070∗∗∗ -4324.78 8712.50 0.1503
TB3M 0.0257 0.0266∗∗∗ 0.9695∗∗∗ 0.8351∗∗∗ 1.0013 10.3411 76.6569 4.0069∗∗∗ -4327.47 8717.88 0.0169
|     |        | 0.0252∗∗∗ | 0.9690∗∗∗ | 1.0498∗∗∗ | -0.4232∗∗ |        |         | 4.0432∗∗∗ |                  |        |
| --- | ------ | --------- | --------- | --------- | --------- | ------ | ------- | --------- | ---------------- | ------ |
| TED | 0.0259 |           |           |           |           | 2.3613 | 18.6653 |           | -4323.46 8709.85 | 0.2514 |
GREA 0.0250 0.0261∗∗∗ 0.9680∗∗∗ 0.2193 2.0565∗∗∗ 1.4045∗∗∗ 2.4596∗∗∗ 3.8446∗∗∗ -4323.41 8709.76 0.4006
Table 16: GARCH-MIDAS estimation results for Silver log returns 01 Jan 1996-30 Dec 2005 with K = 16 and
Theasterisks∗∗∗,∗∗,and∗indicatesignificanceat1%,5%,and10%,respectively.
Beta-weightingscheme.
|     | µ   | α   | β   | m   | θ   | ω1  | ω2  | ν   | LogL | BIC VR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------ |
GARCH 0.0437∗∗ 0.0320∗∗∗ 0.9651∗∗∗ 1.3212∗∗∗ 4.0933∗∗∗ -9821.85 19686.50 –
|          | 0.0465∗∗∗ | 0.0443∗∗ | 0.9381∗∗∗ | 0.7810∗∗ | 0.0024∗∗∗ |        | 83.0789∗ | 3.9107∗∗∗ |                   |        |
| -------- | --------- | -------- | --------- | -------- | --------- | ------ | -------- | --------- | ----------------- | ------ |
| GARCH-RV |           |          |           |          |           | 1.0099 |          |           | -9807.06 19682.60 | 0.6349 |
quarterlygrowthrates
PPI 0.0438∗∗ 0.0313∗∗∗ 0.9661∗∗∗ 1.8006∗∗ -0.8058 3.8597 3.5828 4.1071∗∗∗ -9821.54 19711.56 0.0328
IP 0.0413∗∗ 0.0313∗∗∗ 0.9638∗∗∗ 1.6979∗∗∗ -0.5755∗∗∗ 7.9290∗∗ 3.2556∗∗ 3.9458∗∗∗ -9810.22 19688.91 0.5929
|       | 0.0432∗∗ | 0.0310∗∗∗ | 0.9660∗∗∗ | 1.4688∗∗∗ |         |        |        | 4.0162∗∗∗ |                   |        |
| ----- | -------- | --------- | --------- | --------- | ------- | ------ | ------ | --------- | ----------------- | ------ |
| SENTI |          |           |           |           | -0.1096 | 6.3735 | 1.9238 |           | -9818.16 19704.79 | 0.1200 |
EPUI 0.0432∗∗∗ 0.0304∗∗∗ 0.9670∗∗∗ 1.0527∗∗∗ 0.1041∗∗∗ 1.3912∗∗∗ 1.0160∗∗∗ 4.0715∗∗∗ -9817.14 19702.77 0.2633
| EERUS | 0.0433∗∗∗ | 0.0332∗∗∗ | 0.9633∗∗∗ | 1.3684∗∗∗ |         |         |        | 4.0422∗∗∗ |                   |        |
| ----- | --------- | --------- | --------- | --------- | ------- | ------- | ------ | --------- | ----------------- | ------ |
|       |           |           |           |           | -0.1165 | 10.6712 | 6.3816 |           | -9820.93 19710.34 | 0.0468 |
MOVE 0.0424∗∗ 0.0330∗∗∗ 0.9640∗∗∗ 1.5793∗∗∗ -0.0989∗∗∗ 4.8681∗∗∗ 6.2699∗∗∗ 4.0090∗∗∗ -9815.79 19700.06 0.5141
VIX 0.0432∗∗ 0.0323∗∗∗ 0.9648∗∗∗ 1.3804∗∗∗ -0.0177 1.0000 1.5541 4.1158∗∗∗ -9821.13 19710.75 0.0127
|      | 0.0437∗∗ | 0.0319∗∗∗ | 0.9652∗∗∗ | 1.3197∗∗∗ | -0.0002∗∗∗ | 1.0091∗ | 83.8038∗∗∗ | 4.0940∗∗∗ |                   |        |
| ---- | -------- | --------- | --------- | --------- | ---------- | ------- | ---------- | --------- | ----------------- | ------ |
| TB3M |          |           |           |           |            |         |            |           | -9821.83 19712.15 | 0.0001 |
TED 0.0436∗∗∗ 0.0324∗∗∗ 0.9645∗∗∗ 1.1627∗∗∗ 0.0187 2.8007 1.0278∗∗∗ 4.0941∗∗∗ -9820.27 19709.03 0.0555
GREA 0.0409∗∗ 0.0343∗∗∗ 0.9585∗∗∗ 1.2123∗∗∗ 0.0303∗∗∗ 1.7438∗∗∗ 1.0000∗∗∗ 3.8106∗∗∗ -9805.35 19679.18 0.7758
quarterlyvariances
|     | 0.0423∗∗∗ | 0.0328∗∗∗ | 0.9624∗∗∗ | 1.0157∗∗∗ | 0.5806∗∗∗ |        | 2.0668∗∗ | 3.8862∗∗∗ |                   |        |
| --- | --------- | --------- | --------- | --------- | --------- | ------ | -------- | --------- | ----------------- | ------ |
| PPI |           |           |           |           |           | 3.8481 |          |           | -9809.51 19687.49 | 0.6934 |
IP 0.0431 0.0310∗∗∗ 0.9663∗∗∗ 1.1171∗ 0.4158 11.7699 5.1126 4.0287∗∗∗ -9814.09 19696.67 0.4184
SENTI 0.0429∗∗∗ 0.0324∗∗∗ 0.9621∗∗∗ 0.5284∗ 1.0944∗∗∗ 1.1030∗∗∗ 1.1206∗∗∗ 3.9014∗∗∗ -9812.88 19694.23 0.5758
|      | 0.0425∗∗∗ | 0.0331∗∗∗ | 0.9624∗∗∗ | 0.8464∗∗∗ | 0.5059∗∗∗ | 7.7741∗∗∗ | 2.3468∗∗∗ | 4.0287∗∗∗ |                   |        |
| ---- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | ----------------- | ------ |
| EPUI |           |           |           |           |           |           |           |           | -9815.66 19699.80 | 0.3144 |
EERUS 0.0430∗∗ 0.0348∗∗∗ 0.9588∗∗∗ 0.0987 1.1393∗∗∗ 1.0000∗∗∗ 1.0035∗∗∗ 3.9217∗∗∗ -9812.08 19692.65 0.5212
|      | 0.0440∗∗ | 0.0315∗∗∗ | 0.9654∗∗∗ | 1.2063∗∗∗ |        | 2.8670∗∗ | 17.8667∗∗∗ | 4.0923∗∗∗ |                   |        |
| ---- | -------- | --------- | --------- | --------- | ------ | -------- | ---------- | --------- | ----------------- | ------ |
| MOVE |          |           |           |           | 0.0900 |          |            |           | -9820.99 19710.47 | 0.0207 |
VIX 0.0438∗∗ 0.0330∗∗∗ 0.9637∗∗∗ 1.1519∗∗∗ 0.2404 3.3450∗∗∗ 7.9462∗ 4.0268∗∗∗ -9820.63 19709.73 0.0866
TB3M 0.0438 0.0335∗∗∗ 0.9629∗∗∗ 1.1401∗∗∗ 1.5771 1.9279 4.7203 3.9665∗∗∗ -9817.53 19703.54 0.3332
|     | 0.0426∗∗ | 0.0318∗∗∗ | 0.9648∗∗∗ | 1.0386∗∗ |        |        |        | 3.9782∗∗∗ |                   |        |
| --- | -------- | --------- | --------- | -------- | ------ | ------ | ------ | --------- | ----------------- | ------ |
| TED |          |           |           |          | 0.3296 | 9.2090 | 3.9062 |           | -9812.80 19694.08 | 0.5940 |
GREA 0.0429∗ 0.0328∗∗∗ 0.9634∗∗∗ 1.1146∗ 0.3024 6.6235 3.9496 3.9844∗∗∗ -9814.33 19697.14 0.4840
Table 17: GARCH-MIDAS estimation results for Silver log returns 01 Jan 1996-31 Dec 2015 with K = 16 and
Theasterisks∗∗∗,∗∗,and∗indicatesignificanceat1%,5%,and10%,respectively.
Beta-weightingscheme.
35
Electronic copy available at: https://ssrn.com/abstract=3294967

|     | µ   | α   | β   | m   | θ   | ω1  | ω2  | ν   | LogL BIC | VR  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
GARCH 0.0907∗∗∗ 0.0375∗∗∗ 0.9587∗∗∗ 2.1132∗∗∗ 3.8691∗∗∗ -5483.77 11006.88 –
|          | 0.0993∗∗∗ | 0.0548∗∗∗ | 0.8743∗∗∗ | 0.9295∗∗∗ | 0.0019∗∗∗ | 1.0095∗∗ | 83.4410∗∗∗ | 4.1106∗∗∗ |                   |        |
| -------- | --------- | --------- | --------- | --------- | --------- | -------- | ---------- | --------- | ----------------- | ------ |
| GARCH-RV |           |           |           |           |           |          |            |           | -5468.47 10999.88 | 0.9018 |
quarterlygrowthrates
PPI 0.0913∗∗∗ 0.0348∗∗∗ 0.9621∗∗∗ 2.4923∗∗∗ -0.6830 9.8578 5.0049 3.9153∗∗∗ -5483.29 11029.52 0.0970
IP 0.0878∗∗∗ 0.0364∗∗∗ 0.9587∗∗∗ 2.1420∗∗∗ -0.2459∗∗∗ 179.9227 82.6539 3.8218∗∗∗ -5476.51 11015.96 0.4993
|       | 0.0897∗∗ | 0.0417∗∗∗ | 0.9431∗∗∗ | 1.9118∗∗∗ | -0.2218∗ |        |        | 3.7376∗∗∗ |                   |        |
| ----- | -------- | --------- | --------- | --------- | -------- | ------ | ------ | --------- | ----------------- | ------ |
| SENTI |          |           |           |           |          | 1.9385 | 3.9716 |           | -5477.23 11017.40 | 0.6529 |
EPUI 0.0902∗∗∗ 0.0374∗∗∗ 0.9587∗∗∗ 2.0856∗∗∗ 0.0012 81.9244 1.6282 3.8775∗∗∗ -5483.64 11030.21 0.0026
EERUS 0.0874∗∗∗ 0.0348∗∗∗ 0.9585∗∗∗ 1.8484∗∗∗ -0.4669∗∗ 1.8373∗ 3.5444∗∗∗ 3.8450∗∗∗ -5478.97 11020.87 0.5169
MOVE 0.0888∗∗∗ 0.0369∗∗∗ 0.9600∗∗∗ 2.2329∗∗∗ 0.0205 48.2304 17.1513 3.8579∗∗∗ -5481.21 11025.35 0.1320
VIX 0.0909∗∗∗ 0.0373∗∗∗ 0.9588∗∗∗ 2.0690∗∗∗ 0.0020 145.5044 1.3124∗∗∗ 3.8846∗∗∗ -5483.30 11029.53 0.0094
|      | 0.0876∗∗ | 0.0306∗∗∗ | 0.9659∗∗∗ | 1.8408∗∗∗ | 0.0100∗ |         |         | 4.0344∗∗∗ |                   |        |
| ---- | -------- | --------- | --------- | --------- | ------- | ------- | ------- | --------- | ----------------- | ------ |
| TB3M |          |           |           |           |         | 22.8378 | 38.3590 |           | -5479.86 11022.65 | 0.2495 |
TED 0.0859∗∗∗ 0.0447∗∗∗ 0.9420∗∗∗ 1.1699∗∗∗ 0.0665∗∗∗ 1.4902∗∗∗ 1.6795∗∗∗ 3.6900∗∗∗ -5477.28 11017.50 0.5806
GREA 0.0856∗∗∗ 0.0394∗∗∗ 0.9461∗∗∗ 1.4230∗∗∗ 0.0179∗∗∗ 287.3127∗∗∗ 416.9896∗∗∗ 3.7682∗∗∗ -5472.45 11007.82 0.7409
quarterlyvariances
|     | 0.0849∗∗∗ | 0.0359∗∗∗ | 0.9614∗∗∗ | 1.9179∗∗∗ | 0.4612∗ |        |        | 3.6182∗∗∗ |                   |        |
| --- | --------- | --------- | --------- | --------- | ------- | ------ | ------ | --------- | ----------------- | ------ |
| PPI |           |           |           |           |         | 5.4713 | 2.5666 |           | -5475.67 11014.28 | 0.9643 |
IP 0.0871∗∗∗ 0.0345∗∗∗ 0.9613∗∗∗ 1.8278∗∗∗ 0.3100∗∗ 13.8031 5.9790 3.7692∗∗∗ -5476.30 11015.54 0.6944
SENTI 0.0921∗∗∗ 0.0377∗∗∗ 0.9583∗∗∗ 1.8458∗∗∗ 0.3124∗ 14.0765 3.1050∗ 3.8052∗∗∗ -5481.10 11025.14 0.2584
|      | 0.0907∗∗∗ | 0.0337∗∗∗ | 0.9630∗∗∗ | 2.1305∗∗∗ | -0.0776∗ | 362.5067∗∗∗ | 406.4929∗∗∗ | 3.9312∗∗∗ |                   |        |
| ---- | --------- | --------- | --------- | --------- | -------- | ----------- | ----------- | --------- | ----------------- | ------ |
| EPUI |           |           |           |           |          |             |             |           | -5482.07 11027.06 | 0.0681 |
EERUS 0.0845∗∗∗ 0.0380∗∗∗ 0.9561∗∗∗ 0.9829∗∗ 0.7489∗∗∗ 1.8372 1.9628∗∗ 3.7743∗∗∗ -5478.60 11020.14 0.6017
|      | 0.0904∗∗∗ | 0.0346∗∗∗ | 0.9620∗∗∗ | 2.1397∗∗∗ | -0.0851∗ | 326.3961∗∗ | 367.8816∗∗ | 3.9291∗∗∗ |                   |        |
| ---- | --------- | --------- | --------- | --------- | -------- | ---------- | ---------- | --------- | ----------------- | ------ |
| MOVE |           |           |           |           |          |            |            |           | -5481.69 11026.31 | 0.0811 |
VIX 0.0881∗∗∗ 0.0368∗∗∗ 0.9550∗∗∗ 2.1525∗∗∗ -0.1949∗ 20.5215 9.7711 3.8327∗∗∗ -5480.11 11023.15 0.2124
TB3M 0.0856∗∗ 0.0403∗∗∗ 0.9513∗∗∗ 2.2544∗∗∗ -1.0564∗∗ 13.2454 5.1491 3.8439∗∗∗ -5480.91 11024.75 0.3405
|     | 0.0903∗∗∗ | 0.0375∗∗∗ | 0.9586∗∗∗ | 2.0368∗∗∗ | 0.0866∗∗ |         |         | 3.7756∗∗∗ |                   |        |
| --- | --------- | --------- | --------- | --------- | -------- | ------- | ------- | --------- | ----------------- | ------ |
| TED |           |           |           |           |          | 17.1358 | 30.7011 |           | -5481.07 11025.08 | 0.1611 |
GREA 0.0887∗∗∗ 0.0353∗∗∗ 0.9615∗∗∗ 1.9409∗∗∗ 0.1567 16.5214 9.0003 3.8249∗∗∗ -5479.60 11022.12 0.4984
Table 18: GARCH-MIDAS estimation results for Silver log returns 02 Jan 2006-31 Dec 2015 with K = 16 and
Theasterisks∗∗∗,∗∗,and∗indicatesignificanceat1%,5%,and10%,respectively.
Beta-weightingscheme.
|     | µ   | α   | β   | m   | θ   | ω1  | ω2  | ν   | LogL BIC | VR  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
GARCH 0.0339∗ 0.1586 0.8150∗∗∗ 1.2934∗∗ 3.4664∗∗∗ -4013.71 8066.76 –
|     | 0.0323∗ |     | 0.8947∗∗∗ |     | 0.0035∗∗∗ |     |     | 3.8138∗∗∗ |     |     |
| --- | ------- | --- | --------- | --- | --------- | --- | --- | --------- | --- | --- |
GARCH-RV 0.0791 0.3364 1.0090 83.9702 -4002.70 8068.34 0.4224
quarterlygrowthrates
PPI 0.0333∗ 0.2578∗∗ 0.6848∗∗∗ 3.2823∗∗∗ -3.1115∗∗∗ 2.5128∗∗∗ 12.1340∗∗∗ 3.2540∗∗∗ -3992.55 8048.03 0.7136
IP 0.0342∗ 0.1589 0.8132∗∗∗ 1.2390 0.0286 81.9483 1.6262 3.4693∗∗∗ -4013.66 8090.25 0.0021
|       | 0.0304∗ |        | 0.7206∗∗ | 1.2214∗∗ | -0.2600∗∗∗ |        | 1.5212∗∗ | 3.3790∗∗∗ |                  |        |
| ----- | ------- | ------ | -------- | -------- | ---------- | ------ | -------- | --------- | ---------------- | ------ |
| SENTI |         | 0.2158 |          |          |            | 3.7847 |          |           | -4000.42 8063.77 | 0.3361 |
EPUI 0.0341∗ 0.2128 0.6749 0.6886∗∗ 0.0631∗∗∗ 15.6968∗∗ 4.1246∗∗∗ 3.4973∗∗∗ -4004.72 8072.38 0.2287
| EERUS | 0.0341∗ |        | 0.7316∗∗∗ |        | 0.2138∗∗∗ |         |         | 3.3163∗∗∗ |                  |        |
| ----- | ------- | ------ | --------- | ------ | --------- | ------- | ------- | --------- | ---------------- | ------ |
|       |         | 0.2151 |           | 1.2224 |           | 35.3422 | 55.6114 |           | -4000.45 8063.83 | 0.3790 |
MOVE 0.0277 0.2776∗∗∗ 0.6991∗∗∗ 1.6964∗∗ 0.1594∗∗∗ 11.8624∗∗∗ 3.0591∗∗∗ 3.1712∗∗∗ -3994.52 8051.98 1.0162
VIX 0.0381∗∗ 0.2031∗∗ 0.6526∗∗∗ 0.5193∗∗ 0.0535∗∗∗ 12.4498∗∗ 17.1932∗∗∗ 3.5645∗∗∗ -3999.16 8061.26 0.3510
|      | 0.0343∗∗ | 0.2459∗ | 0.6558∗∗∗ | 0.9231∗∗ | -0.0630∗∗∗ | 1.2903∗∗∗ | 1.8357∗∗∗ | 3.4004∗∗∗ |                  |        |
| ---- | -------- | ------- | --------- | -------- | ---------- | --------- | --------- | --------- | ---------------- | ------ |
| TB3M |          |         |           |          |            |           |           |           | -3999.79 8062.52 | 0.3113 |
TED 0.0311∗ 0.2491 0.6734∗∗ 1.4745∗∗ -0.0810∗∗∗ 2.4157∗∗∗ 2.1967∗∗∗ 3.3456∗∗∗ -3996.69 8056.32 0.3832
GREA 0.0353∗∗ 0.1719∗ 0.7982∗∗∗ 1.4817∗∗ 0.0183∗∗ 82.0635∗∗∗ 1.6174 3.4072∗∗∗ -4010.61 8084.17 0.1210
quarterlyvariances
|     | 0.0380∗ |        | 0.7067∗∗ | 1.5199∗∗∗ | -2.1606∗∗ |         |         | 3.3845∗∗∗ |                  |        |
| --- | ------- | ------ | -------- | --------- | --------- | ------- | ------- | --------- | ---------------- | ------ |
| PPI |         | 0.2257 |          |           |           | 55.1574 | 13.8272 |           | -4005.06 8073.06 | 0.3001 |
IP 0.0356 0.1887 0.7544 0.7661 0.6056 85.9877 26.9975 3.4357∗∗∗ -4006.44 8075.82 0.2591
SENTI 0.0312∗ 0.2359∗ 0.7218∗∗∗ 0.8482 1.3691∗∗∗ 7.9020∗∗∗ 28.7594∗∗ 3.3212∗∗∗ -3997.67 8058.28 0.5587
|      | 0.0331∗ |        | 0.7969∗∗∗ | 1.1877∗∗ | 0.1453∗ | 149.8911∗∗ | 523.9091∗∗ | 3.4414∗∗∗ |                  |        |
| ---- | ------- | ------ | --------- | -------- | ------- | ---------- | ---------- | --------- | ---------------- | ------ |
| EPUI |         | 0.1728 |           |          |         |            |            |           | -4011.60 8086.13 | 0.0530 |
EERUS 0.0404∗∗ 0.2106∗∗∗ 0.5791∗∗∗ 1.3501∗∗∗ -0.7587∗∗∗ 20.7528∗∗∗ 31.0566∗∗∗ 3.6414∗∗∗ -3996.97 8056.88 0.3435
|      |        | 0.3876∗∗∗ | 0.6095∗∗∗ | 5.9311∗∗∗ | -3.0950∗∗ | 21.0106∗∗∗ | 21.3607∗∗∗ | 3.3348∗∗∗ |                  |        |
| ---- | ------ | --------- | --------- | --------- | --------- | ---------- | ---------- | --------- | ---------------- | ------ |
| MOVE | 0.0021 |           |           |           |           |            |            |           | -3986.76 8036.47 | 9.9683 |
VIX 0.0233 0.2835∗∗∗ 0.7061∗∗∗ 4.9491∗ -2.7049 5.1241 4.8063 3.1888∗∗∗ -3989.07 8041.07 1.1482
TB3M 0.0302∗ 0.1901∗ 0.7805∗∗∗ 0.9941 7.1550∗∗∗ 20.5930 28.3359 3.4395∗∗∗ -4006.26 8075.47 0.2142
|     | 0.0386∗∗ |     |     |     | 0.3116∗∗ |     |     | 3.4125∗∗∗ |     |     |
| --- | -------- | --- | --- | --- | -------- | --- | --- | --------- | --- | --- |
TED 0.2278 0.6869 0.8365 1.0746 47.3333 -4009.09 8081.11 0.1941
GREA 0.0293 0.3390∗ 0.6287∗∗∗ 2.5732 -1.9193 110.8338 13.6325 3.2338∗∗∗ -4002.47 8067.88 1.1297
Table 19: GARCH-MIDAS estimation results for Platinum log returns 01 Jan 1996-30 Dec 2005 with K = 16 and
Theasterisks∗∗∗,∗∗,and∗indicatesignificanceat1%,5%,and10%,respectively.
Beta-weightingscheme.
36
Electronic copy available at: https://ssrn.com/abstract=3294967

|     | µ α | β   | m   | θ   | ω1  | ω2  | ν   | LogL BIC | VR  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
GARCH 0.0330∗∗ 0.0518∗∗∗ 0.9388∗∗∗ 0.7359∗∗∗ 4.7068∗∗∗ -8459.52 16961.84 –
|          | 0.0335∗∗ 0.0700∗∗∗ | 0.8912∗∗∗ |        | 0.0036∗∗∗ | 1.0094∗∗∗ | 83.5819∗∗∗ | 4.9570∗∗∗ |                   |        |
| -------- | ------------------ | --------- | ------ | --------- | --------- | ---------- | --------- | ----------------- | ------ |
| GARCH-RV |                    |           | 0.1348 |           |           |            |           | -8432.08 16932.63 | 0.6199 |
quarterlygrowthrates
PPI 0.0335∗∗ 0.0553∗∗∗ 0.9326∗∗∗ 1.4729∗∗∗ -1.3339∗∗∗ 2.5123∗∗∗ 7.4165∗∗ 4.5780∗∗∗ -8453.98 16976.44 0.2098
IP 0.0316∗∗ 0.0581∗∗∗ 0.9267∗∗∗ 0.9541∗∗∗ -0.4889∗∗∗ 1.0000 2.0819 4.5984∗∗∗ -8452.55 16973.58 0.3059
|       | 0.0331∗∗ 0.0507∗∗∗ | 0.9386∗∗∗ | 0.7362∗∗∗ |         |         |         | 4.6768∗∗∗ |                   |        |
| ----- | ------------------ | --------- | --------- | ------- | ------- | ------- | --------- | ----------------- | ------ |
| SENTI |                    |           |           | -0.0631 | 21.1998 | 21.8385 |           | -8456.72 16981.91 | 0.0820 |
EPUI 0.0340∗∗ 0.0651∗ 0.9111∗∗∗ 0.4465∗∗∗ 0.0820∗∗∗ 1.8464∗∗ 4.2458 4.6069∗∗∗ -8452.31 16973.11 0.3451
EERUS 0.0335∗∗ 0.0503∗∗∗ 0.9407∗∗∗ 0.7561∗∗∗ 0.2414∗∗∗ 5.9780∗∗ 9.7761∗∗ 4.6249∗∗∗ -8453.59 16975.67 0.2373
MOVE 0.0317∗∗ 0.0522∗∗∗ 0.9396∗∗∗ 0.8088∗∗∗ -0.0473 2.8624 4.6507 4.6995∗∗∗ -8458.52 16985.52 0.1128
VIX 0.0345∗∗ 0.0492∗∗∗ 0.9348∗∗∗ 0.4568∗∗ 0.0461∗ 8.3231 11.4871 4.6300∗∗∗ -8450.06 16968.60 0.2675
|      | 0.0334∗∗ 0.0524∗∗∗ | 0.9376∗∗∗ | 0.7355∗∗∗ |        | 78.4182∗ |        | 4.6778∗∗∗ |                   |        |
| ---- | ------------------ | --------- | --------- | ------ | -------- | ------ | --------- | ----------------- | ------ |
| TB3M |                    |           |           | 0.0026 |          | 8.0393 |           | -8458.93 16986.35 | 0.0128 |
TED 0.0335∗∗ 0.0491∗∗∗ 0.9428∗∗∗ 0.8346∗∗∗ -0.0160 1.0000 1.7985∗∗ 4.7439∗∗∗ -8458.59 16985.67 0.0399
GREA 0.0315∗∗ 0.0535∗∗∗ 0.9358∗∗∗ 0.6453∗∗∗ 0.0128∗∗∗ 6.1040 3.0419 4.6273∗∗∗ -8454.99 16978.47 0.1994
quarterlyvariances
|     | 0.0322∗∗ 0.0567∗∗∗ | 0.9279∗∗∗ | 0.4254∗∗ |        |        |        | 4.5680∗∗∗ |                   |        |
| --- | ------------------ | --------- | -------- | ------ | ------ | ------ | --------- | ----------------- | ------ |
| PPI |                    |           |          | 0.3385 | 1.0000 | 2.7265 |           | -8451.67 16971.83 | 0.2871 |
IP 0.0326∗ 0.0543∗∗∗ 0.9335∗∗∗ 0.4305 0.3813 1.0000 1.0077∗∗∗ 4.6311∗∗∗ -8455.44 16979.35 0.1471
SENTI 0.0333 0.0484∗∗∗ 0.9379∗∗∗ 0.3791 0.3483 8.8676 42.0634 4.6234∗∗∗ -8445.72 16959.92 0.3033
|      | 0.0334∗ 0.0545∗∗∗ | 0.9343∗∗∗ |        | 0.4199∗∗ |        |        | 4.6435∗∗∗ |                   |        |
| ---- | ----------------- | --------- | ------ | -------- | ------ | ------ | --------- | ----------------- | ------ |
| EPUI |                   |           | 0.2920 |          | 1.9911 | 2.7254 |           | -8456.91 16982.31 | 0.1540 |
EERUS 0.0342∗∗ 0.0472∗∗∗ 0.9425∗∗∗ 0.4624∗∗ 0.1590∗∗∗ 134.5047∗∗∗ 476.9330∗∗∗ 4.7343∗∗∗ -8455.09 16978.65 0.0767
|      | 0.0328∗∗ 0.0530∗∗∗ | 0.9364∗∗∗ | 0.5011∗∗ | 0.2338∗∗ |         |        | 4.6662∗∗∗ |                   |        |
| ---- | ------------------ | --------- | -------- | -------- | ------- | ------ | --------- | ----------------- | ------ |
| MOVE |                    |           |          |          | 24.9823 | 7.5259 |           | -8456.59 16981.67 | 0.1004 |
VIX 0.0321∗∗ 0.0502∗∗∗ 0.9398∗∗∗ 0.9216∗∗∗ -0.1957∗ 23.5924∗∗∗ 13.9511∗∗∗ 4.7352∗∗∗ -8456.27 16981.02 0.1133
TB3M 0.0329∗∗ 0.0514∗∗∗ 0.9383∗∗∗ 0.4731∗∗ 1.1478∗∗∗ 8.7651∗∗∗ 17.6852∗∗∗ 4.6256∗∗∗ -8452.49 16973.46 0.2356
|     | 0.0329∗∗ 0.0534∗∗∗ | 0.9344∗∗∗ | 0.5419∗∗∗ | 0.1390∗∗∗ |        | 15.0613∗ | 4.6330∗∗∗ |                   |        |
| --- | ------------------ | --------- | --------- | --------- | ------ | -------- | --------- | ----------------- | ------ |
| TED |                    |           |           |           | 7.9833 |          |           | -8454.88 16978.23 | 0.1449 |
GREA 0.0331∗∗ 0.0538∗∗∗ 0.9342∗∗∗ 0.5439∗∗ 0.1548∗∗ 2.4824 6.7928 4.6040∗∗∗ -8454.58 16977.64 0.1589
Table 20: GARCH-MIDAS estimation results for Platinum log returns 01 Jan 1996-31 Dec 2015 with K = 16 and
Theasterisks∗∗∗,∗∗,and∗indicatesignificanceat1%,5%,and10%,respectively.
Beta-weightingscheme.
|     | µ α | β   | m   | θ   | ω1  | ω2  | ν   | LogL BIC | VR  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
GARCH 0.0300 0.0456∗∗∗ 0.9447∗∗∗ 0.7478∗∗∗ 6.2938∗∗∗ -4425.83 8890.99 –
|     | 0.0604∗∗∗ | 0.8774∗∗∗ |     | 0.0037∗∗∗ |     |     | 6.9227∗∗∗ |     |     |
| --- | --------- | --------- | --- | --------- | --- | --- | --------- | --- | --- |
GARCH-RV 0.0311 0.0758 24.3272 255.1780 -4409.27 8881.47 0.8150
quarterlygrowthrates
PPI 0.0306 0.0440∗∗∗ 0.9437∗∗∗ 1.0334 -0.5756 12.6634 3.4820 6.2714∗∗∗ -4424.10 8911.13 0.0877
IP 0.0315 0.0529∗∗∗ 0.9253∗∗∗ 0.7417∗∗∗ -0.2508∗∗ 1.0000 5.7033 6.3182∗∗∗ -4424.12 8911.18 0.2267
|       | 0.0545∗∗∗ | 0.9139∗∗∗ | 0.7380∗∗∗ | -0.1761∗∗∗ | 2.6163∗∗∗ | 5.7937∗∗∗ | 6.4853∗∗∗ |                  |        |
| ----- | --------- | --------- | --------- | ---------- | --------- | --------- | --------- | ---------------- | ------ |
| SENTI | 0.0287    |           |           |            |           |           |           | -4422.37 8907.67 | 0.4884 |
EPUI 0.0340 0.0524∗∗∗ 0.9225∗∗∗ 0.5001∗∗∗ 0.0528∗∗∗ 6.4260∗ 14.3876∗∗ 6.2923∗∗∗ -4421.54 8906.01 0.3897
| EERUS | 0.0424∗∗ | 0.9472∗∗∗ | 0.8112∗∗∗ |        |         |        | 6.2459∗∗∗ |                  |        |
| ----- | -------- | --------- | --------- | ------ | ------- | ------ | --------- | ---------------- | ------ |
|       | 0.0304   |           |           | 0.1081 | 19.5980 | 4.4161 |           | -4423.75 8910.43 | 0.1019 |
MOVE 0.0311 0.0462∗∗∗ 0.9418∗∗∗ 0.7085∗∗∗ 0.0293 6.5894 6.5141∗∗ 6.2270∗∗∗ -4424.36 8911.65 0.1159
VIX 0.0317 0.0493∗∗ 0.9348∗∗∗ 0.5724∗∗ 0.0362 3.9869 6.6769∗∗ 6.2280∗∗∗ -4423.99 8910.92 0.1590
|      | 0.0448∗∗∗ | 0.9454∗∗∗ | 0.7415∗∗∗ |        |         |         | 6.3418∗∗∗ |                  |        |
| ---- | --------- | --------- | --------- | ------ | ------- | ------- | --------- | ---------------- | ------ |
| TB3M | 0.0296    |           |           | 0.0027 | 75.4897 | 16.0426 |           | -4425.07 8913.08 | 0.0260 |
TED 0.0303 0.0516∗∗∗ 0.9211∗∗∗ 0.4067∗∗ 0.0243∗∗ 3.8885 7.4124∗ 6.4031∗∗∗ -4422.02 8906.97 0.2929
GREA 0.0294 0.0430∗∗∗ 0.9419∗∗∗ 0.5022∗∗∗ 0.0083∗∗∗ 157.0659∗∗ 194.9784∗∗ 6.4949∗∗∗ -4422.73 8908.39 0.1519
quarterlyvariances
|     | 0.0452∗∗∗ | 0.9437∗∗∗ | 0.6786∗∗∗ |        |        |          | 6.3186∗∗∗ |                  |        |
| --- | --------- | --------- | --------- | ------ | ------ | -------- | --------- | ---------------- | ------ |
| PPI | 0.0301    |           |           | 0.0372 | 1.2090 | 186.0719 |           | -4424.98 8912.88 | 0.0355 |
IP 0.0304 0.0429∗∗∗ 0.9481∗∗∗ 0.6976∗∗∗ 0.0433 274.0033∗∗∗ 507.6348∗∗∗ 6.2969∗∗∗ -4424.74 8912.42 0.0342
SENTI 0.0301 0.0359∗∗ 0.9527∗∗∗ 0.3958∗∗ 0.1810∗∗∗ 65.6088∗∗∗ 354.0111∗∗∗ 6.4251∗∗∗ -4420.05 8903.03 0.2115
|      | 0.0454∗∗∗ | 0.9451∗∗∗ | 0.7255∗∗∗ |        |         |         | 6.2937∗∗∗ |                  |        |
| ---- | --------- | --------- | --------- | ------ | ------- | ------- | --------- | ---------------- | ------ |
| EPUI | 0.0300    |           |           | 0.0245 | 64.3915 | 14.7670 |           | -4425.72 8914.37 | 0.0036 |
EERUS 0.0312 0.0360∗∗ 0.9562∗∗∗ 0.8525∗∗∗ -0.1308∗ 365.2327∗∗ 418.5269∗∗ 6.3115∗∗∗ -4423.51 8909.96 0.0866
|     | 0.0406∗∗∗ | 0.9511∗∗∗ | 0.7785∗∗∗ |     |     |     | 6.3628∗∗∗ |     |     |
| --- | --------- | --------- | --------- | --- | --- | --- | --------- | --- | --- |
MOVE 0.0304 -0.0420 437.5169 471.1373 -4424.19 8911.31 0.0353
VIX 0.0288 0.0458∗∗∗ 0.9406∗∗∗ 0.8521∗∗∗ -0.1153∗ 28.6868 13.5037 6.4315∗∗∗ -4423.86 8910.66 0.0840
TB3M 0.0289 0.0455∗∗∗ 0.9434∗∗∗ 0.8256∗∗∗ -0.2740 14.2147 9.1240 6.3559∗∗∗ -4425.59 8914.12 0.0202
|     | 0.0431∗∗∗ | 0.9468∗∗∗ | 0.6224∗∗∗ |        |         |         | 6.2360∗∗∗ |                  |        |
| --- | --------- | --------- | --------- | ------ | ------- | ------- | --------- | ---------------- | ------ |
| TED | 0.0302    |           |           | 0.0613 | 18.2489 | 31.1852 |           | -4424.42 8911.76 | 0.0746 |
GREA 0.0309 0.0428∗∗∗ 0.9477∗∗∗ 0.7735∗∗∗ -0.0245 292.0120 416.8249 6.3483∗∗∗ -4424.89 8912.72 0.0285
Table 21: GARCH-MIDAS estimation results for Platinum log returns 02 Jan 2006-31 Dec 2015 with K = 16 and
Theasterisks∗∗∗,∗∗,and∗indicatesignificanceat1%,5%,and10%,respectively.
Beta-weightingscheme.
37
Electronic copy available at: https://ssrn.com/abstract=3294967

|     | µ   | α   | β   | m   | θ   | ω1  | ω2  | ν   | LogL BIC | VR  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
GARCH 0.0337 0.0296∗∗∗ 0.9623∗∗∗ 0.5866∗∗∗ 7.7919∗∗∗ -4296.02 8631.38 –
|          | 0.0413∗ | 0.0273∗∗ | 0.8740∗∗∗ | -0.3922∗∗∗ | 0.0076∗∗∗ | 1.0092∗ |         | 9.3249∗∗∗ |                  |        |
| -------- | ------- | -------- | --------- | ---------- | --------- | ------- | ------- | --------- | ---------------- | ------ |
| GARCH-RV |         |          |           |            |           |         | 83.7609 |           | -4274.46 8611.86 | 1.2897 |
quarterlygrowthrates
PPI 0.0351 0.0298∗∗∗ 0.9593∗∗∗ 0.0490 0.8052∗∗∗ 2.3534∗ 14.5811∗ 7.6468∗∗∗ -4293.61 8650.16 0.2351
IP 0.0328 0.0265∗∗∗ 0.9642∗∗∗ 0.7595∗∗∗ -0.2368∗∗ 69.8688 93.1873 7.7217∗∗∗ -4292.31 8647.56 0.3913
|       |        | 0.0297∗∗∗ | 0.9534∗∗∗ | 0.6121∗∗∗ | -0.2158∗∗∗ |        | 1.0305∗∗∗ | 8.1249∗∗∗ |                  |        |
| ----- | ------ | --------- | --------- | --------- | ---------- | ------ | --------- | --------- | ---------------- | ------ |
| SENTI | 0.0373 |           |           |           |            | 1.4336 |           |           | -4292.43 8647.80 | 0.4481 |
EPUI 0.0350 0.0281∗∗∗ 0.9635∗∗∗ 0.5517∗∗∗ 0.0129 57.5813 15.4331 7.9140∗∗∗ -4293.48 8649.90 0.1192
EERUS 0.0328 0.0294∗∗∗ 0.9547∗∗∗ 0.5349∗∗∗ -0.1210∗∗ 8.8021 34.7204 7.8958∗∗∗ -4293.11 8649.15 0.4082
MOVE 0.0335 0.0295∗∗∗ 0.9635∗∗∗ 0.5756∗∗∗ 0.0109∗∗ 165.2972 1.3426∗∗∗ 7.8307∗∗∗ -4291.79 8646.52 0.1743
VIX 0.0341 0.0284∗∗∗ 0.9540∗∗∗ 0.6867∗∗∗ -0.0442∗ 2.7346 6.3189 7.9551∗∗∗ -4292.48 8647.91 0.5282
|      |        | 0.0302∗∗∗ | 0.9467∗∗∗ | 0.4599∗∗∗ | -0.0384∗∗∗ |        |        | 8.1731∗∗∗ |                  |        |
| ---- | ------ | --------- | --------- | --------- | ---------- | ------ | ------ | --------- | ---------------- | ------ |
| TB3M | 0.0348 |           |           |           |            | 3.7532 | 1.4671 |           | -4292.12 8647.19 | 0.5351 |
TED 0.0326 0.0263∗∗∗ 0.9673∗∗∗ 0.5283∗∗∗ 0.0090 7.1072 45.6490 7.9765∗∗∗ -4292.44 8647.83 0.1953
GREA 0.0351 0.0302∗∗∗ 0.9535∗∗∗ 0.5230∗∗∗ 0.0107∗∗∗ 1.0942∗∗∗ 215.7361 7.9720∗∗∗ -4292.45 8647.83 0.5465
quarterlyvariances
|     |        |        | 0.9814∗∗∗ |        | 1.7909∗∗ |         | 1.2627∗∗ | 7.7372∗∗∗ |                  |        |
| --- | ------ | ------ | --------- | ------ | -------- | ------- | -------- | --------- | ---------------- | ------ |
| PPI | 0.0307 | 0.0140 |           | 0.2032 |          | 16.4393 |          |           | -4287.23 8637.40 | 0.7699 |
IP 0.0347 0.0298∗∗∗ 0.9589∗∗∗ 0.9351∗∗∗ -0.7060∗ 8.2033∗ 19.8492∗∗ 7.8330∗∗∗ -4293.06 8649.06 0.4240
SENTI 0.0346 0.0314∗∗∗ 0.9587∗∗∗ 0.5201∗∗∗ 0.1329 12.1836 73.1224 7.8001∗∗∗ -4295.40 8653.74 0.0397
|      |        | 0.0267∗∗∗ | 0.9650∗∗∗ | 0.3415∗∗ | 0.2801∗∗∗ | 44.8413∗∗∗ | 76.6800∗∗ | 7.8621∗∗∗ |                  |        |
| ---- | ------ | --------- | --------- | -------- | --------- | ---------- | --------- | --------- | ---------------- | ------ |
| EPUI | 0.0331 |           |           |          |           |            |           |           | -4290.06 8643.06 | 0.4668 |
EERUS 0.0334 0.0295∗∗∗ 0.9631∗∗∗ 0.5552∗∗∗ 0.0500 539.9855 362.1371 7.7629∗∗∗ -4295.79 8654.51 0.0112
|      |        | 0.0297∗∗∗ | 0.9600∗∗∗ | 0.6920∗∗∗ |         |         |         | 7.8497∗∗∗ |                  |        |
| ---- | ------ | --------- | --------- | --------- | ------- | ------- | ------- | --------- | ---------------- | ------ |
| MOVE | 0.0356 |           |           |           | -0.1632 | 30.3358 | 90.4268 |           | -4293.46 8649.86 | 0.2200 |
VIX 0.0361 0.0308∗∗∗ 0.9607∗∗∗ 0.7287∗∗ -0.1846 58.1115 10.6744 8.1741∗∗∗ -4291.18 8645.29 0.2935
TB3M 0.0351 0.0247∗∗∗ 0.9644∗∗∗ 0.2718∗ 4.4812∗∗∗ 22.4442∗∗∗ 48.3471∗∗∗ 7.7858∗∗∗ -4290.20 8643.34 0.4628
|     |        | 0.0290∗∗∗ | 0.9585∗∗∗ |        | 0.4441∗∗ |         | 2.9070∗∗ | 7.8732∗∗∗ |                  |        |
| --- | ------ | --------- | --------- | ------ | -------- | ------- | -------- | --------- | ---------------- | ------ |
| TED | 0.0337 |           |           | 0.2638 |          | 10.6457 |          |           | -4293.75 8650.43 | 0.4117 |
GREA 0.0337 0.0289∗∗∗ 0.9631∗∗∗ 0.5704∗∗∗ 0.0311 1.1348 163.7488 7.8064∗∗∗ -4295.95 8654.83 0.0034
Table 22: GARCH-MIDAS estimation results for GSCI log returns 01 Jan 1996-30 Dec 2005 with K = 16 and
Theasterisks∗∗∗,∗∗,and∗indicatesignificanceat1%,5%,and10%,respectively.
Beta-weightingscheme.
|     | µ   | α   | β   | m   | θ   | ω1  | ω2  | ν   | LogL BIC | VR  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
GARCH 0.0138 0.0355∗∗∗ 0.9621∗∗∗ 0.7735∗∗∗ 7.9946∗∗∗ -8633.33 17309.47 –
|     |     | 0.0321∗∗ | 0.9612∗∗∗ |     | 0.0036∗∗∗ |     |     | 8.3741∗∗∗ |     |     |
| --- | --- | -------- | --------- | --- | --------- | --- | --- | --------- | --- | --- |
GARCH-RV 0.0138 0.1774 1.0093 83.6688 -8616.70 17301.88 0.4904
quarterlygrowthrates
PPI 0.0140 0.0337∗∗∗ 0.9634∗∗∗ 0.1585 0.9523∗∗∗ 2.7977∗ 7.9148 7.9797∗∗∗ -8631.41 17331.30 0.1195
IP 0.0138 0.0355∗∗∗ 0.9619∗∗∗ 0.8864∗ -0.1665 1.0002 1.3451 7.9548∗∗∗ -8633.16 17334.81 0.0329
|       |        | 0.0366∗∗∗ | 0.9581∗∗∗ | 0.8109∗∗∗ | -0.2637∗∗∗ | 1.9431∗∗∗ | 2.4398∗∗ | 7.8219∗∗∗ |                   |        |
| ----- | ------ | --------- | --------- | --------- | ---------- | --------- | -------- | --------- | ----------------- | ------ |
| SENTI | 0.0145 |           |           |           |            |           |          |           | -8630.43 17329.34 | 0.3646 |
EPUI 0.0140 0.0339∗∗∗ 0.9635∗∗∗ 0.6465∗∗ 0.0433 1.3927∗∗ 2.4952∗∗ 7.9557∗∗∗ -8631.76 17332.00 0.0846
| EERUS |        | 0.0343∗∗∗ | 0.9625∗∗∗ |        |         |        |        | 8.0688∗∗∗ |                   |        |
| ----- | ------ | --------- | --------- | ------ | ------- | ------ | ------ | --------- | ----------------- | ------ |
|       | 0.0133 |           |           | 0.6732 | -0.1964 | 3.6775 | 6.7039 |           | -8631.81 17332.11 | 0.1524 |
MOVE 0.0139 0.0350∗∗∗ 0.9617∗∗∗ 0.6130∗∗ 0.0801∗ 1.6295∗∗∗ 2.3221∗∗ 7.9797∗∗∗ -8631.09 17330.67 0.2385
VIX 0.0140 0.0355∗∗∗ 0.9612∗∗∗ 0.9785∗∗∗ -0.0643 2.7828 2.3999∗∗ 7.8885∗∗∗ -8631.26 17330.99 0.2274
|      |        | 0.0373∗∗∗ | 0.9589∗∗∗ | 0.7852∗∗∗ | -0.0260∗∗ | 3.9756∗ | 4.3302∗∗∗ | 7.9396∗∗∗ |                   |        |
| ---- | ------ | --------- | --------- | --------- | --------- | ------- | --------- | --------- | ----------------- | ------ |
| TB3M | 0.0147 |           |           |           |           |         |           |           | -8630.82 17330.12 | 0.2172 |
TED 0.0139 0.0349∗∗∗ 0.9621∗∗∗ 0.6522∗∗ 0.0160 2.7806∗∗∗ 10.7078 8.0273∗∗∗ -8629.56 17327.61 0.1362
GREA 0.0156 0.0338∗∗∗ 0.9616∗∗∗ 0.5567∗∗∗ 0.0133∗∗∗ 139.2172∗∗∗ 379.6359∗∗∗ 8.1156∗∗∗ -8626.68 17321.84 0.3587
quarterlyvariances
|     |        | 0.0328∗∗∗ | 0.9650∗∗∗ | 0.7209∗∗∗ |        |        |         | 7.9586∗∗∗ |                   |        |
| --- | ------ | --------- | --------- | --------- | ------ | ------ | ------- | --------- | ----------------- | ------ |
| PPI | 0.0137 |           |           |           | 0.0629 | 5.1439 | 57.4938 |           | -8631.28 17331.04 | 0.0409 |
IP 0.0141 0.0357∗∗∗ 0.9616∗∗∗ 0.5661∗ 0.3206 1.0000 1.6954 7.9292∗∗∗ -8631.93 17332.33 0.1472
SENTI 0.0142 0.0307∗∗∗ 0.9672∗∗∗ 0.5416 0.1484∗∗∗ 355.1335 98.6121 8.1465∗∗∗ -8628.22 17324.93 0.0861
|      |        | 0.0350∗∗ | 0.9625∗∗∗ |        |        |        | 1.0097∗∗∗ | 8.0058∗∗∗ |                   |        |
| ---- | ------ | -------- | --------- | ------ | ------ | ------ | --------- | --------- | ----------------- | ------ |
| EPUI | 0.0136 |          |           | 0.4693 | 0.2860 | 1.9733 |           |           | -8632.48 17333.45 | 0.0634 |
EERUS 0.0145 0.0357∗∗∗ 0.9612∗∗∗ 0.5736∗∗∗ 0.1239∗∗ 117.4395 421.5937 8.0356∗∗∗ -8630.49 17329.45 0.0517
|      |        | 0.0361∗∗∗ | 0.9603∗∗∗ | 0.9706∗∗∗ |         |        |         | 7.9138∗∗∗ |                   |        |
| ---- | ------ | --------- | --------- | --------- | ------- | ------ | ------- | --------- | ----------------- | ------ |
| MOVE | 0.0146 |           |           |           | -0.2153 | 5.4298 | 16.9621 |           | -8630.69 17329.86 | 0.1218 |
VIX 0.0155 0.0367∗∗∗ 0.9545∗∗∗ 1.1878∗∗∗ -0.5452∗∗ 4.1654 2.4004∗ 8.0417∗∗∗ -8624.41 17317.29 0.4437
TB3M 0.0157 0.0343∗∗∗ 0.9602∗∗∗ 0.9128∗∗∗ -1.3805∗∗∗ 15.0349∗∗ 14.8720∗ 8.0454∗∗∗ -8626.68 17321.85 0.3833
|     |        | 0.0345∗∗∗ | 0.9630∗∗∗ | 0.7758∗∗∗ |         | 156.1020∗ | 26.7437∗ | 8.0657∗∗∗ |                   |        |
| --- | ------ | --------- | --------- | --------- | ------- | --------- | -------- | --------- | ----------------- | ------ |
| TED | 0.0145 |           |           |           | -0.0229 |           |          |           | -8631.77 17332.02 | 0.0142 |
GREA 0.0138 0.0355∗∗∗ 0.9621∗∗∗ 0.7736∗∗∗ -0.0004 81.9808 3.7147 7.9945∗∗∗ -8633.33 17335.15 0.0000
Table 23: GARCH-MIDAS estimation results for GSCI log returns 01 Jan 1996-31 Dec 2015 with K = 16 and
Theasterisks∗∗∗,∗∗,and∗indicatesignificanceat1%,5%,and10%,respectively.
Beta-weightingscheme.
38
Electronic copy available at: https://ssrn.com/abstract=3294967

|     | µ   | α   | β   | m   | θ   | ω1  | ω2  | ν   | LogL BIC | VR  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
GARCH -0.0013 0.0410∗∗∗ 0.9577∗∗∗ 0.9868∗∗∗ 8.2257∗∗∗ -4332.77 8704.88 –
|     |     | 0.0366∗∗ | 0.9611∗∗∗ |     | 0.0027∗∗∗ |     |     | 8.4427∗∗∗ |     |     |
| --- | --- | -------- | --------- | --- | --------- | --- | --- | --------- | --- | --- |
GARCH-RV -0.0030 0.5325 1.0094 83.5544 -4325.33 8713.59 0.2929
quarterlygrowthrates
PPI -0.0012 0.0393∗∗∗ 0.9594∗∗∗ 0.9292∗∗∗ 0.0861 86.9516∗∗ 335.2204∗ 8.2212∗∗∗ -4331.70 8726.34 0.0103
IP -0.0013∗ 0.0421∗∗∗ 0.9561∗∗∗ 1.2429∗∗∗ -0.5693 1.0000 1.2227 8.0693∗∗∗ -4331.83 8726.60 0.1853
|       |         | 0.0427∗∗∗ | 0.9523∗∗∗ | 0.9142∗∗ | -0.3322∗∗∗ | 1.9839∗∗∗ | 2.6837∗∗ | 7.9402∗∗∗ |                  |        |
| ----- | ------- | --------- | --------- | -------- | ---------- | --------- | -------- | --------- | ---------------- | ------ |
| SENTI | -0.0010 |           |           |          |            |           |          |           | -4331.53 8726.00 | 0.5223 |
EPUI -0.0012 0.0399∗∗∗ 0.9588∗∗∗ 1.0297∗∗ 0.0684 1.8943 3.9855 8.0367∗∗∗ -4331.05 8725.03 0.2017
EERUS 0.0386∗∗∗ 0.9597∗∗∗ 0.8613∗∗ 3.0571∗∗ 6.6568∗∗ 8.2653∗∗∗
|     | -0.0014 |     |     |     | -0.2350 |     |     |     | -4331.82 8726.57 | 0.0911 |
| --- | ------- | --- | --- | --- | ------- | --- | --- | --- | ---------------- | ------ |
MOVE -0.0020 0.0388∗∗∗ 0.9601∗∗∗ 1.1720∗∗∗ 0.0586 1.1462∗∗∗ 1.9691∗∗∗ 8.0081∗∗∗ -4330.91 8724.75 0.1293
VIX -0.0011 0.0399∗∗∗ 0.9570∗∗∗ 0.7976∗∗∗ -0.0417 5.2271 3.5473∗∗ 8.2804∗∗∗ -4332.06 8727.04 0.1370
|      |         | 0.0428∗∗∗ | 0.9556∗∗∗ | 1.2595∗∗ |         |        | 4.1815∗∗∗ | 8.0109∗∗∗ |                  |        |
| ---- | ------- | --------- | --------- | -------- | ------- | ------ | --------- | --------- | ---------------- | ------ |
| TB3M | -0.0003 |           |           |          | -0.0267 | 3.6507 |           |           | -4331.62 8726.17 | 0.2036 |
TED -0.0010 0.0390∗∗∗ 0.9599∗∗∗ 1.2940∗∗∗ -0.0295 4.3113∗∗∗ 3.6607∗∗ 8.2753∗∗∗ -4331.58 8726.10 0.1438
GREA -0.0011 0.0388∗∗∗ 0.9513∗∗∗ 0.0211∗∗ 0.0300∗∗∗ 4.1313 8.3313 8.2099∗∗∗ -4326.54 8716.02 0.7998
quarterlyvariances
|     |         | 0.0417∗∗∗ | 0.9564∗∗∗ |        | 0.5034∗∗ |        |        | 7.9760∗∗∗ |                  |        |
| --- | ------- | --------- | --------- | ------ | -------- | ------ | ------ | --------- | ---------------- | ------ |
| PPI | -0.0014 |           |           | 0.4472 |          | 1.0000 | 1.3721 |           | -4330.54 8724.01 | 0.2963 |
IP -0.0011 0.0416 0.9566∗∗∗ 0.6878 0.3966 1.0000 1.4148 8.0926∗∗∗ -4331.60 8726.13 0.2007
SENTI -0.0002 0.0360∗∗∗ 0.9632∗∗∗ 0.5362 0.6649 6.3414 2.2041∗∗ 8.1227∗∗∗ -4328.28 8719.49 0.2877
|      |         | 0.0381∗∗∗ | 0.9613∗∗∗ |        | 0.8519∗∗ | 1.0423∗∗∗ | 1.0280∗∗∗ | 8.1019∗∗∗ |                  |        |
| ---- | ------- | --------- | --------- | ------ | -------- | --------- | --------- | --------- | ---------------- | ------ |
| EPUI | -0.0006 |           |           | 0.4079 |          |           |           |           | -4330.06 8723.05 | 0.2776 |
EERUS -0.0015 0.0412∗∗∗ 0.9571∗∗∗ 0.8314 0.1266 1.0000 8.5213 8.1972∗∗∗ -4331.88 8726.70 0.0324
|      |         | 0.0407∗∗∗ | 0.9580∗∗∗ | 0.9732∗∗∗ |        |          |         | 8.2752∗∗∗ |                  |        |
| ---- | ------- | --------- | --------- | --------- | ------ | -------- | ------- | --------- | ---------------- | ------ |
| MOVE | -0.0004 |           |           |           | 0.0363 | 299.1063 | 14.4674 |           | -4332.16 8727.26 | 0.0073 |
VIX 0.0005 0.0401∗∗∗ 0.9437∗∗∗ 1.3351∗∗∗ -0.5838∗∗∗ 8.4087∗ 4.9784∗∗ 8.2239∗∗∗ -4323.59 8710.11 0.6389
TB3M 0.0009 0.0382∗∗∗ 0.9534∗∗∗ 1.3114∗∗∗ -1.9862∗∗∗ 12.2317∗∗ 11.1743∗ 8.1446∗∗∗ -4326.98 8716.90 0.5752
|     | -0.0004∗∗ | 0.0383∗∗∗ | 0.9604∗∗∗ | 0.9876∗∗∗ | -0.0235∗ | 264.0076∗∗ | 45.8487∗ | 8.3710∗∗∗ |                  |        |
| --- | --------- | --------- | --------- | --------- | -------- | ---------- | -------- | --------- | ---------------- | ------ |
| TED |           |           |           |           |          |            |          |           | -4331.07 8725.08 | 0.0181 |
GREA -0.0011 0.0399∗∗∗ 0.9588∗∗∗ 0.9779∗∗ 0.0176 420.2258 44.6902 8.2203∗∗∗ -4332.32 8727.58 0.0086
Table 24: GARCH-MIDAS estimation results for GSCI log returns 02 Jan 2006-31 Dec 2015 with K = 16 and
Theasterisks∗∗∗,∗∗,and∗indicatesignificanceat1%,5%,and10%,respectively.
Beta-weightingscheme.
39
Electronic copy available at: https://ssrn.com/abstract=3294967

∗∗∗5924.0- ∗∗∗0184.0- ∗∗∗6435.0- ∗∗∗1474.0- ∗∗8524.0- ∗∗1693.0- ∗∗∗4425.0- ∗∗∗4334.0-
enilpS 0020.0- 2655.0 9192.0 5262.0 ∗5622.0- 6963.0 6780.0 5091.0 0340.0 0081.0- 5004.0 6950.0 7103.0 2891.0- 0831.0- 5563.0 2552.0 1073.0 0985.0 5124.0 1696.0 1067.0 3317.0 3678.0 ∗5512.0- 1315.0 6532.0 0382.0
|     |     | ∗∗7983.0- | ∗∗2744.0- ∗∗4564.0- |     |
| --- | --- | --------- | ------------------- | --- |
8112.0 0481.0 9193.0 5567.0 0665.0 4685.0 7432.0 9211.0 1483.0 6676.0 5854.0 2005.0 1830.0 2770.0- 9713.0 9350.0 0503.0 ∗8642.0- 5651.0 5190.0 6173.0 4564.0 2492.0 6726.0 3227.0 3136.0 9378.0 6041.0 8820.0- 6681.0 0207.0 1245.0 6795.0
VR
.ecnedfinoc%579.0)4102(ylekezS&ibrecAfo
|     |     | ∗∗∗8307.0- ∗∗∗1695.0- | ∗∗9792.0- ∗∗∗7455.0- ∗∗8474.0- |     |
| --- | --- | --------------------- | ------------------------------ | --- |
HCRAG 2780.0 0461.0- 8740.0- 4496.0 8944.0 0484.0 1591.0 3460.0- 6041.0 9166.0 7173.0 1153.0 9622.0- 8501.0 3560.0- 0261.0- 5182.0 8761.0 9452.0 0573.0 6531.0 3004.0 8456.0 6705.0 6086.0 9640.0 ∗0112.0- 1660.0- 5036.0 8804.0 2145.0
|                   |          | ∗∗∗5976.0- ∗∗∗4006.0- | ∗∗∗4755.0-        |     |
| ----------------- | -------- | --------------------- | ----------------- | --- |
| ∗9532.0- ∗7391.0- | ∗8691.0- |                       | ∗9492.0- ∗4472.0- |     |
AERG 1410.0- 0856.0 9743.0 8844.0 4560.0 1120.0 5295.0 9133.0 5043.0 4822.0- 2231.0 9660.0- 8361.0- 5402.0 9471.0 9843.0 8323.0 3211.0 1623.0 2556.0 8964.0 5776.0 1250.0 4271.0- 2420.0 8135.0 5704.0 8645.0
|     |     | ∗∗∗1386.0- ∗∗∗5895.0- | ∗∗∗0946.0- ∗∗6844.0- |     |
| --- | --- | --------------------- | -------------------- | --- |
5031.0 5610.0- 3650.0 2696.0 0094.0 4174.0 2042.0 7710.0 3831.0 3766.0 8874.0 6283.0 9081.0- 0331.0 6070.0- 4811.0- ∗4832.0- 8463.0 7511.0 2452.0 3943.0 0061.0 4273.0 0286.0 7335.0 1776.0 8240.0 6181.0- 1590.0- 9075.0 3904.0 8545.0
DET
|     |     | ∗∗∗1158.0- ∗∗∗7776.0- | ∗∗∗1955.0- ∗∗∗0084.0- |     |
| --- | --- | --------------------- | --------------------- | --- |
2951.0- ∗2232.0- 6431.0- ∗8162.0- 6831.0- 4681.0- ∗5692.0- 1961.0- 9511.0-
M3BT 6340.0 5327.0 5374.0 0574.0 2571.0 4830.0 3075.0 9133.0 8263.0 4490.0 8082.0 7661.0 2452.0 6943.0 4701.0 5883.0 2856.0 8535.0 4256.0 8821.0 5436.0 3374.0 3784.0
|     |     | ∗∗∗4056.0- ∗∗4644.0- | ∗3992.0- ∗∗∗8216.0- ∗∗∗4684.0- |     |
| --- | --- | -------------------- | ------------------------------ | --- |
2651.0 0390.0- 3090.0- 9756.0 6374.0 0654.0 3471.0 6160.0- 2811.0 0296.0 4273.0 2093.0 5931.0- 2951.0 3090.0- 7511.0- 3772.0 3461.0 7152.0 3683.0 7232.0 9555.0 9545.0 8515.0 7508.0 1290.0 2661.0- 9320.0 9406.0 4184.0 2885.0
XIV 2
Ztsetkcab”tcerid“llaftrohSdetcepxEehtrofstluseR
munitalP
| ITW | tnerB | dloG                  | revliS                          | ICSG |
| --- | ----- | --------------------- | ------------------------------- | ---- |
|     |       | ∗∗∗0156.0- ∗∗∗1565.0- | ∗∗2223.0- ∗∗∗6965.0- ∗∗∗9384.0- |      |
EVOM 7201.0 4141.0- 5710.0- 6556.0 2183.0 3854.0 5920.0 5501.0- 6730.0 1895.0 2473.0 0163.0 4891.0- 0231.0 1040.0- 0761.0- 0822.0 0211.0 2942.0 1843.0 1831.0 7104.0 5186.0 7205.0 9876.0 1760.0 ∗0322.0- 5131.0- 7865.0 8114.0 6584.0
|     |     | ∗∗∗2637.0- ∗∗∗2495.0- | ∗∗∗4775.0- |     |
| --- | --- | --------------------- | ---------- | --- |
SUREE 4661.0- 4501.0- 7441.0- ∗6852.0- 7990.0- 9131.0- ∗∗0933.0- ∗∗4054.0- 0380.0- 0620.0-
1380.0 4296.0 6544.0 8354.0 7861.0 8141.0 2366.0 2304.0 5883.0 7990.0 9352.0 3631.0 8242.0 4583.0 2671.0 6493.0 8556.0 3985.0 3856.0 5211.0 5926.0 2474.0 3745.0
|     |     | ∗∗∗6786.0- ∗∗∗5335.0- | ∗∗3193.0- ∗∗∗1156.0- ∗∗∗7374.0- | ∗9691.0- |
| --- | --- | --------------------- | ------------------------------- | -------- |
IUPE 7200.0 2771.0- 1561.0- 0756.0 2344.0 1344.0 8960.0 8261.0- 6020.0- 9656.0 6963.0 1353.0 7312.0- 7931.0 0520.0- 9230.0- 7442.0 6470.0 2881.0 6494.0 6491.0 3355.0 1766.0 7145.0 4057.0 3530.0- 4021.0- 5695.0 7993.0 5044.0
| ∗∗8223.0- |     | ∗∗∗4747.0- ∗∗∗3755.0- | ∗∗∗5815.0- ∗∗3474.0- |     |
| --------- | --- | --------------------- | -------------------- | --- |
ITNES 8820.0- ∗8712.0- 0456.0 3533.0 2534.0 3490.0 0241.0- 5110.0- 1166.0 0393.0 6763.0 2061.0- 4551.0 3290.0- 6370.0- ∗8642.0- 6152.0 0041.0 5282.0 5573.0 8801.0 9653.0 3626.0 6214.0 6156.0 5440.0 ∗7412.0- 4401.0- 5955.0 6034.0 4535.0
|     |     | ∗∗∗5685.0- ∗∗∗2035.0- | ∗∗∗9285.0- |     |
| --- | --- | --------------------- | ---------- | --- |
∗∗9443.0- ∗∗2553.0-
2521.0 9210.0 9280.0 2296.0 4454.0 7094.0 0661.0 0850.0- 4071.0 5206.0 2273.0 5353.0 5181.0- 1402.0 6440.0- 8620.0- 3223.0 2231.0 6303.0 9593.0 3412.0 2624.0 1196.0 0575.0 6057.0 9311.0 8201.0- 2110.0 8036.0 6744.0 0355.0
PI
:52elbaT
|     |     | ∗∗∗6326.0- ∗∗5524.0- | ∗∗6913.0- ∗∗∗0985.0- ∗∗∗8015.0- |     |
| --- | --- | -------------------- | ------------------------------- | --- |
9580.0 2101.0- 9050.0- 5627.0 4354.0 5784.0 4560.0 7901.0- 8930.0 5826.0 1853.0 2423.0 4821.0- 9513.0 8710.0 5620.0 1252.0 8931.0 2582.0 5725.0 4243.0 3036.0 5087.0 9446.0 1178.0 8140.0 ∗4052.0- 5370.0- 1195.0 0234.0 8525.0
IPP
yad-02 yad-02 yad-02 yad-02 yad-02 yad-02 yad-02 yad-02 yad-02 yad-02 yad-02 yad-02
yad-1 yad-5 yad-1 yad-5 yad-1 yad-5 yad-1 yad-5 yad-1 yad-5 yad-1 yad-5 yad-1 yad-5 yad-1 yad-5 yad-1 yad-5 yad-1 yad-5 yad-1 yad-5 yad-1 yad-5
gnol trohs gnol trohs gnol trohs gnol trohs gnol trohs gnol trohs
40
Electronic copy available at: https://ssrn.com/abstract=3294967