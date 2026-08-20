Energy Economics 140 (2024) 107987
ContentslistsavailableatScienceDirect
Energy Economics
journalhomepage:www.elsevier.com/locate/eneeco
Dynamic connectedness in the higher moments between clean energy and
oil prices
Wei Haoa,*, Linh Phamb
aSchoolofEconomicsandFinance,MasseyUniversity,WallaceStreet,MountCook,Wellington6021,NewZealand
bEconomics,BusinessandFinanceDepartment,LakeForestCollegeLakeForest,IL60045,USA
A R T I C L E I N F O A B S T R A C T
JELclassifications: Focusingoncleanenergystocksandoilprices,wefindthatconnectednessbetweentheseassetsnotonlyexistsin
G10 volatility, but also at higher-order moments, such as skewness and kurtosis, which have been largely under
G11 studiedintheexistingliterature.Estimatingtheconnectednessusingintra-daydata,ourinitialstaticanalyses
Q4
suggestthattheconnectednessbetweenthecleanenergyandoilmarketsisheterogenousacrossthemoments
Keywords: andtheshocktransmitter/recipientroleplayedbyeachmarketvariesacrossmoments.Furtherdynamicanalyses
Cleanenergy
indicatethathigher-ordermomentconnectednessisalsotimevaryingandappearstobestrongerduringun-
Oil
certainmarketconditions.Inaddition,weidentifyday-of-the-weekpatternsofhigher-ordermomentconnect-
Higher-ordermomentspillovers
Higher-ordermomentportfoliostrategies ednessduringhighuncertaintyperiods,butthesepatternsappeartobereversedduringlowuncertaintyperiods.
TheemploymentofMarkovswitchingregressionmodelsfurthercorroboratesthemarketuncertaintiesasthe
determinantsofhigher-ordermomentconnectedness.Asanimportantextension,weprovideempiricalevidence
thatincludingcleanenergystocksintheinvestmentportfoliocaneffectivelyhedgeoilpricerisksandconsidering
higher-order moments in constructing investment strategies adds extra value to investors. Our utility-based
hedging strategy and minimum connectedness portfolio can offer higher utility gains and better risk-return
trade-offstothoseinvestorswhoarenotinfinitelyrisk-averse.
1. Introduction (HenriquesandSadorsky,2008;ManagiandOkimoto,2013;Kocaarslan
andSoytas,2019;Yahyaetal.,2021;Hammoudehetal.,2021;Tiwari
Since the early 2000s, the clean energy market has witnessed etal.,2023).Thesepreviousstudieshaveextensivelystudiedtherela-
tremendousgrowththankstoincreasinginterestamonginvestors,pol- tionshipbetweenthecleanenergyandoilmarkets.However,theyhave
icymakers, and the public in reducing climate risks and promoting a focusedondocumentingthecleanenergy-oilpricerelationshipineither
climate-resilienteconomy.Since2004,globalenergytransitioninvest- returnsorvolatilityusingdailydata,whilelittleempiricalevidencehas
menthaswitnessedanincreasingtrendthatremainedstrongthroughout existedontherelationshipathigher-ordermoments.Sinceassetreturns
the most recent crises including the global financial crisis and the typicallydemonstratenon-normal,asymmetric,andfat-taileddistribu-
COVID-19 pandemic. In 2022, global energy transition investment tion intherealworld, itis highly relevant andimportant toconsider
totaled$1.1trillionrepresentinganincreaseof31%comparedtothe higher-order moments of asset return distribution beyond just return
previousyear(BloombergNewEnergyFinance,2023).Despitethefast andvolatility(Bourietal.,2021).Modelingthedynamicconnectedness
growthincleanenergyinvestments,fossilfuelsremainamainsourceof structurebetweencleanenergyandoilpricesathigher-ordermoments
energy.In2021,13.47%ofglobalprimaryenergycamefromrenewable canofferadditionalvaluableinformationtoguideinvestorsandport-
technologies.1 foliomanagersinconstructingoptimalportfolios.This,inturn,facili-
Moreover,asasubstituteforfossilfuelenergy,theperformanceof tatestheinvestmentflowstowardgreeneconomicactivitiesandabetter
cleanenergystockmarketsdependslargelyonmovementinoilprices. transitiontoaclimate-resilienteconomy.Againstthisbackground,the
Theliteraturehasprovidedawiderangeofempiricalevidenceonthe objectives of this paper are as follows. First, we estimate the higher-
relationship between clean energy stock markets and oil prices order moments, specifically, realized volatility, the jump component
* Correspondingauthor.
E-mailaddress:w.hao@massey.ac.nz(W.Hao).
1 https://ourworldindata.org/renewable-energy
https://doi.org/10.1016/j.eneco.2024.107987
Received6November2023;Receivedinrevisedform6October2024;Accepted12October2024
Available online 24 October 2024
0140-9883/© 2024 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ).

W.HaoandL.Pham Energy Economics 140 (2024) 107987
of realized volatility, realized skewness, and realized kurtosis,for the cluster,whileotherrenewablemarketsformanothercluster.Finally,we
cleanenergyandoilmarkets.Inaddition,weexaminethespilloveref- findanincreaseintheconnectednessacrossthemarketsduringthemost
fectsamongcleanenergystockmarketsandoilpricesathigher-order recentCOVID-19andRussia-Ukrainewarcrisis.
moments. Indoing so,we are abletounveilunique characteristicsof Next, using paired sample t-tests, our results confirm that the
thecleanenergy-oillinkagesthatarenotcapturedbythefirstmoments connectednessacrossoilandcleanenergymarketsvariesacrosstrading
(e.g.,volatility,jump,asymmetry,andfattailriskspillovers).Thisal- dayswherethetotalconnectednessindexesarethelowestonMondays
lowsustoquantifythespilloversofspecificrisks,suchasdownsideor andgraduallytrendupwardthroughoutthetradingweek.Thiscanbe
tail risks. Moreover, we identify the roles of financial and macroeco- attributedtotheinitiallackofnewinformationattheopeningofthe
nomicuncertaintyonthehigher-ordermomentspilloversbyidentifying tradingweek.Inaddition,wenoticethatthispatternisstrongerduring
thespilloverpatternsacrosslowandhighuncertaintystates.Finally,we highuncertaintyperiodscomparedtolowuncertaintyperiodssuggest-
derive the economic and financial implications of our results for in- ing that the connectedness across the oil and clean energy markets
vestorsandpolicymakers. significantlydependsuponmarketuncertainty.Tofurtherexplorethis
Toachievetheaboveobjectives,wecollectintra-daydataatthefive- phenomenon, we estimate a Markov-switching model of the total
minutefrequencyonoilpricesandvariouscleanenergysubsectorin- connectedness indexes on various financial and economic uncertainty
dexesfromOctober2010–November2022.Specifically,weconsiderthe variables.Ourresultsindicatethatoilandstockmarketuncertaintyplay
NASDAQOMXBiofuel,Wind,Solar,RenewableEnergyGeneration,and asignificantroleindeterminingtheconnectednessacrossthemarkets,
EnergyEfficiencyIndexes.Basedontheintra-daydata,wecalculatethe while economic policy uncertainty and geopolitical risk play a more
realizedvarianceanditsjumpcomponent,realizedskewnessandreal- modestrole.
izedkurtosisofeachvariablefollowingAndersenandBollerslev(1998), Finally, we present the usefulness of incorporating higher-order
Barndorff-Nielsenetal.(2010)andCorsietal.(2010).Next,westudy moments into asset allocation decisions by considering the perfor-
thelinksbetweenthecleanenergyandoilmarketsusingBalcilaretal.’s manceofalternativehedgingstrategies.Ourresultsshowthathigher-
(2021) time-varying parameter (TVP) extended joint connectedness order moment connectedness across clean energy and oil returns is
model. Then, we analyze the day-of-the week pattern of the connect- significant,andthatincorporatinghigher-ordermomentconnectedness
edness across the markets and employ a Markov-switching regression intoportfoliomanagementstrategiesleadstobetterrisk-returntradeoffs
model to investigate how this connectedness varies across different (asproxiedbyinformationratio)andhigherutilityforcertaingroupsof
states.Finally,wedemonstratetheusefulnessofhigher-ordermoments investorsdependingontheirriskpreferences.
in portfolio management.2 Compared to other approaches, such as Ourpapercontributestotheliteratureinthefollowingways.While
quantile regressions or copulas, our model offers several advantages. previousstudiesfocusonthespillovereffectsinreturnsandvolatility,
First,weutilizehighfrequency,intradaydatatocalculatetherealized we focus on the spillovers across the oil and clean energy markets at
higher-order moments of clean energy and oil returns. While copula higher realized moments. Recent empirical studies have shown that
modelsorquantileanalyses,suchasthequantileconnectednessmodel, connectedness in higher realized moments can reveal meaningful in-
estimate extreme market spillovers using daily data, intraday data formation,particularlywhenassetreturnsarenotnormallydistributed
containsricherinformationaboutmarketmovement(Andersenetal., (Bonatoetal.,2020;Bourietal.,2021;Zhangetal.,2023;Hanifetal.,
2003;Barndorff-Nielsenetal.,2010;Baruníketal.,2015,2017).Spe- 2023). Skewness spillovers capture the spread of return asymmetry
cifically,realizedvolatilitymeasuresthereturnvariationsandskewness acrossmarkets,whilekurtosisspilloverscapturethespreadofextreme
measuresthereturnasymmetries,whilekurtosismeasuresthethickness events or fat tail risks across markets. These higher-order-moment
ofthetailsofthereturndistributions.Byanalyzingthespilloversacross spillovers can influence the stability of financial markets raising the
markets at higher-order moments, we seek to quantify specific risk needtostudythemindetail.
spilloversbetweentheoilandcleanenergymarkets,suchasdownside Our results provide important implications for both investors and
risks or tail risks. In addition, the realized measures are semi- policymakers.First,weprovideempiricalevidencethatincludingclean
nonparametricmeasuresofhighermomentsthatdonotdependonun- energystocksinaninvestmentportfoliocaneffectivelyhedgeoilprice
derlying assumptions about return distributions. Moreover, our risks, and considering higher-order moments of asset returns offers
connectednessmodelallowsustomodeltheconnectednessacrossvar- betterutilityandrisk-returntrade-offtoinvestors.Ourfindingsprovide
iablesinamultivariatesetting.Thishelpsidentifythedependencebe- greater incentives for environmentally conscious investors to pursue
tweenanypairofassetsinthesystemwhilecontrollingforinteractions greeninvestments.Inaddition,wefindthattheconnectednessbetween
withotherassets. thecleanenergyandoilmarketsismomentdependent,andtheshock
Our connectedness model indicates that the total connectedness transmitter and recipient roles played by these markets are heteroge-
indexishighestforrealizedvolatilityanditsjumpcomponent,whichis nous and time varying. Policymakers should consider these unique
approximately three times larger than that of realized skewness and featuresindesigningpoliciestotackleenergychallengesandtopromote
kurtosis.Thisindicatesthatrealizedvolatilityandjumpspilloversare asustainableandgreenerfuture.
the dominant determinants of the interdependence among the clean Theremainderofthepaperproceedsasfollows.Section2presents
energyandoilmarkets.However,ourresultsalsoindicatetherelevance the literature review, while Section 3 describes the data sources and
ofanalyzingthecleanenergy-oilrelationshipinskewnessandkurtosis empiricalmethodology.Section4providestheestimationresults.Sec-
as significant spillovers (i.e., more than 20 %) still exist at these mo- tion 5 discusses the economic and financial implications with the
ments. Moreover, the roles of each market in the system vary widely empiricalevidence,andSection6providesourconclusions.
acrossthemoments.Forexample,oilisashocktransmitterinvolatility
anditsjumpcomponent,butbecomesashockreceiverinskewnessand 2. Literaturereview
kurtosis.Cleanenergysectors,suchasbiofuel,renewableenergygen-
eration,andenergyefficiencysectors,arenetshockreceiversinvola- Ourpaperrelatestotheliteratureregardingtherelationshipbetween
tility, but move toward the shock transmitter roles in skewness and oilpricesandthecleanenergystockmarkets.Earlyworksinthisliter-
kurtosis.Inaddition,weidentifytwoclustersofrelativelyhighlycon- atureemploy vector-autoregressive(VAR)andvector error correction
nectedassetsinthesystem.Specifically,biofuelandoilformtheirown model (VECM) approaches to model the clean energy-oil nexus. For
example,HenriquesandSadorsky(2008)useafour-variableVARmodel
andfindaninsignificantimpactofoilpriceshocksonrenewableenergy
2 WepresentablockdiagraminAppendixDtohelpreadersbetterunder- stock prices. Kumar et al. (2012) extend this framework by adding
standourmethodologies. carbon prices as an additional variable and find evidence of a
2

