|     | Learning | Transferable |     |     | Features | with Deep | Adaptation | Networks |     |     |
| --- | -------- | ------------ | --- | --- | -------- | --------- | ---------- | -------- | --- | --- |
MingshengLong†♯
MINGSHENG@TSINGHUA.EDU.CN
| YueCao†          |     |     |     |     |     |     | YUE-CAO14@MAILS.TSINGHUA.EDU.CN |                         |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | ------------------------------- | ----------------------- | --- | --- |
| JianminWang†     |     |     |     |     |     |     |                                 | JIMWANG@TSINGHUA.EDU.CN |     |     |
| MichaelI.Jordan♯ |     |     |     |     |     |     |                                 | JORDAN@BERKELEY.EDU     |     |     |
†SchoolofSoftware,TNListLabforInfo.Sci.
&Tech.,InstituteforDataScience,TsinghuaUniversity,China
♯DepartmentofElectricalEngineeringandComputerScience,UniversityofCalifornia,Berkeley,CA,USA
Abstract data from relevant source domains to the target domains.
Recentstudiesrevealthatadeepneuralnetwork Domainadaptationaddressestheproblemthatwehavedata
fromtworelateddomainsbutunderdifferentdistributions.
| can | learn transferable | features | which | generalize |     |     |     |     |     |     |
| --- | ------------------ | -------- | ----- | ---------- | --- | --- | --- | --- | --- | --- |
Thedomaindiscrepancyposesamajorobstacleinadapting
| welltonoveltasksfordomainadaptation. |                                     |     |     |     | How- |                                |               |                     |           |        |
| ------------------------------------ | ----------------------------------- | --- | --- | --- | ---- | ------------------------------ | ------------- | ------------------- | --------- | ------ |
|                                      |                                     |     |     |     |      | predictivemodelsacrossdomains. |               | Forexample,anobject |           |        |
| ever,                                | as deepfeatureseventuallytransition |     |     |     | from |                                |               |                     |           |        |
|                                      |                                     |     |     |     |      | recognition                    | model trained | on manually         | annotated | images |
generaltospecificalongthenetwork,thefeature
transferabilitydropssignificantlyinhigherlayers maynotgeneralizewellontestingimagesundersubstantial
|                                  |     |     |     |            |     | variationsinthepose,occlusion,orillumination. |     |     |     | Domain |
| -------------------------------- | --- | --- | --- | ---------- | --- | --------------------------------------------- | --- | --- | --- | ------ |
| withincreasingdomaindiscrepancy. |     |     |     | Hence,itis |     |                                               |     |     |     |        |
adaptationestablishesknowledgetransferfromthelabeled
importanttoformallyreducethedatasetbiasand
enhancethetransferabilityintask-specificlayers. sourcedomaintotheunlabeledtargetdomainbyexploring
|     |     |     |     |     |     | domain-invariant | structures | that bridge | different | domains |
| --- | --- | --- | --- | --- | --- | ---------------- | ---------- | ----------- | --------- | ------- |
Inthispaper,weproposeanewDeepAdaptation
ofsubstantialdistributiondiscrepancy(Pan&Yang,2010).
| Network | (DAN) | architecture, | which | generalizes |     |     |     |     |     |     |
| ------- | ----- | ------------- | ----- | ----------- | --- | --- | --- | --- | --- | --- |
deepconvolutionalneuralnetworktothedomain One of the main approaches to establishing knowledge
adaptationscenario. InDAN,hiddenrepresenta- transfer is to learn domain-invariant models from data,
tionsofalltask-specificlayersareembeddedina
|     |     |     |     |     |     | whichcanbridgethesourceandtargetdomainsin |     |     |     | aniso- |
| --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | ------ |
reproducingkernelHilbertspacewherethemean morphiclatentfeaturespace.Inthisdirection,afruitfulline
embeddingsofdifferentdomaindistributionscan
ofpriorworkhasfocusedonlearningshallowfeaturesby
be explicitly matched. The domain discrepancy jointlyminimizingadistancemetricofdomaindiscrepancy
is furtherreducedusingan optimalmulti-kernel (Panetal.,2011;Longetal.,2013;Baktashmotlaghetal.,
selectionmethodformeanembeddingmatching.
2013;Gongetal.,2013;Zhangetal.,2013;Ghifaryetal.,
DANcanlearntransferablefeatureswithstatisti- 2014; Wang&Schneider, 2014). However, recentstudies
calguarantees,andcanscalelinearlybyunbiased
haveshownthatdeepneuralnetworkscanlearnmoretrans-
estimateofkernelembedding.Extensiveempiri- ferablefeaturesfordomainadaptation(Glorotetal.,2011;
calevidenceshowsthattheproposedarchitecture Donahueetal.,2014;Yosinskietal.,2014),whichproduce
| yields | state-of-the-art | image | classification |     | error |                     |        |                           |     |     |
| ------ | ---------------- | ----- | -------------- | --- | ----- | ------------------- | ------ | ------------------------- | --- | --- |
|        |                  |       |                |     |       | breakthroughresults | onsome | domainadaptationdatasets. |     |     |
ratesonstandarddomainadaptationbenchmarks. Deep neural networks are able to disentangle exploratory
factorsofvariationsunderlyingthedatasamples,andgroup
featureshierarchicallyinaccordancewiththeirrelatedness
1. Introduction
toinvariantfactors,makingrepresentationsrobusttonoise.
The generalization error of supervised learning machines Whiledeepneuralnetworksaremorepowerfulforlearning
withlimitedtrainingsampleswillbeunsatisfactorilylarge, generalandtransferablefeatures,thelatestfindingsalsore-
whilemanuallabelingofsufficienttrainingdatafordiverse
vealthatthedeepfeaturesmusteventuallytransitionfrom
applicationdomainsmaybeprohibitive.Therefore,thereis generaltospecificalongthenetwork,andfeaturetransfer-
incentivetoestablishingeffectivealgorithmstoreducethe ability dropssignificantlyin higherlayerswith increasing
labelingcost, typically byleveragingoff-the-shelflabeled domaindiscrepancy.Inotherwords,thefeaturescomputed
|     |     |     |     |     |     | in higher | layers of the | network must | depend | greatly on |
| --- | --- | --- | --- | --- | --- | --------- | ------------- | ------------ | ------ | ---------- |
32nd
| Proceedings                 | of the | International      | Conference |     | on Machine |                            |     |                       |     |       |
| --------------------------- | ------ | ------------------ | ---------- | --- | ---------- | -------------------------- | --- | --------------------- | --- | ----- |
|                             |        |                    |            |     |            | the specificdatasetandtask |     | (Yosinskietal.,2014), |     | which |
| Learning,Lille,France,2015. |        | JMLR:W&CPvolume37. |            |     | Copy-      |                            |     |                       |     |       |
aretask-specificfeaturesandarenotsafelytransferableto
right2015bytheauthor(s).

