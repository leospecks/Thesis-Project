IEEETRANSACTIONSONKNOWLEDGEANDDATAENGINEERING, VOL.22, NO.10, OCTOBER2010 1345
A Survey on Transfer Learning
Sinno Jialin Pan and Qiang Yang, Fellow, IEEE
Abstract—Amajorassumptioninmanymachinelearninganddataminingalgorithmsisthatthetrainingandfuturedatamustbeinthe
samefeaturespaceandhavethesamedistribution.However,inmanyreal-worldapplications,thisassumptionmaynothold.For
example,wesometimeshaveaclassificationtaskinonedomainofinterest,butweonlyhavesufficienttrainingdatainanotherdomain
ofinterest,wherethelatterdatamaybeinadifferentfeaturespaceorfollowadifferentdatadistribution.Insuchcases,knowledge
transfer,ifdonesuccessfully,wouldgreatlyimprovetheperformanceoflearningbyavoidingmuchexpensivedata-labelingefforts.In
recentyears,transferlearninghasemergedasanewlearningframeworktoaddressthisproblem.Thissurveyfocusesoncategorizing
andreviewingthecurrentprogressontransferlearningforclassification,regression,andclusteringproblems.Inthissurvey,we
discusstherelationshipbetweentransferlearningandotherrelatedmachinelearningtechniquessuchasdomainadaptation,multitask
learningandsampleselectionbias,aswellascovariateshift.Wealsoexploresomepotentialfutureissuesintransferlearning
research.
IndexTerms—Transferlearning,survey,machinelearning,datamining.
Ç
1 INTRODUCTION
DATA mining and machine learning technologies have The need for transfer learning may arise when the data
already achieved significant success in many knowl- can be easily outdated. In this case, the labeled data
edge engineering areas including classification, regression, obtained in one time period may not follow the same
and clustering (e.g., [1], [2]). However, many machine distribution in a later time period. For example, in indoor
learningmethodsworkwellonlyunderacommonassump- WiFi localization problems, which aims to detect a user’s
tion: the training and test data are drawn from the same currentlocation basedonpreviouslycollectedWiFidata,it
featurespaceandthesamedistribution.Whenthedistribu-
is very expensive to calibrate WiFi data for building
tionchanges,moststatisticalmodelsneedtoberebuiltfrom
localization models in a large-scale environment, because
scratch using newly collected training data. In many real-
auserneedstolabelalargecollectionofWiFisignaldataat
worldapplications,itisexpensiveorimpossibletorecollect
each location. However, the WiFi signal-strength values
theneededtrainingdataandrebuildthemodels.Itwouldbe
maybeafunctionoftime,device,orotherdynamicfactors.
nice to reduce the need and effort to recollect the training
A model trained in one time period or on one device may
data. In such cases, knowledge transfer or transfer learning
cause the performance for location estimation in another
betweentaskdomainswouldbedesirable.
time period or on another device to be reduced. To reduce
Many examplesinknowledgeengineeringcanbefound
the recalibration effort, we might wish to adapt the
where transfer learning can truly be beneficial. One
localization model trained in one time period (the source
example is Web-document classification [3], [4], [5], where
domain) for a new time period (the target domain), or to
our goal is to classify a given Web document into several
adaptthelocalizationmodeltrainedonamobiledevice(the
predefined categories. As an example, in the area of Web-
source domain) for a new mobile device (the target
documentclassification(see,e.g.,[6]),thelabeledexamples
domain), as done in [7].
may be the university webpages that are associated with
As a third example, consider the problem of sentiment
category information obtained through previous manual-
classification,whereourtaskistoautomaticallyclassifythe
labeling efforts.Foraclassificationtaskonanewlycreated
reviews on a product, such as a brand of camera, into
website where the data features or data distributions may positiveandnegative views.Forthis classification task,we
bedifferent,theremaybealackoflabeledtrainingdata.As need to first collect many reviews of the product and
a result, we may not beable to directly apply the webpage annotate them. We would then train a classifier on the
classifiers learned on the university website to the new reviewswiththeircorrespondinglabels.Sincethedistribu-
website. In such cases, it would be helpful if we could tionofreviewdataamongdifferenttypesofproductscanbe
transfer the classification knowledge into the new domain. verydifferent,tomaintaingoodclassificationperformance,
weneedtocollectalargeamountoflabeleddatainorderto
train the review-classification models for each product.
. The authors are with the Department of Computer Science and
However,thisdata-labelingprocesscanbeveryexpensiveto
Engineering, Hong Kong University of Science and Technology,
do. To reduce the effort for annotating reviews for various
Clearwater Bay, Kowloon, Hong Kong.
E-mail: {sinnopan, qyang}@cse.ust.hk. products,wemaywanttoadaptaclassificationmodelthatis
Manuscript received 13 Nov. 2008; revised 29 May 2009; accepted 13 July trainedonsomeproductstohelplearnclassificationmodels
2009;publishedonline12Oct.2009. forsomeotherproducts.Insuchcases,transferlearningcan
RecommendedforacceptancebyC.Clifton. saveasignificantamountoflabelingeffort[8].
For information on obtaining reprints of this article, please send e-mail to:
Inthissurveypaper,wegiveacomprehensiveoverview
tkde@computer.org,andreferenceIEEECSLogNumberTKDE-2008-11-0600.
DigitalObjectIdentifierno.10.1109/TKDE.2009.191. oftransferlearningforclassification,regression,andcluster-
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 20:44:14 UTC from IEEE Xplore. Restrictions apply.
1041-4347/10/$26.00(cid:2)2010IEEE PublishedbytheIEEEComputerSociety

1346 IEEETRANSACTIONSONKNOWLEDGEANDDATAENGINEERING, VOL.22, NO.10, OCTOBER2010
ing developed in machine learning and data mining areas.
Therehasbeenalargeamountofworkontransferlearning
forreinforcementlearninginthemachinelearningliterature
(e.g., [9], [10]). However, in this paper, we only focus on
transferlearningforclassification,regression,andclustering
problemsthatarerelatedmorecloselytodataminingtasks.
Bydoingthesurvey,wehopetoprovideausefulresourcefor
thedataminingandmachinelearningcommunity.
Therestofthesurveyisorganizedasfollows:Inthenext
four sections, we first give a general overview and define
somenotationswewilluselater.We,then,brieflysurveythe
Fig. 1. Different learning processes between (a) traditional machine
history of transfer learning, give a unified definition of
learningand(b)transferlearning.
transferlearningandcategorizetransferlearningintothree
different settings (given in Table 2 and Fig. 2). For each transfer, multitask learning, knowledge consolidation,
setting,wereviewdifferentapproaches,giveninTable3in context-sensitivelearning,knowledge-basedinductivebias,
detail. After that, in Section 6, we review some current
metalearning, and incremental/cumulative learning [20].
researchonthetopicof“negativetransfer,”whichhappens
Among these, a closely related learning technique to
when knowledge transfer has a negative impact on target
transfer learning is the multitask learning framework [21],
learning. In Section 7, we introduce some successful
which tries to learn multiple tasks simultaneously even
applications of transfer learning and list some published
when they are different. A typical approach for multitask
datasetsandsoftwaretoolkitsfortransferlearningresearch.
learningistouncoverthecommon(latent)featuresthatcan
Finally, we conclude the paper with a discussion of future
benefit each individual task.
worksinSection8.
In 2005, the Broad Agency Announcement (BAA) 05-29
ofDefenseAdvancedResearchProjectsAgency(DARPA)’s
2 OVERVIEW Information Processing Technology Office (IPTO)2 gave a
new mission of transfer learning: the ability of a system to
2.1 A Brief History of Transfer Learning
recognize and apply knowledge and skills learned in
Traditional data mining and machine learning algorithms
previous tasks to novel tasks. In this definition, transfer
makepredictionsonthefuturedatausingstatisticalmodels
learning aims to extract the knowledge from one or more
thataretrainedonpreviouslycollectedlabeledorunlabeled
source tasks and applies the knowledge to a target task. In
training data [11], [12], [13]. Semisupervised classification
contrasttomultitasklearning,ratherthanlearningallofthe
[14], [15], [16], [17] addresses the problem that the labeled
source and target tasks simultaneously, transfer learning
datamaybetoofewtobuildagoodclassifier,bymakinguse
caresmostaboutthetargettask.Therolesofthesourceand
ofalargeamountofunlabeleddataandasmallamountof
target tasks are no longer symmetric in transfer learning.
labeled data. Variations of supervised and semisupervised
Fig.1showsthedifferencebetweenthelearningprocesses
learning for imperfect data sets have been studied; for
of traditional and transfer learning techniques. As we can
example,ZhuandWu[18]havestudiedhowtodealwiththe
see,traditionalmachinelearningtechniquestrytolearneach
noisy class-label problems. Yang et al. considered cost-
task from scratch, while transfer learning techniques try to
sensitivelearning[19]whenadditionaltestscanbemadeto
transfertheknowledgefromsomeprevioustaskstoatarget
futuresamples.Nevertheless,mostofthemassumethatthe
taskwhenthelatterhasfewerhigh-qualitytrainingdata.
distributionsofthelabeledandunlabeleddataarethesame.
Today, transfer learning methods appear in several top
Transferlearning,incontrast,allowsthedomains,tasks,and
venues, most notably in data mining (ACM KDD, IEEE
distributionsusedintrainingandtestingtobedifferent.In
ICDM, and PKDD, for example), machine learning (ICML,
the real world, we observe many examples of transfer
NIPS, ECML, AAAI, and IJCAI, for example) and applica-
learning. For example, we may find that learning to
tions of machine learning and data mining (ACM SIGIR,
recognize apples might help to recognize pears. Similarly,
WWW, and ACL, for example).3 Before we give different
learning to play the electronic organ may help facilitate
categorizations of transfer learning, we first describe the
learningthepiano.ThestudyofTransferlearningismotivated
notations used in this paper.
by the fact that people can intelligently apply knowledge
learned previously to solve new problems faster or with 2.2 Notations and Definitions
better solutions. The fundamental motivation for Transfer
Inthissection,weintroducesomenotationsanddefinitions
learninginthefieldofmachinelearningwasdiscussedina
that are used in this survey. First of all, we give the
NIPS-95workshopon“LearningtoLearn,”1whichfocused
definitionsofa“domain”anda“task,”respectively.
ontheneedforlifelongmachinelearningmethodsthatretain
Inthissurvey,adomainDconsistsoftwocomponents:a
andreusepreviouslylearnedknowledge.
featurespaceXandamarginalprobabilitydistributionPðXÞ,
Research on transfer learning has attracted more and
more attention since 1995 in different names: learning to
whereX¼fx
1
;...;x
n
g2X.Forexample,ifourlearningtask
learn, life-long learning, knowledge transfer, inductive
2.http://www.darpa.mil/ipto/programs/tl/tl.asp.
3. We summarize a list of conferences and workshops where transfer
1. http://socrates.acadiau.ca/courses/comp/dsilver/NIPS95_LTL/ learning papers appear in these few years in the following webpage for
transfer.workshop.1995.html. reference,http://www.cse.ust.hk/~sinnopan/conferenceTL.htm.
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 20:44:14 UTC from IEEE Xplore. Restrictions apply.

