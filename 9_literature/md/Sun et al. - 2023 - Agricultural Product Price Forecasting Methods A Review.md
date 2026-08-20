agriculture
Review
Agricultural Product Price Forecasting Methods: A Review
FeihuSun1,2,3,XianyongMeng1,2,3,YanZhang1,2,3,YanWang1,2,3,HongtaoJiang1,2,3andPingzengLiu1,2,3,*
1 SchoolofInformationScienceandEngineering,ShandongAgriculturalUniversity,Taian271018,China
2 KeyLaboratoryofHuang-Huai-HaiSmartAgriculturalTechnology,MinistryofAgricultureandRuralAffairs,
Taian271018,China
3 AgriculturalBig-DataResearchCenter,ShandongAgriculturalUniversity,Taian271018,China
* Correspondence:pzliu@sdau.edu.cn
Abstract:Agriculturalpricepredictionisahotresearchtopicinthefieldofagriculture,andaccurate
predictionofagriculturalpricesiscrucialtorealizethesustainableandhealthydevelopmentofagri-
culture.Itexplorestraditionalforecastingmethods,intelligentforecastingmethods,andcombination
modelforecastingmethods,anddiscussesthechallengesfacedinthecurrentresearchlandscapeof
agriculturalcommoditypriceprediction.Theresultsofthestudyshowthat:(1)Theuseofcombined
modelsforagriculturalproductpriceforecastingisafuturedevelopmenttrend,andexploringthe
combinationprincipleofthemodelsisakeytorealizeaccurateforecasting;(2)theintegrationofthe
combinationofstructureddataandunstructuredvariabledataintothemodelsforpriceforecasting
is a future development trend; and (3) in the prediction of agricultural product prices, both the
accuracyofthevaluesandtheprecisionofthetrendsshouldbeensured. Thispaperreviewsand
analyzesthemethodsofagriculturalproductpricepredictionandexpectstoprovidesomehelpfor
thedevelopmentofresearchinthisfield.
Keywords: price forecasting; combined models; intelligent prediction methods; agricultural
productprice
1. Introduction
Price information is the vane of variations in the agricultural product market, the
frequentandlargefluctuationsofpriceshavegreatlyaffectedthelivelihoodofthecountry
Citation:Sun,F.;Meng,X.;Zhang,Y.; andsocialstability. Agriculturalpriceforecastingisnotonlyabouttheeconomicstability
Wang,Y.;Jiang,H.;Liu,P. ofindividualcountriesorregions,butalsoabouttheglobalbalanceoffoodsupplyand
AgriculturalProductPrice demand. Astheworld’spopulationcontinuestogrow,foodsecurityhasbecomeaglobal
ForecastingMethods:AReview. concern. Accurate forecasting of agricultural commodity prices can help international
Agriculture2023,13,1671. https:// organizations,governments,andagribusinessestomaketimelyresponsestoensureade-
doi.org/10.3390/agriculture13091671
quatefoodsupplyandmaintainglobalfoodsecurity. Therefore,thestudyofagricultural
Received:5July2023 priceforecastingmethodsisofspecialimportanceforimprovingthesafetyofagricultural
Revised:13August2023 productsintermsofquantityandpromotingeconomicandsocialdevelopment[1].
Accepted:15August2023 Comparedtogeneralcommodityprices,agriculturalpricesareinfluencedbymore
Published:24August2023 complex factors and exhibit irregular fluctuations, such as non-stationary and nonlin-
ear [2,3]. Frequent and sharp fluctuations in agricultural commodity prices may affect
nationalandglobalfoodsecurity[4]. Researchershavefoundthatsupplyanddemand
haveasignificantimpactonagriculturalpriceformation. Productionaffectssupplyand
Copyright: © 2023 by the authors.
demand,whichleadstopricevolatility[5–7]. Inaddition,agriculturalcommodityprices
Licensee MDPI, Basel, Switzerland.
are influenced by factors, such as labor costs, growing costs, and international market
This article is an open access article
environment. Scholars have also conducted studies on the transmission mechanism of
distributed under the terms and
prices and found that agricultural price transmission is asymmetric [8,9]. Factors such
conditionsoftheCreativeCommons
as climate and policy also affect agricultural prices to varying degrees. Gu et al. [10]
Attribution(CCBY)license(https://
conductedastudyonthefactorsaffectingthepricesofagriculturalproductsandfound
creativecommons.org/licenses/by/
that temperature, hours of sunshine, and epidemics all have an impact on prices. The
4.0/).
Agriculture2023,13,1671.https://doi.org/10.3390/agriculture13091671 https://www.mdpi.com/journal/agriculture

Agriculture2023,13,1671 2of20
resultsandcontributionsmadebymanyscholarsonthecharacteristicsofagriculturalprice
fluctuationsandtheinfluencingfactorshavelaidasolidfoundationforachievingaccurate
forecastingofagriculturalprices.
Agriculturalproductpriceforecastingreferstotheuseofscientificmethodstoestimate
orjudgethetrendandlevelofagriculturalproductpricechangesoveraperiodoftimein
thefuturebasedonhistoricaldataandcurrentinformation. Agriculturalpriceforecasting
methodsaredividedintoqualitativeanalysisandquantitativeanalysis.Qualitativeanalysis
isbasedonthefullgraspofmarketpriceinformation,usingexperiencetomakeabasic
judgmentonthedirectionoftheoverallpricetrend;quantitativeanalysisisbasedonthe
collationofobtainedmarketpriceinformation,usingcertainforecastingmethodstomake
aspecificquantitativejudgmentonthenumberormagnitudeofcommoditypricechanges.
Quantitative analysis is the main analysis method currently used in agricultural price
forecasting,mainlydividedintoregressionanalysis(causalanalysis),timeseriesanalysis
method,machinelearningmethodsandcombinedmodels,andfromtheperspectiveof
variablesaredividedintounivariateforecastingandmultivariateforecasting.
Agriculturalproductpricesareaffectedbyavarietyoffactors,suchassupplyand
demand,climatechange,policyintervention,marketcompetition,internationaltrade,etc.
Pricesandtherelationshipsbetweenfactorsareoftennonlinear,dynamicanduncertain,and
difficulttodescribeandquantifywithsimplemathematicalmodels. Traditionalmethods
arerelativelysimpleandeasytounderstandandimplement,butthepredictioneffectis
poorfornonlinear,non-smooth,andhigh-dimensionaldata,andtheyrequiremoreapriori
knowledgeandassumptions.Intelligentmethodsareabletohandlecomplexdatawithhigh
accuracyandgeneralization,butrequirelargeamountsofdataandcomputationalresources,
andlackinterpretabilityandstability. Therefore,understandingthecharacteristicsofeach
forecastingmethodandchoosingtheappropriatealgorithmtobuildapriceforecasting
modelisakeyissuetobesolvedforgoodagriculturalpriceforecastingresearch.
Thispaperdescribesthedevelopmentofagriculturalproductpriceforecastingmeth-
ods from single model to combination model, from traditional forecasting methods to
intelligentforecastingmethods. Anintroductionoftheadvantagesanddisadvantagesof
differentmethodswithspecificexamplesispresentedandthefuturedevelopmenttrend
ofagriculturalproductpricepredictionmethodsisdiscussed. Thispaperanalyzesand
discussesthedevelopmentstatusofagriculturalpriceforecastingmethodsonthebasisof
reviewingthehistoryofthedevelopmentofthisfield. Itsummarizesthecurrentproblems
andchallengesfacedbyagriculturalpriceforecastingmethods,withaviewtoproviding
Agriculture 2023, 13, x FOR PEER REVIEW 3 of 24
certainhelpandguidanceforthedevelopmentofthefieldofagriculturalpriceforecasting.
Figure1showsthestructureofthispaper.
Figure 1. The sFtriugcutruere1 .oTf htheiss tpruacpteurr.e ofthispaper.
2. Traditional Forecasting Method
2.1. Regression Analysis Forecasting Method
Regression analysis was founded by Galton, a famous British anthropologist and stat-
istician, when he studied the paternal height relationship in the UK. In 1917, Moore [11]
marked the shift from qualitative to quantitative methods for agricultural price forecast-
ing by constructing a multiple linear regression model to forecast cotton production and
prices. Regression analysis predicts prices by constructing a mathematical model between
prices and influencing factors. The regression analysis method mainly includes linear re-
gression model (LR), generalized linear regression model (GLR), nonlinear regression
model (NLR), multiple adaptive regression splines (MARS), generalized additive model
(GAM), etc. Limitations and Challenges: Regression models require a substantial amount
of data to estimate model parameters accurately and reliably. They also assume that data
are devoid of errors, outliers, and multicollinearity (high correlation among explanatory
variables). If the data exhibit nonlinearity, seasonality, or cyclical patterns, or if there are
structural changes or external shocks in the data-generating process, regression models
might struggle to perform effectively. Regression models may also suffer from overfitting
(fitting noise in the data rather than the signal) or underfitting (failure to capture the com-
plexity of the data) issues, thereby impacting their predictive performance and generali-
zation ability. Suitability: Regression models are suitable for short-term or medium-term
forecasting problems where explanatory variables are known or can be reasonably esti-
mated. They are also appropriate for problems where the response variable maintains a
linear or simple nonlinear relationship with explanatory variables, and where the data
pattern remains relatively stable and consistent over a period of time.
Ma et al. [12] established a VAR model to predict the short-term price of hogs based
on the analysis of factors affecting hog prices. The results indicate that the VAR model
performs well in predicting short-term prices of live pigs. But the prediction performance
was poor when medium- and long-term forecasts were made for hog prices. Ge et al. [13]
studied changes in corn prices and factors affecting them. They developed two types of
models to forecast maize prices: A univariate nonlinear regression model using time as
the independent variable and a multiple linear regression model incorporating produc-
tion, consumption, import, and export volumes as independent variables. While the uni-
variate nonlinear regression models provide reasonable corn price predictions, they lack
a comprehensive examination of the intricate internal factors driving price changes. Con-
sequently, the accuracy of these predictions is significantly compromised, rendering them
suitable only for rough estimations. The foundational assumption of local pattern inde-
pendence leads to some deviation when applying the regression analysis forecasting
equation to medium- to long-term predictions. Furthermore, the complexity of factors in-
fluencing agricultural commodity prices poses challenges in encompassing all relevant

Agriculture2023,13,1671 3of20
2. TraditionalForecastingMethod
2.1. RegressionAnalysisForecastingMethod
Regression analysis was founded by Galton, a famous British anthropologist and
statistician,whenhestudiedthepaternalheightrelationshipintheUK.In1917,Moore[11]
markedtheshiftfromqualitativetoquantitativemethodsforagriculturalpriceforecasting
byconstructingamultiplelinearregressionmodeltoforecastcottonproductionandprices.
Regressionanalysispredictspricesbyconstructingamathematicalmodelbetweenprices
andinfluencingfactors. Theregressionanalysismethodmainlyincludeslinearregression
model(LR),generalizedlinearregressionmodel(GLR),nonlinearregressionmodel(NLR),
multiple adaptive regression splines (MARS), generalized additive model (GAM), etc.
LimitationsandChallenges: Regressionmodelsrequireasubstantialamountofdatato
estimatemodelparametersaccuratelyandreliably. Theyalsoassumethatdataaredevoid
oferrors,outliers,andmulticollinearity(highcorrelationamongexplanatoryvariables).
Ifthedataexhibitnonlinearity,seasonality,orcyclicalpatterns,oriftherearestructural
changesorexternalshocksinthedata-generatingprocess,regressionmodelsmightstruggle
toperformeffectively. Regressionmodelsmayalsosufferfromoverfitting(fittingnoise
inthedataratherthanthesignal)orunderfitting(failuretocapturethecomplexityofthe
data) issues, thereby impacting their predictive performance and generalization ability.
Suitability: Regression models are suitable for short-term or medium-term forecasting
problemswhereexplanatoryvariablesareknownorcanbereasonablyestimated. They
arealsoappropriateforproblemswheretheresponsevariablemaintainsalinearorsimple
nonlinear relationship with explanatory variables, and where the data pattern remains
relativelystableandconsistentoveraperiodoftime.
Maetal.[12]establishedaVARmodeltopredicttheshort-termpriceofhogsbased
ontheanalysisoffactorsaffectinghogprices. TheresultsindicatethattheVARmodel
performswellinpredictingshort-termpricesoflivepigs. Butthepredictionperformance
waspoorwhenmedium-andlong-termforecastsweremadeforhogprices. Geetal.[13]
studied changes in corn prices and factors affecting them. They developed two types
ofmodelstoforecastmaizeprices: Aunivariatenonlinearregressionmodelusingtime
as the independent variable and a multiple linear regression model incorporating pro-
duction,consumption,import,andexportvolumesasindependentvariables. Whilethe
univariatenonlinearregressionmodelsprovidereasonablecornpricepredictions, they
lackacomprehensiveexaminationoftheintricateinternalfactorsdrivingpricechanges.
Consequently,theaccuracyofthesepredictionsissignificantlycompromised,rendering
themsuitableonlyforroughestimations. Thefoundationalassumptionoflocalpattern
independenceleadstosomedeviationwhenapplyingtheregressionanalysisforecasting
equation to medium- to long-term predictions. Furthermore, the complexity of factors
influencingagriculturalcommoditypricesposeschallengesinencompassingallrelevant
variablesduringthemodelingprocess. Nonetheless,theregressionanalysismethodexcels
inrevealingintrinsicpatterns,relationships,andcorrelationsamongfactors,contributing
to its relatively high precision. Its straightforward comprehension and applicability in
refining basic models make it a popular choice for short-term agricultural commodity
priceforecasting.
2.2. GrayModelPredictionMethod
Graymodelisamethodforpredictingsystemscontaininguncertainties. Thismethod
isasemiparametricmodelthatusesasmallamountofdatatoconstructdifferentialequa-
tionsdescribingtrendsinthedata. Thegoalistoestimatetheparametersoftheequation
usingleastsquaresanduseittopredictfuturevaluesofthevariable. Someexamplesof
graymodelsareGM(1,1),GM(2,1),andDGM(2,1). LimitationsandChallenges: Gray
modelsrequirethedatatohaveadegreeofregularityandmonotonicity,meaningthatthey
steadilyincreaseordecreaseovertime. Theyalsoassumethatthedatahaveanexponential
lawdistribution,whichmeanstheygrowordecayexponentiallyovertime. Graymodels
maynotworkwellifthedatahaveirregular,non-monotonic,ornon-exponentialpatterns,