LearningTransferableFeatureswithDeepAdaptationNetworks
noveltasks. Anothercuriousphenomenonisthatdisentan- computer vision (Saenkoetal., 2010; Gongetal., 2012;
glingthevariationalfactorsinhigherlayersofthenetwork Baktashmotlaghetal., 2013; Longetal., 2013), etc. It is
mayenlargethedomaindiscrepancy,asdifferentdomains widelyrecognizedthatthedomaindiscrepancyintheprob-
withthenewdeeprepresentationsbecomemore“compact” ability distributions of different domains should be for-
andaremoremutuallydistinguishable(Glorotetal.,2011). mallymeasuredandreduced. Themajorbottleneckishow
Although deep features are salient for discrimination, en- to match different domain distributions effectively. Most
largeddatasetbiasmaydeterioratedomainadaptationper- existingmethodslearnanewshallowrepresentationmodel
formance, resulting in statistically unbounded risk for the inwhichthedomaindiscrepancycanbeexplicitlyreduced.
targettasks(Mansouretal.,2009;Ben-Davidetal.,2010). However, without learning deep features which can sup-
pressdomain-specificfactors,thetransferabilityofshallow
Inspired by the literature’s latest understanding about the
featurescouldbelimitedbythetask-specificvariability.
transferabilityofdeepneuralnetworks,weproposeinthis
paperanewDeepAdaptationNetwork(DAN)architecture, Deep neuralnetworkslearn nonlinearrepresentationsthat
whichgeneralizesdeepconvolutionalneuralnetworktothe disentangleandhidedifferentexplanatoryfactorsofvaria-
domain adaptation scenario. The main idea of this work tionbehinddatasamples(Bengioetal.,2013).Thelearned
istoenhancethefeaturetransferabilityinthetask-specific deep representationsmanifestinvariantfactorsunderlying
layers of the deep neural network by explicitly reducing differentpopulationsandaretransferablefromtheoriginal
thedomaindiscrepancy. Toestablishthisgoal,thehidden taskstosimilarnoveltasks(Yosinskietal.,2014). Hence,
representationsofallthetask-specificlayersareembedded deepneuralnetworkshavebeenexploredfordomainadap-
toareproducingkernelHilbertspacewherethemeanem- tation (Glorotetal., 2011; Chenetal., 2012), multimodal
beddingsofdifferentdomaindistributionscanbeexplicitly and multi-source learning problems (Ngiametal., 2011;
matched. Asmeanembeddingmatchingissensitivetothe Geetal.,2013),wheresignificantperformancegainshave
kernelchoices,anoptimalmulti-kernelselectionprocedure beenobtained. However,allthesemethodsdependonthe
isdevisedtofurtherreducethedomaindiscrepancy.Inad- assumption that deep neural networks can learn invariant
dition,weimplementalinear-timeunbiasedestimateofthe representationsthataretransferableacrossdifferenttasks.
kernelmeanembeddingtoenablescalabletraining,which In reality, the domain discrepancy can be alleviated, but
isverydesirablefordeeplearning.Finally,asdeepmodels notremoved,bydeepneuralnetworks(Glorotetal.,2011).
pre-trainedwithlarge-scalerepositoriessuchasImageNet Datasetshifthasposedabottlenecktothetransferabilityof
(Russakovskyetal., 2014) are representative for general- deepnetworks,resultinginstatisticallyunboundedriskfor
purposetasks(Yosinskietal.,2014;Hoffmanetal.,2014), targettasks(Mansouretal.,2009;Ben-Davidetal.,2010).
the proposed DAN model is trained by fine-tuning from
OurworkisprimarilymotivatedbyYosinskietal.(2014),
theAlexNetmodel(Krizhevskyetal.,2012)pre-trainedon
which comprehensivelyexplores feature transferability of
ImageNet,whichisimplementedinCaffe(Jiaetal.,2014).
deep convolutionalneural networks. The method focuses
Comprehensive empirical evidence demonstrates that the
onadifferentscenariowherethelearningtasksarediffer-
proposed architecture outperforms state-of-the-art results
ent across domains, hence it requires sufficient target la-
evaluatedonthestandarddomainadaptationbenchmarks.
beled examples such that the source network can be fine-
The contributions of this paper are summarized as fol- tuned to the target task. In many real problems, labeled
lows. (1) We propose a noveldeep neuralnetwork archi- data is usually limited especially for a novel target task,
tecturefordomainadaptation,inwhichallthelayerscor- hencethemethodcannotbedirectlyapplicabletodomain
responding to task-specific features are adapted in a lay- adaptation.Thereareseveralveryrecenteffortsinlearning
erwise manner, hence benefiting from “deep adaptation.” domain-invariantfeaturesin the contextof shallow neural
(2)Weexploremultiplekernelsforadaptingdeeprepresen- networks (Ajakanetal., 2014; Ghifaryetal., 2014). Due
tations,whichsubstantiallyenhancesadaptationeffective- to the limited capacity of shallow architectures, the per-
ness compared to single kernel methods. Our model can formance of these proposals does not surpass deep CNN
yieldunbiaseddeepfeatureswithstatisticalguarantees. (Krizhevskyetal., 2012). Tzeng et al. (2014) proposed a
DDCmodelthataddsanadaptationlayerandadatasetshift
2. RelatedWork losstothedeepCNN forlearningadomain-invariantrep-
resentation. Whileperformancewasimproved,DDConly
Arelatedliteratureistransferlearning(Pan&Yang,2010), adaptsasinglelayerofthenetwork,whichmayberestric-
whichbuildsmodelsthatbridgedifferentdomainsortasks, tiveinthattherearemultiplelayerswherethehiddenfea-
explicitly taking domain discrepancy into consideration. tures are not transferable (Yosinskietal., 2014). DDC is
Transferlearningaimstomitigatetheeffortofmanualla- also limited by suboptimalkernelmatchingof probability
beling for machine learning (Panetal., 2011; Gongetal., distributions(Grettonetal.,2012b)anditsquadraticcom-
2013; Zhangetal., 2013; Wang&Schneider, 2014) and putationalcostthatrestrictstransferabilityandscalability.

LearningTransferableFeatureswithDeepAdaptationNetworks
3. DeepAdaptation Networks
learn learn learn learn
Inunsuperviseddomainadaptation,wearegivenasource
a do t m ar a g i e n t D do s m = ai { n (x D s i t ,y = i s)} { n i x = s t j 1 } w n j= t it 1 h w n s ith lab n e t le u d nl e a x b a e m le p d le e s x , a a m nd - frozen frozen frozen fi tu n n e e - fi tu n n e e - M M M K D - M M M K D - M M M K D - s o o t o a u u u r t t g p p rc e u u e t t t
ples. The source domain and target domain are charac-
terized by probability distributions p and q, respectively. input conv1 conv2 conv3 conv4 conv5 fc6 fc7 fc8
We aim to construct a deep neural network which is able
to learn transferablefeaturesthatbridgethe cross-domain Figure1.TheDANarchitectureforlearningtransferablefeatures.
discrepancy, and build a classifier y = θ(x) which can Sincedeepfeatureseventuallytransitionfromgeneraltospecific
minimize target risk ǫ t (θ) = Pr (x,y)∼q [θ(x)6=y] using alongthenetwork,(1)thefeaturesextractedbyconvolutionallay-
source supervision. In semi-supervised adaptation where ersconv1–conv3 aregeneral, hencetheselayersarefrozen, (2)
thetargethasasmallnumberoflabeledexamples,wede- the features extracted by layers conv4–conv5 are slightly less
note by D = {(xa,ya)} the n annotated examples of transferable, hence these layers are learned via fine-tuning, and
a i i a (3) fully connected layers fc6–fc8 are tailored to fit specific
sourceandtargetdomains.
tasks,hencetheyarenottransferableandshouldbeadaptedwith
MK-MMD.
3.1.Model
MK-MMD Domainadaptationischallenginginthatthe
targetdomainhasno(oronlylimited)labeledinformation.
adoptedfor the mean embeddingsof p and q is criticalto
To approach this problem, many existing methods aim to
ensurethetestpowerandlow testerror. Themulti-kernel
boundthetargeterrorbythesourceerrorplusadiscrepancy
kcanleveragedifferentkernelstoenhanceMK-MMDtest,
metricbetweenthesourceandthetarget(Ben-Davidetal.,
leadingtoaprincipledmethodforoptimalkernelselection.
2010). Two classes of statistics have been explored for
thetwo-sampletesting,whereacceptanceorrejectiondeci- One of the feasible strategies for controlling the domain
sionsaremadeforanullhypothesisp = q,givensamples discrepancy is to find an abstract feature representation
generatedrespectivelyfrompandq: energydistancesand through which the source and target domains are simi-
maximum mean discrepancies (MMD) (Sejdinovicetal., lar (Ben-Davidetal., 2010). Although this idea has been
2013).Inthispaper,wefocusonthemultiplekernelvariant explored in several papers (Panetal., 2011; Zhangetal.,
ofMMD(MK-MMD)proposedbyGrettonetal.(2012b), 2013;Wang&Schneider,2014),todatetherehasbeenno
which is formalized to jointly maximize the two-sample attempttoenhancethetransferabilityoffeaturerepresenta-
test powerandminimizethe TypeII error,i.e., the failure tionviaMK-MMDindeepneuralnetworks.
ofrejectingafalsenullhypothesis.
DeepAdaptationNetworks(DAN) Inthispaper,weex-
Denote by H be the reproducing kernel Hilbert space ploretheideaofMK-MMD-basedadaptationforlearning
k
(RKHS)endowedwithacharacteristickernelk. Themean transferablefeaturesindeepnetworks. Westartwithdeep
embedding of distribution p in H is a unique element convolutional neural networks (CNN) (Krizhevskyetal.,
k
µ
k
(p) such that Ex∼p f(x) = hf(x),µ
k
(p)i
Hk
for all 2012), a strong model when it is adapted to novel tasks
f ∈H . TheMK-MMDd (p,q)betweenprobabilitydis- (Donahueetal., 2014; Hoffmanetal., 2014). The main
k k
tributionspandqisdefinedastheRKHSdistancebetween challenge is that the target domain has no or just limited
themeanembeddingsofpandq. Thesquaredformulation labeled information, hence directly adapting CNN to the
ofMK-MMDisdefinedas target domain via fine-tuning is impossible or is prone to
over-fitting. With the idea of domain adaptation, we are
d2 k (p,q), E p [φ(xs)]−E q φ xt 2 Hk . (1) targetingadeepadaptationnetwork(DAN)thatcanexploit
both source-labeled data and target-unlabeled data. Fig-
Themostimportan (cid:13) (cid:13)tpropertyisthatp (cid:2) = (cid:0) qiff (cid:1)(cid:3) d (cid:13) (cid:13) 2 k (p,q)=0 ure1givesanillustrationoftheproposedDANmodel.
(Grettonetal.,2012a).Thecharacteristickernelassociated
with the feature map φ, k(xs,xt) = hφ(xs),φ(xt)i, is We extend the AlexNet architecture (Krizhevskyetal.,
definedastheconvexcombinationofmPSDkernels{k }, 2012), which is comprised of five convolutional layers
u
(conv1–conv5) and three fully connected layers (fc6–
m m fc8). Each fc layer ℓ learns a nonlinear mapping hℓ =
K, k = β u k u : β u =1,β u >0,∀u , (2) fℓ Wℓhℓ−1+bℓ , wherehℓ isthe ℓthlayerhidden i rep-
( ) i i
u X =1 u X =1 resentationofpointx i ,Wℓandbℓaretheweightsandbias
(cid:0) (cid:1)
wherethe constraintsoncoefficients{β }are imposedto of the ℓth layer, and fℓ is the activation, taking as recti-
u
guaranteethatthe derivedmulti-kernelk is characteristic. fierunitsfℓ(x) = max(0,x)forhiddenlayersorsoftmax
AsstudiedtheoreticallyinGrettonetal.(2012b),thekernel unitsfℓ(x) = e x / |x| exj fortheoutputlayer. Letting
j=1
P