| PANANDYANG: | ASURVEYONTRANSFERLEARNING |     |     |     |     |     |     |     |     |     |     |     |     |     | 1347 |
| ----------- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
TABLE1
Relationshipbetween TraditionalMachineLearning and VariousTransfer Learning Settings
isdocumentclassification,andeachtermistakenasabinary probabilitydistributionsbetweendomaindataaredifferent;
feature,thenXisthespaceofalltermvectors,x istheithterm PðX Þ6¼PðX Þ, X 2X X 2X
|     |     |     |     |     |     | i   |     | i.e., |     | S   | T where | Si  | S and | Ti  | T. As an |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ------- | --- | ----- | --- | -------- |
vector corresponding to some documents, and X is a example, in our document classification example, case 1
particular learning sample. In general, if two domains are corresponds to when the two sets of documents are
different, then they may have different feature spaces or describedindifferentlanguages,andcase2maycorrespond
differentmarginalprobabilitydistributions. to when the source domain documents and the target-
Given a specific domain, D¼fX;PðXÞg, a task consists domaindocumentsfocusondifferenttopics.
of two components: a label space Y and an objective Given specific domains D and D T, when the learning
S
| predictivefunctionfð(cid:2)Þ(denotedbyT |     |     |     |     | ¼fY;fð(cid:2)Þg),whichis |     |     |       | T   | T     |                  |     |      |        |              |
| --------------------------------------- | --- | --- | --- | --- | ------------------------ | --- | --- | ----- | --- | ----- | ---------------- | --- | ---- | ------ | ------------ |
|                                         |     |     |     |     |                          |     |     | tasks |     | S and | T are different, |     | then | either | 1) the label |
not observed but can be learned from the training data, spaces between the domains are different, i.e., Y S 6¼Y T , or
whichconsistofpairsfx ;y g,wherex 2Xandy 2Y.The 2) the conditional probability distributions between the
|     |     |     | i i |     | i   | i   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
functionfð(cid:2)Þcanbeusedtopredictthecorrespondinglabel, domains are different; i.e., PðY jX Þ6¼PðY jX Þ, where
|     |     |     |     |     |     |     |     |     |     |       |      |        | S S      | T              | T   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---- | ------ | -------- | -------------- | --- |
|     |     |     |     |     |     |     |     | Y   | 2Y  | and Y | 2Y . | In our | document | classification |     |
fðxÞ, of a new instance x. From a probabilistic viewpoint, Si S Ti T
fðxÞcanbewrittenasPðyjxÞ.Inourdocumentclassification example, case 1 corresponds to the situation where source
example,Y isthesetofalllabels,whichisTrue,Falsefora domain has binary document classes, whereas the target
|                       |     |         |         |               |          |          |          | domain      |     | has 10 classes | to        | classify | the documents |        | to. Case 2 |
| --------------------- | --- | ------- | ------- | ------------- | -------- | -------- | -------- | ----------- | --- | -------------- | --------- | -------- | ------------- | ------ | ---------- |
| binary classification |     | task,   | and     | y i is “True” | or       | “False.” |          |             |     |                |           |          |               |        |            |
|                       |     |         |         |               |          |          |          | corresponds |     | to the         | situation | where    | the           | source | and target |
| For simplicity,       |     | in this | survey, | we only       | consider |          | the case |             |     |                |           |          |               |        |            |
wherethereisonesourcedomainD S,andonetargetdomain, documents are very unbalanced in terms of the user-
|     |     |     |     |     |     |     |     | defined |     | classes. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | -------- | --- | --- | --- | --- | --- |
D T,asthisisbyfarthemostpopularoftheresearchworksin
Inaddition,whenthereexistssomerelationship,explicit
theliterature.Morespecifically,wedenotethesourcedomain
orimplicit,betweenthefeaturespacesofthetwodomains,
| data as D | ¼fðx | ;y Þ;...;ðx |     | ;y  | Þg, where | x   | 2X  | is  |     |     |     |     |     |     |     |
| --------- | ---- | ----------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
S S1 S1 SnS SnS Si S we say that the source and target domains are related.
y 2Y
| the data | instance | and | Si  | S is the | corresponding |     | class |     |     |     |     |     |     |     |     |
| -------- | -------- | --- | --- | -------- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
label.Inourdocumentclassificationexample,D Scanbeaset 2.3 A Categorization of
of term vectors together with their associated true or false Transfer Learning Techniques
classlabels.Similarly,wedenotethetarget-domaindataas
|     |     |     |     |     |     |     |     | In  | transfer | learning, | we  | have | the following |     | three main |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- | ---- | ------------- | --- | ---------- |
D T ¼fðx T1 ;y T1 Þ;...;ðx TnT ;y TnT Þg, where the input x Ti is in research issues: 1) what to transfer, 2) how to transfer, and
| X andy             | 2Y   | isthecorrespondingoutput.Inmostcases, |     |     |     |     |     |     |                                               |              |     |     |     |     |     |
| ------------------ | ---- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | ------------ | --- | --- | --- | --- | --- |
| T                  | Ti T |                                       |     |     |     |     |     | 3)  | when                                          | to transfer. |     |     |     |     |     |
| 0(cid:3)n (cid:4)n | S.   |                                       |     |     |     |     |     |     |                                               |              |     |     |     |     |     |
| T                  |      |                                       |     |     |     |     |     |     | “Whattotransfer”askswhichpartofknowledgecanbe |              |     |     |     |     |     |
We now give a unified definition of transfer learning. transferred across domains or tasks. Some knowledge is
|            |             |     |            |       |                |     |     | specific |     | for individual | domains |     | or tasks, | and some | knowl- |
| ---------- | ----------- | --- | ---------- | ----- | -------------- | --- | --- | -------- | --- | -------------- | ------- | --- | --------- | -------- | ------ |
| Definition | 1 (Transfer |     | Learning). | Given | a sourcedomain |     | D   | S        |     |                |         |     |           |          |        |
and learning task T , a target domain D and learning task edgemaybecommonbetweendifferentdomainssuchthat
|     |     | S   |     |     | T   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
T ,transferlearningaimstohelpimprovethelearningofthe theymayhelpimproveperformanceforthetargetdomainor
T
task.Afterdiscoveringwhichknowledgecanbetransferred,
| targetpredictivefunctionf |           |     | T ð(cid:2)ÞinD | T        | usingtheknowledgein |     |     |          |     |            |      |       |           |     |              |
| ------------------------- | --------- | --- | -------------- | -------- | ------------------- | --- | --- | -------- | --- | ---------- | ---- | ----- | --------- | --- | ------------ |
|                           |           |     |                |          |                     |     |     | learning |     | algorithms | need | to be | developed | to  | transfer the |
| D and                     | T , where | D   | 6¼D ,          | or T 6¼T | .                   |     |     |          |     |            |      |       |           |     |              |
S S S T S T knowledge,whichcorrespondstothe“howtotransfer”issue.
Intheabovedefinition,adomainisapairD¼fX;PðXÞg. “Whentotransfer”asksinwhichsituations,transferring
|                    |                                            |       |                      |     |     |     |          | skills       | should | be       | done.       | Likewise, | we        | are interested | in     |
| ------------------ | ------------------------------------------ | ----- | -------------------- | --- | --- | --- | -------- | ------------ | ------ | -------- | ----------- | --------- | --------- | -------------- | ------ |
| Thus,theconditionD |                                            | S 6¼D | T impliesthateitherX |     |     | S   | 6¼X T or |              |        |          |             |           |           |                |        |
|                    |                                            |       |                      |     |     |     |          | knowing      |        | in which | situations, |           | knowledge | should         | not be |
| P ðXÞ6¼P           | ðXÞ.Forexample,inourdocumentclassification |       |                      |     |     |     |          |              |        |          |             |           |           |                |        |
| S                  | T                                          |       |                      |     |     |     |          | transferred. |        | In some  | situations, |           | when      | the source     | domain |
example,thismeansthatbetweenasourcedocumentsetand
andtargetdomainarenotrelatedtoeachother,brute-force
atargetdocumentset,eitherthetermfeaturesaredifferent
|     |     |     |     |     |     |     |     | transfer |     | may be | unsuccessful. |     | In the | worst case, | it may |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------ | ------------- | --- | ------ | ----------- | ------ |
betweenthetwosets(e.g.,theyusedifferentlanguages),or
|     |     |     |     |     |     |     |     | even | hurt | the | performance | of  | learning | in  | the target |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- | ----------- | --- | -------- | --- | ---------- |
theirmarginaldistributionsaredifferent.
|     |     |     |     |     |     |     |     | domain, |     | a situation | which | is often | referred | to  | as negative |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----------- | ----- | -------- | -------- | --- | ----------- |
Similarly, a task is defined as a pair T ¼fY;PðYjXÞg. transfer. Most current work on transfer learning focuses on
| Thus,theconditionT |     | 6¼T | impliesthateitherY |     |     |     | 6¼Y or |     |     |     |     |     |     |     |     |
| ------------------ | --- | --- | ------------------ | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
S T S T “What to transfer” and “How to transfer,” by implicitly
| PðY jX Þ6¼PðY |     | jX Þ.Whenthetargetandsourcedomains |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
S S T T assuming that the source and target domains be related to
arethesame,i.e.,D S ¼D T,andtheirlearningtasksarethe each other. However, how to avoid negative transfer is an
same, i.e., T S ¼T T, the learning problem becomes a important open issue that is attracting more and more
traditional machine learning problem. When the domains attention in the future.
| are different, | then | either | 1) the | feature | spaces | between | the |     |     |     |     |     |     |     |     |
| -------------- | ---- | ------ | ------ | ------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Basedonthedefinitionoftransferlearning,wesummarize
domainsaredifferent,i.e.,X S 6¼X T,or2)thefeaturespaces the relationship between traditional machine learning and
between the domains are the same but the marginal various transfer learning settings in Table 1, where we
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 20:44:14 UTC from IEEE Xplore.  Restrictions apply.

1348 IEEETRANSACTIONSONKNOWLEDGEANDDATAENGINEERING, VOL.22, NO.10, OCTOBER2010
TABLE2
Different Settings ofTransfer Learning
categorizetransferlearningunderthreesubsettings,inductive distributions of the input data are different,
transfer learning, transductive transfer learning, and unsuper- PðX
S
Þ6¼PðX
T
Þ.
visedtransferlearning,basedondifferentsituationsbetween The latter case of the transductive transfer
thesourceandtargetdomainsandtasks. learning setting is related to domain adaptation
for knowledge transfer in text classification [23]
1. Intheinductivetransferlearningsetting,thetargettask
and sample selection bias [24] or covariate shift
isdifferentfromthesourcetask,nomatterwhenthe
[25],whoseassumptionsaresimilar.
sourceandtargetdomainsarethesameornot.
3. Finally, in the unsupervised transfer learning setting,
In this case, some labeled data in the target
similartoinductivetransferlearningsetting,thetarget
domainarerequiredtoinduceanobjectivepredictive
task is different from but related to the source task.
modelf
T
ð(cid:2)Þforuseinthetargetdomain.Inaddition,
However, the unsupervised transfer learning focus on
according to different situations of labeled and
solving unsupervised learning tasks in the target
unlabeleddatainthesourcedomain,wecanfurther
domain,suchasclustering,dimensionalityreduction,
categorize the inductive transfer learning setting into
anddensityestimation[26],[27].Inthiscase,thereare
two cases:
no labeled data available in both source and target
a. A lot of labeled data in the source domain are domainsintraining.
available. In this case, the inductive transfer The relationship between the different settings of
learningsettingissimilartothemultitasklearning transfer learning and the related areas are summarized in
setting. However, the inductive transfer learning Table 2 and Fig. 2.
settingonlyaimsatachievinghighperformance Approaches to transfer learning in the above three
inthetargettaskbytransferringknowledgefrom different settings can be summarized into four cases based
the source task while multitask learning tries to on “What to transfer.” Table 3 shows these four cases and
learnthetargetandsourcetasksimultaneously. brief description. The first context can be referred to as
b. No labeled data in the source domain are instance-based transfer learning (or instance transfer)
available. In this case, the inductive transfer
approach [6], [28], [29], [30], [31], [24], [32], [33], [34], [35],
learning setting is similar to the self-taught
which assumes that certain parts of the data in the source
learningsetting,whichisfirstproposedbyRaina
domain can be reused for learning in the target domain by
etal.[22].Intheself-taughtlearningsetting,the
reweighting.Instancereweightingandimportancesampling
label spaces between the source and target
are two major techniques in this context.
domains may be different, which implies the
A second case can be referred to as feature-representa-
sideinformationofthesourcedomaincannotbe
tion-transfer approach [22], [36], [37], [38], [39], [8], [40],
used directly. Thus, it’s similar to the inductive
[41],[42],[43],[44].Theintuitiveideabehindthiscaseisto
transfer learning setting where the labeled data
learna“good”featurerepresentationforthetargetdomain.
in the source domain are unavailable.
Inthiscase,theknowledgeusedtotransferacrossdomains
2. Inthetransductivetransferlearningsetting,thesource
isencodedintothelearnedfeaturerepresentation.Withthe
and target tasks are the same, while the source and
new feature representation, the performance of the target
target domains are different.
task is expected to improve significantly.
In this situation, no labeled data in the target
A third case can be referred to as parameter-transfer
domain are available while a lot of labeled data in
approach [45], [46], [47], [48], [49], which assumes that the
the source domain are available. In addition,
source tasks andthe target tasks share some parameters or
according to different situations between the source
priordistributionsofthehyperparametersofthemodels.The
and target domains, we can further categorize the
transductive transfer learning setting into two cases. transferred knowledge is encoded into the shared para-
metersorpriors.Thus,bydiscoveringthesharedparameters
a. The feature spaces between the source and orpriors,knowledgecanbetransferredacrosstasks.
target domains are different, X S 6¼X T. Finally, the last case can be referred to as the relational-
b. The feature spaces between domains are the knowledge-transferproblem[50],whichdealswithtransfer
same, X S ¼X T, but the marginal probability learning for relational domains. The basic assumption
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 20:44:14 UTC from IEEE Xplore. Restrictions apply.

| PANANDYANG: |     | ASURVEYONTRANSFERLEARNING |     |     |     |     |     |     |     |     |     |     |     | 1349 |
| ----------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
Fig.2.Anoverviewofdifferentsettingsoftransfer.
behindthiscontextisthatsomerelationshipamongthedata f T ð(cid:2)Þ in D T using the knowledge in D S and T S , where
| in the    | source | and target     | domains | is           | similar. | Thus, | the | T 6¼T | .   |     |     |     |     |     |
| --------- | ------ | -------------- | ------- | ------------ | -------- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- |
|           |        |                |         |              |          |       |     | S     | T   |     |     |     |     |     |
| knowledge | to     | be transferred | is the  | relationship |          | among | the |       |     |     |     |     |     |     |
data. Recently, statistical relational learning techniques Based on the above definition of the inductive transfer
dominatethiscontext[51],[52]. learningsetting,afewlabeleddatainthetargetdomainare
Table 4 shows the cases where the different approaches required as the training data to induce the target predictive
| are used | for each | transfer | learning | setting. | We  | can see | that      |     |              |     |            |      |              |         |
| -------- | -------- | -------- | -------- | -------- | --- | ------- | --------- | --- | ------------ | --- | ---------- | ---- | ------------ | ------- |
|          |          |          |          |          |     |         | function. |     | As mentioned |     | in Section | 2.3, | this setting | has two |
the inductive transfer learning setting has been studied in cases:1)labeleddatainthesourcedomainareavailableand
many research works, while the unsupervised transfer 2) labeled data in the source domain are unavailable while
| learning | setting | is a relatively | new | research | topic | and | only      |     |      |        |        |        |                |      |
| -------- | ------- | --------------- | --- | -------- | ----- | --- | --------- | --- | ---- | ------ | ------ | ------ | -------------- | ---- |
|          |         |                 |     |          |       |     | unlabeled |     | data | in the | source | domain | are available. | Most |
studied in the context of the feature-representation-transfer transfer learning approaches in this setting focus on the
| case. In         | addition, | the | feature-representation-transfer |     |                   | problem | former | case.        |     |           |     |              |     |     |
| ---------------- | --------- | --- | ------------------------------- | --- | ----------------- | ------- | ------ | ------------ | --- | --------- | --- | ------------ | --- | --- |
| has beenproposed |           | to  | all three settingsof            |     | transferlearning. |         |        |              |     |           |     |              |     |     |
|                  |           |     |                                 |     |                   |         | 3.1    | Transferring |     | Knowledge |     | of Instances |     |     |
However,theparameter-transferandtherelational-knowledge-
transfer approach are only studied in the inductive transfer The instance-transfer approach to the inductive transfer
learning setting, which we discuss in detail below. learningsettingisintuitivelyappealing:althoughthesource
|     |     |     |     |     |     |     | domain |     | data cannot | be  | reused | directly, | there | are certain |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ----------- | --- | ------ | --------- | ----- | ----------- |
3 INDUCTIVE TRANSFER LEARNING partsofthedatathatcanstillbereusedtogetherwithafew
|     |     |     |     |     |     |     | labeled | data | in  | the target | domain. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---- | --- | ---------- | ------- | --- | --- | --- |
Definition 2(Inductive TransferLearning).Given a source Daietal.[6]proposedaboostingalgorithm,TrAdaBoost,
domain D and a learning task T , a target domain D whichisanextensionoftheAdaBoostalgorithm,toaddress
|     | S          |      |               | S        |          |     | T                                                      |     |     |     |     |     |     |     |
| --- | ---------- | ---- | ------------- | -------- | -------- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
| and | a learning | task | T , inductive | transfer | learning |     | aims                                                   |     |     |     |     |     |     |     |
|     |            |      | T             |          |          |     | theinductivetransferlearningproblems.TrAdaBoostassumes |     |     |     |     |     |     |     |
to help improve the learning of the target predictive function thatthesourceandtarget-domaindatauseexactlythesame
TABLE3
|     |     |     |     |     | Different | Approaches | toTransfer |     | Learning |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | ---------- | ---------- | --- | -------- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 20:44:14 UTC from IEEE Xplore.  Restrictions apply.

