FinancialMarketsandPortfolioManagement(2021)35:533–553
https://doi.org/10.1007/s11408-021-00385-5
Havetrend-followingsignalsincommodityfuturesmarkets
becomelessreliableinrecentyears?
Benjamin R. Auer1,2,3
Accepted:24February2021/Publishedonline:15April2021
©SwissSocietyforFinancialMarketResearch2021
Abstract
Varioustrend-followingtradingruleshavebeenshowntobevaluableforpredicting
marketdirectionsandthustheformulationofinvestmentstrategies.However,recent
equitymarketresearchhasprovidedstrikingevidencethatthepredictivepowerofsuch
rules appears to diminish over time due to increased investor attention and lowered
arbitragebarriers.Giventhattrend-followingrulesarealsoverysuccessfulandhave
been widely used in futures markets, we analyze whether a similar effect can be
observedforcommodityfuturescontracts.Usingatrendregressionapproachbased
ontime-varyingsuccessratios,wedetectsignificantlyhigherpredictiveaccuracyfor
cross-sectionalthanfortime-seriesstrategies.Inaddition,withtheexceptionofafew
commodities,wefindnosignificanttrendingbehaviorintradingrulereliability.These
results,whicharerobustinavarietyofsettings,indicatestrongmomentumstabilityin
futuresmarketsandjustifytheapplicationofthisclassoftradingrulesincommodity
futuresinvesting.
Keywords Trend-followingrules·Movingaverages·Momentum·Trends·
Commodityfutures
JELClassification G10·G17·C10
B
BenjaminR.Auer
auer@b-tu.de
1 ChairofFinance,BrandenburgUniversityofTechnologyCottbus-Senftenberg,
Erich-Weinert-Str.1,03046Cottbus,Germany
2 DepartmentofFinance,UniversityofLeipzig,GrimmaischeStr.12,04109Leipzig,Germany
3 ResearchNetworkAreaMacro,MoneyandInternationalFinance,CESifoMunich,Schackstr.4,
80539Munich,Germany
123

534 B.R.Auer
1 Introduction
Trend-followingtradingrulesarestrategieswhereonebetsthatpastassetperformance
will continue into the near future. Such strategies can be implemented in the cross-
sectionalandthetime-seriesdimensions(seeSzakmaryetal.2010).Cross-sectional
momentuminvolvestakinglongpositionsinassetsthatperformedrelativelywell(past
winners) and short positions in assets that performed relatively poorly (past losers).
Thisapproach,datingbacktoJegadeeshandTitman(1993, 2001),hasbeenshown
toearnsignificantabnormalreturnsinawidevarietyofmarkets(seeSwinkels2004;
FamaandFrench2012)andisoftenconsideredtobethemostimportantcapitalmarket
effectdiscoveredsofar(seeFamaandFrench2008).Time-seriesmomentumcanbe
motivatedbythetechnicaltradingrulesofBrocketal.(1992),wherethecrossingof
movingaveragesindicateswhetheralong(short)positionshouldbeenteredtobenefit
fromaninitiatedupward(downward)trend.1Ratherthanlookingattherelativereturns
ofseveralassetsinthecrosssection,movingaveragesfocusonthehistoryofasingle
asset and also contain valuable investment information (see Kavajecz and Odders-
White2004;Fifieldetal.2008).2
Unfortunately, studies on trend-following strategies in equity markets are often
criticized on the grounds that their profits may be illusory (see Foltice and Langer
2015). For example, Korajczyk and Sadka (2004) argue that, after direct and indi-
rect transaction costs, cross-sectional momentum strategies would not have yielded
abnormalreturnspriortothedecimalizationofstockpricequotes.Thesedifficulties
areexacerbatedbyLesmondetal.(2004)showingthatmomentumreturnsaremainly
generatedbyreturncontinuationamongpoorlyperformingstocks.Sellingsuchstocks
short,asrequiredbyamomentumstrategy,couldprovedifficultduetotheuptickrule,
theinabilitytogainaccesstoshortsaleproceedsandthegeneraldifficultyassociated
with borrowing shares of small, illiquid stocks. Similar issues have been raised by
BajgrowiczandScaillet(2012)andTaylor(2014),highlightingthattheperformance
oftypicaltrend-basedtechnicaltradingrulesisoffsetbytheintroductionoflowtrans-
actioncosts,cruciallyreliesontheabilityofinvestorstoshort-sellstocksandappears
tobeconfinedtoparticularperiods.
Partlyasaresultofthesefrictions,attentionhasrecentlyshiftedtotheexamination
of trend-following strategies in commodity futures markets, where, as discussed by
Shenetal.(2007)andMarshalletal.(2008),nearbycontractsforstandardcommodi-
tiesaretypicallyveryliquid,cheaptotrade,easiertoshortandallowmorerealistic
portfoliosizesthantypicalacademicmomentumstockportfolioscontaininghundreds
or thousands of stocks.3 Shen et al. (2007) and Miffre and Rallis (2007) show that
cross-sectional momentum strategies in commodity futures earn impressive returns
thataretoolargetobesubsumedbythelowtransactioncostsprevailinginthesemar-
1 Moskowitzetal.(2012)alternativelypredicttime-seriescontinuationandreversalviaregressionsof(a)
scaledreturnsonpastscaledreturnsand(b)scaledreturnsonpastreturnsigns.
2 Time-seriesmomentumisatimingstrategy,whereascross-sectionalmomentumisaselectionstrategy.
3 Furthermore,futurescontracts(andfutures-basedmomentumportfolios)areexcellentdiversifiersand
inflationhedges,especiallywhentheyareactivelymanaged(seeGortonandRouwenhorst2006;Erband
Harvey2006;MiffreandRallis2007;MiffreandFernandez-Perez2015).
123

Havetrend-followingsignalsincommodityfuturesmarkets… 535
kets.4 Inthelatterstudyfrom1979to2004,tacticalallocationincommodityfutures
marketshasgeneratedsignificantlypositiveannualreturnsofabout10%,whereasan
equallyweightedportfolioofcommodityfutureslosesabout3%peryear.Szakmary
etal.(2010)andClareetal.(2014)providesimilarevidenceforvariousparameteri-
zationsofdualmovingaverage(crossoverandchannel)strategiesafterdatamining
adjustmentsandtransactioncosts.Finally,theresultsofFuertesetal.(2010, 2015),de
Grootetal.(2014)andBianchietal.(2015a)highlightthattrend-followingstrategies
can even be enhanced by combining them with other selection variables like term
structuresignals,reversalmeasuresoridiosyncraticvolatilities.5
While this performance is quite impressive, recent stock market research doubts
thatthepredictivepoweroftrend-followingtradingrulescanbeconsideredconsistent
overtime.Severalauthorshaveprovidedstrikingevidencethatmanyvariableswhich
havebeenshowntobegoodpredictorsoffuturestockreturnstendtolosethiscapa-
bilityovertime.Forexample,Chordiaetal.(2014)highlightthattherecentregime
of reduced transaction costs, increased trading activity and thus higher market liq-
uidityisassociatedwithanattenuationofadozenprominentequityreturnstrategies
(including momentum and reversal) due to increased arbitrage. Similarly, McLean
and Pontiff (2016) and Jacobs and Müller (2020) show that the out-of-sample and
post-publicationpredictivepowerofabout100traditionalforecastingvariables(again
including momentum) is significantly lower than the in-sample results presented in
earlierstudies.Theyconcludethatthisfindingisrelatedtodataminingeffectsandthe
factthatinvestorstendtoadjusttheirtradingbehaviorbasedonwhattheylearnfrom
academic publications. As summarized by Park and Irwin (2007) and supported by
Strobel and Auer (2018), with similar explanations of data mining or adaptive mar-
kets,thepredictivepoweroftechnicaltradingrulesinequitymarketsalsoappearsto
weakenovertime.
This brings us directly to the question of whether such tendencies also arise in
commodityfuturesmarkets.Sofar,thereisonlylimitedevidenceonpotentialtime-
varyingpredictivepoweroftrend-followingtradingrulesinthesemarkets,eventhough
mutualfundinvestmentsandcomputerizedtradehavebeencontinuouslyincreasing
hereaswell(seeIrwinandYoshimaru1999;HongandYogo2012).Somesubsample
robustnesschecksperformedinpreviousstudiessuggestthattheforecastingaccuracy
may change over time. For example, Park and Irwin (2005) and Szakmary et al.
(2010) show that the returns of various trend-following strategies are lower in the
mostrecentsubperiodsoftheirstudies.Furthermore,Narayanetal.(2015)highlight
lowerreturnsintheperiodcoveringthefinancialcrisisof2007.Unfortunately,such
examplesdonotallowthedeductionofgeneraltendencies.Thisiswhywestepinto
thepictureandsystematicallystudythepredictivepoweroftrend-followingtrading
rulesincommodityfuturesmarketsovertime.
4 Transactioncostsinfuturesmarketsrangefrom0.0004to0.033%(seeFlemingetal.1996;Lockeand
Venkatesch1997),whichismuchlessthantheconservative0.5%estimateofJegadeeshandTitman(1993)
orthemorerealistic2.3%estimateofLesmondetal.(2004)fortheequitymarket.
5 Foranexcellentreviewofadditionaltechniquestostrengthentraditionalmomentumsignals,seeMiffre
(2016).AlsonotethatFuertesetal.(2015)introduceaveryintuitivemethodofformingbivariateand
trivariateportfolios(viacombinedrankingscores)whichmightsetanimportantstandardforfutureresearch.
123