Agriculture2023,13,1671 4of20
oriftherearesuddenchangesorfluctuationsinthedata. Graymodelsmayalsosuffer
fromlowaccuracyandpooradaptability,whichaffectstheirpredictiveperformanceand
robustness. Applicability: Graymodelsaresuitableforlong-termforecastingproblems
wheredataarescarceorincomplete. Theyarealsosuitableforproblemswherevariables
havesmoothandmonotonictrends, andwheredata patterns arerelativelysimpleand
stableovertime.
LuoHanGuoisakindoffruitproducedinGuangxi,China.Fengetal.[14]constructed
aGM(1,1)modeltopredictitsprice. ItwasfoundthattheGM(1,1)modelcouldbetter
portrayitspricechangepatternduetoitshighin-samplesimulationaccuracy.Itisconcluded
thattheGM(1,1)modelhastheadvantagesofrequiringlessdata,highfittingandprediction
accuracy,andeasyprogrammingimplementationinthepredictionproblemforthepriceof
LuoHanGuo,relativetothepredictionmodels,suchasregressionmodelsandtimeseries
models,andcanprovideascientificreferenceforthepredictionofthepriceofLuoHanGuo.
2.3. TimeSeriesForecastingMethod
Timeseriesanalysisisacommonlyusedunivariateforecastingmethod,whichrefers
toastatisticalmethodofmodelingandanalyzingagriculturalcommoditypricesbasedon
theregularitypresentedbythepriceitselfovertime,andextrapolatingfuturedatafrom
existing data. The time series analysis method mainly includes autoregressive moving
average(ARMA),autoregressiveintegratedmovingaverage(ARIMA),seasonalautoregres-
siveintegratedmovingaverage(SARIMA),autoregressiveconditionalheteroskedasticity
(ARCH),generalizedautoregressiveconditionalheteroskedasticity(GARCH),etc.
Theadvantageoftimeseriesanalysisisthatitissimpleandstraightforward. Itrelies
entirelyonhistoricaldata,andthetimeseriesmethodologyisaveryflexibleorshort-term
forecasting.Themethodperformswellwhenthedatashowclearseasonal,trend,andcyclical
patterns. Modelsandforecastsarecreatedwithouttheneedtoconsiderotherinfluencing
factors.Timeseriesforecastingmethodsassumethatthefuturepatternofchangeisthesameas
thehistoricalpatternofchange,butinpractice,manytimestheyareaffectedbyexternalfactors,
leadingtobiasedorfailedforecasts.Climatechange,policyimplementation,andunforeseen
eventsmayleadtostructuralchangesinthetimeseries,makinghistoricaldatanotagood
reflectionofthefuture.Themethodrequirescomplexsteps,suchassmoothnesstestingofthe
data,parameterestimationandmodelselection,whichoftenrequirespecializedknowledge
and skills and can be subjective and uncertain. For example, an ARIMA model requires
determiningthevaluesofp,d,andq. Thesevaluesmayaffectmodelfittingeffectiveness
andforecastingaccuracy.Inaddition,timeseriesforecastingmethodsoftensufferfromerror
accumulationwhenperformingmulti-stepforecasts,resultinginpoorlong-termforecasts.For
example,ifamovingaveragemethodisusedtoforecastdataatseveralpointsinthefuture,
datafromearlierforecastswillneedtobeusedasinput,whichwillshifttheerrorfromearlier
tolater,makingtheforecastsincreasinglyinaccurate. Table1summarizescommonlyused
forecastingmethodsfortimeseriesanalysis.
Table1.Commontimeseriesanalysismethods.
Model Principle Characteristic Reference
TheARmodelassumesthatthecurrent
Capturingthedynamicpropertiesand
AR(Autoregressive observationsarealinearcombinationofpast
evolutionarytrendsoftimeseries;handlingtime [15]
Model) observationsanduseshistoricalobservationsto
seriesdatawithlongmemory.
predictfuturevalues.
Capableofcapturingtherandomnessand
Reflectsnewobservationsbyconstantlyupdating
MA(MovingAverage uncertaintyofpricefluctuations,especiallywhen
themovingaverage.Aweightedaverageofthe -
Model) marketsupplyanddemandconditionsare
mean,whitenoiseerrors,andtheirlaggedvalues.
unstable.

Agriculture2023,13,1671 5of20
Table1.Cont.
Model Principle Characteristic Reference
ThebasicprincipleoftheARIMAmodelistouse
Abilitytocapturetimeseriestrendingand
pastdatapoints,errors,anddifferenceoperations
ARIMA(Autoregressive seasonality.Essentiallyonlycaptureslinear
topredictfuturedatapoints.Themodelminimizes
IntegratedMoving relationships,notnonlinearrelationships.Itis [16]
thepredictionerrorbyadjustingtheparametersof
Average) requiredthatthetimingdataarestableorare
theautoregressivecoefficients,movingaverage
stablebydifferentialdifferentiation.
coefficients,anddifferenceoperations.
Itcanreducethenoiseandseasonalityofthetime
Itisbasedontheprincipleofusinghistoricaldata
series,thusimprovingpredictionaccuracyand
topredictfuturetrendsbyconstantlyadjustingthe
ES(Exponential stability.Predictingnewtrendsandcyclesrequires
weightsinorderthatthemostrecentdatahavea [17,18]
Smoothing) constantupdatingofthemodel.Thechoiceof
greaterimpactonthepredictionresultstoreflect
smoothingconstantsissensitiveandlesseffective
thetrendandperiodicityofthetimeseriesdata.
fortimeserieswithstrongperiodicfluctuations.
3. IntelligentPredictionMethod
Traditionalagriculturalpriceforecastingmethods,suchasregressionanalysis,time
series forecasting, and gray models, are usually applicable to the situation where the
variablesareindependent,thedataobeynormaldistribution,andthereisalinearorsimple
nonlinearrelationship. However,realisticagriculturalpriceforecastingoftenfailstomeet
theseconditions,andoftenpresentscomplexproblems,suchashighdimensionality,small
samplesize,andnonlinearity.
Comparedwitheconometricandmathematical-statisticalmethods,intelligentfore-
castingmethodshavefewerrestrictionsandassumptionsinmodelingandcaneffectively
modelnonlinearrelationshipsinpriceseries. Traditionalmachinelearningmethods,such
asdecisiontrees,supportvectormachines,andplainBayes,havetheadvantagesofsimplic-
ity,fasttrainingandrobustness,buttheyhavelimitedabilitytohandlecomplexnonlinear
relationships,requiremanualselectionandextractionoffeatures,andhaveinsufficient
generalizationability. Deeplearningmodels,withtheirpowerfulexpressionandfeature
extractioncapabilities,canextracteffectivefeatureinformationfromtheoriginalsequence
withoutrelyingonfeatureengineeringandhavebetterprocessingabilityfornonlinear
relationships in the sequence when supervision is effective, data quantity is sufficient,
and data quality is high. However, the deep learning method has limitations, such as
highdatavolumerequirement,difficultparameteradjustment,easyoverfitting,andpoor
interpretability. Thismoduledescribestwotraditionalmachinelearningmethods, sup-
portvectormachinesandplainBayes,andtheapplicationofneuralnetworkmethodsin
agriculturalpriceprediction.
3.1. SupportVectorMachine-BasedPredictionMethod
Thesupportvectormachine(SVM)isamachinelearningapproachrootedinstatis-
ticallearningtheory[19]. IthingesonVCdimensionaltheory,theprincipleofstructural
riskminimization[20,21],andrepresentsthepioneeringalgorithmgroundedingeomet-
ricdistance[22]. Servingasasmall-samplelearningtechniquewitharobusttheoretical
foundation,anSVM’sfinaldecisionfunctionisinfluencedbyonlyahandfulofsupport
vectors. Its computational complexity hinges on these vectors rather than the sample
space’sdimensionality,sidesteppingtheso-called“dimensionaldisaster”. Wangetal.[23]
harnessedSVMtopredictthenonlinearfacetofgarlicprices,couplingitwithARIMAfor
linearpriceprediction,yieldingaccurateresults. Nevertheless,SVMdoeshavedrawbacks,
includingdiminishedperformancewhendatafeatures(dimensions)surpassthesample
size, sensitivity to parameters and kernel functions. Consequently, approaches like pa-
rameteroptimizationarefrequentlyemployedtoenhanceSVMpredictionperformance.
Duanetal.[24]employedageneticalgorithmtoidentifyoptimalparametercombinations
forasupportvectorregressionmodel. Withtheseoptimizedparameters,theyconstructed
asupportvectorregressionmodelforpredictingfishprices, yieldingpreciseoutcomes

Agriculture2023,13,1671 6of20
withminorerrors. SVR’sremarkableabilitytomanagehigh-dimensional,nonlinear,and
small-sampledatapositionsisavitaltechniqueinagriculturalpriceprediction.
3.2. BayesianNetwork-BasedPredictionMethod
A Bayesian network is essentially a directed acyclic graph that uses probabilistic
networkstomakeuncertaintyinferences. TheexcellenceofBayesiannetworksinsolving
agriculturalpriceforecastingaswellasotheragriculturalproblemsstemsmainlyfromthe
followingkeyfeatures: (1)Bayesiannetworkscanhandleincompletedatasets;(2)Bayesian
networksallowonetounderstandtherelationshipsbetweenvariablesandquantifythe
strength of these relationships; (3) the ability to combine quantitative and qualitative
data; (4)theabilitytocombineexpertknowledgeanddataintoBayesiannetwork; and
(5)Bayesianmethodscanrelativelyeasilyavoiddataoverfittingduringthelearningprocess.
Putri [25] used Bayesian network algorithms as a data mining classification method to
predictpeppercommoditypricesinBandungregionbasedonweatherinformation. One
disadvantageofBayesiannetworksisthattheydonotsupportringnetworks[26],which
wouldweakentherobustinferencecapabilityofthenetwork, andthislimitationisnot
friendly to static Bayesian networks. Dynamic Bayesian network (DBN) is a dynamic
modelamalgamatingprobabilitytheoryandinfluencediagram. Itcombinesatime-varying
hiddenMarkovmodelwithatraditionalstaticBayesiannetwork,capturingbenefitsfrom
bothwhilesidesteppingtheirlimitationsthroughdynamicadaptabilityovertimeandthe
incorporation of new states [27]. Ma Zaixing [28] used the PC algorithm to learn from
data,constructaccordingtoexpertknowledge,andcombineexpertknowledgeandPC
algorithmtoperformstructurallearning. Afterobtainingtheinitialstructure,headjusted
theobtainedinitialstructuretoobtainthenetworkstructureofthemodel,andthenused
the EM algorithm to perform parameter learning. Moreover, he obtained a complete
dynamicBayesiannetworkmodelforpriceprediction,andselectedthebestmodelbased
on the prediction results to predict the price and output of live pigs. The results show
thatthepredictioneffectisbetterthanthecontrolgroup’sARIMA,SVM,andBPneural
networkmodels.
3.3. NeuralNetwork-BasedPredictionMethod
Neuralnetworksarecommonlyreferredtoasartificialneuralnetworks(ANN).They
constituteacomplexnonlinearnetworksystemcomposedofnumerousprocessingunits
interconnectedinamannerresemblingbiologicalneurons. Neuralnetworksexhibitrobust
nonlinearfittingcapabilities,enablingthemtomapintricatenonlinearrelationships. Fur-
thermore,theirlearningrulesaresimple,makingthemeasilyimplementableoncomputers.
Theypossessstrongrobustness,memory,nonlinearmappingabilities,andpowerfulself-
learningcapabilities,showcasinguniqueadvantagesinaddressingagriculturalcommodity
pricepredictionchallenges. In1987,LapedesandFarber[29]pioneeredtheapplicationof
neuralnetworkstoforecasting,markingtheinceptionofneuralnetworkpredictions. In
1993,Kohzadietal.[30]wereamongthefirsttoemployfeed-forwardneuralnetworksfor
predictingUSwheatandcattleprices. Theycomparedthepredictiveresultswiththose
fromARIMA,concludingthatneuralnetworksexhibitedsuperiorturningpointprediction
capabilitiesandachievedmoreaccuratepriceforecasting.
Asbigdataandartificialintelligencetechnologyadvance,neuralnetworksfindin-
creasinglywideapplicationintheagriculturaldomain[31]. Intherealmofpriceprediction,
prevalentneuralnetworkmodelsareasfollows(Table2,alongwithexamples,summarizes
theapplicationsofneuralnetworksinagriculturalcommoditypriceprediction):
• Backpropagation (BP) Networks [32–34]: BP networks are easy to implement and
understand. However,itiseasytofallintolocaloptimalsolutionsandthetraining
speedisrelativelyslow.
• RadialBasisFunctionNeuralNetworks(RBFNN)[35,36]: ABPnetworkisaglobal
approximationofanonlinearmapping,whereasanRBFnetworkisalocalapproxima-
tionofanonlinearmappingandisfastertotrain. RBFcanhandlecomplexnonlinear