| W.HaoandL.Pham |     |     |     |     |     |     |     |     |     |     |     | Energy Economics 140 (2024) 107987  |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- |
substitution effect between oil and renewable energy stock prices. we construct high order moments (i.e., realized volatility, jump vola-
Managi and Okimoto (2013) introduce structural breaks to the VAR tility,realizedskewness,andrealizedkurtosis)usingfive-minutedata
modelandconfirmachangingrelationshipbetweenoilandrenewable oncleanenergy stock andoil prices. Usingtherealized high-moment
energypricesbeforeandafterthebreak.Anotherstrandoftheliterature measures, in the second step, we estimate the total, directional, and
employsGARCHmodelstoaccountforthevolatilityclusteringpatterns netconnectednessamongthemarketsusingatime-varyingparameter
ofoilandcleanenergystockprices(Broadstocketal.,2012;Sadorsky, vector autoregression (TVP-VAR) model. In the third step, using
2012;Ahmadetal.,2018;Pham,2019;Lvetal.,2021).Thesestudies regressionanalysis,weexploretherolesofmacroeconomic,financial,
indicatethatcleanenergystocksare,onaverage,weaklycorrelatedwith and environmental variables in determining the spillovers in higher-
oilprices.However,therelationshipbetweencleanenergystocksandoil ordermomentsamongthecleanenergyandoilmarkets.
pricesvariesacrosscleanenergysubsectors.Specifically,Pham(2019)
findsthatbiofuelandenergymanagementstocksarethemostconnected 3.1. Realizedvariance,skewnessandkurtosis
tooilprices,whilewind,geothermal,andfuelcellstocksareamongthe
leastconnectedtooilprices. FollowingAndersenandBollerslev(1998),Barndorff-Nielsenetal.
Onedisadvantageofthestudiesdiscussedaboveisthattheydonot (2010)andBaruníketal.(2015,2017),weuserealizedvarianceasa
capturetherelationshipbetweenoilpricesandcleanenergystocksat measure of clean energy and oil market volatilities. Specifically, the
|     |     |     |     |     |     |     | realizedvariance(RVt |     |     | )isgivenbythefollowingequation: |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ------------------------------- | --- | --- | --- | --- |
thetails,whichmayberelevantforinvestmentdecisionsduringcrisis
| periods,suchasaglobalfinancialcrisis,therecentCOVID-19pandemic, |     |     |     |     |     |     |     | ∑N  |     |     |     |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ortheRussia-Ukrainewar.Usingcopulas,Reboredo(2015)findsatime- RVt = r 2 ,t=1,2,….,T (1)
|                                                            |     |     |     |     |     |     |     |     | s ,t |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
| varyingandsymmetrictaildependencebetweenoilandrenewableen- |     |     |     |     |     |     |     | s=1 |      |     |     |     |     |     |
ergy.Tiwarietal.(2021)employadependence-switchingcopulamodel
toexaminethetaildependencebetweenoilpricesandthestockreturns wheretdenotesatradingdayandsdenotesafive-minuteintervalwithin
ofcleanenergyandtechnologycompanies.Theyfindthatthedepen- thetradingday.rs,t istheintradayreturnduringintervalsobtainedby
dencestructuresacrossthesemarketsvarybetweenpositiveandnega- log-differencingthefive-minuteprices.
tive correlation regimes. Uddin et al. (2019) employ a cross- Next, we calculate the jump component of realized volatility. The
quantilogram approach to study the dependence between renewable realized volatility measure (RVt ) captures the average dispersion of
|     |     |     |     |     |     |     | financial |     | returns during | a   | given trading | day. | In contrast, | the jump |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------------- | --- | ------------- | ---- | ------------ | -------- |
energyandotherassetsanddeterminethatrenewableenergyisposi-
componentofrealizedvolatilitycapturesanydiscontinuityinrealized
tivelyinfluencedbyoilprices,andthisrelationshipdissipatesinthelong
|     |     |     |     |     |     |     | volatility. |     | This has | been shown | to  | influence | market spillovers | signifi- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | ---------- | --- | --------- | ----------------- | -------- |
run.Tiwarietal.(2023)extendthisframeworktoincludeawiderrange
cantly(Bonatoetal.,2020;Gkillasetal.,2022;Hanifetal.,2023).In
| of oil and | clean energy | assets. | They note | heterogeneous |     | dependence |     |     |     |     |     |     |     |     |
| ---------- | ------------ | ------- | --------- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
structuresbetweenthecleanenergyandoilmarkets.Fogliaetal.(2022) thispaper,wefirstdetectjumpsusingthethresholdbi-powervariation
(TBPV)
constructatail-eventdrivennetworkacrosscleanenergyandoilfirms (TBPV) (Corsi et al., 2010). Specifically, the jump statistic J is
t
and find that the connection across the markets is time varying. calculatedasfollows:
| F u rt he rm | o r e , t h e y o b se | r v e a st | r on g d e p | e n de n ce | a c r o s s fi | r m s w i t h in th e |     |     |     |      |         |               |     |     |
| ------------ | ---------------------- | ---------- | ------------ | ----------- | -------------- | --------------------- | --- | --- | --- | ---- | ------- | ------------- | --- | --- |
|              |                        |            |              |             |                |                       |     | √̅  | ̅̅  | (RVt | (cid:0) | )RV (cid:0) 1 |     |     |
sa m e se ct o r ( i. e . , cle a n e n e r gy o r o il) , w h i le th e cr o s s - s ec t o rd e p e n d en c e (TBPV)= [ TBP { Vt t }]
|     |     |     |     |     |     |     | J t |     | T   |     |     |     | 1/2 | (2) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
between oil and clean energy firms is more limited. Although copula (ζ(cid:0) 4+2ζ(cid:0) 2(cid:0) 5)max 1,TQ TBPV (cid:0) 2
|           |                   |       |         |     |           |                |     |     | 1         | 1   |             | t         | t     |      |
| --------- | ----------------- | ----- | ------- | --- | --------- | -------------- | --- | --- | --------- | --- | ----------- | --------- | ----- | ---- |
| models or | quantile analyses | could | capture | the | tail risk | of the oil and |     |     |           |     |             |           |       |      |
|           |                   |       |         |     |           |                |     |     | √̅̅̅̅̅̅̅̅ |     |             | ∑ ⃒ ⃒     | ⃒ ⃒   | ⃒ ⃒  |
|           |                   |       |         |     |           |                |     |     | = 2/π;    | =   | Tζ(cid:0) 3 | N ⃒ ⃒4/3⃒ | ⃒4/3⃒ | ⃒4/3 |
stockmarketnexustosomeextent,theexistingliteratureonlyapplies where ζ 1 TQt 4/ s=1 rt,s rt,s+1 rt,s+2 is the
3
theseapproachesbasedondailyorweeklydata(Xiaoetal.,2018;Zhang realizedtri-powerquarticityandconverginginprobabilitytointegrated
andLiu,2018;ReboredoandUgolini,2016;Sukcharoenetal.,2014).In (TBPV)
|     |     |     |     |     |     |     | quarticity.ThejumpstatisticJ |     |     |     | t   | followsthestandardGaussiandis- |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | ------------------------------ | --- | --- |
thisstudy,wemeasurehigher-momentconnectednessbetweenoiland
tribution.Next,usingtheresultsofthejumptest,wecalculatethejump
cleanenergypricesusingintradaydata.Highfrequencyintradaydata
componentofvolatilityasfollows:
| contain richer | and more | valuable | information |     | about | the asset price |     |     |     |     |     |     |     |     |
| -------------- | -------- | -------- | ----------- | --- | ----- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
{
b e h a v i o r a llowing investors to grasp investment opportunities more (cid:0) (TBPV)>Ω
|                    |     |     |     |     |     |     | =   | RVt | TBPVtifJ | t   | α   |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
| ef f e ct i v e ly | .   |     |     |     |     |     | Jt  |     |          |     |     |     |     | (3) |
0otherwise
Morerecently,theliteraturehasmovedtowardanalyzingtherela-
tionshipbetweenoilandcleanenergystockmarketsusingmultivariate
whereΩα denotesthecriticalvalueofaGaussiandistributionforanα
network models.Thisallowsdocumentingthebi-variaterelationships significantlevel.TBPVtisthethresholdbi-powervariation,whichisan
acrossthemarkets,whilecontrollingforthespilloversfromothersec- estimate for the jump-free component of volatility and is given by:
|     |     |     |     |     |     |     |     |     | ∑ ⃒ | ⃒ ⃒ ⃒ |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
t o r s. Ah m a d ( 20 1 7 ) fi n d s t h at t e c h n o l o g y a nd c le a n e n e r gy s t o c k s a r e = N ⃒ ⃒, ⃒ ⃒ { } { }
|                |                      |            |               |             |               |                          | TBPVt |     | s=2 rt,s(cid:0)1 | rt,s I | |rt,s(cid:0)1 |2≤θi(cid:0)1 | I |rt,s(cid:0)1 | |2≤θi , where | I{•} repre- |
| -------------- | -------------------- | ---------- | ------------- | ----------- | ------------- | ------------------------ | ----- | --- | ---------------- | ------ | --------------------------- | --------------- | ------------- | ----------- |
| n e t em it te | r so f re t u rn s , | w h i le c | r u d e o i l | i s th e ne | t r e ce i ve | r . Fe r r e r e t a l . |       |     |                  |        |                             |                 |               |             |
(2018) study the time-frequency connectedness between renewable sentsanindicatorfunction,rt,sistheintradayreturnseries,andΘisthe
energy stocks and crude oil prices and note similar results. Xia et al. thresholdfunction.
(2019)examinetheextremeconnectednessbetweenenergypricesand Finally, we calculate two additional higher-moment realized mea-
renewableenergystocksanddeterminethatcleanenergystocksarenet sures (i.e., skewness and kurtosis) to capture the asymmetry and tail
risktransmittersunderextremeconditions.Saeedetal.(2021)analyze risksinassetreturns.Therealizedskewness(RSt )canbeexpressedas:
| theextremereturnconnectednessbetweencleananddirtyinvestments |     |     |     |     |     |     |     | √̅̅̅̅∑ |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
N 3
a n d fin d e v id e n ce o f a s t ro n g e r co nn ec te d n es s a t th e t a i ls t h an a t t h e N i= r ,s
|             |                       |              |          |             |              |                        | RSt | =   | 1 t |     |     |     |     | (4) |
| ----------- | --------------------- | ------------ | -------- | ----------- | ------------ | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|             |                       |              |          |             |              |                        |     | RV3 | /2  |     |     |     |     |     |
| m e an o ft | h e r e tu rn d i str | i b u ti o n | s. In th | is s tu d y | , w e e xt e | n d t h e ex is t in g |     |     | t   |     |     |     |     |     |
| literature  | by conducting         | both         | static   | and dynamic | analyses     | on the                 |     |     |     |     |     |     |     |     |
Andtherealizedkurtosisisgivenby:
| connectedness | between | clean | energy | stocks and | oil prices | at higher- |     | ∑   |     |     |     |     |     |     |
| ------------- | ------- | ----- | ------ | ---------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
N
| o rd e r m o | m en t s a n d e x   | a m i n e t  | he h e t e    | rogenous | roles of | oil and clean |     | N   | i= r 4 ,s |     |     |     |     |     |
| ------------ | -------------------- | ------------ | ------------- | -------- | -------- | ------------- | --- | --- | --------- | --- | --- | --- | --- | --- |
|              |                      |              |               |          |          |               | RKt | =   | 1 t       |     |     |     |     | (5) |
| e n e rg y m | a rk et s i n s ho c | k s t r a ns | m iss i o n . |          |          |               |     | RV  | 2         |     |     |     |     |     |
t
3. Datasourcesandempiricalmethodology
Ourempiricalmethodologyconsistsofthreesteps.Inthefirststep,
3

| W.HaoandL.Pham |     |     |     |     |     |     |     |     |     |     |     | Energy Economics 140 (2024) 107987  |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- |
3.2. TVP-VARconnectednessamonghighermoments
|             |     |             |       |                       |     |         | (cid:0)   |     | ) ∑H(cid:0)1 |                |     |     |     |     |     |
| ----------- | --- | ----------- | ----- | --------------------- | --- | ------- | --------- | --- | ------------ | -------------- | --- | --- | --- | --- | --- |
|             |     |             |       |                       |     |         | E ζ (H)ζT | (H) | =            | Ah,t Σ tAT h,t | .   |     |     |     | (9) |
| We estimate |     | an extended | joint | dynamic connectedness |     | network | t         | t   |              |                |     |     |     |     |     |
h=0
basedonthegeneralizedforecasterrordecompositionofatime-varying
|     |     |     |     |     |     |     | Next,thejointconnectednessindexesarecalculatedusinga(cid:0) |     |     |     |     |     |     |     | ro)w-sum |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- |
vectorautoregression(TVP-VAR)modelfollowingBalcilaretal.(2021).
|     |     |     |     |     |     |     | normalization |     | method | based | on the | goodness-of-fit |     | matrix | R2 . Spe- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | ----- | ------ | --------------- | --- | ------ | --------- |
ThisapproachextendstheconnectednessapproachofDieboldandYil-
|            |       |       |                 |                  |      |        | cifically,Sj | nt, | f r omindicatestheimpactofallothervariablesonvariablei |     |     |     |     |     |     |
| ---------- | ----- | ----- | --------------- | ---------------- | ---- | ------ | ------------ | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
| maz (2009, | 2012, | 2014) | that summarizes | the multivariate | risk | trans- |              | i←  | . , t                                                  |     |     |     |     |     |     |
missionswithinlargenetworksofvariablesusingvectorautoregression, andiscalculatedasfollows:
|     |     |     |     |     |     |     |     | [   | ]   |     |     |     |     |     | ]   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
impulse response functions, and generalized forecast error variance [ (cid:0) )⃒
|     |     |     |     |     |     |     |     | ζ2  | (H) (cid:0) | ζ (H)(cid:0) | ζ   | (H ) ⃒ | ,…,u∀=∕i,t+H |     | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | ------ | ------------ | --- | --- |
d e co m po si ti o n s . W h il e th e o ri g i na l c o n n e c t ed n e s s m o d e l w a s a b le t o E i,t E i,t E i ,t u∀=∕i,t+1
|     |     |     |     |     |     |     | Sj nt, f r | om= |     |     | [   | ]   |     |     | (10) |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | ---- |
ca p tu re th e s p il l o ve rs a cr o ss m a n y v ar i a b le s , o n e o f it sd r a w b a c ks i s th a t i← . , t ( )
E ζ2 ,t H
itreliesontheselectionofanarbitraryrollingwindowtoanalyzethe i
| c h an g e i | n t h e s p   | i l l o v e r s  | o v e r t im e . | A n o t h e r d ra w     | b a c k is t ha | t i t d e -  |          | nt,       |                |           |        |                      |          |                |            |
| ------------ | ------------- | ---------------- | ---------------- | ------------------------ | --------------- | ------------ | -------- | --------- | -------------- | --------- | ------ | -------------------- | -------- | -------------- | ---------- |
|              |               |                  |                  |                          |                 |              | Sj       | f r om is | the proportion |           | of the | H-step               | forecast | error variance | of         |
| c o m p o se | s e a c h v a | r i a b l e ’ sf | o r e ca s te r  | ro r v a r i a nc e c on | d i t ion in g  | o n o th e r |          | i← . , t  |                |           |        |                      |          |                |            |
|              |               |                  |                  |                          |                 |              | variable | i that    | can be         | explained | by     | jointly conditioning |          | on             | the future |
variables’
shocks one at a time. To address these issues, Antonakakis shocksofalloftheothervariables. Under thisapproach,nonormali-
| et al. (2020) | propose | using | a time-varying | parameter | vector | autore- |     |     |     |     |     |     |     |     |     |
| ------------- | ------- | ----- | -------------- | --------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
zationisneeded.
gression(TVP-VAR)modelwithintheconnectednessframeworkthatis
Tocalculatethespilloversfromvariableitoalloftheothervariables
notsensitivetothelengthoftherollingwindow,lesspronetooutliers,
inthenetwork,Balcilaretal.(2021)introducemultiplescalingfactors
| and more | appropriate | for | a shorter | time series. Lastrapes | and | Wiesen | (λ),specifically: |     |     |     |     |     |     |     |     |
| -------- | ----------- | --- | --------- | ---------------------- | --- | ------ | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
(2021)developjointconnectednessmetricsthatdecomposeeachvari-
| a b le ’ s f o | r ec a s t e r | r o r va ri | a n c e c o n di | t io n a l up o n a | l l o t h e r v | a ria b le s’ |     | S j n t , f r o m |     |     |     |     |     |     |     |
| -------------- | -------------- | ----------- | ---------------- | ------------------- | --------------- | ------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
|                |                |             |                  |                     |                 |               | λ = | i ← . , t         |     |     |     |     |     |     |     |
sh o c k s j o in tl y . B a l c il ar et a l . ( 20 2 1 ) c o m b i ne th e a p p r o a c h es b y A n to - i g en , f r o m (11)
S ← . ,
| nakakis et                       | al. (2020) | and | Lastrapes | and Wiesen (2021) | to develop | an  |     | i t |     |     |     |     |     |     |     |
| -------------------------------- | ---------- | --- | --------- | ----------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| extendedjointconnectednessmodel. |            |     |           |                   |            |     |     | ∑   |     |     |     |     |     |     |     |
1 n
Inthispaper,wefollowtheextendedjointconnectednessapproach λ= λ (12)
n i i
byBalcilaretal.(2021)toanalyzethetime-varyingspilloversacrossthe
,
cleanenergyandoilmarketsforthefollowingreasons.TheTVP-VAR whereSg en f romisthespilloverfromalloftheothervariablestovariablei
i← . , t
| Extended | Joint Connectedness |     | Model | allows us to | capture the | time- |     |     |     |     |     |     |     |     |     |
| -------- | ------------------- | --- | ----- | ------------ | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
undertheoriginalDieboldandYilmaz(2009,2012,2014)framewo)rk.
v a ry i ng s p il lo v e r s a c r o s s t h e c le an e n e rg y a n d o i l m a r k et s w it h o u t t h e ,
|     |     |     |     |     |     |     | Thus,thespilloversfromvariableitoalloftheothervariables(Sg |     |     |     |     |     |     |     | en t o is |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- |
s p e ci fi ca t io n o f a r b it r a r y r o l lin g w in d o w s, w h i le r e d uc i n g t he s e n si t iv i ty i← . , t
ofourresultstooutliers.Furthermore,theTVP-VARmodelallowspa- calculatedusingthefollowingsteps:
| r a m e te r s  | to c h a n g | e o v e r t   | im e . Th e r e   | f o re , i t a d j u st s | b e tt e r t o p a | ra m e te r |          |              |               |     |     |     |     |     |      |
| --------------- | ------------ | ------------- | ----------------- | ------------------------- | ------------------ | ----------- | -------- | ------------ | ------------- | --- | --- | --- | --- | --- | ---- |
|                 |              |               |                   |                           |                    |             | jSOTij,t | =λ igSOTij,t |               |     |     |     |     |     | (13) |
| c h an g e s .W | e b e l ie   | v e t h e a   | d ju s tm e n t s | o f t h e p a r a m e t   | e rs i n t h e T   | V P -V A R  |          |              |               |     |     |     |     |     |      |
| s e t ti n g a  | n d the m    | o d e l ’ s i | n d e pe n d e n  | c e o f ar bi tr ar y     | r ol l in g wi n   | d o w s i s |          |              |               |     |     |     |     |     |      |
|                 |              |               |                   |                           |                    |             | jSOTii,t | =1(cid:0)    | Sj nt, f r om |     |     |     |     |     | (14) |
a p p l ic ab l e to ou r a n a l y s i s o f h ig h e r - or d er m o m e nt s a c ro ss t h e c le a n i← . , t
| energyandoilmarkets.Thisallowsthemodeltoadjusttothevarious   |     |     |     |     |     |     |          | ∑        |          |     |     |     |     |     |      |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | -------- | -------- | -------- | --- | --- | --- | --- | --- | ---- |
|                                                              |     |     |     |     |     |     | ,        | n        |          |     |     |     |     |     |      |
|                                                              |     |     |     |     |     |     | Sg en t  | o=       | jSOTij,t |     |     |     |     |     | (15) |
| positiveandnegativeshocksintheenergymarketsduringoursampling |     |     |     |     |     |     | i→ . , t | j=1,i=∕j |          |     |     |     |     |     |      |
periods,suchasthe2014–2016oilglut,theCOVID-19financialcrisis,
andtheRussia-Ukrainewar,togetherwithageneralincreaseinpublic where gSOTij,t is the spillover from variable j to variable i under the
awarenessandinvestorpreferencesforrenewableenergy.Finally,since originalDieboldandYilmaz(2009,2012,2014)model.
the model decomposes each variable’s forecast error variance condi- Thejointtotalconnectednessindexisgivenby:
t io na l u p o na l l ot h e r v a r i a b le s ’ sh o c k s j oi nt ly ,th is a ll o w s u s to c a lc u la t e ∑n ∑n
|     |     |     |     |     |     |     |     | 1   | nt, | 1   | nt, |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t h e G F E V D a n d c o n n e c t e d n e s s in d e x e s m o re ac cu r a t el y a s ar g u e d b y jSOIt = Sj f r om== Sj t o (16)
|                      |     |     |     |     |     |     |     | n   | i← . , t | n   | i→ . , t |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --- | --- | --- |
| Balcilaretal.(2021). |     |     |     |     |     |     |     | i=1 |          | i=1 |          |     |     |     |     |
Theextendedjointconnectednessmodelstartswiththeestimationof
Thejointnetconnectednessisgivenby:
thefollowingTVP-VARmodel:
|               |         |        |     |     |     |     | Sj n t,net=Sj | nt, t o  | (cid:0) Sj nt, f r om |     |     |     |     |     | (17) |
| ------------- | ------- | ------ | --- | --- | --- | --- | ------------- | -------- | --------------------- | --- | --- | --- | --- | --- | ---- |
| =Btzt(cid:0)1 | +ut ;ut | ∼N(0,Σ | )   |     |     |     | i, t          | i→ . , t | i← . , t              |     |     |     |     |     |      |
| yt            |         |        | t   |     |     | (6) |               |          |                       |     |     |     |     |     |      |
Thepairwisedirectionalconnectednessbetweenvariablesiandjis
| vec(Bt )=vec(Bt(cid:0)1 |     | )+vt ;vt∼N(0,Rt | )   |     |     |     |          |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
|                         |     |                 |     |     |     | (7) | givenby: |     |     |     |     |     |     |     |     |
whereyt isann×1vectorofvolatility,jumps,skewness,orkurtosis. Sj n t ,net=gSOTji,t (cid:0) gSOTij,t (18)
ij , t
| zt(cid:0)1 isamatrixofthelaggedvaluesofyt |               |               |                    | withtheoptimallaglength  |                    |              |      |                |               |              |                 |             |             |               |                |
| ----------------------------------------- | ------------- | ------------- | ------------------ | ------------------------ | ------------------ | ------------ | ---- | -------------- | ------------- | ------------ | --------------- | ----------- | ----------- | ------------- | -------------- |
|                                           |               |               |                    |                          |                    |              | H    | i g he r j S   | O I t im p    | l ie s a h   | i g h e r l e v | el o f sp   | ill o v e r | s i n t h e   | s y s te m . A |
| d e te r m i n                            | e d b y t he  | B a y e s i a | n in fo r m a t    | i o n c ri te r i o n (B | IC ) . B t i s a m | a tr i x o f |      | ,n             |               |              |                 |             |             |               |                |
|                                           |               |               |                    |                          |                    |              | posi | ti v e S j n t | e t i n d ica | t e s th a t | v a r ia b l e  | i is a n et | s h o c k   | t r an s m it | t e r in t h e |
| th e t i m e -v                           | a r y in g co | e f fi c i e  | n ts th a t fo l l | o w s a r a n d o m w    | a l k p r o c es   | s. u t a n d |      | i, t           |               |              |                 |             |             |               |                |
denotetheerrorterms,whileΣ network.ApositiveSj n t ,netimpliesthattheamountofshockstransmitted
| vt  |     |     | t andRt | denotetheircorresponding |     |     |     |     |     | ,   |     |     |     |     |     |
| --- | --- | --- | ------- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ij t
variance-covariancematrices.FollowingBalcilaretal.(2021),theTVP- fromvariablejtovariableiislargerthanthatintheoppositedirection.
VARmodelisestimatedusingaKalmanfilterwithforgettingfactors.
Next,weusetheWoldrepresentationtheoremtotransformtheTVP-
VARmodelintoatime-varyingparametervectormovingaverage(TVP- 3.3. Datasources,descriptivestatisticsandpreliminaryanalyses
|              |     | ∑               |       | ∑                       |           |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | --------------- | ----- | ----------------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VMA)model:zt | =   | p Bitzt(cid:0)i | +ut = | ∞ Ajtut(cid:0)j,whereA0 | =In.TheH- |     |     |     |     |     |     |     |     |     |     |
|              |     | i=1             |       | j=0                     |           |     |     |     |     |     |     |     |     |     |     |
Toinvestigatethespilloversacrosscleanenergystockandoilprices
stepforecasterroriscomputedas:
) at higher moments, we collect intraday data at the five-minute fre-
∑H(cid:0)1 quency.Specifically,weusetheWTIcrudeoilspotpriceasaproxyfor
| ζ (H)=yt+H | (cid:0) E(yt+H | |yt ,yt(cid:0)1 | ,… = |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | -------------- | --------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t Ah,tut+H(cid:0)h (8) oilpricesandtheNASDAQOMXBiofuel,Wind,Solar,RenewableEn-
h=0
ergyGeneration,andEnergyEfficiencyIndexesasproxiesfordifferent
Theforecasterrorcovariancematrixofζ (H)isgivenby: sectorsofthecleanenergystockmarket.Wefocusonindividualsectors
t
4

| W.HaoandL.Pham |     |     |     |     |     |     | Energy Economics 140 (2024) 107987  |     |
| -------------- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- |
ofthecleanenergymarketinsteadofusinganaggregatestockindexfor volatility in Fig. 1.1 reveal that turbulent time periods are associated
the entire clean energy stock market to capture the heterogeneous withsharpincreaseintherealizedvolatilityforboththecleanenergy
relationship between clean energy subsectors and oil prices (Pham, andoilmarkets.Forexample,dailyrealizedvolatilityforthecleanen-
2019).WecollectintradaycleanenergystockpricedatafromBloom- ergy sectors and the oil market appears to be high during the 2011
bergandintradayoilpricedatafromFirstRateData.Ourdatasetspans Europeandebtcrisis,between2015and2016duringtheoilpricecrash
from October 13, 2010-November 30, 2022. The beginning of the caused by the reduction in oil production and low demand for oil in
samplingperiodisbasedontheavailabilityofthedata. developingcountries,andbetween2020and2022duringtheCovid-19
InTable1,weprovidesummarystatisticsofrealizedvolatility,the inducedmarketcrashandtheRussia-Ukrainewar.Consistentevidence
jumpcomponent,realizedskewness,andrealizedkurtosiscalculatedfor is observed in the plots of jumps as shown in Fig. 1.2 in which the
stocksinfivecleanenergysectorsandtheoilprices.Itisevidentthatoil dramaticsurgesin2020andearly2022areofparticularinterest.The
prices experience the greatest daily realized volatility and jumps bigjumpscoincidewiththeRussia-SaudiArabiaoilpricewarduringthe
(0.00583and0.00047,respectively)followedbythebiofuelsectorin Covid-19pandemicin2020andthebeginningofRussia-UkraineWarin
thecleanenergymarket(0.00056,0.00039,respectively).Otherclean 2022.Fluctuationsarealsoobservedinrealizedskewness(Fig.1.3)and
energysectorshaverelativelysmalldailyvolatilityandjumpsranging kurtosis (Fig. 1.4) throughout our sample period. In particular, sub-
between0.00015and0.00006,0.00003and0.00001,respectively.On stantialvariationsinpriceasymmetryandtailrisksaredocumentedfor
average, the biofuel, solar, and oil markets are negatively skewed, allcleanenergysectorsandoilpricesaround2013and2017,possibly
whereas the wind, renewable energy generation, and the energy effi- attributable to the global oil supply interruptions and oversupplies in
ciencymarketsarepositivelyskewed.Wefindrealizedkurtosisranges these periods. Taken together, we find highly consistent time series
from 5.32 to 9.67, indicating the return distributions for stocks in all variations across the clean energy sectors and the oil market. Such
clean energy sectors and oil prices have fatter tails compared with preliminary evidence points to the existence of high correlations be-
normaldistribution.TheJarque-Beratestsprovideadditionalevidence tweenthecleanenergyandoilmarketsathigh-ordermoments.
tothepresenceofasymmetryandtailrisksforcleanenergystockandoil
prices.Infact,theJarque-Beratestsrejectthenormaldistributionhy- 4. Empiricalresults
pothesesforallofthehigh-ordermoments.TheADFtestsandLjung-Box
tests,whichtestfortheunitrootandautocorrelation,furtherconfirm 4.1. Statichigher-ordermomentconnectednessbetweencleanenergy
| thevalidityofoursampleforfurtheranalysis. |     |     |     |     | stockandoilprices |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | ----------------- | --- | --- | --- |
Toillustratethetimeseriestrendofthehigh-ordermomentsinour
sample period, we present the plots of realized volatility, jumps, the In this section, we examine the high-order moment connectedness
realized skewness, and realized kurtosis in Fig. 1. Plots of realized between clean energy stock and oil prices. We present the static
Table1
Summarystatistics.
|     | Mean | Std.Dev. | Skewness | Kurtosis | Jarque-Bera | ADF | Q   | Q2  |
| --- | ---- | -------- | -------- | -------- | ----------- | --- | --- | --- |
Table1.1.Realizedvolatility
BIO 0.00056 0.01452 39.11* 1538.51* 298,934,587.0* (cid:0) 22.37* 0.03204 0.03903
SOLAR 0.00015 0.0003 9.87* 140.21* 2,430,098.3* (cid:0) 9.44* 16,419.1* 7482.2*
|      |         |        |        |          | 1.093e+09* | (cid:0) |       |          |
| ---- | ------- | ------ | ------ | -------- | ---------- | ------- | ----- | -------- |
| WIND | 0.00004 | 0.0004 | 53.81* | 2940.46* |            | 20.88*  | 3.894 | 0.009755 |
(cid:0)
REG 0.00006 0.0009 38.41* 1493.36* 281,630,996.7* 21.84* 0.3128 0.04146
ENEF 0.00006 0.0002 13.92* 265.67* 8,823,238.1* (cid:0) 10.22* 11,871.1* 3806.7*
Oil 0.00583 0.1496 32.52* 1104.28* 153,904,333.6* (cid:0) 19.77* 2110.8* 1221.6*
Table1.2.Jumpcomponentofrealizedvolatility
BIO 0.00039 0.01452 39.14* 1540.07* 299,541,732.5* (cid:0) 22.45* 0.04689 0.03896
(cid:0)
SOLAR 0.00001 0.00004 21.85* 632.20* 50,305,744.9* 20.50* 287.2* 655.4*
|      |         |         |        |          | 1.151e+09* | (cid:0) |        |         |
| ---- | ------- | ------- | ------ | -------- | ---------- | ------- | ------ | ------- |
| WIND | 0.00001 | 0.00042 | 54.86* | 3017.84* |            | 22.31*  | 0.1155 | 0.01006 |
REG 0.00003 0.00088 38.84* 1516.15* 290,304,820.0* (cid:0) 22.44* 0.05834 0.04019
ENEF 0.00000 0.00002 23.79* 839.87* 88,852,125.8* (cid:0) 19.95* 18.31 0.2605
(cid:0)
Oil 0.00047 0.01175 31.74* 1088.94* 149,638,138.9* 16.43* 1576.5* 735.0*
Table1.3.RealizedSkewness
|       | (cid:0) |      | (cid:0) |        |           | (cid:0)        |       |       |
| ----- | ------- | ---- | ------- | ------ | --------- | -------------- | ----- | ----- |
| BIO   | 0.05    | 0.93 | 0.63*   | 13.47* | 14,074.4* | 22.02*         | 23.83 | 55.3* |
|       | (cid:0) |      | (cid:0) |        |           | (cid:0)        |       |       |
| SOLAR | 0.02    | 1.09 | 0.13*   | 7.15*  | 2188.5*   | 22.54*         | 28.31 | 71.9* |
| WIND  | 0.01    | 1.54 | 0.09*   | 4.38*  | 244.8*    | (cid:0) 21.50* | 27.82 | 28.77 |
| REG   | 0.02    | 1.04 | 0.29*   | 9.52*  | 5423.5*   | (cid:0) 21.85* | 36.4  | 48.9* |
(cid:0)
| ENEF | 0.01 | 0.95 | 0.13* | 6.55* | 1598.4* | 23.58* | 34.5 | 12.78 |
| ---- | ---- | ---- | ----- | ----- | ------- | ------ | ---- | ----- |
Oil (cid:0) 0.01 1.15 (cid:0) 0.14* 8.65* 4043.8* (cid:0) 23.11* 27.36 150.2*
Table1.4.RealizedKurtosis
(cid:0)
| BIO | 5.32 | 4.1 | 7.65* | 93.94* | 1,075,553.3* | 6.43* | 76.2* | 45.1* |
| --- | ---- | --- | ----- | ------ | ------------ | ----- | ----- | ----- |
SOLAR 6.07 4.11 6.22* 73.03* 639,654.9* (cid:0) 5.77* 237.6* 31.25
WIND 9.67 5.81 3.67* 26.32* 75,574.4* (cid:0) 4.83* 88.3* 39.9
(cid:0)
| REG | 5.91 | 4.15 | 7.73* | 108.09* | 1,426,800.2* | 5.61* | 117.1* | 6.035 |
| --- | ---- | ---- | ----- | ------- | ------------ | ----- | ------ | ----- |
ENEF 5.43 3.11 6.81* 116.80* 1,661,098.7* (cid:0) 4.98* 85.4* 5.186
Oil 6.06 4.74 6.53* 75.28* 682,177.4* (cid:0) 5.88* 274.5* 180.0*
Notes:No.ofobservations:3035.*indicatessignificanceatthe5%level.Jarque-BerastandsfortheJarque-Beratestforthenullhypothesisofanormaldistribution.
ADFindicatestheunitroottestofDickeyandFuller(1979)thatchecksthenullhypothesisoftheunitrootfortheresiduals.QandQ2signifytheLjung-Boxtestsonthe
originalseriesanditssquaredterms.BIO,SOLAR,WIND,REG,ENEFrepresenttheNASDAQOMXBiofuel,Wind,Solar,RenewableEnergyGeneration,EnergyEf-
ficiencyIndexes.Oilsignifiestheoilmarket.Thehigher-ordermomentsofallvariablesareestimatedusingintra-dayfive-minutereturndatawherereturnsare
calculatedbylog-differencingtheintradayprices.
5

W.HaoandL.Pham Energy Economics 140 (2024) 107987
connectedness results in Table 2. In each sub-table, the numbers re- volatility(Table2.1),73.30forjumps(Table2.2),29.72forskewness
ported in the top six rows reflect the forecast error variance (in per- (Table2.3),and20.14forkurtosis(Table2.4).Ourresultsindicatethat
centageterms)explainedbythevariablesshowninthecorresponding cleanenergysectorsandtheoilmarketarehighlyconnectedatallhigh-
columns.Total connectednessreceivedby eachmarket fromall other ordermoments.Furthermore,realizedvolatilityandjumpspilloversare
marketsisreportedinthelastcolumn“FROM,”whiletotalconnected- the dominant determinants of the interdependence among the clean
ness transmittedbyeach markettoall othermarkets inthesystemis energyandoilmarkets.However,analyzingthespilloversinskewness
reportedintherow“TO.”Therow“Inc.Own”presentsthetotalspill- andkurtosisstilladdsvaluableinformationaboutthedynamicsofthe
oversfromeachmarkettoallmarketsincludingitself.Therow“NET” cleanenergyandoilmarketssincesignificantspillovers(morethan20
captures the net connectedness where positive (negative) values indi- %)stillexistatthesehigher-ordermoments.
cate a net shock transmitter (receiver). “TCI” denotes the total Table 2 also reveals the major shock transmitters and receivers at
connectedness indexreflecting the overall degree ofconnectednessin eachmoment.Forvolatilityspillovereffects(Table2.1),theoilmarket
thesystem. isthelargestshocktransmitterwherethe“TO”and“NET”connected-
Considering the overall connectedness, TCI is 73.84 for realized nessindexesare150.69and113.32,whichissubstantiallyhigherthan
Fig.1. Timeseriesplotsofrealizedvolatility,jumps,realizedskewnessandrealizedkurtosis.
Fig.1.1Realizedvolatility.
Fig.1.2Jumpcomponentofrealizedvolatility.
Fig.1.3Realizedskewness.
Fig.1.4RealizedKurtosis.
Note:Thefigureplotsthedailytimeseriesofthehigher-ordermomentsofcleanandoilreturns.BIO,SOLAR,WIND,REG,ENEFrepresenttheNASDAQOMXBiofuel,
Wind,Solar,RenewableEnergyGeneration,EnergyEfficiencyIndexes.Oilsignifiestheoilmarket.Thehigher-ordermomentsofallvariablesareestimatedusing
intra-dayfive-minutereturndatawherereturnsarecalculatedbylog-differencingtheintradayprices.
6

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.1.(continued).
7

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.1.(continued).
8

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.1.(continued).
theothermarkets.Allcleanenergysectorsarethenetshockreceivers cleanenergymarketsdrivethepatternofshockspilloversintailevents
with the biofuel sector being the largest receiver. For jump spillover thatarecapturedbytheskewnessandkurtosisspillovermatrices.
effects (Table 2.2), the oil and biofuel markets are the largest shock Moreover, Table 2 suggests that the own-market spillover effects
transmittersinthesystem.The“TO”connectednessindexis101.97for (shown diagonally in the tables) are stronger than the cross-market
the oil market and 115.42 for the biofuel market, while the “NET” spillover effects. In other words, shocks within each market account
connectednessindexis28.31fortheoilmarketand50.52forthebiofuel forthelargestshareofforecasterrorvariance.Theown-marketspillover
market.Solar,wind,andrenewableenergygenerationsectorsarenet effectsalsoincreasewiththeincreaseofmomentorders(fromTable2.1
shockreceiverswithNETconnectednessindexesrangingfrom(cid:0) 29.44 to Table 2.4) consistent with the findings of Zhang et al. (2023) and
to(cid:0) 4.09.Notethattheoilmarketplaysadifferentandlesssignificant Fogliaetal.(2022)thateachmarketisprimarilyaffectedbyitsinternal
role in determining the spillover effects in skewness and kurtosis shocks.
(Tables2.3and2.4).Forexample,oilbecomesanetreceiverofshocksin Next, we discuss the spillover effects between the oil market and
thethirdandfourthmoments,whilebiofuelandtherenewableenergy eachcleanenergysector.Table2suggestsasignificantroleoftheoil
generationsectorsbecomethenetshocktransmitter.Ourresultsexpand market in determining the behavior of the clean energy markets in
theresultsofpreviousresearchthatfindstheshockreceiverroleofoil realized volatility and its jump component. Specifically, in these two
prices in the first moment in a system of oil, clean energy, and tech- moments, the spillovers from the oil to the clean energy markets are
nologystockmarkets(Pham,2019;Nasreenetal.,2020).Wearguethat typicallymorethan17%,rangingfrom17.43to37.39%.Alternatively,
therelationshipsbetweenoilpricesandcleanenergystocksaremoment thevolatilityandjumpspilloversfromthecleanenergymarketstothe
dependent.Specifically,whileoilshocksareimportantindetermining oilmarketaremorelimited.Cleanenergymarketstypicallyaccountfor
the spillovers across the oil and clean energy markets in volatilities, lessthan15%ofshocksinoil’srealizedvolatilityandjumpcomponent
9

| W.HaoandL.Pham |     |     |     |     |     | Energy Economics 140 (2024) 107987  |     |
| -------------- | --- | --- | --- | --- | --- | ----------------------------------- | --- |
Table2
Averagehigher-ordermomentconnectednessacrosscleanenergystockandoilprices.
Table2.1:Realizedvolatility
|         | BIO   | SOLAR | WIND  | REG   | ENEF  | Oil    | FROM  |
| ------- | ----- | ----- | ----- | ----- | ----- | ------ | ----- |
| BIO     | 23.89 | 7.72  | 9.65  | 21.48 | 9.18  | 28.08  | 76.11 |
| SOLAR   | 7.07  | 11.42 | 12.97 | 11.37 | 25.27 | 31.91  | 88.58 |
| WIND    | 6.41  | 13.3  | 14.38 | 10.51 | 18.01 | 37.39  | 85.62 |
| REG     | 16.09 | 10.97 | 7.57  | 32.87 | 10.47 | 22.03  | 67.13 |
| ENEF    | 8.36  | 22.77 | 14.57 | 11.24 | 11.78 | 31.28  | 88.22 |
| Oil     | 2.91  | 4.94  | 15.2  | 4.08  | 10.23 | 62.64  | 37.36 |
| TO      | 40.84 | 59.7  | 59.97 | 58.68 | 73.16 | 150.69 | TCI   |
| Inc.Own | 64.72 | 71.12 | 74.35 | 91.55 | 84.94 | 213.32 | 73.84 |
NET (cid:0) 35.28 (cid:0) 28.88 (cid:0) 25.65 (cid:0) 8.45 (cid:0) 15.06 113.32
Table2.2:Jumpcomponentofrealizedvolatility
|         | BIO    | SOLAR | WIND  | REG   | ENEF  | Oil    | FROM  |
| ------- | ------ | ----- | ----- | ----- | ----- | ------ | ----- |
| BIO     | 35.09  | 9.03  | 9.98  | 16.62 | 7.33  | 21.94  | 64.91 |
| SOLAR   | 19.37  | 22.83 | 12.78 | 12.53 | 12.53 | 19.97  | 77.17 |
| WIND    | 25.52  | 11.5  | 20.17 | 11.46 | 10.2  | 21.14  | 79.83 |
| REG     | 22.03  | 10.44 | 10.02 | 32.69 | 7.4   | 17.43  | 67.31 |
| ENEF    | 18.42  | 14.09 | 12.33 | 10.58 | 23.09 | 21.5   | 76.91 |
| Oil     | 30.08  | 10.77 | 10.76 | 12.03 | 10.01 | 26.34  | 73.66 |
| TO      | 115.42 | 55.83 | 55.87 | 63.22 | 47.47 | 101.97 | TCI   |
| Inc.Own | 150.52 | 78.66 | 76.04 | 95.91 | 70.56 | 128.31 | 73.30 |
NET 50.52 (cid:0) 21.34 (cid:0) 23.96 (cid:0) 4.09 (cid:0) 29.44 28.31
Table2.3:Realizedskewness
|         | BIO    | SOLAR   | WIND    | REG    | ENEF  | Oil     | FROM  |
| ------- | ------ | ------- | ------- | ------ | ----- | ------- | ----- |
| BIO     | 86.28  | 2.19    | 2.01    | 4.17   | 4.01  | 1.34    | 13.72 |
| SOLAR   | 2.4    | 58.6    | 2.36    | 22.64  | 12.51 | 1.49    | 41.4  |
| WIND    | 2.46   | 2.61    | 74.1    | 15.18  | 4.64  | 1.01    | 25.9  |
| REG     | 4.23   | 20.84   | 12.08   | 45.57  | 16.1  | 1.18    | 54.43 |
| ENEF    | 3.86   | 10.62   | 3.72    | 14.98  | 64.6  | 2.22    | 35.4  |
| Oil     | 1.54   | 1.42    | 0.87    | 1.31   | 2.34  | 92.52   | 7.48  |
| TO      | 14.48  | 37.7    | 21.04   | 58.28  | 39.6  | 7.24    | TCI   |
| Inc.Own | 100.76 | 96.3    | 95.14   | 103.85 | 104.2 | 99.77   | 29.72 |
|         |        | (cid:0) | (cid:0) |        |       | (cid:0) |       |
| NET     | 0.76   | 3.7     | 4.86    | 3.85   | 4.2   | 0.23    |       |
Table2.4:Realizedkurtosis
|         | BIO    | SOLAR        | WIND         | REG    | ENEF   | Oil         | FROM  |
| ------- | ------ | ------------ | ------------ | ------ | ------ | ----------- | ----- |
| BIO     | 91.22  | 1.41         | 1.68         | 2.43   | 2.59   | 0.67        | 8.78  |
| SOLAR   | 1.38   | 76.26        | 1.64         | 12.51  | 7.01   | 1.2         | 23.74 |
| WIND    | 1.49   | 1.83         | 82.31        | 10.34  | 3.07   | 0.96        | 17.69 |
| REG     | 2.26   | 12.21        | 8.84         | 62.41  | 12.66  | 1.63        | 37.59 |
| ENEF    | 2.67   | 6.5          | 2.6          | 12.16  | 73.78  | 2.29        | 26.22 |
| Oil     | 1.01   | 1.09         | 0.92         | 1.72   | 2.12   | 93.15       | 6.85  |
| TO      | 8.81   | 23.04        | 15.68        | 39.15  | 27.44  | 6.75        | TCI   |
| Inc.Own | 100.02 | 99.31        | 97.98        | 101.56 | 101.23 | 99.9        | 20.14 |
| NET     | 0.02   | (cid:0) 0.69 | (cid:0) 2.02 | 1.56   | 1.23   | (cid:0) 0.1 |       |
Note:Eachcellcapturesthespilloversfromthecolumnvariabletotherowvariable.ThecolumnFROMcapturesthespilloverfromalloftheothervariablestotherow
variable.TherowTOcapturesthespilloverfromthecolumnvariabletoalloftheothervariables.TherowInc.Owncapturestheamountofspilloverfromthecolumn
variabletoallofthevariablesincludingitself.TherowNETcapturesthenetspilloverwherepositive(negative)valuesindicatenetshocktransmitters(receivers).The
totalconnectednessindex(TCI)islistedatthebottomrightcornerofthetable.BIO,SOLAR,WIND,REG,ENEFrepresenttheNASDAQOMXBiofuel,Wind,Solar,
RenewableEnergyGeneration,EnergyEfficiencyIndexes.Oilsignifiestheoilmarket.Thehigher-ordermomentsofallvariablesareestimatedusingintra-dayfive-
minutereturndatawherereturnsarecalculatedbylog-differencingtheintradayprices.
with the exception of the biofuel market. Specifically, biofuel jumps order moments. For example, we find significant spillovers from the
account for 30.08 % of the forecast error variance in oil jumps. One renewableenergygenerationsectortothesolar,wind,andenergyef-
ficiencysectors(>10%)inrealizedskewnessandkurtosis.Thishigh-
explanationisthatbiofuelandoilareconsideredclosesubstitutes.Thus,
a jump in biofuel prices can lead to a significant jump in oil prices. lightstherelevanceofanalyzingthespilloversacrossthecleanenergy
Moreover,wefindasmallerspillovereffectbetweenoilpricesandclean andoilmarketsathigher-ordermoments.
energypricesatthethirdandfourthmoments. To better visualize the connectedness network between the clean
Finally,Table2alsoallowsustoidentifytheconnectednesspattern energysectorsandtheoilmarket,wepresenttheconnectednessgraphin
across the clean energy sectors. Our results suggest that although the Fig. 2. As shown by the pairwise directional spillover measures, oil
total connectedness index declines as we move from lower to higher- marketsandcleanenergysectorsarehighlyconnectedinvolatilityand
ordermoments,significantpairwisespilloversstillexistatthehigher- jumps, but less connected in skewness and kurtosis. Consistent with
10

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.2. Networkconnectedness.
Fig.2.1Realizedvolatility.
Fig.2.2Jumpcomponentofrealizedvolatility.
Fig.2.3Realizedskewness.
Fig.2.4Realizedkurtosis.
Note:Red(blue)nodesindicatenetshocktransmitters(receivers).Thesizeofthenodesindicatesthemagnitudeofthenetspilloverindexes.Thedirectionofthe
arrowscapturesthedirectionofspilloversbetweenanytwovariablesandthearrows’thicknesscapturethestrengthofthepairwisespillovers.BIO,SOLAR,WIND,
REG,andENEFrepresenttheNASDAQOMXBiofuel,Wind,Solar,RenewableEnergyGeneration,andEnergyEfficiencyIndexes.Oilsignifiestheoilmarket.The
higher-order moments of all of the variables are estimated using intra-day five-minute return data where returns are calculated by log-differencing the
intradayprices.
Table2,thenetshocktransmitterandrecipientrolesplayedbythese and2017,droptorelativelylowlevelsin2018and2019,peakin2020,
marketsvaryacrossmomentsandaremorepronouncedinvolatilityand and then remain at relatively high levels afterward. The peaks of
jump spillovers, but weaker in skewness and kurtosis spillovers. Our connectednessin2020coincidewiththeRussia-SaudiArabiaoilprice
findingsindicatethatwhenalowprobabilityeventoccurs,connected- war during the Covid-19 pandemic. Together with other turbulent
nessbetweentheoilandcleanenergymarketsstillpersists.However, events,suchastheRussia-Ukrainewar,Figs.3.1and3.2indicateahigh
different markets may experience different reactions (Zhang et al., levelofconnectednessamongthemarketssince2020.InFigs.3.3and
2023). 3.4, the TCIs of skewness and kurtosis demonstrate similar trends
throughout the sample period, but with relatively stronger variation
documentedforthekurtosisTCI.Forbothskewnessandkurtosis,TCIs
4.2. Time-varyinghigher-ordermomentsconnectednessacrossoiland arecomparativelyhighduringthe2011Europeandebtcrisis,the2015
cleanenergystocks oilpricecrash,the2020Russia-SaudiArabiaoilpricewarduringthe
Covid-19pandemic,andthe2022Russia-Ukrainewar.Overall,ourre-
Wenextexaminethetimedynamicsofconnectednessbyplottingthe sultsindicatethattotalconnectednessindexesathigh-ordermoments
TCIandNETconnectednessindexesoveroursampleperiodandpresent aretimevaryingandtendtostrengthenwithinstableoilmarketsand
theplotsinFigs.3and4.InFigs.3.1and3.2,theTCIsshowgenerally worsening economic conditions. The finding of intensified connected-
consistent trends for volatility and jumps. Specifically, the total ness during turbulent periods is consistent with previous studies
connectednessindexesforvolatilityandjumpfluctuatebetween2010
11

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.3. Totalconnectednessindexes.
Fig.3.1Realizedvolatility.
Fig.3.2Jumpcomponentofrealizedvolatility.
Fig.3.3Realizedskewness.
Fig.3.4Realizedkurtosis.
Note:Thefigurepresentsthetotalconnectednessindexesamongcleanenergyandoilmarketsinhigher-momentsusingtheTVP-VARJointConnectednessapproach.
includingReboredo(2015),ReboredoandUgolini(2016),Naeemetal. responsetohighlyvolatileoilpricesduringthisperiod.InFig.4.2,the
(2020)andZhangetal.(2023).AssuggestedbyBakasandTriantafyllou most noticeable changes of jump connectedness are identified in the
(2018) and Bouri et al. (2021), macroeconomic uncertainties can biofuel sector, the energy efficiency sector, and the oil market. The
translate into rising uncertainty about future aggregate demand and strongpositivenetconnectednessindexessuggestthatthesemarketsact
supply.Giventhatcommoditypricesarehighlysensitivetoaggregate asthebiggestnetshocktransmittersmostofthetime.Solarandwind
demandandsupplyconditions,increasesintheuncertaintysurrounding sectorsremaintheprimarynetshockreceiversduringthesampleperiod,
the macroeconomy can lead to higher volatility in commodity prices. whereastherenewableenergygenerationsectorshowssmallswitches
Thiseffectspillsovertootherenergycommoditiesandtheirvolatilities. between these two roles. For the net connectedness in skewness as
Ourresultscomplementthesepreviousfindingsbyprovidingadditional showninFig.4.3,renewableenergygenerationandenergyefficiency
evidence regarding the stronger spillover effects among higher-order sectorsbecomethemajornetshocktransmitters,whilesolarandwind
momentsduringhigheruncertaintyperiods. arethemajornetshockreceivers.Biofuelandoilmarketsexhibitcycle
We conduct similar time-series analyses using net connectedness changes between positive and negative values in net skewness
indexes and present the plots in Fig. 4. Different from the total connectedness. In Fig. 4.4, small constant fluctuations in net kurtosis
connectednessindexinFig.3,thenetdirectionalmeasureofconnect- connectednessarefoundforallmarketsindicatingweakpredictability
ednessprovidesusefulinformationaboutthetimevaryingroleplayed of net kurtosis connectedness among these markets when low proba-
by each market as net shock transmitter or receiver over our sample bility events occur. For all high-order moments, the time varying net
period.Specifically,apositive(negative)valueinFig.4indicatesanet connectednessofthecleanenergyandoilmarkets,togetherwiththeir
transmitter(receiver)roleinconnectednessofthecorrespondingmarket timevaryingnetshocktransmitter/receiverroles,aregenerallyconsis-
to (from) all of the other markets. Overall, we find that all net tentwiththepreviousfindingsdocumentedinTable2andFigs.2and3.
connectednessindexesdisplaysubstantialvariationsovertimewiththe Insummary,ourconnectednessresultsdemonstratelargevariations
largestnetconnectednessdocumentedduringtheperiodswithunstable in the spillovers across clean energy and the oil markets at different
marketconditionsconsistentwiththefindingsinFig.3.InFig.4.1,the moments.Oilisthedominantshocktransmitterinvolatilityandjumps.
oilmarketisthemainnetshocktransmitterofvolatilityconnectedness However,itsrolefluctuatesinskewnessandkurtosis.Mostcleanenergy
mostofthetime,whilethefivecleanenergysectorsareprimarilynet markets arenet shockreceivers involatilitythroughout oursampling
shock recipients. In the 2020 Russia-Saudi Arabia oil price war and period. However, they are more likely to switch to the net shock
Covid-19 pandemic period, biofuel and renewable energy generation transmitterrolesathighermoments(i.e.,skewnessandkurtosis).This
sectorsexperienceasharpincreaseintheirnetconnectednessindexes reflectsinvestors’interestsinalternativeenergyunderlowprobability
andbecomenetshocktransmittersforashortperiodoftime.Thisre- events. Furthermore, we find that the fluctuations of the markets be-
flects an increase in public interest toward alternative energy in tween the shock transmitter and receiver roles decrease at higher
12

W.HaoandL.Pham Energy Economics 140 (2024) 107987
moments.Thisindicatesthatthespilloversacrossthecleanenergyand between the clean energy and oil markets across weekdays. To allow
oil markets are less predictable when low probability events occur. meaningfulcomparison,wematchfivenon-missingweekdaysfromeach
Finally,ourresultssuggestthesignificantroleofthesecondmoments(i. same week and then calculate mean TCI on each weekday. This
e., volatility and its jump component) in explaining the overall inter- matching strategy enables us to compare connectedness variations
dependence among the clean energy and oil markets. However, an acrossweekdaystoidentifyday-of-the-weekpatternsholdingtheeco-
analysisofthespilloversatthethirdandfourthmomentsisstillvaluable nomicconditionsduringtheweekconstant.Wetestthestatisticalsig-
assignificantspilloversstillexistamongthemarketsatthesemoments. nificance of daily differences in TCI between two weekdays using a
Our results also highlight the unpredictability of spillovers at higher- pairedsamplet-test.
ordermoments,andempiricalanalysesthatfocusonthefirstandsec- AsshowninFig.5,PanelA,theconnectednesspatternsinrealized
ondmomentsmaynotbeabletocapturethisunpredictability. volatility, skewness, and kurtosis between clean energy stock and oil
prices demonstrate similar overall trends from Mondays to Fridays.
4.3. Doesday-of-the-weekeffectexistforhigher-ordermoments Specifically,thetotalconnectednessindex(TCI)appearstobethelowest
connectednessacrossoilandcleanenergystocks? onMondaysandgraduallytrendsupwardacrosstherestoftheweek-
days.Forconnectednessinvolatilityjump,therearechangingdynamics
Intheearliersections,wehavestudiedthetimedynamicsofhigh- fromTuesdaystoFridays.TheTCIforvolatilityjumpstartsrisingfrom
ordermomentconnectednessovertheentiresampleperiod.Toinves- thetradingopeningonMondaysandpeaksonTuesdays,butdropson
tigatethetimevaryingbehaviorofconnectednessfurther,westudyTCI Wednesdaysandthesechangesarestatisticallysignificantat1%and5
Fig.4. Netconnectednessindexes.
Fig.4.1Realizedvolatility.
Fig.4.2Jumpcomponentofrealizedvolatility.
Fig.4.3Realizedskewness.
Fig.4.4Realizedkurtosis.
Note:Thefigurepresentsthetime-varyingnetconnectednessofcleanenergyandoilmarketsinhighermoments.Positive(negative)valuesindicateamarketisanet
shocktransmitter(receiver).BIO,SOLAR,WIND,REG,andENEFstandfortheNASDAQOMXBiofuel,Wind,Solar,RenewableEnergyGeneration,andEnergy
EfficiencyIndexes.Oilsignifiestheoilmarket.
13

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.4.(continued).
14

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.4.(continued).
15

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.4.(continued).
%, respectively. The degree of connectedness intensifies again on indexes including the daily CBOE Oil Volatility Index (OVX), the VIX
ThursdaysandremainstowardtheclosingoftradingonFridays.Since Volatility Index (VIX), Economic Policy Uncertainty (EPU), and the
the jump component of volatility better captures the discontinuity in Geopolitical Risk Index (GPR). Specifically, if the value of the daily
realizedvolatility,thefluctuationsintheconnectednesspatternreflect OVX/VIX/EPU/GPRindexisaboveitsmedianvalue,thedayisclassi-
thechangesinthemarketreactionsduetotheinfluxofnewsinforma- fiedashighOVX/VIX/EPU/GPR.Otherwise,thedayisclassifiedaslow
tionaroundthemiddleoftheweek. OVX/VIX/EPU/GPR.Then,withineachsubsample,wematchthefive
Overall, our results are complementary to the well documented non-missingweekdaysfromeachsameweekandcalculatethemeanTCI
Mondayeffectexistingamongstockreturnsinwhichstockreturnshave oneachweekdayforcomparison.WepresenttheplotsinFigs.5.2–5.5.
beenfoundtobesignificantlyloweronMondayscomparedwithother As shown in Fig. 5.2, during high OVX periods, TCI for realized
days within the week (Cross, 1973; French, 1980). Our findings volatilityhasanupwardtrendandTCIforvolatilityjumpsexhibitsmore
corroboratethatvariationexistsinthetimingofreleasingnewsinfor- variablepatternsacrossthefiveweekdays.Thesepatternsareconsistent
mationacrossweekdays.Inparticular,thenumberofpublicnewsan- withtheoverallconnectednesspatternsreportedinFig.5.1.However,
nouncementshasbeenfoundtobelowonMondays,butincreasesfrom the connectedness at higher moments (i.e., skewness and kurtosis)
Tuesdays to Thursdays and then tapers off on Fridays (Mitchell and weakens considerably from Wednesdays during high OVX periods.
Mulherin,1994).The relativelylowconnectednessbetweentheclean Intriguingly, the connectedness patterns for all high-order moments
energystockmarketandtheoilmarketonMondayscanbeattributedto (exceptjumps)appeartobereversedinlowOVXperiodscomparedwith
theinitiallackofnewsinformationinthemarketsattheopeningofthe highOVXperiodsindicatingthetimedynamicsofTCIishighlydepen-
trading week. However, TCI strengthens as more news information is dentuponmarketuncertainty.
being released, incorporated, and accumulated throughout the rest of As illustrated in Figs. 5.3–5.5, the day-of-the-week connectedness
thetradingweek. patternsduringhighVIX/EPU/GPRperiodspersistconsistentlyingen-
Toexploretheday-of-the-weekconnectednesspatternsfurther,we eral. With theexceptionof theconnectednessof jumps duringa high
partition our full sample periods into high uncertainty vs. low uncer- GPRperiod,totalconnectednessindexesarealltrendingupwardacross
tainty periods based on the median values of the daily uncertainty the five weekdays, consistent with the overall connectedness patterns
16

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.5. Day-of-the-weekpatternsinconnectednessbetweenoilpricesandgreenstocks.(Forinterpretationofthereferencestocolourinthisfigurelegend,thereader
isreferredtothewebversionofthisarticle.)
Fig.5.1TCI.
Fig.5.2TCIinhighOVXvslowOVXperiods.
Fig.5.3TCIinhighVIXvslowVIXperiods.
Fig.5.4TCIinhighEPUvslowEPUperiods.
Fig.5.5TCIinhighGPRvslowGPRperiods.
17

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.5.(continued).
presentedinFig.5.1.Theseresultscanbeexplainedbythefactthatthe andSanati,2018).Ourfindingssuggestthatthismomentumeffectalso
accumulationofnewsinformationisfasterandsteadierduringahigh exists in the higher moment connectedness. During turbulent periods
uncertainty tradingweek,whichincreasesthetotalconnectednessin- with high uncertainty, investors underreact to the negative news
dexesthroughouttheweekdays.Inmostcases,theconnectednessforall releasedinthemarketscausinginformationtobeincorporatedintothe
high-order moments demonstrates opposite patterns during low VIX/ pricesofenergycommoditiesslowlyandgradually.Theinformationis
EPU/GPR periodscompared withhigh VIX/EPU/GPRperiods.During accumulatedandspilledoveracrosstheenergymarketsthroughoutthe
low VIX/EPU/GPR periods, total connectedness indexes for all high- trading days within a week leading to the upward day-of-the-week
order moments are generally trending downward across the five connectedness patterns at the higher-order moments. The reversed
weekdays. day-of-the-week connectedness patterns hold true when investors
Viewed collectively,the opposite patternsdocumented during low overreacttopositiveinformationduringthelowuncertaintyperiods.
vs.highuncertaintyperiodshaveinterestingimplications.Wefindthat
connectedness tends to trend upward throughout the trading days 4.4. Uncertaintyandhigher-ordermomentconnectedness
within a week during turbulent periods with high uncertainty. This
pattern is reversed during low uncertainty periods. It has been well Thusfar,wehaveestablishedthehigh-ordermomentconnectedness
establishedintheliteraturethatthestockmarkettendstooverreactto betweenthecleanenergyandoilmarketsandhavealsostudiedthetime
goodnewsandunderreacttobadnews.Whenrespondingtonegative dynamicsoftheirconnectedness.Inaddition,ouranalysisinSection4.3
information, investors initially demonstrate underreaction causing in- implies that the relationship between uncertainty factors and higher-
formationtobeincorporatedintostockpricesslowlyandpricecontin- order moment connectedness among oil and clean energy stocks is
uation(orreturndrift)afterthenewsshocks(Hongetal.,2000;Frank state-dependent. In this section, we further identify how the
18

| W.HaoandL.Pham |     |     |     |     |     |     |     |     |     |     |     | Energy Economics 140 (2024) 107987  |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- |
Table3
Uncertaintyandthehigher-momentconnectednessbetweenoilandcleanenergystocks.
|     | (1) |     | (2) |     | (3) |     | (4) | (5) |     | (6) |     | (7) | (8) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Variable: RV RV Jump Jump Skewness Skewness Kurtosis Kurtosis
TCI
| State | Low |     | High |     | Low |     | High | Low |     | High |     | Low | High |     |
| ----- | --- | --- | ---- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- | ---- | --- |
connectedness connectedness connectedness connectedness connectedness connectedness connectedness connectedness
OVX (cid:0) 10.6130*** (cid:0) 3.8000*** 10.6105*** (cid:0) 5.4398*** (cid:0) 2.5723*** (cid:0) 0.9197*** (cid:0) 5.1498*** 2.6595***
[1.2807] [0.3646] [1.6381] [0.3780] [0.2499] [0.3150] [0.2945] [0.6530]
|     |     |     |     |     | (cid:0) |     | (cid:0) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
VIX 8.4199*** 4.0047*** 7.4474*** 7.1421*** 4.3765*** 9.7466*** 4.7509*** 6.3735***
[1.3514] [0.5247] [0.7685] [0.7194] [0.3090] [0.5355] [0.3122] [0.8281]
EPU 3.1715*** 1.1541*** 1.1966** (cid:0) 1.9603*** 0.9774*** 0.9148*** 1.3244*** (cid:0) 0.8608*
[0.6880] [0.2070] [0.4770] [0.2093] [0.1256] [0.1648] [0.1772] [0.4807]
|     |     |     | (cid:0) |     | (cid:0) |     |     | (cid:0) |     |     |     | (cid:0) |     |     |
| --- | --- | --- | ------- | --- | ------- | --- | --- | ------- | --- | --- | --- | ------- | --- | --- |
GPR 0.4954 1.5230*** 2.3129*** 0.0867 0.6587*** 0.2816 0.0336 1.0830*
[0.5177] [0.2193] [0.6115] [0.2431] [0.1678] [0.3096] [0.1879] [0.6545]
Constant 48.8595*** 82.9451*** 46.8327*** 139.9058*** 19.9081*** 3.7467* 11.8620*** 2.2690
[5.1641] [1.7582] [5.4109] [1.5307] [1.2150] [1.9550] [1.5314] [4.0276]
ln(sigma) 1.8432*** 1.4487*** 2.1826*** 1.2632*** 0.8887*** 1.3606*** 0.9819*** 2.2169***
[0.0354] [0.0196] [0.0169] [0.0199] [0.0223] [0.0290] [0.0213] [0.0291]
| N   | 3056 |     | 3056 |     | 3056 |     | 3056 | 3056 |     | 3056 |     | 3056 | 3056 |     |
| --- | ---- | --- | ---- | --- | ---- | --- | ---- | ---- | --- | ---- | --- | ---- | ---- | --- |
Note:RobustSEinbrackets.***p<0.01,**p<0.05,*p<0.1.OVX,VIX,EPU,GPRstandsfortheCBOEoilvolatilityindex,CBOEVIXindex,EconomicPolicy
Uncertaintyindex,andgeopoliticalriskindex.Allregressionsincludedummiesforthe2014–2016oilglut,theCOVID-19financialcrisis,andtheUkraine-Russiawar
period.
connectednessamongoilandcleanenergystocksisrelatedtoeconomic, states.Notethatthemagnitudeofthecoefficientsoneconomicpolicy
political,andfinancialmarketuncertaintyacrosshighandlowuncer- uncertainty is smaller (in absolute value) than those on oil and stock
taintystates.Tothisend,weestimatethefollowingMarkovswitching marketvolatility.Finally,theeffectofgeopoliticalriskonhigher-order
regressionmodel3: momentconnectednessacrosscleanenergyandthestockmarketsisless
( ) statistically significant. Altogether, our results suggest that market
jSOIt =μ s,t +α s,tUNCt +βXt +ϵ s,t ;ϵ s,t ∼iid 0,σ2 s,t (19) volatility,suchasoilandstockmarketvolatility,arethemaindriversof
higher-ordermomentconnectednessamongcleanenergystockandoil
wherejSOItdenotesthetotaljointspilloverindexforvolatility,thejump
prices.Changesinthemarketvolatilityhaveastronganddirectimpact
component of volatility, skewness, and kurtosis. UNCt is a vector of onthehigher-ordermomentconnectednessbetweentheoilandclean
uncertaintyindexesthatincludestheCBOEoilvolatilityindex(OVX), energymarkets.Incontrast,economicpolicyuncertaintyandgeopolit-
the CBOE VIX index (VIX), the Economic Policy Uncertainty index ical risk play a more modest role. Despite the fact that economic un-
(EPU), and the geopolitical risk index (GPR). s denotes the state certainty has been found to have strong impact on a single financial
(st ∈[1,2]), and the effects of uncertainty factors can be switched be- market(Guetal.,2021;ZhangandYan,2020),ourresultssuggestthatit
tweenthestateswiththemeanμ andvariance,σ2 .Xtisasetofdummy has a relatively weaker and indirect impact on cross-market connect-
|     |     |     | s,t |     | s,t |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2014–2015 edness. Economic uncertainty can be transmitted to the oil and clean
| variables | to indicate | the |     | oil glut, | the | COVID-19 | financial |     |     |     |     |     |     |     |
| --------- | ----------- | --- | --- | --------- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
crisis,andtheRussia-Ukrainewar.ϵ energy markets by affecting the market volatility and financial in-
s,t denotestheerrorterm.
|     |     |     |     |     |     |     |     | vestors’ sentiment | (Lyu | et al., | 2021; | Bakas and | Triantafyllou, | 2018; |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | ---- | ------- | ----- | --------- | -------------- | ----- |
Table3presentstheestimationresults.Theoddnumberedcolumns
Wangetal.,2023),bothofwhicharecapturedinthemeasuresofmarket
indicatetheeffectofuncertaintyvariablesontheconnectednessacross
cleanenergyandoilpricesduringlowconnectednessperiods,whilethe volatilitysuchasOVXandVIX,resulting inastrengthenedimpactof
financialmarketvolatilityonoilandcleanenergyconnectedness.4
| even numbered |     | columns | indicate | the results | for | high connectedness |     |     |     |     |     |     |     |     |
| ------------- | --- | ------- | -------- | ----------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
periods.Wefindthatoilpricevolatility(proxiedbytheOVXindex)is
associatedwithadecreaseinconnectednessamongoilandcleanenergy 5. Economicandfinancialimplications
| stocks in | most cases. | This | suggests | that | clean energy | stocks | tend to |     |     |     |     |     |     |     |
| --------- | ----------- | ---- | -------- | ---- | ------------ | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
decouplefrom oilpricesinresponse toincreasingoil volatility.How- 5.1. Utility-basedhedgeratios
ever,ourresultsalsoshowseveralexceptionstothisdecouplingpattern.
|     |     |     |     |     |     |     |     | In previous | sections, | we  | demonstrate | that there | is a | significant |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | ----------- | ---------- | ---- | ----------- |
Forexample,jumpconnectednessandkurtosisconnectednessincrease
amountofspilloversamongthecleanenergyandoilmarketsathigher-
| in response                       | to  | increasing | oil | volatility            | during | the low | and high |                |         |              |            |              |             |              |
| --------------------------------- | --- | ---------- | --- | --------------------- | ------ | ------- | -------- | -------------- | ------- | ------------ | ---------- | ------------ | ----------- | ------------ |
|                                   |     |            |     |                       |        |         |          | order moments. | This    | highlights   | the        | relevance of | considering | these        |
| connectednessstates,respectively. |     |            |     | Inaddition,anincrease |        |         | intheVIX |                |         |              |            |              |             |              |
|                                   |     |            |     |                       |        |         |          | higher-order   | moments | in designing | investment | strategies.  |             | In this sec- |
index(aproxyforstockmarketvolatility)isassociatedwithanincrease
intheconnectednessacrossallthehigher-ordermomentsexceptforthe tion,wediscusstheusefulnessofincorporatinghigher-ordermomentsin
jumpcomponentofvolatilities.Moreover,anincreaseintheeconomic portfolioallocationdecisionsintermsofhedgingeffectiveness,utility,
uncertaintyindexisassociatedwithanincreaseinconnectednessexcept andtheinformationratio.FollowingAlexanderandBarbosa(2008),we
forthejumpandkurtosisconnectednessduringthehighconnectedness analyzehowalongpositioninoilpricescanbehedgedbyashortpo-
sitionincleanenergystocks.Letrj,tbetherealizedreturnforassetj(j=
Oil,Clean)ondayt.Thereturnonahedgedportfolio(p)isgivenby:
|                                                               |     |     |     |     |     |     |     | rp,t =rOil,t (cid:0) β | rClean,t |     |     |     |     | (20) |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | -------- | --- | --- | --- | --- | ---- |
| 3 TheMarkovSwitchingmodelassumesthatthetimeseriescanswitchbe- |     |     |     |     |     |     |     |                        | t        |     |     |     |     |      |
tweendifferentregimes.TVP-VARmodelextendsthestandardVARframework
whereβ istheoptimalhedgeratiofordayt,whichischosentomaxi-
| byallowingtheparameterstochangeovertime.Bothmodelsintendtocapture |     |     |     |     |     |     |     | t                                |     |     |     |                             |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --------------------------- | --- | --- |
|                                                                   |     |     |     |     |     |     |     | mizeexpectedutility.Thevaluesofβ |     |     |     | dependonthefunctionalformof |     |     |
the dynamic changes in time series data. In this paper, we conduct a state- t
| dependent | connectedness | analysis. |     | In such a | framework, | the connectedness |     |     |     |     |     |     |     |     |
| --------- | ------------- | --------- | --- | --------- | ---------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
measuresamongoilandcleanenergystockscanvaryacrossdifferentstates,
whichprovidesinsightsastohowconnectionsamongvariableschangeduring
differenteconomicconditions. 4 VIXisalsowell-knownasafeargaugeindicator.
19

| W.HaoandL.Pham |     |     |     |     |     | Energy Economics 140 (2024) 107987  |     |
| -------------- | --- | --- | --- | --- | --- | ----------------------------------- | --- |
Fig.6. Optimalhedgeratio(Minimumvarianceportfolio).
Note:BIO,SOLAR,WIND,REG,andENEFrepresenttheNASDAQOMXBiofuel,Wind,Solar,RenewableEnergyGeneration,andEnergyEfficiencyIndexes.
| theutilityfunctionandhedgers’riskaversion. |     |     |     | energymarkets. |     |     |     |
| ------------------------------------------ | --- | --- | --- | -------------- | --- | --- | --- |
Under the minimum variance hedging strategy, the objective is to Notethattheminimumvariancestrategyassumesthatreturnsare
minimize risk regardless as to the return and investors are subject to normallydistributedandinvestorsareinfinitelyriskaverse(Cotterand
infiniteriskaversion.Theoptimalhedgeratiois: Hanly, 2015). Thus, this strategy may produce suboptimal asset allo-
|     |     |     |     | cations if | either of the assumptions | are violated. | Following Patton |
| --- | --- | --- | --- | ---------- | ------------------------- | ------------- | ---------------- |
β = CovOil,Clean,t
t (21) (2004),weadoptautility-basedhedgingmeasureasanalternative.The
VarClean,t objectiveistochooseahedgeratiotomaximizeinvestors’utility,which
|                      |                                              |              |              | depends upon | their risk preference. | To accommodate | the effect of         |
| -------------------- | -------------------------------------------- | ------------ | ------------ | ------------ | ---------------------- | -------------- | --------------------- |
| whereCovOil,Clean,t  | denotestherealizedcovariancebetweentheoiland |              |              |              |                        |                |                       |
|                      |                                              |              |              | higher-order | moments on expected    | utility, we    | adopt the exponential |
| clean energy markets | and VarClean,t denotes                       | the variance | of the clean |              |                        |                |                       |
20

| W.HaoandL.Pham |     |     | Energy Economics 140 (2024) 107987  |     |     |
| -------------- | --- | --- | ----------------------------------- | --- | --- |
Optimalhedgeratio(Exponentialutility-λ =10).
Fig.7.
Note:BIO,SOLAR,WIND,REG,andENEFrepresenttheNASDAQOMXBiofuel,Wind,Solar,RenewableEnergyGeneration,andEnergyEfficiencyIndexes.
utilityfunction:
|                                |           | 1 1                                               | 1                |     |      |
| ------------------------------ | --------- | ------------------------------------------------- | ---------------- | --- | ---- |
|                                | E[Wt      | ](cid:0) Var(Wt )+ Skew(Wt                        | )(cid:0) Kurt(Wt | )   | (23) |
| U(Wt )= (cid:0) λe (cid:0)Wt/λ | (22)      | 2λ 6λ2                                            | 24λ3             |     |      |
|                                | whereE[Wt | ]istheexpectedreturn.VAR(Wt),Skew(Wt),andKurt(Wt) |                  |     |      |
whereWt denotesinvestors’wealthandλdenotestheirriskaversion.5
Weconsidertwoalternativevaluesforλ,specifically,λ=10andλ=5, are the variance, skewness, and kurtosis of the portfolio and are esti-
toaccountfordifferentlevelsofriskaversion.Theoptimalhedgingratio mated based on realized higher-order moments using five-minute
foraninvestorwithexponentialutilitycanbeestimatedbychoosingβ
t
thatmaximizesthefollowingexpression:
5 Higherλcorrespondstohigherriskaversion.
21

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.8. Optimalhedgeratio(Exponentialutilityλ =5).
Note:BIO,SOLAR,WIND,REG,andENEFrepresenttheNASDAQOMXBiofuel,Wind,Solar,RenewableEnergyGeneration,andEnergyEfficiencyIndexes.
22

| W.HaoandL.Pham |     |     |     |     |     |     | Energy Economics 140 (2024) 107987  |     |
| -------------- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- |
Table4 withariskaversionparameterof10,andExponentialUtilitywithariskaversion
Portfolioperformancemetrics. parameteroffive.Mean,SD,andHEaretheaveragehedgeratio,thestandard
deviationofhedgeratios,andhedgingeffectiveness.Therows“Exponential(λ =
Portfoliostrategies
|     |     |     |     |     | 10)”and“Exponential(λ |     | =5)”presenttheutilityvaluesof | theexponential |
| --- | --- | --- | --- | --- | --------------------- | --- | ----------------------------- | -------------- |
Portfolio Unhedged Minimum Exponential Exponential utilityfunctionundereachinvestmentstrategyforriskaversionparametersof
|     |     | Variance | Utility(λ=10) | Utility(λ=5) |     |     |     |     |
| --- | --- | -------- | ------------- | ------------ | --- | --- | --- | --- |
10andfive.Therow“InformationRatio”presentstheinformationratio,which
(OIL,BIO) istheratiobetweenportfolioreturnsandthestandarddeviation.BIO,SOLAR,
|     | –   |     |     | (cid:0) |     |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- |
Mean 0.3126 0.0167 0.0848 WIND, REG, and ENEF represent the NASDAQ OMX Biofuel, Wind, Solar,
| SD  | –   | 1.0904 | 5.2755 | 2.9977 |     |     |     |     |
| --- | --- | ------ | ------ | ------ | --- | --- | --- | --- |
RenewableEnergyGeneration,andEnergyEfficiencyIndexes.
| HE  | –   | 0.3462 | (cid:0) 2.2995 | (cid:0) 0.7617 |     |     |     |     |
| --- | --- | ------ | -------------- | -------------- | --- | --- | --- | --- |
Exponential
| (lambda= |        | (cid:0) |        | (cid:0) |     |     |     |     |
| -------- | ------ | ------- | ------ | ------- | --- | --- | --- | --- |
|          | 0.0014 | 0.2616  | 0.4053 | 0.2108  |     |     |     |     |
10)
Table5
Ex p o ne n t ia l
= (cid:0) 0.0006 (cid:0) 2.0170 (cid:0) 6.3080 0.6700 Expectedutilitygainunderalternativehedgingstrategies.
| ( la m b d a | 5)  |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Information
Hedgingstrategies
| Ratio | 0.4098 | 0.5024 | 3.674 | 3.516 |     |     |     |     |
| ----- | ------ | ------ | ----- | ----- | --- | --- | --- | --- |
λ
|             |        |                |         |                | Portfolio   |     | MinimumVariance | ExponentialUtility |
| ----------- | ------ | -------------- | ------- | -------------- | ----------- | --- | --------------- | ------------------ |
|             |        |                |         |                | (OIL,BIO)   | 10  | (cid:0) 0.2630  | 0.4039             |
| (OIL,SOLAR) |        |                |         |                |             | 5   | (cid:0) 2.0163  | 0.6706             |
| Mean        | –      | 0.3743         | 0.0377  | (cid:0) 0.0076 |             |     | (cid:0)         |                    |
|             |        |                |         |                | (OIL,SOLAR) | 10  | 0.0018          | 0.7490             |
| SD          | –      | 0.6314         | 5.5974  | 3.1454         |             | 5   | (cid:0) 0.0234  | 1.2865             |
|             | –      | ¡0.1352        | (cid:0) | (cid:0)        |             |     |                 |                    |
| HE          |        |                | 3.0513  | 1.0303         | (OIL,WIND)  | 10  | (cid:0) 0.1724  | 0.1463             |
| Exponential |        |                |         |                |             |     | (cid:0)         |                    |
|             |        |                |         |                |             | 5   | 1.2851          | 0.1198             |
| (lambda=    | 0.0014 | (cid:0) 0.0003 | 0.7505  | 0.0955         |             |     | (cid:0)         |                    |
|             |        |                |         |                | (OIL,REG)   | 10  | 0.0211          | 0.2430             |
| 10)         |        |                |         |                |             | 5   | (cid:0) 0.1814  | 0.3363             |
Ex p o ne n t ia l (cid:0) 0.0006 (cid:0) 0.0240 (cid:0) 5.9270 1.2858 (OIL,ENEF) 1 0 (cid:0) 1 . 9 2 2 2 0 . 7 0 6 7
| ( la m b d a = | 5)  |     |     |     |     |     | (cid:0)      |             |
| -------------- | --- | --- | --- | --- | --- | --- | ------------ | ----------- |
|                |     |     |     |     |     | 5   | 1 4 . 7 7 35 | 1 . 2 9 0 4 |
Information
|       |        |        |       |       | Note: The | table presents the | expected utility gain | of the minimum variance |
| ----- | ------ | ------ | ----- | ----- | --------- | ------------------ | --------------------- | ----------------------- |
| Ratio | 0.4098 | 0.5568 | 3.717 | 3.858 |           |                    |                       |                         |
hedgeratiosandtheexponentialutilityhedgeratios,comparedtotheutilityof
anunhedgedpositioninoil,acrossdifferentriskaversionparameters(λ).BIO,
(OIL,WIND) SOLAR, WIND, REG, and ENEF represent the NASDAQ OMX Biofuel, Wind,
Mean – 0.4598 (cid:0) 0.0072 (cid:0) 0.0159 Solar,RenewableEnergyGeneration,andEnergyEfficiencyIndexes.
–
| SD  |     | 1.1611 | 4.4808         | 2.3353         |     |     |     |     |
| --- | --- | ------ | -------------- | -------------- | --- | --- | --- | --- |
| HE  | –   | 0.0230 | (cid:0) 1.1298 | (cid:0) 0.2919 |     |     |     |     |
Exponential
| (lambda= |        | (cid:0) |        | (cid:0) |     |     |     |     |
| -------- | ------ | ------- | ------ | ------- | --- | --- | --- | --- |
|          | 0.0014 | 0.1710  | 0.1477 | 0.1843  |     |     |     |     |
10)
Ex p o ne n t ia l
|                | (cid:0) 0.0006 | (cid:0) 1.2857 | (cid:0) 9.3510 | 0.1191 | Table6 |     |     |     |
| -------------- | -------------- | -------------- | -------------- | ------ | ------ | --- | --- | --- |
| ( la m b d a = | 5)             |                |                |        |        |     |     |     |
Minimumconnectednessportfolioperformanceindicators.
Information
| Ratio | 0.4098 | 0.4777 | 3.989 | 3.411 |     |     |     |     |
| ----- | ------ | ------ | ----- | ----- | --- | --- | --- | --- |
Table6.1.Portfolioreturnsummarystatistics.
|     |     |     |     |     | Portfolio |     | Mean   | SDof Info.   |
| --- | --- | --- | --- | --- | --------- | --- | ------ | ------------ |
|     |     |     |     |     |           |     | Return | Return Ratio |
(OIL,REG)
| Mean | –   | 0.6875 | (cid:0) 0.0702 | (cid:0) 0.0767 |                         |     |         |                 |
| ---- | --- | ------ | -------------- | -------------- | ----------------------- | --- | ------- | --------------- |
|      |     |        |                |                | Oil(Unhedged)           |     | 0.00200 | 0.06990 0.02864 |
| SD   | –   | 0.9476 | 5.0539         | 2.7102         |                         |     |         |                 |
|      |     |        |                |                | MCP(RealizedVolatility) |     | 0.00228 | 0.05967 0.03823 |
HE – 0.0664 (cid:0) 0.7489 (cid:0) 0.2099 MCP(Jumpcomponentofrealized
|             |        |                |        |                |                       |     | 0.00113 | 0.03101 0.03643 |
| ----------- | ------ | -------------- | ------ | -------------- | --------------------- | --- | ------- | --------------- |
| Exponential |        |                |        |                | volatility)           |     |         |                 |
| (lambda=    | 0.0014 | (cid:0) 0.0196 | 0.2445 | (cid:0) 0.0804 |                       |     |         |                 |
|             |        |                |        |                | MCP(RealizedSkewness) |     | 0.00064 | 0.02017 0.03192 |
10)
|                    |           |         |         |        | MCP(RealizedKurtosis) |     | 0.00064 | 0.01962 0.03264 |
| ------------------ | --------- | ------- | ------- | ------ | --------------------- | --- | ------- | --------------- |
| Ex p o ne n t ia l | (cid:0)   | (cid:0) | (cid:0) |        |                       |     |         |                 |
| ( la m b d a =     | 5) 0.0006 | 0.1820  | 5.8670  | 0.3357 |                       |     |         |                 |
Information
Ratio 0.4098 0.4996 4.137 3.156 Table6.2Averageweightsofoilandhedgingeffectiveness
|     |     |     |     |     | Portfolio |     | Mean SDof     | Hedging          |
| --- | --- | --- | --- | --- | --------- | --- | ------------- | ---------------- |
|     |     |     |     |     |           |     | weight weight | effectiveness(%) |
(OIL,ENEF)
Mean – 0.6953 0.0067 (cid:0) 0.0637 Oil(Unhedged) 1.00 0.00 0.00
–
SD 1.9684 5.4068 3.0163 MCP(RealizedVolatility) 0.37 0.29 0.27
HE – 0.2254 (cid:0) 1.2337 (cid:0) 0.4124 MCP(Jumpcomponentof
|             |     |         |     |     |                     |     | 0.14 0.15 | 0.80 |
| ----------- | --- | ------- | --- | --- | ------------------- | --- | --------- | ---- |
| Exponential |     |         |     |     | realizedvolatility) |     |           |      |
| (lambda=    |     | (cid:0) |     |     |                     |     |           |      |
0.0014 1.9207 0.7081 0.5044 MCP(RealizedSkewness) 0.22 0.05 0.92
|     |     |     |     |     | MCP(RealizedKurtosis) |     | 0.20 0.04 | 0.92 |
| --- | --- | --- | --- | --- | --------------------- | --- | --------- | ---- |
10)
Ex p o ne n t ia l
(cid:0) 0.0006 (cid:0) 14.7741 (cid:0) 0.1941 1.2898 Note:Thetablepresentstheperformanceindicatorsofanunhedgedpositionin
| ( la m b d a = | 5)  |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
oilprice,andtheminimumconnectednessportfolioinrealizedvolatility,the
Information
Ratio 0.4098 0.2266 3.809 3.147 jumpcomponentofvolatility,realizedskewness,andrealizedkurtosis.Table6.1
presentstheportfolioreturns,thestandarddeviationofreturns,andtheinfor-
| Note: Each panel | presents | the performance | metrics for | a portfolio of a long |     |     |     |     |
| ---------------- | -------- | --------------- | ----------- | --------------------- | --- | --- | --- | --- |
mationratios.Table6.2reportstheaverageweightofoilineachportfolioand
positioninoilandashortpositioninthecleanenergymarkets.Fourinvestment
thehedgingeffectivenessprovidedbyeachportfolioagainstvariationsinoil
| scenarios are | considered: | Unhedged, Minimum | Variance, | Exponential Utility |     |     |     |     |
| ------------- | ----------- | ----------------- | --------- | ------------------- | --- | --- | --- | --- |
prices.
23

W.HaoandL.Pham Energy Economics 140 (2024) 107987
intradaydata.6 aversionandhigher-ordermomentmovementsofassetreturns,ourre-
Figs. 6–8 plot the time-varying optimal hedge ratios under the sults illustrate the usefulness of considering higher-order moments in
minimum variance and the exponential utility-based strategies from assetallocationstrategies.
2010to2022.Overall,wefindthattheexponentialutilitybasedhedge Intermsoftheutilityderivedfromeachhedgingstrategy,wefind
ratiosaremorevariablethantheminimumvariancehedgeratios.This thatinvestorscanbenefitfromswitchingtoautility-basedhedge.For
canbeexplainedbythefactthathigher-ordermomentsareincludedin example,theutilityfromtheexponentialutilityfunctionforaninvestor
λ=10
the exponential utility function while they are not included in the with a risk averse parameter of is 0.4053 in the (OIL, BIO)
minimumvariancestrategy.Sincethesehigher-ordermomentscapture portfolio.Similarly,investorswithasmallerriskaversion(λ =5)also
additionalrisks,suchasasymmetryrisks(measuredbyskewness)and derive larger utility from the exponential utility portfolio (0.6700).
fat tail risks (measured by kurtosis), this requires more frequent ad- Thesearesignificantlyhigherthantheutilityderivedfromtheunhedged
justments of the optimal hedge ratios. Under the minimum variance portfolio(0.0014and(cid:0) 0.0006forλ=10andλ=5,respectively),or
hedgingstrategy(Fig.6),wefindthebiggestadjustmentinthehedging fromtheminimumvarianceportfolio((cid:0) 0.2616and(cid:0) 2.0170forλ=10
portfoliosduringtheCovid-19pandemicperiodandRussia-SaudiAra- andλ=5,respectively).Similarobservationscanbemadeforotheroil-
biaoilpricewarin2020.Theadjustmentisthemostpronouncedforthe cleanenergystockpairs.
Renewable Energy Generation stocks with the optimal hedge ratio Table 5 presents the expected utility gain of the portfolios under
increasedsignificantlyto70%.Thehedgeratiosincreaseto40%and alternativehedgingstrategiescomparedtoanunhedgedpositioninoil.
30 %, respectively, for Biofuel and Wind stocks and 20 % and 15 %, The table reports that the minimum variance portfolios yield smaller
respectively, for Solar and Energy Efficiency stocks during the same utilitythantheunhedgedpositionsincetheexpectedutilitygainfrom
period.Whileinotherperiods,thehedgeratiosremainrelativelystable thisstrategyisnegativeforallassetpairs.Additionally,thelossinutility
acrossallcleanenergysectors.Undertheutility-basedhedgingstrategy fromtheminimumvarianceportfolioislargerforλ=5thanforλ =10.
(Figs.7and8),hedgeratiosreflecttheshort-termrisksbetterwiththe Asλindicatesthelevelofriskaversion,theresultsfromTable5suggests
inclusion of higher-order moments. Optimal hedge ratios switch be- thatinvestorswithlessriskaversion(smallerλ)willsufferfromlarger
tween positive and negative values throughout the sampling period utility loss compared to other investors from the minimum variance
acrossallenergysectors.Inotherwords,toeffectivelyusecleanenergy portfolio.Conversely,theutilitygainforinvestorswithlessriskaversion
stocktohedgeoilpricerisks,itisnecessarytoactivelyswitchbetween islargerintheexponentialutilityhedgingstrategy.Thisisillustratedby
thefactthattheutilitygainforinvestorswithλ=5islargerthanthatfor
longandshortpositions.Theswitchesbetweenthelongandshortpo-
λ=10acrossallassetpairsinTable5.
| sitions | are stronger | and | more | active when | Biofuel, | Solar, | Renewable |     |     |     |     |     |
| ------- | ------------ | --- | ---- | ----------- | -------- | ------ | --------- | --- | --- | --- | --- | --- |
Energy Generation, and Energy Efficiency stocks are included in the To demonstrate the utility gain from switching to a utility-based
hedging positions against the oil price risk and become weaker when hedging strategy further, we compare the utility gain from the mini-
Windstocksareincludedinthehedgingpositions.Theswitchesbetween mum variance and exponential utility hedge ratios during the post-
thelongandshortpositionsalsoappeartobestrongerwheninvestors COVID-19 period in Table B.1. We define the post-COVID period as
aremoreriskaverseasshowninFig.7. theperiodafterJanuary1,2020untiltheendofoursamplingperiod.
Table4summarizestheperformancemetricsforalternativeportfolio Our results indicate that while the utility gain from the exponential
strategies. The boldednumbers indicatethe bestperforming portfolio utilityhedgingstrategyisstillpositiveacrossallassetpairs,themini-
foragivenperformancemetric.Intermsofthehedgingeffectiveness, mumvariancehedgeratiosleadtoalargerreductioninutilityduring
defined as the percentage of volatility reduction by investing in the thepost-COVID-19period.Thus,ourresultsindicatetheusefulnessof
portfoliocomparedtoanunhedgedoilposition,theminimumvariance the exponential utility hedging strategies during the most recent eco-
strategyoffersthehighesthedgingeffectivenesscomparedtotheutility- nomiccrisisforinvestorswhoarenotinfinitelyriskaverse.
basedstrategies.Thisisinlinewiththefactthatinvestorswhochoose
theminimumvariancestrategyareassumedtobeextremelyriskaverse.
5.2. Minimumconnectednessportfolios
| Therefore,they |     | arewillingtominimizeriskregardless |     |     |     |     | ofthereturns. |     |     |     |     |     |
| -------------- | --- | ---------------------------------- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
However,forinvestorswhoarelessriskaverse,theutility-basedstrat-
egyoffershigherutilityimplyingthattheminimumvariancestrategy Todemonstratetheusefulnessofthehigher-ordermomentsinoil-
mayleadtosub-optimalassetallocationsinthesescenarios.Specifically, cleanenergyportfoliomanagementfurther,weconstructfouralterna-
theinformationratiosshowthattheexponentialutility-basedportfolios tiveportfoliosbasedontheTVP-VARconnectednessnetworkinSection
offerbetterrisk-returntrade-offsthantheminimumvarianceportfolio. 4.2. Specifically, we construct the minimum connectedness portfolios
(MCPs)inrealizedvolatility,thejumpcomponentofrealizedvolatility,
| For example, |     | in the (OIL, | BIO) | portfolio, | information |     | ratios for the |     |     |     |     |     |
| ------------ | --- | ------------ | ---- | ---------- | ----------- | --- | -------------- | --- | --- | --- | --- | --- |
(λ=10) (λ=5), realizedskewness,andrealizedkurtosis.Intheseportfolios,theweights
| exponential | utility | portfolios | are | 3.674 |     | and | 3.516 |     |     |     |     |     |
| ----------- | ------- | ---------- | --- | ----- | --- | --- | ----- | --- | --- | --- | --- | --- |
oftheassetsvaryaccordingtotheirconnectednesswithothervariables
| which | are significantly |     | higher | than those | for the | unhedged | andmini- |     |     |     |     |     |
| ----- | ----------------- | --- | ------ | ---------- | ------- | -------- | -------- | --- | --- | --- | --- | --- |
ineachhighermoment.Wefirstcalculatethepairwiseconnectedness
mumvarianceportfolio(0.4098and0.5024).Similarobservationscan
indexinhighermomentsbetweentwoassetsasfollows(Tiwarietal.,
| be made | for | other oil-clean | energy | stock | pairs. | Since the | exponential |     |     |     |     |     |
| ------- | --- | --------------- | ------ | ----- | ------ | --------- | ----------- | --- | --- | --- | --- | --- |
utility-based portfolios incorporate information about investors’ risk 2022;Broadstocketal.,2022):
+
|     |     |     |     |     |     |     |     |         | =2*      | j S O T | i j , t j S O Tj i, t |      |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------- | --------------------- | ---- |
|     |     |     |     |     |     |     |     | PCIij,t |          | +j      | +j +jSOTjj,t          | (24) |
|     |     |     |     |     |     |     |     |         | jSOTii,t | S O T   | j i , t S O T ij , t  |      |
6 Thesearegivenby:Var(Wt ) =VarOil,t (cid:0) 2*β +β2VarClean,t Byconstruction,PCIij,t ∈[0,1]andcapturesthelevelofconnectivity
tCovOil,Clean,t
(cid:0) ) be t w ee n t h e v a r ia b l e s. L e t P C I b e t h e p a i rw is e c on n e c te d n es sm a t r ix o n
| Skew(Wt | )=SkewOil,t | (cid:0) β3 |     | +3 β2(cid:0) | β   |     |     |     |     |     | t   |     |
| ------- | ----------- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
t SkewClean,t CoSkewOil,Clean,t d a y t, w h o s e ij -t h e l e m e n t i s P C I t. L e t I b e th e n × n i d e n ti ty m at ri x . T h e
ij,
|         |             |                 |     | (cid:0)         | )                 |     |                    | portfolioweightsofthevariablesinthesystemare: |     |     |     |     |
| ------- | ----------- | --------------- | --- | --------------- | ----------------- | --- | ------------------ | --------------------------------------------- | --- | --- | --- | --- |
| Kurt(Wt | )=KurtOil,t | +β4 KurtClean,t |     | (cid:0) 4 β3 +β | CoKurtOil,Clean,t |     | +6β4CovOil,Clean,t |                                               |     |     |     |     |
|         |             | t               |     | t               | t                 |     |                    |                                               |     |     |     |     |
PCI(cid:0)1*I
w= t
|          | ,S          | ,                  |                 |                |                   |                |                             |     | (cid:0)1*I |     |     | (25) |
| -------- | ----------- | ------------------ | --------------- | -------------- | ----------------- | -------------- | --------------------------- | --- | ---------- | --- | --- | ---- |
| w h e re | V a rj ,t k | e w j, t a n d K u | r tj ,t s t a n | d f or t h e v | a r i an c e ,    | sk e w n e ss, | a n d k u r t o s is o f    |     | I*PC I     |     |     |      |
|          |             | ,C                 | ,               |                |                   |                |                             |     | t          |     |     |      |
| as se t  | j o n d a y | t . C o v i, j,t o | S k e w i ,j ,t | an d C o K u   | r ti ,j, t st a n | d f o r th e   | co - v ar i a n c e , c o - |     |            |     |     |      |
skewness,andco-kurtosisbetweenassetsi,jondayt.WeestimateVarj,t ,Skewj,t , Table 6 presents a summary of the performance indicators of an
,Covi,j,t ,CoSkewi,j,t ,andCoKurti,j,t unhedged position in oil price and the minimum connectedness port-
| Kurtj,t |     |     |     | by calculating |     | the realized | measures |     |     |     |     |     |
| ------- | --- | --- | --- | -------------- | --- | ------------ | -------- | --- | --- | --- | --- | --- |
folios(MCPs)ineachhighermoment(i.e.,realizedvolatility,thejump
| using | the five-minute | intraday | data | following | Nekhili | and Bouri | (2023). See |     |     |     |     |     |
| ----- | --------------- | -------- | ---- | --------- | ------- | --------- | ----------- | --- | --- | --- | --- | --- |
NekhiliandBouri(2023)formoredetails. component of realized volatility, realized skewness, and realized
24

W.HaoandL.Pham Energy Economics 140 (2024) 107987
kurtosis).Table6.1presentstheportfolioreturns,standarddeviationof utility gains from utilizing the utility-based hedge ratios across the
returns,andinformationratios.Table6.2providestheaverageweightof alternativeutilityfunctions.Asapointofreference,wealsoincludethe
oil in each portfolio and the hedging effectiveness provided by each utility gains from using the quadratic utility function that takes into
portfolio against variations in oil prices. The table indicates that the accountthefirstandsecondmomentsofthereturndistributions.Our
informationratioontheMCPsishigherthanthatforoilpriceimplying resultsinTablesB.2-B.3indicatethatourpreviousconclusionsarestill
thattheMCPsprovidebetterrisk-returntradeoffscomparedtoanun- valid.Specifically,investorswhoarenotinfinitelyriskaversecanenjoy
hedged position in oil. Additionally, the hedging effectiveness of the potentialutilitygainsfromswitchingtoutility-basedhedgingstrategies,
MCPsarepositive.Thus,theMCPsofferssomehedgingbenefitsagainst especially during the post-COVID-19 period. This highlights the rele-
anunhedgedpositioninoil.However,wefindthehedgingeffectiveness vanceofconsideringhighermomentsinportfoliomanagement.
oftheMCPstobequitesmall.Thus,thiscorroboratesourfindingsin Finally, we consider the performance of the minimum higher
Section 5.1 that while higher-order moment portfolio strategies offer momentconnectednessportfolioduringthepost-COVID-19period.Our
smaller hedging effectiveness, they offer better risk-return trade-offs. resultsinTableC.1.oftheappendixsuggestthattheinformationratioof
Investors who arenot infinitely risk-averse would preferhigher-order theminimumconnectednessportfoliobasedonrealizedvolatilityandits
moment portfolio strategies, while infinitely risk-averse investors jump component is larger than that of the unhedged position in oil.
wouldprefertheminimumvariancehedgingstrategy. However,usingotherhigher-ordermomentstoconstructtheminimum
connectedness portfolio leads to a slight decrease in the information
5.3. Robustnessanalyses ratio during this period. This reflects the fact that the energy market
experiencesanumberofshocksduringthisperiod,suchastheCOVID-
Totesttherobustnessofouranalysis,weconsideralternativefore- 19financialcrisis,theRussia-SaudiArabiaoilpricewar,andtheRussia-
casthorizonsoffivedays(atradingweek-Fig.A.1),20days(atrading Ukrainewar.Thissuggeststhatotherhedgingstrategiesmaybeusefulto
month-Fig.A.2),and60days(atradingquarter-Fig.A.3)andalter- hedgeoilpriceshocksduringcrisisperiods.Thisresultisconsistentwith
native lag structures of the TVP-VAR model (Figs. A.4-A.5). We also NekhiliandBouri(2023)whofindthathigher-ordermomenthedging
consider alternative prior models,such as the Bayesian and the unin- strategiesdonotimprovethehedgingperformanceofgoldagainstoil
formative priors (Figs. A.6-A.7), and alternative forgetting factors pricesduringtheCOVID-19period.Inaddition,wetesttheex-anteor
(Figs.A.8-A.9).Next,wetesttherobustnessofourresultsusingalter- out-of-sampleperformanceofthehigher-orderminimumconnectedness
nativeconnectednessmodelsthatincludetheoriginalmodelsofDiebold strategies.Specifically,foreachperiod,wefirstcalculatetheone-step-
andYilmaz(2009,2012,2014)witha200-dayrollingwindow,thejoint aheadpairwiseconnectednessindexmatrixthatisthenusedtocalcu-
connectednessmodelwitha200-dayrollingwindowofLastrapesand latetheone-step-aheadminimumconnectednessportfolioandportfolio
Wiesen (2021) and the TVP-VAR model of Antonakakis et al. (2020) performance.Weobtain2000one-step-aheadminimumconnectedness
(Figs.A.10-A.12).7Wepresenttheresultsofthesealternativemodelsin portfoliosfromthisprocedure.TablesC.2inAppendixCpresentsthe
Appendix A. Overall; we find that our results are consistent with the estimation results. We find that the out-of-sample higher-moment
resultsofthesealternativemodels. portfoliosareverysimilartotheex-posthigher-momentportfoliosusing
Next,wetesttherobustnessofourresultsundertheR2model-free thefullsampledatainTable6.Moreover,wecomparetheout-of-sample
connectednessmodelofBallietal.(2023).Thismodelisameasureof higher-orderminimumconnectednessportfoliosinTableC.2withthe
unconditionalconnectedness,builtsolelyuponvarianceandcovariance, out-of-sample minimum quantile connectedness portfolios. The
and allows separating total connectedness into contemporaneous and quantile-based portfolios are based on the results of the quantile
lagged connectedness. Fig. A.13 presents the total connectedness in- connectednessmodelsattheextremeupperandlowerquantiles(i.e.,the
dexesunderthismodel.Wefindthatthecontemporaneousandlagged 5thand95thquantilesofassetreturns).TableC.3presentstheestima-
connectedness indexes tend to be in the same direction, and the tion results. We find that the portfolio performances are comparable
contemporaneous connectedness are typically larger than the lagged between the higher-moment portfolios (Table C.2) and the quantile-
connectedness.Becausethecontemporaneouseffectplaysalargerrole based portfolios (Table C.3). However, the higher-moment portfolios,
in explaining the spillovers across the variables, we will leave the particularlytheportfoliosconstructedfromthe3rdand4thmoments,
explorationofthelaggedeffectsforfutureresearch.Finally,wetestthe offerbetterrisk-returntrade-offsandhedgingeffectivenesscomparedto
robustnessofourresultsusingthequantilevectorautoregressionmodel thequantileportfolios.Webelieveboththequantileandhigher-moment
for the median quantile with a rolling window of 200 days following portfoliosofferdifferentinsightsintoassetbehaviorandaresuitablefor
Andoetal.(2022).Thebenefitofusingaquantileregressionisthatit investors withdifferent riskappetites. Specifically, thequantile-based
makesnoassumptionabouttheparametricformofthedistributionof portfolios focus on one specific region of the return distributions and
the response variables nor does it assume that the variance of the depend upon the choices of the quantiles. The higher-moment-based
responsevariablesisconstant.OurresultsinFig.A.14oftheappendix portfoliosarerealizedmeasuresandfocusontheshapesofthereturn
indicatethattheconnectednessindexesunderthequantileconnected- distributions(e.g.,asymmetry,tailthickness).Weleavefurtherexplo-
ness model are similar to those obtained from our TVP-VAR model. rationsofhowtocombinethequantileandhigher-momentmethodsin
However, a drawback of the quantile connectedness model is that it portfoliomanagementstrategiesforfutureresearch.
reliesontheselectionofanarbitraryrollingwindow.Additionally,itis
computationallyunabletoestimatetheconnectednessindexesforthe 6. Conclusions
jumpcomponentofvolatility.Thus,werelyontheTVP-VARmodelfor
our main analysis and present the quantile connectedness results as In this paper, we study the connectedness between clean energy
robustnesschecks. stock and oil prices at higher-order moments including realized vola-
Inaddition,weconsidertheutility-basedhedgeratiosunderalter- tility,jumps,realizedskewness,andrealizedkurtosis,anddemonstrate
nativeutilityfunctions,suchasthequartic,logarithmic,andhyperbolic theusefulnessofconsideringhigher-ordermomentsinacleanenergy-oil
powerutility.Theseutilityfunctionsarealternativewaystoincorporate portfolio. Our initial analysis on static higher-order moment connect-
allofthemomentsofthedistributionsintohedgingstrategyconstruc- ednessbetweencleanenergystockandoilpricesshowsthattheclean
tions (Brooks et al., 2012). Tables B.2-B.3 of Appendix B present the energysectorsandoilmarketarehighlyconnectedatallhigher-order
moments. We find that the connectedness between clean energy and
oil markets are moment dependent, and the shock transmitter or
7 Our results for the rolling-window models are consistent across other recipientrolesplayedbyeachcleanenergysectorandoilmarketalso
choicesoftherollingwindows(150or250days). varyacrossdifferentmoments.Ourfurtheranalysisregardingthetime
25