1350 IEEETRANSACTIONSONKNOWLEDGEANDDATAENGINEERING, VOL.22, NO.10, OCTOBER2010
TABLE4
Different ApproachesUsedin Different Settings
setoffeaturesandlabels,butthedistributionsofthedatain learning setting, the common features can be learned by
the two domains are different. In addition, TrAdaBoost solving an optimization problem, given as follows:
assumesthat,duetothedifferenceindistributionsbetween
the source and the target domains, some of the source argmin X X
nt
Lðy ;ha;UTx iÞþ(cid:2)kAk2
domain data may be useful in learning for the target A;U t2fT;Sg i¼1 ti t ti 2;1 ð1Þ
domain but some of them may not and could even be
s:t: U 2Od:
harmful. It attempts to iteratively reweight the source
domain data to reduce the effect of the “bad” source data
In this equation, S and T denote the tasks in the source
whileencouragethe“good”sourcedatatocontributemore domainandtargetdomain,respectively.A¼½a ;a (cid:5)2Rd(cid:6)2
S T
for the target domain. For each round of iteration,
is a matrix of parameters. U is a d(cid:6)d orthogonal matrix
TrAdaBoosttrainsthebaseclassifierontheweightedsource
(mapping function) for mapping the original high-dimen-
and target data. The error is only calculated on the target
sional data to low-dimensional representations. The ðr;pÞ-
data. Furthermore, TrAdaBoost uses the same strategy as norm of A is defined as kAk :¼ð Pd kaikpÞ 1 p. The
AdaBoosttoupdatetheincorrectlyclassifiedexamplesinthe r;p i¼1 r
optimization problem (1) estimates the low-dimensional
target domain while using a different strategy from
AdaBoost to update the incorrectly classified source exam- representations UTX T, UTX S and the parameters, A, of the
model at the same time. The optimization problem (1) can
ples in the source domain. Theoretical analysis of TrAda-
Boost in also given in [6]. befurthertransformedintoanequivalentconvexoptimiza-
Jiang and Zhai [30] proposed a heuristic method to tion formulation and be solved efficiently. In a follow-up
remove “misleading” training examples from the source work,Argyriouetal.[41]proposedaspectralregularization
domain based on the difference between conditional framework on matrices for multitask structure learning.
probabilities Pðy T jx T Þ and Pðy S jx S Þ. Liao et al. [31] Leeetal.[42]proposedaconvexoptimizationalgorithm
proposed a new active learning method to select the forsimultaneouslylearningmetapriorsandfeatureweights
unlabeled data in a target domain to be labeled with the from an ensemble of related prediction tasks. The meta-
help of the source domain data. Wu and Dietterich [53] priors can be transferred among different tasks. Jebara [43]
integrated the source domain (auxiliary) data an Support proposed to select features for multitask learning with
Vector Machine (SVM) framework for improving the SVMs. Ru¨ckert and Kramer [54] designed a kernel-based
classification performance. approach to inductive transfer, which aims at finding a
suitable kernel for the target data.
3.2 Transferring Knowledge of Feature
Representations 3.2.2 Unsupervised Feature Construction
The feature-representation-transfer approach to the induc- In [22], Raina et al. proposed to apply sparse coding [55],
tivetransferlearningproblemaimsatfinding“good”feature which is an unsupervised feature construction method, for
learninghigherlevelfeaturesfortransferlearning.Thebasic
representations to minimize domain divergence andclassi-
ideaofthisapproachconsistsoftwosteps.Inthefirststep,
ficationorregressionmodelerror.Strategiestofind“good”
feature representations are different for different types of higher level basis vectors b¼fb 1 ;b 2 ;...;b s g are learned on
the source domain data by solving the optimization
thesourcedomaindata.Ifalotoflabeleddatainthesource
problem (2) as shown as follows:
domain are available, supervised learning methods can be
usedtoconstructafeaturerepresentation.Thisissimilarto (cid:2) (cid:2)2
[ c 4 o 0 m ] m . I o f n no fea l t a u b r e e le l d ear d n a i t n a g in in th th e e so f u ie r l c d e o d f om m a u i l n tit a a r s e k av le a a i r la n b in le g , m a; i b n X i (cid:2) (cid:2) (cid:2) (cid:2) x Si (cid:7) X j aj Si b j (cid:2) (cid:2) (cid:2) (cid:2) 2 þ(cid:3) (cid:2) (cid:2)a Si (cid:2) (cid:2) 1 ð2Þ
unsupervised learning methods are proposed to construct s:t: kb k (cid:3)1; 8j21;...;s:
j 2
the feature representation.
In this equation, aj Si is a new representation of basis b j for
3.2.1 Supervised Feature Construction input x Si and (cid:3) is a coefficient to balance the feature
Supervised feature construction methods for the inductive constructiontermandtheregularizationterm.Afterlearning
transferlearningsettingaresimilartothoseusedinmultitask the basis vectors b, in the second step, an optimization
learning. The basic idea is to learn a low-dimensional algorithm (3) is applied on the target-domain data to learn
representation that is shared across related tasks. In
higherlevelfeaturesbasedonthebasisvectorsb.
addition, the learned new representation can reduce the
(cid:2) (cid:2)2
c A
m
la r
e
g s
t
s
h
y i
o
r f i i
d
o ca u t
f
i
o
o e
r
n t
m
o a r l.
u
r
l
e [
t
4 g
it
0 r
a
] e
s
s
k
p si r o
l
o
e
n p
a
m o
rn
s o e
in
d d
g
e
.
l a e
I
r
n
s r p o a
t
r
h
r o s
e
e fe
i
f
n
a e c
d
a h
u
tu
c
t
t
r a
i
e
v
sk
e
le a
t
a s
ra
r w n
ns
i e n
f
l
e
g l
r
. a(cid:8) Ti ¼arg
aT
m
i
in (cid:2) (cid:2) (cid:2)
(cid:2)
x Ti (cid:7) X
j
aj Ti b j (cid:2) (cid:2) (cid:2)
(cid:2) 2
þ(cid:3) (cid:2) (cid:2)a Ti (cid:2) (cid:2) 1 : ð3Þ
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 20:44:14 UTC from IEEE Xplore. Restrictions apply.

PANANDYANG: ASURVEYONTRANSFERLEARNING 1351
Finally, discriminative algorithms can be applied to fa(cid:8)
Ti
g0s
w
m
0;v
i
t
n
;(cid:4)ti
Jðw 0 ;v t ;(cid:4) ti Þ
with corresponding labels to train classification or regres-
sionmodelsforuseinthetargetdomain.Onedrawbackof ¼ X X nt (cid:4) þ (cid:5) 1 X kvk2þ(cid:5) kw k2
ti 2 t 2 0 ð4Þ
this method is that the so-called higher level basis vectors t2fS;Tg i¼1 t2fS;Tg
learned on the source domain in the optimization problem s:t: y ðw þvÞ(cid:2)x (cid:9)1(cid:7)(cid:4) ;
(2) may not be suitable for use in the target domain.
ti 0 t ti ti
(cid:4) (cid:9)0; i2f1;2;...;ng and t2fS;Tg:
Recently, manifold learning methods have been ti t
adapted for transfer learning. In [44], Wang and Mahade- By solving the optimization problem above, we can learn
van proposed a Procrustes analysis-based approach to the parameters w 0, v S, and v T simultaneously.
manifold alignment without correspondences, which can Severalresearchershavepursuedtheparameter-transfer
be used to transfer the knowledge across domains via the approach further. Gao et al. [49] proposed a locally
aligned manifolds. weighted ensemble learning framework to combine multi-
ple models for transfer learning, where the weights are
3.3 Transferring Knowledge of Parameters
dynamically assigned according to a model’s predictive
Mostparameter-transferapproachestotheinductivetransfer power on each test example in the target domain.
learning setting assume that individual models for related
tasks should share some parameters or prior distributions 3.4 Transferring Relational Knowledge
of hyperparameters. Most approaches described in this Different from other three contexts, the relational-knowl-
section, including a regularization framework and a edge-transfer approach deals with transfer learning pro-
hierarchical Bayesian framework, are designed to work blemsinrelationaldomains,wherethedataarenon-i.i.d.and
under multitask learning. However, they can be easily canberepresentedbymultiplerelations,suchasnetworked
modified for transfer learning. As mentioned above, multi- dataandsocialnetworkdata.Thisapproachdoesnotassume
task learning tries to learn both the source and target tasks thatthedatadrawnfromeachdomainbeindependentand
simultaneously and perfectly, while transfer learning only identically distributed (i.i.d.) as traditionally assumed. It
aims at boosting the performance of the target domain by tries to transfer the relationship among data from a source
utilizing the source domain data. Thus, in multitask domaintoatargetdomain.Inthiscontext,statisticalrelational
learning, weights of the loss functions for the source and learningtechniquesareproposedtosolvetheseproblems.
target data are the same. In contrast, in transfer learning, Mihalkovaetal.[50]proposedanalgorithmTAMARthat
weights in the loss functions for different domains can be transfers relational knowledge with Markov Logic Net-
different. Intuitively, we may assign a larger weight to the works (MLNs) across relational domains. MLNs [56] is a
lossfunctionofthetargetdomaintomakesurethatwecan powerful formalism, which combines the compact expres-
achieve better performance in the target domain. siveness of first-order logic with flexibility of probability,
Lawrence and Platt [45] proposed an efficient algorithm for statistical relational learning. In MLNs, entities in a
known as MT-IVM, which is based on Gaussian Processes relational domain are represented by predicates and their
(GP),tohandlethemultitasklearningcase.MT-IVMtriesto relationshipsarerepresentedinfirst-orderlogic.TAMARis
learn parametersof aGaussianProcessover multiple tasks motivatedbythefactthatiftwodomainsarerelatedtoeach
other, there may exist mappings to connect entities and
by sharing the same GP prior. Bonilla et al. [46] also
theirrelationshipsfromasourcedomaintoatargetdomain.
investigated multitask learning in the context of GP. The
For example, a professor can be considered as playing a
authorsproposedtouseafree-formcovariancematrixover
similar role in an academic domain as a manager in an
tasks to modelintertaskdependencies, whereaGPprior is
industrial management domain. In addition, the relation-
used to induce correlations between tasks. Schwaighofer
ship between a professor and his or her students is similar
et al. [47] proposed to use a hierarchical Bayesian frame-
to the relationship between a manager and his or her
work (HB) together with GP for multitask learning.
workers.Thus,theremayexistamappingfromprofessorto
Besides transferring the priors of the GP models, some
manager and a mapping from the professor-student
researchers also proposed to transfer parameters of SVMs
relationship to the manager-worker relationship. In this
underaregularizationframework.EvgeniouandPontil[48]
vein, TAMAR tries to use an MLN learned for a source
borrowed the idea of HB to SVMs for multitask learning.
domain to aid in the learning of an MLN for a target
The proposed method assumed that the parameter, w, in
domain. Basically, TAMAR is a two-stage algorithm. In the
SVMsforeachtaskcanbeseparatedintotwoterms.Oneis
first step, a mapping is constructed from a source MLN to
a common term over tasks and the other is a task-specific
thetargetdomainbasedonweightedpseudolog-likelihood
term. In inductive transfer learning,
measure (WPLL). In the second step, a revision is done for
w ¼w þv and w ¼w þv ; the mapped structure in the target domain through the
S 0 S T 0 T
FORTE algorithm [57], which is an inductive logic
wherew S andw T areparametersoftheSVMsforthesource programming (ILP) algorithm for revising first-order
task and the target learning task, respectively. w 0 is a theories. The revised MLN can be used as a relational
commonparameterwhilev S andv T arespecificparameters model for inference or reasoning in the target domain.
for the source task and the target task, respectively. By
In the AAAI-2008 workshop on transfer learning for
assuming f t ¼w t (cid:2)x to be a hyperplane for task t, an complex tasks,4 Mihalkova and Mooney [51] extended
extensionofSVMstomultitasklearningcasecanbewritten
as the following: 4.http://www.cs.utexas.edu/~mtaylor/AAAI08TL/.
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 20:44:14 UTC from IEEE Xplore. Restrictions apply.