Agriculture2023,13,1671 7of20
relationships and has good generalization ability. However, it is sensitive to the
networkstructureandhyperparameters,andthetrainingandtuningarerelatively
complicated. Whentheprobleminvolvescomplexnonlinearrelationshipsandthereis
enoughtrainingdata,youcantrytouseRBFneuralnetwork.
• LongShort-TermMemoryNetworks(LSTM)[37,38]:LSTMneuralnetworkisaspecial
kindofrecurrentneuralnetworkthatsolvestheproblemsoflong-termdependency
andgradientvanishingbyintroducingstructures,suchasforgettinggates,inputgates,
andoutputgates,tocontroltheflowofinformationthroughtheunitstates. LSTM
neuralnetworkshavetheabilitytomemorizeandcapturelong-termdependencies.
Therefore,LSTMisagoodchoicewhenthepredictionprobleminvolvestimeseries
data,especiallywithlong-termdependencies.
• Convolutional Neural Networks (CNN) [39]: CNN is a multi-layer feed-forward
neuralnetworkthatextractslocalandglobalfeaturesfromdatathroughstructures,
suchasconvolutional,pooling,andfullyconnectedlayerstoenableautomaticfeature
learning and abstraction. In price prediction tasks, CNNs can learn and capture
importantfeatures,suchastimeseries,datatrends,periodicity,etc.,intheinputdata.
Marketpricesareusuallyaffectedbyacombinationofseveralfactors,andCNNscan
betterhandlethesecomplexnonlinearrelationships.
• Chaos Neural Networks (CNN) [40,41]: Chaos neural network (CNN) is a kind of
intelligent information processing system that combines chaos theory and neural
network. Chaotic neural networks exploit the sensitivity and unpredictability of
chaoticphenomenatoenhancethelearningandgeneralizationcapabilitiesofneural
networks,thusimprovingtheaccuracyofpredictionandmodeling. Byintroducing
methods,suchaschaoticnoiseorlogisticmaps,chaoticneuralnetworksareableto
avoidneuralnetworksfromfallingintolocalminimatoacertainextent,thusspeeding
upthetrainingprocessandincreasingtheconvergencerate.
• Extreme Learning Machines (ELM) [42]: The extreme learning machine is a feed-
forward neural network that was first proposed by Professor Huang Guangbin of
NanyangTechnologicalUniversityinSingaporein2006. ELMhastheadvantagesof
fasttraining,highgeneralizationability,andsimpleimplementation.
• WaveletNeuralNetworks(WNN)[43,44]:Waveletneuralnetwork(WNN)isamethod
basedonwavelettransformandneuralnetwork. Bydecomposingtheoriginaldata
into wavelet coefficients at different scales, it is able to effectively extract a variety
of features in the data, such as trend, cycle, seasonality, etc. WNN combines the
powerfulfittingabilityofneuralnetworks,whichiscapableofnonlinearmapping,
thusachievingaccuratepredictionoffutureprices. However,highcomplexityand
highdatarequirementsaretheunavoidabledrawbacksofthismethod.

Agriculture2023,13,1671 8of20
Table2.Applicationexamplesofneuralnetwork-basedpriceforecastingforagriculturalproducts.
Reference [32] [35] [38] [39] [41] [42] [44]
Models/Algorithms BPNN RBFNN LSTM CNN Chaoticneuralnetworks ELM WNN
Waveletneuralnetwork
Iteffectivelyovercomesthe combinestheadvantages
problemofgradient Thealgorithmcanrandomly ofneuralnetworkand
vanishingcausedbythe generatetheinputweightsand waveletfunction,using
Ithasbetterapproximation increaseinnetworklayers TheeffectivenessofCNN hiddenlayerthresholdsrequired Morletwaveletasthe
Theoutputofthenetwork
ability,classificationability, inRNN.Thismodelis infeatureextractionand bytheneuralnetworkwithout hiddenlayerbasis
notonlydependsonthe
andlearningspeedthan especiallysuitablefortasks autonomouslearningof multipleadjustments.Aslongas function,whichcanextract
currentinput,butalsoon
Strongnonlinearmapping BPneuralnetwork,simple withverylongtime nonlinearpatternsmakesit thenumberofhiddenlayernodes localdynamicfeatures,
thepastoutput.After
ability,highself-learning structure,concisetraining, intervalsanddelays,and performwellinimage isreasonable,auniqueoptimal andcanbuildalocal
training,thenetworkwill
andself-adaptiveability, fastlearningconvergence hasexcellentperformance. classificationandaudio solutioncanbeobtained.Its approximation
havebetteradaptabilityto
abilitytoapplylearning speed,canapproximate Researchresultsshowthat recognitiontasks.This parametersettingprocessis feed-forwardneural
nonlineardataandisvery
outcomestonew anynonlinearfunction, parametertuninghasa studyreviewsthefactors simple,doesnotneedtobe network,reducethe
suitableforpredicting
knowledge,andcertain andovercomethelocal largeimpactonthe thataffectcropyieldand adjustedrepeatedly,thetraining interferencebetween
Characteristic complex,non-stationary,
faulttolerance.Research minimumproblem. predictioneffectofLSTM proposesa3DCNNmodel speedissignificantlyimproved, nodes,andimprovethe
andnonlineartimeseries.
resultsshowthattheBP Researchresultsshowthat networkmodel,andthe topredictfuturecrop andthepredictionresultsare predictionaccuracy.This
Thedesignedpotatoprice
neuralnetworkmodelhas theinfluencingfactorsof mainparameterswith prices.Themodelhelps moreaccurate.Comparedwith studyuseswaveletneural
timeseriesprediction
thelong-termprediction soybeanpricearedifferent largeimpactinclude decision-makerstobetter traditionalneuralnetwork networktopredictthe
modelbasedondynamic
abilityforthe atdifferentpricelevels, iterationtimes,learning predictcroppricetrends learningalgorithms(suchasBP pricesoftwokindsof
chaoticneuralnetworkhas
futuresmarket. andtheconstructionofthis rate,windowsize,and andformulatestrategic algorithm),itovercomesthe Chinesemedicinal
clearadvantagesover
modelisbeneficialtothe networklayers.Compared plans,selecttradepartners, disadvantageoffallingintolocal materials,Radix
ARMAmodelinprediction
predictionof withARIMAmodel,MLP reducecosts,andsolve optimum.Thisstudyuses CodonopsisandAngelica
accuracyandperformance.
soybeanprice. modelandSVRmodel, foodinsecurityissues. PCA-ELMmodeltopredictgrain sinensis,andtheresults
LSTMnetworkmodelhas pricesandachievesgood showthattheprediction
higheraccuracyin predictionresults. errorisverysmallandthe
predictionresults. predictionaccuracyis
veryhigh.
Agricultural
Egg Soybeans Soybeans FivedifferentCrops Potato Grain Chineseherbalmedicine
Product
DomesticSoybean
Production,Soybean
Imports,GlobalSoybean Totalgrainproduction,percapita
Soybeanmealprice,cull Production,Domestic grainconsumption,averagegrain Plantingarea,yield,
Environmental,economic,
chickenprice,cornprice, SoybeanDemand, productionpriceindex,percapita province’sdisasterarea,
ObservedFeatures Pricetimeseries andcommoditytrading Pricetimeseries
eggseedlingprice,duck ConsumerPriceIndex, disposableincomeofurban hypefactor,andmarket
data
eggprice ConsumerConfidence residents,consumerpriceindex, demand
Index,MoneySupply, grainsownarea
ImportedSoybeanPort
DeliveryPrices
MeanAbsoluteError,Root
MeanAbsoluteError,Root
MeanAbsolutePercentage MeanAbsolutePercentage MeanSquareError,Mean
EvaluationMethod MeanSquareError,Mean MeanSquareError MeanSquareError Relativeerror
Error Error,Relativeerror AbsolutePercentageError,
AbsolutePercentageError
R-Square

Agriculture2023,13,1671 9of20
4. CombinedModelPredictionMethod
Inpracticalforecastingapplications,duetodifferentmodelingmechanismsandstart-
ingpoints,usuallythesameproblemcanhavedifferentforecastingmethods. Different
forecastingmethodsprovidedifferentusefulinformation,havetheirownadvantagesand
disadvantages,andtheyarenotmutuallyexclusive,butinterlinkedandcomplementary
toeachother. Amorescientificapproachistocombineanumberofdifferentforecasting
methodsappropriately,thusformingtheso-calledcombinedforecastingmethod. Combina-
tionforecastingmodelisacombinationoftwoormoremodelstoforecastvariables,which
canmakegreatuseofsampledatainformation,overcometheshortcomingssuchassingle
modelismoreinfluencedbyrandomfactors,andbemorecomprehensiveandaccurate,
whichwillfacilitatethesynthesisofusefulinformationprovidedbyvariousmethodsas
wellasimprovetheaccuracyofforecasting. Combinatorialforecastingisanimportant
researchbranchinthefieldofforecasting,andsinceBatesandGranger[45]firstproposed
thetheoreticalsystemofcombinatorialforecastingin1969,themethodhasthenreceivedex-
tensiveattentionfromscholarsathomeandabroad. Therearevariouswaystoclassifythe
combinatorialforecastingmodels. Inordertoclarifythecombinatorialforecastingmodels
inmoredetail,thisstudyintroducesthemintotwocategories: “traditionalcombinatorial
forecastingmodels”and“decomposition-combination”-basedforecastingmodels. Table3
summarizesseveralexamplesofcombinationmodels.
Table3.Examplesofapplicationofintegrationmethod.
| Reference | [46] | [23] | [47] | [48] | [49] | [50] |
| --------- | ---- | ---- | ---- | ---- | ---- | ---- |
Differentweights
|     | areassigned |     | Nonlinear |     |     |     |
| --- | ----------- | --- | --------- | --- | --- | --- |
combinationof
Integration accordingtothe Equalweighting Equalweighting Equalweighting
|     |     |     | different |     |     | Equalweightingmethod |
| --- | --- | --- | --------- | --- | --- | -------------------- |
Method predictionerrorofa method predictionresults method method
singlemodeland
byBPmodel
thensummed
Thevegetableprice
datawere
|     |     |     |     | decomposedinto     | First,decompose    | First,theempiricalmodal |
| --- | --- | --- | --- | ------------------ | ------------------ | ----------------------- |
|     |     |     |     | seasonal,trend,and | thepriceseriesinto | decomposition(EMD)      |
|     |     |     |     | residual           | nonlinearuptrend,  | methodisusedto          |
|     |     |     |     | componentsusing    | seasonaltrend,     | decomposeandintegrate   |
ARIMAforecasting theSTLmethod.In cyclicfluctuation themonthlyporkmarket
model,GM(1,1) thiscase,the trend,andrandom pricesintothreemodules:
forecastingmodel, AnARIMA-SVM derivedvariablesof fluctuationtrend High-frequencypart,
andcombined combined pricearecreatedin usingwavelet low-frequencypart,and
forecastingmodel forecastingmodelis theresidual analysis,then residualtermtosolvethe
Acombined
wereusedto establishedto component.Next, predictthe volatileandnon-stationary
AttLSTM-
Application forecastthe forecastgarlic ARIMA-BP theinputvariables nonlinearuptrend problem.Onthebasisof
wholesalemarket prices,andthe arelearnedthrough usingsupport thismethod,support
| Examples |     |     | forecastingmodel |     |     |     |
| -------- | --- | --- | ---------------- | --- | --- | --- |
priceofpotatoesin predictionresultsof toforecastcorn theattentionlayer vectormachine, vectormachine(SVM)is
2020,andtheresults ARIMAandSVM andattention predicttheseasonal appliedtoforecasteachof
prices
ofARIMAandGM aresummedto weightsare trend,cyclic thethreeintegrated
werecombined obtainthefinal assignedtoallinput fluctuationtrend modulestosolvethe
linearlytoobtain forecastvalue variables.Input andarbitrary nonlinearproblem.Finally,
thefinalforecast variableswith fluctuationtrend thepredictionresultsofthe
|     | value |     |     | attentionweights   | usingARIMA,and    | threeintegratedmodules |
| --- | ----- | --- | --- | ------------------ | ----------------- | ---------------------- |
|     |       |     |     | assignedare        | finallysumupthe   | areintegratedagainto   |
|     |       |     |     | learnedthroughthe  | predictedvaluesto | reconstructthepork     |
|     |       |     |     | LSTMmodeland       | getthepredicted   | marketpriceprediction  |
|     |       |     |     | vegetablepricesfor | value             | value                  |
thenextmonthare
predicted
Agricultural
|     | Potato | Garlic | Corn | Vegetable | Chinesecabbage | Pork |
| --- | ------ | ------ | ---- | --------- | -------------- | ---- |
Product
Vegetableprices,
weather
Foodpricesin
| Observed |     |     |     | informationfor |     |     |
| -------- | --- | --- | --- | -------------- | --- | --- |
Pricetimeseries Pricetimeseries different majorproduction Pricetimeseries Pricetimeseries
| Features |     |     | geographical |     |     |     |
| -------- | --- | --- | ------------ | --- | --- | --- |
areas,andvegetable
|     |     |     | areas | importandexport |     |     |
| --- | --- | --- | ----- | --------------- | --- | --- |
data