536 B.R.Auer
Within a sample of 24 commodity futures indices covering almost 50 years of
data,weimplementseveralspecificationsofcross-sectionalandtime-seriesmomen-
tumrules,whichpreviousstudieshavelabeledprofitable,anddocumenttheirtrading
signals.Inafirstcontribution,weevaluatetheirpredictivepowerbycalculatingapop-
ular metric of forecasting accuracy: the success ratio h, which gives the percentage
ofcorrectsignals(seeMorana2001;Wangetal.2004;Katusiimeetal.2015).This
ratioisimportantbecausepreviousstudiesdonotreportthesignalreliabilitybehind
the monetary value of the strategies. Our more detailed analysis can reveal whether
thestrategiesoftenforeseerelativecommoditypositionsandmarketdirectionortheir
returnsaremainlygeneratedbyonlyafewcorrectsignals.Inasecondcontribution,
we investigate the evolution of predictive power over time by implementing a trend
regression approach similar to Olson (2004), Chordia et al. (2014) and Strobel and
Auer (2018). If we found downward trends in predictive power, this could be inter-
pretedasevidenceofadaptivemarketswhereinvestorsreacttotheprevioussuccess
oftradingrulessuchthat—amplifiedbytheadditionaltrendofincreasingmarketliq-
uidityandalgorithmictradingactivity(seeHendershottetal.2011;HongandYogo
2012)—itisnowmoredifficulttopredictbasedontheserulesthanitwasinthepast.In
contrast,insignificanttrendingbehaviororsignificantlypositivetrendswouldindicate
thatfutureperformanceislikelytobesimilartothepastorevenhigher,respectively.
Theremainderofourarticleisorganizedasfollows.Section2offersabriefdescrip-
tionofourdataset.Section3discussesourmomentumspecificationsandourtrend
regressionsetup.Section4containsourmainresultsandtheoutcomesofsomerobust-
nesschecks.Section5concludesandoutlinesdirectionsforfutureresearch.
2 Data
ForouranalysisfromJanuary1970toDecember2019,weuseaselectionofcommod-
ityfutureswhichguaranteeshighliquidityandinvestability.Specifically,wefollow
ErbandHarvey(2006),Bianchietal.(2015a,b, 2016)andZaremba(2016)bycon-
centrating on the 24 commodities listed in the Standard & Poors Goldman Sachs
CommodityIndex(S&PGSCI):sixenergyproducts(Brentcrudeoil,WTIcrudeoil,
gasoil,heatingoil,naturalgasandunleadedgasoline),twopreciousmetals(goldand
silver),fiveindustrialmetals(aluminum,copper,lead,nickelandzinc),eightagricul-
turalproducts(cocoa,coffee,corn,cotton,soybeans,sugar,ChicagowheatandKansas
wheat)andthreelivestockproducts(feedercattle,leanhogsandlivecattle).Foreach
commodity,thereexistsadailytotalreturnindexwhichrepresentsaninvestmentin
fullycollateralizednearbyfuturesandthuscanbeconsideredausefulrepresentation
ofcommodityreturnsactuallyavailabletoinvestors.Weobtaintheindexdatafrom
ThomsonReutersDatastream.6
Ineachindex,futurescontractsarerolledforwardatthebeginningoftheirexpiration
months,alwayskeepingtheinvestmentinnearbyfutures.Table1illustratesthatmany
commodities (e.g., in the energy and industrial metals sectors) have liquid futures
6 Becausethepropertiesofthecorrespondingreturnshavebeenextensivelydocumented(see,forexample,
Auer2015;Zhangetal.2018),weomitdescriptivestatisticsillustratingnon-normalityandserialcorrelation.
However,theyareavailableuponrequest.
123

Havetrend-followingsignalsincommodityfuturesmarkets… 537
contractsthatexpireeverymonthandarethusrolledforwardeverymonth.Incontrast,
othercommodities(e.g.,agriculturalandlivestockproducts)haveonlyafewcontract
monthseachyearthattradewithsufficientliquidity.Thesecommodities,withfutures
that expire less frequently, are rolled forward less frequently than every month. As
specified in S&P Dow Jones Indices (2016), an expiring futures contract is rolled
over to a contract further from expiration at a rate of 20% per day for the five days
of the roll period (i.e., from the fifth to the ninth business day of a month).7 Until
justbeforetheendofthefifthbusinessday,weareinvestedintheexpiringcontract.
At the end of the fifth day, the holdings are adjusted so that 20% new contracts are
heldand80%remainintheexpiringcontract.Therollprocesscontinuesonthesixth,
seventhandeighthbusinessdayswithrelativeweightsoftheoldtothenewcontract
of60%/40%,40%/60%and20%/80%.Attheendoftheninthbusinessday,theroll
iscompletedwithapositionof100%inthenewcontract.Thiskindofadjustmentis
similartotheapproachofKho(1996)whicheliminatesanypricegapateachjointpoint
of two successive contracts. Otherwise time-series momentum rules could generate
spurioussignals.Furthermore,incontrasttoanimmediaterollover,thesmoothingof
therolloverensureslowerimpactofbigfinancialinvestorsonpriceswhentheysell
beforeexpiration.
Finally,notethat,eventhoughnotallcommodityfutureshavedataovertheentire
sampleperiod,ouranalysiscanbeperformedwithoutobstacles.Thisisbecause,con-
sistentwithactualinvestorbehavior,weincludeonlythecommoditieswithavailable
datawhenperiodicallyderivingthecommodityrankingsforthecross-sectionalstrate-
gies.Similarly,thetime-seriesstrategiesfortheindividualcommoditiessimplystart
whenthereissufficientdatafortheirimplementation.
3 Methodology
3.1 Trend-followingrules
Cross-sectionalmomentumCross-sectionalmomentumstrategiesaretypicallyimple-
mentedbybuyingassetswithstrongpastperformanceandsellingassetswithweak
pastperformance,wherecumulativereturnshavebecomethestandardmeasureforpast
performance(seeYao2012).Whenspecifyingamomentumstrategy,itisimportant
toadequatelysetthe‘evaluationperiod’(thetimeperiodinwhichpastperformance
ismeasured)andthe‘holdingperiod’(thetimeperiodinwhichlongandshortposi-
tions are held until a new evaluation of winners and losers is performed). While, in
equitymarkets,theevaluationperiodtypicallycoversthepast12monthswithoutthe
mostrecentmonth—becauseashort-termreversaleffect(pastwinners(losers)tend
to become future losers (winners)) exists when using only the performance of the
mostrecentmonth—andtheholdingperiodisusuallyonemonth(seeChordiaetal.
2014),settingsinfuturesmarketsareslightlydifferent.Here,researcherstypicallyuse
evaluation periods covering the most recent 1, 2, 3, 6, 9 or 12 months (see Bianchi
7 Incontrast,DowJonesUBScommodityindiceshaveaslightlydifferentrollover,fromthesixthtothe
tenthbusinessday(seeBianchietal.2015a).
123

| 538 |     |     | B.R.Auer |
| --- | --- | --- | -------- |
Table1 Commodityfuturescontracts
Commodity Tradingfacility Ticker Expirationmonths Availability
Energy
| Crudeoil(Brent)  | ICEUK   | LCO All | 1999 |
| ---------------- | ------- | ------- | ---- |
| Crudeoil(WTI)    | NYM/ICE | CL All  | 1987 |
| Gasoil           | ICEUK   | LGO All | 1999 |
| Heatingoil       | NYM     | HO All  | 1983 |
| Naturalgas       | NYM/ICE | NG All  | 1994 |
| Unleadedgasoline | NYM     | RB All  | 1988 |
Preciousmetals
| Gold   | CMX | GC Feb,Apr,Jun,Aug,Dec | 1977 |
| ------ | --- | ---------------------- | ---- |
| Silver | CMX | SI Mar,May,Jul,Sep,Dec | 1973 |
Industrialmetals
| Aluminum | LME | MAL All | 1991 |
| -------- | --- | ------- | ---- |
| Copper   | LME | MCU All | 1977 |
| Lead     | LME | MPB All | 1995 |
| Nickel   | LME | MNI All | 1993 |
| Zinc     | LME | MZN All | 1991 |
Agriculture
| Cocoa          | ICEUS | CC Mar,May,Jul,Sep,Dec | 1984 |
| -------------- | ----- | ---------------------- | ---- |
| Coffee         | ICEUS | KC Mar,May,Jul,Sep,Dec | 1981 |
| Corn           | CBT   | C Mar,May,Jul,Sep,Dec  | 1970 |
| Cotton         | ICEUS | CT Mar,May,Jul,Dec     | 1977 |
| Soybeans       | CBT   | S Jan,Mar,May,Jul,Nov  | 1970 |
| Sugar          | ICEUS | SB Mar,May,Jul,Oct     | 1973 |
| Wheat(Chicago) | CBT   | W Mar,May,Jul,Sep,Dec  | 1970 |
| Wheat(Kansas)  | KBT   | KW Mar,May,Jul,Sep,Dec | 1999 |
Livestock
| Feedercattle | CME | FC Jan,Mar,Apr,May,Aug,Sep,Oct,Nov | 2002 |
| ------------ | --- | ---------------------------------- | ---- |
| Leanhogs     | CME | LH Feb,Apr,Jun,Jul,Aug,Oct,Dec     | 1976 |
| Livecattle   | CME | LC Feb,Apr,Jun,Aug,Oct,Dec         | 1970 |
Forthe24commoditiescoveredbytheS&PGSCI(i.e.,thecorrespondingfuturescontracts),thistable
showsthetradingfacility,theticker,theexpirationmonthsandthestartingyearofdataavailabilityin
ThomsonReutersDatastream.Tradingfacilityabbreviationsareusedasfollows:CBT=ChicagoBoardof
Trade,CME=ChicagoMercantileExchange,CMX=NewYorkCommoditiesExchange,ICEUK(US)
=IntercontinentalExchangeUnitedKingdom(UnitedStates),KBT=KansasCityBoardofTrade,LME
=LondonMetalExchange,NYM=NewYorkMercantileExchange.Theterm‘all’referstoallcalendar
monthsfromJanuarytoDecember
etal.2015a)andoftenfocusexclusivelyon1-monthholdingperiods(seeSzakmary
etal.2010).Thisisbecausetheshort-termreversaleffectdocumentedinstockmarkets
doesnotoccurinfuturesmarkets(seeMiffreandRallis2007)orislimitedtospecific
researchsettings(seeWangandYu2004;LubnauandTodorova2015).Furthermore,
the highest returns of momentum strategies are typically observed for a 12-month
123