1352 IEEETRANSACTIONSONKNOWLEDGEANDDATAENGINEERING, VOL.22, NO.10, OCTOBER2010
TAMAR to the single-entity-centered setting of transfer Most approaches described in the following sections are
learning, where only one entity in a target domain is related to case 2 above.
available. Davis and Domingos [52] proposed an approach
4.1 Transferring the Knowledge of Instances
to transferring relational knowledge based on a form of
Most instance-transfer approaches to the transductive
second-orderMarkovlogic.Thebasicideaofthealgorithm
transfer learning setting are motivated by importance
istodiscoverstructuralregularitiesinthesourcedomainin
sampling.Toseehowimportance-sampling-basedmethods
theformofMarkovlogicformulaswithpredicatevariables,
may help in this setting, we first review the problem of
by instantiating these formulas with predicates from the
empirical risk minimization (ERM) [60]. In general, we
target domain.
mightwanttolearntheoptimalparameters(cid:6)(cid:8) ofthemodel
by minimizing the expected risk,
4 TRANSDUCTIVE TRANSFER LEARNING
(cid:6)(cid:8) ¼argminEE ½lðx;y;(cid:6)Þ(cid:5);
Thetermtransductivetransferlearningwasfirstproposedby
ðx;yÞ2P
(cid:6)2(cid:2)
Arnold et al. [58], where they required that the source and
where lðx;y;(cid:6)Þ is a loss function that depends on the
target tasks be the same, although the domains may be
parameter (cid:6). However, since it is hard to estimate the
different. On top of these conditions, they further required
probabilitydistributionP,wechoosetominimizetheERM
thatallunlabeleddatainthetargetdomainareavailableat
instead,
training time, but we believe that this condition can be
relaxed;instead,inourdefinitionofthetransductivetransfer 1X n
learning setting, we only require that part of the unlabeled (cid:6)(cid:8) ¼argmin n ½lðx i ;y i ;(cid:6)Þ(cid:5);
target data be seen at training time in order to obtain the (cid:6)2(cid:2) i¼1
marginal probability for the target data. where n is size of the training data.
Note that the word “transductive” is used with several
In the transductive transfer learning setting, we want to
meanings. In the traditional machine learning setting,
learn an optimal model for the target domain by minimiz-
transductive learning [59] refers to the situation where all
ing the expected risk,
test data are required to be seen at training time, and that
the learned model cannot be reused for future data. Thus, (cid:6)(cid:8) ¼argmin X PðD Þlðx;y;(cid:6)Þ:
T
when some new test data arrive, they must be classified
together with all existing data. In our categorization of
(cid:6)2(cid:2) ðx;yÞ2DT
transferlearning,incontrast,weusethetermtransductiveto However, since no labeled data in the target domain are
emphasizetheconceptthatinthistypeoftransferlearning, observed in training data, we have to learn a model from
the tasks must be the same and there must be some thesourcedomaindatainstead.IfPðD
S
Þ¼PðD
T
Þ,thenwe
unlabeled data available in the target domain.
may simply learn the model by solving the following
Definition 3 (Transductive Transfer Learning). Given a optimization problem for use in the target domain,
source domain D and a corresponding learning task T , a
S S X
target domain D T and a corresponding learning task T T , (cid:6)(cid:8) ¼argmin PðD S Þlðx;y;(cid:6)Þ:
transductivetransferlearningaimstoimprovethelearningof (cid:6)2(cid:2) ðx;yÞ2DS
thetargetpredictivefunctionf T ð(cid:2)ÞinD T usingtheknowledgein Otherwise, when PðD S Þ6¼PðD T Þ, we need to modify the
D andT ,whereD 6¼D andT ¼T .Inaddition,some
S S S T S T above optimization problem to learn a model with high
unlabeledtarget-domaindatamustbeavailableattrainingtime.
generalization ability for the target domain, as follows:
ThisdefinitioncoverstheworkofArnoldetal.[58],since (cid:6)(cid:8) ¼argmin X PðD T Þ PðD Þlðx;y;(cid:6)Þ
thelatterconsidereddomainadaptation,wherethedifference PðD Þ S
lies between the marginal probability distributions of (cid:6)2(cid:2) ðx;yÞ2DS S ð5Þ
source and target data; i.e., the tasks are the same but the (cid:10)argmin X nS P T ðx Ti ;y Ti Þ lðx ;y ;(cid:6)Þ:
domains are different. P ðx ;y Þ Si Si
(cid:6)2(cid:2) i¼1 S Si Si
Similar to the traditional transductive learning setting,
which aims to make the best use of the unlabeled test data Therefore,byaddingdifferentpenaltyvaluestoeachinstance
f tr o a r n l s e f a e r r ni l n ea g r , n in in o g u , r w c e la a s l s s i o fic a a s t s io u n m s e ch th e a m t e so u m nd e e t r a t r r g a e n t s -d d o u m ct a iv in e ðx Si ;y Si Þ with the corresponding weight P P T Sð ð x x S T i i ; ; y y S T i i Þ Þ , we can
learn a precise model for the target domain. Furthermore,
unlabeled data be given. In the above definition of
transductive transfer learning, the source and target tasks since PðY T jX T Þ¼PðY S jX S Þ. Thus, the difference between
are the same, which implies that one can adapt the PðD S ÞandPðD T ÞiscausedbyPðX S ÞandPðX T Þand
predictive function learned in the source domain for use
P ðx ;y Þ Pðx Þ
inthetargetdomainthroughsomeunlabeledtarget-domain T Ti Ti ¼ Si :
P ðx ;y Þ Pðx Þ
data.AsmentionedinSection2.3,thissettingcanbesplitto S Si Si Ti
two cases: 1) The feature spaces between the source and
Ifwecanestimate
PðxSi Þ
foreachinstance,wecansolvethe
target domains are different, X
S
6¼X
T
, and 2) the feature
transductive transfer
P
l
ð
e
x
a
Ti
r
Þ
ning problems.
spaces between domains are the same, X S ¼X T, but the
Thereexistvariouswaystoestimate
PðxSi Þ
.Zadrozny[24]
marginal probability distributions of the input data are PðxTi Þ
different, PðX S Þ6¼PðX T Þ. This is similar to the require- proposed to estimate the terms Pðx Si Þ and Pðx Ti Þ indepen-
ments in domain adaptation and sample selection bias. dently by constructing simple classification problems.
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 20:44:14 UTC from IEEE Xplore. Restrictions apply.

| PANANDYANG: |     | ASURVEYONTRANSFERLEARNING |     |     |     |     |     |     |     |     |     |     |     | 1353 |
| ----------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
Fan et al. [35] further analyzed the problems by using domains. Then, SCL removes these pivot features from the
dataandtreatseachpivotfeatureasanewlabelvector.The
| various | classifiers | to       | estimate      | the | probability | ratio.   | Huang |                  |     |          |        |                 |             |             |
| ------- | ----------- | -------- | ------------- | --- | ----------- | -------- | ----- | ---------------- | --- | -------- | ------ | --------------- | ----------- | ----------- |
|         |             |          |               |     |             |          |       | m classification |     | problems | can    | be constructed. |             | By assuming |
| et al.  | [32]        | proposed | a kernel-mean |     |             | matching | (KMM) |                  |     |          |        |                 |             |             |
|         |             |          |               |     |             |          |       | each problem     |     | can be   | solved | by linear       | classifier, | which is    |
P ð x S Þ
algorithm to learn i directly by matching the means shown as follows:
P ð x Ti Þ
betweenthesourcedomaindataandthetargetdomaindata
|                                                  |     |     |     |     |     |     |     |     | fðxÞ¼sgn |     | (cid:6) wT | (cid:2)x (cid:7) ; l¼1;...;m: |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | ----------------------------- | --- | --- |
| inareproducing-kernelHilbertspace(RKHS).KMMcanbe |     |     |     |     |     |     |     |     |          | l   | l          |                               |     |     |
rewritten as the following quadratic programming (QP) SCLcanlearnamatrixW ¼½w w ...w (cid:5)ofparameters.In
|     |     |     |     |     |     |     |     |     |     |     |     | 1 2 | m   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
optimization problem. thethirdstep,singularvaluedecomposition(SVD)isapplied
|     |     |     |     |     |     |     |     |           |     |       |                     | ¼UDVT,then(cid:6)¼U |     | T              |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----- | ------------------- | ------------------- | --- | -------------- |
|     |     |     |     |     |     |     |     | tomatrixW | ¼½w | 1 w 2 | ...w m (cid:5).LetW |                     |     |                |
|     |     |     | 1   |     |     |     |     |           |     |       |                     |                     |     | ½ 1:h;:(cid:5) |
min (cid:3)TK(cid:3)(cid:7)(cid:7)T(cid:3) (histhenumberofthesharedfeatures)isthematrix(linear
2
|     | (cid:3) |     |     |             |     |         |     | mapping)whoserowsarethetopleftsingularvectorsofW. |     |     |     |     |     |     |
| --- | ------- | --- | --- | ----------- | --- | ------- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |         |     |     | (cid:3)     |     | (cid:3) |     | ð6Þ                                               |     |     |     |     |     |     |
|     |         |     |     | (cid:3)X nS |     | (cid:3) |     |                                                   |     |     |     |     |     |     |
2½0;B(cid:5)and(cid:3) (cid:3)(cid:3)n Finally,standarddiscriminativealgorithmscanbeappliedto
|     | s:t: | (cid:3) i |     |            | (cid:3) i (cid:7)n S(cid:3) | S       | (cid:8); |                                                   |        |     |          |         |          |           |
| --- | ---- | --------- | --- | ---------- | --------------------------- | ------- | -------- | ------------------------------------------------- | ------ | --- | -------- | ------- | -------- | --------- |
|     |      |           |     | (cid:3)    |                             |         |          | theaugmentedfeaturevectortobuildmodels.Theaugmen- |        |     |          |         |          |           |
|     |      |           |     | (cid:3)i¼1 |                             | (cid:3) |          |                                                   |        |     |          |         |          |           |
|     |      |           |     |            |                             |         |          | ted feature                                       | vector |     | contains | all the | original | feature x |
i
| where |     |     |          |     |         |     |     |          |        |         |          |          | (cid:6)x  |           |
| ----- | --- | --- | -------- | --- | ------- | --- | --- | -------- | ------ | ------- | -------- | -------- | --------- | --------- |
|       |     |     |          |     |         |     |     | appended | with   | the new | shared   | features | i. As     | mentioned |
|       |     |     |          |     |         |     |     | in [38], | if the | pivot   | features | are well | designed, | then the  |
|       |     |     | (cid:4)K | K   | (cid:5) |     |     |          |        |         |          |          |           |           |
K ¼ S;S S;T learnedmapping(cid:6)encodesthecorrespondencebetweenthe
K K
T;S T;T features from the different domains. Although Ben-David
K ¼kðx ;x K K et al. [61] showed experimentally that SCL can reduce the
| and | ij  | i j Þ. | S;S and | T;T | are kernel | matrices |     | for |     |     |     |     |     |     |
| --- | --- | ------ | ------- | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
differencebetweendomains;howtoselectthepivotfeatures
| the source |     | domain | data | and the | target | domain |     | data, |     |     |     |     |     |     |
| ---------- | --- | ------ | ---- | ------- | ------ | ------ | --- | ----- | --- | --- | --- | --- | --- | --- |
Pn S i s d i f f ic u l ta n d d om a i n d e p e n d e n t . I n [ 3 8 ] ,B l it z e r e t a l .u s e d a
| respectively. |     | (cid:7) ¼ n S | T kðx | ;x   | Þ, where | x   | 2X  | X T, |     |     |     |     |     |     |
| ------------- | --- | ------------- | ----- | ---- | -------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
|               |     | i n           | j¼ 1  | i Tj |          | i   | S   |      |     |     |     |     |     |     |
wh i le x 2 X . T h e u r i s ti c m e t ho d to s e le c t p i vo t f e a t u r e s f o r n a t u ra l l a n g u a g e
|     | T   | T   |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j P ð x Þ p r o c es s i n g (N L P) pr o b l em s ,s u c h a s ta g g in g o f se n ten c es .I n
| I t ca | n b e p | ro v edthat(cid:3) | ¼   | S i [32].Anadvantageofusing |     |     |     |     |     |     |     |     |     |     |
| ------ | ------- | ------------------ | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i P ð x Ti Þ th e i r f o l lo w -u p w o r k , th e r e s ea r ch e r s p ro p o s ed t o u s e
| KMM | is that | it can avoid | performing |     | density | estimation |     | of  |     |     |     |     |     |     |
| --- | ------- | ------------ | ---------- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
MutualInformation(MI)tochoosethepivotfeaturesinstead
| eitherPðx | ÞorPðx | Þ,whichisdifficultwhenthesizeofthe |     |     |     |     |     |                                                       |     |     |     |     |     |     |
| --------- | ------ | ---------------------------------- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|           | Si     | Ti                                 |     |     |     |     |     | ofusingmoreheuristiccriteria[8].MI-SCLtriestofindsome |     |     |     |     |     |     |
datasetissmall.Sugiyamaetal.[34]proposedanalgorithm pivotfeaturesthathavehighdependenceonthelabelsinthe
| known | as Kullback-Leibler |     |     | Importance |     | Estimation | Proce- |     |     |     |     |     |     |     |
| ----- | ------------------- | --- | --- | ---------- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
sourcedomain.
PðxSi Þ
dure (KLIEP) to estimate P ðx directly, based on the Transfer learning in the NLP domain is sometimes
Ti Þ
minimization of the Kullbac k -L eibler divergence. can be referred to as domain adaptation. In this area, Daume´ [39]
|     |     |     |     |     |     |     |     | proposed | a kernel-mapping |     |     | function | for NLP | problems, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | --- | -------- | ------- | --------- |
integratedwithcross-validationtoperformmodelselection
whichmapsthedatafrombothsourceandtargetdomainsto
automaticallyintwosteps:1)estimatingtheweightsofthe
ahigh-dimensionalfeaturespace,wherestandarddiscrimi-
sourcedomaindataand2)trainingmodelsonthereweighted
|       |        |             |          |     |     |       |              | native learning |     | methods     | are | used to        | train the | classifiers. |
| ----- | ------ | ----------- | -------- | --- | --- | ----- | ------------ | --------------- | --- | ----------- | --- | -------------- | --------- | ------------ |
| data. | Bickel | et al. [33] | combined | the | two | steps | in a unified |                 |     |             |     |                |           |              |
|       |        |             |          |     |     |       |              | However,        | the | constructed |     | kernel-mapping |           | function is  |
frameworkbyderivingakernel-logisticregressionclassifier. domain knowledge driven. It is not easy to generalize the
Besides sample reweighting techniques, Dai et al. [28] kernel mapping to other areas or applications. Blitzer et al.
extended a traditional Naive Bayesian classifier for the [62] analyzed the uniform convergence bounds for algo-
transductivetransferlearningproblems.Formoreinforma- rithmsthatminimizedaconvexcombinationofsourceand
targetempiricalrisks.
| tion on | importance | sampling |     | and | reweighting | methods |     | for |     |     |     |     |     |     |
| ------- | ---------- | -------- | --- | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
In[36],Daietal.proposedacoclustering-basedalgorithm
covariateshiftorsampleselectionbias,readerscanrefertoa
topropagatethelabelinformationacrossdifferentdomains.
recentlypublishedbook[29]byQuionero-Candelaetal.One
|          |         |            |     |        |           |     |         | In [63],           | Xing | et al. proposed |         | a novel algorithm    |     | known as    |
| -------- | ------- | ---------- | --- | ------ | --------- | --- | ------- | ------------------ | ---- | --------------- | ------- | -------------------- | --- | ----------- |
| can also | consult | a tutorial | on  | Sample | Selection |     | Bias by | Fan                |      |                 |         |                      |     |             |
|          |         |            |     |        |           |     |         | bridged refinement |      | to              | correct | the labels predicted |     | by a shift- |
andSugiyamainICDM-08.5
unawareclassifiertowardatargetdistributionandtakethe
4.2 Transferring Knowledge of Feature mixturedistributionofthetrainingandtestdataasabridge
Representations to better transfer from the training data to the test data. In
[64],Lingetal.proposedaspectralclassificationframework
| Most | feature-representation-transfer |     |     |     | approaches |     | to  | the |     |     |     |     |     |     |
| ---- | ------------------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
transductive transfer learning setting are under unsuper- for cross-domain transfer learning problem, where the
objectivefunctionisintroducedtoseekconsistencybetween
| vised      | learning       | frameworks. |          | Blitzer | et al. | [38]       | proposed | a             |     |             |     |                       |     |           |
| ---------- | -------------- | ----------- | -------- | ------- | ------ | ---------- | -------- | ------------- | --- | ----------- | --- | --------------------- | --- | --------- |
|            |                |             |          |         |        |            |          | the in-domain |     | supervision |     | and the out-of-domain |     | intrinsic |
| structural | correspondence |             | learning |         | (SCL)  | algorithm, | which    |               |     |             |     |                       |     |           |
extends [37], to make use of the unlabeled data from the structure. In [65], Xue et al. proposed a cross-domain text
target domain to extract some relevant features that may classification algorithm that extended the traditional prob-
reducethedifferencebetweenthedomains.Thefirststepof abilistic latent semantic analysis (PLSA) algorithm to
SCListodefineasetofpivotfeatures6(thenumberofpivot
|     |     |     |     |     |     |     |     | integrate | labeled | and | unlabeled | data | from | different but |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | --- | --------- | ---- | ---- | ------------- |
feature is denoted by m) on the unlabeled data from both relateddomains,intoaunifiedprobabilisticmodel.Thenew
modeliscalledTopic-bridgedPLSA,orTPLSA.
5. Tutorial slides can be found at http://www.cs.columbia.edu/~fan/ Transfer learning via dimensionality reduction was
PPT/ICDM08SampleBias.ppt.
recentlyproposedbyPanetal.[66].Inthiswork,Panetal.
| 6. The     | pivot | features | are domain | specific | and | depend | on  | prior     |     |         |      |             |     |           |
| ---------- | ----- | -------- | ---------- | -------- | --- | ------ | --- | --------- | --- | ------- | ---- | ----------- | --- | --------- |
| knowledge. |       |          |            |          |     |        |     | exploited | the | Maximum | Mean | Discrepancy |     | Embedding |
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 20:44:14 UTC from IEEE Xplore.  Restrictions apply.