Agriculture2023,13,1671 10of20
Table3.Cont.
|     |              | Thestudyused   |              | Thestudy       |     | Thestudyevaluatedthe   |
| --- | ------------ | -------------- | ------------ | -------------- | --- | ---------------------- |
|     |              |                | Thestudy     | evaluatedthe   |     | modelusingRMSE,MAPE,   |
|     | Thestudyused | RMSEtoevaluate |              |                |     |                        |
|     |              |                | evaluatesthe | modelusingRMSE |     | anddirectionalsymmetry |
evaluationmethods, themodel performanceof andMAPE.The Thestudyevaluates methods.Theresultsshow
|     | suchasabsolute   | performance.The   |               |                   |               |                      |
| --- | ---------------- | ----------------- | ------------- | ----------------- | ------------- | -------------------- |
|     |                  |                   | themodelusing | resultsofthestudy | themodelusing | thatthecombinedmodel |
|     | errorandabsolute | resultsofthestudy |               |                   |               |                      |
percentageerror,to showedthatthe MAPE,RMSE, showthattheLSTM MAPEandRMSE. EMD-SVMfullyconsiders
|     |                  |               | andMAE.The   | model            | Theresultsofthe  | thecharacteristicsof    |
| --- | ---------------- | ------------- | ------------ | ---------------- | ---------------- | ----------------------- |
|     | evaluatethemodel | accuracyofthe |              |                  |                  |                         |
|     |                  |               | resultsofthe | incorporatingthe | studyshowthatthe | randomness,periodicity, |
performance.The hybrid studyshowthat STLmethod combinedmodel andtrendofmonthlypork
|     | conclusionisthat | ARIMA-SVM |     |     |     |     |
| --- | ---------------- | --------- | --- | --- | --- | --- |
Evaluation themodelisnot (STL-LSTM) adequatelyanalyzes marketprice,explainsthe
| method | theestablished | modelforgarlic |     |     |     |     |
| ------ | -------------- | -------------- | --- | --- | --- | --- |
combinationmodel pricepredictionis onlysuitablefor improvesthe thevarioustrends innermeaningofprice
|     |           |               | priceforecasting | predictionaccuracy | inthepriceseries | fluctuation,andnotonly |
| --- | --------- | ------------- | ---------------- | ------------------ | ---------------- | ---------------------- |
|     | hasbetter | betterthanthe |                  |                    |                  |                        |
Agriculture 2023, 13, xp rFeOdiRct iPoEnEefRfe RctE,VIEWs ingleARIMAand duringperiodsof by12%comparedto anditsforecasting showshighpred1ic2ti oonf 24
|     |                  |              | stabledata      | theLSTMmodel  | performanceis | accuracy,butalsocan     |
| --- | ---------------- | ------------ | --------------- | ------------- | ------------- | ----------------------- |
|     | anditsprediction | SVMmodelsand |                 |               |               |                         |
|     |                  |              | changes,butalso | withouttheSTL | betterthanthe | bettergraspthedirection |
accuracyand canbeusedasan givesaccurate methodand singleARIMAand oftheporkpricetrend,
|     | stabilityarebetter | effectivemethodfor |               |             |           |                    |
| --- | ------------------ | ------------------ | ------------- | ----------- | --------- | ------------------ |
|     |                    |                    | forecastswhen | resolvesthe | SVMmodel. | whichcanprovidenew |
|     | thanthetwo         | predicting         |               |             |           |                    |
singlemodels. short-termprices thepricechanges predictionlag ideasandmethodsforthe prediction of
|     |     |     | arelarge. | causedbyhigh |     | pricepredictionof |
| --- | --- | --- | --------- | ------------ | --- | ----------------- |
ofgarlic.
|     |     |     |     | seasonality. |     | poprkomrakr kmet.arket.  |
| --- | --- | --- | --- | ------------ | --- | ------------------------ |
4.14.. 1T.rTardaidtiiotnioanl aCloCmombinbiantaotroiarli aFloFroerceacsatsintign gMModoedl el
ThTeh perpinricnipcilpe loefo tfratrdaidtiiotinoanl aelnesnesmemblbe lmemodoedlse lisnivnovlovlevse ustuiltiizliinzign dgidffiefrfeernetn ftofroerceacsatisntign g
mmodoedlse ltsot porperdeidcti catgargicruiclutultruarl aclocmommmodoidtyi tpyrpicreicse ssespeapraatrealtye.l yE.vEevnetnutaullayl,l yt,htehsees ienidnidviivdiudaul al
prperdeidcticiotinosn saraer eccoommbbiinneedd uussiinngg ssppeecciifificc ininteteggrraatitoionnm metehtohdosdsto toy ieylideltdh ethoev eorvaellrfaollr efcoarset-ed
caostuetdco omutec(oFmigeu (rFeig2ua)r.eF 2iag)u. rFeig2ubrpe r2obv pidreosvaidneesx aanm epxlaemopflae torfa da ittriaodniatlioennasle emnbsleemfobrlee cfaosrtei-ng
camstiondge lm. oIdnelt.h Iisn itnhsista inncset,antwceo, tdwisot idnicsttimncot dmelosdaerles aerme pelmoypeldoyteod ptore pdricetdipcrti cperidcea tdaaatan d
anrde sriedsuidalusaslse psaepraatrealtye.lyS.u Sbusebqseuqeunetlnyt,lyth, ethirepirr epdreicdtiicotniosnasr earaed addeddetdo gtoegthetehretro tpo rpordoudcuecteh e
thfie nfianlaflo froerceacsatesdtedou otucotcmome[e2 3[2].3].

|     |     |     | (a)  |     | (b)  |     |
| --- | --- | --- | ---- | --- | ---- | --- |
FigFuigrue r2e. 2(a.)( aS)cShcehmematiact idcidaigargarmam ofo tfhteh etrtardaditiitoinonala lppoortrftofoliloio foforreeccaassttiinngg mmooddeell pprroocceessss;; ((bb)) aann eexxaammp-le
pleo fotfh tehea papplpicliactaiotinono foaf atr atrdaidtiiotinoanlaclo cmombibniantaiotinonp rperdeidctiicotinonm modoedl.el.
4.24.. 2D.eDcoemcopmopsiotsiiotnio-nC-oCmobminbaintiaotnio FnoFreocraecsatisntign MgModoedl el
ThTeh “ed“edceocmompopsoitsiiotnio-enn-esnemsebmleb”l ef”orfeocraesctaisntgin mgemtheothdo ids ibsabseadse odno tnheth meumltui-lstic-aslcea ldeed-e-
cocmompopsoitsiiotnio onfo ofroigriignianl aclocmomplpexle tximtime seesreiersie dsadtaat. aI.t Idtidssisescetsc ttshteh fleuflcutuctautaiotino npapttaetrtenrsn asnadn d
tretrnedn drergeugluarlaitriietsie osfo ifnitnritcraictaet esyssytestmems sata vtavraioriuosu sscsaclaelse. sB.yB yunudnedrestrasntadnidngin gthteh ienihnehreernetn t
operationalpatternsofthesystem,predictiveresearchisconducted,leadingtoasignifi-
operational patterns of the system, predictive research is conducted, leading to a signifi-
cant enhancement in forecasting performance. The decomposed ensemble combination  cantenhancementinforecastingperformance. Thedecomposedensemblecombination
modelreferstosplittingtheintricatepricesequenceintoseveralsimplersub-sequences.
model refers to splitting the intricate price sequence into several simpler sub-sequences.
Eachsub-sequenceisindividuallyforecastedusingmodels,andthepredictionsofthese
Each sub-sequence is individually forecasted using models, and the predictions of these
sub-sequencesarethenintegratedtoobtaintheforecastedvaluesoftheoriginalsequence
sub-sequences are then integrated to obtain the forecasted values of the original sequence
(Figure 3). The core of this methodology lies in selecting effective data decomposition
(Figure 3). The core of this methodology lies in selecting effective data decomposition
tools. Common decomposition methods include seasonal decomposition [48], wavelet de-
composition [49], empirical mode decomposition [50], and variational mode decomposi-
tion [51]. The advantages of the “decomposition-ensemble” combination forecasting
model lie in its ability to leverage information across different scales. It mitigates the im-
pact of features like noise, trends, and cycles inherent in complex data, thus enhancing
prediction accuracy and robustness. However, a drawback of the “decomposition-ensem-
ble” combination forecasting model is the need to determine suitable data decomposition
tools and integration methods; otherwise, it could affect the extraction and reconstruction
of data features. Table 4 summarizes the commonly used decomposition methods.

Agriculture2023,13,1671 11of20
tools. Common decomposition methods include seasonal decomposition [48], wavelet
decomposition[49],empiricalmodedecomposition[50],andvariationalmodedecomposi-
tion[51]. Theadvantagesofthe“decomposition-ensemble”combinationforecastingmodel
lieinitsabilitytoleverageinformationacrossdifferentscales. Itmitigatestheimpactof
featureslikenoise,trends,andcyclesinherentincomplexdata,thusenhancingprediction
accuracyandrobustness. However,adrawbackofthe“decomposition-ensemble”combi-
nationforecastingmodelistheneedtodeterminesuitabledatadecompositiontoolsand
Agriculture 2023, 13, x FOR PEER REiVnItEeWgr ationmethods;otherwise,itcouldaffecttheextractionandreconstructiono1f3d oaft a24

features. Table4summarizesthecommonlyuseddecompositionmethods.