W.HaoandL.Pham Energy Economics 140 (2024) 107987
dynamic higher-order moment connectedness between clean energy pricerisks.Weconsideraminimumvarianceinvestmentstrategythat
stockandoilpricesrevealsthattheconnectednessistimevaryingand seeks to minimize risk regardless as to the return for risk averse in-
turbulenttimeperiodsareassociatedwithstrongerconnectednessbe- vestors,autility-basedinvestmentstrategywhosegoalistomaximize
tweenthecleanenergyandoilmarkets. investors’utilitybyconsideringinvestors’riskpreferenceandhigher-
Toexplorethetimevaryingbehaviorsfurther,westudytheday-of- ordermomentmovementsofassetreturns,andaminimumconnected-
the-weekpatternsofhigher-ordermomentconnectedness.Wefindthat nessportfolioinhighermomentsthataimstominimizesthepairwise
connectednessintensifiesfromMondaystoFridaysduetotheincorpo- higher-moment connectedness across variables. Our results show that
ration and accumulation of news information throughout the trading theminimumvariancestrategyoffersthehighesthedgingeffectiveness
week. The day-of-the-week patterns appear to be the opposite during compared to the utility-based strategy. However, the utility-based
lowvs.highuncertaintyperiodsindicatingthattheconnectednessbe- strategy and the minimum connectedness portfolios in higher mo-
tweenthecleanenergyandoilmarketsisconditionaluponthemarket ments offer higher utility and better risk-return trade-offs than the
statesanduncertainty.WenextemployaMarkovswitchingregression minimum variance portfolio corroborating the usefulness and impor-
modeltoestablishaformalrelationshipbetweenhigher-ordermoment tanceofconsideringhigher-ordermomentsinassetallocationstrategies.
connectedness and economic, political, and financial market uncer-
tainty.Ourresultssuggestthatoilandstockmarketvolatilityarethe CRediTauthorshipcontributionstatement
main drivers of higher-order moment connectedness, while economic
policyuncertaintyandgeopoliticalriskplaymoremodestroles. Wei Hao: Writing – review & editing, Writing – original draft,
Wecontributetotheliteraturebyunravelinghowtheoilandclean Validation, Project administration, Methodology, Formal analysis,
energymarketsarerelatedtoeachotheracrosshigher-ordermoments, Conceptualization.LinhPham:Writing–review&editing,Writing–
therebycapturingtheirspilloversinasymmetryrisks,jumprisks,andfat original draft, Validation, Software, Methodology, Formal analysis,
tailrisks.Ourfindingsoftheheterogeneousconnectednessbetweenthe Conceptualization.
oilandcleanenergymarketsacrossthemomentshighlighttherelevance
of considering higher-order moments in investment portfolio design.
The above findings have important implications for investors in port- Declarationofcompetinginterest
folioallocationdecisions.Asanimportantextension,weconductformal
tests to investigate how clean energy stocks can be used to hedge oil None.
AppendixA. Robustnessanalysesoftheconnectednessmodels
Fig.A.1. Totalconnectednessindexes–TVP-VARExtendedJointConnectednessModelwitha5-dayforecasthorizon.
Note:ThefigurepresentstheTCIobtainedfromusingaforecasthorizonof5daysinourmainempiricalmodel.
26

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.A.2. Totalconnectednessindexes–TVP-VARExtendedJointConnectednessModelwitha20-dayforecasthorizon.
Note:ThefigurepresentstheTCIobtainedfromusingaforecasthorizonof20daysinourmainempiricalmodel.
Fig.A.3. Totalconnectednessindexes–TVP-VARExtendedJointConnectednessModelwitha60-dayforecasthorizon.
Note:ThefigurepresentstheTCIobtainedfromusingaforecasthorizonof60daysinourmainempiricalmodel.
27

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.A.4. Totalconnectednessindexes–TVP-VARExtendedJointConnectednessModelwithalaglengthof1intheTVP-VARregression.
Note:ThefigurepresentstheTCIobtainedfromusingalaglengthof1inourmainempiricalmodel.
Fig.A.5. Totalconnectednessindexes–TVP-VARExtendedJointConnectednessModelwithalaglengthof2intheTVP-VARregression.
Note:ThefigurepresentstheTCIobtainedfromusingalaglengthof2inourmainempiricalmodel.
28

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.A.6. Totalconnectednessindexes–TVP-VARExtendedJointConnectednessModelwithBayesianPriors.
Note:ThefigurepresentstheTCIobtainedfromusingtheBayesianpriorsinourmainempiricalmodel.
Fig.A.7. Totalconnectednessindexes–TVP-VARExtendedJointConnectednessModelwithUninformativePriors.
Note:ThefigurepresentstheTCIobtainedfromusingtheuninformativepriorsinourmainempiricalmodel.
29

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.A.8. Totalconnectednessindexes–TVP-VARExtendedJointConnectednessModelwitha0.98forgettingfactor.
Note:ThefigurepresentstheTCIobtainedfromusingaforgettingfactorof0.98inourmainempiricalmodel.
30

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.A.9. Totalconnectednessindexes–TVP-VARExtendedJointConnectednessModelwitha0.97forgettingfactor.
Note:ThefigurepresentstheTCIobtainedfromusingaforgettingfactorof0.97inourmainempiricalmodel.
31

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.A.10. OriginalDYmodelwith200daysrollingwindow.
Note:ThefigurepresentstheTCIobtainedfromtheOriginalDYConnectednessmodelwitha200-dayrollingwindow.
32

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.A.11. ExtendedJointConnectednessmodelwitha200-dayrollingwindow.
Note:ThefigurepresentstheTCIobtainedfromtheExtendedJointConnectednessmodelwitha200-dayrollingwindow.
33

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.A.12. TVP-VARConnectednessmodel.
Note:ThefigurepresentstheTCIobtainedfromtheTVP-VARmodel.
34

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Fig.A.13. R2Model-FreeConnectednessmodel.
Note:ThefigurepresentstheTCIobtainedfromtheR2ModelFreeConnectedness.Theblackarearepresentstotalconnectedness,whiletheblueandredareas
representthecontemporaneousandlaggedconnectedness.
35