1354 IEEETRANSACTIONSONKNOWLEDGEANDDATAENGINEERING, VOL.22, NO.10, OCTOBER2010
(MMDE) method, originally designed for dimensionality data to reduce the dimensions. These two steps run
reduction, to learn a low-dimensional space to reduce the iteratively to find the best subspace for the target data.
difference of distributions between different domains for
transductivetransferlearning.However,MMDEmaysuffer 6 TRANSFER BOUNDSAND NEGATIVE TRANSFER
from its computational burden. Thus, in [67], Pan et al.
further proposed an efficient feature extraction algorithm, Animportantissueistorecognizethelimitofthepowerof
knownasTransferComponentAnalysis(TCA)toovercome transfer learning. In [68], Mahmud and Ray analyzed the
thedrawbackofMMDE. case of transfer learning using Kolmogorov complexity,
where some theoretical bounds are proved. In particular,
the authors used conditional Kolmogorov complexity to
5 UNSUPERVISED TRANSFER LEARNING
measurerelatednessbetweentasksandtransferthe“right”
Definition 4 (Unsupervised Transfer Learning). Given a amountofinformationinasequentialtransferlearningtask
sourcedomainD S withalearningtaskT S ,atargetdomainD T under a Bayesian framework.
and a corresponding learning task T T , unsupervised transfer Recently,Eatonetal.[69]proposedanovelgraph-based
learning aims to help improve the learning of the target method for knowledge transfer, where the relationships
predictivefunctionf T ð(cid:2)Þ7inD T usingtheknowledgeinD S and betweensourcetasksaremodeledbyembeddingthesetof
T S ,whereT S 6¼T T andY S andY T arenotobservable. learnedsourcemodelsinagraphusingtransferabilityasthe
metric.Transferringtoanewtaskproceedsbymappingthe
Based on the definition of the unsupervised transfer problemintothegraphandthenlearningafunctiononthis
learning setting, no labeled data are observed in the source graph that automatically determines the parameters to
andtargetdomainsintraining.Sofar,thereislittleresearch
transfertothenewlearningtask.
work on this setting. Recently, Self-taught clustering (STC)
Negativetransferhappenswhenthesourcedomaindata
[26] and transferred discriminative analysis (TDA) [27]
andtaskcontributetothereducedperformanceoflearning
algorithms are proposed to transfer clustering and transfer
in the target domain. Despite the fact that how to avoid
dimensionality reduction problems, respectively.
negative transfer is a very important issue, little research
5.1 Transferring Knowledge of Feature workhasbeenpublishedonthistopic.Rosensteinetal.[70]
Representations empiricallyshowedthatiftwotasksaretoodissimilar,then
Dai et al. [26] studied a new case of clustering problems, brute-forcetransfermayhurtthe performanceofthe target
known as self-taught clustering. Self-taught clustering is an task. Some works have been exploited to analyze related-
instance of unsupervised transfer learning, which aims at ness among tasks and task clustering techniques, such as
clustering a small collection of unlabeled data in the [71], [72], which may help provide guidance on how to
target domain with the help of a large amount of avoid negative transfer automatically. Bakker and Heskes
unlabeled data in the source domain. STC tries to learn [72] adopted a Bayesian approach in which some of the
a common feature space across domains, which helps in model parameters are shared for all tasks and others more
clustering in the target domain. The objective function of looselyconnectedthroughajointpriordistributionthatcan
STC is shown as follows: belearnedfromthedata.Thus,thedataareclusteredbased
onthetaskparameters,wheretasksinthesameclusterare
JðX~
T
;X~
S
;Z~Þ
supposed to be related to each other. Argyriou et al. [73]
ð7Þ
¼IðX ;ZÞ(cid:7)IðX~ ;Z~Þþ(cid:5) (cid:8) IðX ;ZÞ(cid:7)IðX~ ;Z~Þ (cid:9) ; considered situations in which the learning tasks can be
T T S S
dividedintogroups.Taskswithineachgrouparerelatedby
where X S and X T are the source and target domain data, sharing a low-dimensional representation, which differs
respectively.Z isasharedfeaturespacebyX S andX T,and among different groups. As a result, tasks within a group
Ið(cid:2);(cid:2)Þ is the mutual information between two random can find it easier to transfer useful knowledge.
variables.Supposethatthereexistthreeclusteringfunctions
X C ~ X T T ,X : ~ X S, T a ! nd X Z~ ~ T a , re C c X o S rr : e X sp S o ! nd X i ~ n S g , c a lu n s d ter C s Z of :Z X T ! ,X Z~ S , ,a w n h d e Z re , 7 APPLICATIONS OF TRANSFER LEARNING
respectively. The goal of STC is to learn X~ T by solving the Recently, transfer learning techniques have been applied
successfully in many real-world applications. Raina et al.
optimization problem (7):
[74] and Dai et al. [36], [28] proposed to use transfer
argminJðX~ ;X~ ;Z~Þ: ð8Þ learning techniques to learn text data across domains,
T S
X~ T;X~ S;Z~ respectively. Blitzer et al. [38] proposed to use SCL for
solving NLPproblems.An extensionof SCLwas proposed
Aniterativealgorithmforsolvingtheoptimizationfunction
in[8]forsolvingsentimentclassificationproblems.Wuand
(8) was given in [26].
Dietterich [53] proposed to use both inadequate target
Similarly,Wangetal.[27]proposedaTDAalgorithmto
domaindataandplentyoflowqualitysourcedomaindata
solvethetransferdimensionalityreductionproblem.TDAfirst
for image classification problems. Arnold et al. [58]
applies clustering methods to generate pseudoclass labels
proposed to use transductive transfer learning methods to
forthetargetunlabeleddata.Itthenappliesdimensionality
solve name-entity recognition problems. In [75], [76], [77],
reduction methods to the target data and labeled source
[78], [79], transfer learning techniques are proposed to
extract knowledge from WiFi localization models across
7. In unsupervised transfer learning, the predicted labels are latent
variables,suchasclustersorreduceddimensions. time periods, space, and mobile devices, to benefit WiFi
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 20:44:14 UTC from IEEE Xplore. Restrictions apply.

PANANDYANG: ASURVEYONTRANSFERLEARNING 1355
localization tasks in other settings. Zhuo et al. [80] studied for localization around 145:5(cid:6)37:5m2 in two
howtotransferdomainknowledgetolearnrelationalaction different time periods.
models across domains in automated planning. 4. Sen. This data set was first used in [8].11 This data
In[81],Raykaretal.proposedanovelBayesianmultiple- set contains product reviews downloaded from
instancelearningalgorithm,whichcanautomaticallyidenti- Amazon.com from four product types (domains):
fytherelevantfeaturesubsetanduseinductivetransferfor Kitchen, Books, DVDs, and Electronics. Each
learning multiple, but conceptually related, classifiers, for domain has several thousand reviews, but the
computeraideddesign(CAD).In[82],Lingetal.proposed exact number varies by domain. Reviews contain
an information-theoretic approach for transfer learning to star ratings (1-5 stars).
addressthecross-languageclassificationproblemfortranslating
Empirical evaluation. To show how much benefit
webpagesfromEnglishtoChinese.Theapproachaddressed
transfer learning methods can bring as compared to
the problem when there are plenty of labeled English text
traditional learning methods, researchers have used some
data whereas there are only a small number of labeled
publicdatasets.Weshowalisttakenfromsomepublished
Chinese text documents. Transfer learning across the two
transfer learning papers in Table 5. In [6], [84], [49], the
featurespacesareachievedbydesigningasuitablemapping authors used the 20 Newsgroups data12 as one of the
functionasabridge.
evaluation data sets. Due to the differences in the pre-
So far, there are at least two international competitions
processing steps of the algorithms by different researchers,
basedontransferlearning,whichmadeavailablesomemuch
itis hardto comparethe proposedmethods directly.Thus,
needed public data. In the ECML/PKDD-2006 discovery
we denote them by 20-Newsgroups , 20-Newsgroups , and
challenge,8 the task was to handle personalized spam 1 2
20-Newsgroups , respectively, and show the comparison
3
filtering and generalization across related learning tasks.
results between the proposed transfer learning methods
Fortrainingaspam-filteringsystem,weneedtocollectalot
and nontransfer learning methods in the table.
ofe-mailsfromagroupofuserswithcorrespondinglabels:
On the 20Newsgroups data, Dai et al. [6] showed the
1
spamornotspam,andtrainaclassifierbasedonthesedata.
comparison experiments between standard SVM and the
Foranewe-mailuser,wemightwanttoadaptthelearned
proposed TrAdaBoost algorithm. On 20Newsgroups , Shi
2
modelfortheuser.Thechallengeisthatthedistributionsof
et al. [84] applied an active learning algorithm to select
emailsforthefirstsetofusersandthenewuseraredifferent.
important instances for transfer learning (AcTraK) with
Thus,thisproblemcanbemodeledasaninductivetransfer
TrAdaBoost and standard SVM. Gao et al. [49] evaluated
learningproblem,whichaimstoadaptanoldspam-filtering
their proposed locally weighted ensemble learning algo-
model to a new situation with fewer training data and less
rithms, pLWE and LWE, on the 20Newsgroups , compared
trainingtime. 3
to SVM and Logistic Regression (LR).
A second data set was made available through the
In addition, in the table, we also show the comparison
ICDM-2007Contest,inwhichataskwastoestimateaWiFi
results on the sentiment classification data set reported in
client’sindoorlocationsusingtheWiFisignaldataobtained
[8]. On this data set, SGD denotes the stochastic gradient-
overdifferentperiodsoftime[83].SincethevaluesofWiFi
descentalgorithmwithHuber loss,SCLrepresentsalinear
signal strength may be a function of time, space, and
predictor on the new representations learned by Structural
devices, distributions of WiFi data over different time
Correspondence Learning algorithm, and SCL-MI is an
periodsmaybeverydifferent.Thus,transferlearningmust
extension of SCL by applying Mutual Information to select
be designed to reduce the data relabeling effort.
the pivot features for the SCL algorithm.
Data sets for transfer learning. So far, several data sets
Finally, on the WiFi localization data set, we show the
have been published for transfer learning research. We
comparisonresultsreportedin[67],wherethebaselineisa
denote the text mining data sets, Email spam-filtering data
regularizedleast squareregression model(RLSR), which is
set,theWiFilocalizationovertimeperiodsdataset,andthe
a standard regression model, and KPCA, which represents
SentimentclassificationdatasetbyText,E-mail,WiFi,and
to apply RLSR on the new representations of the data
Sen, respectively.
learned by Kernel Principle Component Analysis. The
1. Text. Three data sets, 20 Newsgroups, SRAA, and compared transfer learning methods include KMM and
Reuters-21578,9 have been preprocessed for a trans- the proposed algorithm, TCA. For more detail about the
ferlearningsettingbysomeresearchers.Thedatain experimentalresults,thereadersmayrefertothereference
these data sets are categorized to a hierarchical papersshowedinthetable.Fromthesecomparisonresults,
structure. Data from different subcategories under we can find that the transfer learning methods designed
the same parent category are considered to be from appropriately for real-world applications can indeed im-
different but related domains. The task is to predict prove the performance significantly compared to the
the labels of the parent category. nontransfer learning methods.
2. E-mail.Thisdatasetisprovidedbythe2006ECML/ Toolboxes for transfer learning. Researchers at UC
PKDD discovery challenge. Berkeley provided a MATLAB toolkit for transfer learn-
3. WiFi. This data set is provided by the ICDM-2007 ing.13 The toolkit contains algorithms and benchmark data
Contest.10 The data were collected inside a building setsfortransferlearning.Inaddition,itprovidesastandard
8.http://www.ecmlpkdd2006.org/challenge.html. 11.http://www.cis.upenn.edu/~mdredze/datasets/sentiment/.
9.http://apex.sjtu.edu.cn/apex_wiki/dwyak. 12.http://people.csail.mit.edu/jrennie/20Newsgroups/.
10.http://www.cse.ust.hk/~qyang/ICDMDMC2007. 13.http://multitask.cs.berkeley.edu/.
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 20:44:14 UTC from IEEE Xplore. Restrictions apply.