LearningTransferableFeatureswithDeepAdaptationNetworks
l
Θ = Wℓ,bℓ denotethesetofallCNNparameters, thatdistinguishDANfromrelevantliteratureare:(1)multi-
ℓ=1
theempiricalriskofCNNis layer adaptation. As revealed by (Yosinskietal., 2014),
| (cid:8) |     | (cid:9) |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
featuretransferabilitygetsworseonconv4–conv5andsig-
na
|     |     | 1   |              |     |     |     | nificantly | drops | on fc6–fc8, |     | hence | it is critical | to  | adapt |
| --- | --- | --- | ------------ | --- | --- | --- | ---------- | ----- | ----------- | --- | ----- | -------------- | --- | ----- |
|     |     | min | J(θ(xa),ya), |     |     | (3) |            |       |             |     |       |                |     |       |
i i multiple layers instead of only one layer. In other words,
|     |     | Θ n a |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i=1
|     |     |     | X   |     |     |     | adapting | a single | layer | cannot | undo | the dataset | bias | be- |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ----- | ------ | ---- | ----------- | ---- | --- |
where is the cross-entropy loss function, and θ(xa) is tween the source and the target, since there are other lay-
J
i
the conditionalprobabilitythattheCNN assignsxa tola- ersthatarenottransferable.Anotherbenefitofmulti-layer
i
bel ya. We will notdiscuss how to computethe convolu- adaptationisthatbyjointlyadaptingtherepresentationlay-
i
ersandtheclassifierlayer,wecouldessentiallybridgethe
tionallayersaswewillnotimposedistribution-adaptation
regularizationinthoselayers, giventhattheconvolutional domaindiscrepancyunderlyingboththemarginaldistribu-
layerscanlearngenericfeaturesthattendtobetransferable tion and the conditional distribution, which is crucial for
in layers conv1–conv3 and are slightly domain-biased in domain adaptation (Zhangetal., 2013). (2) multi-kernel
conv4–conv5(Yosinskietal., 2014). Hence,whenadapt- adaptation.AspointedoutbyGrettonetal.(2012b),kernel
choiceiscriticaltothetestingpowerofMMDsincediffer-
| ingthe | pre-trainedAlexNetto |     |     | thetarget, | we  | optto freeze |     |     |     |     |     |     |     |     |
| ------ | -------------------- | --- | --- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
conv1–conv3 and fine-tune conv4–conv5 to preserve the entkernelsmayembedprobabilitydistributionsindifferent
efficacyoffragileco-adaptation(Hintonetal.,2012). RKHSswheredifferentordersofsufficientstatisticscanbe
emphasized.Thisiscrucialformomentmatching,whichis
InstandardCNNs,deepfeaturesmusteventuallytransition
notwellexploredbypreviousdomainadaptationmethods.
fromgeneraltospecificbythelastlayerofthenetwork,and
thetransferabilitygapgrowswiththedomaindiscrepancy
3.2.Algorithm
andbecomesparticularlylargewhentransferringthehigher
layersfc6–fc8(Yosinskietal.,2014). Inotherwords,the LearningΘ Usingthekerneltrick,MK-MMD(1)canbe
fclayersaretailoredtotheiroriginaltaskattheexpenseof computedastheexpectationofkernelfunctionsd2(p,q)=
k
degradedperformanceonthetargettask,hencetheycannot Exsx′sk(xs,x′s) k(xt,x′t) k(xs,xt),
|     |     |     |     |     |     |     |     |     | + E | xtx′t |     | − 2Exsxt |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | -------- | --- | --- |
bedirectlytransferredtothetargetdomainviafine-tuning wherexs,x′si id p,xt,x′ti id
|                               |     |     |     |                         |     |     |     |     | ∼   | ∼   | q,andk | ∈ K. | However,this |     |
| ----------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | ------ | ---- | ------------ | --- |
| withlimitedtargetsupervision. |     |     |     | Inthispaper,wefine-tune |     |     |     |     |     |     |        |      |              |     |
computationincursacomplexityofO(n2),whichisrather
| CNN on | the source | labeled | examplesand |     | require | the dis- |             |     |      |       |        |       |         |      |
| ------ | ---------- | ------- | ----------- | --- | ------- | -------- | ----------- | --- | ---- | ----- | ------ | ----- | ------- | ---- |
|        |            |         |             |     |         |          | undesirable | for | deep | CNNs, | as the | power | of deep | neu- |
tributionsofthesourceandtargettobecomesimilarunder
ralnetworkslargelyderivesfromlearningwithlarge-scale
| the hidden | representationsof |               | fully    | connected |              | layers fc6– |           |           |      |           |       |            |            |       |
| ---------- | ----------------- | ------------- | -------- | --------- | ------------ | ----------- | --------- | --------- | ---- | --------- | ----- | ---------- | ---------- | ----- |
|            |                   |               |          |           |              |             | datasets. | Moreover, | the  | summation |       | over       | pairwise   | simi- |
| fc8. This  | can               | be realizedby | addingan |           | MK-MMD-based |             |           |           |      |           |       |            |            |       |
|            |                   |               |          |           |              |             | larities  | between   | data | points    | makes | mini-batch | stochastic |       |
multi-layeradaptationregularizer(1)totheCNNrisk(3):
gradientdescent(SGD)moredifficult,whereasmini-batch
na l2 SGD is crucial to the training effectiveness of deep net-
1
min J(θ(xa),ya)+λ d2 Dℓ,Dℓ , (4) works. WhilepriorworkbasedonMMD(Panetal.,2011;
|     |     | i   | i   |       | k       | s t     |                                                      |     |     |     |     |                |     |     |
| --- | --- | --- | --- | ----- | ------- | ------- | ---------------------------------------------------- | --- | --- | --- | --- | -------------- | --- | --- |
| Θ   | n a |     |     |       |         |         | Tzengetal.,2014)rarelyaddressesthisissue,webelieveit |     |     |     |     |                |     |     |
|     | i=1 |     |     | ℓ =l1 |         |         |                                                      |     |     |     |     |                |     |     |
|     | X   |     |     | X     | (cid:0) | (cid:1) |                                                      |     |     |     |     |                |     |     |
|     |     |     |     |       |         |         | iscriticalinthecontextofdeeplearning.                |     |     |     |     | Inthispaper,we |     |     |
whereλ > 0isapenaltyparameter,l 1 andl 2 arelayerin- adopt the unbiased estimate of MK-MMD (Grettonetal.,
dicesbetweenwhichtheregularizeriseffective.Inourim- 2012b) which can be computed with linear complexity.
| plementationofDAN,wesetl |     |     |     | = 6andl |     | = 8,although |                    |     |         |     |     |       |       |       |
| ------------------------ | --- | --- | --- | ------- | --- | ------------ | ------------------ | --- | ------- | --- | --- | ----- | ----- | ----- |
|                          |     |     |     | 1       | 2   |              | More specifically, |     | d2(p,q) |     | = 2 | ns/2g | (z ), | where |
|                          |     |     |     |         |     |              |                    |     | k       |     | ns  | i=1   | k i   |       |
differentconfigurationsarealsopossible,dependingonthe
|     |     |     |     |     |     |     | we denote | quad-tuple |     | z , | (xs | ,xs ,xt | ,xt | ), and |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | --- | --- | ------- | --- | ------ |
sizeofthelabeledsourcedatasetandthenumberofparam- i 2i−1P2i 2i−1 2i
|                                          |     |     |     |     |     |      | evaluatemulti-kernelfunctionk |     |     |        | oneachquad-tuplez |        |     | by  |
| ---------------------------------------- | --- | --- | --- | --- | --- | ---- | ----------------------------- | --- | --- | ------ | ----------------- | ------ | --- | --- |
| etersinthelayersthataretobefine-tuned.Dℓ |     |     |     |     |     | h∗ℓ  |                               |     |     |        |                   |        |     | i   |
|                                          |     |     |     |     |     | = is |                               |     |     |        |                   |        |     |     |
|                                          |     |     |     |     |     | ∗ i  | g (z ),k(xs                   |     | ,xs | )+k(xt | ,xt               | )−k(xs | ,xt | )−  |
theℓthlayerhiddenrepresentationforthesourceandtarget k i 2i−1 2i 2i−1 2i 2i−1 2i
|           |     |          |     |            |     | (cid:8) (cid:9) | k(xs ,xt | ).   | This approachcomputesan |     |     |     | expectationof |     |
| --------- | --- | -------- | --- | ---------- | --- | --------------- | -------- | ---- | ----------------------- | --- | --- | --- | ------------- | --- |
| examples, | and | d2 Dℓ,Dℓ | is  | the MK-MMD |     | between the     | 2i       | 2i−1 |                         |     |     |     |               |     |
|           |     | k s      | t   |            |     |                 |          |      |                         |     |     |     |               |     |
independentvariablesasin(1)withcostO(n).
sourceandtargetevaluatedontheℓthlayerrepresentation.
|          |        | (cid:0)      | (cid:1) |         |        |            |         |       |          |     |            |      |     |      |
| -------- | ------ | ------------ | ------- | ------- | ------ | ---------- | ------- | ----- | -------- | --- | ---------- | ---- | --- | ---- |
|          |        |              |         |         |        |            | When we | train | deep CNN | by  | mini-batch | SGD, | we  | only |
| Training | a deep | CNN requires |         | a large | amount | of labeled |         |       |          |     |            |      |     |      |
needtoconsiderthegradientofobjective(4)withrespectto
| data, which  |             | is prohibitive                       | for  | many      | domain  | adaptation     |                            |     |                                     |     |                        |     |     |     |
| ------------ | ----------- | ------------------------------------ | ---- | --------- | ------- | -------------- | -------------------------- | --- | ----------------------------------- | --- | ---------------------- | --- | --- | --- |
|              |             |                                      |      |           |         |                | eachdatapointx             |     | . Sincethelinear-timeMK-MMDtakes    |     |                        |     |     |     |
| problems,    | hence       | we start                             | with | an        | AlexNet | model pre-     |                            |     | i                                   |     |                        |     |     |     |
|              |             |                                      |      |           |         |                | a nicesummationformthatcan |     |                                     |     | bereadilydecoupledinto |     |     |     |
| trained      | on ImageNet | 2012                                 | and  | fine-tune | it      | as in Yosinski |                            |     |                                     |     |                        |     |     |     |
|              |             |                                      |      |           |         |                | thesumofg                  | (z  | )’s,weonlyneedtocomputethegradients |     |                        |     |     |     |
| etal.(2014). |             | WiththeproposedDANoptimizationframe- |      |           |         |                |                            | k   | i                                   |     |                        |     |     |     |
∂g (z ℓ )
work(4), weareabletolearntransferablefeaturesfroma k i forthequad-tuplezℓ = hs ℓ ,hs ℓ ,ht ℓ ,ht ℓ of
|     |     |     |     |     |     |     | ∂ Θ ℓ   |                             |     | i   | 2 i−1 | 2 i                  | 2 i−1 | 2 i |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------------------------- | --- | --- | ----- | -------------------- | ----- | --- |
|     |     |     |     |     |     |     | the ℓth | layer hiddenrepresentation. |     |     |       | To be consistentwith |       |     |
sourcedomaintoarelatedtargetdomain.Thelearnedrep-
|     |     |     |     |     |     |     |     |     |     |     | (cid:0) |     |     | (cid:1) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | ------- |
resentation can both be salient benefiting from CNN, and the gradient of MK-MMD, we need to compute the cor-
(z
unbiasedthankstoMK-MMD.Twoimportantadvantages responding gradient of CNN risk ∂ J i), where J(z ) =
|     |     |     |     |     |     |     |     |     |     |     | ∂   | Θ ℓ |     | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