FFigiguurere 33.. SchSecmheamtica tdiciagdriaamgr aomf thoef “dtheecom“dpeocsoitmiopno-isnittieognr-aitnioteng”r-abtaiosend” -pbraisceed foprercicaestifnogr epcoarsttfionlgio
model.
portfoliomodel.
TTaabblele4 4..C Coommmmoonnd deeccoommppoosistiitoionnm meeththoodds.s.
Decomposition STLSeasonal EmpiricalModal VariationalModal Variational
|        |               | DecompositiWonav eleStTDLec oSmepaossointioanl  |                | Wavelet Decom-Empirical Modal  |                                     |                           |
| ------ | ------------- | ----------------------------------------------- | -------------- | ------------------------------ | ----------------------------------- | ------------------------- |
| Method | Decomposition |                                                 |                | Decomposition                  |                                     | DecomMpoosditaioln Decom- |
|        |               | Method                                          | Decomposition  | position                       | Decomposition                       |                           |
|        |               |                                                 | Themulti-scale | Itdecomposestheprice           | Itdecomposesthepproicseisteiorines  |                           |
Itdecomposestheprice decompositionofprice seriesintoseveral intoseveraleigenmodal
It decomposes
seriesintotrend,seasonal, seriesusingwavelet eigenmodularfunctions functions(IMFs),whichcan
effectivelyavtohide tpheripcaet tseernries
|     | andresidualcomponents, |     | functioncanextract | (IMFs)andresidualterms, |     |     |
| --- | ---------------------- | --- | ------------------ | ----------------------- | --- | --- |
whichcanhandle featureswithdifferent whichcanhandle It decommpixoinsgesp henoimnteon osneivnetrhaelE MD
Characteristics non-stationarytimeseries frequencies,whichis nonlinearand decompositionmethodand
andissuitablefor suitableforprice Thnoen m-stuatlitoin-sacryalteim esthereie spriciem sperroiveest hedeeigcoemnpmosoitdioanl func-
forecastingagricultural predicItti odneocfoamgrpicoulsteusra l deacdoapmtivpeolysiatniodnis osuf iitnabtole seveefrfeaclt ,andistsiuoitnasb l(eIfMorFpsr)ic, e
priceswithsignificant productswithmultiple forforecastingagricultural predictionofagricultural
|     |     |     | the price series  | price series using eigenmodular  |     | which can effec- |
| --- | --- | --- | ----------------- | -------------------------------- | --- | ---------------- |
seasonality. periodicityandabrupt priceswithcomplex productswithhigh-frequency
|     |     |     | changienptooi ntrtse.nd, sea-      | wvaovlaetlielitty fuchnacraticotenri sftiucsn.ctionans d(IlMowF-fsr)e qutievneclyyc oamvpooidne tnhtse.  |                                 |                 |
| --- | --- | --- | ---------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------- | --------------- |
|     |     |     | sonal, and resid-                  | can extract fea-                                                                                         | and residual                    | pattern mixing  |
|     |     |     | ual components, tures with differ- |                                                                                                          | terms, which can phenomenon in  |                 |
Whetheritisatraditionalensembleforecastingmodelora“decomposition-ensemble”-
basedcombinationwfohrieccha sctainng hmanoddleel e,ntht efreefqfeucetnivceiense,s shoafncdomle bnionnatliinoneafro rtehcea EstMinDg rdeeliceosmto-
acCerhtaarinacetxetreisntticosn  tnhoenc-hstoasteinoninarteyg ratwiohnicmhe itsh soudi,tanbalme ealyn,dd nifofenr-esntattwioenig-hptodseistiigonn smcheethmoeds .
Utilizingeffectiveitnimtege rsaetrioiens manedth ios dfosrm paryiceev pernedleiacd- taorysu tpimereio srercioems binaantido nimfoprreocvaes ttihneg
resultscomparedtsoutihtaebblee sftoirn fdoirvei-dutiaolnf oorfe acgarsitcsu.lT-ablaed5asputimvemlya rainzdes iss edveecroamlcpoomsimtioonn ly
usedintegrationmceatshtoindgs .aTghriecsuel-mettuhroadl sparloldfaulcltus ndesruliitnaebaler ifnotre fgorraet-ioenffaepctp, raonadc hise ss,uaist-
theyinvolvemultiptulyrainl gprtihceesp wreidthic twiointhr emsuullttsipolfed pieff-ecraesnttinmgo adgerliscubly-waebigleh tfocro epfrfiicceie nts
andthensumming s t i h g e n m ifi t c o an o t b   t s a e i a n - therifiondailciftoyr eacnadst arbe-sutlut.raLli nperaicrecso wmibthin aptiroendimcteiothno odfs aagr-e
commonintegrationtechniques,buttheyarenotthesoleones. Therearealsononlinear
|     |     |     | sonality.  | rupt change  | complex volatil- | ricultural prod- |
| --- | --- | --- | ---------- | ------------ | ---------------- | ---------------- |
|     |     |     |            | points.      | ity characteris- | ucts with high-  |
|     |     |     |            |              | tics.            | frequency and    |
low-frequency
components.
Whether it is a traditional ensemble forecasting model or a “decomposition-ensem-
ble”-based combination forecasting model, the effectiveness of combination forecasting
relies to a certain extent on the chosen integration method, namely, different weight de-
sign schemes. Utilizing effective integration methods may even lead to superior combina-
tion forecasting results compared to the best individual forecasts. Table 5 summarizes

Agriculture2023,13,1671 12of20
combinationmethods,suchasneuralnetworks,supportvectormachines,andfuzzylogic.
These methods employ more complex functions to combine predictions from different
models. Hanetal.[52]foundthatnonlinearcombinationforecastingmethodsgenerally
outperformlinearcombinationmethods. Amongthem,neuralnetwork-basednonlinear
combinationforecastingmethodsexhibithigherpredictiveaccuracythanotheroptimal
combinationmethods. Guo[47]constructedanAttLSTM-ARIMA-BPcombinationmodel
for predicting corn prices. This model utilizes a BP model to train LSTM and ARIMA
predictionresultstogeneratethefinalforecastvalue,andtheresultsdemonstratefavorable
predictiveperformance.
Table5.Commonintegrationmethods.
|                   |                      | MinimumVariance | DominanceMatrix | LeastSquaresEstimation |
| ----------------- | -------------------- | --------------- | --------------- | ---------------------- |
| IntegrationMethod | EqualWeightingMethod |                 |                 |                        |
|                   |                      | Method          | Method          | Method                 |
Thedominancematrix
|     |     |                       | methodrefersto         | Theleastsquares        |
| --- | --- | --------------------- | ---------------------- | ---------------------- |
|     |     | Theminimumvariance    | constructingadominance | estimationmethodrefers |
|     |     | methodreferstogivinga | matrixbasedonthe       | toestimatingtheoptimal |
Theequalweightmethod
|     |     | largerweighttothemodel | degreeofprediction | weightcoefficientsbased |
| --- | --- | ---------------------- | ------------------ | ----------------------- |
referstoassigningthe
|     |     | withsmallvariancebased | dominanceofeachmodel | ontheleastsquares |
| --- | --- | ---------------------- | -------------------- | ----------------- |
sameweightstothe
|           |                        | onthevarianceofthe         | indifferenttimeperiods, | relationshipbetweenthe |
| --------- | ---------------------- | -------------------------- | ----------------------- | ---------------------- |
| Principle | predictionresultsofall |                            |                         |                        |
|           |                        | historicalpredictionerrors | andthengiving           | historicalprediction   |
modelsandthen
|     |     | ofeachmodel,andthen | correspondingweightsto | resultsandthetruevalues |
| --- | --- | ------------------- | ---------------------- | ----------------------- |
averagingthemtoobtain
|     |     | findingtheweighted | eachelementofthematrix | ofeachmodel,andthen |
| --- | --- | ------------------ | ---------------------- | ------------------- |
thefinalpredictionresults.
|     |     | averagetoobtainthefinal | accordingtoitssize,and | findingtheweighted      |
| --- | --- | ----------------------- | ---------------------- | ----------------------- |
|     |     | predictionresults.      | thenfindingtheweighted | averagetoobtainthefinal |
|     |     |                         | averagetogetthefinal   | predictionresults.      |
predictionresults.
Theadvantageofthis
Theadvantageofthis
|     | Theadvantageofthis |                        | approachisthatitcan     |                          |
| --- | ------------------ | ---------------------- | ----------------------- | ------------------------ |
|     |                    | approachisthatitcan    |                         | Theadvantageofthis       |
|     | approachisthatitis |                        | synthesizethe           |                          |
|     |                    | reducethevarianceofthe |                         | methodisthattheoptimal   |
|     | simpleandeasyto    |                        | performanceofdifferent  |                          |
|     |                    | combinedpredictionsand |                         | solutioncanbeobtained    |
|     | implement.The      |                        | modelsoverdifferenttime |                          |
|     |                    | improvestability.The   |                         | usingstatisticalmethods, |
Characteristics disadvantageisthatit disadvantageisthatit periods,andthe andthedisadvantageis
|     | doesnotreflectthe        |                       | disadvantageisthat     |                          |
| --- | ------------------------ | --------------------- | ---------------------- | ------------------------ |
|     |                          | cannottakeintoaccount |                        | thatcertainassumptions,  |
|     | predictivepowerand       |                       | constructingthe        |                          |
|     |                          | thecorrelationbetween |                        | suchaslinearrelationship |
|     | accuracyofdifferent      |                       | dominancematrix        |                          |
|     |                          | modelsandmayleadto    |                        | andnormaldistribution,   |
|     | modelsandmayleadto       |                       | requiresacertainamount |                          |
|     |                          | overrelianceoncertain |                        | needtobesatisfied.       |
|     | inefficientcombinations. |                       | ofsubjectivejudgment   |                          |
models.
andexperience.
| Reference | [53] | [54] | [55] | [56] |
| --------- | ---- | ---- | ---- | ---- |
5. ModelParameterOptimizationMethod
Whenestablishingagriculturalcommoditypriceforecastingmodels,theinitiallyset
orobtainedparametersarelikelynotoptimalornearoptimal. Inthesecases,parameter
optimizationisnecessarytoattainanimprovedpredictivemodel. Commonmethodsfor
parameteroptimizationincludecrossvalidation,gridsearch,geneticalgorithms,particle
swarmoptimization,andsimulatedannealing. Additionally,algorithmsinspiredbycol-
lectivebehaviorsofsocialinsectsorgroupanimals, suchasbeecolonyalgorithms, ant
colonyalgorithms,andfishswarmalgorithms,arefrequentlyemployedtooptimizemodel
parametersbasedonbiologicalcollectivebehaviorpatterns. Lu[57]employedtheparticle
swarmoptimization(PSO)algorithmtodevelopaPSO-BPforecastingmodelforvegetable
retailprices. Zhang[35]proposedahybridalgorithmcalledGDGA,whichcombinesthe
bestfeaturesofglobalandlocalsearchmethods. Resultsindicatethattheproposedhybrid
GDGA algorithm outperforms multivariate linear regression and pure GA methods in
termsofpredictiveperformanceandconvergesfasterthanpuregeneticalgorithms(GA).
ExperimentalfindingsdemonstratethatcomparedtotraditionalBPmethods,thePSO-BP
approachcanovercomeoverfittingandlocalminimumissues,effectivelyreducingtraining
errorsandenhancingpredictiveaccuracy.

Agriculture2023,13,1671 13of20
Withincreasingresearch,investigatorshavegraduallyfoundthatpredictivemodels
utilizingcombinationoptimizationalgorithmstendtoexhibitsuperiorforecastingperfor-
mancecomparedtosingleoptimizationalgorithms. Combinationparameteroptimization
algorithmsofferseveraladvantages:theyhandlecomplexoptimizationproblemsinvolving
discrete,nonlinear,andmulti-modalfunctionsbetterthansingleparameteroptimization
algorithms,whichoftenrequirecertainconditionsorassumptionslikedifferentiabilityand
convexity. Combinationparameteroptimizationalgorithmsaremoreeffectiveatavoiding
localoptima,assingleparameteroptimizationalgorithmsareoftensusceptibletoinitial
value influence, leading to slow convergence or getting stuck in suboptimal solutions.
Moreover,combinationparameteroptimizationalgorithmscanflexiblyadapttodiverse
problemcharacteristicsandrequirements. Forinstance,theycanemployvariousfitness
functions,crossover-mutationstrategies,andneighborhoodstructures. Incontrast,single
parameteroptimizationalgorithmsareusuallymorerigidanduniform,makingadjustment
andimprovementchallenging. Ofcourse,combinationparameteroptimizationalgorithms
alsohavedrawbacks,suchashighercomputationalcomplexity,challengingtheoretical
analysis, and sensitivity to parameter choices. Therefore, in practical applications, ap-
propriateoptimizationalgorithmsshouldbeselectedbasedonspecificproblemfeatures
andobjectives,andadjustmentsandimprovementsshouldbemadeaccordingly. Table6
summarizesseveralclassicparameteroptimizationmethodsusingexamplestoprovidea
comprehensiveoverview.
Table6.Commonoptimizationmethodsandexamples.
| Optimization |     |     |     | ParticleSwarm |     |
| ------------ | --- | --- | --- | ------------- | --- |
CrossValidation GridSearch GeneticAlgorithm SimulatedAnnealing
| Methods |     |     |     | Optimization |     |
| ------- | --- | --- | --- | ------------ | --- |
Gridsearchisamethod
|     |                    | tofindtheoptimal  |                      | Particleswarm   |     |
| --- | ------------------ | ----------------- | -------------------- | --------------- | --- |
|     | Crossvalidationisa | modelparametersby | Ageneticalgorithmisa | optimizationisa |     |
methodtoevaluatethe traversingagivenrange heuristicoptimization population Simulatedannealingisa
probability-basedoptimization
|     | performanceofamodel | andcombinationof | algorithmthat | intelligence-based |     |
| --- | ------------------- | ---------------- | ------------- | ------------------ | --- |
algorithmthatsimulatesthe
bydividingthedataset parameters,cross simulatestheprocessof optimizationalgorithm processofasolidsubstance
|     | intoseveralsubsets, | validatingeach | biologicalevolutionin | thatsimulatesthe |     |
| --- | ------------------- | -------------- | --------------------- | ---------------- | --- |
reachinganenergyminimum
usingonesubsetata combinationof naturebycontinuously foragingbehaviorofa
timeasthetestsetand parameters,andthen updatingasetof flockofbirdsby stateduringheatingand
| Principle |     |     |     |     | coolingbyrandomly |
| --------- | --- | --- | --- | --- | ----------------- |
theothersubsetsasthe selectingthe candidatesolutions adjustingthespeedand
trainingset,repeating combinationof (calledpopulations) positionofeach perturbingthecurrentsolution
(calledthestate)andaccepting
|     | severaltimes,andthen | parameterswiththe | throughoperations, | candidatesolution |     |
| --- | -------------------- | ----------------- | ------------------ | ----------------- | --- |
orrejectingthenewsolution
calculatingtheaverage bestcrossvalidation suchasselection, (calledparticles)to basedonaprobability(called
|     | performancemetricsof | performanceasthe | crossover,andmutation, | moveclosertothe |     |
| --- | -------------------- | ---------------- | ---------------------- | --------------- | --- |
theBoltzmannfunction)that
|     | themodelonthe | optimalparameters,the | untiltermination | individualoptimal |     |
| --- | ------------- | --------------------- | ---------------- | ----------------- | --- |
differenttestsets. markervalues,andtheir conditionsaremet. solutionandtheglobal decreaseswithtemperature.
|     |     | correspondingoptimal |     | optimalsolution. |     |
| --- | --- | -------------------- | --- | ---------------- | --- |
parametervalues.
|     |     |     | Geneticalgorithmscan | Particleswarm |     |
| --- | --- | --- | -------------------- | ------------- | --- |
Gridsearchcan handlenonlinear, optimizationhasthe Simulatedannealingcanjump
Crossvalidationcan systematicallyexplore multi-peaked,discrete advantagesoffast outofthelocaloptimal
makeeffectiveuseof
theparameterspace orcontinuous convergence,few solutionandfindtheglobal
limiteddatatoavoid
over-orunder-fitting andfindtheglobal optimizationproblems parameters,andsimple optimalsolution,whichis
Characteristics optimalsolution,butit withstrongglobal andeasy suitableforcombinatorial
problemsandcanalso
iscomputationally searchcapabilityand implementationofthe optimizationproblems,butit
beusedtoselect expensiveandcannot robustness,but algorithm,butitalso takesalongertimetoadjust
optimalmodel
handlecontinuous convergenceisslowand hastheproblemof theparametersandcooling
parametersorfeatures.
|     |     | parameters. | pronetofallintoearly | fallingintolocal  | progress. |
| --- | --- | ----------- | -------------------- | ----------------- | --------- |
|     |     |             | convergence.         | optimalsolutions. |           |
Thesimulatedannealing
|     |     | Itismainlyusedtofind |     |     | algorithmisageneral-purpose |
| --- | --- | -------------------- | --- | --- | --------------------------- |
theoptimalmodel
|     |     |     | Geneticalgorithmshave | Itismainlyusedfor | optimizationalgorithmwith |
| --- | --- | --- | --------------------- | ----------------- | ------------------------- |
Forselectingthe parameters,suchas beenwidelyusedinthe optimizationof theoreticallyprobabilistic
|     | optimalmodel          | penaltyparametersand |                       |                     |                    |
| --- | --------------------- | -------------------- | --------------------- | ------------------- | ------------------ |
|     |                       |                      | fieldsofcombinatorial | continuousproblems, | globaloptimization |
|     | parametersorfeatures, | kernelfunction       |                       |                     |                    |
Application suchasregularization parametersofsupport optimization,machine suchasfunction performance,whichhasbeen
|     |                     |                 | learning,signal     | optimizationproblems, | widelyusedinengineering, |
| --- | ------------------- | --------------- | ------------------- | --------------------- | ------------------------ |
|     | coefficients,kernel | vectormachines, |                     |                       |                          |
|     |                     |                 | processing,adaptive | neuralnetworktraining | suchasVLSI,production    |
functions,feature learningrate,and control,andartificial problems,engineering scheduling,control
|     | subsets,etc. | numberofhiddenlayer |       |                     |                              |
| --- | ------------ | ------------------- | ----- | ------------------- | ---------------------------- |
|     |              |                     | life. | designproblems,etc. | engineering,machinelearning, |
nodesofneural
|     |     | networks. |     |     | neuralnetworks,signal |
| --- | --- | --------- | --- | --- | --------------------- |
processing,andotherfields.
| Reference | [58] | [59] | [60] | [61] | [62] |
| --------- | ---- | ---- | ---- | ---- | ---- |