1356 IEEETRANSACTIONSONKNOWLEDGEANDDATAENGINEERING, VOL.22, NO.10, OCTOBER2010
TABLE5
|     |     |     | Comparison |     | betweenTransfer |     | Learning | and NontransferLearning |     |     | Methods |     |     |     |     |
| --- | --- | --- | ---------- | --- | --------------- | --- | -------- | ----------------------- | --- | --- | ------- | --- | --- | --- | --- |
platform for developing and testing new algorithms for auxiliary rating matrix. They then constructed a cluster-
transfer learning. level rating matrix known as a codebook. By assuming the
|              |              |     |               |                   |          |                 |          | target rating   | matrix | (on        | movies)    | is  | related | to the        | auxiliary |
| ------------ | ------------ | --- | ------------- | ----------------- | -------- | --------------- | -------- | --------------- | ------ | ---------- | ---------- | --- | ------- | ------------- | --------- |
| 7.1 Other    | Applications |     |               | of Transfer       | Learning |                 |          |                 |        |            |            |     |         |               |           |
|              |              |     |               |                   |          |                 |          | one (on books), |        | the target | domain     |     | can be  | reconstructed | by        |
| Transfer     | learning     | has | found         | many applications |          | in              | sequen-  |                 |        |            |            |     |         |               |           |
|              |              |     |               |                   |          |                 |          | expanding       | the    | codebook,  | completing |     | the     | knowledge     | trans-    |
| tial machine | learning     |     | as well.      | For example,      |          | Kuhlmann        | and      | fer process.    |        |            |            |     |         |               |           |
| Stone [85]   | proposed     |     | a graph-based |                   | method   | for identifying |          |                 |        |            |            |     |         |               |           |
| previously   | encountered  |     | games,        | and               | applied  | this technique  |          |                 |        |            |            |     |         |               |           |
|              |              |     |               |                   |          |                 |          | 8 CONCLUSIONS   |        |            |            |     |         |               |           |
| to automate  | domain       |     | mapping       | for value         | function |                 | transfer |                 |        |            |            |     |         |               |           |
and speed up reinforcement learning on variants of In this survey paper, we have reviewed several current
trendsoftransferlearning.Transferlearningisclassifiedto
| previously | played    |           | games.       | A new         | approach       | to            | transfer  |                  |              |           |             |              |          |             |        |
| ---------- | --------- | --------- | ------------ | ------------- | -------------- | ------------- | --------- | ---------------- | ------------ | --------- | ----------- | ------------ | -------- | ----------- | ------ |
|            |           |           |              |               |                |               |           | three different  |              | settings: | inductive   |              | transfer | learning,   | trans- |
| between    | entirely  | different |              | feature       | spaces         | is proposed   | in        |                  |              |           |             |              |          |             |        |
|            |           |           |              |               |                |               |           | ductive transfer |              | learning, | and         | unsupervised |          | transfer    | learn- |
| translated | learning, | which     | is           | made possible |                | by learning   |           | a                |              |           |             |              |          |             |        |
|            |           |           |              |               |                |               |           | ing. Most        | previous     |           | works       | focused      | on       | the former  | two    |
| mapping    | function  |           | for bridging | features      | in             | two           | entirely  |                  |              |           |             |              |          |             |        |
|            |           |           |              |               |                |               |           | settings.        | Unsupervised |           | transfer    | learning     |          | may attract | more   |
| different  | domains   | (images   |              | and text)     | [86]. Finally, |               | Li et al. |                  |              |           |             |              |          |             |        |
|            |           |           |              |               |                |               |           | and more         | attention    | in        | the future. |              |          |             |        |
| [87], [88] | have      | applied   | transfer     | learning      | to             | collaborative |           |                  |              |           |             |              |          |             |        |
Furthermore,eachoftheapproachestotransferlearning
| filtering | problems |          | to solve | the cold  | start  | and            | sparsity |                   |              |      |      |          |       |                   |          |
| --------- | -------- | -------- | -------- | --------- | ------ | -------------- | -------- | ----------------- | ------------ | ---- | ---- | -------- | ----- | ----------------- | -------- |
|           |          |          |          |           |        |                |          | can be classified |              | into | four | contexts | based | on                | “what to |
| problems. | In       | [87], Li | et al.   | learned a | shared | rating-pattern |          |                   |              |      |      |          |       |                   |          |
|           |          |          |          |           |        |                |          | transfer”         | in learning. |      | They | include  | the   | instance-transfer |          |
mixture model, known as a Rating-Matrix Generative approach, the feature-representation-transfer approach, the
| Model | (RMGM), | in  | terms | of the latent | user- | and | item- |     |     |     |     |     |     |     |     |
| ----- | ------- | --- | ----- | ------------- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
parameter-transferapproach,andtherelational-knowledge-
| cluster | variables. | RMGM | bridges | multiple |     | rating | matrices |                    |     |               |     |     |        |       |          |
| ------- | ---------- | ---- | ------- | -------- | --- | ------ | -------- | ------------------ | --- | ------------- | --- | --- | ------ | ----- | -------- |
|         |            |      |         |          |     |        |          | transfer approach, |     | respectively. |     | The | former | three | contexts |
from different domainsby mapping the users and items in haveani.i.d.assumptiononthedatawhilethe lastcontext
each rating matrix onto the shared latent user and item dealswithtransferlearningonrelationaldata.Mostofthese
spaces in order to transfer useful knowledge. In [88], they approaches assume that the selected source domain is
applied coclustering algorithms on users and items in an relatedtothetargetdomain.
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 20:44:14 UTC from IEEE Xplore.  Restrictions apply.