LearningTransferableFeatureswithDeepAdaptationNetworks
J(θ(xa),ya), and {(xa,ya)} indicates the labeled aimingto consolidatethe transferabilityof DAN features.
i′ i′ i′ i′ i′
examples in quad-tuple z —for instance, in unsupervised We accordinglyadoptanalternatingoptimizationthatup-
i
P
adaptationwherethetargetdomainhasnolabeleddata,we datesΘbymini-batchSGD(5)andβbyQP(8)iteratively.
have {(xa,ya)} = {(xs ,ys ),(xs ,ys )}. To per- BothupdatescostO(n)andarescalabletolargedatasets.
i′ i′ 2i−1 2i−1 2i 2i
formamini-batchupdate,wecomputethegradientofob-
jective(4)withrespecttotheℓthlayerparameterΘℓ as 3.3.Analysis
∂J(z ) ∂g zℓ Weprovideananalysisoftheexpectedtarget-domainrisk
∇ Θℓ = ∂Θℓ i +λ ∂ k Θℓ i . (5) ofourapproach,makinguseofthetheoryofdomainadap-
(cid:0) (cid:1) tation(Ben-Davidetal.,2007;2010;Mansouretal.,2009)
Suchamini-batchSGDcanbeeasilyimplementedwithin andthetheoryofkernelembeddingofprobabilitydistribu-
the Caffe framework for CNNs (Jiaetal., 2014). Given tions(Sriperumbuduretal.,2009;Grettonetal.,2012a;b).
kernelk as the linear combinationof m Gaussian kernels
{ b k e u re ( a x d i i , l x y j c ) om = p e u − te k d x i u − s x in jk g 2/ th γ e u} c , ha th in e r g u r l a e d . i F e o n r t in ∂g s ∂ k ta Θ ( n z ℓ ℓ i c ) e, can t T h h e e e o x r p e e m cte 1 d L ri e s t k θ so ∈ fs H ou b r e ce a a h n y d po ta th rg e e si t s r , e ǫ s s p ( e θ c ) ti a v n e d ly ǫ , t t ( h θ e ) n be
∂k(hsℓ ,htℓ) m 2β ǫ t (θ)6ǫ s (θ)+2d k (p,q)+C, (9)
2i−1 2i =− u k hsℓ ,htℓ
∂Wℓ γ u 2i−1 2i where C is a constant for the complexity of hypothesis
u
u=1
X (cid:0) (cid:1) (6) spaceandtheriskofanidealhypothesisforbothdomains.
× hsℓ −htℓ
2i−1 2i
T Proofsketch: AresultfromBen-Davidetal.(2007)shows
×(cid:0)I hs(ℓ−1) −(cid:1) I ht(ℓ−1) ,
2i−1 2i thatǫ (θ) 6 ǫ (θ)+d (p,q)+C ,whered (p,q)isthe
t s H 0 H
(cid:16) h i h i(cid:17) H-divergencebetweenpandq,whichisdefinedas
where the last row computes the gradientof the ℓth layer
rectifierunits,withIbeingdefinedasanindicatorsuchthat
d (p,q),2sup Pr [η(xs)=1]− Pr η(xt)=1 .
I hℓ
j
−
i
1 =hℓ
j
−
i
1ifW
j
ℓ
·
hℓ
i
−1+bℓ
j
>0,elseI hℓ
j
−
i
1 =0. H
η∈H(cid:12)
xs∼p xt∼q
(cid:12)
(cid:12) (cid:2) (1(cid:3)(cid:12)0)
L(cid:2)earnin(cid:3)gβ Theproposedmulti-layeradapta(cid:2)tionre(cid:3)gular- (cid:12) (cid:12)
TheH-divergence(cid:12)reliesonthecapacityofthehypothes(cid:12)is
izerperformslayerwisematchingbyMK-MMD,hencewe
space H to distinguishdistributionsp fromq, and η ∈ H
seektolearnoptimalkernelparameterβforMK-MMDby
canbeviewedasatwo-sampleclassifier. Bychoosingηas
jointlymaximizingthetestpowerandminimizingtheType
a (kernel) Parzen window classifier (Sriperumbuduretal.,
IIerror(Grettonetal.,2012b),leadingtotheoptimization
2009),d (p,q)canbeboundedbytheempiricalestimate
H
maxd2 k D s ℓ,D t ℓ σ k −2, (7) d (p,q)6dˆ (D ,D )+C
k∈K H H s t 1
L w e h t e ti r n e g σ d k 2 = =E (d zg , k 2 d (z ,. ) . − ., [E d (cid:0) zg ) k T, (z ea ) c ] (cid:1) 2 h i d ses is ti M ma M ti D on v v ia ar k ia e n rn c e e l . 6 2 1− η i ∈ n H f "i n P = s 1 L[η( n xs i s )=1] + j P n = t 1 L[η(x n t j t )=−1] #! +C1
1 2 m u =2(1+d (p,q))+C ,
k . CovarianceQ = cov(g ) ∈ Rm×m canbecomputed k 1
u k (11)
inO(m2n)cost,i.e. Q uu′ = n 4 s n i= s/ 1 4g k ∆ u (¯z i )g k ∆ u′ (¯z i ), whereL(·)isthelinearlossfunctionoftheParzenwindow
where ¯z , (z ,z ) and g∆ (¯z ) , g (z ) − classifierη,L[η =1],−η,L[η =−1],η. Byexplicitly
i 2i−1 2i kPu i ku 2i−1
g (z ). Hence(7)reducestoaquadraticprogram(QP), minimizingMK-MMDinmultiplelayers,thefeaturesand
ku 2i
classifierlearnedbytheproposedDANmodelcandecrease
T
min β (Q+εI)β, (8) theupperboundontargetrisk.Thesourceclassifierandthe
dTβ=1,β>0
two-sampleclassifier togetherprovidea way to assess the
where ε = 10−3 is a small regularizerto make the prob- adaptationperformance,andcanfacilitatemodelselection.
lemwell-defined. Bysolving(8),weobtainamulti-kernel
NotethatwemaximizeMK-MMDw.r.t.β(7)tominimize
k = m β k thatjointlymaximizesthetestpowerand TypeIItesterror,andtohelptheParzenwindowclassifier
u=1 u u
minimizestheTypeIIerror. achieveminimalriskoftwo-samplediscriminationin(11).
P
WenotethattheDANobjective(4)isessentiallyaminimax
4. Experiments
problem;i.e.,wecomputeminmaxd2 Dℓ,Dℓ σ−2. The
k s t k
Θ K
CNNparameterΘislearnedbyminimizingMK-MMDas We compare the DAN model to state-of-the-art transfer
(cid:0) (cid:1)
adomaindiscrepancy,whiletheMK-MMDparameterβis learninganddeeplearningmethodson bothunsupervised
learnedbyminimizingthe TypeII error. Both criteria are andsemi-supervisedadaptationproblems,focusingonthe
dedicatedtoaneffectiveadaptationofdomaindiscrepancy, efficacyofmulti-layeradaptationwithmulti-kernelMMD.

