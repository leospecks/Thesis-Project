| Journal  | of Futures Markets |     |     |     |     |     |
| -------- | ------------------ | --- | --- | --- | --- | --- |
| RESEARCH | ARTICLE            |     |     |     |     |     |
‐
| Predicting    | Commodity       |        | Returns            | Through | Image | Based |
| ------------- | --------------- | ------ | ------------------ | ------- | ----- | ----- |
| Price         | Patterns        |        |                    |         |       |       |
| TianxiangHao1 | | Qingfu Liu1,2 | | Deyu | Miao1 | YiumanTse3 |         |       |       |
1SchoolofEconomics,FudanUniversity,Shanghai,China | 2ShanghaiInstituteofMathematicsandInterdisciplinarySciences,Shanghai,China | 3EdG.
SmithCollegeofBusiness,UniversityofMissouri–St.Louis,St.Louis,Missouri,USA
Correspondence:DeyuMiao(dymiao22@m.fudan.edu.cn)
| Received:14February2025 | | Revised:20July2025 | |   | Accepted:1September2025 |     |     |     |
| ----------------------- | -------------------- | --- | ----------------------- | --- | --- | --- |
Keywords:CNN|commodityfutures|machinelearning|OHLCcharts|pricepattern
ABSTRACT
We examine the predictability of commodity futures returns using image‐based price patterns extracted from open‐high‐low‐
close (OHLC) charts. Applying convolutional neural networks (CNNs) to US commodity futures data, we extract predictive
image‐based
signals without predefined patterns such as momentum or mean reversion. Empirical results demonstrate that
predictions enhance predictive accuracy, particularly over short‐ and medium‐term horizons, with 20‐day OHLC images
yieldingthemostrobustperformance.Comparedwithtraditionalfinancialpredictors,CNNscapturenonlineardependencies
while retaining unique explanatory power. Panel regressions confirm that image‐based predictions are correlated with estab-
lished return factors. However, transfer learning—from the US to the Chinese markets—proves ineffective in commodity
market‐specificadaptation.
| futuresmarkets, | highlightingthe | necessityof |     |     |     |     |
| --------------- | --------------- | ----------- | --- | --- | --- | --- |
JELClassification:G13,G17,G45
1 | Introduction Although Jiang et al. (2023) demonstrate the effectiveness of
image‐basedpricepatternpredictioninequitymarkets,whether
|     |     |     | well‐known |     |     | external‐shock‐driven |
| --- | --- | --- | ---------- | --- | --- | --------------------- |
Traditional empirical studies have focused on the same approach can capture the and
phenomena such as momentum effects, mean reversion, and oftenregime‐shiftingdynamicsofcommodityfuturesremainsan
seasonal patterns, providing valuable insights into market openquestion.Commodityfuturesmarketsexhibituniquechar-
dynamics (Poterba and Summers 1988; Jegadeesh 1991; acteristics that differentiate them from traditional asset classes
Jegadeesh and Titman 1993). However, these methods often suchasequitiesandbonds.Thesemarketsaredrivenprimarilyby
rely on predefined patterns and linear assumptions, which supply‐demand dynamics, seasonality, storage costs, geopolitical
may overlook the complex, evolving nature of financial mar- factors,aswellasexternalshockssuchasweatherevents,natural
kets. Recent research has increasingly adopted data‐driven disasters,andtradepolicychanges,leadingtoreturnpatternsthat
methodologies to uncover latent patterns in financial data are distinct from those influenced by macroeconomic indicators
(Mullainathan and Spiess 2017; Gu et al. 2020; Leippold (Bianchi et al. 2015). Moreover, commodity futures markets are
etal.2022).Jiangetal.(2023)showthatopen‐high‐low‐close
characterizedbyhigherleverage,greatervolatility,andadiverse
(OHLC) charts in stock markets contain rich visual informa- participant base—including producers, consumers, hedgers, and
tion, which when analyzed with convolutional neural net- speculators—which amplifies the nonlinear nature of price
|     |     | short‐ | long‐term |     |     |     |
| --- | --- | ------ | --------- | --- | --- | --- |
works (CNNs), can effectively predict and behavior. Additionally, the low correlation between commodity
returns. This suggests that price patterns reflect complex futures returns and those of equities and bonds underscores
investorbehaviorandmicrostructuralfeaturesthattraditional their importance for asset allocation and risk management
| models fail | to capture. |     |     | (Heideetal.2025). |     |     |
| ----------- | ----------- | --- | --- | ----------------- | --- | --- |
©2025WileyPeriodicalsLLC.
JournalofFuturesMarkets,2025;45:2434–2456 2434
https://doi.org/10.1002/fut.70043