| PANANDYANG: |     | ASURVEYONTRANSFERLEARNING |     |     |     |     |     |        |         |       |         |            |           |     | 1357     |
| ----------- | --- | ------------------------- | --- | --- | --- | --- | --- | ------ | ------- | ----- | ------- | ---------- | --------- | --- | -------- |
|             |     |                           |     |     |     |     |     | [6] W. | Dai, Q. | Yang, | G. Xue, | and Y. Yu, | “Boosting | for | Transfer |
Inthefuture,severalimportantresearchissuesneedtobe
Learning,”Proc.24thInt’lConf.MachineLearning,pp.193-200,June
| addressed. | First, | how | to avoid | negative | transfer | is  | an open |     |     |     |     |     |     |     |     |
| ---------- | ------ | --- | -------- | -------- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
2007.
problem.AsmentionedinSection6,manyproposedtransfer
|     |     |     |     |     |     |     |     | [7] S.J.Pan,V.W.Zheng,Q.Yang,andD.H.Hu,“TransferLearning |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
learning algorithms assume that the source and target for WiFi-Based Indoor Localization,” Proc. Workshop Transfer
domainsarerelatedtoeachotherinsomesense.However, LearningforComplexTaskofthe23rdAssoc.fortheAdvancementof
ArtificialIntelligence(AAAI)Conf.ArtificialIntelligence,July2008.
| if the assumption |     | does | not | hold, negative |     | transfer | may |                 |     |         |     |             |               |            |     |
| ----------------- | --- | ---- | --- | -------------- | --- | -------- | --- | --------------- | --- | ------- | --- | ----------- | ------------- | ---------- | --- |
|                   |     |      |     |                |     |          |     | [8] J. Blitzer, | M.  | Dredze, | and | F. Pereira, | “Biographies, | Bollywood, |     |
happen,whichmaycausethelearnertoperformworsethan
|     |     |     |     |     |     |     |     | Boom-Boxes |     | and Blenders: |     | Domain Adaptation |     | for | Sentiment |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------- | --- | ----------------- | --- | --- | --------- |
no transferring at all. Thus, how to make sure that no Classification,”Proc.45thAnn.MeetingoftheAssoc.Computational
negative transfer happens is a crucial issue in transfer Linguistics,pp.432-439,2007.
learning. In order to avoid negative transfer learning, we [9] J. Ramon, K. Driessens, and T. Croonenborghs, “Transfer
|     |     |     |     |     |     |     |     | Learning | in  | Reinforcement |     | Learning Problems |     | through | Partial |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------- | --- | ----------------- | --- | ------- | ------- |
needtofirststudytransferabilitybetweensourcedomainsor Policy Recycling,” Proc. 18th European Conf. Machine Learning
tasks and target domains or tasks. Based on suitable (ECML ’07), pp. 699-707, 2007.
transferabilitymeasures,wecanthenselectrelevantsource [10] M.E.TaylorandP.Stone,“Cross-DomainTransferforReinforce-
mentLearning,”Proc.24thInt’lConf.MachineLearning(ICML’07),
domainsortaskstoextractknowledgefromforlearningthe
pp.879-886,2007.
| target tasks.                                      | To  | define | the transferability |     | between |     | domains |                                                                  |          |     |            |             |            |     |      |
| -------------------------------------------------- | --- | ------ | ------------------- | --- | ------- | --- | ------- | ---------------------------------------------------------------- | -------- | --- | ---------- | ----------- | ---------- | --- | ---- |
|                                                    |     |        |                     |     |         |     |         | [11] X.Yin,J.Han,J.Yang,andP.S.Yu,“EfficientClassificationacross |          |     |            |             |            |     |      |
| andtasks,wealsoneedtodefinethecriteriatomeasurethe |     |        |                     |     |         |     |         |                                                                  |          |     |            |             |            |     | IEEE |
|                                                    |     |        |                     |     |         |     |         | Multiple                                                         | Database |     | Relations: | A Crossmine | Approach,” |     |      |
similaritybetweendomainsortasks.Basedonthedistance Trans. Knowledge and Data Eng., vol. 18, no. 6, pp. 770-783, June
2006.
measures,wecanthenclusterdomainsortasks,whichmay
|              |     |                  |     |           |       |     |         | [12] L.I. | Kuncheva | and      | J.J. Rodrłguez, | “Classifier | Ensembles |          | with a |
| ------------ | --- | ---------------- | --- | --------- | ----- | --- | ------- | --------- | -------- | -------- | --------------- | ----------- | --------- | -------- | ------ |
| help measure |     | transferability. |     | A related | issue | is  | when an |           |          |          |                 |             |           |          |        |
|              |     |                  |     |           |       |     |         | Random    | Linear   | Oracle,” | IEEE            | Trans.      | Knowledge | and Data | Eng.,  |
entiredomaincannotbeusedfortransferlearning,whether
vol.19,no.4,pp.500-508,Apr.2007.
wecanstilltransferpartofthedomainforusefullearningin [13] E. Baralis, S. Chiusano, and P. Garza, “A Lazy Approach to
AssociativeClassification,”IEEETrans.KnowledgeandDataEng.,
thetargetdomain.
vol.20,no.2,pp.156-171,Feb.2008.
| In addition, |     | most | existing | transfer | learning | algorithms |     |                                                                |     |     |     |     |     |     |     |
| ------------ | --- | ---- | -------- | -------- | -------- | ---------- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|              |     |      |          |          |          |            |     | [14] X.Zhu,“Semi-SupervisedLearningLiteratureSurvey,”Technical |     |     |     |     |     |     |     |
so far focused on improving generalization across differ- Report1530,Univ.ofWisconsin-Madison,2006.
ent distributions between source and target domains or [15] K. Nigam, A.K. McCallum, S. Thrun, and T. Mitchell, “Text
tasks. In doing so, they assumed that the feature spaces Classification from Labeled and Unlabeled Documents Using
between the source and target domains are the same. EM,”MachineLearning,vol.39,nos.2/3,pp.103-134,2000.
|     |     |     |     |     |     |     |     | [16] A. Blum | and | T. Mitchell, |     | “Combining | Labeled | and Unlabeled |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------ | --- | ---------- | ------- | ------------- | --- |
However, in many applications, we may wish to transfer Proc. 11th Ann. Conf. Computational
|     |     |     |     |     |     |     |     | Data | with | Co-Training,” |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | ------------- | --- | --- | --- | --- | --- |
knowledge across domains or tasks that have different LearningTheory,pp.92-100,1998.
feature spaces, and transfer from multiple such source [17] T.Joachims,“TransductiveInferenceforTextClassificationUsing
SupportVectorMachines,”Proc.16thInt’lConf.MachineLearning,
| domains. | We  | refer to | this | type of | transfer | learning | as  |     |     |     |     |     |     |     |     |
| -------- | --- | -------- | ---- | ------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
pp.825-830,1999.
| heterogeneous |     | transfer learning. |          |     |            |      |      |             |     |        |        |                |     |           |       |
| ------------- | --- | ------------------ | -------- | --- | ---------- | ---- | ---- | ----------- | --- | ------ | ------ | -------------- | --- | --------- | ----- |
|               |     |                    |          |     |            |      |      | [18] X. Zhu | and | X. Wu, | “Class | Noise Handling | for | Effective | Cost- |
| Finally,      | so  | far, transfer      | learning |     | techniques | have | been |             |     |        |        |                |     |           |       |
SensitiveLearningbyCost-GuidedIterativeClassificationFilter-
ing,”IEEETrans.KnowledgeandDataEng.,vol.18,no.10,pp.1435-
| mainly | applied | to small | scale | applications |     | with | a limited |     |     |     |     |     |     |     |     |
| ------ | ------- | -------- | ----- | ------------ | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
1440,Oct.2006.
| variety,        | such     | as sensor-network-based |                |      | localization, |        | text    |                  |     |                                         |          |             |            |     |           |
| --------------- | -------- | ----------------------- | -------------- | ---- | ------------- | ------ | ------- | ---------------- | --- | --------------------------------------- | -------- | ----------- | ---------- | --- | --------- |
|                 |          |                         |                |      |               |        |         | [19] Q. Yang,    | C.  | Ling,                                   | X. Chai, | and R. Pan, | “Test-Cost |     | Sensitive |
| classification, |          | and image               | classification |      | problems.     |        | In the  |                  |     |                                         |          |             |            |     |           |
|                 |          |                         |                |      |               |        |         | Classificationon |     | DatawithMissingValues,”IEEETrans.Knowl- |          |             |            |     |           |
| future,         | transfer | learning                | techniques     | will | be            | widely | used to |                  |     |                                         |          |             |            |     |           |
edgeandDataEng.,vol.18,no.5,pp.626-638,May2006.
solve other challenging applications, such as video classi- [20] Learning to Learn. S. Thrun and L. Pratt, eds. Kluwer Academic
fication, social network analysis, and logical inference. Publishers,1998.
|     |     |     |     |     |     |     |     | [21] R.Caruana,“MultitaskLearning,”MachineLearning,vol.28,no.1, |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
pp.41-75,1997.
| ACKNOWLEDGMENTS |     |     |     |     |     |     |     | [22] |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
R.Raina,A.Battle,H.Lee,B.Packer,andA.Y.Ng,“Self-Taught
Learning:TransferLearningfromUnlabeledData,”Proc.24thInt’l
TheauthorsthankthesupportofHongKongCERGProject Conf.MachineLearning,pp.759-766,June2007.
621307 and a grant from NEC China Lab. [23] H. Daume´ III and D. Marcu, “Domain Adaptationfor Statistical
|     |     |     |     |     |     |     |     | Classifiers,” |     | J. Artificial | Intelligence | Research, | vol. | 26, pp. | 101-126, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------- | ------------ | --------- | ---- | ------- | -------- |
2006.
REFERENCES [24] B.Zadrozny,“LearningandEvaluatingClassifiersunderSample
SelectionBias,”Proc.21stInt’lConf.MachineLearning,July2004.
| [1] X.Wu,V.Kumar,J.R.Quinlan,J.Ghosh,Q.Yang,H.Motoda,G.J. |     |     |     |     |     |     |     | [25] |     |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
H.Shimodaira,“ImprovingPredictiveInferenceunderCovariate
McLachlan,A.F.M.Ng,B.Liu,P.S.Yu,Z.-H.Zhou,M.Steinbach, Shift by Weighting the Log-Likelihood Function,” J. Statistical
D.J.Hand,andD.Steinberg,“Top10AlgorithmsinDataMining,”
PlanningandInference,vol.90,pp.227-244,2000.
KnowledgeandInformationSystems,vol.14,no.1,pp.1-37,2008.
|             |     |        |                 |     |          |         |        | [26] W. | Dai, Q. | Yang, G. | Xue, | and Y. Yu, | “Self-Taught | Clustering,” |     |
| ----------- | --- | ------ | --------------- | --- | -------- | ------- | ------ | ------- | ------- | -------- | ---- | ---------- | ------------ | ------------ | --- |
| [2] Q. Yang | and | X. Wu, | “10 Challenging |     | Problems | in Data | Mining |         |         |          |      |            |              |              |     |
Proc.25thInt’lConf.MachineLearning,pp.200-207,July2008.
| Research,” |     | Int’l J. Information |     | Technology | and | Decision | Making, |               |     |       |        |                     |     |                |     |
| ---------- | --- | -------------------- | --- | ---------- | --- | -------- | ------- | ------------- | --- | ----- | ------ | ------------------- | --- | -------------- | --- |
|            |     |                      |     |            |     |          |         | [27] Z. Wang, | Y.  | Song, | and C. | Zhang, “Transferred |     | Dimensionality |     |
vol.5,no.4,pp.597-604,2006.
[3] G.P.C. Fung, J.X. Yu, H. Lu, and P.S. Yu, “Text Classification Reduction,” Proc. European Conf. Machine Learning and Knowledge
DiscoveryinDatabases(ECML/PKDD’08),pp.550-565,Sept.2008.
| without | Negative | Examples | Revisit,” |     | IEEE Trans. | Knowledge | and |     |     |     |     |     |     |     |     |
| ------- | -------- | -------- | --------- | --- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[28]
DataEng.,vol.18,no.1,pp.6-20,Jan.2006. W. Dai, G. Xue, Q. Yang, and Y. Yu, “Transferring Naive Bayes
|                              |        |     |             |            |          |                 |     | Classifiers |     | for Text      | Classification,” | Proc.  | 22nd  | Assoc.     | for the  |
| ---------------------------- | ------ | --- | ----------- | ---------- | -------- | --------------- | --- | ----------- | --- | ------------- | ---------------- | ------ | ----- | ---------- | -------- |
| [4] H. Al                    | Mubaid | and | S.A. Umair, | “A         | New Text | Categorization  |     |             |     |               |                  |        |       |            |          |
|                              |        |     |             |            |          |                 |     | Advancement |     | of Artificial | Intelligence     | (AAAI) | Conf. | Artificial | Intelli- |
| TechniqueUsingDistributional |        |     |             | Clustering | and      | LearningLogic,” |     |             |     |               |                  |        |       |            |          |
IEEETrans.KnowledgeandDataEng.,vol.18,no.9,pp.1156-1165, gence,pp.540-545,July2007.
Sept.2006. [29] J. Quionero-Candela, M. Sugiyama, A. Schwaighofer, and N.D.
[5] K. Sarinnapakorn and M. Kubat, “Combining Subclassifiers in Lawrence,DatasetShiftinMachineLearning.MITPress,2009.
Text Categorization: A DST-Based Solution and a Case Study,” [30] J.JiangandC.Zhai,“InstanceWeightingforDomainAdaptation
IEEETrans.KnowledgeandDataEng.,vol.19,no.12,pp.1638-1651, Proc. 45th Ann. Meeting of the Assoc. Computational
in NLP,”
| Dec.2007. |     |     |     |     |     |     |     | Linguistics,pp.264-271,June2007. |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 20:44:14 UTC from IEEE Xplore.  Restrictions apply.