LearningTransferableFeatureswithDeepAdaptationNetworks
4.1.Setup forsemi-supervisedadaptation. We comparetheaverages
andstandarderrorsofclassificationaccuracyforeachtask.
Office-31(Saenkoetal.,2010) Thisdatasetisastandard
For baseline methods, we follow the standard procedures
benchmarkfordomainadaptation. Itconsistsof4,652im-
formodelselectionasexplainedintheirrespectivepapers.
ageswithin31categoriescollectedfromthreedistinctdo-
For MMD-based methods (i.e., TCA, DDC, and DAN),
m
fro
a
m
ins
a
:
m
A
a
m
z
a
o
z
n
o
.
n
c
(
o
A
m
),
,
w
W
h
eb
ic
c
h
am
co
(
n
W
tai
)
n
a
s
n
i
d
m
D
ag
S
e
L
s
R
d
(
o
D
w
)
n
,
l
w
oa
h
d
ic
e
h
d we use a Gaussian kernel k(x
i
,x
j
) = e−kx i−x jk2/γ
withthebandwidthγ settothemedianpairwisedistances
areimagestakenbywebcameraanddigitalSLRcamerain
on the training data—the median heuristic (Grettonetal.,
anofficewithdifferentenvironmentvariation,respectively.
2012b). We use multi-kernel MMD for DAN, and con-
We evaluate our method across the 3 transfer tasks, A →
siderafamilyofmGaussiankernels{k }m byvarying
W,D→WandW→D,whicharecommonlyadoptedin u u=1
bandwidth γ between 2−8γ and 28γ with a multiplica-
deeplearningmethods(Donahueetal.,2014;Tzengetal., u
tivestep-sizeof21/2 (Grettonetal., 2012b). Asminimiz-
2014). Forcompleteness,wefurtherincludetheevaluation
ing MMD is equivalent to maximizing the error of clas-
ontheother3transfertasks,A→D,D→AandW→A.
sifying the source from the target (two-sample classifier)
Office-10 + Caltech-10 (Gongetal., 2012). This dataset
(Sriperumbuduretal., 2009), we can automatically select
consistsofthe10commoncategoriessharedbytheOffice-
the MMD penalty parameter λ on a validation set (com-
31 and Caltech-256 (C) (Griffinetal., 2007) datasets and
prisedofsource-labeledinstancesandtarget-unlabeledin-
iswidelyadoptedintransferlearningmethods(Longetal.,
stances) by jointly assessing the test errors of the source
2013;Baktashmotlaghetal.,2013). We canbuildanother
classifier and the two-sample classifier. We use the fine-
6transfertasks:A→C,W→C,D→C,C→A,C→W,
tuningarchitecture(Yosinskietal.,2014),however,dueto
andC→D.Withmoretransfertasks,wearetargetingan
limited training examples in our datasets, we fix convo-
unbiasedlookatthedatasetbias(Torralba&Efros,2011).
lutional layers conv1–conv3 that were copied from pre-
We compare to a variety of methods: TCA (Panetal., trainedmodel,fine-tuneconv4–conv5andfullyconnected
2011), GFK (Gongetal., 2012), CNN (Krizhevskyetal., layersfc6–fc7,andtrainclassifierlayerfc8,bothviaback
2012), LapCNN (Westonetal., 2008), and DDC propagation. As the classifier is trained from scratch, we
(Tzengetal., 2014). Specifically, TCA is a conventional set its learning rate to be 10 times that of the lower lay-
transferlearningmethodbasedonMMD-regularizedPCA. ers. We use stochastic gradient descent (SGD) with 0.9
GFK is a widely-adopted method for our datasets which momentumandthelearningrateannealingstrategyimple-
interpolates across intermediate subspaces to bridge the mentedin Caffe, and cross-validatebase learningrate be-
source and target. CNN was the leading method in the tween10−5and10−2withamultiplicativestep-size101/2.
ImageNet2012competition,anditturnsouttobeastrong
model for learning transferable features (Yosinskietal., 4.2.ResultsandDiscussion
2014). LapCNN is a semi-supervised variant of CNN
TheunsupervisedadaptationresultsonthefirstsixOffice-
basedonLaplaciangraphregularization.Finally,DDCisa
31 transfer tasks are shown in Table 1, and the results
domainadaptationvariantofCNNthataddsanadaptation
on the other six Office-10 + Caltech-10 transfer tasks are
layer between the fc7 and fc8 layers that is regularized
shownin Table 2. To directlycomparewith DDC, we re-
by single-kernel MMD. We implement the CNN-based
port semi-supervised adaptation results of the same tasks
methods, i.e., CNN, LapCNN, DDC, and DAN based on
used by DDC in Table 3. We can observe that DAN sig-
the Caffe (Jiaetal., 2014) implementation of AlexNet
nificantly outperforms the comparison methods on most
(Krizhevskyetal., 2012) trainedonthe ImageNetdataset.
transfertasks,andachievescomparableperformanceonthe
Inordertostudytheefficacyofmulti-layeradaptationand
easytransfertasks,D→WandW→D,wheresourceand
multi-kernel MMD, we evaluate severalvariants of DAN:
targetaresimilar(Saenkoetal., 2010). Thisisreasonable
(1) DAN using only one hidden layer, either fc7 or fc8
astheadaptabilitymayvaryacrossdifferenttransfertasks.
for adaptation, termed DAN and DAN respectively; (2)
7 8
The performanceboostdemonstratesthatour architecture
DAN using single-kernel MMD for adaptation, termed
ofmulti-layeradaptationviamulti-kernelMMDisableto
DAN .
SK
transferpre-traineddeepmodelsacrossdifferentdomains.
We mainly follow standard evaluation protocol for unsu-
From the experimental results, we can make the follow-
pervisedadaptationanduseallsourceexampleswithlabels
ingobservations. (1)Deeplearningbasedmethodssignif-
andalltargetexampleswithoutlabels(Gongetal., 2013).
icantly outperform conventionalshallow transfer learning
Tomakeourresultsdirectlycomparabletomostpublished
methods by a large margin. (2) Among the deep learn-
results,wereportaclassicalprotocol(Saenkoetal.,2010)
ing methods, the semi-supervised LapCNN provides no
in that we randomly down-sample the source examples,
improvementover CNN, suggesting that the challenge of
andfurtherrequire3labeledtargetexamplespercategory
domain discrepancy cannot be readily bridged by semi-