Existing research on commodity futures markets has largely Jiang et al. (2023) report that patterns learned from US stocks
concentratedonpredefinedpricepatternssuchasmomentum, areeffectiveininternationalmarketsthroughtransferlearning.
mean reversion, and seasonality (Miffre and Rallis 2007; However, our study finds that image‐based models trained on
Bianchi et al. 2015; Li et al. 2024). While these strategies have US commodity futures data fail to generalize effectively to
shown varying degrees of success, they frequently struggle to Chinese commodity futures.Structural differencesacrosscom-
adapt to evolving market conditions, presenting limitations in moditymarkets,shapedbylocalsupplyanddemandconditions,
the highly volatile and dynamic environment of commodity regulatory frameworks, andthecomposition ofmarket partici-
futuresmarketswhereexogenousshockscanrapidlyinvalidate pants, constrain the generalizability of predictive patterns.
fixedpattern assumptions(Wang andZhang 2024). These findings underscore the need for market‐specific adap-
tation and indicate that direct transfer without retraining is
Toaddressthesechallenges,weuseCNNstoanalyzeOHLCprice ineffectivefor commodity futuresreturnprediction.
chartsinthecommodityfuturesmarket.Originallydevelopedfor
image recognition tasks, CNNs are well suited to capturing This article contributes to the literature by extending image‐
complex spatial patterns and extracting latent features from based price prediction methods to the commodity futures
structured visual inputs. In recent years, the financial literature market. Our approach avoids reliance on predefined assump-
has increasingly explored the use of CNNs. However, prior tionsorlinearmodels,insteademployingaflexible,data‐driven
research has largely concentrated on applications involving the framework to autonomously identify and validate predictive
predictionofindividualassetpricesortaskssuchasimage‐based patterns.Thismakesitparticularlysuitedtothenonlinearand
clustering and classification (Obaid and Pukthuanthong 2022), dynamic nature of commodity futures markets. Our study
with a focus on equities (Cohen et al. 2020), oil futures (Göncü reinforcesandextendsthefindingsofJiangetal.(2023)forUS
etal.2024;Renetal.2024),andstockindexes(Chenetal.2016; stocks. It offers practical implications by providing tools for
HoseinzadeandHaratizadeh2019).Notably,therehasbeenlittle developingtrading strategiesandoptimizing assetallocation.
attention devoted to large‐scale return forecasting at various
commodity futures with a comprehensive portfolio analysis and The remainder of thisarticle is organized as follows.Section 2
transfer learning between the US and Chinese commodity mar- reviews the literature on commodity futures trading strategies.
ketsexaminedinourstudy. Section 3 introduces the data, explains OHLC chart construc-
tion,andoutlinespreprocessingstepsforCNNimplementation.
By explicitly modeling the spatial signatures left by weather Section 4 presents empirical results, evaluating CNN model
events, geopolitical headlines, and inventory shocks on price performance in return prediction and comparing it to other
charts, our study demonstrates that CNNs offer a powerful trading strategies. Section 5 explores CNN interpretability by
alternativetodifferenttrend‐basedandmachinelearning(ML) analyzing learned patterns from OHLC charts and discussing
strategies. We address this gap by providing novel empirical transferlearning across markets.Section6 concludes.
evidence on the application of CNNs in asset pricing and by
exploring the learning process of CNNs and their effectiveness
in developing systematic trading strategies in the commodity 2 | Literature Review on Trading Strategies in
futuresmarket. Commodity Futures
OurML–basedframeworkautonomouslyidentifiesandextracts Early empirical work interprets expected commodity futures
latent patterns with predictive power from a vast data set of returns through the lens of risk premium theory. In practice,
price charts, offering a flexible tool for forecasting commodity variables such as the basis, the slope of the term structure, and
futures returns. Whereas traditional analysis of these patterns empirical proxies for convenience yield reliably forecast excess
often involves subjective judgment, ML algorithms like CNNs returns(FamaandFrench1988;ErbandHarvey2006).Thepar-
offerasystematic,objectivemeansofidentifyingandvalidating allelliteraturesortscontractsonlaggedpricedynamics.Portfolios
these patterns, thereby enabling the timely incorporation of formed on monthly momentum, calendar seasonality, and long‐
external shocks into forecasting models and enhancing the horizon reversal deliver sizable risk‐adjusted profits, although
robustness of trading signals, making them particularly well performancevariesacrossbusinesscyclephasesandissensitiveto
suited forfinancialapplications. roll costs (Sørensen 2002; Gorton and Rouwenhorst 2006; Miffre
andRallis2007).Factorextensionssuchasthecommoditycapital
ThefindingsofthisstudyhighlighttheeffectivenessofCNNsin assetpricingmodel(Adrianetal.2013)andthebasis‐momentum
capturing nonlinear, complex patterns embedded in OHLC two‐factor model (Szymanowska et al. 2014; Boons and
charts, significantly improving return prediction accuracy over Prado 2019) improve cross‐sectional explanatory power, yet they
short‐andmedium‐termhorizons.Predictionsbasedon20‐day remain linear and largely time invariant. More recent research
OHLC charts achieve the best balance between signal stability embeds seasonality and inventory cycles, documenting state‐
and predictive performance, consistently outperforming tradi- dependent interactions between carry and momentum (Gorton
tional strategies such as momentum and mean reversion in etal.2013;Chengetal.2023).
terms of Sharpe ratios (SRs) and risk‐adjusted returns. Fur-
thermore, our analysis demonstrates that image‐based models While these approaches are firmly grounded in economic the-
extract predictive signals that are strongly correlated with ory, their parametric structure limits their ability to capture
financialfactors such as momentum, short‐term reversals, and higher‐order interactions, multicollinearity, and structural
proximity to 52‐week highs while autonomously capturing breaks, motivating a shift toward data‐driven methods. The
nonlinearinteractions andtemporaldependencies. recentliteraturehasadoptedMLtechniquestorelaxfunctional‐
2435
10969934,
2025,
12,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/fut.70043
by
Universita
Bocconi
Milano,
Wiley
Online
Library
on
[14/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 10969934, 2025, 12, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/fut.70043 by Universita Bocconi Milano, Wiley Online Library on [14/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
FIGURE1 | PlatinumApr'08(PLJ08).ThisfigurepresentsanOHLCchartsourcedfromBarchart(https://www.barchart.com/futures/quotes/
PLJ08/interactive-chart),depictingPlatinumApr'08(PLJ08)data.Thechartfeaturesa20‐daymovingaveragepricelineanddailytradingvolume
bars,spanningtheperiodfromJanuary29,2008,toApril30,2008.
|                  |                      |                |        |                   |            | 3 | Data   | and Methodology |     |     |
| ---------------- | -------------------- | -------------- | ------ | ----------------- | ---------- | ---------- | --------------- | --- | --- |
| form constraints |                      | and exploit    | richer | information       | sets (Gu   |            |                 |     |     |
| et al. 2020).    | Classical            | ML algorithms, |        | including support | vector     |            |                 |     |     |
| machines         | and gradient‐boosted |                | trees, | capture nonlinear | inter-     | 3.1 | OHLC |                 |     |     |
| actions among    | carry,               | momentum,      |        | volatility,       | and macro- |            |                 |     |     |
economicvariables,leadingtosignificantgainsinout‐of‐sample
|     |     |     |     |     |     | Many popular | websites, such | as Bloomberg, | Yahoo Finance, |
| --- | --- | --- | --- | --- | --- | ------------ | -------------- | ------------- | -------------- |
predictive accuracy (Gong et al. 2022; Wang and Zhang 2024). andGoogle Finance, provide historical price chartsfor various
Han and Kong (2022) apply adaptive Lasso to uncover serial financialassets.Figure1illustratesanexampleofPlatinumApr
dependence in futures returns and document significant '08(PLJ08)datadisplayedonBarchartinastandardpricechart
predictability. format.ThechartincludesOHLCbargraphsdepictingthedaily
|     |     |     |     |     |     | open, high, | low, and close | prices, along | with a 20‐day moving |
| --- | --- | --- | --- | --- | --- | ----------- | -------------- | ------------- | -------------------- |
Deep networks push the frontier further. Rad et al. (2023) average of closing prices. Daily trading volume is displayed at
employneural networkstostudy thelinks between128 macro thebottomof thechart.
| financial predictors |     | and subsequent |     | futures returns, | showing |     |     |     |     |
| -------------------- | --- | -------------- | --- | ---------------- | ------- | --- | --- | --- | --- |
economic‐state
that variables contain information about com- Although such charts arereadily available online,we generate
modity risk premia. Herrera et al. (2019) compare neural net- our own price charts from scratch to enable controlled experi-
worksandrandomforestswithtraditionaleconometricmodels mentationbyadjustingtheamountofinformationvisibletothe
over longer horizons and find persistent outperformance in CNNmodel.OurchartsadheretothebasicformatofFigure1,
energy contracts. Ren et al. (2024) and Göncü et al. (2024) using black OHLC bar graphs where the high and low prices
predictedtheoil futurespricewith aCNN model. correspond to the top and bottom of the central vertical bar,
whiletheopenandclosepricesaremarkedbysmallhorizontal
Despitetheseadvances,previousstudiesstillfocusonalimited linesontheleftandrightsides,respectively.Eachdayoccupies
three‐pixel‐wide
setofcontractsorextendlinearfactormodelsonlymarginally. a space: one pixel for the central bar, one for
Consequently,boththereturn‐predictivepowerofimage‐based theopen marker, andonefor theclose marker.
cross‐
| representations | and | their | robustness | across a | broad |     |     |     |     |
| --------------- | --- | ----- | ---------- | -------- | ----- | --- | --- | --- | --- |
section of commodities remain largely unexplored. Addressing Following Jiang et al. (2023), our commodity futures images
this gap, we develop an image‐based framework that learns consist of OHLC bar graphs spanning 5, 20, or 60
directly from OHLC price images for a large panel of liquid continuous days, corresponding approximately to weekly,
monthly,andquarterlypricetrajectories.Thus,ann‐dayimage
| futures. Benchmarking |     | against | canonical | factor | strategies and |     |     |     |     |
| --------------------- | --- | ------- | --------- | ------ | -------------- | --- | --- | --- | --- |
state‐of‐the‐art ML algorithms reveals that the CNN captures hasawidthof3npixels.Insteadofrawprices,weuseadjusted
additional information and materially enhances risk‐adjusted returns, converting the open, close, high, and low prices into
performance.1
|      |     |     |     |     |     | relative values. | After assigning | dates, we                    | fix the image height |
| ---- | --- | --- | --- | --- | --- | ---------------- | --------------- | ---------------------------- | -------------------- |
| 2436 |     |     |     |     |     |                  |                 | JournalofFuturesMarkets,2025 |                      |

FIGURE2 | Sixty‐day OHLC image with volume bar and moving average. This figure depicts a 60‐day commodity futures contracts image,
includingvolumebarsandthe60‐daymovingaverageline.
andscaletheverticalaxissothatthemaximumandminimum (CBT), the Intercontinental Exchange (ICE), New York Mer-
oftheOHLCpathalignwiththetopandbottomoftheimage. cantile Exchange (NYMEX), Chicago Mercantile Exchange
As a result, all images for a given period share identical pixel (CME),andtheLondonMetalExchange(LME),wecompute5‐,
dimensions. 20‐, and 60‐day logarithmic returns for these 24 futures and
forwardcontracts.ThesampleperiodspansfromJanuary1980
Tooptimizestorageefficiency,weuseablackbackgroundwith to October 2024, incorporating the most recent data from our
white for all visible chart elements. Since black pixels are rep- provider, Commodity Systems Inc. For contracts introduced
resented by (0,0,0), this design minimizes data storage after 1980, we begin the analysis from their first trading day.
requirements by producing sparse images. In line with Table 1 presents the sample details and summary statistics for
Bloombergandsimilarplatforms,weomitcolordistinctionsfor 20‐day logcommodity returns.
“up”and“down”days,aspricedirectionisalreadyencodedin
the open and close markers. This allows us to focus on two‐ Commodity futures pose unique challenges due to rollovers as
dimensional (2D) pixel matrices without tracking red, green, contracts approach expiration and the existence of multiple
andblue pixelintensities. contracts with different expiration dates for the same product.
Manyexistingstudiesaddressthisissuebyexcludingcontracts
Additional information, such as trading volume and moving withfewerthan15tradingdaystoexpirationandimmediately
averages, is incorporated into the OHLC graphs. Each image rolling into the next contract (Miffre and Rallis 2007; Shen
includesamovingaverageline(e.g.,a20‐daymovingaveragefora etal.2007)orbygraduallyrollingintothenextcontract(Wang
20‐daywindow)andavolumebarchart.Thevolumechartoccu- andYu2004;Marshalletal.2008).However,akeylimitationof
pies the bottom one‐fifth of the image, while the OHLC plot fills theseapproachesisthatmultiplecontractsforthesameproduct
thetopfour‐fifths.Tomaintainconsistency,wescalethemaximum oftenexhibit significant differencesin liquidity.
volume within an image to match the upper limit of the volume
section,adjustingtheothervolumebarsproportionally. Topreventinformationleakageandmaintaindatavalidity,we
selectthefuturescontractwiththehighesttradingvolumeover
Figure 2 provides an example from our data set, featuring a thepast5tradingdaysasthenext‐daycontract,providedithas
60‐dayOHLCchartforcornfuturesstartingonAugust9,2007. more than 15 trading days until expiration (Han et al. 2016;
Thischartencapsulateskeydetailsaboutpricetrends,volatility, Yang et al. 2018). This approach assumes that the most liquid
intraday and overnight return patterns, and trading volume. contract is likely to remain the most active on the following
The design balances informational richness and storage effi- tradingday.Whenarolloveroccurs, weadjustthepriceseries
ciency,ensuringacomprehensivedatasetfortheCNNmodel. by rebasing the price using the true daily returns of the new
contract.
3.2 | Commodity Futures For visualization, we use the newly constructed continuous
priceseriesandaggregatedtradingvolumestogenerateOHLC
WeutilizethesamediverserangeofmarketsasKeloharjuetal. charts, rendering them in grayscale pixels. In cases of trading
(2016), covering 20 commodity futures and 4 metal forward haltsormarketsuspensions,wedonotleavegapsinthecharts.
contracts across agricultural products, energy, livestock, and Instead, to maintain visual continuity, we backfill the OHLC
metals. Using daily closing prices of near‐month futures con- chart using the most recent N valid trading days, ensuring
tractstradedonexchangessuchastheChicagoBoardofTrade reliable pricepattern representation.
2437
10969934,
2025,
12,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/fut.70043
by
Universita
Bocconi
Milano,
Wiley
Online
Library
on
[14/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 10969934, 2025, 12, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/fut.70043 by Universita Bocconi Milano, Wiley Online Library on [14/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
5914.0 7705.0 3362.0 1254.0 9684.0 3306.0 0353.0 5045.0 7866.0 7794.0 0106.0 2645.0 5064.0 1615.0 8871.0 9571.0 2573.0 5382.0 8057.0 2343.0 2772.0 5663.0 6024.0 8293.0 sbO.stcartnocdrawroflatem4dnaserutufytidommoc02sedulcnitesatadehT.slateMdna,kcotseviL,ygrenE,erutlucirgA:srotcesruofotnidezirogetac,stessagniylrednu42rofscitsitatsevitpircsedehtstneserpelbatsihT:etoN ,doirepyad‐02arevosnrutergolfoseulavmumixamdna,elitnecrepht57,elitnecrepht52,muminim,noitaiveddradnats,egarevaehttroperxaMdna,57p,52p,niM,DS,gvAsnmulocehT.syadgnidartforebmunehtstneserper
xaM
0230.0 1630.0 7330.0 3330.0 6540.0 0640.0 4830.0 0350.0 2060.0 8450.0 6560.0 0760.0 3260.0 6550.0 3620.0 8520.0 1440.0 0630.0 7150.0 9140.0 9340.0 5520.0 7240.0 3340.0
57p
0040.0− 6050.0− 8530.0− 2340.0− 8250.0− 7160.0− 5140.0− 1260.0− 1940.0− 2840.0− 9740.0− 4990.0− 1640.0− 2540.0− 8220.0− 1120.0− 3540.0− 7330.0− 2050.0− 7630.0− 9630.0− 7620.0− 0740.0− 5830.0−
52p
6173.0− 1253.0− 0023.0− 2133.0− 4834.0− 1184.0− 6243.0− 0783.0− 4459.0− 7565.0− 3202.1− 5006.0− 0318.0− 5546.0− 5582.0− 9682.0− 3384.0− 2682.0− 8795.0− 7864.0− 8654.0− 7323.0− 8381.1− 3445.0−
niM
2660.0 8170.0 5060.0 1960.0 4970.0 2490.0 6760.0 1790.0 6990.0 6780.0 1301.0 5131.0 4390.0 4980.0 8040.0 7930.0 7170.0 3650.0 1980.0 6960.0 4860.0 8740.0 1980.0 6070.0
DS
1400.0− 3600.0− 2000.0− 3300.0− 9200.0− 5400.0− 1100.0− 8300.0− 2710.0− 2200.0− 0100.0− 4400.0−
|     |     |     |     | 6100.0 9100.0 8500.0 | 0500.0 | 9300.0 3000.0 2100.0 | 0100.0 | 4100.0 8100.0 7100.0 | 9100.0 |
| --- | --- | --- | --- | -------------------- | ------ | -------------------- | ------ | -------------------- | ------ |
gvA
.4202rebotcOhguorhtdnetxedna,tessahcaerofyadgnidartelbaliavatsrifehtro,0891,1yraunaJnonigebserutufllA.ylevitcepser
572,11 572,11 572,11 672,11 322,11 222,11 332,11 322,11 414,01 432,11 280,11 282,11 282,11 282,11 303,11 113,11 742,11 742,11 742,11
| sbO |     |     |     | 1999 | 4568 3629 |     | 4349 | 4219 |     |
| --- | --- | --- | --- | ---- | --------- | --- | ---- | ---- | --- |
etadtratS 10/10/0891 10/10/0891 10/10/0891 10/10/0891 10/10/0891 10/10/0891 10/10/0891 10/10/0891 80/40/3891 10/10/0891 11/21/4891 11/40/0991 10/10/0891 41/40/1891 10/10/0891 10/70/8891 10/10/0891 21/60/7891 10/10/0891 10/10/0891 20/90/8891 10/10/0891 10/10/0891 10/10/0891
.tekramserutufytidommocSUnisnruteryad‐02foscitsitatsyrammuS
egnahcxE
|     |             | SU‐ECI | SU‐ECI SU‐ECI SU‐ECI | XEMYN XEMYN XEMYN | XEMYN UE‐ECI | UE‐ECI  |         | XEMOC       | XEMOC XEMOC |
| --- | ----------- | ------ | -------------------- | ----------------- | ------------ | ------- | ------- | ----------- | ----------- |
|     | TBC TBC TBC | TBC    |                      |                   |              | EMC EMC | EMC EML | EML EML EML |             |
kcotsdnelB
taehW
saGlarutaN
liosaGruhpluS‐woL
DSLU
| ytidommoC |          |         |              |                           | edurC | elttaCredeeF |                   |                |        |
| --------- | -------- | ------- | ------------ | ------------------------- | ----- | ------------ | ----------------- | -------------- | ------ |
|           | snaebyoS | WRHytiC |              | liO detalumrofeR‐enilosaG |       | elttaCeviL   | sgoHnaeL munimulA |                |        |
|           | taehW    |         | nottoC       |                           |       |              |                   | lekciN         | reppoC |
|           | nroC     | aocoC   | eeffoC raguS | robraHYN                  |       |              |                   | daeL cniZ dloG | revliS |
edurC
|     |     |     |     |     | buHyrneH tnerB |     |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
sasnaK
erutlucirgA
|
kcotseviL
| 1ELBAT |     |     |     | ygrenE |     |     |        |     |     |
| ------ | --- | --- | --- | ------ | --- | --- | ------ | --- | --- |
| rotceS |     |     |     |        |     |     | slateM |     |     |
2438 JournalofFuturesMarkets,2025

 10969934, 2025, 12, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/fut.70043 by Universita Bocconi Milano, Wiley Online Library on [14/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
modelingofhistoricaltime‐seriesdataorone‐dimensional(1D)
Ourpricetrendanalysisconstructscontinuousreturnseriesby
adjustingforcontractrollovers.Foreachimage,westandardize models. In contrast, our approach leverages 2D CNNs, as rep-
the first day's closing price to one and calculate window‐level resenting the data as images enables convolutional filters to
|     | RET | q=5, |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
returns, t+q , 20, 60, using subsequent daily closing capture nonlinear spatial correlations between various price
prices.Thisensuresthatreturnsarecomparableacrossdifferent patterns. Images integrate information about directional price
contracts andconsistent acrossanalysiswindows. Incommod- movements, deviations from moving average trends, price vol-
ityfutures,rollingfromonecontracttoanothermayintroduce atility,andtrading volumeintoaunifiedrepresentation.
artificialpricediscontinuities.Werebasethepriceseriesateach
rollover pointusing actualreturns to preservecontinuity. For instance, considering price direction and volatility simulta-
neouslyintraditionaltime‐seriesmodelswouldrequirerestrictive
|     |     |     | RET =ln(p |     | )−ln(p | )   | (1) |     |     |     |     |
| --- | --- | --- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- |
t+q t+q t assumptions andmanual featureengineering. Incorporating vola-
|     |     |     |     |     |     |     |     | tility information | typically necessitates | nonlinear | transformations |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | ---------------------- | --------- | --------------- |
We analyze market data images spanning the past 5, 20, or of the price series using stochastic volatility or generalized auto-
60days,assigningbinarylabelsof1or0basedonwhetherthe regressive conditional heteroskedasticity models. However, 2D
returns over the subsequent 5, 20, or 60 days are positive or CNN eliminates the need for manual feature design by autono-
nonpositive. As a result, our primary analysis consists of nine mouslyextractingpredictivepatternsfromthemarketdataseries.
separately estimated models. Following Gu et al. (2020) and Additionally,2DCNNappliedtoprice‐chartimagesaddressesthe
short‐term
acknowledging the stochastic nature of CNN optimization, we limitations of 1D models (e.g., long memory [LSTM]),
independently retrain the CNN five times for each model con- which are constrained to analyzing linear relationships. For ex-
figurationandaveragethepredictions to enhancerobustness. ample,a3×2filtercantreat“nochange,”“minorincrease,”and
“majorincrease”asdistinctfeatures,assigningdifferentweightsto
thesepatternsforfinalpredictions.Whenappliedtoimages,these
3.3 | Training the CNN Models filters function as indicator mechanisms for detecting different
pricemovements.
| We follow | Jiang | et  | al. (2023) | closely | in implementing |     | the CNN |     |     |     |     |
| --------- | ----- | --- | ---------- | ------- | --------------- | --- | ------- | --- | --- | --- | --- |
models. The models impose cross‐parameter constraints, signifi- Wedividetheentiredatasetintotraining,validation,andtestsets.
cantly reducing parameterization, which makes them easier to For model estimation and validation, we used data from January
trainandmoreeffectiveforpredictionsusingrelativelysmalldata 1980toDecember2000asthetrainingsample.Withinthisdataset,
sets (Krizhevsky et al. 2017; Obaid and Pukthuanthong 2022). 70%imagesarerandomlyselectedfortraining,whiletheremaining
Additionally, the CNN integrates various tools that enable the 30% are used for validation. Random sampling for training and
modeltoaccommodatedeformationsandrelocationsofkeyobjects validation helps balance the distribution of positive and negative
withintheimages.TheCNNtransformsrawimagesintoasetof labels in the classification task, mitigating potential biases caused
predictive features through a series of stacked operations, ulti- byprolongedbullishorbearishmarkettrends.Theremainingyears
matelygeneratingpredictions. (from January 2001 to October 2024) of data are reserved as the
out‐of‐sampletestdataset.
| The | CNN consists |     | of three | primary | operations: |     | convolution, |     |     |     |     |
| --- | ------------ | --- | -------- | ------- | ----------- | --- | ------------ | --- | --- | --- | --- |
activation, and pooling. Convolution operates similarly to ker- The task of predicting future returns is inherently a binary
nel smoothing. It scans the image both horizontally and verti- classification problem. The training process minimizes the
cally,summarizingthecontentofneighboringregionsforeach standardobjectivefunctionforclassificationproblems,whichis
elementintheimagematrix(Krizhevskyetal.2017).Activation thecross‐entropy loss function:
“leaky
| applies | a nonlinear |     | transformation, |     | specifically |     | the      |     |     |     |     |
| ------- | ----------- | --- | --------------- | --- | ------------ | --- | -------- | --- | --- | --- | --- |
| ReLU”   |             |     |                 |     |              |     | element‐ |     |     |     |     |
to the output of the convolution filter on an L(y,yˆ)=−y log(ˆy)−(1−y)log(1−yˆ) (2)
| wise | basis. | The final | operation | in  | the building | block | is “max |     |     |     |     |
| ---- | ------ | --------- | --------- | --- | ------------ | ----- | ------- | --- | --- | --- | --- |
pooling,” whereyˆisthesoftmaxoutputfromtheCNNinthefinalstep.If
|     | which | scans | the | input | matrix and | returns | the maxi- |     |     |     |     |
| --- | ----- | ----- | --- | ----- | ---------- | ------- | --------- | --- | --- | --- | --- |
mum value from neighboring regions in the image. This the predicted probability matches the label perfectly (yˆ =y),
reduces the data's dimensionality and noise. The final CNN theloss is 0; otherwise,theloss is positive.
| layer | is fullyconnected |     | andactivated |     | by asoftmaxfunction. |     |     |           |                    |                    |                   |
| ----- | ----------------- | --- | ------------ | --- | -------------------- | --- | --- | --------- | ------------------ | ------------------ | ----------------- |
|       |                   |     |              |     |                      |     |     | The model | consists of two to | four convolutional | layers, each fol- |
TheobjectiveoftheCNNistopredictbinaryoutcomes,wherea lowed by batch normalization (BatchNorm) to mitigate internal
value of 1 indicates a positive return within the specified covariate shifts during training (Ioffe and Szegedy 2015). Leaky
forward‐looking ReLU(Maasetal.2013)isusedastheactivationfunctionforthe
|     |     | period, | and | a value | of 0 | indicates | otherwise. |     |     |     |     |
| --- | --- | ------- | --- | ------- | ---- | --------- | ---------- | --- | --- | --- | --- |
Consequently, the fitted value of the CNN represents an esti- convolutionallayers,withtheslopeparametersetto0.01toprevent
mateoftheprobability ofapositive outcome. the “dead neuron” issue often associated with traditional ReLU
activations.Eachconvolutionaloperationisimmediatelyfollowed
Each image in our data set is represented as a pixel value ma- by max pooling, with a pooling window size of 2×1. This pro-
trix,whereblackorwhitepixelsareassignedvaluesof0or255, gressively reduces the size of feature maps, lowers computational
respectively, and each element corresponds to the grayscale complexity,andenhancesthemodel'sfocusoncriticalfeatures.
| intensity | at  | the corresponding |     | position | in  | the image. | Standard |     |     |     |     |
| --------- | --- | ----------------- | --- | -------- | --- | ---------- | -------- | --- | --- | --- | --- |
image‐processing CNNs, referred to as 2D CNNs, move their The convolutional layer parameters dynamically adapt to the
rectangular filters horizontally and vertically across the image lengthofthetimewindow(e.g.,thespanoftheinputdata).For
|         |             |     |                  |     |         |      |                | example, with | a 5‐day window | input, the | model includes two |
| ------- | ----------- | --- | ---------------- | --- | ------- | ---- | -------------- | ------------- | -------------- | ---------- | ------------------ |
| matrix. | Traditional |     | price prediction |     | methods | rely | on statistical |               |                |            |                    |
2439

 10969934, 2025, 12, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/fut.70043 by Universita Bocconi Milano, Wiley Online Library on [14/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
convolutional layers with dilation and stride parameters set to marketvalueofholdingsandthecashbalance,isupdatedatthe
1×1.2 This adaptive design enables the model to extract fea- endofeachtradingday.Dailyreturns(R )andtheirvariance(σ )
|     |     |     |     |     |     |     |     |     |     |     | d   |     | d   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
turesfrom data spanningdifferent timehorizons. arethencalculatedbasedontheseupdates,andtheSharpeRatio
(SR)iscomputedusingannualizeddailyreturns.
| After the | convolutional | layers, |     | the resulting | feature | maps are |     |     |     |     |     |     |     |
| --------- | ------------- | ------- | --- | ------------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
flattened into 1D vectors and passed to fully connected layers. R
|     |     |     |     |     |     |     |     |     | SR= | d × | days |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
The number of input features in the fully connected layers is perYear (3)
σ
d
| determined | dynamically |     | by the | output | of the convolutional |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | ------ | ------ | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
layers. For instance, assuming specific input tensors and con- 4.2 | Portfolio Performance
| volutionaloperations,theflattenedfeature |     |     |        |     | dimensionsare256 |     |             |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | ------ | --- | ---------------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
| 5‐day                                    |     |     | 20‐day |     |                  |     | Image‐based |     |     |     |     |     |     |
for a window, 512 for a window, and 1024 for a return prediction represents a technical price
60‐day window. The fully connected layers map these features trend signal. In the stock market, Jiang et al. (2023) demon-
to the number of target classes (e.g., for binary or multiclass strate that image‐based strategies are most effective over rela-
classificationtasks).3Finally,theoutputoftheCNNisasetof
|     |     |     |     |     |     |     | tively short | horizons | (5  | days). Table | 2 presents |     | the prediction |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ------------ | ---------- | --- | -------------- |
contract‐level resultsofCNNmodelsemployingimage‐basedstrategiesinthe
|     | estimates | for | commodities, |     | indicating | the proba- |     |     |     |     |     |     |     |
| --- | --------- | --- | ------------ | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
bility of a positive subsequent return over short (5‐day), US commodity futures market. Panel A reports the results for
medium(20‐day), andlong(60‐day) horizons.4 short‐horizon (5‐day‐ahead) returns, Panel B focuses on
|     |     |     |     |     |     |     | medium‐horizon |     | (20‐day‐ahead) |     |          |       |              |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------------- | --- | -------- | ----- | ------------ |
|     |     |     |     |     |     |     |                |     |                |     | returns. | Panel | C highlights |
To prevent overfitting, an early stopping mechanism is em- long‐horizon (60‐day‐ahead) returns, corresponding to weekly,
ployed.Specifically,trainingstopsifthevalidationlossdoesnot monthly, and quarterly horizons, respectively. The table eval-
improve for two consecutive epochs. Additionally, whenever uatesthepredictivepowerofthesestrategiesfromaneconomic
the validation loss decreases, the model saves its current perspective by summarizing the performance of portfolios
weights,ensuringthatthebest‐performingweightsareusedfor ranked based on CNN predictions. We emphasize the annual-
finaldeployment. ized average portfolio return and the annualized SR of the
|     |     |     |     |     |     |     | holdingperiod | returns. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | --- | --- | --- | --- | --- |
4 | CNN Prediction for US Commodity Futures Each panel reports equal‐weighted tercile portfolios. The low
Returns tercilerepresentsfutureswiththelowestprobabilityofpositive
|     |     |     |     |     |     |     | future returns | and | consistently |     | achieves | highly | negative SRs, |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --- | -------- | ------ | ------------- |
4.1 | Portfolio Construction exceeding −1.0for all imagesizes. The SRincreases monoton-
icallyacrosstheupwardtercileswhenpredictingreturnsusing
| Rebalancing | is conducted |     | on the | first day | of standard | weekly, | 20‐day images. |     |     |     |     |     |     |
| ----------- | ------------ | --- | ------ | --------- | ----------- | ------- | -------------- | --- | --- | --- | --- | --- | --- |
monthly,andquarterlycycles.Theprobabilitiesderivedfromthe
image data up to and including the trading day before the Tobenchmarktheseresults,wealsoreporttheperformanceof
rebalancingdayaresortedintotercileportfoliosbasedonout‐of‐ holding‐period (2‐12
|     |     |     |     |     |     |     | alternative |     |     | strategies | based | on  | MOM |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | ---------- | ----- | --- | --- |
sampleCNNestimatesfortheprobabilityofapositivesubsequent momentum), STR (short‐term reversal), WSTR (1‐week short‐
return.Portfoliosmaintainproportionalweightsfortheassetsin term reversal), and TREND (the trend strategy of Han
|     |     |     |     |     |     |     |     | signals.5 |     | short‐term |     |     | image‐based |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------- | --- | --- | ----------- |
eachtercile.Forfuturesat theboundaryof terciles, theiralloca- et al. 2016) In predictions,
tionsaresplitproportionallybetweentherelevantportfolios. strategies generally achieve higher SRs than traditional price‐
|     |     |     |     |     |     |     | trend‐based | strategies | (except | WSTR). | In  | medium‐ | and long‐ |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ------- | ------ | --- | ------- | --------- |
image‐based
At the time of rebalancing, the opening prices are used to cal- horizon predictions, strategies exhibit similar
results.Withintheimage‐basedstrategies,using20‐dayimages
| culate the | differences | between |     | the current | holdings | and the |     |     |     |     |     |     |     |
| ---------- | ----------- | ------- | --- | ----------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
targetportfolioweights.Adjustmentsaremadethroughbuying to predict future returns consistently outperforms predictions
|              |       |          |      |          |             |             | using5‐ |     | 60‐dayimages. |     |     |     |     |
| ------------ | ----- | -------- | ---- | -------- | ----------- | ----------- | ------- | --- | ------------- | --- | --- | --- | --- |
| and selling, | while | ensuring | that | at least | 0.1% of the | total port- | made    | or  |               |     |     |     |     |
long‐short
| folio value | is held | as cash. | We  | also construct |     | a   |     |     |     |     |     |     |     |
| ----------- | ------- | -------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
portfolio (“H‐L”), where the long positions correspond to the Specifically,fortheI20/R20horizon,theCNNmodelyieldsthe
highest tercile (“High”) and the short positions correspond to highest average return (5.66%) and SR (0.38) for the “H‐L”
(“Low”).
the lowest tercile To address the inconsistency portfolio, followed by TREND (4.49% return and 0.22 SR from
betweentheholdingperiodofeachportfolioandthepredictive the CNN), while the other strategies exhibit negative returns.
horizonofthemodelandtoensureuniformityinfuturereturn Similarly, for the I20/R60 horizon, the CNN model achieves a
periods across different time frames for more robust pattern higher return (2.55%) and SR (0.16) compared with other
predictions, the predicted values derived from images are strategies. The results remain consistent when considering the
alignedtoastandardizedhorizonof5‐,20‐,or60‐dayintervals. High portfolio for the I20/R20 horizon (7.13% return and
0.42SRfromtheCNN)andtheI20/R60horizon(2.55%return
Weconductevaluationsonaweekly,monthly,orquarterlybasis. and0.16 SRfrom theCNN).
Thefirstdayofeachcycleisdesignatedastherebalancingdate,
minimizing deviations and accounting for realistic market fric- To evaluate portfolio stability, Table 2 reports the average
tions in both experimental and practical settings. The notation turnover rate, which is calculated using the standard formula
“Ix/Ry” represents models that use x‐day image predictions to forfundturnover.Specifically,foreachrebalancingperiod,the
forecast returns over the subsequent y‐day holding period. For turnover rate is determined by dividing the absolute value of
each portfolio, the total asset value, which includes both the total purchases (|Buy| t ) and total sales (|Sell| t ) by the
| 2440 |     |     |     |     |     |     |     |     |     |     | JournalofFuturesMarkets,2025 |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- |

 10969934, 2025, 12, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/fut.70043 by Universita Bocconi Milano, Wiley Online Library on [14/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| TABLE2 | |               | PortfolioperformanceoftheCNNmodelwithotherstrategies. |                                |        |     |        |     |        |     |        |     |         |          |     |
| ------ | --------------- | ----------------------------------------------------- | ------------------------------ | ------ | --- | ------ | --- | ------ | --- | ------ | --- | ------- | -------- | --- |
|        |                 | I5/R5                                                 |                                | I20/R5 |     | I60/R5 |     | MOM/R5 |     | STR/R5 |     | WSTR/R5 | TREND/R5 |     |
|        |                 | Ret                                                   | SR                             | Ret    | SR  | Ret    | SR  | Ret SR |     | Ret SR | Ret | SR      | Ret      | SR  |
| Panel  | A:Short‐horizon |                                                       | (one‐week)portfolioperformance |        |     |        |     |        |     |        |     |         |          |     |
Low 5.92 0.38 3.53 0.22 1.96 0.13 4.11 0.23 3.24 0.18 1.49 0.08 4.46 0.23
2 0.09 0.01 4.05 0.25 5.33 0.32 2.98 0.20 5.26 0.35 4.67 0.31 3.89 0.26
High 6.93 0.41 5.11 0.31 5.56 0.34 5.32 0.27 3.98 0.21 6.92 0.37 4.11 0.23
H‐L 1.01 0.07 1.59 0.11 3.60 0.24 1.21 0.06 0.75 0.03 5.42 0.26 −0.35 −0.02
Turnover (%) 3180.69 3101.49 3013.85 646.76 1633.79 3170.02 1525.92
|       |                                      | I5/R20 |     | I20/R20 |     | I60/R20 |             | MOM/R20 |     | STR/R20 |     | WSTR/R20 | TREND/R20 |     |
| ----- | ------------------------------------ | ------ | --- | ------- | --- | ------- | ----------- | ------- | --- | ------- | --- | -------- | --------- | --- |
|       |                                      | Ret    | SR  | Ret     | SR  | Ret     | SR          | Ret SR  | Ret | SR      | Ret | SR       | Ret       | SR  |
| Panel | B:Middle‐horizon(one‐month)portfolio |        |     |         |     |         | performance |         |     |         |     |          |           |     |
Low 4.06 0.26 1.47 0.09 4.49 0.28 5.41 0.30 4.68 0.26 4.93 0.27 0.59 0.03
2 4.29 0.26 4.07 0.25 1.24 0.08 2.46 0.16 7.00 0.47 3.99 0.26 6.73 0.44
High 3.79 0.23 7.13 0.42 6.55 0.38 4.76 0.26 0.36 0.02 3.43 0.19 5.08 0.28
H‐L −0.26 −0.02 5.66 0.38 2.05 0.13 −0.65 −0.03 −4.31 −0.21 −1.51 −0.08 4.49 0.22
Turnover (%) 748.57 759.03 697.94 264.96 753.08 766.71 548.15
|     |     | I5/R60 |     | I20/R60 |     | I60/R60 |     | MOM/R60 |     | STR/R60 | WSTR/R60 |     | TREND/R60 |     |
| --- | --- | ------ | --- | ------- | --- | ------- | --- | ------- | --- | ------- | -------- | --- | --------- | --- |
|     |     | Ret    | SR  | Ret     | SR  | Ret     | SR  | Ret SR  | Ret | SR      | Ret      | SR  | Ret       | SR  |
C:Long‐horizon(one‐quarter)portfolio
| Panel |     |     |     |     |     |     | performance |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Low 4.90 0.31 3.14 0.21 3.97 0.27 5.64 0.32 3.75 0.20 4.63 0.26 4.48 0.24
2 2.62 0.16 4.71 0.30 3.15 0.19 3.58 0.24 4.40 0.30 2.67 0.17 3.43 0.23
High 5.32 0.31 5.69 0.32 5.88 0.33 2.72 0.14 4.91 0.26 4.98 0.28 4.90 0.26
| H‐L |     |      |      |      |      |      |      | −2.92 −0.14 |      |      |      |      |      |      |
| --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ----------- | ---- | ---- | ---- | ---- | ---- | ---- |
|     |     | 0.42 | 0.03 | 2.55 | 0.16 | 1.91 | 0.12 |             | 1.15 | 0.06 | 0.36 | 0.02 | 0.42 | 0.02 |
Turnover (%) 242.42 243.22 250.71 146.22 265.55 252.35 229.93
Note:ThistablecomparestheportfolioperformanceoftheCNNmodelwithotherstrategiesintheUScommodityfuturesmarket.PanelsA–Cpresentresultsforshort‐
horizon(one‐week),middle‐horizon(one‐month),andlong‐horizon(one‐quarter)performance,respectively.“Ret”isexpressedasapercentage(%).FollowingJiangetal.
(2023),webenchmarktheCNNstrategyagainstfourtraditionalpricetrendstrategies:2–12monthmomentum(MOM),1‐monthshort‐termreversal(STR),1‐weekshort‐
termreversal(WSTR),andthetrendstrategy(TREND)proposedbyHanetal.(2016),whichincorporatesshort‐,medium‐,andlong‐termpricetrends.
portfolio's total equity value (Equity). Following Pástor et al. returns from the real return curve, ensuring that observed
t
(2017,2020),theabsolutevaluesoftotalpurchasesandsalesare volatilityaccuratelyreflects real‐worldmarket fluctuations.
| computed | based | on the | hypothetical |     | trades | generated | by  | the |     |     |     |     |     |     |
| -------- | ----- | ------ | ------------ | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
portfolio'srebalancingprocessundertheproposedstrategy.The This measure provides a standardized approach to comparing
analysisassumesaninitialportfoliovalueandupdatesholdings portfolio trading activity across different time periods and
overtimeaccordingtothestrategy‐determinedweights,without single‐event
|     |     |     |     |     |     |     |     | strategies. | Unlike |     |     | turnover | rates, | it aggregates |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | --- | --- | -------- | ------ | ------------- |
considering transaction costs. The average turnover rate turnover over all trading periods, ensuring consistency in eva-
(Turnover) is then annualized to reflect the portfolio's trading luation. Annualization accounts for variations in trading fre-
activityover theyears: quency across years, enabling more intuitive comparisons. By
|     |           |     |     |      |               |     |     | averaging     | normalized |                         | turnover  | rates over | multiple | years, the  |
| --- | --------- | --- | --- | ---- | ------------- | --- | --- | ------------- | ---------- | ----------------------- | --------- | ---------- | -------- | ----------- |
|     |           |     |     |      |               |     |     | reported      | value      | reflects                | long‐term | trading    | behavior | while miti- |
|     |           |     | 1 N | 1 Ti | |Buy| +|Sell| |     |     |               |            |                         |           |            |          |             |
|     | Turnover= |     |     |      | t             | t   |     | (4) gatingthe | impactof   | short‐termfluctuations. |           |            |          |             |
|     |           |     | N   | T    | Equity        |     |     |               |            |                         |           |            |          |             |
|     |           |     | i=1 | it=1 |               | t   |     |               |            |                         |           |            |          |             |
  T o f u r th e r s tr e n g t h e n t h e b e n ch m a r k c om p a ris o n , w e a dd i -
whereT isthenumberoftradin gperiodswithinyear i,andNis tio n a ll y i n co r p o r a t e m u l ti fa ct o r st ra t e gie s fr o m B i a nc h i e t a l .
i
thetotalnumberofyearsoverwhichtheturnoverisaveraged. medium‐term
|     |     |     |     |     |     |     |     | (2015), | including | the | standard |     |     | momentum |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | -------- | --- | --- | -------- |
momentum‐reversal
|     |     |     |     |     |     |     |     | strategy | (Mom | 12–1 ) and | the | combined |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ---------- | --- | -------- | --- | --- |
We use the opening price of each period as the rebalancing strategies (Mom –Ctr , where T  {18, 24, 36, 48, 60}).6
|     |     |     |     |     |     |     |     |     |     | 12  | {T} |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
pricetoensuremeaningfulturnovercalculations.Allsignalsare These strategies integrate medium‐term momentum signals
withlong‐termreversaleffectsandareamongthemostwidely
| generated | using | data | available | at the | previous | trading |     | day's |     |     |     |     |     |     |
| --------- | ----- | ---- | --------- | ------ | -------- | ------- | --- | ----- | --- | --- | --- | --- | --- | --- |
close, eliminating future information leakage and allowing used benchmarks in the commodity futures literature. To en-
sufficient time for rebalancing preparation. Additionally, all surecomparabilitywiththeCNN2DresultsreportedinTable2,
| performance |     | metrics | are calculated |     | based | on actual |     | daily |         |            |      |        |       |     |
| ----------- | --- | ------- | -------------- | --- | ----- | --------- | --- | ----- | ------- | ---------- | ---- | ------ | ----- | --- |
|             |     |         |                |     |       |           |     | weuse | thesame | testperiod | from | 2001to | 2024. |     |
2441

 10969934, 2025, 12, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/fut.70043 by Universita Bocconi Milano, Wiley Online Library on [14/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
TABLE3 | Portfolioperformanceofdifferentmomentumandreversalstrategiesincommodityfutures.
|             |            |        | Mom    | 12–1  | Mom | –Ctr   |     | Mom –Ctr | Mom    | –Ctr  | Mom | –Ctr   | Mom | –Ctr   |
| ----------- | ---------- | ------ | ------ | ----- | --- | ------ | --- | -------- | ------ | ----- | --- | ------ | --- | ------ |
|             |            |        |        |       |     | 12     | 18  | 12 24    |        | 12 36 |     | 12 48  |     | 12 60  |
| Ann.        | Ret(%)     |        |        | −1.65 |     | 0.28   |     | 0.28     |        | 2.10  |     | −1.83  |     | 2.02   |
| Ann.        | Sharpe     |        | −0.079 |       |     | 0.011  |     | 0.011    |        | 0.086 |     | −0.077 |     | 0.083  |
| Ann.        | volatility |        |        | 0.207 |     | 0.250  |     | 0.249    |        | 0.244 |     | 0.237  |     | 0.243  |
| Skewness    |            |        |        | 0.106 |     | 0.104  |     | 0.133    |        | 0.129 |     | 0.091  |     | 0.324  |
| Kurtosis    |            |        |        | 0.939 |     | 0.487  |     | 0.646    |        | 0.901 |     | 0.490  |     | 0.822  |
| %           | ofpositive | months |        | 50.37 |     | 50.38  |     | 49.62    |        | 50.40 |     | 49.58  |     | 45.54  |
| Maxdrawdown |            |        | −0.831 |       |     | −0.829 |     | −0.793   | −0.784 |       |     | −0.826 |     | −0.797 |
Note:Inthistable,wereportthelong‐shortportfolioperformanceofvariouscombinationsofmomentumandreversalstrategiesasproposedinBianchietal.(2015).To
ensurecomparabilitywithourCNN2Dresults,weusethesametestsampleperiodfrom2001to2024.ThestrategiesincludeMom12–1,whichisapuremomentum
strategywitha12‐monthrankingperiodanda1‐monthholdingperiod,aswellasmomentum‐contrarianstrategies(Mom12 –Ctr{T},whereT=18,24,36,48,and60),
whichapplyadouble‐sortprocedure:firstrankingbasedon12‐monthmomentumandthenapplyingacontrarianrankingoverTmonths,allwitha1‐monthholding
period.Wereportannualizedreturninpercentageterms(Ann.Ret),annualizedSharperatio(Ann.Sharpe),annualizedreturnvolatility(Ann.Volatility),skewness,
kurtosis,thepercentageofpositivemonths,andmaximumdrawdown.
The findings in Table 3 show that the single‐sort momentum return (195.79%) with the lowest drawdown (30.80%). This
strategy (Mom 12–1 ) yields an annualized return of approxi- suggests that CNN models capture market dynamics most
|     | −1.65% |     |     | −0.08. |     |     |     |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mately with an SR of Among the combined effectively at this horizon, balancing predictive accuracy and
momentum‐reversaldouble‐sortstrategies, thehighest annual- riskexposure.Incontrast,PanelAshowstheshort‐term(5‐day)
–Ctr ),whilethelowestis−1.83%
izedreturnis2.10%(Mom 12 36 predictions, which exhibit high volatility and inconsistent per-
|     | –Ctr |     |     |     |     |     |     |     |     | “H‐L” |     |     |     | near‐ |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | ----- |
(Mom ). Notably, all these strategies underperform formance, with the portfolio in I5/R5 generating
|     | 12  | 48  |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
compared with the CNN 2D results in the “Ix/R20” configura- zero cumulative returns (−1.75%) and a substantial drawdown
tion, providing further evidence of the superior predictive per- (48.91%),indicatingthatshort‐termfluctuationsaredifficultto
|     |     |     |     |     |     |     |     |     |     | long‐term |     | (60‐day) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------- | --- | --- |
formance oftheCNN approach. predict reliably. For forecasts in Panel C,
|     |     |     |     |     |     |     |     | cumulative | returns | decline | steadily, | with I60/R20 |     | and I60/R60 |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------- | --------- | ------------ | --- | ----------- |
In Appendix A, we present the predictions of the univariate producingonlymodestgains(21.16%and18.00%,respectively)
model at different horizons using the same methodology as in alongside elevated drawdowns (70.83% and 50.00%, respec-
Table2.Asabenchmark,wecomparetheCNN1Dmodelwith tively). This reflects the model's diminishing predictive power
theLSTMmodels,withresultsshowninTablesA1andA2.The over extendedhorizons.
| performance |     | of the benchmark |     | models | consistently |     | falls short |     |     |     |     |     |     |     |
| ----------- | --- | ---------------- | --- | ------ | ------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
image‐based
of the CNN 2D model across all prediction horizons, high- Overall, the results confirm that predictions are
lightingthesuperiorpredictivepoweroftheCNN2Dmodelin mosteffectiveinmedium‐termtradingstrategies,particularlyin
forecastingreturns using image‐based data. 20‐dayhorizons,wherepredictivestrengthremainsrobustand
Short‐term
|     |     |     |     |     |     |     |     | risk is | better controlled. |     |     | predictions | suffer | from ex- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------------ | --- | --- | ----------- | ------ | -------- |
PanelsA–CofFigure3displaythecumulativereturncurvesfor cessive volatility, while long‐term forecasts weaken due to sig-
short‐term, medium‐term, and long‐term strategies, respec- nal decay, reinforcing the importance of selecting an optimal
(1–3)
tively. Columns correspond to strategies that predict predictingwindow.
returnsoverthenext5,20,and60days.Eachplotillustratesthe
| cumulative |     | return curves | for | different | tercile | portfolios, | along |     |     |     |     |     |     |     |
| ---------- | --- | ------------- | --- | --------- | ------- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
withthe“H‐L”portfolio,withthemaximumdrawdownpoints
|     |     |     |     |     |     |     |     | 5 | | Exploring | the | Learning | Process | of  | CNNs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------- | ------- | --- | ---- |
highlighted.
|        |            |        |            |             |     |             |       | To better | understand | the | patterns      | identified  | by  | image‐based |
| ------ | ---------- | ------ | ---------- | ----------- | --- | ----------- | ----- | --------- | ---------- | --- | ------------- | ----------- | --- | ----------- |
| Figure | 3 presents | the    | cumulative | returns     | of  | image‐based | long‐ |           |            |     |               |             |     |             |
|        |            |        |            |             |     |             |       | models,   | we employ  | two | complementary | approaches. |     | First, we   |
| short  | portfolios | across | different  | forecasting |     | horizons,   | high- |           |            |     |               |             |     |             |
examinetherelationshipbetweenCNNpredictionsandasetof
| lighting | distinct | patterns | in  | predictive | efficacy. | Portfolios | 1,  | 2,     |         |           |         |         |           |           |
| -------- | -------- | -------- | --- | ---------- | --------- | ---------- | --- | ------ | ------- | --------- | ------- | ------- | --------- | --------- |
|          |          |          |     |            |           |            |     | widely | studied | financial | signals | related | to price, | risk, and |
and3tracethecumulativereturnsofthebottom‐,middle‐,and
liquidity.Second,weutilizeregression‐basedapproximationsto
| top‐tercile |     |                           |     |         |     | “H‐L” |           |     |     |     |     |     |     |     |
| ----------- | --- | ------------------------- | --- | ------- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
|             |     | portfolios, respectively, |     | whereas |     | the   | portfolio |     |     |     |     |     |     |     |
showsthecumulativereturnofazero‐coststrategythatislong analyze the underlying data representations used by CNNs in
|     |     |     |     |     |     |     |     | image‐based | forecasting. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | --- | --- | --- | --- |
thetoptercileandshortthebottomtercile.Theresultsindicate
medium‐term
| that    | CNN   | models perform |     | best over |        |     | horizons, |     |     |     |     |     |     |     |
| ------- | ----- | -------------- | --- | --------- | ------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
|         |       |                |     |           | short‐ |     | long‐term |     |     |     |     |     |     |     |
| whereas | their | effectiveness  |     | declines  | for    | and |           |     |     |     |     |     |     |     |
predictions due to heightened volatility and weaker signal 5.1 | Relationship With Traditional Predictive
| strength. |     |     |     |     |     |     |     | Factors |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
In Panel B, the medium‐term (20‐day) predictions deliver the Our analysis focuses on several key metrics commonly associ-
strongest and most stable returns, particularly in I20/R20, atedwithassetreturnpredictability,includingpricetrendsand
“H‐L”
where the portfolio achieves the highest cumulative volatility. Table 4 reports the univariate correlations between
| 2442 |     |     |     |     |     |     |     |     |     |     |     | JournalofFuturesMarkets,2025 |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- |

 10969934, 2025, 12, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/fut.70043 by Universita Bocconi Milano, Wiley Online Library on [14/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
Differenthorizonsportfolioperformanceofimage‐basedmodelprediction.Thisfigurepresentsthecumulativereturnperformance
| FIGURE3 | |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- |
oflong‐shortportfoliosbasedonCNNmodelpredictionsacrossdifferenthorizons.Eachpanelshowsthereturntrendsoftercileportfoliosrankedby
predictedreturns.Portfolios1,2,and3tracethecumulativereturnsofthebottom,middle,andtoptercileportfolios,respectively,whilethehigh‐
minus‐low(H‐L)portfolioshowsthecumulativereturnofazero‐coststrategythatislongthetoptercileandshortthebottomtercile.Resultsindicate
| image‐based |     |     | H‐L |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- |
that predictions perform best in the middle horizons, where the portfolio maintains consistent positive returns with lower
drawdowns. As the forecasting horizon extends, the return spread narrows, with the 60‐day horizon showing weaker profitability, suggesting
diminishedpredictivepoweroverlongerperiods.Thesefindingsunderscorethemodel'seffectivenessincapturingshort‐andmiddle‐horizonprice
patternsincommodityfuturesmarketswhilehighlightingitslimitationsforlonger‐horizonpredictions.PanelA.Short‐Horizon(5‐Day)Portfolio
Performance.PanelB.Middle‐Horizon(20‐Day)PortfolioPerformance.PanelC.Long‐Horizon(60‐Day)PortfolioPerformance.
| TABLE4 | CorrelationbetweenCNNpredictionsandfuturecharacteristics. |      |       |       |       |       |            |
| ------------------------------------------------------------------ | ---- | ----- | ----- | ----- | ----- | ---------- |
| Model                                                              | MOM  | STR   | WSTR  | TREND | 52WH  | Volatility |
| I5/R5                                                              | 0.02 | −0.12 | −0.15 | 0.00  | −0.07 | 0.00       |
|                                                                    |      | −0.17 | −0.05 |       | −0.06 | −0.01      |
| I5/R20                                                             | 0.00 |       |       | 0.00  |       |            |
| I5/R60                                                             | 0.10 | −0.12 | 0.00  | −0.01 | −0.08 | −0.01      |
| I20/R5                                                             | 0.09 | −0.20 | −0.19 | 0.03  | −0.09 | −0.02      |
|                                                                    |      | −0.16 | −0.12 | −0.01 | −0.07 |            |
| I20/R20                                                            | 0.05 |       |       |       |       | 0.00       |
| I20/R60                                                            | 0.07 | −0.20 | −0.06 | −0.02 | −0.15 | 0.00       |
|                                                                    |      | −0.26 | −0.32 |       | −0.11 | −0.01      |
| I60/R5                                                             | 0.09 |       |       | 0.09  |       |            |
| I60/R20                                                            | 0.04 | −0.21 | −0.11 | −0.01 | −0.12 | 0.01       |
| I60/R60                                                            | 0.09 | −0.19 | −0.08 | −0.04 | −0.13 | 0.00       |
Note:Thistablepresentstheaveragecross‐sectionalcorrelationbetweenCNNmodelpredictionsandvariousfuturecharacteristicfactors(MOM,STR,WSTR,TREND,
52WH,andVolatility)overthetestsample.Amongthesefactors,STRexhibitsthestrongestassociationwithCNNpredictions,rangingfrom12%to26%.WSTRfollowsa
similarpatternbutweakensasthepredictionhorizonextendsfrom5‐to60‐dayimages,aligningwiththeCNNcapturingaweeklySTRpattern.ConsistentwithJiang
etal.'s(2023)findingsinthestockmarket,MOMshowsitshighestcorrelation(9%)withlong‐horizonforecastsfromlargeimages(I60/R60)anditslowestcorrelation(2%)
withshort‐horizonforecastsfromsmallimages(I5/R5).
2443

 10969934, 2025, 12, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/fut.70043 by Universita Bocconi Milano, Wiley Online Library on [14/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
these characteristics and the predictions generated by the TABLE5 | CNNpredictionsandstandardfuturescharacteristics.
| image‐based |         |               |     |            | cross‐sectional |     |     |     |     |     |       |        |        |
| ----------- | ------- | ------------- | --- | ---------- | --------------- | --- | --- | --- | --- | --- | ----- | ------ | ------ |
|             | models. | Specifically, |     | we compute |                 |     |     |     |     |     |       |        |        |
|             |         |               |     |            |                 |     |     |     |     |     | 5D/5P | 20D/5P | 60D/5P |
rankcorrelationsbetweeneachfactorandtheCNNforecastson
aperiod‐by‐period basis,thenreportthetime‐seriesaverageof Panel A:5‐day prediction
cross‐sectionalcorrelations
| these |                |              |     | over thetestsample |             | period. |      | MOM12–1 |     |     | 0.01     | 0.01     | 0.05  |
| ----- | -------------- | ------------ | --- | ------------------ | ----------- | ------- | ---- | ------- | --- | --- | -------- | -------- | ----- |
|       |                |              |     |                    |             |         |      | STR     |     |     | −0.11*** | −0.25*** | −0.08 |
| Among | these factors, | STR exhibits |     | the strongest      | association |         | with |         |     |     |          |          |       |
|       |                |              |     |                    |             |         |      | WSTR    |     |     | −0.21*** | 0.01     | 0.1   |
CNNmodelpredictions,withcorrelationcoefficientsrangingfrom
12%to26%acrossdifferentforecastinghorizons.WSTRfollowsa TREND −0.02 −0.03 −0.04
| similar pattern, |            | demonstrating | a    | strong correlation |             | with    | CNN    |            |     |     |       |       |        |
| ---------------- | ---------- | ------------- | ---- | ------------------ | ----------- | ------- | ------ | ---------- | --- | --- | ----- | ----- | ------ |
|                  |            |               |      |                    |             |         |        | 52WH       |     |     | −0.01 | −0.03 | −0.20* |
| forecasts        | in shorter | horizons      | but  | diminishing        | in strength |         | as the |            |     |     |       |       |        |
|                  |            |               |      |                    |             |         |        | Volatility |     |     | 0.02  | 0.06  | 0.04   |
| forecasting      | window     | extends       | from | 5 to 60            | days. This  | pattern | is     |            |     |     |       |       |        |
consistentwiththeCNNmodelcapturingweeklySTRsignals. McFaddenR2R² −0.45 −0.21 −0.32
|              |     |             |             |      |      | long‐horizon |     |     |     | 5D/20P |     | 20D/20P | 60D/20P |
| ------------ | --- | ----------- | ----------- | ---- | ---- | ------------ | --- | --- | --- | ------ | --- | ------- | ------- |
| MOM displays |     | its highest | correlation | (9%) | with |              |     |     |     |        |     |         |         |
forecasts(I60/R60)butexhibitsasubstantiallyweakerrelationship Panel B:20‐day prediction
| (2%) for | short‐term | predictions | (I5/R5). | Other | predictive | factors, |     |         |     |     |     |      |        |
| -------- | ---------- | ----------- | -------- | ----- | ---------- | -------- | --- | ------- | --- | --- | --- | ---- | ------ |
|          |            |             |          |       |            |          |     | MOM12–1 |     |     | 0   | 0.06 | −0.16* |
includingTrend,52‐WeekHigh(52WH),andVolatility,exhibitthe
|           |              |      |               |     |             |         |     | STR |     | −0.12* |     | −0.26*** | −0.24*** |
| --------- | ------------ | ---- | ------------- | --- | ----------- | ------- | --- | --- | --- | ------ | --- | -------- | -------- |
| strongest | correlations | with | CNN forecasts | at  | the longest | horizon |     |     |     |        |     |          |          |
(I60),suggestingthatimage‐basedmodelsextractinformationrel- WSTR −0.25*** −0.10** 0.09
longer‐term
evant to return patterns in the commodity futures TREND 0.03 −0.02 −0.06
market.ThesefindingsconfirmthatCNNscanidentifymeaningful
|     |     |     |     |     |     |     |     | 52WH |     | −0.21** |     | −0.11* | −0.58*** |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ------- | --- | ------ | -------- |
predictivesignalsfromdataabstractedintoimagerepresentations.
|     |     |     |     |     |     |     |     | Volatility |     | −0.02 |     | 0.07 | 0.21*** |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----- | --- | ---- | ------- |
To evaluate the joint explanatory power of CNN forecasts and McFaddenR2 0.72 0.88 2.10
| traditional | financial | characteristics, |     | we employ |     | panel logistic |     |     |     |     |     |     |     |
| ----------- | --------- | ---------------- | --- | --------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
regressionstomodeltheprobabilityofapositivereturnover5, 5D/60P 20D/60P 60D/60P
20, or 60days.The regressionmodel is Panel C:60‐day prediction
|     |     |     |     |     |     |     |     | MOM12–1 |     |     | 0.06 | −0.05 | −0.17* |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | ---- | ----- | ------ |
K
Logit  ( Pr ( CNN(m,n)=1 )) =β + β X +ϵ STR −0.14 −0.42*** −0.18*
|                  |     | i,t     |     | 0         | k k,i,t    | i,t | (5) |       |     |          |      |       |        |
| ---------------- | --- | ------- | --- | --------- | ---------- | --- | --- | ----- | --- | -------- | ---- | ----- | ------ |
|                  |     |         |     | k=1       |            |     |     | WSTR  |     | −0.43*** |      | −0.01 | 0.08   |
|                  |     |         |     |           |            |     |     | TREND |     |          | 0.11 | −0.01 | −0.15* |
| where CNN(m,n)=1 |     | denotes | the | CNN‐based | prediction |     | for |       |     |          |      |       |        |
i,t
|     |     |     |     |     |     |     |     | 52WH |     | −0.22* |     | −0.18* | −0.78*** |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ------ | --- | ------ | -------- |
commodityiattimet,generatedusingimagerepresentationsof
thepastmtradingdaystoforecastthepositivereturnoverthe Volatility 0.18* 0.08 0.31***
| next n days | (and       | 0 otherwise). | X    | are   | cross‐section | ranked |     |            |     |     |      |      |      |
| ----------- | ---------- | ------------- | ---- | ----- | ------------- | ------ | --- | ---------- | --- | --- | ---- | ---- | ---- |
|             |            |               |      | k,i,t |               |        |     | McFaddenR2 |     |     | 1.29 | 1.22 | 2.98 |
| predictors  | (including | MOM,          | STR, | WSTR, | TREND,        | 52WH,  |     |            |     |     |      |      |      |
Volatility),andϵ is theerror term. Note:Thistablepresentsthejointexplanatorypowerofallfeaturesforimage‐based
i,t predictions,withPanelsA,B,andCcorrespondingtoforecastsfor5‐,20‐,and
60‐dayhorizons,respectively.Weestimateapanellogisticregressionusingthe
Table5presentstheresultsofpanellogisticregressionsevaluating
cross‐sectionalranksofallfactors.Inthemultivariateregression,STRandWSTR
image‐based
the joint explanatory power of return forecasts and emergeasthemostsignificantexplanatoryvariablesacrossimagesizes,whileonly
52WHissignificantfor60‐dayimages.ThissuggeststhatwhiletheCNNdetects
standardfinancialcharacteristicsacrossdifferentforecasthorizons.
signalsassociatedwithwell‐knownpredictivevariables,itsimage‐basedpredictions
Thedependentvariableisabinaryindicatorofwhetherapositive
retaindistinctanduniquevariation.***,**,and*denotesignificanceatthe1%,5%,
and10%levels,respectively,basedonNewey–Weststandarderrors.
| return is | realized | over the | subsequent | 5, 20, | or 60 | days, and | all |     |     |     |     |     |     |
| --------- | -------- | -------- | ---------- | ------ | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
regressionsareestimatedexclusivelyonthetestsample.PanelsA,
B,andCcorrespondtopredictionhorizonsof5,20,and60days, weakensastheforecastwindowextendsto60days,suggesting
thatthemean‐revertingnatureofshort‐termreturnsdissipates
| respectively, | allowing | for a | systematic | comparison |     | of predictive |     |     |     |     |     |     |     |
| ------------- | -------- | ----- | ---------- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
performanceovervaryingtimeframes.Allpredictorvariablesare over longer periods.
| transformed | into | cross‐sectional | ranks | to mitigate |     | distributional |     |     |     |     |     |     |     |
| ----------- | ---- | --------------- | ----- | ----------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
distortionsandensurerobustness. Incontrast,the20‐daypredictionhorizon(PanelB)revealsamore
−0.12
|     |     |     |     |     |     |     |     | persistent | role of | STR | and WSTR, | with coefficients | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | --- | --------- | ----------------- | --- |
In the 5‐day prediction horizon (Panel A), STR and WSTR (significantatthe10%level)and−0.25(significantatthe1%level)
emergeasthemostsignificantpredictors,bothexhibitingstrong
|     |     |     |     |     |     |     |     | in 5D/20P, | respectively. |     | The coefficient | of WSTR | in 20D/20P is |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | --------------- | ------- | ------------- |
−0.10
negativeassociationswithfuturereturns.STRhasacoefficient (significant at the 5% level), maintaining statistical signifi-
of −0.11 in 5D/5P (significant at the 1% level), reinforcing the cancebeyondtheshortestforecastwindow.Additionally,thevari-
presence of short‐term mean reversion in price movements. able52WHexhibitsstrongerpredictivepoweratthishorizon,witha
−0.21 coefficientof−0.21in5D/20P(significantatthe5%level)and−0.11
| Similarly, | WSTR | shows | a coefficient | of  |     | in  | 5D/5P |     |     |     |     |     |     |
| ---------- | ---- | ----- | ------------- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
(significantatthe1%level),furthersupportingtheimportance in 20D/20P (significant at the 5% level), suggesting that assets
of short‐term price corrections. The statistical significance of trading near their 52‐week highs tend to experience downward
| these variables |     | persists in | the 20‐day | predictive |     | horizon | but |     |     |     |     |     |     |
| --------------- | --- | ----------- | ---------- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
correctionsoverintermediatehorizons.Volatilitybecomespositively
| 2444 |     |     |     |     |     |     |     |     |     |     |     | JournalofFuturesMarkets,2025 |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- |

 10969934, 2025, 12, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/fut.70043 by Universita Bocconi Milano, Wiley Online Library on [14/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
otherwise).ThedefinitionsofCNN(m,n)
associated with future returns in 20D/20P (coefficient=0.07) and i,t and X k,i,t arethesame
60D/20P(coefficient=0.21,significantatthe1%level),indicatinga as inEquation (5).
risk‐returntrade‐offthatstrengthensovertime.
|     |     |     |     |     |     |     | Three | regression | models | are | estimated | for | each | CNN specifi- |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | ------ | --- | --------- | --- | ---- | ------------ |
60‐day
At the prediction horizon (Panel C), most traditional cation: (i) a univariate regression using only CNN forecasts,
predictors lose significance except for 52WH, which becomes (ii) a regression including traditional characteristics but ex-
the dominant explanatory variable. The coefficient of 52WH is cluding CNN forecasts, and (iii) a multivariate regression
−0.20in60D/5P(significantatthe5%level)and−0.78in60D/
|     |     |     |     |     |     |     | incorporating |     | both CNN | forecasts |     | and standard |     | financial pre- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | --------- | --- | ------------ | --- | -------------- |
60P (significant at the 1% level), demonstrating a consistent dictors. Since the independent variables and the dependent
downward price correction effect for assets trading near their variable remain consistent across the CNN specifications, the
| 52‐week |     |     |     |     |     | long‐term |     |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
highs. This pattern aligns with mean coefficients for financial predictors remain unchanged across
reversion theories, suggesting that commodity futures experi- different models. The results suggest that the CNN forecasts
encing prolonged uptrends are more susceptible to reversals retain strong predictive power even in the presence of con-
learning‐
over extended periods. Volatility also exhibits increased signif- ventional financial predictors, indicating that deep
icance at this horizon, with a coefficient of 0.31 in 60D/60P based forecasts provide additional insights that are not fully
(significant at the 1% level), reinforcing the notion that riskier capturedby traditionalreturncharacteristics.
| assets exhibitstronger |     |     | returnpredictability |     | atlonger | horizons. |     |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | -------------------- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
image‐based
|     |     |     |     |     |     |     | The |     | return | forecasts | exhibit | strong | and | statistically |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | ------- | ------ | --- | ------------- |
The McFadden R2 values provide additional insights into the significantpredictivepoweracrossallreturnhorizons.InPanelA,
overall explanatory power of the models. In Panel A, negative the estimated coefficients on CNN increase from 0.23 at the
|     | R2  |     |     | −0.45 | −0.21) |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
McFadden (ranging from to indicate that tra- shortesthorizon(I5/R5)to0.72atthelongesthorizon(I60/R5),all
ditional financial predictors alone provide limited explanatory significant at the 1% level. Panel B shows that CNN achieves the
power, underscoring the distinctiveness of image‐based fore- bestperformanceinpredicting20‐dayreturnswithacoefficientof
|     |     |     | 20‐ | 60‐day |     | R2  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
casts. However, in the and horizons, McFadden 1.04atI60/R20.Incorporatingstandardreturnpredictorsincreases
valuesincreasesubstantially(e.g.,0.72in5D/20P,2.98in60D/ thecoefficientto1.07,suggestingaslightimprovementinpredic-
60P),reflectingagreateralignmentbetweenstandardfinancial tive power. This increasing trend suggests that CNN models
characteristicsandreturndynamicsoverlongerperiods.These effectively extract return‐relevant signals that persist and
|     |     |     |     | short‐term |     |     |     |     |     |     |     | medium‐ |     | long‐term |
| --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --------- |
patterns suggest that, whereas reversals dominate strengthen over time, particularly in and
the predictive landscape in the immediate term, longer‐term forecasts. The stability of CNN's predictive power across the uni-
price movements exhibit stronger associations with structural variate and multivariate regressions implies that its forecasts pro-
financialcharacteristics suchas prior highs andvolatility. videincrementalinformationthatisnotmerelyatransformationof
traditionalfinancialpredictors.
| The findings |     | underscore | the | time‐varying |     | nature of return |     |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | --- | ------------ | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
short‐term Amongconventionalfinancialpredictors,past‐weekreturn(WSTR)
| predictability, |     | where |     | forecasts | are | dominated by |     |     |     |     |     |     |     |     |
| --------------- | --- | ----- | --- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
rapidreversals,whilelong‐termpredictionsincreasinglyreflect
|     |     |     |     |     |     |     | exhibits | a statistically |     | significant | positive | relationship |     | with future |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | ----------- | -------- | ------------ | --- | ----------- |
structural price corrections and risk‐related factors. The returns,asreflectedintheircoefficientsof0.10(I5/R5,significantat
diminishingroleofSTRandWSTRatlongerhorizonssuggests the1%level)and0.19(I60/R5). Thisfindingalignswiththewell‐
|           |           |         |     |          |          | short‐term | documentedshort‐termmomentumeffect,whererecentgainstend |     |     |     |     |     |     |     |
| --------- | --------- | ------- | --- | -------- | -------- | ---------- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| that mean | reversion | effects |     | are more | relevant | for        |                                                         |     |     |     |     |     |     |     |
trading strategies, whereas investors with longer holding peri- topersistovershorttomediumhorizons.Conversely,52WHcon-
ods may benefit from incorporating measures such as prior sistentlyexhibitsastrongnegativeassociationwithfuturereturns,
−0.26
highs and volatility. Moreover, the improvement in model fit with coefficients ranging from (I5/R5, significant at the 1%
|     |     |     | image‐based |     |     |     |     | −0.19 |     |     |     |     |     | mean‐ |
| --- | --- | --- | ----------- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | ----- |
over time indicates that forecasts capture unique level) to (I60/R5). This pattern is consistent with
predictive information that complements traditional financial reversion effects, where futures trading near their historical highs
|              |                      |     | short‐term |                   |           |       | tendtoexperiencedownwardpricecorrectionsovertime. |     |               |              |     |      |       |            |
| ------------ | -------------------- | --- | ---------- | ----------------- | --------- | ----- | ------------------------------------------------- | --- | ------------- | ------------ | --- | ---- | ----- | ---------- |
| predictors,  | particularly         |     | in         | price             | movements | where |                                                   |     |               |              |     |      |       |            |
| conventional | factorsexhibitweaker |     |            | explanatorypower. |           |       |                                                   |     |               |              |     |      |       |            |
|              |                      |     |            |                   |           |       | In Panel                                          | B's | 20‐day return | predictions, |     | 52WH | shows | a signifi- |
Table 6 reports the results of panel logistic regressions ex- cant negative predictive effect, with its significance decreasing
image‐based
amining the predictive power of return forecasts as the prediction horizon lengthens. Other traditional predic-
for future returns, controlling for standard return predictors. tors, such as momentum (MOM) and short‐term trend in-
Theregressionsareestimatedexclusivelyonthetestsampleto dicators (TREND), display weaker and less consistent
prevent data leakage, maintaining the independence of CNN relationshipswithfuturereturns,reinforcingthelimitationsof
parameters from the data set used for evaluation. The general linear financial predictors in fully capturing complex return
form oftheregression equationcanbe expressedas: patterns. For instance, MOM remains statistically insignificant
|     |     |     |     |     |     |     | across | all specifications. |     | In  | Panel | C, however, |     | all standard |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------------- | --- | --- | ----- | ----------- | --- | ------------ |
long‐term
|     |     |     |     |     |     | K   | return | predictors | lose | their | predictive |     | power | in  |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | ---- | ----- | ---------- | --- | ----- | --- |
Logit(Pr(R >0))=β +β CNN(m,n)+ β X +ϵ forecasts, further emphasizing the challenges of using tradi-
|     | i,t,t+n |     | 0   | 1   | i,t | k k,i,t i,t |                  |     |                    |     |     |             |     |     |
| --- | ------- | --- | --- | --- | --- | ----------- | ---------------- | --- | ------------------ | --- | --- | ----------- | --- | --- |
|     |         |     |     |     |     | k=2         | tionalpredictors |     | forlong‐termmarket |     |     | prediction. |     |     |
(6)
|     |     |     |     |     |     |     | The | out‐of‐sample | McFadden |     | R2 metrics |     | further | validate the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | --- | ---------- | --- | ------- | ------------ |
n‐day
where the dependent variable equals 1 if the realized CNN's superiority. Positive values at intermediate horizons
| (R  | ) is positive | on  | commodity | i starting | from | day t (and 0 |     |     |     |     |     |     |     |     |
| --- | ------------- | --- | --------- | ---------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
i,t,t+n (e.g.,1.72forI20/R5or0.53forI60/R60)indicatethatthemodel
2445

 10969934, 2025, 12, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/fut.70043 by Universita Bocconi Milano, Wiley Online Library on [14/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| TABLE6 | CNN,futurereturns,andstandardfuturecharacteristics. |            |          |          |         |        |         |         |        |         |
| ------------------------------------------------------------ | ---------- | -------- | -------- | ------- | ------ | ------- | ------- | ------ | ------- |
|                                                              |            | I5/R5    |          |         | I20/R5 |         |         | I60/R5 |         |
| Panel A:5‐day                                                | prediction |          |          |         |        |         |         |        |         |
| CNN                                                          | 0.23***    |          | 0.23***  | 0.46*** |        | 0.44*** | 0.72*** |        | 0.71*** |
| MOM                                                          |            | −0.05    | −0.05    |         | −0.01  | −0.01   |         | 0      | −0.02   |
| STR                                                          |            | −0.01    | 0        |         | −0.07  | 0.01    |         | −0.01  | 0.06    |
| WSTR                                                         |            | 0.10***  | 0.13***  |         | 0.15*  | 0.13    |         | 0.19   | 0.16    |
| TREND                                                        |            | 0.02     | 0.02     |         | 0.08   | 0.08    |         | 0.21*  | 0.2     |
| 52WH                                                         |            | −0.26*** | −0.25*** |         | −0.2   | −0.16   |         | −0.19  | −0.15   |
| Volatility                                                   |            | 0.07**   | 0.07**   |         | −0.07  | −0.07   |         | −0.23  | −0.25*  |
OOS McFaddenR2 −0.02 0.32 0.1 −0.34 1.72 −0.2 −3.65 1.55 −3.57
|                |            | I5/R20  |               |     | I20/R20 |         |         | I60/R20 |         |
| -------------- | ---------- | ------- | ------------- | --- | ------- | ------- | ------- | ------- | ------- |
| Panel B:20‐day | prediction |         |               |     |         |         |         |         |         |
| CNN            | 0.16**     |         | 0.15* 0.54*** |     |         | 0.51*** | 1.04*** |         | 1.07*** |
| MOM            |            | 0.05    | 0.04          |     | 0.12*   | 0.09    |         | −0.02   | 0.04    |
| STR            |            | 0.04    | 0.06          |     | −0.05   | −0.01   |         | 0.15    | 0.16    |
| WSTR           |            | 0.08    | 0.1           |     | −0.04   | 0.01    |         | −0.06   | −0.06   |
| TREND          |            | 0       | 0             |     | −0.01   | −0.01   |         | −0.01   | −0.05   |
| 52WH           |            | −0.34** | −0.34**       |     | −0.18** | −0.15*  |         | −0.26*  | 0.05    |
| Volatility     |            | 0.06    | 0.06          |     | 0.08    | 0.07    |         | 0.11    | 0.02    |
OOS McFaddenR2 0.3 −0.4 −0.06 −0.52 −0.37 −0.6 −0.58 −0.31 −0.96
|                |            | I5/R60 |              |     | I20/R60 |         |         | I60/R60 |         |
| -------------- | ---------- | ------ | ------------ | --- | ------- | ------- | ------- | ------- | ------- |
| Panel C:60‐day | prediction |        |              |     |         |         |         |         |         |
| CNN            | 0.12       |        | 0.09 0.78*** |     |         | 0.79*** | 0.65*** |         | 0.64*** |
| MOM            |            | 0.21   | 0.21         |     | 0.05    | −0.02   |         | 0.06    | 0.06    |
| STR            |            | 0.03   | 0.03         |     | −0.05   | 0.08    |         | −0.05   | −0.04   |
| WSTR           |            | −0.01  | 0.01         |     | −0.03   | 0.03    |         | −0.03   | −0.02   |
| TREND          |            | −0.04  | −0.04        |     | −0.02   | −0.03   |         | 0.09    | 0.08    |
| 52WH           |            | −0.17  | −0.17        |     | −0.17   | −0.16   |         | −0.17   | −0.03   |
| Volatility     |            | −0.1   | −0.1         |     | −0.12   | −0.16   |         | −0.12   | −0.20*  |
OOS McFaddenR2 0.11 −0.31 −0.17 0.38 −0.25 0.59 0.57 −0.32 0.53
Note:Thistablepresentsslopecoefficientsfrompanellogisticregressionsoffuturereturnsonimage‐basedCNNmodelforecastsandstandardfuturecharacteristics.The
regressionsareestimatedduringthetestsampleusingCNNmodelstrainedonthetrainingsample.Additionally,thetablereportsout‐of‐sampleMcFaddenR2values,
comparingthecross‐entropylossofthetrainedmodelagainstabenchmarkmodelthatusesthefuture‐levelin‐samplemeanasthepredictor.***,**,and*denote
significanceatthe1%,5%,and10%levels,respectively,basedonNewey–Weststandarderrors.
generalizes effectively to unseen data, capturing persistent patterns. Meanwhile, the mixed performance of traditional
R2
market anomalies. In contrast, negative values at extreme predictors highlights the difficulty of using linear features to
horizons (e.g., −3.57 for I60/R5 or −0.96 for I60/R20) may capture return dynamics. The strong out‐of‐sample predictive
reflect unmodeled nonlinearities or regime shifts in low‐ performance of CNN forecasts further reinforces their applica-
bilityinfinancialmarkets,suggestingthatdeeplearning–based
| frequency regimes, | where logistic | frameworks | struggle to |     |     |     |     |     |     |
| ------------------ | -------------- | ---------- | ----------- | --- | --- | --- | --- | --- | --- |
approximateabruptmarkettransitions.Thesefindingsresonate modelscanserveasvaluabletoolsforreturnforecastinginboth
withtheadaptivemarkethypothesis,suggestingthattheCNN's short‐termand long‐terminvestment strategies.
advantageliesinidentifyingslow‐decayinginefficiencies,while
short‐termnoise
remains challenging tosystematize. InAppendixB,weemployalogisticregressiontoapproximate
|     |     |     |     | the | predictive | performance | of the CNN | model. Given | that the |
| --- | --- | --- | --- | --- | ---------- | ----------- | ---------- | ------------ | -------- |
These findings reinforce the superiority of deep learning tech- CNNarchitecturefunctionsasaprobabilisticclassifier,logistic
niquesinidentifyingcomplexreturnsignalsthatextendbeyond regression serves as an appropriate approximation model, en-
those captured by traditional financial predictors. The statisti- ablingalinearizedinterpretationoftheCNN'sdecision‐making
cally significant and increasing coefficients of CNN forecasts process.ByestimatingtherelationshipsbetweenCNNforecasts
confirmthatthesemodelssuccessfullyextractpersistentreturn and fundamental market variables, we assess the extent to
| 2446 |     |     |     |     |     |     |     | JournalofFuturesMarkets,2025 |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- |

 10969934, 2025, 12, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/fut.70043 by Universita Bocconi Milano, Wiley Online Library on [14/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| TABLE7   | | PortfolioperformanceoftheCNNmodelfordifferentsectors. |       |             |       |     |        |       |       |           |       |        |      |
| -------- | ------------------------------------------------------- | ----- | ----------- | ----- | --- | ------ | ----- | ----- | --------- | ----- | ------ | ---- |
|          |                                                         |       | Agriculture |       |     | Energy |       |       | Livestock |       | Metals |      |
|          |                                                         | Ret   |             | SR    |     | Ret    | SR    | Ret   |           | SR    | Ret    | SR   |
| Low      |                                                         | 1.36  |             | 0.10  |     | −3.81  | −0.11 | −3.93 |           | −0.16 | 6.28   | 0.44 |
| 2        |                                                         | −1.76 |             | −0.13 |     | 9.53   | 0.28  | −0.20 |           | −0.01 | 2.15   | 0.17 |
| High     |                                                         | 6.73  |             | 0.32  |     | 5.37   | 0.16  | 3.35  |           | 0.19  | 9.62   | 0.41 |
| H‐L      |                                                         | 5.37  |             | 0.26  |     | 9.18   | 0.36  | 7.28  |           | 0.27  | 3.34   | 0.16 |
| Turnover | (%)                                                     |       | 662.67      |       |     | 765.28 |       |       | 635.17    |       | 614.88 |      |
Note:ThistablepresentstheportfolioperformanceoftheCNNmodelacrossdifferentsectors(Agriculture,Energy,Livestock,andMetals,asshowninTable1).Wereport
theresultsbasedontheI20/R20methodologyforitsbestperformance.Forindividualcommodityfutures,weareunabletoconstructseparateportfolios,soweutilizethe
full‐samplemodel,trainedacrossallsectors,tobacktestthefuturesofeachsector.TheEnergysectoryieldsthehighestlong‐shortreturnat9.18%,withanSRof0.36.The
Livestocksectorfollowswithalong‐shortreturnof7.28%andanSRof0.27.TheAgricultureandMetalssectorsrankthirdandfourth,withlong‐shortreturnsof5.37%and
3.34%andSRsof0.26and0.16,respectively.
return‐relevant short‐termcommodityreturnforecasting(Gongetal.2022;Gao
| which the | deep learning | model | captures |     |     | infor- |     |     |     |     |     |     |
| --------- | ------------- | ----- | -------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
mation beyondtraditional financialindicators. et al. 2025). However, these studies often require extensive
|     |     |     |     |     |     |     | domain‐specific | calibration |     | or focus on | a narrow set | of assets, |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ----------- | --- | ----------- | ------------ | ---------- |
TofurthervalidatethepredictiveperformanceofourCNNmodel, limitingtheir extensibility.
weusethefull‐samplemodeltrainedacrossfoursectors(Energy,
Livestock,Agriculture,andMetals)tobacktestthefuturesofeach Our study adopts a unified CNN architecture to forecast fu-
sector. As shown in Table 7, the Energy sector generates the turesreturnsacrossenergy,livestock,agriculture,andmetals
long‐short
highest return at 9.18%, with an SR of 0.36. The Live- sectors. The model achieves consistent predictive accuracy
stocksectorfollowswithalong‐shortreturnof7.28%andanSRof and generates robust long‐short signals across commodities
0.27. The Agriculture and Metals sectors rank third and fourth, with diverse fundamentals. Compared with prior methods
long‐short
with returns of 5.37% and 3.34% and SRs of 0.26 and that often target individual assets or require extensive
0.16,respectively.Theseresultsdemonstratetherobustnessofthe domain‐specific calibration, our approach demonstrates
CNNmodelacrossdifferentmarketsectors,highlightingitseffec- strong generalization across heterogeneous markets. These
tivenessinpredictingsector‐specificfutures.
|     |     |     |     |     |     |     | results contribute |     | to the        | existing literature | and highlight | the    |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------------- | ------------------- | ------------- | ------ |
|     |     |     |     |     |     |     | practical value    | of  | deep learning | models              | in commodity  | return |
Building on a growing body of research in commodity futures forecasting and portfolio‐level applications, particularly in
risk‐adjusted
forecasting, recent studies have found that ML methods, particu- enhancing performance.
| larly deep | learning models, | are | better | suited than | traditional | sta- |     |     |     |     |     |     |
| ---------- | ---------------- | --- | ------ | ----------- | ----------- | ---- | --- | --- | --- | --- | --- | --- |
tisticalapproachesforcapturingnonlineardynamicsandstructural Overall, the results confirm that image‐based forecasts extract
shifts in price behavior. For instance, in agricultural markets, meaningful return signals that extend beyond conventional
|     |     |     | long‐ | short‐term |     | time‐series |     |     |     |     |     |     |
| --- | --- | --- | ----- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Ouyang et al. (2019) employ a and financial variables. The logistic regression analysis demon-
network to capture both high‐ and low‐frequency features of strates that CNN models systematically incorporate extreme
multivariate series, achieving significant improvements over pricemovements,trenddeviations,andliquidityconditionsinto
haveintroducedtext‐
benchmark models. Similarly, recentworks return expectations. The significant improvement in return
basedandhybridfeatureextractionmethods,suchastheintegra- classification, even after controlling for traditional predictors,
tionofemotionalsignalsortopicmodelingfromnews,toenhance underscores the value of deep learning techniques in financial
forecasting performance for specific commodities like soybean, forecasting, particularly in markets where complex, nonlinear
pork,andcorn(Anetal.2023;Wuetal.2024;WangandLiu2025). interactions drivepricemovements.
| While these     | methods  | have | demonstrated | promising |     | accuracy  |     |     |     |     |     |     |
| --------------- | -------- | ---- | ------------ | --------- | --- | --------- | --- | --- | --- | --- | --- | --- |
| within targeted | domains, | they | are largely  | designed  | and | evaluated |     |     |     |     |     |     |
withinsingle‐commoditycontexts.
|     |     |     |     |     |     |     | 5.2 | Transfer |     | Learning |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | --- | --- | --- |
In energy and metals markets, prior research has frequently Transferlearningenablestheapplicationofpredictivepatterns
fromonemarkettoanother,leveraginginsightsfromdata‐rich
focusedonvolatilityforecastingordirectionalpredictionusing
neuralnetworks,randomforests,orensemblelearningmethods environments to enhance forecasting in markets with limited
(Herreraetal.2019;Luetal.2022;ForoutanandLahmiri2024). historical data. Compared with the United States, the Chinese
More recent developments have also introduced feature selec- commodity futures market has a shorter history and a more
tionandmodelinterpretabilitytechniques,includingtheuseof constrained data set, making it challenging to train complex
Shapley value decomposition to assess the marginal impact of deep learning models effectively. If return‐predictive patterns
macroeconomic and market‐specific variables on return pre- from US commodity futures generalize across markets, their
diction(ElHokayemetal.2024;WangandZhang2024).Other direct applicationto China couldmitigate data limitations and
contributions emphasize the use of high‐dimensional data in- improve forecasting accuracy. However, this generalizability
puts,includingtext‐derivedsentimentindicesanddeepfeature remains an empirical question given the structural differences
representations from models such as transformers, to improve betweenthetwo markets.
2447

 10969934, 2025, 12, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/fut.70043 by Universita Bocconi Milano, Wiley Online Library on [14/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
–
To test the feasibility of international transfer learning, we further, with I60/R60 showing negative or zero Transfer
|     |     |     |     |     |     |     |     | “H‐L” |     | (−0.66%, | SR=–0.06). |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | -------- | ---------- | --- |
applyaCNNmodeltrainedonUScommodityfuturestopredict Retrain return differences These
returns intheChinese market.The transferlearning approach findings show that direct transfer lacks stable predictive ad-
directlyemploysCNNmodelsestimatedonUSdatatoforecast vantagesandis particularly ineffectiveover longer horizons.
| Chinese | commodity | futures | returns | without | retraining. | We  |     |     |     |     |     |     |
| ------- | --------- | ------- | ------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
constructtercile‐rankedportfoliosbasedontheseforecastsand In summary, direct transfer fails to systematically outperform
evaluate their out‐of‐sample returns and SRs, comparing them retraining and, in most cases, results in weaker return pre-
to CNNmodels trainedexclusively on Chinesemarket data. dictability. Although isolated instances of marginal improve-
|     |     |     |     |     |     |     | ment exist, | they | are neither | robust | nor consistent | across |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ----------- | ------ | -------------- | ------ |
Thedatasetconsistsof36Chinesecommodityfuturescontracts horizons, underscoring the necessity of market‐specific adap-
from 1998 to 2024 (Bianchi et al. 2021; Liu et al. 2021; Ming tation in commodity futures return prediction. The observed
et al. 2023). The sample is divided into a training period differences across these implementation strategies suggest that
(1998–2008), with 70% allocated for training and 30% for vali- whereas image‐based models have demonstrated success in
|     |     | post‐2009 |     |     | out‐of‐sample |     | cross‐market |     |     |     |     |     |
| --- | --- | --------- | --- | --- | ------------- | --- | ------------ | --- | --- | --- | --- | --- |
dation, while the period serves as the transferability within many international stock
data set. The data set covers contracts from the Shanghai Fu- markets(Jiangetal.2023),theireffectivenessdoesnotextendto
turesExchange,DalianCommodityExchange,andZhengzhou commodity futuresmarkets.
| Commodity | Exchange, | spanning |     | four primary | sectors: | (i) met- |     |     |     |     |     |     |
| --------- | --------- | -------- | --- | ------------ | -------- | -------- | --- | --- | --- | --- | --- | --- |
als, (ii) industrial materials, (iii) energy, and (iv) agricultural We replicate the results of transfer learning using 15 Chinese
products. This broad coverage enables a robust assessment of commodity futures contracts that most closely match the
cross‐market return predictability across different commodity product specifications of their corresponding US counterparts.
groups. Table C1 in Appendix C presents these 15 comparable com-
modityfuturesandreportsthereturncorrelationsbetweentheir
Table 8 compares the performance of image‐based return pre- counterparts in the US and Chinese markets. The results indi-
|     |     |     |     |     |     |     |     |     | correlations—below |     |     | cases— |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | ------ |
dictions in the Chinese commodity futures market using two cate generally low 0.3 in most
approaches:(i)retrainingtheCNNmodelonChinesedataand except for three metals: nickel (0.41), zinc (0.38), and silver
(ii) directly transferring the US‐trained CNN model without (0.31). As shown in Table C2, the findings are qualitatively
modification, while also reporting the performance differential consistentwiththoseinTable8,whichusesabroadersetof36
| (“Transfer | – Retrain”). |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The results reveal systematic under- Chinese futures contracts: there is no observed benefit from
performance of direct transfer compared with retraining, par- transferlearning.
| ticularly | in capturing |     | cross‐sectional |     | return patterns | and |     |     |     |     |     |     |
| --------- | ------------ | --- | --------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
risk‐adjusted
generating returns. Two factors explain why transfer learning does not work in
|     |     |     |     |     |     |     | commodity | markets. | First, | commodity | futures returns | are |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ------ | --------- | --------------- | --- |
Panel A examines short‐horizon portfolio performance, show- heavily influenced by localized supply‐demand imbalances,
ingthatwhereasdirecttransferslightlyoutperformsretraining government policies, and inventory cycles, which exhibit sub-
(“H‐L” stantialmarket‐specificvariations.Unlikestockmarkets,where
| in I5/R5 |     | return | difference=0.07%, |     | SR  | difference= |     |     |     |     |     |     |
| -------- | --- | ------ | ----------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
0.01), this advantage diminishes as the prediction horizon ex- global macroeconomic forces and common risk factors create
tends. In I20/R5 and I60/R5, Transfer – Retrain “H‐L” return structural similarities, commodity markets are shaped by
differencesdropto−0.84%and−1.32%,withSRsof−0.09and
|     |     |     |     |     |     |     | idiosyncratic | economic | and | geopolitical | factors | that limit |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | --- | ------------ | ------- | ---------- |
−0.12, respectively. Additionally, direct transfer results in the generalizability of a model trained in one country to
higher turnover, increasing trading frequency without improv- another. Second, Chinese commodity futures markets exhibit
short‐horizon
ing returns, reinforcing its failure in predictions distinctcharacteristicscomparedwithUScommoditymarkets,
for Chinesecommodity futures. including differences in liquidity conditions, regulatory struc-
|                |     |     |     |     |     |     | tures, and | market | participant | composition, | which can | signifi- |
| -------------- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ----------- | ------------ | --------- | -------- |
| middle‐horizon |     |     |     |     |     | –   |            |        |             |              |           |          |
In the setting (Panel B), Transfer Retrain cantly impact priceformationdynamics.
“H‐L”
| shows systematically |     | positive |     | return | differences, | partic- |     |     |     |     |     |     |
| -------------------- | --- | -------- | --- | ------ | ------------ | ------- | --- | --- | --- | --- | --- | --- |
ularly in I20/R20 (“H‐L” return=2.34%, SR=0.22). However, Recent studies provide further insights into the failure of
this improvement stems from retraining underperformance transfer learning in this context. Chinese commodity futures
short‐term
ratherthanthesuperiorityofdirecttransfer.Thedirecttransfer markets are dominated by retail speculators. As of
models fail to generate consistently strong return differentials, 2016, individual investors accounted for over 86% of open
asallIx/R20portfoliosshow“H‐L”returnsbelow1%withnear‐ interest and had an average holding period of less than 4h,
zero SRs. The lack of stable outperformance suggests direct whereas US exchanges are predominantly institution driven
transfer offers no meaningful advantage over retraining in the (Fan and Zhang 2020). Retail dominance in China interacts
Chinese market. Weak results from both methods indicate withstringenttradingrules—suchasmultitierdailypricelimits
image‐based
potential fundamental limitations of models for (±4% for nondelivered contracts and ±6% for delivery con-
| medium‐term |     |     |     |     |     |     |     |     | margin‐based |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- |
returnpredictionincommodities. tracts) and strict position caps that prevent in-
|     |     |     |     |     |     |     | dividuals | from participating |     | in the | delivery month. | These |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------------ | --- | ------ | --------------- | ----- |
Panel C confirms direct transfer's inapplicability in long‐ constraints shift liquidity away from the front‐month contract,
middle‐horizon
horizon settings. Like the results, although and individual traders are restricted to a maximum of 10% of
“Transfer – Retrain” reaches 2.58% (SR=0.36) in I5/R60, this outstanding open interest (Bianchi et al. 2021). Consequently,
gain results from retraining failures rather than direct transfer the market is highly speculative. Aggregate trading volume is
261timesopeninterest—farabovetheNorthAmericanratioof
| effectiveness. | As  | the horizon | extends, | direct | transfer | weakens |     |     |     |     |                              |     |
| -------------- | --- | ----------- | -------- | ------ | -------- | ------- | --- | --- | --- | --- | ---------------------------- | --- |
| 2448           |     |             |          |        |          |         |     |     |     |     | JournalofFuturesMarkets,2025 |     |

.tekramserutufytidommocesenihCniledomNNCehtfoecnamrofrepoiloftroP
|
8ELBAT
niarteR–refsnarT
refsnarttceriD
niarteR
5R/06I
5R/02I
5R/5I
5R/06I
5R/02I
5R/5I
5R/06I
5R/02I
5R/5I
RS
teR
RS
teR
RS
teR
RS
teR
RS
teR
RS
teR
RS
teR
RS
teR
RS
teR
ecnamrofrepoiloftrop)keew‐eno(noziroh‐trohS
:AlenaP
81.0
51.1
30.0
71.0
10.0−
80.0−
23.0
41.3
73.0
26.3
72.0
6.2
52.0
83.2
63.0
15.3
62.0
56.2
woL
91.0−
82.1−
90.0
55.0
80.0
35.0
23.0
12.3
63.0
65.3
63.0
67.3
14.0
60.4
23.0
91.3
43.0
14.3
2
20.0−
71.0−
11.0−
76.0−
0
10.0−
23.0
57.3
82.0
3.3
63.0
60.4
33.0
68.3
33.0
47.3
73.0
70.4
hgiH
21.0−
23.1−
90.0−
48.0−
10.0
70.0
80.0
16.0
40.0−
23.0−
2.0
64.1
91.0
84.1
30.0
32.0
2.0
24.1
L‐H
17.3602
11.7312
83.6912
61.6681
55.7102
44.1812
)%(revonruT
niarteR–refsnarT
refsnarttceriD
niarteR
02R/06I
02R/02I
02R/06I
02R/02I
02R/5I
02R/06I
02R/02I
02R/5I
02R/5I
RS
teR
RS
teR
RS
teR
RS
teR
RS
teR
RS
teR
RS
teR
RS
teR
RS
teR
ecnamrofrep
oiloftrop)htnom‐eno(
noziroh‐elddiM:BlenaP
82.0−
57.1−
63.0−
82.2−
60.0−
63.0−
92.0
48.2
63.0
73.3
93.0
87.3
34.0
4
94.0
88.4
4.0
20.4
woL
25.0
5.3
93.0
66.2
30.0
2.0
4.0
50.4
23.0
72.3
62.0
66.2
71.0
37.1
41.0
5.1
62.0
35.2
2
20.0−
61.0−
10.0
60.0
91.0
81.1
3.0
15.3
92.0
74.3
53.0
70.4
13.0
26.3
13.0
34.3
92.0
82.3
hgiH
51.0
85.1
22.0
43.2
61.0
45.1
90.0
76.0
10.0
90.0
40.0
92.0
50.0−
83.0−
81.0−
64.1−
90.0−
37.0−
L‐H
15.394
57.805
95.905
99.374
23.125
56.715
)%(revonruT
niarteR–refsnarT
refsnarttceriD
niarteR
06R/06I
06R/02I
06R/5I
06R/06I
06R/02I
06R/5I
06R/06I
06R/02I
06R/5I
RS
teR
RS
teR
RS
teR
RS
teR
RS
teR
RS
teR
RS
teR
RS
teR
RS
teR
ecnamrofrep
oiloftrop)retrauq‐eno(noziroh‐gnoL
:ClenaP
42.0
74.1
1.0−
46.0−
61.0
67.0
24.0
69.3
52.0
14.2
44.0
61.4
13.0
99.2
13.0
38.2
83.0
66.3
woL
10.0−
80.0−
13.0
1.2
33.0−
50.2−
52.0
14.2
33.0
22.3
12.0
60.2
62.0
64.2
91.0
38.1
43.0
24.3
2
11.0
18.0
71.0
30.1
85.0
53.3
73.0
95.4
4.0
97.4
23.0
28.3
43.0
50.4
43.0
11.4
41.0
16.1
hgiH
60.0−
66.0−
71.0
76.1
63.0
85.2
70.0
26.0
3.0
93.2
40.0−
43.0−
31.0
60.1
61.0
82.1
52.0−
50.2−
L‐H
88.461
79.361
80.171
62.161
39.461
60.371
)%(revonruT
‐elddim,)keew‐eno(noziroh‐trohsotdnopserrocC–AslenaP.tekramserutufytidommocesenihCehtniseigetartsrehtoedisgnolaledomNNCehtfoecnamrofrepoiloftropelicretelpmas‐fo‐tuodezilaunnaehtstneserpelbatsihT:etoN gnisuledomNNChcaesniartertahteno:seigetartsdesab‐egamiowterapmocew,)3202(.lategnaiJgniwolloF.)%(egatnecrepasadesserpxesi”teR“.ylevitcepser,ecnamrofrep)retrauq‐eno(noziroh‐gnoldna,)htnom‐eno(noziroh
.gniniartertuohtiwatadSUnodeniartsledomNNCsrefsnartyltceridtahtrehtonadnaatadserutufytidommocesenihC
2449
10969934,
2025,
12,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/fut.70043
by
Universita
Bocconi
Milano,
Wiley
Online
Library
on
[14/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules of use; OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 10969934, 2025, 12, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/fut.70043 by Universita Bocconi Milano, Wiley Online Library on [14/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
DataAvailabilityStatement
31reportedbyFanetal.(2022).Inaddition,liquidity,volatility,
deferred‐month
and basis dynamics are concentrated in con- FuturesdatawereobtainedfromCommoditySystemsInc.(CSI).
| tracts rather | than | in the nearby | contracts |     | that underpin | most |     |     |     |     |     |     |     |
| ------------- | ---- | ------------- | --------- | --- | ------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
USprice‐imagestudies.
Endnotes
|                     |     |                 |     |        |               |           | 1Gao et | al. (2025) | demonstrate | the | important | role of ChatGPT | in  |
| ------------------- | --- | --------------- | --- | ------ | ------------- | --------- | ------- | ---------- | ----------- | --- | --------- | --------------- | --- |
| These institutional |     | characteristics |     | create | a significant | distribu- |         |            |             |     |           |                 |     |
forecastingcommoditymarketdynamics.Weleavetheexplorationof
| tionalshiftforanyCNNtrainedon |     |     |     | USdata. | Dailypricelimits |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | ------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
howChatGPTcanenhanceourresultsforfutureresearch.
| truncate           | extreme | returns and | generate  | steplike | intraday    | price     |        |                |         |               |     |                 |      |
| ------------------ | ------- | ----------- | --------- | -------- | ----------- | --------- | ------ | -------------- | ------- | ------------- | --- | --------------- | ---- |
|                    |         |             |           |          |             |           | 2For a | 20‐day window, | a third | convolutional |     | layer is added, | with |
| charts. Meanwhile, |         | liquidity   | migration |          | to deferred | contracts |        |                |         |               |     |                 |      |
dilationadjustedto2×1andstrideto3×1.Fora60‐daywindow,a
disruptstheconsistentfront‐monthterm‐structurepatternsthat
fourthconvolutionallayerisadded,withdilationsetto3×1.
CNNsinterpretashigh‐orderspatialfeatures.Theprevalenceof
|              |      |            |            |     |       |             | 3To mitigate | overfitting, | dropout | is applied | after | the fully | connected |
| ------------ | ---- | ---------- | ---------- | --- | ----- | ----------- | ------------ | ------------ | ------- | ---------- | ----- | --------- | --------- |
| retail order | flow | introduces | fat‐tailed |     | noise | and herding |              |              |         |            |       |           |           |
layers,randomlymasking50%oftheneurons'outputstoimprovethe
| dynamics. | Furthermore, | global | information |     | is  | primarily ab- |         |                 |        |           |         |             |       |
| --------- | ------------ | ------ | ----------- | --- | --- | ------------- | ------- | --------------- | ------ | --------- | ------- | ----------- | ----- |
|           |              |        |             |     |     |               | model's | generalization. | During | training, | weights | are updated | using |
sorbed via overnight price gaps, with intraday returns driven stochastic gradient descent combined with the Adam optimizer
largelybydomesticorderflow,notbyUSmarketco‐movements
(KingmaandBa2014;Srivastavaetal.2014).Theinitiallearningrate
(Fung et al. 2013). Taken together, the truncation of tails, issetto1×10−5.
| liquidity | shifts | across maturities, | and | jump‐driven |     | information |            |                    |     |         |         |            |            |
| --------- | ------ | ------------------ | --- | ----------- | --- | ----------- | ---------- | ------------------ | --- | ------- | ------- | ---------- | ---------- |
|           |        |                    |     |             |     |             | 4Note that | return information |     | appears | only in | the output | target and |
flows violate the covariate stability assumption that underpins notasanadditionalinputchannel.
| transfer | learning. | The pixel‐level |     | distributions, |     | temporal |            |        |             |     |       |           |          |
| -------- | --------- | --------------- | --- | -------------- | --- | -------- | ---------- | ------ | ----------- | --- | ----- | --------- | -------- |
|          |           |                 |     |                |     |          | 5Following | Han et | al. (2016), | the | TREND | factor is | computed |
dependencies,andlabeldynamicsobservedinChinesemarkets
|     |     |     |     |     |     |     | each month | by ranking | commodities |     | on composite | moving‐average |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | ----------- | --- | ------------ | -------------- | --- |
diverge substantially from the US data used during model trendsignalsandtakinganequal‐weightedlongpositioninthetop
training,thereby preventingeffective generalization. groupagainstanoffsettingshortpositioninthebottomgroup,with
theresultinglong‐minus‐shortreturndefiningthefactor.
|     |     |     |     |     |     |     | 6InBianchietal.(2015),Mom |     |     | referstoamomentumstrategythat, |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | ------------------------------ | --- | --- | --- |
12–1
6 | Conclusion ateachmonthT,rankscommoditiesintotercilesbasedontheirpast
|     |     |     |     |     |     |     | 12‐month | returns, | going long | the top | tercile | and short the | bottom |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ---------- | ------- | ------- | ------------- | ------ |
tercile,withaholdingperiodof1month.Thedouble‐sortstrategies,
| Building | on the | success of | image‐based | methodsin |     | stockmar- |              |     |                                             |     |     |     |     |
| -------- | ------ | ---------- | ----------- | --------- | --- | --------- | ------------ | --- | ------------------------------------------- | --- | --- | --- | --- |
|          |        |            |             |           |     |           | denotedasMom |     | –Ctr ,applyatwo‐stageprocedure:thefirstsort |     |     |     |     |
ket prediction, we extend deep learning applications to com- 12 {T}
|     |     |     |     |     |     |     | ranks using | 12‐month | momentum |     | (Mom ), | and the second | sort |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | -------- | --- | ------- | -------------- | ---- |
12
modity futures markets by employing CNNs to analyze OHLC appliesacontrarianrankingoverTmonths,whereTis18,24,36,48,
price charts. We bypass the limitations of parametric models, or 60 months. The double‐sort strategy takes long positions in
which rely on restrictive assumptions, and instead capture medium‐termwinnersthatarelong‐termlosersandshortpositions
nonlinear price dynamics such as volatility clustering and inmedium‐termlosersthatarelong‐termwinners.Allstrategiesuse
a1‐monthholdingperiod.
| leverage | effects. | Empirical | results | show | that CNNs | improve |     |     |     |     |     |     |     |
| -------- | -------- | --------- | ------- | ---- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
returnpredictionaccuracy,particularlyovershort‐tomedium‐
| termhorizons.Amongtestedconfigurations,modelstrainedon |     |     |     |     |     |     | References |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
20‐day
OHLC charts perform most consistently, balancing sig- Adrian, T., R. K. Crump, and E. Moench. 2013. “Pricing the Term
nal persistence and noise reduction. Portfolios based on CNN Structure With Linear Regressions.” Journal of Financial Economics
predictionsachievesuperiorrisk‐adjustedreturns,asevidenced 110,no.1:110–138.
by higher SRs, highlighting the framework's utility for trading An, W., L. Wang, and D. Zhang. 2023. “Comprehensive Commodity
strategies. PriceForecastingFrameworkUsingTextMiningMethods.”Journalof
Forecasting42,no.7:1865–1888.
WeshowtheCNNmodelstrainedonUScommodityfuturesfail
Bianchi,R.J.,M.E.Drew,andJ.H.Fan.2015.“CombiningMomentum
on Chinese commodity futures. Structural differences, includ- WithReversal inCommodityFutures.” JournalofBanking &Finance
| ing supply‐demand     |     | dynamics | and | regulations,    | hinder | transfer-   | 59:423–444. |           |         |                |             |           |     |
| --------------------- | --- | -------- | --- | --------------- | ------ | ----------- | ----------- | --------- | ------- | -------------- | ----------- | --------- | --- |
| ability, highlighting |     | the need | for | market‐specific |        | adaptation. |             |           |         |                |             |           |     |
|                       |     |          |     |                 |        |             | Bianchi, R. | J., J. H. | Fan,and | T. Zhang.2021. | “Investable | Commodity |     |
Overall, our work underscores the potential of integrating PremiainChina.”JournalofBanking&Finance127:106127.
| computer    | vision   | with financial |           | econometrics, |           | offering both |            |        |           |       |                   |     |            |
| ----------- | -------- | -------------- | --------- | ------------- | --------- | ------------- | ---------- | ------ | --------- | ----- | ----------------- | --- | ---------- |
|             |          |                |           |               |           |               | Boons, M., | and M. | P. Prado. | 2019. | “Basis‐Momentum.” |     | Journal of |
| theoretical | insights | into price     | formation | and           | practical | tools for     |            |        |           |       |                   |     |            |
Finance74,no.1:239–279.
marketparticipants.
|     |     |     |     |     |     |     | Chen, J.          | F., W. L. Chen, | C.  | P. Huang,   | S. H. Huang, | and A.         | P. Chen |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --------------- | --- | ----------- | ------------ | -------------- | ------- |
|     |     |     |     |     |     |     | (2016, November). | “Financial      |     | Time‐Series | Data         | Analysis Using | Deep    |
ConvolutionalNeuralNetworks.”In20167thInternationalConference
| Acknowledgments |     |     |     |     |     |     | onCloudComputingandBigData(CCBD),87–92.IEEE. |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
Liu acknowledged thesupport by Shanghai Municipal Education Chen,L.,M.Pelger,andJ.Zhu.2024.“DeepLearninginAssetPricing.”
Commission Special Program on AI‐Driven Reform of Scientific ManagementScience70,no.2:714–750.
ResearchParadigmsandDisciplinaryAdvancement(24KXZNA19)and
Cheng,D.,Y.Liao,andZ.Pan.2023.“TheGeopoliticalRiskPremium
| the National | Natural | Science | Foundation | of  | China (72121002). | We  |     |     |     |     |     |     |     |
| ------------ | ------- | ------- | ---------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
intheCommodityFuturesMarket.”JournalofFuturesMarkets43,no.
thanktwoanonymousreviewersfortheirvaluablecomments.
8:1069–1090.
Cohen,N.,T.Balch,andM.Veloso.2020October.“TradingviaImage
ConflictsofInterest Classification.”InProceedingsoftheFirstACMInternationalConference
onAIinFinance,1–6.ACM.
Theauthorsdeclarenoconflictsofinterest.
| 2450 |     |     |     |     |     |     |     |     |     |     | JournalofFuturesMarkets,2025 |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- |

 10969934, 2025, 12, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/fut.70043 by Universita Bocconi Milano, Wiley Online Library on [14/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
Erb,C.B.,andC.R.Harvey.2006.“TheStrategicandTacticalValueof “Return
|     |     |     |     |     |     |     |     | Keloharju, | M., J. T. | Linnainmaa, | and P. | Nyberg. | 2016. | Sea- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ----------- | ------ | ------- | ----- | ---- |
CommodityFutures.”FinancialAnalystsJournal62,no.2:69–97. sonalities.”JournalofFinance71,no.4:1557–1590.
“Dividend
Fama, E. F., and K. R. French. 1988. Yields and Expected Kingma,D.P.,andJ.Ba.2014.Adam:AMethodforStochasticOpti-
StockReturns.”JournalofFinancialEconomics22,no.1:3–25.
mization,preprint,arXiv:1412.6980.
Fan,J.H.,D.Mo,andT.Zhang.2022.“The‘NecessaryEvil’inChinese Krizhevsky,A.,I.Sutskever,andG.E.Hinton.2017.“ImageNetClassi-
CommodityMarkets.”JournalofCommodityMarkets25:100186. ficationWithDeepConvolutionalNeuralNetworks.”Communicationsof
theACM60,no.6:84–90.
Fan,J.H.,andT.Zhang.2020.“TheUntoldStoryofCommodityFu-
turesinChina.”JournalofFuturesMarkets40,no.4:671–706. Leippold,M.,Q.Wang,andW.Zhou.2022.“MachineLearninginthe
Market.”
Foroutan,P.,andS.Lahmiri.2024.“DeepLearningSystemsforFore- Chinese Stock Journal of Financial Economics 145, no. 2:
64–82.
| casting the | Prices | of Crude | Oil | and Precious | Metals.” |     | Financial |     |     |     |     |     |     |     |
| ----------- | ------ | -------- | --- | ------------ | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
Innovation10,no.1:111. Liu,Q.,Y.Tse,andK.Zheng.2021.“TheImpactofTradingBehavioral
Fung, H. G., Y. Tse, J. Yau, and L. Zhao. 2013. “A Leader of the World BiasesonMarketLiquidityUnderAbnormalPriceVolatility:Evidence
FromtheChineseCommodityFuturesMarkets.”FinancialReview56:
| Commodity | Futures | Markets | in the | Making? | The Case | of China's | Com- |     |     |     |     |     |     |     |
| --------- | ------- | ------- | ------ | ------- | -------- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
671–692.
modityFutures.”InternationalReviewofFinancialAnalysis27:103–114.
“Return
Gao,S.,S.Wang,Y.Wang,andQ.Zhang.2025.“ChatGPTandCom- Li, Y., Q. Liu, D. Miao, and Y. Tse. 2024. Seasonality in
CommodityFutures.”InternationalReviewofEconomics&Finance93:
modityReturn.”JournalofFuturesMarkets45,no.3:161–175.
448–462.
Göncü,A.,T.U.Kuzubaş,andB.Saltoğlu.2024.“PredictingOilPrices:
“Oil
AComparativeAnalysisofMachineLearningand ImageRecognition Lu, X., F. Ma, J. Xu, and Z. Zhang. 2022. Futures Volatility Pre-
Models.”
AlgorithmsforTrendPrediction.”FinanceResearchLetters67:105874. dictability: New Evidence Based on Machine Learning
InternationalReviewofFinancialAnalysis83:102299.
Gong,X.,K.Guan,andQ.Chen.2022.“TheRoleofTextualAnalysisin
Maas,A.L.,A.Y.Hannun,andA.Y.Ng.2013.“RectifierNonlinearities
OilFuturesPriceForecastingBasedonMachineLearningApproach.”
Models.”
JournalofFuturesMarkets42,no.10:1987–2017. Improve Neural Network Acoustic Proceedings of the
Gorton,G.,andK.G.Rouwenhorst.2006.“FactsandFantasiesAbout InternationalConferenceonMachineLearning30,no.1:3.
Marshall,B.R.,R.H.Cahan,andJ.M.Cahan.2008.“CanCommodity
CommodityFutures.”FinancialAnalystsJournal62,no.2:47–68.
|     |     |     |     |     |     |     |     | Futures Be | Profitably | Traded | With Quantitative |     | Market | Timing Strat- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | ------ | ----------------- | --- | ------ | ------------- |
Gorton,G.B.,F.Hayashi,andK.G.Rouwenhorst.2013.“TheFunda- egies?”JournalofBanking&Finance32,no.9:1810–1819.
mentalsofCommodityFuturesReturns.”ReviewofFinance17,no.1:
Medvedev,N.,andZ.Wang.2022.“MultistepForecastoftheImplied
35–105.
VolatilitySurfaceUsingDeepLearning.”JournalofFuturesMarkets42,
| Gu,S.,B.Kelly,andD.Xiu.2020.“EmpiricalAssetPricingviaMachine |     |     |     |     |     |     |     | no.4:645–667. |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
Learning.”ReviewofFinancialStudies33,no.5:2223–2273.
“Momentum
|     |     |     |     |     |     |     |     | Miffre, J., | and G. Rallis. | 2007. |     | Strategies | in  | Commodity |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | ----- | --- | ---------- | --- | --------- |
Han, Y., T. Hu, and J. Yang. 2016. “Are There Exploitable Trends in FuturesMarkets.”JournalofBanking&Finance31,no.6:1863–1886.
CommodityFuturesPrices?”JournalofBanking&Finance70:214–234.
“Revisiting
|     |     |     |     |     |     |     |     | Ming, L., | W. Song, | and M. | Dong. 2023. |     |     | Time Series |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ------ | ----------- | --- | --- | ----------- |
Han,Y.,andL.Kong.2022.TheLead‐LagRelationsintheCommodity
|     |     |     |     |     |     |     |     | Momentum | in China's | Commodity | Futures | Market: |     | Evidence on |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --------- | ------- | ------- | --- | ----------- |
Futures Returns: A Machine Learning Approach. Available at SSRN SourcesofMomentumProfits.”EconomicModelling128:106522.
3536046.
“Machine
|     |     |     |     |     |     |     |     | Mullainathan, | S., and | J. Spiess. | 2017. |     | Learning: | An Applied |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | ---------- | ----- | --- | --------- | ---------- |
Han,Y.,G.Zhou,andY.Zhu.2016.“ATrendFactor:AnyEconomic EconometricApproach.”JournalofEconomicPerspectives31,no.2:87–106.
GainsFromUsingInformationOverInvestmentHorizons?”Journalof
K.Pukthuanthong.2022.“APictureis
| FinancialEconomics122,no.2:352–375. |     |     |     |     |     |     |     | Obaid,K.,and |           |          |           |     | WorthaThou- |         |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | -------- | --------- | --- | ----------- | ------- |
|                                     |     |     |     |     |     |     |     | sand Words:  | Measuring | Investor | Sentiment | by  | Combining   | Machine |
Heide, M., B. R. Auer, and F. Schuhmacher. 2025. “Optimal Versus LearningandPhotosFromNews.”JournalofFinancialEconomics144,
| Naive Diversification |     | in  | Commodity | Futures | Markets.” | Journal | of  | no.1:273–297. |     |     |     |     |     |     |
| --------------------- | --- | --- | --------- | ------- | --------- | ------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
FuturesMarkets45:3–22.
“Agricultural
|     |     |     |     |     |     |     |     | Ouyang, H., | X. Wei, | and Q. | Wu. 2019. |     | Commodity | Fu- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ------ | --------- | --- | --------- | --- |
turesPricesPredictionviaLong‐andShort‐TermTimeSeriesNetwork.”
| Herrera,        | G. P., M. | Constantino, | B.  | M. Tabak, | H. Pistori, | J. J.       | Su, and |                                           |     |     |     |     |     |     |
| --------------- | --------- | ------------ | --- | --------- | ----------- | ----------- | ------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |
|                 |           | “Long‐Term   |     |           |             |             |         | JournalofAppliedEconomics22,no.1:468–483. |     |     |     |     |     |     |
| A. Naranpanawa. |           | 2019.        |     | Forecast  | of Energy   | Commodities |         |                                           |     |     |     |     |     |     |
PriceUsingMachineLearning.”Energy179:214–221.
Pástor,Ľ.,R.F.Stambaugh,andL.A.Taylor.2017.“DoFundsMake
ElHokayem,J.,I.Jamali,andA.Hejase.2024.“AForecastingModelfor More?”
|            |       |         |        |          |              |         |     | More When  | They Trade |     | The | Journal of | Finance | 72, no. 4: |
| ---------- | ----- | ------- | ------ | -------- | ------------ | ------- | --- | ---------- | ---------- | --- | --- | ---------- | ------- | ---------- |
|            |       |         |        |          | Indicators.” |         |     | 1483–1528. |            |     |     |            |         |            |
| Oil Prices | Using | a Large | Set of | Economic |              | Journal | of  |            |            |     |     |            |         |            |
Forecasting43,no.5:1615–1624.
Pástor,Ľ.,R.F.Stambaugh,andL.A.Taylor.2020.“FundTradeoffs.”
Hoseinzade,E.,andS.Haratizadeh.2019.“CNNpred:CNN‐BasedStock JournalofFinancialEconomics138,no.3:614–634.
Variables.”
Market Prediction Using a Diverse Set of Expert Systems “Mean
WithApplications129:273–285. Poterba, J. M., and L. H. Summers. 1988. Reversion in Stock
Prices:EvidenceandImplications.”JournalofFinancialEconomics22,
no.1:27–59.
Ioffe,S.,andC.Szegedy.2015.BatchNormalization:AcceleratingDeep
Network Training by Reducing Internal Covariate Shift, preprint, “The
|     |     |     |     |     |     |     |     | Rad, H., R. | K. Y. Low, | J. Miffre, | and R. | Faff. 2023. |     | Commodity |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ---------- | ------ | ----------- | --- | --------- |
arXiv:1502.03167. RiskPremiumandNeuralNetworks.”JournalofEmpiricalFinance74:
“Seasonality
| Jegadeesh, | N. 1991. |     | in  | Stock Price | Mean | Reversion: | Evi- | 101433. |     |     |     |     |     |     |
| ---------- | -------- | --- | --- | ----------- | ---- | ---------- | ---- | ------- | --- | --- | --- | --- | --- | --- |
denceFromtheUSandtheUK.”JournalofFinance46,no.4:1427–1444.
Ren,X.,W.Jiang,Q.Ji,andP.Zhai.2024.“SeeingisBelieving:Fore-
“Returns castingCrudeOilPriceTrendFromthePerspectiveofImages.”Journal
| Jegadeesh,      | N., and      | S. Titman. | 1993.     |        | to Buying    | Winners | and |                                 |     |     |     |     |     |     |
| --------------- | ------------ | ---------- | --------- | ------ | ------------ | ------- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- |
|                 |              |            |           |        | Efficiency.” |         |     | ofForecasting43,no.7:2809–2821. |     |     |     |     |     |     |
| Selling Losers: | Implications |            | for Stock | Market |              | Journal | of  |                                 |     |     |     |     |     |     |
Finance48,no.1:65–91.
Shen,Q.,A.C.Szakmary,andS.C.Sharma.2007.“AnExaminationof
|     |     |     |     | “(Re‐)Imag(in)ingPrice |     |     | Trends.” |     |     |     |     |     | Markets.” |     |
| --- | --- | --- | --- | ---------------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --------- | --- |
Jiang, J., B. Kelly, and D. Xiu. 2023. Momentum Strategies in Commodity Futures Journal of
JournalofFinance78,no.6:3193–3249. FuturesMarkets27,no.3:227–256.
2451

 10969934, 2025, 12, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/fut.70043 by Universita Bocconi Milano, Wiley Online Library on [14/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
AppendixA
Srivastava,N.,G.Hinton,A.Krizhevsky,I.Sutskever,andR.Salakhutdinov.
“Dropout:
| 2014. | A Simple | Way to Prevent | Neural | Networks From | Over- |     |     |     |     |     |     |     |     |
| ----- | -------- | -------------- | ------ | ------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
fitting.”JournalofMachineLearningResearch15,no.1:1929–1958. One‐DimensionalModelsasBenchmarksforReturnPrediction
|     |     |     |     |     |     | In Appendix | A,  | we use the CNN | 1D  | model | and the | LSTM model | to  |
| --- | --- | --- | --- | --- | --- | ----------- | --- | -------------- | --- | ----- | ------- | ---------- | --- |
Szymanowska,M.,F.DeRoon,T.Nijman,andR.VanDenGoorbergh.
“An Premia.” representthe1Dmodelsservingasbenchmarks,allowingustoevaluate
| 2014. | Anatomy of Commodity | Futures | Risk |     | Journal of |     |     |     |     |     |     |     |     |
| ----- | -------------------- | ------- | ---- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Finance69,no.1:453–482. theperformance ofour proposedCNN2D modelagainstwidelyused
|     |     |     |     |     |     | deep | learning approaches. |     | Specifically, | the | CNN | 1D serves | as a |
| --- | --- | --- | --- | --- | --- | ---- | -------------------- | --- | ------------- | --- | --- | --------- | ---- |
Sørensen, C. 2002. “Modeling Seasonality in Agricultural Commodity benchmark for models that capture local temporal patterns through
Futures.”JournalofFuturesMarkets22,no.5:393–426. convolutionalongthetimeaxis,whiletheLSTMservesasabenchmark
formodelsdesignedtocapturenonlinearlong‐andshort‐termdepen-
| Wang, C., | and M. Yu. 2004. | “Trading | Activity | and Price | Reversals |     |     |     |     |     |     |     |     |
| --------- | ---------------- | -------- | -------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
denciesinsequentialdata.Thiscombinationallowsustocomparethe
inFuturesMarkets.”JournalofBanking&Finance28,no.6:1337–1361.
CNN2Dnotonlyagainstmodelsthatfocusonlocalstructuresbutalso
Wang, S., and T. Zhang. 2024. “Predictability of Commodity Futures againstthosethataredesignedforlongerrangetemporaldynamics.We
Returns With Machine Learning Models.” Journal of Futures Markets conduct the same “Ix/Ry” portfolio analysis as in Table 2, and the
44,no.2:302–322. correspondingresultsarereportedinTablesA1andA2.
Wang,W.,andY.Liu.2025.“ANovelFrameworkforAgricultural
FuturesPricePredictionWithBERT‐BasedTopicIdentificationand IntheCNN1Dmodel,thedataarerepresentedasamatrixwithrows
SentimentAnalysis.”JournalofForecasting44:1969–1992. correspondingtotimeandcolumnstovariables.Convolutionalfiltersin
thissettingspanthefullwidthofthedatamatrixandslideonlyalong
time‐series
Wu, B., Z. Wang, and L. Wang. 2024. “Interpretable Corn Future Price the time dimension. The CNN 1D, as a CNN, processes
ForecastingWithMultivariateTimeSeries.”JournalofForecasting43,no.5:
|     |     |     |     |     |     | continuous | numerical | representations |     | of market | data, | such as | OHLC |
| --- | --- | --- | --- | --- | --- | ---------- | --------- | --------------- | --- | --------- | ----- | ------- | ---- |
1575–1594. timeseries,byapplyingconvolutionexclusivelyalongthetemporalaxis
(Jiangetal.2023).Thisarchitectureenablesthemodeltocapturelocal
Yang,Y.,A.Göncü,andA.A.Pantelous.2018.“MomentumandReversal temporaldependenciesandshort‐termpatternsbutlimitsitsabilityto
StrategiesinChineseCommodityFuturesMarkets.”InternationalReview extractthespatialstructuresembeddedinprice‐chartimages.Asshown
ofFinancialAnalysis60:177–196. inTableA1,althoughtheCNN1Dachievespositive“H‐L”returnsin
| TABLEA1 | | PortfolioperformanceoftheCNN1Dmodel. |     |       |     |     |     |        |     |     |     |        |     |     |
| ------- | -------------------------------------- | --- | ----- | --- | --- | --- | ------ | --- | --- | --- | ------ | --- | --- |
|         |                                        |     | I5/R5 |     |     |     | I20/R5 |     |     |     | I60/R5 |     |     |
|         |                                        | Ret |       | SR  |     | Ret |        | SR  |     | Ret |        |     | SR  |
PanelA:Short‐horizon(one‐week)portfolioperformance
| Low         |     | 4.22  |         | 0.26  |     | 3.48 |         | 0.21 |     | 3.54 |         |     | 0.23 |
| ----------- | --- | ----- | ------- | ----- | --- | ---- | ------- | ---- | --- | ---- | ------- | --- | ---- |
| 2           |     | 4.96  |         | 0.29  |     | 4.64 |         | 0.27 |     | 3.63 |         |     | 0.21 |
| High        |     | 3.74  |         | 0.22  |     | 4.75 |         | 0.27 |     | 5.72 |         |     | 0.32 |
| H‐L         |     | −0.48 |         | −0.03 |     | 1.27 |         | 0.07 |     | 2.18 |         |     | 0.13 |
| Turnover(%) |     |       | 3123.70 |       |     |      | 2267.89 |      |     |      | 2021.45 |     |      |
|             |     |       | I5/R20  |       |     |      | I20/R20 |      |     |      | I60/R20 |     |      |
|             |     | Ret   |         | SR    |     | Ret  |         | SR   |     | Ret  |         |     | SR   |
PanelB:Middle‐horizon(one‐month)portfolioperformance
| Low         |     | 4.06  |        | 0.25  |     | 3.15 |         | 0.21 |     | 1.07 |         |     | 0.07 |
| ----------- | --- | ----- | ------ | ----- | --- | ---- | ------- | ---- | --- | ---- | ------- | --- | ---- |
| 2           |     | 4.27  |        | 0.25  |     | 2.57 |         | 0.15 |     | 5.86 |         |     | 0.35 |
| High        |     | 3.73  |        | 0.22  |     | 6.76 |         | 0.38 |     | 5.58 |         |     | 0.30 |
| H‐L         |     | −0.33 |        | −0.02 |     |      |         |      |     |      |         |     |      |
|             |     |       |        |       |     | 3.61 |         | 0.20 |     | 4.51 |         |     | 0.25 |
| Turnover(%) |     |       | 726.52 |       |     |      | 700.85  |      |     |      | 614.05  |     |      |
|             |     |       | I5/R60 |       |     |      | I20/R60 |      |     |      | I60/R60 |     |      |
|             |     | Ret   |        | SR    |     | Ret  |         | SR   |     | Ret  |         |     | SR   |
PanelC:Long‐horizon(one‐quarter)portfolioperformance
| Low         |     | 5.42  |        | 0.34  |     | 3.22 |        | 0.22 |     | 2.09 |        |     | 0.14 |
| ----------- | --- | ----- | ------ | ----- | --- | ---- | ------ | ---- | --- | ---- | ------ | --- | ---- |
| 2           |     | 4.62  |        | 0.28  |     | 4.63 |        | 0.28 |     | 4.07 |        |     | 0.24 |
| High        |     | 2.96  |        | 0.16  |     | 5.23 |        | 0.26 |     | 6.84 |        |     | 0.36 |
| H‐L         |     | −2.46 |        | −0.14 |     | 2.01 |        | 0.11 |     | 4.76 |        |     | 0.27 |
| Turnover(%) |     |       | 244.39 |       |     |      | 241.80 |      |     |      | 220.37 |     |      |
Note:ThistablereportstheportfolioperformanceoftheCNN1DmodelintheUScommodityfuturesmarket.PanelsA–Cpresenttheresultsforshort‐horizon(one‐week),
medium‐horizon(one‐month),andlong‐horizon(one‐quarter)performance,respectively.“Ret”isexpressedasapercentage(%).TheCNN1Dmodelapplies
convolutionalfiltersalongasingledimension,typicallythetimeaxis,capturinglocaltemporalpatternsintime‐seriesdatawithoutconsideringspatialrelationshipsacross
variables.Themodelusesthesamehyperparametersettings(e.g.,numberoffilters,learningrate,earlystoppingcriteria,andkernelstride)asthestandardCNN2D
configuration,thoughtheoverallparametercountisreducedduetothelowerdimensionalityoftheinputdata.
| 2452 |     |     |     |     |     |     |     |     |     | JournalofFuturesMarkets,2025 |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- |

 10969934, 2025, 12, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/fut.70043 by Universita Bocconi Milano, Wiley Online Library on [14/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| TABLEA2 | | PortfolioperformanceoftheLSTMmodel. |     |       |     |     |     |     |        |     |     |     |     |        |     |
| ------- | ------------------------------------- | --- | ----- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | ------ | --- |
|         |                                       |     | I5/R5 |     |     |     |     | I20/R5 |     |     |     |     | I60/R5 |     |
|         |                                       | Ret |       |     | SR  |     | Ret |        |     | SR  |     | Ret |        | SR  |
PanelA:Short‐horizon(one‐week)portfolioperformance
| Low         |     | 3.09 |         |     | 0.12 |     | 3.61 |         |     | 0.09 |     | 4.01 |         | 0.24 |
| ----------- | --- | ---- | ------- | --- | ---- | --- | ---- | ------- | --- | ---- | --- | ---- | ------- | ---- |
| 2           |     | 6.71 |         |     | 0.39 |     | 5.74 |         |     | 0.33 |     | 3.79 |         | 0.22 |
| High        |     | 3.93 |         |     | 0.24 |     | 4.96 |         |     | 0.29 |     | 4.82 |         | 0.27 |
| H‐L         |     | 0.84 |         |     | 0.10 |     | 1.35 |         |     | 0.18 |     | 0.80 |         | 0.04 |
| Turnover(%) |     |      | 3105.14 |     |      |     |      | 1738.13 |     |      |     |      | 2381.43 |      |
|             |     |      | I5/R20  |     |      |     |      | I20/R20 |     |      |     |      | I60/R20 |      |
|             |     | Ret  |         |     | SR   |     | Ret  |         |     | SR   |     | Ret  |         | SR   |
PanelB:Middle‐horizon(one‐month)portfolioperformance
| Low         |     | 5.26  |        |     | 0.32  |     | 1.70 |         |        | 0.04 |     | 3.93 |         | 0.11 |
| ----------- | --- | ----- | ------ | --- | ----- | --- | ---- | ------- | ------ | ---- | --- | ---- | ------- | ---- |
| 2           |     | 0.65  |        |     | 0.04  |     | 5.13 |         |        | 0.30 |     | 5.76 |         | 0.28 |
| High        |     | 4.92  |        |     | 0.34  |     | 6.40 |         |        | 0.37 |     | 5.95 |         | 0.33 |
| H‐L         |     | −0.34 |        |     | −0.04 |     |      |         |        |      |     |      |         |      |
|             |     |       |        |     |       |     | 4.70 |         |        | 0.30 |     | 2.02 |         | 0.20 |
| Turnover(%) |     |       | 749.46 |     |       |     |      |         | 720.93 |      |     |      | 516.80  |      |
|             |     |       | I5/R60 |     |       |     |      | I20/R60 |        |      |     |      | I60/R60 |      |
|             |     | Ret   |        |     | SR    |     | Ret  |         |        | SR   |     | Ret  |         | SR   |
PanelC:Long‐horizon(one‐quarter)portfolioperformance
| Low         |     | 6.85  |        |     | 0.43  |     | 2.79 |     |        | 0.17 |     | 3.00 |        | 0.19 |
| ----------- | --- | ----- | ------ | --- | ----- | --- | ---- | --- | ------ | ---- | --- | ---- | ------ | ---- |
| 2           |     | 0.90  |        |     | 0.05  |     | 6.94 |     |        | 0.42 |     | 6.29 |        | 0.38 |
| High        |     | 5.40  |        |     | 0.29  |     | 3.39 |     |        | 0.18 |     | 3.87 |        | 0.21 |
| H‐L         |     | −1.45 |        |     | −0.08 |     | 0.60 |     |        | 0.03 |     | 0.88 |        | 0.05 |
| Turnover(%) |     |       | 240.30 |     |       |     |      |     | 254.36 |      |     |      | 232.87 |      |
Note:ThistablereportstheportfolioperformanceoftheLSTMmodelintheUScommodityfuturesmarket.PanelsA–Cpresentresultsforshort‐horizon(one‐week),
middle‐horizon(one‐month),andlong‐horizon(one‐quarter)performance,respectively.“Ret”isexpressedasapercentage(%).TheLSTMmodel,designedtocaptureboth
short‐andlong‐termdependenciesinsequentialdatathroughgatedmemorycells,isconfiguredwith12hiddenunitsandasinglelayer.Allothersettings,includingthe
learningrateandearlystoppingcriteria,areidenticaltothoseusedfortheCNNsmodel.
theshort‐horizonportfolios(e.g.,−0.48%withanSRof−0.03underI5/
AppendixB
| R5), its performance | deteriorates |     | over longer | horizons, | with | several |     |     |     |     |     |     |     |     |
| -------------------- | ------------ | --- | ----------- | --------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
negativeornear‐zero“H‐L”returns,suchas−0.33%(SR=–0.02)under LogisticRegressionApproximationofCNNPredictive
| I5/R20and−2.46%(SR=–0.14)underI5/R60. |     |     |     |     |     |     | Performance |     |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Inthisappendix,weemploylogisticregressiontoestimatethepredictive
In contrast, the LSTM model is a recurrent neural network specifi- performance of the CNN model using the underlying market data em-
cally designed to capture both short‐ and long‐term nonlinear bedded in the image representations. Following Jiang et al. (2023), the
dependenciesinsequentialdata.Usinggatedmemorycells,itretains logisticregressionspecificationissimilartoEquation(5)and(6),wherethe
andupdatesrelevantinformationovertime,makingitwellsuitedfor dependentvariableistheout‐of‐samplepredictiongeneratedbytheCNN
time‐series forecasting tasks (Medvedev and Wang 2022; Chen modelon5‐dayimages(codedas1ifthepredictedprobabilityexceeds0.5,
et al. 2024). However, like the CNN 1D, the LSTM operates strictly and0otherwise),andtheindependentvariablesaretheunderlying5‐day
along the time dimension and thus cannot exploit the 2D spatial marketdatarescaledtomirrortheimagerepresentations.
| patterns present | in chart‐based |     | representations. |     | As reported | in  |     |     |     |     |     |     |     |     |
| ---------------- | -------------- | --- | ---------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Table A2, the LSTM shows limited and inconsistent predictive Table B1 presents the results of logistic regressions examining the
power, with short‐horizon “H‐L” returns of only 0.84% (SR=0.10) association between image‐based forecasts, historical price and
underI5/R5,andnegativeorweaklypositive“H‐L”returnsatlonger liquidity‐relatedfactors,andfuturereturnrealizationsacrossdifferent
horizons, including −1.45% (SR=–0.08) under I5/R60 and 0.60% predictive horizons. The analysis is divided into two primary compo-
(SR=0.03)underI20/R60. nents. The first set of regressions evaluates the extent to which CNN
|     |     |     |     |     |     |     | forecasts | are | systematically | related | to lagged | price | dynamics, | trading |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------------- | ------- | --------- | ----- | --------- | ------- |
Overall, these results highlight the consistent advantage of the pro- volume,andtrendmeasures.Thesecondsetmodelstheprobabilityofa
posed CNN2Dmodel overthe1Dbenchmarks.UnliketheCNN1D positive return, incorporating CNN forecasts alongside conventional
and LSTM, which struggle to deliver stable predictive performance predictorstoassesstheirrelativecontributionstoreturnpredictability.
| across horizons, | the CNN | 2D leverages | spatial | information | in  | price‐ |     |     |     |     |     |     |     |     |
| ---------------- | ------- | ------------ | ------- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
chartimagestoachievesuperiorandmorerobustportfoliooutcomes, image‐based
|              |                      |     |              |         |     |         | The           | first set | of regressions | suggests | that             |     | predictions  | are     |
| ------------ | -------------------- | --- | ------------ | ------- | --- | ------- | ------------- | --------- | -------------- | -------- | ---------------- | --- | ------------ | ------- |
| as evidenced | by the substantially |     | higher “H‐L” | returns | and | SRs re- |               |           |                |          |                  |     |              |         |
|              |                      |     |              |         |     |         | significantly |           | influenced     | by past  | market behavior, |     | particularly | extreme |
portedinTable2.
|     |     |     |     |     |     |     | price | fluctuations. |     | Notably, prior | highs | exhibit | a strong | positive |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------------- | --- | -------------- | ----- | ------- | -------- | -------- |
2453

 10969934, 2025, 12, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/fut.70043 by Universita Bocconi Milano, Wiley Online Library on [14/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| TABLEB1 | | Logisticregressionsusingmarketdatawithimagescaling. |               |         |       |                                   |         |        |                 |        |         |
| --------- | --------------------------------------------------- | ------------- | ------- | ----- | --------------------------------- | ------- | ------ | --------------- | ------ | ------- |
|           | CNNasDep.Var.                                       |               |         |       | PositivereturnindicatorasDep.Var. |         |        |                 |        |         |
|           |                                                     |               |         | I5/R5 |                                   |         | I5/R20 |                 | I5/R60 |         |
|           | I5/R5                                               | I5/R20 I5/R60 |         |       |                                   |         |        |                 |        |         |
|           | (1)                                                 | (2) (3)       | (4)     | (5)   | (6)                               | (7)     | (8)    | (9) (10)        | (11)   | (12)    |
| CNN       |                                                     |               | 0.24*** |       | 0.23***                           | 0.55*** |        | 0.55*** 0.90*** |        | 0.89*** |
open_lag_1 0.76 −0.43 −0.59 −7.98*** −8.07*** −8.67*** −8.74*** −9.28*** −9.44***
open_lag_2 −0.51 −2.30** −1.01 −1.78 −1.75 −1.88 −1.59 −1.53 −1.39
| open_lag_3 | −0.51 | −0.77 0.17 |     | −1   | −0.96 |     | −1   | −0.86 | −1.06 | −1.06 |
| ---------- | ----- | ---------- | --- | ---- | ----- | --- | ---- | ----- | ----- | ----- |
| open_lag_4 | 1.03  | −0.51 0.83 |     | 0.64 | 0.53  |     | 0.58 | 0.72  | 0.52  | 0.42  |
open_lag_5 −1.22 −0.1 0.42 −0.21 −0.15 −0.34 −0.33 −0.3 −0.42
high_lag_1 −1.27 −0.29 −1.51 −2.57** −2.47** −3.28*** −3.23** −3.33*** −3.13**
| high_lag_2 | −0.22 | 0.88 1.26  |     | 1.04 | 1.03 |     | 1.18 | 1.09 | 1.02 | 0.78 |
| ---------- | ----- | ---------- | --- | ---- | ---- | --- | ---- | ---- | ---- | ---- |
| high_lag_3 | −1.16 | 0.45 −1.03 |     | 0.44 | 0.52 |     | 0.55 | 0.37 | 0.44 | 0.69 |
high_lag_4 0.05 0.19 1.96* 2.04* 2.05* 2.13* 2.11* 2.06* 1.69
high_lag_5 1.58* 1.16 1.15 7.62*** 7.53*** 7.82*** 7.77*** 7.64*** 7.64***
low_lag_1 −1.77* 0.23 −0.15 −3.67*** −3.57*** −3.87*** −3.90*** −4.13*** −4.23***
| low_lag_2 | 1.16 | −0.03 −1.04 |     | 0.55 | 0.46 |     | 0.63 | 0.57 | 0.44 | 0.56 |
| --------- | ---- | ----------- | --- | ---- | ---- | --- | ---- | ---- | ---- | ---- |
| low_lag_3 | 1.55 | 0.2 −1.59   |     | 1.15 | 1.05 |     | 1.05 | 1.02 | 0.92 | 1.21 |
| low_lag_4 | 0.67 | 0.19 1.5    |     | 1.01 | 1.04 |     | 1.11 | 1.13 | 1    | 0.78 |
low_lag_5 0.47 1.33 2.24** 9.84*** 9.83*** 9.87*** 9.74*** 9.85*** 9.75***
| close_lag_1 | 2.80** | 2.10* 1.71 |     | 1.25 | 1.12 |     | 0.95 | 0.65 | 0.76 | 0.54 |
| ----------- | ------ | ---------- | --- | ---- | ---- | --- | ---- | ---- | ---- | ---- |
close_lag_2 −0.03 0.81 0.36 −1.53 −1.52 −1.81 −1.88 −1.56 −1.56
close_lag_3 −0.87 −1.02 0.35 −0.27 −0.23 −0.3 −0.15 −0.09 −0.32
close_lag_4 0.26 −0.37 −2.57** −1.23 −1.25 −1.51 −1.49 −1.45 −0.98
ma_lag_1 −1.51* −0.76 −3.36* −5.03*** −4.99*** −2.23* −2.23* −0.77 −0.18
| ma_lag_2 | 1.26  | −3.71** 2.38 |     | 0.19  | 0.17  |     | −1.61 | −1.04 | −1.75 | −2.18 |
| -------- | ----- | ------------ | --- | ----- | ----- | --- | ----- | ----- | ----- | ----- |
| ma_lag_3 | −0.56 | 2.51 −4.46*  |     | 0.09  | 0.1   |     | 0.48  | 0.15  | −1.14 | −0.38 |
| ma_lag_4 | −0.87 | −1.61 3.99*  |     | −0.82 | −0.78 |     | −0.96 | −0.75 | 2.74  | 1.97  |
| ma_lag_5 | −1.13 | 1.8 −1.11    |     | 0.23  | 0.32  |     | 1.1   | 0.86  | −1.01 | −0.73 |
volume_lag_1 −0.07 0.05 0.07 −0.17*** −0.17*** −0.17*** −0.18*** −0.17*** −0.19***
volume_lag_2 0.15** −0.03 −0.1 −0.16** −0.16** −0.15** −0.15** −0.15** −0.14*
volume_lag_3 −0.1 −0.02 0.09 −0.1 −0.09 −0.1 −0.1 −0.11 −0.14*
volume_lag_4 0.08 0 −0.01 0.16** 0.16** 0.16** 0.16** 0.16** 0.17**
volume_lag_5 −0.04 0.02 −0.03 0.23*** 0.23*** 0.24*** 0.24*** 0.24*** 0.26***
| McFaddenR2 | −0.17 | −0.17 0.17 |     |     |     |     |     |     |     |     |
| ---------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
OOSMcFaddenR2 −0.1 2.57 2.37 −1.12 2.66 1.46 −2.91 2.65 −0.26
Note:Thistablepresentstheresultsoflogisticregressionsonout‐of‐sampleCNNforecastsandrealizedfuturereturnindicatorsbasedondailypriceandvolumedata.
PanelregressionsareestimatedduringthetestsampleusingCNNmodelstrainedinthetrainingsample.Tocomparepredictiveperformance,wereportout‐of‐sample
McFaddenR2values,whichassessthecross‐entropylossofthetrainedmodelagainstabenchmarkmodelthatusesthefuture‐levelin‐samplemeanasthepredictor.Since
ma_lag_1isdefinedasthesimpleaverageofclose_lag_1toclose_lag_5,weexcludeclose_lag_5fromtheregressiontoavoidmulticollinearity.***,**,and*denote
significanceatthe1%,5%,and10%levels,respectively,basedonNewey–Weststandarderrors.McFaddenR2valuesarecomputedusingtestsampledata.
relationshipwithCNNforecasts,asseeninhigh_lag_5(1.58,significant thatCNNmodelsadjusttodeviationsfromhistoricalsmoothedtrends
atthe10%levelinI5/R5)andhigh_lag_4(1.96,significantatthe10% rather than relying solely on absolute price levels. Although recent
level in I5/R60), indicating that CNN models capture short‐term closing prices (close_lag_1=2.80, significant at the 5% level in I5/R5)
momentumeffects,wherepastpeakssignalupwardpersistence.Con- contributetoshort‐termforecasts,theirimpactdiminishesoverlonger
versely,low_lag_1(−1.77,significantatthe10%levelinI5/R5)suggests horizons,suggestingthatCNNmodelsprioritizemorestructuralmarket
| that CNN forecasts | also incorporate | mean‐reversion   | tendencies, | with      | signalsovertime. |     |     |     |     |     |
| ------------------ | ---------------- | ---------------- | ----------- | --------- | ---------------- | --- | --- | --- | --- | --- |
| previous downward  | price movements  | being associated | with        | lower ex- |                  |     |     |     |     |     |
pectedfuturereturns.Additionally,themovingaveragelag(ma_lag_1) Thesecondsetofregressions,whichmodelstheprobabilityofapositive
showsasignificantnegativerelationshipwithCNNforecasts(−1.51in return, underscores the predictive strength of image‐based forecasts.
I5/R5and−3.36inI5/R60,bothatthe10%level),reinforcingthenotion Across all horizons, CNN coefficients remain highly significant,
| 2454 |     |     |     |     |     |     |     | JournalofFuturesMarkets,2025 |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- |

 10969934, 2025, 12, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/fut.70043 by Universita Bocconi Milano, Wiley Online Library on [14/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
confirming that CNN models extract meaningful predictive signals TABLEC1 | Returncorrelationsbetweencommodityfuturesin
beyond traditional financial indicators. The magnitude of the CNN theUSandChinesemarkets.
| coefficient      | increases as the | forecast horizon   | extends | (0.24 in | I5/R5 to |        |           |           |             |
| ---------------- | ---------------- | ------------------ | ------- | -------- | -------- | ------ | --------- | --------- | ----------- |
|                  |                  |                    |         |          | return‐  | Sector | Commodity | Startdate | Correlation |
| 0.90 in I5/R60), | suggesting       | that deep learning | models  | capture  |          |        |           |           |             |
1999‐01
relevant patterns that persist over longer time frames. Additionally, Metals Aluminum 0.259185
prioropeningpricesexhibitaconsistentlynegativeandhighlysignifi- 2015‐04
|                   |                | (−7.98  | −9.44, |        |        |     | Nickel |         | 0.410403 |
| ----------------- | -------------- | ------- | ------ | ------ | ------ | --- | ------ | ------- | -------- |
| cant relationship | with future    | returns | to     | all at | the 1% |     |        |         |          |
|                   | mean‐reversion |         |        |        |        |     |        | 2011‐04 |          |
level), reinforcing a effect where higher past opening Lead 0.288524
prices reduce the likelihood of future gains. Meanwhile, prior price 2007‐04
|              |                       |      |               |               |     |     | Zinc |     | 0.381278 |
| ------------ | --------------------- | ---- | ------------- | ------------- | --- | --- | ---- | --- | -------- |
| highs remain | positively associated | with | future return | probabilities |     |     |      |     |          |
2008‐01
(high_lag_5=7.64,significantatthe1%levelinI5/R60),consistentwith Gold 0.283164
short‐termmomentumeffects.Incontrast,priorlowprices(low_lag_1
2012‐05
tolow_lag_5)showsignificantnegativecoefficients(−3.67to−4.23,all Silver 0.311421
|     |     |     | mean‐reversion |     |     |     |     | 1999‐01 |     |
| --- | --- | --- | -------------- | --- | --- | --- | --- | ------- | --- |
at the 1% level), further supporting the role of ten- Copper 0.290257
| denciesinreturndynamics. |     |     |     |     |     |             |          | 1999‐01 |          |
| ------------------------ | --- | --- | --- | --- | --- | ----------- | -------- | ------- | -------- |
|                          |     |     |     |     |     | Agriculture | Soybeans |         | 0.114598 |
2004‐09
Theregressionresultsalsohighlighttheinfluenceoftradingvolumeon Corn 0.124255
returnpredictability,withvolume_lag_1tovolume_lag_5beingmostly 2013‐01 −0.009913
|          |                        | (−0.17 | −0.19, |           |         |     | Wheat |     |     |
| -------- | ---------------------- | ------ | ------ | --------- | ------- | --- | ----- | --- | --- |
| negative | and highly significant | to     | all    | at the 1% | level), |     |       |     |     |
1999‐01
suggestingthathigherpasttradingactivityreducestheprobabilityofa KansasCityHRW 0.028520
|                  |              |             | liquidity‐driven |       |         |     | Wheata |     |     |
| ---------------- | ------------ | ----------- | ---------------- | ----- | ------- | --- | ------ | --- | --- |
| positive return. | This finding | aligns with |                  | price | adjust- |     |        |     |     |
ments,wheresurgesintradingvolumecorrespondtopricecorrections 2004‐06
|     |     |     |     |     |     |     | Cotton |     | 0.273992 |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | -------- |
ratherthansustaineddirectionaltrends.
2006‐01
|     |     |     |     |     |     |     | Sugar |     | 0.115446 |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | -------- |
Toevaluate model fit, Table B1 reports McFadden R2 and out‐of‐sample Low‐Sulphur 2020‐07
|     |     |     |     |     |     | Energy |     |     | 0.283205 |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | -------- |
(OOS)McFaddenR2values.WhileMcFaddenR2valuesremainlowacross
Gasoil
| all specifications | (−0.17 to | 2.66), consistent | with the | inherent | noise in |     |     |     |     |
| ------------------ | --------- | ----------------- | -------- | -------- | -------- | --- | --- | --- | --- |
2021‐01
financial return predictions, the OOS McFadden R2 values indicate that Livestock LeanHogs 0.077227
| CNN models | improve predictive | performance | relative | to traditional |     |     |     |     |     |
| ---------- | ------------------ | ----------- | -------- | -------------- | --- | --- | --- | --- | --- |
Note:Thistablepresentsthe15comparablecommodityfuturesandreportsthe
| benchmarks | (2.37 in I5/R5, | 1.46 in I5/R20). | These findings | suggest | that |     |     |     |     |
| ---------- | --------------- | ---------------- | -------------- | ------- | ---- | --- | --- | --- | --- |
returncorrelationsbetweentheircounterpartsintheUSandChinesemarkets,
althoughCNNmodelsdonotfullyexplainreturnvariations,theyprovide
adjustedforcontractmisalignment.
incrementalpredictivepowerthatbecomesincreasinglyrelevantatlonger aForKansasCityHRWWheat,weselectedhardwheatfromtheChinesefutures
timescales.Inparticular,thelogisticregressionanalysisrevealsthatCNN marketasthecomparablecontract,asthetwoarehighlysimilarinbothtypeand
| modelsconsistentlyintegrateextremepricemovements,trenddeviations, |     |     |     |     |     | characteristics. |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- |
andliquidityconditionsintoreturnpredictions.
AppendixC
ReplicationofTransferLearningUsingMatchedCommodity
Futures
InthisAppendix,wereplicatetheresultsoftransferlearningusing15
| Chinese | commodity futures | contracts that | most | closely match | the |     |     |     |     |
| ------- | ----------------- | -------------- | ---- | ------------- | --- | --- | --- | --- | --- |
productspecificationsoftheircorrespondingUScounterparts.
2455

 10969934, 2025, 12, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/fut.70043 by Universita Bocconi Milano, Wiley Online Library on [14/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
C–AslenaP.1CelbaTsaserutufytidommocemasehthtiwtekramserutufytidommocesenihCehtniseigetartsrehtoedisgnolaledomNNCehtfoecnamrofrepoiloftropelicretelpmas‐fo‐tuodezilaunnaehtstneserpelbatsihT:etoN
|     |     | 61.0− | 51.0− 42.0 | 52.0 |     | 81.0 | 21.0 72.0− | 82.0− |     | 51.0 | 40.0 60.0 | 40.0− |
| --- | --- | ----- | ---------- | ---- | --- | ---- | ---------- | ----- | --- | ---- | --------- | ----- |
RS RS RS desab‐egamiowterapmocew,)3202(.lategnaiJgniwolloF.)%(egatnecrepasadesserpxesi”teR“.ylevitcepser,ecnamrofrep)retrauq‐eno(noziroh‐gnoldna,)htnom‐eno(noziroh‐elddim,)keew‐eno(noziroh‐trohsotdnopserroc
|     | 5R/06I |     |     |     | 02R/06I |     |     |     | 06R/06I |     |     |     |
| --- | ------ | --- | --- | --- | ------- | --- | --- | --- | ------- | --- | --- | --- |
teR 93.1− 63.1− 72.2 66.3 teR 57.1 61.1 40.3− 97.4− 12.1 73.0 36.0 85.0−
teR
|     | niarteR–refsnarT |      | 91.0− | 22.0− | niarteR–refsnarT |      | 11.0− |      | niarteR–refsnarT |      |            |      |
| --- | ---------------- | ---- | ----- | ----- | ---------------- | ---- | ----- | ---- | ---------------- | ---- | ---------- | ---- |
|     | RS               | 61.0 | 10.0  |       | RS               | 60.0 | 60.0  | 10.0 |                  | 51.0 | 11.0− 22.0 | 50.0 |
RS
02R/02I
|     | 5R/02I |      |             |       |        |       |           |      | 06R/02I |      |            |      |
| --- | ------ | ---- | ----------- | ----- | ------ | ----- | --------- | ---- | ------- | ---- | ---------- | ---- |
|     |        | 83.1 | 11.0 6.1−   | 89.2− |        |       | 99.0−     |      |         |      |            |      |
|     | teR    |      |             |       | teR    | 54.0  | 26.0      | 71.0 | teR     | 43.1 | 1.1− 40.2  | 17.0 |
|     |        | 97.0 | 86.0− 30.0− | 74.0− |        | 42.0− |           |      |         | 51.0 | 81.0− 92.0 | 11.0 |
|     | RS     |      |             |       | RS     |       | 71.0 51.0 | 32.0 | RS      |      |            |      |
|     | 5R/5I  |      |             |       | 02R/5I |       |           |      | 06R/5I  |      |            |      |
.gniniartertuohtiwatadSUnodeniartsledomNNCsrefsnartyltceridtahtrehtonadnaatadserutufytidommocesenihCgnisuledomNNChcaesniartertahteno:seigetarts
|     |     |      | 79.5− 42.0− | 69.6− |     |       |           |      |     |      |            |     |
| --- | --- | ---- | ----------- | ----- | --- | ----- | --------- | ---- | --- | ---- | ---------- | --- |
|     | teR | 27.6 |             |       | teR | 86.2− | 66.1 56.1 | 33.4 | teR | 22.1 | 75.1− 26.2 |     |
4.1
|     | RS     | 80.0 | 63.0 74.0 | 24.0    |         |      |          |        |         |      |           |        |
| --- | ------ | ---- | --------- | ------- | ------- | ---- | -------- | ------ | ------- | ---- | --------- | ------ |
|     |        |      |           |         | RS      | 23.0 | 72.0 3.0 | 40.0   | RS      | 32.0 | 52.0 94.0 | 43.0   |
|     | 5R/06I |      |           | 24.3681 | 02R/06I |      |          |        |         |      |           |        |
|     |        |      |           |         |         |      |          | 73.244 | 06R/06I |      |           | 54.841 |
86.0 81.3 82.5
|     | teR            |      |           | 6.4     | teR     | 68.2 | 34.2 53.3 | 94.0  |         |      |          |        |
| --- | -------------- | ---- | --------- | ------- | ------- | ---- | --------- | ----- | ------- | ---- | -------- | ------ |
|     |                |      |           |         |         |      |           |       | teR     | 89.1 | 2.2 20.6 | 40.4   |
|     | refsnarttceriD |      |           | 40.0−   |         |      |           |       |         |      |          |        |
|     | RS             | 33.0 | 52.0 22.0 |         | RS      | 42.0 | 42.0 53.0 | 61.0  |         | 62.0 | 22.0     | 22.0   |
|     |                |      |           |         |         |      |           |       | RS      |      | 4.0      |        |
|     | 5R/02I         |      |           | 82.5491 |         |      |           |       |         |      |          |        |
|     |                |      |           |         | 02R/02I |      |           |       | 06R/02I |      |          |        |
|     |                |      |           |         |         |      |           | 9.144 |         |      |          | 97.841 |
teR 50.3 31.2 85.2 74.0− teR 41.2 31.2 89.3 48.1 teR 62.2 68.1 47.4 84.2
refsnarttceriD
| .tekramserutufytidommocesenihCniledomNNCehtfoecnamrofrepoiloftroP |     |      |           |      |     |      |           |      | refsnarttceriD |      |           |     |
| ----------------------------------------------------------------- | --- | ---- | --------- | ---- | --- | ---- | --------- | ---- | -------------- | ---- | --------- | --- |
|                                                                   |     |      |           |      |     | 41.0 | 15.0 32.0 | 11.0 |                |      |           |     |
|                                                                   |     | 54.0 | 40.0 63.0 | 20.0 | RS  |      |           |      |                | 62.0 | 72.0 63.0 |     |
|                                                                   | RS  |      |           |      |     |      |           |      | RS             |      |           | 2.0 |
38.0991
5R/5I
|     |        |      |           |         | 02R/5I  |     |           | 99.954 |         |      |           |        |
| --- | ------ | ---- | --------- | ------- | ------- | --- | --------- | ------ | ------- | ---- | --------- | ------ |
|     |        |      |           |         |         |     |           |        | 06R/5I  |      |           | 80.551 |
|     |        |      |           |         | teR     |     | 45.4 46.2 | 43.1   |         |      |           |        |
|     | teR    | 30.4 | 83.0 22.4 | 2.0     |         | 3.1 |           |        | teR     | 41.2 | 13.2 55.4 | 14.2   |
|     |        |      |           |         |         |     | 91.0 64.0 | 33.0   |         |      |           |        |
|     |        | 81.0 | 74.0 33.0 |         | RS      | 2.0 |           |        |         |      |           |        |
|     | RS     |      |           | 2.0     | 02R/06I |     |           |        | RS      | 41.0 | 52.0 74.0 | 83.0   |
|     |        |      |           | 56.6281 |         |     |           | 78.464 |         |      |           |        |
|     | 5R/06I |      |           |         |         |     |           |        | 06R/06I |      |           | 48.241 |
ecnamrofrepoiloftrop)htnom‐eno(noziroh‐elddiM:BlenaP
|     |                |                                                        |           |         | teR     |      | 66.1 63.5 | 76.3   |                 | ecnamrofrepoiloftrop)retrauq‐eno(noziroh‐gnoL:ClenaP |          |      |
| --- | -------------- | ------------------------------------------------------ | --------- | ------- | ------- | ---- | --------- | ------ | --------------- | ---------------------------------------------------- | -------- | ---- |
|     | teR            | ecnamrofrepoiloftrop)keew‐eno(noziroh‐trohS:AlenaP 6.1 | 80.4 77.3 | 71.2    |         | 7.1  |           |        |                 |                                                      |          |      |
|     |                |                                                        |           |         |         |      |           |        | teR             | 81.1                                                 | 69.1 6.5 | 34.4 |
|     |                | 42.0                                                   | 42.0 23.0 | 41.0    | RS      | 22.0 | 43.0 3.0  | 51.0   |                 |                                                      |          |      |
|     | RS             |                                                        |           |         |         |      |           |        |                 | 71.0                                                 |          | 91.0 |
|     |                |                                                        |           | 11.9391 | 02R/02I |      |           | 39.274 | RS              |                                                      | 3.0 3.0  |      |
|     | niarteR 5R/02I |                                                        |           |         | niarteR |      |           |        | niarteR 06R/02I |                                                      |          |      |
82.261
|     | teR | 31.2 | 60.2 46.3 | 5.1 | teR | 58.1 | 87.2 75.3 | 27.1 |     |      |      |      |
| --- | --- | ---- | --------- | --- | --- | ---- | --------- | ---- | --- | ---- | ---- | ---- |
|     |     |      |           |     |     |      |           |      | teR | 73.1 | 83.3 | 10.2 |
6.2
|     |     | 50.0− |          |      |     |      |           | 31.0− |     |      |           |      |
| --- | --- | ----- | -------- | ---- | --- | ---- | --------- | ----- | --- | ---- | --------- | ---- |
|     | RS  |       | 94.0 4.0 | 34.0 | RS  | 53.0 | 93.0 31.0 |       |     |      |           |      |
|     |     |       |          |      |     |      |           |       |     | 51.0 | 83.0 52.0 | 31.0 |
RS
|     | 5R/5I |     |     | 82.3302 | 02R/5I |     |     | 29.584 | 06R/5I |     |     |     |
| --- | ----- | --- | --- | ------- | ------ | --- | --- | ------ | ------ | --- | --- | --- |
13.261
|     |     | 34.0− |     |     |     |     |     | 35.1− |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
teR 43.4 83.4 28.4 teR 80.3 44.3 55.1 teR 33.1 43.3 18.2 84.1
| |   |     |     |     | )%(revonruT |     |     |     | )%(revonruT |     |     |     | )%(revonruT |
| --- | --- | --- | --- | ----------- | --- | --- | --- | ----------- | --- | --- | --- | ----------- |
2CELBAT
|      |     |     | hgiH |     |     |     | hgiH |     |     |     | hgiH |                              |
| ---- | --- | --- | ---- | --- | --- | --- | ---- | --- | --- | --- | ---- | ---------------------------- |
|      |     | woL |      | L‐H |     | woL |      | L‐H |     | woL |      | L‐H                          |
|      |     |     | 2    |     |     |     | 2    |     |     |     | 2    |                              |
| 2456 |     |     |      |     |     |     |      |     |     |     |      | JournalofFuturesMarkets,2025 |