| W.HaoandL.Pham |     |     |     |     |     | Energy Economics 140 (2024) 107987  |     |
| -------------- | --- | --- | --- | --- | --- | ----------------------------------- | --- |
Fig.A.14. QuantileConnectednessmodel–Medianquantile.
Note:ThefigurepresentstheTCIobtainedfromtheQuantileConnectednessModelatthemedianquantile.
AppendixB. Robustnesschecksfortheutility-basedhedgingportfolioperformance
TableB.1
Expectedutilitygainunderalternativehedgingstrategies–Post-COVID-19period.
Hedgingstrategies
| Portfolio |     | λ   |     | MinimumVariance |     | ExponentialUtility |     |
| --------- | --- | --- | --- | --------------- | --- | ------------------ | --- |
|           |     | 10  |     | (cid:0) 1.0838  |     | 0.2013             |     |
(OIL,BIO)
|     |     | 5   |     | (cid:0) 8.3189 |     | 0.2418 |     |
| --- | --- | --- | --- | -------------- | --- | ------ | --- |
(cid:0)
|             |     | 10  |     | 0.0096         |     | 0.1796 |     |
| ----------- | --- | --- | --- | -------------- | --- | ------ | --- |
| (OIL,SOLAR) |     | 5   |     | (cid:0) 0.0927 |     | 0.1686 |     |
|             |     | 10  |     | (cid:0) 0.7115 |     | 0.1685 |     |
| (OIL,WIND)  |     | 5   |     | (cid:0) 5.2968 |     | 0.1463 |     |
(cid:0)
|            |     | 10  |     | 0.0858         |     | 0.1135 |     |
| ---------- | --- | --- | --- | -------------- | --- | ------ | --- |
| (OIL,REG)  |     | 5   |     | (cid:0) 0.7337 |     | 0.0892 |     |
|            |     | 10  |     | (cid:0) 7.9299 |     | 1.1316 |     |
|            |     |     |     | (cid:0)        |     | 2.1671 |     |
| (OIL,ENEF) |     | 5   |     | 60.9713        |     |        |     |
Note:Thetablepresentstheexpectedutilitygainoftheminimumvariancehedgeratiosandtheexponentialutilityhedgeratios,comparedtotheutilityofanunhedged
positioninoil,acrossdifferentriskaversionparameters(λ)duringthepost-COVID-19periodfromJanuary1,2020totheendofoursamplingperiod.BIO,SOLAR,
WIND,REG,andENEFrepresenttheNASDAQOMXBiofuel,Wind,Solar,RenewableEnergyGeneration,andEnergyEfficiencyIndexes.
TableB.2
Expectedutilitygainunderalternativeutility-basedhedgingstrategies–Fullsample.
Utilityfunctions
Portfolio λ Quadratic ExponentialUtility Quartic Power Logarithm
| (OIL,BIO)   | 10  | 0.1816 | 0.4039 |     | 1.5461 | 0.3982 | 0.2371 |
| ----------- | --- | ------ | ------ | --- | ------ | ------ | ------ |
|             | 5   | 0.3582 | 0.6706 |     | 1.7186 | 0.6876 | 0.4696 |
|             | 10  | 1.1097 | 0.7490 |     | 2.5296 | 0.7434 | 0.4445 |
| (OIL,SOLAR) | 5   | 2.1850 | 1.2865 |     | 3.1536 | 1.3194 | 0.8871 |
(continuedonnextpage)
36