Agriculture2023,13,1671 14of20
6. Discussion
Intheprocessofbuildingagriculturalpriceforecastingmodels(Figure4),inaddition
tothekeystepofalgorithmselection,processessuchasfeatureselection,modelconstruc-
tion,andmodeloptimizationarealsocrucial. Inthispaper,weexplorepossibleresearch
Agriculture 2023, 13, x FOR PEER REdVIiEreWc tionsormethodstoimprovetheperformanceofagriculturalpriceforecasting18f roof m24
theperspectivesofdata,models,andstrategies.
FFiigguurree 44.. BBaassiicc flflooww cchhaarrtt ffoorr pprriiccee ffoorreeccaassttiinnggm mooddeellm mooddeelliinngg..
66..11.. DDaattaa:: QQuuaannttiifificcaattiioonn ooff UUnnssttrruuccttuurreedd DDaattaa
UUnnssttrruuccttuurreeddd daatataa raered adtaatath tahtahta hvaevneo nfiox fiedxefdor fmoramtoart sotrr uscttruurcet,usruec, hsuacsht eaxst ,tiemxta, gimes-,
aaugdeiso, ,avuiddieoo,, vetidc.eTo,h eetqcu. aTnhtei fiqcuaatinotnifiocfautinosnt roufc tuunrestdrudcattuarecadn dhaetlap ceaxnt rhacetlpu seexfturlaicnt fuosrmefua-l
tiinofnorfrmomatiiotn,d firsocmov ietr, dhiisdcdoevnerp hatitdedrnens, paanttdesrunps,p aonrtdd seucpispioonrt mdeackiisnigona nmdaikninnogv aantido nin.nWoivtah-
tthioend. eWveiltohp tmheen dteovfeIlnotpemrneenttt eocfh nInotleorgnye,tt hteecahmnooluongtyo, fthuen satmruocutunrte dofd uantastirsuinctcurereadsi ndgatdaa yis
byday. Theextractionandquantificationofunstructureddatainformationisespecially
increasing day by day. The extraction and quantification of unstructured data information
importanttoimprovethepredictionaccuracyofagriculturalprices.
is especially important to improve the prediction accuracy of agricultural prices.
Withthedevelopmentandapplicationofsocialmedia,farmersandconsumersare
With the development and application of social media, farmers and consumers are
increasingly influenced by online public opinion, leading to unreasonable planting or
increasingly influenced by online public opinion, leading to unreasonable planting or pur-
purchasingbehavior,whichhasacompleximpactonthepriceofagriculturalproducts.
chasing behavior, which has a complex impact on the price of agricultural products. The
Theuseof“textmining”technologytoextractinformationfromunstructureddatanotonly
use of “text mining” technology to extract information from unstructured data not only
enrichesthefeatureinformationofagriculturalpricepredictionmodels,butalsoimproves
enriches the feature information of agricultural price prediction models, but also improves
theaccuracyofpredictionandcompensatestheshortcomingsofneuralnetworkmodels
the accuracy of prediction and compensates the shortcomings of neural network models
that are difficult to interpret the output results. Moreover, adding sentiment scores to
that are difficult to interpret the output results. Moreover, adding sentiment scores to ag-
agriculturalpricepredictioncaneffectivelyimprovethepredictionperformance. Ye[63]
ricultural price prediction can effectively improve the prediction performance. Ye [63]
useddiscussionsinonlineprofessionalcommunitiestoconstructheterogeneousgraphs,
used discussions in online professional communities to construct heterogeneous graphs,
andfinally,constructedHGLSTMforprediction. Theexperimentalresultsshowedthat
and finally, constructed HGLSTM for prediction. The experimental results showed that
thepredictionofhogpricesusingforumdiscussiondatawaseffective. Drury[64]studied
the prediction of hog prices using forum discussion data was effective. Drury [64] studied
the application of text mining in agriculture and found that there are a large number
the application of text mining in agriculture and found that there are a large number of
ofagriculturaltextsinagriculturalresearch,suchasscientificpapersandnewsreports,
agricultural texts in agricultural research, such as scientific papers and news reports,
whichcanbeanalyzedbytextminingtechniquestosolveagriculturalproblemsincluding
which can be analyzed by text mining techniques to solve agricultural problems including
agricultural price prediction. Drury concluded that although text mining techniques
agricultural price prediction. Drury concluded that although text mining techniques are
arerelativelymature, textmininghasnotbeenfullyutilizedinthefieldofagricultural
relatively mature, text mining has not been fully utilized in the field of agricultural price
priceprediction. Inrecentyears,researchontextminingtechniquesinthefieldofprice
prediction. In recent years, research on text mining techniques in the field of price fore-
forecasting, including agricultural price forecasting, has gradually increased. Table 7
casting, including agricultural price forecasting, has gradually increased. Table 7 summa-
summarizesseveralexamplesofpricepredictionbasedontextmining.
rizes several examples of price prediction based on text mining.
Table 7. Text Mining Based Price Prediction for Agricultural Products.
Reference [65] [66] [67]
A text-based predic- Proposing an effective Sentiment analysis
Application Exam- tion framework is prediction model us- was used to extract
ples proposed that can ef- ing text data on social key information from
fectively identify and media—two-stage web text from four

Agriculture2023,13,1671 15of20
Table7.TextMiningBasedPricePredictionforAgriculturalProducts.
Reference [65] [66] [67]
Sentimentanalysiswasusedtoextract
keyinformationfromwebtextfromfour
perspectives:Compoundsentiment,
Atext-basedprediction
Proposinganeffectiveprediction negativesentiment,neutralsentiment,
frameworkisproposedthatcan
modelusingtextdataonsocial andpositivesentiment.Thesewere
effectivelyidentifyandquantify
ApplicationExamples media—two-stagehybridlong- constructedasfeaturesandfedintothe
factorsaffectingagricultural
andshort-termmemory oilpricepredictionmodelalongwith
futuresbasedonalargenumber
(TSH-LSTM). theoilpriceitself.Finally,weanalyzed
ofonlinenewsheadlines.
theimpactfromdifferentperspectives
andcameupwithsome
interestingfindings.
AgriculturalProduct Soybean Soybean Oil
Traditionalvariables,suchas
exports,imports,production,
Traditionalvariablesaswellas
ObservedFeatures inventories,etc.;text-based Web-basedSentimentAnalysis,oilprice.
socialmediabasedtextdata.
variables,suchasweatherand
policyfactors.
Theempiricalresultsindicatethat
Theresultsshowthatthe
theincorporationofthesocial
identifiedinfluentialfactorsand
mediatextfeaturehelpsimprove
sentiment-basedvariablesare
forecastingperformances. Usingnetworkinformationforoilprice
effective,andtheproposed
Conclusion Specifically,theproposed forecastingimprovestheaccuracyand
frameworkperformssignificantly
TSH-LSTMismoreaccuratethan stabilityofforecasts.
betterinmedium-andlong-term
univariateLSTM,multivariate
forecastingthanthe
LSTM,andeXtreme
benchmarkmodel.
GradientBoosting.
6.2. Model: TheBalanceofPerformance
Whenevaluatingtheperformanceofagriculturalpriceforecastingmodels,weneedto
considerseveralaspects,suchasbetweentheaccuracyofforecastvaluesandforecasttrends,
between model complexity and interpretability, and the combination of data between
differentscales. Balancingthesefactorsisanimportantgoalforthefuturedevelopmentof
agriculturalpriceforecastingmethods.
1. BalancingAccuracyofPredictedValuesandPredictedTrends. Whenevaluatingthe
qualityofforecastresults,itisoftenassessedfromtwoperspectives: predictedvalues
and the forecasted trend (or rise and fall). For instance, for a certain agricultural
commodity,thepriceondaytis3.7,andtheactualpriceondayt+1is3.73. Predicted
valueais3.85,whilepredictedvaluebis3.65. Fromanerrorperspective,predicted
valuebisclosertothetruevaluethanpredictedvaluea. However,consideringthe
forecastedtrend,predictedvalueaisaccurate,whilepredictedvaluebisopposite
(Figure5). Achievingprecisepredictedvaluesandaccurateforecastedtrendsdoesnot
necessarilyconflict,butsimultaneouslyachievingbothcanbechallenging. Infuture
research,ensuringtheaccuracyofbothpredictedvaluesandforecastdirectionsisa
keyissuetoaddress. Moreover,theaccuracyoftheforecastedtrenddirectionshould
beconsideredasaperformancemetricforfutureforecastingmodels,andmethods
likedirectionalsymmetrycanbeemployedtomeasuretheaccuracyofthemodel’s
forecastdirection.