Havetrend-followingsignalsincommodityfuturesmarkets… 539
evaluation period and 1-month holding period (see Erb and Harvey 2006; Bianchi
etal.2015a).8
WederivebuyandsellsignalssimilartoFongetal.(2005).Thatis,eachdaywe
rankalleligiblecommoditiesindependentlyonthebasisofpasttotalreturns,where
thereturnforeachcommodityduringtheevaluationperiodismeasuredasthetotal
logpercentagechangeintheindexvalue.Takingintoaccountthepreviousevidence,
weusefiveevaluationperiods:1,3,6,9and12months.AsinSzakmaryetal.(2010),
we then assume that a 1-month long position is taken in a commodity if it is a past
winner (topthirdof commodities based on the evaluation period return),a 1-month
short position is entered if it is a past loser (bottom third) and no position is held if
itranksinthemiddle.Thiswaywecandocumentdailytradingsignals(long,short,
neutral)foreachcommodity.9 Notethatwerankdailyandnotonlyattheendofthe
monthfortworeasons.First,toobtainmeaningfulannualsuccessratios,werequire
morethantwelvesignalsayear.Second,ourapproachallowsamoregeneralanalysis
ofpredictivepowerbecauseitalsocoverstheperspectiveofinvestorstradingondays
otherthantheendofthemonth.
Time-series momentum Time-series momentum can be implemented via a variable
movingaverage(VMA)strategy.Accordingtothisstrategy,alongpositionistaken
ifanasset’sshort-termmovingpriceaverage S (overs days)exceedsitslong-term
t
moving price average L (overl days) by w percent, i.e., if S > L (1+w), and a
t t t
shortpositionistakenifS < L (1−w).NopositionisenteredwhenS iswithinthe
t t t
specified moving average band, i.e.,when L (1−w) ≤ S ≤ L (1+w).To avoid
t t t
theperniciouseffectsofdataminingandtofollowtypicalsettingsusedininvestment
practice,previousequitymarketstudieshaveoftenconcentratedonfive(s,l,w)rules
(seeBrocketal.1992;Taylor2000):(1,50,0.01),(1,150,0.01),(5,150,0.01),(1,200,
0.01)and(2,200,0.01),wheres andl aregivenintradingdays.Typicalcontinuous
ruleapplicationcanleadtofrequentpositionchangesatadaytraderlevel(seePark
andIrwin2007).
Interestingly,whileconsiderableresearchhasbeendirectedtothestudyoftechnical
rules in equity markets only a handful of studies have considered futures markets
(see Marshall et al. 2008; Clare et al. 2014). While most of these studies use in-
sampleoptimizationtoderiveoptimalvaluesfors,l andw,recentworkisguidedby
practitioners’choicesbecauseParkandIrwin(2010)haveshownthatdatasnooping
biases can have crucial effects when trading in futures markets. Furthermore, we
canobservethatdifferentdatafrequenciesareusedtocalculatemovingaverages.For
example,Szakmaryetal.(2010)usemonthlydataandthushavespecificationsof(1,6,
0.025),(1,12,0.05),(2,6,0.025)and(2,12,0.05)wheresandlaregiveninmonths.10
8 MiffreandRallis(2007)showthatprofitabilitydeclineswithrisingholdingperiodlength.Theyeven
documentnegative(zero)averagereturnsoverhorizonsof18–24months(beyond24months).
9 SimilartoSzakmaryetal.(2010),wedonotformonemomentumportfoliobasedonallcommodities
butbaseouranalysisonindividualsecurities.Ourcross-sectionalrankingsimplyservesthepurposeof
generatingwinner/losersignalswhichmaybecomparedwiththeactualwinner/loserpositionintheholding
period.
10 Thevalueofwisdifferentfromtypicalstockmarketsettingsbecausethiswaythestrategiesgenerate
neutralsignalsinaboutone-thirdofthetimeandarethuscomparabletothecross-sectionalstrategyoutlined
above.
123

540 B.R.Auer
In contrast, Narayan et al. (2015) analyze both monthly and daily frequencies. The
short-runmovingaveragesrangefrom1to12months(10to40days)andthelong-
run moving averages range from 2 to 36 months (50 to 200 days).11 They consider
end-of-month rule updating (and thus 1-month holding periods) and show that both
frequenciesleadtosuccessfulstrategies.12
In our implementation, we follow Marshall et al. (2008) by using daily data in
movingaverages.TranslatingSzakmaryetal.(2010),ourdailyrulespecificationsare
(20,120,0.025),(20,240,0.05),(40,120,0.025)and(40,240,0.05).Similartoour
cross-sectional strategies and for comparability of results, we generate signals on a
dailybasisandassume1-monthholdingperiods.
3.2 Successratioregression
Toevaluatethepredictivepowerofastrategyforaspecificcommodity,wecompare
itsforecaststotheactualrealizations.Inthecaseofcross-sectionalmomentum,we
checkwhetherpredictedwinners/losersareinfactwinners/losersintheholdingperiod
succeedingasignal.Similarly,fortime-seriesmomentum,weconsiderthepredicted
marketdirection(buysignal=upward,sellsignal=downward)andtheactualmarket
movements.Becausewefocusona1-monthholdingperiod,wederiveactualrealiza-
tionsbylookingattherelativemagnitudesandsignsofthe(cumulative)returnsinthe
20tradingdaysafterasignal,respectively.
Byperformingthiscomparison,wecanidentifythenumbersofcorrect(helpful)
andincorrect(misleading)signals.Relatingtheformertotheirsumgivesastrategy
successratioh(seeKatusiimeetal.2015).Ifwecalculatethesuccessratioeachyear,
weobtainatime-seriesofannualsuccessratios{hτ }m
τ=1
,whereτ isanindexnumber
representingtheyearsinthesampleofagivencommodity.Putdifferently,h ,h and
1 2
h arethesuccessratiosforthefirst,secondandlastsampleyear,respectively.
m
Tojudgetheexistenceofpotentialtrendsinthesuccessratios,wefollowStrobel
and Auer (2018) by regressing hτ on time.13 That is, we perform the least squares
regressionhτ =α+β·τ +(cid:5) τ,whereαandβ aretheregressionconstantandslope,
respectively,τ istheexplanatoryvariableand(cid:5) τ isaclassicerrorterm.Inthissetting,
astatisticallysignificantβ < 0(β > 0)indicatesadownward(upward)trendinthe
successratioandthusdecreasing (increasing) predictive successofagiven strategy
overtime.αcanbeinterpretedasaninitiallevelofsuccess,whichislowered(β <0)
orraised(β >0)whenmovingforwardintime.
11 NotethatNarayanetal.(2015)calculatemovingaveragesbasedonreturnsinsteadofprices.
12 Inarelatedareaofresearch,Narayanetal.(2013)findthatcommodityfuturesarebetterpredictorsfor
spotmarketswhendailydataareusedinsteadofmonthlydata.
13 StrobelandAuer(2018)emphasizethatalternativelyconductingtrendregressionsbasedonstrategy
returnsleadstoverysimilartrendconclusionsbecausesuccessratiosandstrategyreturnsarenaturally
linked.
123