| W.HaoandL.Pham |     |     |     |     | Energy Economics 140 (2024) 107987  |     |
| -------------- | --- | --- | --- | --- | ----------------------------------- | --- |
TableB.2(continued)
Utilityfunctions
Portfolio λ Quadratic ExponentialUtility Quartic Power Logarithm
| (OIL,WIND) | 10  | 0.9149 | 0.1463 | 1.4867 | 0.1253 | 0.0424 |
| ---------- | --- | ------ | ------ | ------ | ------ | ------ |
|            | 5   | 1.8019 | 0.1198 | 0.8759 | 0.1104 | 0.0546 |
|            | 10  | 0.4140 | 0.2430 | 1.5705 | 0.2281 | 0.1142 |
| (OIL,REG)  | 5   | 0.8153 | 0.3363 | 1.2373 | 0.3366 | 0.2094 |
|            | 10  | 0.3067 | 0.7067 | 2.0831 | 0.7173 | 0.4380 |
| (OIL,ENEF) | 5   | 0.6052 | 1.2904 | 2.7925 | 1.3277 | 0.8747 |
Note:Thetablepresentstheexpectedutilitygainofhedgingstrategiesbasedonthequadratic,cubic,quartic,power,andlogarithmutilityfunctions,comparedtothe
utilityofanunhedgedpositioninoil,acrossdifferentriskaversionparameters(λ).BIO,SOLAR,WIND,REG,andENEFrepresenttheNASDAQOMXBiofuel,Wind,
Solar,RenewableEnergyGeneration,andEnergyEfficiencyIndexes.
TableB.3
Expectedutilitygainunderalternativeutility-basedhedgingstrategies–Post-COVID-19period.
Utilityfunctions
Portfolio λ Quadratic ExponentialUtility Quartic Power Logarithm
| (OIL,BIO)   | 10  | 0.1815 | 0.2013 | 1.2603 | 0.1875 | 0.0838 |
| ----------- | --- | ------ | ------ | ------ | ------ | ------ |
|             | 5   | 0.3571 | 0.2418 | 0.9898 | 0.2355 | 0.1447 |
|             | 10  | 1.0976 | 0.1796 | 1.3786 | 0.1584 | 0.0637 |
| (OIL,SOLAR) | 5   | 2.0875 | 0.1686 | 0.9036 | 0.1589 | 0.0822 |
|             | 10  | 0.9151 | 0.1685 | 1.7053 | 0.1452 | 0.0488 |
| (OIL,WIND)  | 5   | 1.8037 | 0.1463 | 1.0321 | 0.1364 | 0.0659 |
|             | 10  | 0.4143 | 0.1135 | 1.1965 | 0.0963 | 0.0298 |
| (OIL,REG)   | 5   | 0.8175 | 0.0892 | 0.6926 | 0.0807 | 0.0388 |
|             | 10  | 0.3068 | 1.1316 | 2.3205 | 1.1662 | 0.7314 |
1.4742
| (OIL,ENEF) | 5   | 0.6055 | 2.1671 | 4.1172 | 2.2369 |     |
| ---------- | --- | ------ | ------ | ------ | ------ | --- |
Note:Thetablepresentstheexpectedutilitygainofhedgingstrategiesbasedonthequadratic,cubic,quartic,power,andlogarithmutilityfunctions,comparedtothe
utilityofanunhedgedpositioninoil,acrossdifferentriskaversionparameters(λ)duringthepostCOVID-19periodfromJanuary1,2020totheendofoursampling
period.BIO,SOLAR,WIND,REG,andENEFrepresenttheNASDAQOMXBiofuel,Wind,Solar,RenewableEnergyGeneration,andEnergyEfficiencyIndexes.
AppendixC. Robustnesschecksfortheminimumconnectednessportfolioperformance
TableC.1
Minimumconnectednessportfolioperformanceindicators–Post-COVID19period
TableC.1.1.Portfolioreturnsummarystatistics
|     | Portfolio               |     | MeanReturn | SDofReturn | Info.Ratio |     |
| --- | ----------------------- | --- | ---------- | ---------- | ---------- | --- |
|     | Oil(Unhedged)           |     | 0.00926    | 0.13781    | 0.06719    |     |
|     | MCP(RealizedVolatility) |     | 0.00961    | 0.11938    | 0.08049    |     |
MCP(Jumpcomponentofrealizedvolatility) 0.00431 0.06000 0.07177
|     | MCP(RealizedSkewness) |     | 0.02354 | 0.03608 | 0.06523 |     |
| --- | --------------------- | --- | ------- | ------- | ------- | --- |
|     | MCP(RealizedKurtosis) |     | 0.02331 | 0.03483 | 0.06691 |     |
TableC.1.2.Averageweightsofoilandhedgingeffectiveness
|     | Portfolio                              |     | Meanweight | SDofweight | Hedgingeffectiveness(%) |     |
| --- | -------------------------------------- | --- | ---------- | ---------- | ----------------------- | --- |
|     | Oil(Unhedged)                          |     | 1.00       | 0.00       | 0.00                    |     |
|     | MCP(RealizedVolatility)                |     | 0.50       | 0.26       | 0.25                    |     |
|     | MCP(Jumpcomponentofrealizedvolatility) |     | 0.19       | 0.20       | 0.81                    |     |
|     | MCP(RealizedSkewness)                  |     | 0.20       | 0.02       | 0.93                    |     |
|     | MCP(RealizedKurtosis)                  |     | 0.19       | 0.01       | 0.94                    |     |
Note:Thetablepresentstheperformanceindicatorsofanunhedgedpositioninoilpriceandtheminimumconnectednessportfolioin
realizedvolatility,thejumpcomponentofvolatility,realizedskewness,andrealizedkurtosisinthepost-COVID-19periodfrom
January1,2020totheendofoursamplingperiod.TableC.1.1presentstheportfolioreturns,thestandarddeviationofreturns,and
theinformationratios.TableC.1.2reportstheaverageweightofoilineachportfolioandthehedgingeffectivenessprovidedbyeach
portfolioagainstvariationsinoilprices.
37