Agriculture 2023, 13, x FOR PEER REVIEW 20 of 24
(Figure 5). Achieving precise predicted values and accurate forecasted trends does
not necessarily conflict, but simultaneously achieving both can be challenging. In fu-
ture research, ensuring the accuracy of both predicted values and forecast directions
is a key issue to address. Moreover, the accuracy of the forecasted trend direction
should be considered as a performance metric for future forecasting models, and
Agriculture2023,13,1671 16of20
methods like directional symmetry can be employed to measure the accuracy of the
model’s forecast direction.
Figure 5. Comparison of different predicted values.
Figure5.Comparisonofdifferentpredictedvalues.
22.. BBaallaanncciinngg MMooddeell CCoommpplleexxiittyy aanndd IInntteerrpprreettaabbiilliittyy.. TThhee eeffffeeccttiivveenneessss ooffa aggrricicuultltuurraall
ccoommmmooddiittyy pprriiccee ffoorreeccaassttiinngg aallssoo rreelliieess oonn ssttrriikkiinngg aa bbaallaannccee bbeettwweeeenn mmooddeell ccoomm--
pplleexxiittyy aanndd iinntteerrpprreettaabbiilliittyy.. CCuurrrreennttllyy,, cceerrttaaiinn mmaacchhiinnee lleeaarrnniinngg aanndd ddeeeeppl eleaarrnniningg
mmeetthhooddss ccaannh haannddlelen noonnlilnineaerara nadndin itnritcraictaetde adtaatrae lraetliaotnioshnisphsipwse wll,eelln, heannhcainngcinpgre pdrice--
tdioicntiaocnc uarcaccuyr.aHcyo. wHeovwere,vthere,s ethmeseet hmodetshaoldsos eallesov aetleemvaoted emlcoodmelp cleoxmitpyleaxnidtyd aenmda ndde-
cmoamnpdu ctoatmiopnuatlartieosnoaulr creesso,udrimceisn, idshiminignimshoindge lminotdeerpl rinettaerbpilrietyta.bIinlitoyr.d Ienr otordiemr ptoro ivme-
tphreovexe pthlaen eaxtpolraynpateorrfoyr pmearfnocremoafntchee omf tohdee ml,osdoeml,e soomfteh oeff tohlleo fwolilnogwminegt hmoedtshocdans cbaen
ubsee uds:euds: iunsginegx pexlapilnaainbalebmle amchacinheinlee aleranrinnignagl aglogroitrhitmhms,ss, uscuhcha sasd deecicsiisoionnt rtreeeess,,l ilnineeaarr
rreeggrreessssiioonn,, llooggiissttiicc rreeggrreessssiioonn,, eettcc..,, wwhhiicchh ccaann vviissuuaallllyy ddeemmoonnssttrraattee tthhee rreellaattiioonnsshhiipp
bbeettwweeeenn ffeeaattuurreess aanndd ttaarrggeett vvaarriiaabblleess,, aass wweellll aass tthhee iimmppoorrttaannccee aanndd wweeiigghhtt ooff tthhee
ffeeaattuurreess;; uussiinngg ffeeaattuurree eennggiinneeeerriinngg aanndd ffeeaattuurree sseelleeccttiioonn tteecchhnniiqquueess,,p prree--pprroocceessssiningg
aanndd ddoowwnnssccaalliinngg ooff ththee raraww ddataat,a e,xetxratrcaticntign tgheth meomsto mstemaneianngifnugl faunlda nindfluineflnutieanl tfieaal-
fteuarteusr, easn,da nredmreomvionvgi nregdruendduanndt aanntda inrdreilrervealenvt afenattfueraetsu troe smtoakme athkee mthoedmelo mdeolrem coorne-
ccoisnec iasneda nedaseya stoy utonudnedrsetrasntadn; du;suinsign mgmodoedle ilnitnetreprrperteattaitoionn totooolsls, ,ssuucchh aass LLIIMMEE,, SSHHAAPP,,
EELLII55,, eettcc..,, ttoo iinntteerrpprreett tthhee pprreeddiiccttiioonn rreessuullttss ooff tthhee mmooddeell llooccaallllyy oorr gglloobbaallllyy,, aannddt too
aannaallyyzzee tthhee ccoonntrtribibuutitoionna annddd degergereeeo foifn iflnufleunecnecoef oefa cehacfhea fteuarteuoren othne tphree dpircetdioicntiroen-
sults,aswellastheinteractioneffectsbetweendifferentfeatures. Althoughtheabove
results, as well as the interaction effects between different features. Although the
methodscanimprovetheinterpretabilityofthemodeltosomeextent. However,for
above methods can improve the interpretability of the model to some extent. How-
thetimebeing,complexityandinterpretabilityseemtobemutuallyexclusive,with
ever, for the time being, complexity and interpretability seem to be mutually exclu-
morecomplexmodelsalsoimplyinglessinterpretability. Therefore,howtomaximize
sive, with more complex models also implying less interpretability. Therefore, how
theinterpretabilityofthemodelwhileensuringitsaccuracyisamajorchallengefor
to maximize the interpretability of the model while ensuring its accuracy is a major
futureresearchinthisarea. Thisincludes,amongotherthings,researchonmodel
challenge for future research in this area. This includes, among other things, research
complexity, methods for establishing interpretability metrics, or the development
on model complexity, methods for establishing interpretability metrics, or the devel-
ofstandards.
opment of standards.
6.3. Strategy: CombinationofDatabetweenDifferentScales
6.3. Strategy: Combination of Data between Different Scales
Ingeneral,peopleoftenusedatawiththesametimescaleforpriceforecasting,such
In general, people often use data with the same time scale for price forecasting, such
as modeling daily data to obtain forecasts at a daily frequency. Some researchers have
as modeling daily data to obtain forecasts at a daily frequency. Some researchers have
foundthattimeseriesdataofdifferenttimescalescontaindifferentamountsofinforma-
found that time series data of different time scales contain different amounts of
tion,andcombiningdatafromdifferenttimescalescanenhancepredictionperformance.
information, and combining data from different time scales can enhance prediction
Lingetal.[68]werethefirsttoattemptthecombinationofforecastsfrommultipletime
performance. Ling et al. [68] were the first to attempt the combination of forecasts from
scales,proposinganovelmulti-timescalecombinationstrategyforforecastingChinese
multiple time scales, proposing a novel multi-time scale combination strategy for
livestockproductprices. Theresearchresultsindicatethatadoptingthisnewcombination
approachcansignificantlyimprovepredictionperformance. Liwenetal.[69]proposeda
multi-timescalecombinationstrategyforpredictingporkprices. Usingdailypricesasa
base,weeklyandmonthlyforecastsaretransformedintodailyfrequencydata,forming
multi-timescaleforecastresultsthatreflectthemultidimensionaldatagenerationprocess
ofpricetimeseries. Variousmulti-scalecombinationstrategieswereconstructedtoaddress
short-,medium-,andlong-termforecastingneeds,investigatingthematchingrelationship
betweenforecasthorizonandtimescale. Theresearchfindingssuggestthatwhilemulti-

Agriculture2023,13,1671 17of20
timescalecombinationstrategiesmaynotenhanceshort-termpredictionperformance,they
caneffectivelyimproveaccuracyinmedium-andlong-termforecasts.
Butthestrategyalsohascertainchallenges. First,thetimescalematchingproblem.
Howtochooseacombinationofdifferenttimescalesandhowtomatchtheforecaststep
andtimescalemaybeachallenge. Differenttimescalesmayhavedifferenttrendsand
periodicities,andhowtoreasonablymatchthesecharacteristicsmayrequiresomeempirical
ormethodologicalsupport.Second,consideringmultipletimescalesmayrequiretheuseof
moresophisticatedmodelstocapturetrendsandrelationshipsatdifferentscales. Thismay
leadtoincreasedmodelcomplexity,requiringmoreparametertuningandcomputational
resources,aswellasincreasedriskofoverfitting. Finally,interpretiveissues. Interpreting
thepredictionsofamodelcanbecomemorecomplexwhenmodelswithmultipletime
scalesareused. Understandinghowdifferenttimescalesinteractwitheachotherandhow
theycollectivelycontributetothepredictionsmaybecomemoredifficult.Infutureresearch,
thereshouldbeastrongerfocusonexploringmulti-timescalecombinationstrategiesand
theirapplicationinmulti-stepforecastingofagriculturalproductprices.
7. Conclusions
Agriculturalproductpriceforecastingisacomprehensive,crosscutting,anddynamic
researchfield. Withthecontinuousdevelopmentandchangesindatasources,datatypes,
dataquality,dataprocessingtechniques,modelconstructiontechniques,andmodelevalu-
ationtechniques,agriculturalproductpriceforecastingmethodswillalsobeupdatedand
improved. Thispapersystematicallysummarizesthedevelopmentofagriculturalprice
forecastingmethodsfromtraditionalmethodstointelligentmethods,fromsinglemodels
tocombinedmodels. Thepossiblefuturedevelopmenttrendsarealsodiscussed. Future
researchcanexplorethefollowingaspects:
(1) developingmoreeffectiveunstructureddatainformationextractionandquantifica-
tiontechniques, andusingmoredatasourcesanddatatypestoenrichthefeature
informationofagriculturalpricepredictionmodels;
(2) findingmoresuitablecombinedmodelintegrationmethods, suchasusingneural
networks,toimprovetheeffectivenessandefficiencyofcombinedmodelprediction
methods;
(3) balancingmodelcomplexityandinterpretabilitytoimprovemodelperformanceand
practicality;
(4) exploringthecombinationstrategyofmultipletimescalesanditseffectivenessand
advantagesintheapplicationofmulti-stepforecastingofagriculturalprices;
(5) consideringtheaccuracyofthetrenddirectionofforecastingresultsasanindicator
toevaluatetheperformanceofforecastingmodels,whileensuringtheaccuracyof
forecastingvaluesandforecastingdirections.
(6) Mechanismsandmethodsfortheconstructionofcombinedmodelsforagricultural
priceforecastingneedtobestudiedindepth,andthecomparisonandintegration
between different methods need to be strengthened to improve the accuracy and
practicalityofforecasting.
AuthorContributions:Conceptualization,F.S.andP.L.;methodology,F.S.;writing—originaldraft
preparation,F.S.;writing—reviewandediting,X.M.andY.Z.;supervision,projectadministration,
Y.W.andH.J.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:ThisresearchwasfundedbytheMajorAgriculturalAppliedTechnologyInnovationProject
ofShandongProvince,grantnumberSD2019ZZ019;theKeyResearchDevelopmentProgram(Major
ScienceandTechnologyInnovationProjects)ofShandongProvince,grantnumber2022CXGC010609;
and the Major Science and Technology Innovation Project of Shandong Province, grant number
2019JZZY010713.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.

Agriculture2023,13,1671 18of20
DataAvailabilityStatement:Notapplicable.
Acknowledgments:ThankstotheKeyLaboratoryofHuang-Huai-HaiSmartAgriculturalTechnol-
ogy,MinistryofAgricultureandRuralAffairs,foritssupportforscientificresearch. Iwouldlike
tothankKeZhu(CollegeofInformationScienceandEngineering,ShandongAgriculturalUniver-
sity),ShiweiXu(AgriculturalInformationInstituteofChineseAcademyofAgriculturalSciences),
YongZheng(DepartmentofAgricultureandRuralAffairs)andotherexpertsfortheirguidanceon
mypaper.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
References
1. Zheng,L.ModelConstructionandEmpiricalStudyonProductionandConsumptionForecastingofMajorAgriculturalProducts
inChina.Master’sThesis,UniversityofChineseAcademyofSciences,Beijing,China,2013.
2. Cao,Y.L.;Mohiuddin,M.SustainableEmergingCountryAgro-FoodSupplyChains:FreshVegetablePriceFormationMechanisms
inRuralChina.Sustainability2019,11,2814.[CrossRef]
3. Zhang,D.;Liu,H.;Zhang,Y.ForecastingChinesedomesticsoybeanpricebasedonQ-RBFneuralnetworkmodel.SoybeanSci.
2017,36,143–149.[CrossRef]
4. Tothova,M.MainChallengesofPriceVolatilityinAgriculturalCommodityMarkets.InMethodstoAnalyseAgriculturalCommodity
PriceVolatility;Springer:NewYork,NY,USA,2011;pp.13–29.[CrossRef]
5. Xiao,X.Y.;Li,C.G.Thepricecharacteristics,problemsandsolutionsofvegetablesinChina.Res.Agric.Mod.2016,37,948–955.
[CrossRef]
6. Xu,L.;Zhang,Q.;Xu,S.W.AnalysisofvegetablepriceincreasesinChinasince2009.FoodNutr.China2012,18,39–44.[CrossRef]
7. Beckert,J.Wheredopricescomefrom?Sociologicalapproachestopriceformation.Socio-Econ.Rev.2011,9,757–786.[CrossRef]
8. Aguiar,D.R.;Santana,J.A.Asymmetryinfarmtoretailpricetransmission:EvidencefromBrazil.Agribus.Int.J.2002,18,37–48.
[CrossRef]
9. Ward,R.W.Asymmetryinretail,wholesale,andshippingpointpricingforfreshvegetables.Am.J.Agric.Econ.1982,64,205–212.
[CrossRef]
10. Gu,Z.;Zhang,Y.AstudyontheInfluenceFactorsofAgriculturalPricesbasedonMachineLearning—Takingoilseedsasan
example.PriceTheoryPract.2023,4,122–126.[CrossRef]
11. Moore,H.L.ForecastingtheYieldandthePriceofCotton;Macmillan:NewYork,NY,USA,1917.
12. Ma,C.;Tao,J.P.;Liu,W.PigEpidemicNetworkConcernsandPorkPriceVolatility:ExacerbatingorCurbing?J.HuazhongAgric.
Univ.(Soc.Sci.Ed.)2022,6,22–34.[CrossRef]
13. Ge,Y.;Wu,H.Predictionofcornpricefluctuationbasedonmultiplelinearregressionanalysismodelunderbigdata. Neural
Comput.Appl.2020,32,16843–16855.[CrossRef]
14. Feng, F.; Wei, F.; Miu, J.H. Price Prediction of Traditional Chinese Medicine Siraitia grosvenorii Based on Grey System
GM(1,1)Model.GuangxiSci.2012,19,15–20.[CrossRef]
15. Cuaresma,J.C.;Hlouskova,J.;Kossmeier,S.;Obersteiner,M.Forecastingelectricityspot-pricesusinglinearunivariatetime-series
models.Appl.Energy2004,77,87–106.[CrossRef]
16. Jadhav,V.;Chinnappa,R.B.;Gaddi,G.ApplicationofARIMAmodelforforecastingagriculturalprices.J.Agric.Sci.Technol.2017,
9,981–992.
17. Brown,R.G.;Meyer,R.F.Thefundamentaltheoremofexponentialsmoothing.Oper.Res.1961,9,673–685.[CrossRef]
18. Wu,L.;Liu,S.;Yang,Y.GreydoubleexponentialsmoothingmodelanditsapplicationonpigpriceforecastinginChina.Appl.
SoftComput.2016,39,117–123.[CrossRef]
19. Zhang,X.G.IntroductiontoStatisticalLearningTheoryandSupportVectorMachines.ActaAutom.Sin.2000,26,32–42.
20. Sain,S.R.TheNatureofStatisticalLearningTheory;Taylor&Francis:Abingdon,UK,1996;Volume38,p.409.[CrossRef]
21. deMello,R.F.;Ponti,M.A.Statisticallearningtheory.Mach.Learn.2018,75–128.
22. Andrew,A.M.AnIntroductiontoSupportVectorMachinesandOtherKernel-BasedLearningMethodsbyNelloChristianiniand
JohnShawe-Taylor,CambridgeUniversityPress,Cambridge.Robotica2000,18,687–689.[CrossRef]
23. Wang,B.;Liu,P.;Chao,Z.;Junmei,W.;Chen,W.;Cao,N.;O’Hare,G.M.;Wen,F.ResearchonHybridModelofGarlicShort-term
PriceForecastingbasedonBigData.Comput.Mater.Contin.2018,57,283–296.[CrossRef]
24. Duan,Q.;Zhang,L.;Wei,F.;Xiao,X.;Wang,L.TimeSeriesGA-SVRbasedFishPricePredictionModelandValidation.Trans.
Chin.Soc.Agric.Eng.2017,33,308–314.[CrossRef]
25. Nuvaisiyah,P.;Nhita,F.;Saepudin,D.PricepredictionofchilicommoditiesinBandungregencyusingBayesianNetwork.IJoICT
2018,4,19–32.[CrossRef]
26. Ticehurst,J.L.;Letcher,R.A.;Rissik,D.Integrationmodellinganddecisionsupport:AcasestudyoftheCoastalLakeAssessment
andManagement(CLAM)Tool.Math.Comput.Simul.2008,78,435–449.[CrossRef]
27. Pearl,J.Graphicalmodelsforprobabilisticandcausalreasoning. QuantifiedRepresent. Uncertain. Imprecision1998,1,367–389.
[CrossRef]