Havetrend-followingsignalsincommodityfuturesmarkets… 541
4 Empiricalanalysis
4.1 Mainresults
Westartdiscussingourresultsbypresentingthetime-seriesaverages(andcorrespond-
ingt-testsignificances)oftheannualsuccessratiosinTable2.Ingeneral,asuccess
ratioof0.5indicatesthattheforecastingeffectivenessofagivenrule(withrespectto
relative rank or direction) is identical to tossing a fair coin. In other words, it has a
50:50chanceofgeneratingacorrectsignal.Thus,ifthesuccessratiosofastrategy
areonaveragesignificantlyabove(below)0.5,itisbetter(worse)thantossingacoin.
As far as cross-sectional momentum is concerned, Table 2 shows that, with few
exceptions,successratiostendtobesignificantlyabove0.5onaverage.Inlinewith
previousevidenceonthepotentialofsuchstrategiesincommoditymarkets,weoften
observethehighestsuccessratioswhenusinga12-monthformationperiodtocapture
pastperformance.Forthreeenergycommodities(Brentcrudeoil,gasoilandunleaded
gasoline), the mean success ratios are not significantly different from 0.5 over all
formation periods.14 For lead, three formation periods (1, 6 and 9 months) show
insignificance.Meansuccessratiosbelow0.5(albeitnotinastatisticallysignificant
way)onlyoccurfortheaforementionedenergycommodities.
The picture for time-series momentum strategies is quite different. Here, more
averages are below 0.5 and fewer are above 0.5. Furthermore, in the latter case, the
number of significant outcomes is noticeably lower. Beating a simple coin toss is
possibleforselectedspecificationsinnaturalgas,aluminum,nickel,zinc,coffeeand
sugarmarkets.Inthecasesofcoffeeandsugarfutures,allstrategyspecificationswork
well.Incontrast,forgold,cocoa,soybeans,feedercattleandleanhogs,tossingacoin
tendstohaveahigherrateofdirectionaleffectiveness.
Tables 3 and 4 report the constant and slope coefficient estimates arising in our
regressions of annual success ratios on time, respectively. For the cross-sectional
momentum strategies, we can make two important observations. First, except for a
slightlyweakerextentintheenergysector,wehavehighandsignificantinitiallevelsof
predictivesuccessacrossallcommodities.15Inarankingofcommodityfutures,therel-
ativepositionsofgoldandzinccouldhavebeenforecastedbest.Second,eventhough
downwardtrendsoutnumberupwardtrends,onlyfewoftheformerandalmostnone
of the latter are statistically significant. Consequently, success ratios do not deviate
stronglyfromtheirinitiallevelsovertime.Mostofthelimitedinstancesofsignificant
declinesinsuccessratiosclusterinthefuturesmarketsforgold,zinc,cocoa,cornand
soybeans.Incomparison,energyandlivestockshownosignificanttrendingbehavior.
Figure1illustratesthesuccessofsomeselectedstrategiesappliedtogoldandsilver
futures.Weseethatthepredictiveaccuracyforgoldisdecliningsignificantlywhereas
it appears to be rather stable (with fluctuations around a mean of about 0.6) for sil-
ver.Overall,ourresultssuggestthatcommodityfutures’cross-sectionalmomentum
14 TheobservabledistinctresultsforBrentandWTIcrudeoilarenotsurprisingbecausetheirtime-series
characteristicsarequitedifferent(seeTianandLai2019).
15 Wewouldnotexpectlevelsveryclosetoonebecausepastreturnsareunlikelytobeabletoforecast
unforeseeableoutsideeventsrelatedtoclimatephenomena(affecting,forexample,wheatprices)orcrisis-
relatedinvestorbehavior(influencing,forexample,asafehavenassetlikegold).
123