W.HaoandL.Pham Energy Economics 140 (2024) 107987
TableC.2
Minimumhigher-momentconnectednessportfolioperformanceindicators–Out-of-sampleanalysis.
TableC.2.1.Portfolioreturnsummarystatistics
| Portfolio               |     |     | MeanReturn |     | SDofReturn |     | Info.Ratio |
| ----------------------- | --- | --- | ---------- | --- | ---------- | --- | ---------- |
| Oil(Unhedged)           |     |     | 0.00322    |     | 0.08550    |     | 0.037758   |
| MCP(RealizedVolatility) |     |     | 0.00303    |     | 0.07303    |     | 0.041555   |
MCP(Jumpcomponentofrealizedvolatility) 0.00159 0.02893 0.055236
| MCP(RealizedSkewness) |     |     | 0.00104 |     | 0.02341 |     | 0.044757 |
| --------------------- | --- | --- | ------- | --- | ------- | --- | -------- |
| MCP(RealizedKurtosis) |     |     | 0.00106 |     | 0.02242 |     | 0.047439 |
TableC.2.2.Averageweightsofoilandhedgingeffectiveness
| Portfolio                              |     |     | Meanweight | SDofweight |     | Hedgingeffectiveness(%) |     |
| -------------------------------------- | --- | --- | ---------- | ---------- | --- | ----------------------- | --- |
| Oil(Unhedged)                          |     |     | 1.00       | 0.00       |     | 0.00                    |     |
| MCP(RealizedVolatility)                |     |     | 0.25       | 0.20       |     | 0.27                    |     |
| MCP(Jumpcomponentofrealizedvolatility) |     |     | 0.21       | 0.22       |     | 0.89                    |     |
| MCP(RealizedSkewness)                  |     |     | 0.22       | 0.04       |     | 0.93                    |     |
| MCP(RealizedKurtosis)                  |     |     | 0.19       | 0.03       |     | 0.93                    |     |
Note:Thetablepresentstheout-of-sampleperformanceindicatorsofanunhedgedpositioninoilpriceandtheminimumconnect-
ednessportfolioinrealizedvolatility,thejumpcomponentofvolatility,realizedskewness,andrealizedkurtosis.TableC.2.1presents
theportfolioreturns,thestandarddeviationofreturns,andtheinformationratios.TableC.2.2reportstheaverageweightofoilin
eachportfolioandthehedgingeffectivenessprovidedbyeachportfolioagainstvariationsinoilprices.
TableC.3
Minimumquantileconnectednessportfolioperformanceindicators–Out-of-sampleanalysis.
TableC.3.1.Portfolioreturnsummarystatistics
|     | Portfolio          | MeanReturn |     | SDofReturn |     | Info.Ratio |     |
| --- | ------------------ | ---------- | --- | ---------- | --- | ---------- | --- |
|     | Oil(Unhedged)      | 0.00322    |     | 0.08550    |     | 0.037758   |     |
|     | MCP(Lowerquantile) | 0.00185    |     | 0.03700    |     | 0.05009    |     |
|     | MCP(Upperquantile) | 0.00130    |     | 0.03136    |     | 0.04156    |     |
TableC.3.2.Averageweightsofoilandhedgingeffectiveness
|     | Portfolio          | Meanweight | SDofweight |     | Hedgingeffectiveness(%) |     |     |
| --- | ------------------ | ---------- | ---------- | --- | ----------------------- | --- | --- |
|     | Oil(Unhedged)      | 1.00       | 0.00       |     | 0.00                    |     |     |
|     | MCP(Lowerquantile) | 0.28       | 0.11       |     | 0.81                    |     |     |
|     | MCP(Upperquantile) | 0.21       | 0.11       |     | 0.87                    |     |     |
Note:Thetablepresentstheout-of-sampleperformanceindicatorsofanunhedgedpositioninoilprice,andthe
minimumconnectednessportfoliointheextremelowerandupperquantilesofreturns(i.e.,the5thand95th
quantilesofreturns).TableC.3.1presentstheportfolioreturns,thestandarddeviationofreturns,andthein-
formationratios.TableC.3.2reportstheaverageweightofoilineachportfolioandthehedgingeffectiveness
providedbyeachportfolioagainstvariationsinoilprices
38