1358 IEEETRANSACTIONSONKNOWLEDGEANDDATAENGINEERING, VOL.22, NO.10, OCTOBER2010
[31] X. Liao, Y. Xue, and L. Carin, “Logistic Regression with an [54] U. Ru¨ckert and S. Kramer, “Kernel-Based Inductive Transfer,”
Auxiliary Data Source,” Proc. 21st Int’l Conf. Machine Learning, Proc. European Conf. Machine Learning and Knowledge Discovery in
pp.505-512,Aug.2005. Databases(ECML/PKDD’08),pp.220-233,Sept.2008.
[32] J. Huang, A. Smola, A. Gretton, K.M. Borgwardt, and B. [55] H.Lee,A.Battle,R.Raina,andA.Y.Ng,“EfficientSparseCoding
Scho¨lkopf,“CorrectingSampleSelectionBiasbyUnlabeledData,” Algorithms,” Proc. 19th Ann. Conf. Neural Information Processing
Proc.19thAnn.Conf.NeuralInformationProcessingSystems,2007. Systems,pp.801-808,2007.
[33] S.Bickel,M.Bru¨ckner,andT.Scheffer,“DiscriminativeLearning [56] M. Richardson and P. Domingos, “Markov Logic Networks,”
forDifferingTrainingandTestDistributions,”Proc.24thInt’lConf. MachineLearningJ.,vol.62,nos.1/2,pp.107-136,2006.
MachineLearning,pp.81-88,2007. [57] S. Ramachandran and R.J. Mooney, “Theory Refinement of
[34] M. Sugiyama, S. Nakajima, H. Kashima, P.V. Buenau, and M. BayesianNetworkswithHiddenVariables,”Proc.14thInt’lConf.
MachineLearning,pp.454-462,July1998.
| Kawanabe, |     | “Direct Importance |     | Estimation |     | with Model | Selection |     |     |     |     |     |     |     |     |
| --------- | --- | ------------------ | --- | ---------- | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
[58] A.Arnold,R.Nallapati,andW.W.Cohen,“AComparativeStudy
anditsApplicationtoCovariateShiftAdaptation,”Proc.20thAnn.
Conf.NeuralInformationProcessingSystems,Dec.2008. of Methods for Transductive Transfer Learning,” Proc. Seventh
[35] W. Fan, I. Davidson, B. Zadrozny, and P.S. Yu, “An Improved IEEEInt’lConf.DataMiningWorkshops,pp.77-82,2007.
Categorization of Classifier’s Sensitivity on Sample Selection [59] T.Joachims,“TransductiveInferenceforTextClassificationUsing
Bias,”Proc.FifthIEEEInt’lConf.DataMining,2005. SupportVectorMachines,”Proc.16thInt’lConf.MachineLearning,
pp.200-209,1999.
| [36] W. | Dai, G. | Xue, Q. | Yang, | and Y. | Yu, “Co-Clustering |     | Based |     |     |     |     |     |     |     |     |
| ------- | ------- | ------- | ----- | ------ | ------------------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
[60] V.N.Vapnik,StatisticalLearningTheory.WileyInterscience,Sept.
| Classification |       | for Out-of-Domain |           | Documents,” |     | Proc. | 13th ACM     |       |     |     |     |     |     |     |     |
| -------------- | ----- | ----------------- | --------- | ----------- | --- | ----- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
| SIGKDD         | Int’l | Conf.             | Knowledge | Discovery   | and | Data  | Mining, Aug. | 1998. |     |     |     |     |     |     |     |
2007. [61] S.Ben-David,J.Blitzer,K.Crammer,andF.Pereira,“Analysisof
[37] R.K.AndoandT.Zhang,“AHigh-PerformanceSemi-Supervised Representations for Domain Adaptation,” Proc. 20th Ann. Conf.
LearningMethodforTextChunking,”Proc.43rdAnn.Meetingon NeuralInformationProcessingSystems,pp.137-144,2007.
|     |     |     |     |     |     |     |     | [62] J. Blitzer, | K. Crammer, |     | A. Kulesza, | F.  | Pereira, | and J. | Wortman, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ----------- | --- | ----------- | --- | -------- | ------ | -------- |
Assoc.forComputationalLinguistics,pp.1-9,2005.
“LearningBoundsforDomainAdaptation,”Proc.21stAnn.Conf.
[38] J.Blitzer,R.McDonald,andF.Pereira,“DomainAdaptationwith
StructuralCorrespondenceLearning,”Proc.Conf.EmpiricalMeth- NeuralInformationProcessingSystems,pp.129-136,2008.
odsinNaturalLanguage,pp.120-128,July2006. [63] D.Xing,W.Dai,G.-R.Xue,andY.Yu,“BridgedRefinementfor
[39] H.Daume´III,“FrustratinglyEasyDomainAdaptation,”Proc.45th TransferLearning,”Proc.11thEuropeanConf.PrinciplesandPractice
ofKnowledgeDiscoveryinDatabases,pp.324-335,Sept.2007.
| Ann. | Meeting | of the Assoc. | Computational |     | Linguistics, |     | pp. 256-263, |     |     |     |     |     |     |     |     |
| ---- | ------- | ------------- | ------------- | --- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
[64] X.Ling,W.Dai,G.-R.Xue,Q.Yang,andY.Yu,“SpectralDomain-
June2007.
TransferLearning,”Proc.14thACMSIGKDDInt’lConf.Knowledge
| [40] A. Argyriou, |     | T. Evgeniou, | and | M.  | Pontil, | “Multi-Task | Feature |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------------ | --- | --- | ------- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
DiscoveryandDataMining,pp.488-496,Aug.2008.
| Learning,” |     | Proc. 19th | Ann. | Conf. Neural |     | Information | Processing |     |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | ---- | ------------ | --- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Systems,pp.41-48,Dec.2007. [65] G.-R.Xue,W.Dai,Q.Yang,andY.Yu,“Topic-BridgedPLSAfor
[41] A.Argyriou,C.A.Micchelli,M.Pontil,andY.Ying,“ASpectral Cross-Domain Text Classification,” Proc. 31st Ann. Int’l ACM
|                |     |           |     |            |     |           |            | SIGIR | Conf. Research | and | Development |     | in Information |     | Retrieval, |
| -------------- | --- | --------- | --- | ---------- | --- | --------- | ---------- | ----- | -------------- | --- | ----------- | --- | -------------- | --- | ---------- |
| Regularization |     | Framework | for | Multi-Task |     | Structure | Learning,” |       |                |     |             |     |                |     |            |
pp.627-634,July2008.
Proc.20thAnn.Conf.NeuralInformationProcessingSystems,pp.25-
|     |     |     |     |     |     |     |     | [66] S.J. | Pan, J.T. Kwok, |     | and Q. | Yang, | “Transfer | Learning | via |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------------- | --- | ------ | ----- | --------- | -------- | --- |
32,2008.
|     |     |     |     |     |     |     |     | Dimensionality | Reduction,” |     | Proc. | 23rd | Assoc. | for the Advancement |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | --- | ----- | ---- | ------ | ------------------- | --- |
[42] S.I.Lee,V.Chatalbashev,D.Vickrey,andD.Koller,“Learninga
Meta-Level Prior for Feature Relevance from Multiple Related ofArtificialIntelligence(AAAI)Conf.ArtificialIntelligence,pp.677-
682,July2008.
| Tasks,” | Proc. | 24th Int’l | Conf. | Machine | Learning, | pp. | 489-496, July |     |     |     |     |     |     |     |     |
| ------- | ----- | ---------- | ----- | ------- | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[67] S.J.Pan,I.W.Tsang,J.T.Kwok,andQ.Yang,“DomainAdaptation
2007.
|                 |             |     |         |     |        |           |            | via | Transfer Component |     | Analysis,” | Proc. | 21st | Int’l Joint | Conf. |
| --------------- | ----------- | --- | ------- | --- | ------ | --------- | ---------- | --- | ------------------ | --- | ---------- | ----- | ---- | ----------- | ----- |
| [43] T. Jebara, | “Multi-Task |     | Feature | and | Kernel | Selection | for SVMs,” |     |                    |     |            |       |      |             |       |
ArtificialIntelligence,2009.
Proc.21stInt’lConf.MachineLearning,July2004.
|     |     |     |     |     |     |     |     | [68] M.M.H. | Mahmud | and | S.R. Ray, | “Transfer |     | Learning | Using |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | --- | --------- | --------- | --- | -------- | ----- |
[44] C. Wang and S. Mahadevan, “Manifold Alignment Using Kolmogorov Complexity: Basic Theory and Empirical Evalua-
| Procrustes |     | Analysis,” | Proc. | 25th Int’l | Conf. | Machine | Learning, |     |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | ----- | ---------- | ----- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
tions,”Proc.20thAnn.Conf.NeuralInformationProcessingSystems,
pp.1120-1127,July2008.
pp.985-992,2008.
| [45] N.D.   | Lawrence | and    | J.C. Platt, | “Learning |      | to Learn    | with the |                |                |     |          |          |              |     |           |
| ----------- | -------- | ------ | ----------- | --------- | ---- | ----------- | -------- | -------------- | -------------- | --- | -------- | -------- | ------------ | --- | --------- |
|             |          |        |             |           |      |             |          | [69] E. Eaton, | M. desJardins, |     | and      | T. Lane, | “Modeling    |     | Transfer  |
| Informative |          | Vector | Machine,”   | Proc.     | 21st | Int’l Conf. | Machine  |                |                |     |          |          |              |     |           |
|             |          |        |             |           |      |             |          | Relationships  | between        |     | Learning | Tasks    | for Improved |     | Inductive |
Learning,July2004. Proc. European Conf. Machine Learning and Knowledge
Transfer,”
[46] E. Bonilla, K.M. Chai, and C. Williams, “Multi-Task Gaussian DiscoveryinDatabases(ECML/PKDD’08),pp.317-332,Sept.2008.
Process Prediction,” Proc. 20th Ann. Conf. Neural Information [70] M.T.Rosenstein,Z.Marx,andL.P.Kaelbling,“ToTransferorNot
ProcessingSystems,pp.153-160,2008.
|     |     |     |     |     |     |     |     | to Transfer,” | Proc. | Conf. | Neural | Information |     | Processing | Systems |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | ----- | ------ | ----------- | --- | ---------- | ------- |
[47] A.Schwaighofer,V.Tresp,andK.Yu,“LearningGaussianProcess
(NIPS’05)WorkshopInductiveTransfer:10YearsLater,Dec.2005.
| Kernels | via | Hierarchical | Bayes,” | Proc. | 17th | Ann. | Conf. Neural | [71]         |     |              |     |             |      |             |     |
| ------- | --- | ------------ | ------- | ----- | ---- | ---- | ------------ | ------------ | --- | ------------ | --- | ----------- | ---- | ----------- | --- |
|         |     |              |         |       |      |      |              | S. Ben-David | and | R. Schuller, |     | “Exploiting | Task | Relatedness | for |
InformationProcessingSystems,pp.1209-1216,2005. Multiple Task Learning,” Proc. 16th Ann. Conf. Learning Theory,
[48] T. Evgeniou and M. Pontil, “Regularized Multi-Task Learning,” pp.825-830,2003.
Proc.10thACMSIGKDDInt’lConf.KnowledgeDiscoveryandData [72] B. Bakker and T. Heskes, “Task Clustering and Gating for
Mining,pp.109-117,Aug.2004.
|              |       |                |           |           |            |       |              | Bayesian     | Multitask      | Learning,” |     | J. Machine |     | Learning  | Research, |
| ------------ | ----- | -------------- | --------- | --------- | ---------- | ----- | ------------ | ------------ | -------------- | ---------- | --- | ---------- | --- | --------- | --------- |
| [49] J. Gao, | W.    | Fan, J. Jiang, | and       | J. Han,   | “Knowledge |       | Transfer via |              |                |            |     |            |     |           |           |
|              |       |                |           |           |            |       |              | vol.4,       | pp.83-99,2003. |            |     |            |     |           |           |
| Multiple     | Model | Local          | Structure | Mapping,” |            | Proc. | 14th ACM     | [73]         |                |            |     |            |     |           |           |
|              |       |                |           |           |            |       |              | A. Argyriou, | A.             | Maurer,    | and | M. Pontil, | “An | Algorithm | for       |
SIGKDD Int’l Conf. Knowledge Discovery and Data Mining, Transfer Learning in a Heterogeneous Environment,” Proc.
pp.283-291,Aug.2008. European Conf. Machine Learning and Knowledge Discovery in
[50] L. Mihalkova, T. Huynh, and R.J. Mooney, “Mapping and Databases(ECML/PKDD’08),pp.71-85,Sept.2008.
Proc.
Revising Markov Logic Networks for Transfer Learning,” [74] R.Raina,A.Y.Ng,andD.Koller,“ConstructingInformativePriors
22ndAssoc.fortheAdvancementofArtificialIntelligence(AAAI)Conf.
UsingTransferLearning,”Proc.23rdInt’lConf.MachineLearning,
ArtificialIntelligence,pp.608-614,July2007. pp.713-720,June2006.
[51] L. Mihalkova and R.J. Mooney, “Transfer Learning by Mapping [75] J.Yin,Q.Yang,andL.M.Ni,“AdaptiveTemporalRadioMapsfor
with Minimal Target Data,” Proc. Assoc. for the Advancement of IndoorLocationEstimation,”Proc.ThirdIEEEInt’lConf.Pervasive
Artificial Intelligence (AAAI ’08) Workshop Transfer Learning for ComputingandComm.,Mar.2005.
ComplexTasks,July2008.
[76] S.J.Pan,J.T.Kwok,Q.Yang,andJ.J.Pan,“AdaptiveLocalization
[52] J. Davis and P. Domingos, “Deep Transfer via Second-Order inaDynamicWiFiEnvironmentthroughMulti-ViewLearning,”
Markov Logic,” Proc. Assoc. for the Advancement of Artificial Proc.22ndAssoc.fortheAdvancementofArtificialIntelligence(AAAI)
Intelligence (AAAI ’08) Workshop Transfer Learning for Complex Conf.ArtificialIntelligence,pp.1108-1113,July2007.
Tasks,July2008. [77] V.W. Zheng, Q. Yang, W. Xiang, and D. Shen, “Transferring
[53] P.WuandT.G.Dietterich,“ImprovingSVMAccuracybyTraining Localization Models over Time,” Proc. 23rd Assoc. for the
onAuxiliaryDataSources,”Proc.21stInt’lConf.MachineLearning, Advancement of Artificial Intelligence (AAAI) Conf. Artificial Intelli-
| July2004. |     |     |     |     |     |     |     | gence,pp.1421-1426,July2008. |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 20:44:14 UTC from IEEE Xplore.  Restrictions apply.

| PANANDYANG: | ASURVEYONTRANSFERLEARNING |     |     |     |     |     |     |     |     |     | 1359 |
| ----------- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
[78] S.J. Pan, D. Shen, Q. Yang, and J.T. Kwok, “Transferring Sinno Jialin Pan received the MS and BS
Localization Models across Space,” Proc. 23rd Assoc. for the degrees from the Applied Mathematics Depart-
Advancement of Artificial Intelligence (AAAI) Conf. Artificial Intelli- ment, Sun Yat-sen University, China, in 2003
gence,pp.1383-1388,July2008. and2005,respectively.HeisaPhDcandidatein
| [79] |     |     |     |     |     |     |     | the Department | of Computer | Science | and |
| ---- | --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | ------- | --- |
V.W.Zheng,S.J.Pan,Q.Yang,andJ.J.Pan,“TransferringMulti-
Device Localization Models Using Latent Multi-Task Learning,” Engineering, the Hong Kong University of
Proc.23rdAssoc.fortheAdvancementofArtificialIntelligence(AAAI) ScienceandTechnology.Hisresearchinterests
Conf.ArtificialIntelligence,pp.1427-1432,July2008. includetransferlearning,semisupervisedlearn-
[80] H.Zhuo,Q.Yang,D.H.Hu,andL.Li,“TransferringKnowledge ing,andtheirapplicationsinpervasivecomput-
from Another Domain for Learning Action Models,” Proc. 10th ing and Web mining. He is a member of the
PacificRimInt’lConf.ArtificialIntelligence,Dec.2008. AAAI.Moredetailsabouthisresearchandbackgroundcanbefoundat
[81] V.C. Raykar, B. Krishnapuram, J. Bi, M. Dundar, and R.B. Rao, http://www.cse.ust.hk/~sinnopan.
| “Bayesian | Multiple | Instance | Learning: | Automatic | Feature | Selec- |     |     |     |     |     |
| --------- | -------- | -------- | --------- | --------- | ------- | ------ | --- | --- | --- | --- | --- |
tion and Inductive Transfer,” Proc. 25th Int’l Conf. Machine Qiang Yang received the bachelor’s degree
Learning,pp.808-815,July2008.
|     |     |     |     |     |     |     |     | from Peking | University | in astrophysics | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --------------- | --- |
[82] X. Ling, G.-R. Xue, W. Dai, Y. Jiang, Q. Yang, and Y. Yu, “Can the PhD degree in computer science from the
ChineseWebPagesbeClassifiedwithEnglishDataSource?”Proc. University of Maryland, College Park. He is a
17thInt’lConf.WorldWideWeb,pp.969-978,Apr.2008. faculty member in Hong Kong University of
[83] Q. Yang, S.J. Pan, and V.W. Zheng, “Estimating Location Using Science and Technology’s Department of
Wi-Fi,”IEEEIntelligentSystems,vol.23,no.1,pp.8-13,Jan./Feb.
|       |     |     |     |     |     |     |     | Computer         | Science and | Engineering. | His re- |
| ----- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ----------- | ------------ | ------- |
| 2008. |     |     |     |     |     |     |     | search interests | are data    | mining and   | machine |
[84] X. Shi, W. Fan, and J. Ren, “Actively Transfer Domain Knowl- learning, AI planning, and sensor-based activ-
edge,” Proc. European Conf. Machine Learning and Knowledge ity recognition. He is a fellow of the IEEE, a
DiscoveryinDatabases(ECML/PKDD’08),pp.342-357,Sept.2008. member of the AAAI and the ACM, a former associate editor for the
[85] G. Kuhlmannand P. Stone, “Graph-Based DomainMapping for IEEE Transactions on Knowledge and Data Engineering, and a
Transfer Learning in General Games,” Proc. 18th European Conf. current associate editor for the IEEE Intelligent Systems. More
MachineLearning,pp.188-200,Sept.2007. details about his research and background can be found at http://
[86] W. Dai, Y. Chen, G.-R. Xue, Q. Yang, and Y. Yu, “Translated www.cse.ust.hk/~qyang.
| Learning,” | Proc. | 21st Ann. | Conf. | Neural Information |     | Processing |     |     |     |     |     |
| ---------- | ----- | --------- | ----- | ------------------ | --- | ---------- | --- | --- | --- | --- | --- |
Systems,2008.
[87] B.Li,Q.Yang,andX.Xue,“TransferLearningforCollaborative
|           |       |               |            |         |       |            | . For more information | on this | or any other | computing | topic, |
| --------- | ----- | ------------- | ---------- | ------- | ----- | ---------- | ---------------------- | ------- | ------------ | --------- | ------ |
| Filtering | via a | Rating-Matrix | Generative | Model,” | Proc. | 26th Int’l |                        |         |              |           |        |
pleasevisitourDigitalLibraryatwww.computer.org/publications/dlib.
Conf.MachineLearning,June2009.
[88]
B.Li,Q.Yang,andX.Xue,“CanMoviesandBooksCollaborate?
| Cross-Domain |     | Collaborative | Filtering | for Sparsity | Reduction,” |     |     |     |     |     |     |
| ------------ | --- | ------------- | --------- | ------------ | ----------- | --- | --- | --- | --- | --- | --- |
Proc.21stInt’lJointConf.ArtificialIntelligence,July2009.
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 20:44:14 UTC from IEEE Xplore.  Restrictions apply.