Agriculture2023,13,1671 19of20
28. Ma,Z.PredictionofHogPriceandProduceBasedonDynamicBayesianNetwork. Master’sThesis,HuazhongAgricultural
University,Wuhan,China,2019.[CrossRef]
29. Lapedes,A.;Farber,R.NonlinearSignalProcessingUsingNeuralNetworks:PredictionandSystemModelling.1987.Available
online:https://www.osti.gov/servlets/purl/5470451(accessedon11November2022).
30. Kohzadi,N.;Boyd,M.S.;Kermanshahi,B.;Kaastra,I.Acomparisonofartificialneuralnetworkandtimeseriesmodelsfor
forecastingcommodityprices.Neurocomputing1996,10,169–181.[CrossRef]
31. Liakos,K.G.;Busato,P.;Moshou,D.;Pearson,S.;Bochtis,D.Machinelearninginagriculture:Areview.Sensors2018,18,2674.
[CrossRef]
32. Gao,Y.;An,S.ComparativeStudyonthePredictiveEffectofthePriceofEggsinChina—ComparativeanalysisbasedonBP
neuralnetworkmodelandeggfuturespredictivemodel.PriceTheoryPract.2021,4,441.[CrossRef]
33. Yu,Y.;Zhou,H.;Fu,J.ResearchonagriculturalproductpriceforecastingmodelbasedonimprovedBPneuralnetwork.J.Ambient
Intell.Humaniz.Comput.2018,1–6.[CrossRef]
34. Nasira, G.; Hemageetha, N. Vegetable price prediction using data mining classification technique. In Proceedings of the
InternationalConferenceonPatternRecognition,InformaticsandMedicalEngineering(PRIME-2012),Salem,India,21–23March
2012;pp.99–102.[CrossRef]
35. Zhang,D.;Zang,G.;Li,J.;Ma,K.;Liu,H.PredictionofsoybeanpriceinChinausingQR-RBFneuralnetworkmodel.Comput.
Electron.Agric.2018,154,10–17.[CrossRef]
36. dosSantosCoelho,L.;Santos,A.A.ARBFneuralnetworkmodelwithGARCHerrors:Applicationtoelectricitypriceforecasting.
Electr.PowerSyst.Res.2011,81,74–83.[CrossRef]
37. Fang,X.;Wu,C.;Yu,S.;Zhang,D.;Ouyang,Q.ResearchonShort-TermForecastModelofAgriculturalProductPriceBasedon
EEMD-LSTM.Chin.J.Manag.Sci.2021,29,68–77.[CrossRef]
38. Fan,J.;Liu,H.;Hu,Y.LSTMDeepLearningBasedSoybeanFuturesPriceForecasting.PricesMon.2021,12,7–15.[CrossRef]
39. Cheung,L.;Wang,Y.;Lau,A.S.;Chan,R.M.Usinganovelclustered3D-CNNmodelforimprovingcropfuturepriceprediction.
Knowl.-BasedSyst.2023,260,110133.[CrossRef]
40. Li,Z.;Cui,L.;Xu,S.;Weng,L.;Dong,X.;Li,G.;Yu,H.Predictionmodelofweeklyretailpriceforeggsbasedonchaoticneural
network.J.Integr.Agric.2013,12,2292–2299.[CrossRef]
41. Li,Z.;Xu,S.;Cui,L.;Zhang,J.Predictionstudybasedondynamicchaoticneuralnetwork—Takingpotatotime-seriespricesasan
example.Syst.Eng.-TheoryPract.2015,35,2083–2091.
42. Guo,T.;Chen,X.ResearchongrainpriceforecastinginChinabasedonPCA-ELM.PricesMon.2015,21–26.[CrossRef]
43. Puchalsky,W.;Ribeiro,G.T.;daVeiga,C.P.;Freire,R.Z.;dosSantosCoelho,L.AgribusinesstimeseriesforecastingusingWavelet
neuralnetworksandmetaheuristicoptimization:Ananalysisofthesoybeansackpriceandperishableproductsdemand.Int.J.
Prod.Econ.2018,203,174–189.[CrossRef]
44. Wang,F.;Lu,L.ResearchonPriceForecastingofChineseHerbalMedicineBasedonWaveletNeuralNetworkMethod.Microcom-
put.Appl.2013,30,34–36.[CrossRef]
45. Bates,J.M.;Granger,C.W.Thecombinationofforecasts.J.Oper.Res.Soc.1969,20,451–468.[CrossRef]
46. Lun,R.;Luo,Q.;Gao,M.;Yang,Y.AnalysisofChina’spotatopriceforecastbasedonacombinationmodel.Chin.J.Agric.Resour.
Reg.Plan.2021,42,97–108.[CrossRef]
47. Guo,Y.;Tang,D.;Tang,W.;Yang,S.;Tang,Q.;Feng,Y.;Zhang,F.AgriculturalPricePredictionBasedonCombinedForecasting
ModelunderSpatial-TemporalInfluencingFactors.Sustainability2022,14,10483.[CrossRef]
48. Yin,H.;Jin,D.;Gu,Y.H.;Park,C.J.;Han,S.K.;Yoo,S.J.STL-ATTLSTM:VegetablepriceforecastingusingSTLandattention
mechanism-basedLSTM.Agriculture2020,10,612.[CrossRef]
49. Cao,S.;He,Y.Waveletdecomposition-basedSVM-ARIMApriceforecastingmodelforagriculturalproducts.Stat.Decis.2015,
92–95.[CrossRef]
50. Cai,C.;Ling,L.;Niu,C.;Zhang,D.AnintegratedEMD-SVMforecastingmodelfordomesticporkmarketprices.Chin.J.Manag.
Sci.2016,845–851.
51. Sun,W.;Huang,C.Acarbonpricepredictionmodelbasedonsecondarydecompositionalgorithmandoptimizedbackpropaga-
tionneuralnetwork.J.Clean.Prod.2020,243,118671.[CrossRef]
52. Han,D.;Niu,W.;Yang,R.TheComparativeStudyOnLinearandNon-linearOptimalForecast-combinationMethods.Inf.Sci.
2007,25,1672–1678.[CrossRef]
53. DelSole,T.;Yang,X.;Tippett,M.K.Isunequalweightingsignificantlybetterthanequalweightingformulti-modelforecasting?
Q.J.R.Meteorol.Soc.2013,139,176–183.[CrossRef]
54. Takeyasu,K.;Nagao,K.Estimationofsmoothingconstantofminimumvarianceanditsapplicationtoindustrialdata.Ind.Eng.
Manag.Syst.2008,7,44–50.
55. Hou,J.;Pelillo,M.Asimplefeaturecombinationmethodbasedondominantsets.PatternRecognit.2013,46,3129–3139.[CrossRef]
56. Ding,F.Combinedstateandleastsquaresparameterestimationalgorithmsfordynamicsystems.Appl.Math.Model.2014,38,
403–412.[CrossRef]
57. Lu,Y.;Li,Y.;Liang,W.;Song,Q.;Liu,Y.;Qin,X.Vegetablepricepredictionbasedonpso-bpneuralnetwork. InProceedings
ofthe20158thInternationalConferenceonIntelligentComputationTechnologyandAutomation(ICICTA),Nanchang,China,
14–15June2015;pp.1093–1096.[CrossRef]

Agriculture2023,13,1671 20of20
58. Arlot,S.;Celisse,A.Asurveyofcross-validationproceduresformodelselection.Statist.Surv.2010,4,40–79.[CrossRef]
59. Fayed,H.A.;Atiya,A.F.Speedupgrid-searchforparameterselectionofsupportvectormachines.Appl.SoftComput.2019,80,
202–210.[CrossRef]
60. Guo,X.;Li,D.;Zhang,A.Improvedsupportvectormachineoilpriceforecastmodelbasedongeneticalgorithmoptimization
parameters.AasriProcedia2012,1,525–530.[CrossRef]
61. Wang,D.;Tan,D.;Liu,L.Particleswarmoptimizationalgorithm:Anoverview.SoftComput.2018,22,387–408.[CrossRef]
62. Chen,J.;He,L.;Quan,Y.;Jiang,W.ApplicationofBPNeuralNetworksbasedongeneticsimulatedannealingalgorithmfor
shorttermelectricitypriceforecasting.InProceedingsofthe2014InternationalConferenceonAdvancesinElectricalEngineering
(ICAEE),Vellore,India,9–11January2014;pp.1–6.[CrossRef]
63. Ye,K.;Piao,Y.;Zhao,K.;Cui,X.AheterogeneousgraphenhancedLSTMnetworkforhogpricepredictionusingonlinediscussion.
Agriculture2021,11,359.[CrossRef]
64. Drury,B.;Roche,M.Asurveyoftheapplicationsoftextminingforagriculture. Comput. Electron. Agric. 2019,163,104864.
[CrossRef]
65. Li,J.;Li,G.;Liu,M.;Zhu,X.;Wei,L.Anoveltext-basedframeworkforforecastingagriculturalfuturesusingmassiveonlinenews
headlines.Int.J.Forecast.2022,38,35–50.[CrossRef]
66. An,W.;Wang,L.;Zeng,Y.R.Text-basedsoybeanfuturespriceforecasting:Atwo-stagedeeplearningapproach.J.Forecast.2023,
42,312–330.[CrossRef]
67. Zhao, L.; Zeng, G.; Wang, W.; Zhang, Z.Forecastingoilpriceusingweb-basedsentimentanalysis. Energies2019, 12, 4291.
[CrossRef]
68. Ling,L.; Zhang, D.; Mugera, A.W.; Chen,S.; Xia,Q.Aforecastcombinationframeworkwithmulti-timescaleforlivestock
Products’priceforecasting.Math.Probl.Eng.2019,2019,1–11.[CrossRef]
69. Liwen,L.;Shixin,C.;Dabin,Z.;Boting,Z.AMulti-TimeScalesCombinationStrategyforPorkPriceForecasting.J.Syst.Sci.Math.
Sci.2021,41,2829–2842.
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.