W.HaoandL.Pham Energy Economics 140 (2024) 107987
AppendixD. Blockdiagramofmethodology
Input Data
Measure Higher-Order Moments
Step 1
(Realized Volatility, Jump Volatility,
Realized Skewness, Realized Kurtosis)
Static Higher-Order Moments
Connectedness Analysis
Estimate Connectedness using TVP-VAR
Step 2 Model Time-varying Higher-Order Moments
(Total, Directional, Net Connectedness) Connectedness Analysis
Day-of-the-week Pattens of Higher-
Order Moments Connectedness
Determinants of Connectedness
Step 3
RegressionAnalysis on Uncertainty and
Higher-Order Moments Connectedness
(Markov-switching Model)
Economic and Financial Implicationson Asset
Step 4 Allocation Decision
(Utility-basedHedging Strategy and Minimum
Connectedness Portfolio)
AppendixE. Supplementarydata
Supplementarydatatothisarticlecanbefoundonlineathttps://doi.org/10.1016/j.eneco.2024.107987.
References BloombergNewEnergyFinance,2023.Energytransitioninvestmenttrends2023.In:
TechnicalReport.
Bonato,M.,Gupta,R.,Lau,C.K.M.,Wang,S.,2020.Moments-basedspilloversacross
Ahmad,W.,2017.Onthedynamicdependenceandinvestmentperformanceofcrudeoil
goldandoilmarkets.EnergyEcon.89,104799.
andcleanenergystocks.Res.Int.Bus.Financ.42,376–389.
Bouri,E.,Lei,X.,Jalkh,N.,Xu,Y.,Zhang,H.,2021.Spilloversinhighermomentsand
Ahmad,W.,Sadorsky,P.,Sharma,A.,2018.Optimalhedgeratiosforcleanenergy
jumpsacrossU.S.stockandstrategiccommoditymarkets.Res.Policy72,102060.
equities.Econ.Model.72,278–295.
Broadstock,D.C.,Cao,H.,Zhang,D.,2012.Oilshocksandtheirimpactonenergyrelated
Alexander,C.,Barbosa,A.,2008.Hedgingindexexchangetradedfunds.J.Bank.Financ. stocksinChina.EnergyEcon.34(6),1888–1895.
32(2),326–337.
Broadstock,D.C.,Chatziantoniou,I.,Gabauer,D.,2022.Minimumconnectedness
Andersen,T.G.,Bollerslev,T.,1998.Answeringtheskeptics:yes,standardvolatility
portfoliosandthemarketforgreenbonds:Advocatingsociallyresponsible
modelsdoprovideaccurateforecasts.Int.Econ.Rev.39,885–905.
investment(SRI)activity.In:ApplicationsinEnergyFinance:TheEnergySector,
Andersen,T.G.,Bollerslev,T.,Diebold,F.X.,Labys,P.,2003.Modelingandforecasting
EconomicActivity,FinancialMarketsandtheEnvironment.SpringerInternational
realizedvolatility.Econometrica71(2),579–625.
Publishing,Cham,pp.217–253.
Ando,T.,Greenwood-Nimmo,M.,Shin,Y.,2022.Quantileconnectedness:modelingtail ˇ
Brooks,C.,Cerný,A.,Miffre,J.,2012.Optimalhedgingwithhighermoments.J.Futur.
behaviorinthetopologyoffinancialnetworks.Manag.Sci.68(4),2401–2431.
Mark.32(10),909–944.
Antonakakis,N.,Chatziantoniou,I.,Gabauer,D.,2020.Refinedmeasuresofdynamic Corsi,F.,Pirino,D.,Reno`,R.,2010.Thresholdbipowervariationandtheimpactofjump
connectednessbasedontime-varyingparametervectorautoregressions.J.Risk onvolatilityforecasting.J.Econ.159(2),276–288.
Financ.Manag.13(4),84.
Cotter,J.,Hanly,J.,2015.Performanceofutilitybasedhedges.EnergyEcon.49,
Bakas,D.,Triantafyllou,A.,2018.Theimpactofuncertaintyshocksonthevolatilityof 718–726.
commodityprices.J.Int.MoneyFinanc.87,96–111.
Cross,F.,1973.ThebehaviorofstockpricesonFridaysandMondays.Financ.Anal.J.29
Balcilar,M.,Gabauer,D.,Umar,Z.,2021.Crudeoilfuturescontractsandcommodity (6),67–69.
markets:newevidencefromaTVP-VARextendedjointconnectednessapproach.
Dickey,D.A.,Fuller,W.A.,1979.Distributionoftheestimatorsforautoregressivetime
Res.Policy73,102219.
serieswithaunitroot.JournaloftheAmericanStatisticalAssociation74(366a),
Balli,F.,Balli,H.O.,Dang,T.H.N.,Gabauer,D.,2023.ContemporaneousandlaggedR2 427–431.
decomposedconnectednessapproach:newevidencefromtheenergyfuturesmarket.
Diebold,F.X.,Yilmaz,K.,2009.Measuringfinancialassetreturnandvolatilityspillovers,
Financ.Res.Lett.57,104168. withapplicationtoglobalequitymarkets.Econ.J.119(534),158–171.
Barndorff-Nielsen,O.E.,Kinnebrouk,S.,Shephard,N.,2010.Measuringdownsiderisk:
Diebold,F.X.,Yilmaz,K.,2012.Bettertogivethantoreceive:predictivedirectional
Realisedsemivariance.In:Bollerslev,T.,Russell,J.,Watson,M.(Eds.),Volatilityand measurementofvolatilityspillovers.Int.J.Forecast.28(1),57–66.
TimeSeriesEconometrics:EssaysinHonorofRobertF.Engle.OxfordUniversity
Diebold,F.X.,Yilmaz,K.,2014.Onthenetworktopologyofvariancedecompositions:
Baru P n r í e k s , s J , . p , p K . o 1 ˇce 1 n 7 d – a 1 , 3 E 6 . . ,V´acha,L.,2015.Volatilityspilloversacrosspetroleummarkets. Ferre m r, ea R s . u , r S i h n a g h t z h a e d, co S n .J n .H ec ., te L d o´ n p e e s z s , o R f ., fi J n a a r n e c n˜ i o a , l F fi ., rm 20 s. 18 J. . E T c im on e . a 1 n 8 d 2 fr (1 eq ), u 1 en 1 c 9 y –1 d 3 y 4 n . amicsof
EnergyJ.36(3),309–329.
Baruník,J.,Koˇcenda,E.,Va´cha,L.,2017.Asymmetricvolatilityconnectednessonthe c
7
o
6
n
,
n
1
e
–
c
2
t
0
ed
.
nessbetweenrenewableenergystocksandcrudeoilprices.EnergyEcon.
forexmarket.J.Int.MoneyFinanc.77,39–56.
Foglia,M.,Angelini,E.,Huynh,T.L.D.,2022.Tailriskconnectednessincleanenergyand
oilfinancialmarket.Ann.Oper.Res.334,575–599.
39

W.HaoandL.Pham Energy Economics 140 (2024) 107987
Frank,M.Z.,Sanati,A.,2018.Howdoesthestockmarketabsorbshocks?J.Financ.Econ. Reboredo,J.C.,2015.Istheredependenceandsystemicriskbetweenoilandrenewable
129(1),136–153. energystockprices?EnergyEcon.48,32–45.
French,K.R.,1980.Stockreturnsandtheweekendeffect.J.Financ.Econ.8(1),55–69. Reboredo,J.C.,Ugolini,A.,2016.Quantiledependenceofoilpricemovementsandstock
Gkillas,K.,Bouri,E.,Gupta,R.,Roubaud,D.,2022.Spilloversinhigher-ordermoments returns.EnergyEcon.54,33–49.
ofcrudeoil,gold,andbitcoin.Q.Rev.Econ.Finance84,398–406. Sadorsky,P.,2012.Correlationsandvolatilityspilloversbetweenoilpricesandthestock
Gu,X.,Zhu,Z.,Yu,M.,2021.ThemacroeffectsofGPRandEPUindexesovertheglobal pricesofcleanenergyandtechnologycompanies.EnergyEcon.34(1),248–255.
oilmarket-arethetwotypesofuncertaintyshockalike?EnergyEcon.100,105394. Saeed,T.,Bouri,E.,Alsulami,H.,2021.Extremereturnconnectednessandits
Hammoudeh,S.,Mokni,K.,Ben-Salha,O.,Ajmi,A.N.,2021.Distributionalpredictability determinantsbetweenclean/greenanddirtyenergyinvestments.EnergyEcon.96,
betweenoilpricesandrenewableenergystocks:istherearolefortheCOVID-19 105017.
pandemic?EnergyEcon.103,105512. Sukcharoen,K.,Zohrabyan,T.,Leatham,D.,Wu,X.,2014.Interdependenceofoilprices
Hanif,W.,Ko,H.E.,Pham,L.,Kang,S.H.,2023.Dynamicconnectednessandnetworkin andstockmarketindices:acopulaapproach.EnergyEcon.44,331–339.
thehighmomentsofcryptocurrency,stock,andcommoditymarkets.Financ.Innov. Tiwari,A.K.,Nasreen,S.,Hammoudeh,S.,Selmi,R.,2021.Dynamicdependenceofoil,
9(1),1–40. cleanenergyandtheroleoftechnologycompanies:newevidencefromcopulaswith
Henriques,I.,Sadorsky,P.,2008.Oilpricesandthestockpricesofalternativeenergy regimeswitching.Energy220,119590.
companies.EnergyEcon.30(3),998–1010. Tiwari,A.K.,Abakah,E.J.A.,Karikari,N.K.,Hammoudeh,S.,2022.Time-varying
Hong,H.,Lim,T.,Stein,J.C.,2000.Badnewstravelsslowly:size,analystcoverage,and dependencedynamicsbetweeninternationalcommoditypricesandAustralian
theprofitabilityofmomentumstrategies.J.Financ.55(1),265–295. industrystockreturns:aperspectiveforportfoliodiversification.EnergyEcon.108,
Kocaarslan,B.,Soytas,U.,2019.Dynamiccorrelationsbetweenoilpricesandthestock 105891.
pricesofcleanenergyandtechnologyfirms:theroleofreservecurrency(U.S. Tiwari,A.K.,Trabelsi,N.,Abakah,E.J.A.,Nasreen,S.,Lee,C.C.,2023.Anempirical
dollar).EnergyEcon.84,104502. analysisofthedynamicrelationshipbetweencleananddirtyenergymarkets.Energy
Kumar,S.,Managi,S.,Matsuda,A.,2012.Stockpricesofcleanenergyfirms,oiland Econ.124,106766.
carbonmarkets:avectorautoregressiveanalysis.EnergyEcon.34(1),215–226. Uddin,G.S.,Rahman,M.L.,Hedstro¨m,A.,Ahmed,A.,2019.Cross-quantilogram-based
Lastrapes,W.D.,Wiesen,T.F.,2021.Thejointspilloverindex.Econ.Model.94,681–691. correlationanddependencebetweenrenewableenergystockandotherassetclasses.
Lv,X.,Dong,X.,Dong,W.,2021.Oilpricesandstockpricesofcleanenergy:new EnergyEcon.80,743–759.
evidencefromChinesesubsectoraldata.Emerg.Mark.Financ.Trade57(4), Wang,X.,Li,J.,Ren,X.,Bu,R.,Jawadi,F.,2023.Economicpolicyuncertaintyand
1088–1102. dynamiccorrelationsinenergymarkets:assessmentandsolutions.EnergyEcon.
Lyu,Y.,Tuo,S.,Wei,Y.,Yang,M.,2021.Time-varyingeffectsofglobaleconomicpolicy 117,106475.
uncertaintyshocksonoilpricevolatility:newevidence.Res.Policy70,101943. Xia,T.,Ji,Q.,Zhang,D.,Han,J.,2019.Asymmetricandextremeinfluenceofenergy
Managi,S.,Okimoto,T.,2013.Doesthepriceofoilinteractwithcleanenergypricesin pricechangesonrenewableenergystockperformance.J.Clean.Prod.241,118338.
thestockmarket?Jpn.WorldEcon.27,1–9. Xiao,J.,Zhou,M.,Wen,F.,Wen,F.,2018.Asymmetricimpactsofoilpriceuncertainty
Mitchell,M.L.,Mulherin,J.H.,1994.Theimpactofpublicinformationonthestock onChinesestockreturnsunderdifferentmarketconditions:evidencefromoil
market.J.Financ.49(3),923–950. volatilityindex.EnergyEcon.74,777–786.
Naeem,M.A.,Peng,Z.,Suleman,M.T.,Nepal,R.,Shahzad,S.J.H.,2020.Timeand Yahya,M.,Kanjilal,K.,Dutta,A.,Uddin,G.S.,Ghosh,S.,2021.Cancleanenergystock
frequencyconnectednessamongoilshocks,electricityandcleanenergymarkets. priceruleoilprice?Newevidencesfromaregime-switchingmodelatfirstand
EnergyEcon.91,104914. secondmoments.EnergyEcon.95,105116.
Nasreen,S.,Tiwari,A.K.,Eizaguirre,J.C.,Wohar,M.E.,2020.Dynamicconnectedness Zhang,G.,Liu,W.,2018.Analysisoftheinternationalpropagationofcontagionbetween
betweenoilpricesandstockreturnsofcleanenergyandtechnologycompanies. oilandstockmarkets.Energy165,469–486.
J.Clean.Prod.260,121015. Zhang,Y.J.,Yan,X.X.,2020.TheimpactofU.S.economicpolicyuncertaintyonWTI
Nekhili,R.,Bouri,E.,2023.Higher-ordermomentsandco-moments’contributionto crudeoilreturnsindifferenttimeandfrequencydomains.Int.Rev.Econ.Financ.69,
spilloveranalysisandportfolioriskmanagement.EnergyEcon.119,10659. 750–768.
Patton,A.J.,2004.Ontheout-of-sampleimportanceofskewnessandasymmetric Zhang,H.,Jin,C.,Bouri,E.,Gao,W.,Xu,Y.,2023.Realizedhigher-ordermoments
dependenceforassetallocation.J.Financ.Econ.2(1),130–168. spilloversbetweencommodityandstockmarkets:evidencefromChina.J.Commod.
Pham,L.,2019.Doallcleanenergystocksrespondhomogeneouslytooilprice?Energy Mark.30,100275.
Econ.81,355–379.
40