LearningTransferableFeatureswithDeepAdaptationNetworks
Table1.AccuracyonOffice-31datasetwithstandardunsupervisedadaptationprotocol(Gongetal.,2013).
|     | Method |     | A→W |     | D→W |     | W→D | A→D | D→A |     | W→A | Average |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
TCA 21.5±0.0 50.1±0.0 58.4±0.0 11.4±0.0 8.0±0.0 14.6±0.0 27.3
GFK 19.7±0.0 49.7±0.0 63.1±0.0 10.6±0.0 7.9±0.0 15.8±0.0 27.8
CNN 61.6±0.5 95.4±0.3 99.0±0.2 63.8±0.5 51.1±0.6 49.8±0.4 70.1
LapCNN 60.4±0.3 94.7±0.5 99.1±0.2 63.1±0.6 51.6±0.4 48.2±0.5 69.5
DDC 61.8±0.4 95.0±0.5 98.5±0.4 64.4±0.3 52.1±0.8 52.2±0.4 70.6
DAN 63.2±0.2 94.8±0.4 98.9±0.3 65.2±0.4 52.3±0.4 52.1±0.4 71.1
7
DAN 63.8±0.4 94.6±0.5 98.8±0.6 65.8±0.4 52.8±0.4 51.9±0.5 71.3
8
DAN 63.3±0.3 95.6±0.2 99.0±0.4 65.9±0.7 53.2±0.5 52.1±0.4 71.5
SK
DAN 68.5±0.4 96.0±0.3 99.0±0.2 67.0±0.4 54.0±0.4 53.1±0.3 72.9
Table2.AccuracyonOffice-10+Caltech-10datasetwithstandardunsupervisedadaptationprotocol(Gongetal.,2013).
|     | Method |     | A→C |     | W→C |     | D→C | C→A | C→W |     | C→D | Average |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
TCA 42.7±0.0 34.1±0.0 35.4±0.0 54.7±0.0 50.5±0.0 50.3±0.0 44.6
GFK 41.4±0.0 26.4±0.0 36.4±0.0 56.2±0.0 43.7±0.0 42.0±0.0 41.0
CNN 83.8±0.3 76.1±0.5 80.8±0.4 91.1±0.2 83.1±0.3 89.0±0.3 84.0
LapCNN 83.6±0.6 77.8±0.5 80.6±0.4 92.1±0.3 81.6±0.4 87.8±0.4 83.9
DDC 84.3±0.5 76.9±0.4 80.5±0.2 91.3±0.3 85.5±0.3 89.1±0.3 84.6
DAN 84.7±0.3 78.2±0.5 81.8±0.3 91.6±0.4 87.4±0.3 88.9±0.5 85.4
7
DAN 84.4±0.3 80.8±0.4 81.7±0.2 91.7±0.3 90.5±0.4 89.1±0.4 86.4
8
DAN 84.1±0.4 79.9±0.4 81.1±0.5 91.4±0.3 86.9±0.5 89.5±0.3 85.5
SK
DAN 86.0±0.5 81.5±0.3 82.0±0.4 92.0±0.3 92.0±0.4 90.5±0.2 87.3
|                                                          |     |     |     |     |     |     |     | error(Grettonetal.,2012b). |     |     | (2)DAN | alsoattainshigher |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | ------ | ----------------- | --- | --- |
| Table3.AccuracyonOffice-31datasetwithclassicunsupervised |     |     |     |     |     |     |     |                            |     |     |        | SK                |     |     |
accuracythanDDC,whichconfirmsthecapabilityofdeep
andsemi-supervisedadaptationprotocols(Saenkoetal.,2010).
|        |     |          |     |          |          |     |         | architecture | for distribution |                | adaptation. | The        | rationale | is   |
| ------ | --- | -------- | --- | -------- | -------- | --- | ------- | ------------ | ---------------- | -------------- | ----------- | ---------- | --------- | ---- |
| Method |     | A→W      |     | D→W      |          | W→D | Average |              |                  |                |             |            |           |      |
|        |     |          |     |          |          |     |         | similar      | to that of       | deep networks: |             | each layer | of deep   | net- |
| DDC    |     | 59.4±0.8 |     | 92.5±0.3 | 91.7±0.8 |     | 81.2    |              |                  |                |             |            |           |      |
workisintendedtoextractfeaturesatadifferentabstraction
|     |     | 66.0±0.4 |     | 93.5±0.2 | 95.3±0.3 |     | 84.9 |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | -------- | -------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
DAN
level,andhenceweneedtomatchthedistributionsateach
| DDC |     | 84.1±0.6 |     | 95.4±0.4 | 96.3±0.3 |     | 91.9 |               |                 |                |                |            |         |      |
| --- | --- | -------- | --- | -------- | -------- | --- | ---- | ------------- | --------------- | -------------- | -------------- | ---------- | ------- | ---- |
|     |     |          |     |          |          |     |      | task-specific | layer           | to consolidate | the            | adaptation | quality | at   |
| DAN |     | 85.7±0.3 |     | 97.2±0.2 | 96.4±0.2 |     | 93.1 |               |                 |                |                |            |         |      |
|     |     |          |     |          |          |     |      | all levels.   | The multi-layer |                | architectureis | one        | of the  | most |
criticalcontributorstotheefficacyofdeeplearning,andwe
believeitisalsoimportantforMMD-basedadaptation.The
| supervised |     | learning. | (3) | DDC, | a cross-domain |     | variant of |          |               |     |             |         |     |        |
| ---------- | --- | --------- | --- | ---- | -------------- | --- | ---------- | -------- | ------------- | --- | ----------- | ------- | --- | ------ |
|            |     |           |     |      |                |     |            | evidence | of comparable |     | performance | between | the | multi- |
CNNwithsingle-layeradaptationviasingle-kernelMMD,
|                                                      |     |     |     |     |     |     |     | layervariantDAN |     | andmulti-kernelvariantsDAN |     |     |     | and |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------------------------- | --- | --- | --- | --- |
| generallyoutperformsCNN,confirmingitseffectivenessin |     |     |     |     |     |     |     |                 |     | SK                         |     |     |     | 7   |
DAN showstheirequalimportancefordomainadaptation.
8
| learningtransferable |     |     | featuresusing |     | domain-adaptivedeep |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | ------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Asexpected,DANobtainsthebestperformancebyjointly
models.NotethatwhileDDCbasedonCaffeAlexNetwas
|     |     |     |     |     |     |     |     | exploringmulti-layeradaptationwith |     |     |     | multi-kernelMMD. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | ---------------- | --- | --- |
showntosignificantlyoutperformDeCAF(Donahueetal.,
|     |     |     |     |     |     |     |     | Anotherbenefit | of  | DAN | is that it | uses a linear-time |     | unbi- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | ---------- | ------------------ | --- | ----- |
2014)inwhichfine-tuningwasnotcarriedout,itdoesnot
asedestimateofthekernelembedding,whichmakesitan
| yield | a large | gain | over | Caffe | AlexNet | using | fine-tuning. |     |     |     |     |     |     |     |
| ----- | ------- | ---- | ---- | ----- | ------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
ordermoreefficientthanexistingmethodsTCAandDDC.
| This | shows | the | limitation | of  | single-layer |     | adaptation via |               |     |            |       |        |              |     |
| ---- | ----- | --- | ---------- | --- | ------------ | --- | -------------- | ------------- | --- | ---------- | ----- | ------ | ------------ | --- |
|      |       |     |            |     |              |     |                | ThoughTzenget |     | al. (2014) | speed | up DDC | by computing |     |
single-kernelMMD,whichcannotexplorethestrengthsof
theMMDwithineachmini-batchoftheSGD,thisleadsto
deepnetworksandmultiplekernelsfordomainadaptation.
abiasedestimateofMMDandloweradaptationaccuracy.
| To dive | deeper | into | DAN, | we  | present | the results | of three |     |     |     |     |     |     |     |
| ------- | ------ | ---- | ---- | --- | ------- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- |
variantsof DAN: (1) DAN 7 and DAN 8 achievebetter ac- 4.3.EmpiricalAnalysis
curacythanDDC,whichhighlightsthatmulti-kernelMMD
|               |        |            |     |             |      |               |         | Feature    | Visualization |         | To demonstrate | the       | transferabil- |     |
| ------------- | ------ | ---------- | --- | ----------- | ---- | ------------- | ------- | ---------- | ------------- | ------- | -------------- | --------- | ------------- | --- |
| can           | bridge | the domain |     | discrepancy | more | effectively   | than    |            |               |         |                |           |               |     |
|               |        |            |     |             |      |               |         | ity of the | DAN           | learned | features,      | we follow | Donahue       | et  |
| single-kernel |        | MMD.       | The | reason      | is   | that multiple | kernels |            |               |         |                |           |               |     |
al.(2014)andTzengetal.(2014)andplotinFigures2(a)–
| with | different | bandwidths |     | can | match | both | the low-order |     |     |     |     |     |     |     |
| ---- | --------- | ---------- | --- | --- | ----- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- |
momentsandhigh-ordermomentstominimizetheTypeII 2(b) and 2(c)–2(d) the t-SNE embeddings of the images