542 B.R.Auer
soitarsseccusegarevA
2elbaT
mutnemomseires-emiT
mutnemomlanoitces-ssorC
)50.0,042,04(
)520.0,021,04(
)50.0,042,02(
)520.0,021,02(
shtnom21
shtnom9
shtnom6
shtnom3
htnom1
ygrenE
105.0
825.0
915.0
625.0
315.0
994.0
805.0
425.0
435.0
)tnerB(lioedurC
884.0
215.0
684.0
315.0
a765.0
c935.0
a565.0
a555.0
b445.0
)ITW(lioedurC
025.0
315.0
825.0
035.0
345.0
294.0
915.0
215.0
135.0
liosaG
184.0
984.0
205.0
905.0
b845.0
c435.0
c835.0
c135.0
b645.0
liognitaeH
435.0
b655.0
c845.0
b265.0
a806.0
b675.0
a016.0
a185.0
a155.0
saglarutaN
125.0
594.0
905.0
294.0
025.0
874.0
384.0
884.0
294.0
enilosagdedaelnU
slatemsuoicerP
384.0
c164.0
c644.0
b544.0
a226.0
a126.0
a536.0
a826.0
a326.0
dloG
494.0
694.0
305.0
284.0
a106.0
a795.0
a895.0
a095.0
a685.0
revliS
slatemlairtsudnI
915.0
c345.0
115.0
c335.0
a936.0
a976.0
a866.0
a466.0
a856.0
munimulA
694.0
315.0
194.0
915.0
a806.0
a685.0
a506.0
a895.0
a465.0
reppoC
225.0
205.0
115.0
215.0
b545.0
215.0
325.0
b355.0
135.0
daeL
915.0
c945.0
525.0
b955.0
635.0
a765.0
a285.0
a675.0
a355.0
lekciN
c255.0
b345.0
025.0
b245.0
a806.0
a506.0
a616.0
a526.0
a995.0
cniZ
123

Havetrend-followingsignalsincommodityfuturesmarkets… 543
deunitnoc
2elbaT
mutnemomseires-emiT
mutnemomlanoitces-ssorC
)50.0,042,04(
)520.0,021,04(
)50.0,042,02(
)520.0,021,02(
shtnom21
shtnom9
shtnom6
shtnom3
htnom1
erutlucirgA
505.0
774.0
c854.0
c574.0
a895.0
a195.0
a495.0
a385.0
b735.0
aocoC
a165.0
a655.0
b945.0
b445.0
a595.0
a995.0
a395.0
a095.0
a455.0
eeffoC
884.0
325.0
484.0
815.0
a036.0
a836.0
a036.0
a926.0
a216.0
nroC
294.0
015.0
394.0
805.0
a195.0
a106.0
a306.0
a785.0
a075.0
nottoC
784.0
c074.0
974.0
b854.0
a416.0
a906.0
a216.0
a495.0
a226.0
snaebyoS
c635.0
a355.0
b745.0
a655.0
a455.0
b245.0
a665.0
a265.0
a165.0
raguS
315.0
015.0
894.0
615.0
a526.0
a216.0
a406.0
a126.0
a526.0
)ogacihC(taehW
205.0
115.0
284.0
984.0
a746.0
a746.0
a356.0
a126.0
a606.0
)sasnaK(taehW
kcotseviL
b044.0
574.0
764.0
784.0
a985.0
b755.0
a965.0
a775.0
a085.0
elttacredeeF
b944.0
474.0
b554.0
c474.0
b645.0
a645.0
a455.0
a245.0
a845.0
sgohnaeL
805.0
915.0
305.0
625.0
a265.0
a565.0
a865.0
a175.0
a685.0
elttaceviL yrammuS
)2(01
)2(8
)3(11
)4(8
)0(0
)0(3
)0(1
)0(1
)0(1
).ngis(5.0<h
¯
)3(41
)6(61
)3(31
)6(61
)02(42
)02(12
)02(32
)12(32
)02(32
).ngis(5.0>h
¯
sseccuslaunnaehtfosegarevaseires-emitehtstroperelbatsiht,seigetartsmutnemomseires-emitdnalanoitces-ssorcfosnoitacfiicepstnereffiddnaseitidommoc42ruoroF defiicepseraselur)AMVro(mutnemomseires-emiT.shtnom21dna9,6,3,1fosdoirepnoitamrofrofdetnemelpmisimutnemomlanoitces-ssorC.3.tceSnidenfiedsoitar rellamstuogniretlfidnabehtgninfiedegatnecrepehtsiwdna,ylevitcepser,segarevagnivomnur-gnoldnanur-trohsehtfo)syadni(htgnelehteraldnaserehw)w,l,s(aiv ,level%01dna%5,%1ehtta5.0morfsecnereffidtnacfiingisylpmicdnab,a,stset-tlacipytnodesaB.htnomenoebotdemussasidoirepgnidloheht,sesacllanI.snoitautcufl yllanoitiddadna)seitidommocllassorca(5.0nahtretaerg/rellamssoitarsseccusnaemforebmunehtstnuocelbatehtfomottobeht,evitcepsrepllarevonaroF.ylevitcepser
sesehtnerapnisesactnacfiingisyllacitsitatsforebmunehtsevig
123

544 B.R.Auer
)50.0,042,04(
|     |       |             |                   |             |       | c106.0 c806.0 |
| --- | ----- | ----------- | ----------------- | ----------- | ----- | ------------- |
|     | 416.0 | 215.0 775.0 | 154.0 064.0 625.0 | 445.0 994.0 | 215.0 | 465.0 375.0   |
)520.0,021,04(
|     | 835.0 | c375.0 835.0 | 094.0 694.0 005.0 | 094.0 435.0 | 084.0 | c285.0 365.0 c785.0 c665.0 |
| --- | ----- | ------------ | ----------------- | ----------- | ----- | -------------------------- |
)50.0,042,02(
c195.0
|     | 395.0 | 635.0 275.0 | 594.0 784.0 784.0 | 405.0 884.0 | 015.0 | 065.0 835.0 475.0 |
| --- | ----- | ----------- | ----------------- | ----------- | ----- | ----------------- |
mutnemomseires-emiT
)520.0,021,02(
|     |       | c975.0 |                   |             |       | c585.0            |
| --- | ----- | ------ | ----------------- | ----------- | ----- | ----------------- |
|     | 125.0 | 835.0  | 705.0 815.0 984.0 | 784.0 505.0 | 894.0 | 955.0 245.0 845.0 |
shtnom21
|     | 015.0 | 945.0 805.0 | 025.0 245.0 345.0 | a147.0 b106.0 | a586.0 | a436.0 b395.0 b516.0 a067.0 |
| --- | ----- | ----------- | ----------------- | ------------- | ------ | --------------------------- |
shtnom9
|     |       |             |                   | a237.0 b516.0 | a407.0 | a426.0 b806.0 a957.0 |
| --- | ----- | ----------- | ----------------- | ------------- | ------ | -------------------- |
|     | 444.0 | 525.0 684.0 | 325.0 084.0 394.0 |               |        | 385.0                |
shtnom6
|     |       | c765.0 |                   | a847.0 a546.0 | a256.0 | a166.0 b716.0 b795.0 a957.0 |
| --- | ----- | ------ | ----------------- | ------------- | ------ | --------------------------- |
|     | 215.0 | 035.0  | 655.0 255.0 025.0 |               |        |                             |
mutnemomlanoitces-ssorC
snoissergerdnertfostneicfifeoctnatsnoC
shtnom3
|     |       | b785.0 |                   | a007.0 a266.0 | a976.0 | a436.0 b236.0 b575.0 a857.0 |
| --- | ----- | ------ | ----------------- | ------------- | ------ | --------------------------- |
|     | 215.0 | 425.0  | 845.0 735.0 584.0 |               |        |                             |
htnom1
|     |       | b595.0 | b575.0       |               |        | b695.0              |
| --- | ----- | ------ | ------------ | ------------- | ------ | ------------------- |
|     | 315.0 | 925.0  | c755.0 235.0 | a956.0 a426.0 | a607.0 | a195.0 745.0 a637.0 |
enilosagdedaelnU
|     | )tnerB(lioedurC | )ITW(lioedurC |     |     | slatemlairtsudnI |     |
| --- | --------------- | ------------- | --- | --- | ---------------- | --- |
slatemsuoicerP
saglarutaN
|        |        |        | liognitaeH |        | munimulA |           |
| ------ | ------ | ------ | ---------- | ------ | -------- | --------- |
| 3elbaT | ygrenE | liosaG |            |        |          | reppoC    |
|        |        |        |            | revliS |          | lekciN    |
|        |        |        |            | dloG   |          | daeL cniZ |
123

Havetrend-followingsignalsincommodityfuturesmarkets… 545
)50.0,042,04( fosnoissergerserauqstsaelfostneicfifeoctnatsnocehtstroperelbatsiht,seigetartsserutufytidommocgniwollof-dnertruofohcaerofdna2elbaTotralimiserutcurtsanI ehtsevigelbatehtfomottobehttayrammusehT.ylevitcepser,level%01dna%5,%1ehtta5.0morfsecnereffidtnacfiingisylpmicdnab,a.emitnosoitarsseccuslaunna
|                   | c375.0            |             | b875.0 c095.0 |       |
| ----------------- | ----------------- | ----------- | ------------- | ----- |
| 945.0 725.0 864.0 | 494.0 894.0 415.0 | 345.0 254.0 |               | )5(71 |
)0(7
)520.0,021,04(
|                   | a185.0            |             | a695.0 b185.0 |            |
| ----------------- | ----------------- | ----------- | ------------- | ---------- |
| 374.0 915.0 815.0 | 325.0 574.0 545.0 | 525.0 294.0 |               | )0(8 )7(61 |
)50.0,042,02(
| 264.0 435.0 564.0 | 994.0 805.0 a985.0 225.0 | 315.0 834.0 | b106.0 b595.0 | )4(61 ecnacfiingisfosesacgnidnopserroceht,sesehtnerapni,dna)seitidommocllassorca(5.0woleb/evobastnatsnocforebmun |
| ----------------- | ------------------------ | ----------- | ------------- | ---------------------------------------------------------------------------------------------------------------- |
)0(8
mutnemomseires-emiT
)520.0,021,02(
|                   | a695.0 c955.0 |             | a416.0 b885.0 |       |
| ----------------- | ------------- | ----------- | ------------- | ----- |
| 764.0 525.0 025.0 | 545.0 584.0   | 254.0 525.0 |               | )6(81 |
)0(6
shtnom21
| a127.0 a886.0 | a526.0 a027.0 b195.0 a136.0 | b386.0 b246.0 | c765.0 | )61(42 |
| ------------- | --------------------------- | ------------- | ------ | ------ |
| 555.0         |                             |               | 845.0  |        |
)0(0
shtnom9
| a696.0 a107.0 | b726.0 a117.0 c675.0 a046.0 | b556.0 | c265.0 | )41(02 |
| ------------- | --------------------------- | ------ | ------ | ------ |
| 055.0         |                             | 075.0  | 945.0  |        |
)0(4
shtnom6
b875.0
| a066.0 735.0 a727.0 | a036.0 a807.0 a736.0 | a566.0 045.0 | 925.0 c965.0 | )61(42 |
| ------------------- | -------------------- | ------------ | ------------ | ------ |
)0(0
mutnemomlanoitces-ssorC
shtnom3
| a217.0 925.0 a907.0 | b206.0 a596.0 b665.0 a466.0 | a107.0 245.0 | b465.0 b575.0 | )71(32 |
| ------------------- | --------------------------- | ------------ | ------------- | ------ |
)0(1
htnom1
| a226.0 a017.0 | a095.0 a776.0 a675.0 a856.0 | a836.0 a316.0 | a575.0 | )81(42 |
| ------------- | --------------------------- | ------------- | ------ | ------ |
| 635.0         |                             |               | 915.0  |        |
)0(0
deunitnoc
)ogacihC(taehW
|             |     | )sasnaK(taehW |     | ).ngis(5.0<αˆ ).ngis(5.0>αˆ |
| ----------- | --- | ------------- | --- | --------------------------- |
| erutlucirgA |     | elttacredeeF  |     |                             |
sgohnaeL elttaceviL
|               | snaebyoS | kcotseviL |     | yrammuS |
| ------------- | -------- | --------- | --- | ------- |
| 3elbaT eeffoC | nottoC   |           |     |         |
| aocoC         | raguS    |           |     |         |
nroC
123

546 B.R.Auer
snoissergerdnertfostneicfifeocepolS
4elbaT
mutnemomseires-emiT
mutnemomlanoitces-ssorC
)50.0,042,04(
)520.0,021,04(
)50.0,042,02(
)520.0,021,02(
shtnom21
shtnom9
shtnom6
shtnom3
htnom1
ygrenE
362.1−
352.0−
578.0−
201.0−
881.0
625.0
870.0−
260.0
042.0
)tnerB(lioedurC
531.0−
083.0−
703.0−
793.0−
850.0
750.0
800.0−
691.0−
423.0−
)ITW(lioedurC
047.0−
173.0−
616.0−
012.0−
924.0
760.0
121.0−
560.0−
580.0
liosaG
941.0
810.0
530.0
430.0
332.0
850.0
170.0−
090.0−
741.0−
liognitaeH
234.0
333.0
133.0
612.0
583.0
016.0
723.0
442.0
490.0−
saglarutaN
031.0−
860.0−
830.0
520.0−
732.0−
901.0−
832.0−
610.0
522.0−
enilosagdedaelnU
slatemsuoicerP
693.0−
061.0−
063.0−
812.0−
b825.0−
c305.0−
b694.0−
723.0−
851.0−
dloG
860.0−
181.0−
910.0
411.0−
500.0
970.0−
102.0−
c792.0−
551.0−
revliS
slatemlairtsudnI
771.0
593.0
031.0
002.0
771.0−
161.0−
670.0
131.0−
243.0−
munimulA
c905.0−
523.0−
623.0−
281.0−
561.0−
002.0−
c282.0−
881.0−
721.0−
reppoC
113.0−
434.0−
202.0−
281.0−
134.0−
174.0−
c257.0−
166.0−
855.0−
daeL
352.0−
392.0−
733.0−
512.0−
384.0−
922.0−
021.0−
930.0−
820.0
lekciN
815.0−
181.0−
083.0−
250.0−
b589.0−
a320.1−
b089.0−
b339.0−
a259.0−
cniZ
123

Havetrend-followingsignalsincommodityfuturesmarkets… 547
)50.0,042,04( evahsetamitsetneicfifeoceht,noitazilausivrettebroF.emitnosoitarsseccuslaunnafosnoissergerserauqstsaelfostneicfifeocepolsehtstroperelbatsiht,3elbaTgnidnetxE evitisop/evitagenforebmunehtsevigelbatehtfomottobehttayrammusehT.ylevitcepser,level%01dna%5,%1ehttaecnacfiingisylpmicdnab,a.001ybdeilpitlumneeb
a835.0− c673.0−
|     | 352.0− 521.0 050.0 | 540.0 170.0− 102.0− 900.0− 351.0− | 122.0− |     |
| --- | ------------------ | --------------------------------- | ------ | --- |
)3(81
)0(6
)520.0,021,04(
a545.0− c572.0−
|     | 250.0 271.0 610.0− | 170.0− 240.0− 531.0− 241.0− 831.0− | 631.0− |     |
| --- | ------------------ | ---------------------------------- | ------ | --- |
)2(91 )0(5
)50.0,042,02(
a316.0− b104.0−
|     | 520.0− 220.0 440.0 | 130.0 541.0− 222.0− 990.0− 560.0− | 812.0 |     |
| --- | ------------------ | --------------------------------- | ----- | --- |
)2(51
)0(9
mutnemomseires-emiT
)520.0,021,02(
a036.0−
|     | 370.0 670.0 720.0− | 481.0− 801.0− 081.0− 381.0− 023.0 | 234.0− | 602.0− |
| --- | ------------------ | --------------------------------- | ------ | ------ |
)1(81 )0(6
ecnacfiingisfosesacgnidnopserroceht,sesehtnerapni,dna)seitidommocllassorca(sdnert
shtnom21
|     | b836.0−      | a354.0−                     |        |             |
| --- | ------------ | --------------------------- | ------ | ----------- |
|     | 962.0 871.0− | 111.0− 601.0− 750.0− 063.0− | 758.0− | 100.0 720.0 |
)4(51 )0(9
| shtnom9 | c085.0−      | b834.0−                     |        |             |
| ------- | ------------ | --------------------------- | ------ | ----------- |
|         | 542.0 302.0− | 631.0− 511.0− 141.0− 502.0− | 713.0− | 200.0 060.0 |
)4(61
)0(8
shtnom6
|     | 833.0− 103.0 b004.0− | 841.0− b714.0− 730.0− 990.0− 322.0− | 181.0 | 811.0 140.0 |
| --- | -------------------- | ----------------------------------- | ----- | ----------- |
)6(81
)0(6
mutnemomlanoitces-ssorC
| shtnom3 | a386.0− b943.0− | 490.0− b653.0− 020.0− 202.0− 378.0− | 413.0 | 290.0− 920.0 |
| ------- | --------------- | ----------------------------------- | ----- | ------------ |
c623.0
)5(81
)1(6
| htnom1 | b164.0− a353.0− | b842.0−                     |        |             |
| ------ | --------------- | --------------------------- | ------ | ----------- |
|        | 101.0           | 211.0− 760.0− 361.0− 004.0− | 284.0− | 421.0 870.0 |
)4(81
)0(6
deunitnoc
)ogacihC(taehW
)sasnaK(taehW
).ngis(0<ˆβ ).ngis(0>ˆβ
|     | erutlucirgA |     | elttacredeeF |     |
| --- | ----------- | --- | ------------ | --- |
sgohnaeL elttaceviL
|        |        | snaebyoS | kcotseviL | yrammuS |
| ------ | ------ | -------- | --------- | ------- |
| 4elbaT | eeffoC | nottoC   |           |         |
|        | aocoC  | raguS    |           |         |
nroC
123

548 B.R.Auer
is likely to remain as effective as documented in the past, which contrasts with the
recentevidenceinstockmarkets(seeChordiaetal.2014).16
Turningtothetime-seriesmomentumstrategies(andfocusingonhighsignificance
of1%and5%only),wedocumenthighinitialforecastingperformanceonlyforsugar,
lean hogs and live cattle. Similar to cross-sectional momentum, significant trending
behavioriswidelyabsent.Thefewcasesofsignificantdeclineclusterinthelivestock
sector. Because the corresponding average success ratios in Table 2 are below 0.5,
thesefindingscallforcautioninafutureuseoftime-seriesmomentumstrategiesfor
livestockcontracts.Forthesecontracts,thestrategiesmayhavehadsuitablepredictive
powerinthepast,butapparentlyithasstartedtovanish.Figure1,whichcoverssuccess
ratiosandcorrespondingtrendlinesforselectedtime-seriesmomentumstrategiesfor
goldandsilver,isrepresentativeformostothersectors.Whilestockmarketsuccess
ratiosexhibitdeclinesfrominitiallyhighlevels(seeStrobelandAuer2018),infutures
markets,thestrategiesarelesspersuasivewithrespecttoforecastingabilityandshow
nosignificanttrendingbehavior.Thisresulthastobeinterpretedcarefullybecauseit
doesnotmeanthatthestrategiesareuseless.Theirdirectionalaccuracymaybesimilar
to tossing a coin but, given the results of the previous literature, this interestingly
appearstobesufficienttoprovidebeneficialinvestmentperformancewhenappliedto
the majority of available commodity futures (see Szakmary et al. 2010; Clare et al.
2014).Theobservationofnotexistingtrendsinsuccessratiosisimportantbecauseit
conveysasenseofstabilityandthuscontinuouspredictivereliability.
4.2 Robustnesschecks
Because some features of our research design might be thought of driving its main
outcome,weperformseveralsensitivitycheckstoensurerobustness.Becausethese
checkslargelyconfirmthefindingsofthepreviousSection,weconcentrateonaverbal
summaryoftheirbasicidea.17
Rollover MiffreandRallis(2007)analyzewhetherrollovermodifications(suchasa
laterrolloverdateandusingmoredistantmaturitycontracts)haveadamagingimpact
onmomentumrulesandfindthat,eventhoughprofitsarelower,momentumpersists.
Nevertheless,onemightarguethatthetypeofrolloverimplementedinGSCIindices
mayinfluenceourtrendresults.Torulethisout,wecollecttheindividualfuturesdata
oftheindicesandmanuallyimplementalternativerollovers.Specifically,wefollow
Lukacetal.(1988)byrollingoverintothenextcontractmonthpriortodeliveryand,
fromthispointon,usingdataofthenewcontractforsignalgeneration.Wealsofollow
Fuertesetal.(2015)byimmediatelyrollingoveratthelasttradingday.However,we
findthatourresultsarenotsensitivetosuchmodifications.
Cross-sectional momentum While it has become standard to rank assets based on
cumulativepastreturns,somestudiesusealternativevariables.Forexample,Rachev
et al. (2007) employ reward-to-risk measures (like the Sharpe ratio) and Narayan
16 Foradetailedempiricalanalysisofthereasonswhymomentumstrategiesbehavedifferentlyinstock
andfuturesmarkets,seeChevallieretal.(2013).
17 Detailedresultsareavailablefromtheauthorsuponrequest.
123

Havetrend-followingsignalsincommodityfuturesmarkets… 549
Fig.1 Exemplarysuccessratiotrendplots.Forgoldandsilverfutures,thisfigureplotstheannualsuc-
cessratiosofselectedtrend-followingtradingrulesandthecorrespondingleastsquarestrendregression
lines.arelatestocross-sectionalmomentumwitha12-monthformationperiod.bcapturesthetime-series
momentum(orVMA)rule(s=40,l=120,w=0.025).Theholdingperiodisonemonth
et al. (2015) implement the momentum indicator (the difference between short-run
and long-run moving return averages). Furthermore, while we followed Szakmary
etal.(2010)bydividingassetsintothreegroups(top,middle,bottom)andusingonly
thetopandbottomthirds,MiffreandFernandez-Perez(2015)suggestconcentrating
onthetopandbottomfifths.18 Incontrasttothisfocusonrelativestrength,wherea
futurewithnegativepastperformancemayshowuponthewinnersidebecauseitis
lessnegativethanothers,ErbandHarvey(2006)usepositiveandnegativereturnsto
drawaclearerdistinctionbetweenwinnersandlosers.Overall,suchsettingsdonot
alterourconclusions.
Time-seriesmomentumOccasionally,movingaveragerulesareimplementedbycal-
culatingthemovingaverageofreturnsinsteadofprices(seeRatnerandLeal1999).
18 Addingmorefuturestothewinnerorlosersidesenhancesriskdiversificationatthecostoflowering
thedispersionofreturnsbetweenthebestandworstperformingfuturesandthustheprofitabilityofthe
strategy.
123

550 B.R.Auer
Furthermore,onemightalsouseexponentiallyweightedaveragesinsteadofarithmetic
averages(seeRosilloetal.2013).19Applyingthesealternativeapproachesrevealsthat
return-basedmovingaveragesleadtolowernumbersofsuccessfulpredictionsandthat
ourresultsremainlargelyunchangedwhenswitchingtoexponentialmovingaverages.
SignalfrequencyandholdingperiodBecauseouranalysisprovidessignalsonadaily
frequency, we have also modified our setup to generate only one signal per month
attheendofthemonth(asinSzakmaryetal.2010)whileleavingallothersettings
untouched.Furthermore,werepeatedourcalculationsfordailyandweeklyholding
periodlengths.Again,ourmainconclusionsholdbutwithsomewhatfewerinstances
ofstatisticallysignificanttrends.
TrendfunctionFinally,wehaveestimatedanexponentialandaquadratictrendmodel
inadditiontoourstandardsetting.Intheformer,weusethenaturallogarithmofthe
successratioastheleft-handvariable;inthelatter,weaddtimesquaredasasecond
right-handvariable(seePindyckandRubinfeld1998).Thisway,wecanconsidera
potentiallynonlinearevolution,butfindthatitdoesnotchangethesignsandsignifi-
cancesofourtrendresults.
5 Conclusion
Pastresearchhasdocumentedimpressiveperformanceoftrend-followingtradingrules
inboththestockandthefuturesmarkets.However,morerecentstudiesindicatethat
thebenefitsofsuchstrategiesinstockmarketstendstodeclinewithfallingarbitrage
barriers(lowertransactioncosts,marketaccessforlow-suminvestors)andincreased
(automated)tradingactivityovertime(seeStrobelandAuer2018;AuerandRottmann
2019). Motivated by such results, we have analyzed whether similar tendencies can
beobservedforcommodityfuturesmarkets.
Using a broad selection of energy, precious metals, industrial metals, agriculture
andlivestockfutures,wehavetestedforsignificanttimetrendsinthesuccessratios
of various cross-sectional and time-series momentum strategies. In other words, we
haverevealedthepredictivecapabilitiesbehindthefinancialperformanceexcessively
documentedinthepreviousresearchandinvestigatedtheirdynamicsovertime.Our
findings for cross-sectional momentum indicate predictive accuracy above the level
ofasimplecointossandonlyfewinstancesoftrending.Incontrast,thesuccessratios
oftime-seriesmomentumareclosetotossingafaircoinbutshowasimilarabsenceof
significanttimetrends.Supportedbyavarietyofrobustnesschecks,theseresultshave
two important implications for commodity investing. First, time-series momentum
increasesinvestors’wealthdespitehavingsuccessratiossimilartoafaircoin.Second,
contrasting stock market research, historically beneficial trend-following strategies
canbeexpectedtocontinuetoperformwellinthefuture(unless,ofcourse,thereare
drasticchangesinmarketstructureorinvestorbehavior).
19 Adaptiveaverageshavealsoreceivedattention.Theyseektoidentifyandadoptchangingmarketcon-
ditionsviaanefficiencyratioderivedfromthenotionoffractalefficiencyandamethodclosetorescaled
rangeanalysis(seeEllisandParbery2005).However,thecorrespondingnewtradingrulesleavetheclassic
VMAframework.
123

Havetrend-followingsignalsincommodityfuturesmarkets… 551
As far as future research is concerned, several issues merit deeper investigation.
First, since we have downward trends in stock markets but (almost) no trends in
commodityfuturesmarkets,itmaybeinstructivetoseehowthisaffectsthepredic-
tiveabilitiesofstrategiesapplyingmomentumacrossassetclasses(see,forexample,
GeorgopoulouandWang2017).Second,becausewehaveconcentratedonlyonone
possibility of implementing time-series momentum, our study may be extended to
regression-basedforms(asin,forexample,Moskowitzetal.2012).Finally,wemight
wishtorevealtheoriginsofthesignificanttrendsdetectedforsomecommodities(such
asgold)bylookingatinvestorsentimentvariables(seeJacobs2015)ortheimpactof
financializationonmomentumperformance(seeZaremba2016).
Acknowledgements TheauthorthanksHorstRottmann,JuliaMehlitz,AnjaVinzelbergandananonymous
reviewerforvaluablecommentsandsuggestions.HeisalsoindebtedtotheFritzThyssenStiftung(Grant
20.18.0.016WW)forgenerousfinancialsupport.
References
Auer,B.:Doesthechoiceofperformancemeasureinfluencetheevaluationofcommodityinvestments?Int.
Rev.Financ.Anal.38,142–150(2015)
Auer,B.,Rottmann,H.:Havecapitalmarketanomaliesworldwideattenuatedintherecenteraofhigh
liquidityandtradingactivity?J.Econ.Bus.103,61–79(2019)
Bajgrowicz,P.,Scaillet,O.:Technicaltradingrevisited:falsediscoveries,persistencetestsandtransaction
costs.J.Financ.Econ.106(3),473–491(2012)
Bianchi,R.,Drew,M.,Fan,J.:Combiningmomentumwithreversalincommodityfutures.J.Bank.Finance
59,423–444(2015a)
Bianchi,R.,Drew,M.,Fan,J.:Microscopicmomentumincommodityfutures.GriffithUniversityDiscussion
PapersFinanceNo.2015-10(2015b)
Bianchi,R.,Drew,M.,Fan,J.:Commoditiesmomentum:abehavioralperspective.J.Bank.Finance72,
133–150(2016)
Brock,W.,Lakonishok,J.,LeBaron,B.:Simpletechnicaltradingrulesandthestochasticpropertiesof
stockreturns.J.Finance47(5),1731–1764(1992)
Chevallier,J.,Gatumel,M.,Ielpo,F.:Understandingmomentumincommoditymarkets.Appl.Econ.Lett.
20(15),1383–1402(2013)
Chordia,T.,Subrahmanyam,A.,Tong,Q.:Havecapitalmarketanomaliesattenuatedintherecenteraof
highliquidtiyandtradingactivity?J.Account.Econ.58(1),41–58(2014)
Clare,A.,Seaton,J.,Smith,P.,Thomas,S.:Trendfollowing,riskparityandmomentumincommodity
futures.Int.Rev.Financ.Anal.31,1–12(2014)
deGroot,W.,Karstanje,D.,Zhou,W.:Exploitingcommoditymomentumalongthefuturescurves.J.Bank.
Finance48,79–93(2014)
Ellis,C.,Parbery,S.:Issmarterbetter?Acomparisonofadaptive,andsimplemovingaveragetrading
strategies.Res.Int.Bus.Finance19(3),399–411(2005)
Erb,C.,Harvey,C.:Thestrategicandtacticalvalueofcommodityfutures.Financ.Anal.J.62(2),69–97
(2006)
Fama,E.,French,K.:Dissectinganomalies.J.Finance63(4),1653–1678(2008)
Fama,E.,French,K.:Size,value,andmomentumininternationalstockreturns.J.Financ.Econ.105(3),
457–472(2012)
Fifield,S.,Power,D.,Knipe,D.:Theperformanceofmovingaveragerulesinemergingstockmarkets.
Appl.Financ.Econ.18(19),1515–1532(2008)
Fleming,J.,Ostdiek,B.,Whaley,R.:Tradingcostsandtherelativeratesofpricediscoveryinstock,futures,
andoptionmarkets.J.FuturesMark.16(4),353–387(1996)
Foltice,B.,Langer,T.:Profitablemomentumtradingstrategiesforindividualinvestors.Financ.Mark.Portf.
Manag.29,85–113(2015)
123

552 B.R.Auer
Fong,W.,Wong,W.,Lean,H.:Internationalmomentumstrategies:astochasticdominanceapproach.J.
Financ.Mark.8(1),89–109(2005)
Fuertes,A.,Miffre,J.,Fernandez-Perez,A.:Commoditystrategiesbasedonmomentum,termstructureand
idiosyncraticvolatility.J.FuturesMark.35(3),274–295(2015)
Fuertes,A.,Miffre,J.,Rallis,G.:Tacticalallocationincommodityfuturesmarkets:combiningmomentum
andtermstructuresignals.J.Bank.Finance34(10),2530–2548(2010)
Georgopoulou,A.,Wang,J.:Thetrendisyourfriend:time-seriesmomentumstrategiesacrossequityand
commoditymarkets.Rev.Finance21(4),1557–1592(2017)
Gorton,G.,Rouwenhorst,K.:Factsandfantasiesaboutcommodityfutures.Financ.Anal.J.62(2),47–68
(2006)
Hendershott,T.,Jones,C.,Menkveld,A.:Doesalgorithmictradingimproveliquidity?J.Finance66(1),
1–33(2011)
Hong,H.,Yogo,M.:Whatdoesfuturesmarketinteresttellusaboutthemacroeconomyandassetprices?
J.Financ.Econ.105(3),473–490(2012)
Irwin,S.,Yoshimaru,S.:Managedfutures,positivefeedbacktrading,andfuturespricevolatility.J.Futures
Mark.19(7),759–776(1999)
Jacobs,H.:Whatexplainsthedynamicsof100anomalies?J.Bank.Finance57,65–85(2015)
Jacobs,H.,Müller,S.:Anomaliesacrosstheglobe:oncepublic,nolongerexistent?J.Financ.Econ.135(1),
213–230(2020)
Jegadeesh,N.,Titman,S.:Returnstobuyingwinnersandsellinglosers:implicationsforstockmarket
efficiency.J.Finance48(1),65–91(1993)
Jegadeesh,N.,Titman,S.:Profitabilityofmomentumstrategies:anevaluationofalternativeexplanations.
J.Finance56(2),699–720(2001)
Katusiime,L.,Shamsuddin,A.,Agbola,F.:Foreignexchangemarketefficiencyandprofitabilityoftradin-
grules:evidencefromadevelopingcountry.Int.Rev.Econ.Finance35,315–332(2015)
Kavajecz,K.,Odders-White,E.:Technicalanalysisandliquidityprovision.Rev.Financ.Stud.17(4),1043–
1071(2004)
Kho,B.:Time-varyingriskpremia,volatility,andtechnicaltradingruleprofits:evidencefromforeign
currencyfuturesmarkets.J.Financ.Econ.41(2),249–290(1996)
Korajczyk,R.,Sadka,R.:Aremomentumprofitsrobusttotradingcosts?J.Finance59(3),1039–1082
(2004)
Lesmond,D.,Schill,M.,Zhou,C.:Theillusorynatureofmomentumprofits.J.Financ.Econ.71(2),349–380
(2004)
Locke,P.,Venkatesch,P.:Futuresmarkettransactioncosts.J.FuturesMark.17(2),229–245(1997)
Lubnau,T.,Todorova,N.:Tradingonmean-reversioninenergyfuturesmarkets.EnergyEcon.51,312–319
(2015)
Lukac,L.,Brorsen,B.,Irwin,S.:Atestoffuturesmarketdisequilibriumusingtwelvedifferenttechnical
tradingsystems.Appl.Econ.20(5),623–639(1988)
Marshall,B.,Cahan,R.,Cahan,J.:Cancommodityfuturesbeprofitablytradedwithquantitativemarket
timingstrategies?J.Bank.Finance32(9),1810–1819(2008)
McLean,R.,Pontiff,J.:Doesacademicresearchdestroystockreturnpredictability?J.Finance71(1),5–32
(2016)
Miffre,J.:Long-shortcommodityinvesting:areviewoftheliterature.J.Commod.Mark.1(1),3–13(2016)
Miffre, J., Fernandez-Perez, A.: The case for long-short commodity investing. J. Altern. Invest. 18(1),
92–104(2015)
Miffre,J.,Rallis,G.:Momentumstrategiesincommodityfuturesmarkets.J.Bank.Finance31(6),1863–
1886(2007)
Morana,C.:Asemiparametricapproachtoshort-termoilpriceforecasting.EnergyEcon.23(3),325–338
(2001)
Moskowitz,T.,Ooi,Y.,Pedersen,L.:Timeseriesmomentum.J.Financ.Econ.104(2),228–250(2012)
Narayan,P.,Ahmed,H.,Narayan,S.:Domomentum-basedtradingstrategiesworkinthecommodityfutures
markets?J.FuturesMark.35(9),868–891(2015)
Narayan,P.,Narayan,S.,Sharma,S.:Ananalysisofcommoditymarkets:whatgainforinvestors?J.Bank.
Finance37(10),3878–3889(2013)
Olson,D.:Havetradingruleprofitsinthecurrencymarketsdeclinedovertime?J.Bank.Finance28(1),
85–105(2004)
123

Havetrend-followingsignalsincommodityfuturesmarkets… 553
Park,C.,Irwin,S.:TheprofitabilityoftechnicaltradingrulesinUSfuturesmarkets:adatasnoopingfree
test.AgMASProjectResearchReport2005-04(2005)
Park,C.,Irwin,S.:ArealitycheckontechnicaltradingruleprofitsintheU.S.futuresmarkets.J.Futures
Mark.30(7),633–659(2010)
Park,C.,Irwin,S.:Whatdoweknowabouttheprofitabilityoftechnicalanalysis?J.Econ.Surv.21(4),
786–826(2007)
Pindyck,R.,Rubinfeld,D.:EconometricModelsandEconomicForecasts.McGraw-Hill,Singapore(1998)
Rachev,S.,Jas˘ic´,T.,Stoyanov,S.,Fabozzi,F.:Momentumstrategiesbasedonreward-riskstockselection
criteria.J.Bank.Finance31(8),2325–2346(2007)
Ratner,M.,Leal,R.:TestsoftechnicaltradingstrategiesintheemergingequitymarketsofLatinAmerica
andAsia.J.Bank.Finance23(12),1887–1905(1999)
Rosillo,R.,delaFuente,D.,Brugos,J.:TechnicalanalysisandtheSpanishstockexchange:testingthe
RSI,MACD,momentumandstochasticrulesusingSpanishmarketcompanies.Appl.Econ.45(12),
1541–1550(2013)
Shen,Q.,Szakmary,A.,Sharma,S.:Anexaminationofmomentumstrategiesincommodityfuturesmarkets.
J.FuturesMark.27(3),227–256(2007)
S&PDowJonesIndices:S&PGSCIMethodology.McGrawHillFinancial,NewYork(2016)
Strobel,M.,Auer,B.:Doesthepredictivepowerofvariablemovingaveragerulesvanishovertimeandcan
weexplainsuchtendencies?Int.Rev.Econ.Finance53,168–184(2018)
Swinkels,L.:Momentuminvesting:asurvey.J.AssetManag.5,120–143(2004)
Szakmary, A., Shen, Q., Sharma, S.: Trend-following trading strategies in commodity futures: a re-
examination.J.Bank.Finance34(2),409–426(2010)
Taylor,N.:Theriseandfalloftechnicaltradingrulesuccess.J.Bank.Finance40,286–302(2014)
Taylor,S.:StockindexandpricedynamicsintheUKandtheUS:newevidencefromatradingruleand
statisticalanalysis.Eu.J.Finance6(1),39–69(2000)
Tian,H.,Lai,W.:ThecausesofstageexpansionofWTI/Brentspread.Pet.Sci.16,1493–1505(2019)
Wang,C.,Yu,M.:Tradingactivityandpricereversalsinfuturesmarkets.J.Bank.Finance28(6),1337–1361
(2004)
Wang,S.,Yu,L.,Lai,K.:AnovelhybridAIsystemframeworkforcrudeoilpriceforecasting.In:Shi,Y.,
Xu,W.,Chen,Z.(eds.)DataMin.Knowl.Manag.,pp.233–242.Springer,Berlin,Heidelberg(2004)
Yao,Y.:Momentum,contrarian,andtheJanuaryseasonality.J.Bank.Finance36(10),2757–2769(2012)
Zaremba,A.:Strategiesbasedonmomentumandtermstructureinfinancializedcommoditymarkets.Bus.
Econ.Res.J.7(1),31–46(2016)
Zhang,H.,Auer,B.,Vortelinos,D.:Performanceranking(dis)similaritiesincommoditymarkets.Glob.
FinanceJ.35,115–137(2018)
Publisher’sNote SpringerNatureremainsneutralwithregardtojurisdictionalclaimsinpublishedmaps
andinstitutionalaffiliations.
Benjamin R. Auer is Full Professor of Finance at the Brandenburg University of Technology Cottbus-
Senftenberg, lecturer for financial data management at the University of Leipzig and Research Affil-
iate of the CESifo Group Munich. He has published in top-tier journals such as Management Sci-
ence, the European Journal of Operational Research and the Review of Derivatives Research and has
recentlybeenrankedplace9amongallGerman-speakingresearchersbelowtheageof40intheHandels-
blatt/WirtschaftswocheResearchRanking2020.Hismainareasofexpertiseareinvestmentmanagement,
riskandperformancemeasurementaswellasappliedfinancialeconometrics.
123