LearningTransferableFeatureswithDeepAdaptationNetworks
| 100 |     |     |     | 100 |     |     |   100 |     |     |   100 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ----- | --- | --- | --- |
| 50  |     |     |     | 50  |     |     | 50    |     |     | 50    |     |     |     |
| 0   |     |     |     | 0   |     |     | 0     |     |     | 0     |     |     |     |
| −50 |     |     |     | −50 |     |     | −50   |     |     | −50   |     |     |     |
−100  −100 −50 0 50 100 −100  −100 −50 0 50 100 −100  −100 −50 0 50 100 −100  −100 −50 0 50 100
(a) DDCFeaturesonSource (b) DDCFeaturesonTarget (c) DANFeaturesonSource (d) DANFeaturesonTarget
Figure2.Featurevisualization:t-SNEofDDCfeaturesonsource(a)andtarget(b);t-SNEofDANfeaturesonsource(c)andtarget(d).
2.2   stract deep featurescan be salient both for discriminating
|     | Raw | CNN DAN |     | 100 |     |     |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2.1
differentcategoriesanddifferentdomains,whichisconsis-
90
2 )%( ycaruccA egarevA tentwithGlorotetal.(2011). However,domainadaptation
ecnatsiD−A 1.9 80 may be deteriorated by the enlarged domain discrepancy
| 1.8 |     |     |     |     |     |     |                        |     |        |                           |                | dˆ  |        |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | ------ | ------------------------- | -------------- | --- | ------ |
|     |     |     |     |     |     |     | (Ben-Davidetal.,       |     | 2010). | It is                     | desirable that |     | on DAN |
| 1.7 |     |     |     | 70  |     |     |                        |     |        |                           |                | A   |        |
|     |     |     |     |     |     |     | featureissmallerthandˆ |     |        | onCNNfeature,whichguaran- |                |     |        |
| 1.6 |     |     |     |     |     |     |                        |     | A      |                           |                |     |        |
60
| 1.5 |     |     |     |     |       |       | teesmoretransferablefeatures. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | ----- | ----------------------------- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | A → W | C → W |                               |     |     |     |     |     |     |
| 1.4 |     |     |     | 50  |       |       |                               |     |     |     |     |     |     |
  A−>W C−>W 0.1   0.4 0.7 1 1.4 1.7 2 Parameter Sensitivity We investigate the effects of the
|     |                | Task |     |                  | λ   |     |           |             |                |       |                 |     |        |
| --- | -------------- | ---- | --- | ---------------- | --- | --- | --------- | ----------- | -------------- | ----- | --------------- | --- | ------ |
|     |                |      |     |                  |     |     | parameter | λ.          | Figure 3(b)    | gives | an illustration |     | of the |
|     | (a) A-Distance |      |     | (b) Accuracyvs.λ |     |     |           |             |                |       |                 |     |        |
|     |                |      |     |                  |     |     | variation | of transfer | classification |       | performance     |     | as λ ∈ |
{0.1,0.4,0.7,1,1.4,1.7,2}ontasksA→WandC→W.
Figure3.Empiricalanalysis:(a)A-DistanceofCNN&DANfea-
tures;(b)sensitivityofλ(dashedlinesshowbestbaselineresults). We canobservethattheDANaccuracyfirstincreasesand
thendecreasesasλvariesanddemonstratesabell-shaped
curve.Thisconfirmsthemotivationofjointlylearningdeep
intaskC→WwithDDCfeaturesandDANfeatures,re- featuresandadaptingdistributiondiscrepancy,sinceagood
trade-offbetweenthemcanenhancefeaturetransferability.
| spectively. | We  | makethefollowingobservations: |     |     |     | (1)With |     |     |     |     |     |     |     |
| ----------- | --- | ----------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
DDCfeatures,thetargetpointsarenotdiscriminatedvery
| well,whilewithDANfeatures,thepointsarediscriminated |         |          |               |     |                |     | 5. Conclusion |     |     |     |     |     |     |
| --------------------------------------------------- | ------- | -------- | ------------- | --- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
| much                                                | better. | (2) With | DDC features, |     | the categories | be- |               |     |     |     |     |     |     |
tween the source and the targetare notaligned verywell, In this paper, we have proposeda novelDeep Adaptation
Network(DAN)architecturetoenhancethetransferability
whilewithDANfeatures,thecategoriesarealignedmuch
better between domains. Both these observationscan ex- offeaturesfromtask-specificlayersoftheneuralnetwork.
Weconfirmthatwhilegeneralfeaturescangeneralizewell
plainthesuperiorperformanceofDANoverDDC:(1)im-
toanoveltask,specificfeaturestailoredtoanoriginaltask
| plies | that the | target points | are | more easily | discriminated |     |     |     |     |     |     |     |     |
| ----- | -------- | ------------- | --- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
with DAN features, and (2) implies that the target points cannotbridgethedomaindiscrepancyeffectively.Weshow
thatfeaturetransferabilitycanbeenhancedsubstantiallyby
| canbebetterdiscriminatedwiththesourceclassifier. |     |     |     |     |     | DAN |     |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
can learn more transferable features for effective domain mean-embedding matching of the multi-layer representa-
tionsacrossdomainsinareproducingkernelHilbertspace.
adaptation.
Anoptimalmulti-kernelselectionstrategyfurtherimproves
| A-Distance |     | AtheoreticalresultinBen-Davidetal.(2010) |     |     |     |     |                       |     |     |                |       |             |     |
| ---------- | --- | ---------------------------------------- | --- | --- | --- | --- | --------------------- | --- | --- | -------------- | ----- | ----------- | --- |
|            |     |                                          |     |     |     |     | the embeddingmatching |     |     | effectiveness, | while | an unbiased |     |
suggests A-distance as a measure of domain discrepancy. estimateofthemeanembeddingnaturallyleadstoalinear-
| As computing |     | the exact | A-distance | is  | intractable, | an ap- |     |     |     |     |     |     |     |
| ------------ | --- | --------- | ---------- | --- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- |
timealgorithmthatisverydesirablefordeeplearningfrom
| proximatedistanceisdefinedasdˆ |     |     |     | =   | 2(1−2ǫ),whereǫ |     |                      |     |                                  |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | -------------- | --- | -------------------- | --- | -------------------------------- | --- | --- | --- | --- |
|                                |     |     |     | A   |                |     | large-scaledatasets. |     | Anextensiveempiricalevaluationon |     |     |     |     |
is the generalizationerror of a two-sample classifier (ker- standard domain adaptationbenchmarksdemonstratesthe
| nel SVM | in  | our case) | trained | on the | binary | problem to |     |     |     |     |     |     |     |
| ------- | --- | --------- | ------- | ------ | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
efficacyoftheproposedmodelagainstpreviousmethods.
| distinguish | input  | samples       | between | the         | source | and target |         |          |            |      |           |          |       |
| ----------- | ------ | ------------- | ------- | ----------- | ------ | ---------- | ------- | -------- | ---------- | ---- | --------- | -------- | ----- |
|             |        |               |         | dˆ          |        |            | As deep | features | transition | from | generalto | specific | along |
| domains.    | Figure | 3(a) displays |         | on transfer |        | tasks A →  |         |          |            |      |           |          |       |
A
W and C → W using Raw features, CNN features, and thenetwork,itisinterestingtostudytheprincipledwayof
decidingtheboundaryofgeneralityandspecificity,andthe
| DAN    | features, | respectively. | It       | reveals | a surprising | obser- |             |                 |     |            |        |               |     |
| ------ | --------- | ------------- | -------- | ------- | ------------ | ------ | ----------- | --------------- | --- | ---------- | ------ | ------------- | --- |
|        |           |               |          |         |              |        | application | of distribution |     | adaptation | to the | convolutional |     |
| vation | that the  | dˆ on         | both CNN | and     | DAN features | are    |             |                 |     |            |        |               |     |
A
largerthan the dˆ on Raw features. Thisimplies thatab- layersofCNNtofurtherenhancethefeaturetransferability.
A

LearningTransferableFeatureswithDeepAdaptationNetworks
Acknowledgments Hinton, G.E., Srivastava, N., Krizhevsky, A., Sutskever, I., and
|     |     |     |     |     |     |     |     | Salakhutdinov, |     | R. R. | Improving | neural | networks | by pre- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | --------- | ------ | -------- | ------- |
ThisworkwassupportedbytheNationalScienceFundsfor venting co-adaptation of feature detectors. Technical report,
DistinguishedYoungScholars(No. 613250154),National arXiv:1207.0580,2012.
ScienceandTechnologySupportingProgramProject(No. Hoffman, J., Guadarrama, S., Tzeng, E., Hu, R., Donahue, J.,
2015BAH14F02),andTsinghuaTNListFundforBigData Girshick, R., Darrell,T., andSaenko, K. LSDA:Largescale
ScienceandTechnology. detectionthroughadaptation. InNIPS,2014.
|     |     |     |     |     |     |     |     | Jia, Y., Shelhamer, |     | E., Donahue, |     | J., Karayev, | S., Long, | J., Gir- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------------ | --- | ------------ | --------- | -------- |
References shick,R.,Guadarrama,S.,andDarrell,T.Caffe:Convolutional
|     |     |     |     |     |     |     |     | architectureforfastfeatureembedding. |     |     |     | InACMMultimedia, |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | ---------------- | --- | --- |
Ajakan,H.,Germain,P.,Larochelle,H.,Laviolette,F.,andMarc-
2014.
| hand,M. | Domain-adversarialneuralnetworks. |     |     |     |     | InNIPS2014 |     |     |     |     |     |     |     |     |
| ------- | --------------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
WorkshoponTransferandMulti-tasklearning: TheoryMeets Krizhevsky, A., Sutskever, I., andHinton, G.E. Imagenet clas-
Practice,2014. sificationwithdeep convolutional neural networks. InNIPS,
2012.
| Baktashmotlagh, |                                             | M., Harandi, | M.  | T., | Lovell, | B. C., and | Salz- |                  |       |            |              |             |        |             |
| --------------- | ------------------------------------------- | ------------ | --- | --- | ------- | ---------- | ----- | ---------------- | ----- | ---------- | ------------ | ----------- | ------ | ----------- |
|                 |                                             |              |     |     |         |            |       | Long, M.,        | Wang, | J., Ding,  | G., Sun,     | J., and     | Yu, P. | S. Transfer |
| mann,M.         | Unsuperviseddomainadaptationbydomaininvari- |              |     |     |         |            |       |                  |       |            |              |             |        |             |
|                 |                                             |              |     |     |         |            |       | feature learning |       | with joint | distribution | adaptation. |        | In ICCV,    |
| antprojection.  |                                             | InICCV,2013. |     |     |         |            |       |                  |       |            |              |             |        |             |
2013.
| Ben-David,S.,Blitzer,J.,Crammer,K.,andPereira,F. |     |     |     |     |            |     | Analysis |                                        |     |     |     |            |               |     |
| ------------------------------------------------ | --- | --- | --- | --- | ---------- | --- | -------- | -------------------------------------- | --- | --- | --- | ---------- | ------------- | --- |
|                                                  |     |     |     |     |            |     |          | Mansour,Y.,Mohri,M.,andRostamizadeh,A. |     |     |     |            | Domainadapta- |     |
| ofrepresentationsfordomainadaptation.            |     |     |     |     | NIPS,2007. |     |          |                                        |     |     |     |            |               |     |
|                                                  |     |     |     |     |            |     |          | tion:Learningboundsandalgorithms.      |     |     |     | COLT,2009. |               |     |
Ben-David,S.,Blitzer,J.,Crammer,K.,Kulesza,A.,Pereira,F.,
Ngiam,J.,Khosla,A.,Kim,M.,Nam,J.,Lee,H.,andNg,A.Y.
| and Vaughan, |     | J. W. | A theory | of learning | from | different | do- |                         |     |     |              |     |     |     |
| ------------ | --- | ----- | -------- | ----------- | ---- | --------- | --- | ----------------------- | --- | --- | ------------ | --- | --- | --- |
|              |     |       |          |             |      |           |     | Multimodaldeeplearning. |     |     | InICML,2011. |     |     |     |
mains. MachineLearning,79(1-2):151–175,2010.
Pan,S.J.andYang,Q.Asurveyontransferlearning.IEEETrans-
| Bengio, Y.,Courville,A.,andVincent,P. |        |         |               |     | Representationlearn- |              |     |         |              |     |          |              |     |              |
| ------------------------------------- | ------ | ------- | ------------- | --- | -------------------- | ------------ | --- | ------- | ------------ | --- | -------- | ------------ | --- | ------------ |
|                                       |        |         |               |     |                      |              |     | actions | on Knowledge |     | and Data | Engineering, |     | 22(10):1345– |
| ing: A                                | review | and new | perspectives. |     | IEEE                 | Transactions | on  |         |              |     |          |              |     |              |
1359,2010.
PatternAnalysisandMachineIntelligence,35(8):1798–1828,
| 2013. |     |     |     |     |     |     |     | Pan,S.J.,Tsang,I.W.,Kwok,J.T.,andYang,Q. |     |     |     |                    | Domainadap- |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | ------------------ | ----------- | --- |
|       |     |     |     |     |     |     |     | tationviatransfercomponentanalysis.      |     |     |     | IEEETransactionson |             |     |
Chen, M., Xu,Z.,Weinberger, K.Q.,andSha,F. Marginalized NeuralNetworksandLearningSystems,22(2):199–210,2011.
denoisingautoencodersfordomainadaptation.InICML,2012.
|     |     |     |     |     |     |     |     | Russakovsky, | O.,Deng, | J.,Su,H.,Krause,J.,Satheesh,S.,Ma, |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | ---------------------------------- | --- | --- | --- | --- |
Donahue,J.,Jia,Y.,Vinyals,O.,Hoffman,J.,Zhang,N.,Tzeng,
|                                  |     |                                        |     |              |     |     |     | S.,Huang,          | Z.,Karpathy,A.,Khosla,A.,Bernstein,M.,Berg, |                                       |                                  |     |     |     |
| -------------------------------- | --- | -------------------------------------- | --- | ------------ | --- | --- | --- | ------------------ | ------------------------------------------- | ------------------------------------- | -------------------------------- | --- | --- | --- |
| E.,andDarrell,T.                 |     | Decaf:Adeepconvolutionalactivationfea- |     |              |     |     |     |                    |                                             |                                       |                                  |     |     |     |
|                                  |     |                                        |     |              |     |     |     | A.C.,andFei-Fei,L. |                                             |                                       | ImageNetLargeScaleVisualRecogni- |     |     |     |
| tureforgenericvisualrecognition. |     |                                        |     | InICML,2014. |     |     |     |                    |                                             |                                       |                                  |     |     |     |
|                                  |     |                                        |     |              |     |     |     | tionChallenge.     |                                             | Technicalreport,arXiv:1409.0575,2014. |                                  |     |     |     |
Ge,L.,Gao,J.,Li,X.,andZhang,A. Multi-sourcedeeplearning Saenko,K.,Kulis,B.,Fritz,M.,andDarrell,T. Adaptingvisual
forinformationtrustworthinessestimation. InKDD,2013. categorymodelstonewdomains. InECCV,2010.
|          |             |     |         |        |     |        |       | Sejdinovic, | D., Sriperumbudur, |     |     | B., Gretton, | A., and | Fukumizu, |
| -------- | ----------- | --- | ------- | ------ | --- | ------ | ----- | ----------- | ------------------ | --- | --- | ------------ | ------- | --------- |
| Ghifary, | M., Kleijn, | W.  | B., and | Zhang, | M.  | Domain | adap- |             |                    |     |     |              |         |           |
tiveneuralnetworksforobjectrecognition. Technicalreport, K. Equivalenceofdistance-basedandrkhs-basedstatisticsin
arXiv:1409.6041,2014. hypothesistesting. TheAnnalsofStatistics,41(5):2263–2291,
2013.
| Glorot, X., | Bordes, | A., | and Bengio, | Y.  | Domain | adaptation | for |     |     |     |     |     |     |     |
| ----------- | ------- | --- | ----------- | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Sriperumbudur,B.K.,Fukumizu,K.,Gretton,A.,Lanckriet,G.,
large-scalesentimentclassification:Adeeplearningapproach.
|     |     |     |     |     |     |     |     | and Scho¨lkopf, |     | B. Kernel | choice | and classifiability |     | for rkhs |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | ------ | ------------------- | --- | -------- |
InICML,2011.
|     |     |     |     |     |     |     |     | embeddingsofprobabilitydistributions. |     |     |     | InNIPS,2009. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | ------------ | --- | --- |
Gong,B.,Shi,Y.,Sha,F.,andGrauman,K.Geodesicflowkernel
|                                  |     |     |     |     |              |     |     | Torralba,A.andEfros,A.A. |     |     | Unbiasedlookatdatasetbias. |     |     | In  |
| -------------------------------- | --- | --- | --- | --- | ------------ | --- | --- | ------------------------ | --- | --- | -------------------------- | --- | --- | --- |
| forunsuperviseddomainadaptation. |     |     |     |     | InCVPR,2012. |     |     |                          |     |     |                            |     |     |     |
CVPR,2011.
| Gong, B.,                             | Grauman,         | K., | and Sha, | F. Connecting |                  | the dots | with |             |            |            |            |             |         |             |
| ------------------------------------- | ---------------- | --- | -------- | ------------- | ---------------- | -------- | ---- | ----------- | ---------- | ---------- | ---------- | ----------- | ------- | ----------- |
|                                       |                  |     |          |               |                  |          |      | Tzeng, E.,  | Hoffman,   | J., Zhang, |            | N., Saenko, | K., and | Darrell, T. |
| landmarks:                            | Discriminatively |     |          | learning      | domain-invariant |          | fea- |             |            |            |            |             |         |             |
|                                       |                  |     |          |               |                  |          |      | Deep domain | confusion: |            | Maximizing | for         | domain  | invariance. |
| turesforunsuperviseddomainadaptation. |                  |     |          |               | InICML,2013.     |          |      |             |            |            |            |             |         |             |
Technicalreport,arXiv:1412.3474,2014.
Gretton,A.,Borgwardt,K.,Rasch,M.,Scho¨lkopf,B.,andSmola, Wang,X.andSchneider,J. Flexibletransferlearningundersup-
A. A kernel two-sample test. Journal of Machine Learning portandmodelshift. InNIPS,2014.
Research,13:723–773,March2012a.
|          |                   |     |                |     |     |             |     | Weston,J.,Rattle,F.,andCollobert,R. |     |     |              | Deeplearningviasemi- |     |     |
| -------- | ----------------- | --- | -------------- | --- | --- | ----------- | --- | ----------------------------------- | --- | --- | ------------ | -------------------- | --- | --- |
| Gretton, | A.,Sriperumbudur, |     | B.,Sejdinovic, |     | D., | Strathmann, | H., |                                     |     |     |              |                      |     |     |
|          |                   |     |                |     |     |             |     | supervisedembedding.                |     |     | InICML,2008. |                      |     |     |
Balakrishnan,S.,Pontil,M.,andFukumizu,K.Optimalkernel
choiceforlarge-scaletwo-sampletests. InNIPS,2012b. Yosinski,J.,Clune,J.,Bengio,Y.,andLipson,H. Howtransfer-
|     |     |     |     |     |     |     |     | ablearefeaturesindeepneuralnetworks? |     |     |     |     | InNIPS,2014. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | ------------ | --- |
Griffin,G.,Holub,A.,andPerona,P.Caltech-256objectcategory
|          |           |         |                     |     |     |                |     | Zhang, K.,                                | Scho¨lkopf, | B., | Muandet, | K., andWang, |              | Z. Domain |
| -------- | --------- | ------- | ------------------- | --- | --- | -------------- | --- | ----------------------------------------- | ----------- | --- | -------- | ------------ | ------------ | --------- |
| dataset. | Technical | report, | CaliforniaInstitute |     |     | of Technology, |     |                                           |             |     |          |              |              |           |
|          |           |         |                     |     |     |                |     | adaptationundertargetandconditionalshift. |             |     |          |              | InICML,2013. |           |
2007.