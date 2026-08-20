IJCNN 2019. International Joint Conference on Neural Networks. Budapest, Hungary. 14-19 July 2019
Ensemble Application of Transfer Learning
and Sample Weighting for Stock Market Prediction
Simone Merello, Andrea Picasso Ratto, Luca Oneto Erik Cambria
DIBRIS, University of Genova SCSE, Nanyang Technological University
Via Opera Pia 11A, I-16145 Genova, Italy 50 Nanyang Ave, Singapore
{simone.merello, andrea.picasso}@smartlab.ws, luca.oneto@unige.it cambria@ntu.edu.sg
Abstract—Forecasting stock market behavior is an interesting Unfortunately, in the world of finance, writings can be
and challenging problem. Regression of prices and classifica- differentfromusualtext[17]thus,specializedtoolshavebeen
tion of daily returns have been widely studied with the main
developedstartingfromspecificdictionaries[17],[18]toword
goal of supplying forecasts useful in real trading scenarios.
embeddingscomputedoneconomicwritings,whosepretrained
Unfortunately, the outcomes are not directly related with the
maximization of the financial gain. Firstly, the optimal strategy version is publicly available [19].
requirestoinvestonthemostperformingasseteveryperiodand In the literature of stock market prediction, different ap-
tradingaccordinglyisnottrivialgiventhepredictions.Secondly, proaches have been used to supply market participants with
price fluctuations of different magnitude are often treated as
useful trading signals. Some work focus on the regression of
equals even if during market trading losses or gains of different
the stock’s future price [20], [21]. Other proposals focus on
intensitiesarederived.Inthispaper,theproblemofstockmarket
forecasting is formulated as regression of market returns. This the optimization of a monetary gain through the training of
approach is able to estimate the amount of price change and machine learning [22] models or through the construction of
thus the most performing assets. Price fluctuations of different a policy able to take investment decisions on the market [23].
magnitude are treated differently through the application of
Most of the recent works propose to map the trading
differentweightsonsamplesandthescarcityofdataisaddressed
decision of each asset in a binary classification task (either
using transfer learning. Results on a real simulation of trading
show how, given a finite amount of capital, the predictions can “buy” or “sell”). Some papers introduce specific new models
be used to invest in high performing stocks and, hence, achieve for the classification [24], [25], while others focus on natural
higher profits with less trades. language processing [26], [27] or on the class balancing
Index Terms—Financial forecasting, Stock market prediction
problem [28]. Ternary classification has been considered as
wellbyaddingathirdclassrepresentingthefinancialdecision
I. INTRODUCTION
“hold the current position” [10].
Thepotentialrevenueandthepossibleimpactonthesociety According to the Capital growth Theory [29], an optimal
ofaccuratestockmarketpredictionhasattractedinvestorsand strategy for the optimization of financial profits is to always
researchers since long time [1]. Nevertheless, its properties of invest the whole capital in the most performing stock of
time dependence, high stochasticity and chaotic behavior lead the next period. As a consequence, the outputs of a good
to a challenging problem. The Efficient market hypothesis [2] predictorshouldprovideanestimationofthemostperforming
states that stocks are always traded at their fair value but stocks in a set so that assets related to lower returns can be
behavioral economics tell us that emotions can profoundly disregarded during trading. Unfortunately, current approaches
affect individual behavior in financial decision making [3], are not directly related to the optimal strategy. Predicting the
[4]. Effects of emotions have been taken into account through futurepricesofastockdoesnotseemtobehelpfulsinceonly
technical analysis, exploiting the existence of patterns or the change (increase or decrease) in the values over time is
motifs that would repeat in the future due to the collective related to the profits.
attitude of investors [5]. Recent works focus on the extraction Classificationapproachesinsteadsupplysignalsregardinga
of sentiment related to the market from several sources of singlestockindependentlyfromtheotherassets.Theoutcomes
textual information, e.g., tweets [6], [7], microblogs [8], [9] of the predictions cannot be used as an estimation of the
and news articles [10], [11]. stock’s performance but two assets can be correctly predicted
In sentiment analysis research [12], sentences are decom- as “buy” even if the strength of their fluctuation differs
posed into concepts and targets of the opinion expressed [13]. significantly and investing the whole capital on the most
Vectorial representations of words are the starting point of performing would have generated higher returns.
many machine learning applications. As a consequence, sev- In this paper, the stock price prediction problem is formu-
eral algorithms have been designed to compute word vectors. lated as regression of market returns. The regression-based
GloVe[14]andWord2Vec[15]focusoncapturingthegeneral approach is able to estimate not only the direction but also
meaning and the relations between words while AffectiveS- the amount of the price change of each stock and thus the
pace [16] poses particular attention on concepts and opinions. most performing assets.
978-1-7281-2009-6/$31.00 ©2019 IEEE paper N-19019.pdf
Personal use is permitted, but republication/distribution requires IEEE permission.
AuthSoeriezehd tlitcpen:/se/dw uwsew li.mieiteeed. otor: gU/npivuebrslitiàc aBtoicocnosni.s Dtaownndloaarddesd/ opnu Jbulnice a1t7i,o2n02s6/ raitg 1h2t:1s2/:i1n0d UeTxC. hfrtomm lIEfEoEr Xmpolorree. i nRfeosrtrmictaiotniso anp.ply.

IJCNN 2019. International Joint Conference on Neural Networks. Budapest, Hungary. 14-19 July 2019
During market trading, investments on fluctuations of dif- The information available at time t relative to technical
ferentintensitieshavedifferentimpactsontheportfoliovalue. indicatorsandnewsarticlesisconsideredasleadingthetrends.
To address the issue, this paper discusses the application of The single news article published in t is encoded in a feature
differentweightsforeachdatapoint.Theresultsarecompared vector defined as n ∈ Rd. For each interval t, I ∈ Rf
|     |     |     |     |     |     |     |     |     |     | t   |     |     |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
with the formulation of the task as a binary classification represents the value of technical indicators computed over the
between ‘up’ and ‘down’ trends. In this setting, the problem recent past data and n ∈Rd+1 represents the aggregation of
t
ofunbalancedclassesisaddressedwithappropriatetechniques news published in the previous interval t∈[t−1,t)
during training and evaluation to avoid biased predictions. (cid:80)
n
With the purpose of generalizing the results, the two ap- t∈[t−1,t) t
|     |     |     |     |     |     |     |     |     |     | n t =[ |     |     | ,   | m t ] |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | ----- | --- | --- |
m
proaches are tested on several models which differ in input t
space and learning algorithm. Two different representations where m is the number of news in the considered interval
t
|            |             |     |       |     |                |      |        | and [·,·] | represents | the | concatenation |     | operation. |     |     |     |
| ---------- | ----------- | --- | ----- | --- | -------------- | ---- | ------ | --------- | ---------- | --- | ------------- | --- | ---------- | --- | --- | --- |
| of textual | information | are | used: | the | first is based | on a | simple |           |            |     |               |     |            |     |     |     |
toolspecificforfinance,thesecondisbasedonmorecomplex Thepotentialrelationoffuturepricefluctuationswithnews
but general purpose pretrained embeddings. Several widely articles is not limited only at the previous interval but time
|     |     |     |     |     |     |     |     | spans | of different | lengths | ending |     | in t are | considered | through |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | ------- | ------ | --- | -------- | ---------- | ------- | --- |
adoptedalgorithmsaretakeninaccount:Kernelsupportvector
| machine | (KSVM), | kernel | support | vector | regression |     | (KSVR) | n . |     |     |     |     |     |     |     |     |
| ------- | ------- | ------ | ------- | ------ | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t,wˆ
(cid:80)w ˆ − 1n
and feed forward neural network (FFNN). As a deep learning i = 0 t−i
|     |     |     |     |     |     |     |     |     |     |     | n t,wˆ = |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
approach, the latter requires huge amounts of data, especially wˆ
| in case of  | complex | relations |       | between | input        | and output | and      |       |     |          |            |     |      |         |     |     |
| ----------- | ------- | --------- | ----- | ------- | ------------ | ---------- | -------- | ----- | --- | -------- | ---------- | --- | ---- | ------- | --- | --- |
|             |         |           |       |         |              |            |          | Thus, | the | input of | the models | can | be   | defined | as: |     |
| significant | noise.  | This      | paper | shows   | how transfer |            | learning |       |     |          |            |     |      |         |     |     |
|             |         |           |       |         |              |            |          |       |     |          | x          | =[N | ,I ] |         |     |     |
techniquecanbeeffectivelyappliedonstockmarketprediction t t t
| so that a | single | model | is trained | on  | a bigger | dataset. |     |       |     |         |          |      |      |       |      |     |
| --------- | ------ | ----- | ---------- | --- | -------- | -------- | --- | ----- | --- | ------- | -------- | ---- | ---- | ----- | ---- | --- |
|           |        |       |            |     |          |          |     | where | N   | = [n ,n | ,n       | ,n   | ,n   | ,n ,n | ] in | the |
|           |        |       |            |     |          |          |     |       | t   | t       | t,5 t,10 | t,15 | t,20 | t,30  | t,50 |     |
Thefinalgoalofthisworkistoproposeanapproachwhose
experiments.
| predictions | can | be useful | in a | real scenario | of  | trading | where |           |     |        |         |             |     |               |     |      |
| ----------- | --- | --------- | ---- | ------------- | --- | ------- | ----- | --------- | --- | ------ | ------- | ----------- | --- | ------------- | --- | ---- |
|             |     |           |      |               |     |         |       | According |     | to the | problem | definition, |     | the collected |     | data |
answeringtothefinancialdecisionofwhichstockstotradein is considered as a time series of samples not independent
thecorrectmomentiscrucial.Forthisreason,usefulproperties
|     |     |     |     |     |     |     |     | (∃(i,j):p(x |     | j ,y j |x i ,y | i )(cid:54)=p(x | j ,y | j )).Inparticular,y |     | t implies |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------------- | --------------- | ---- | ------------------- | --- | --------- | --- |
areobservedusingdatasciencemetricsbutthefinalevaluation the existence of a temporal dependency such that (x ,y )
t t
is based on financial measures. is deterministically correlated with (x ,y ), v ∈ [0,w].
|          |        |       |              |     |             |         |     |     |     |     |     |     | t−v | t−v |     |     |
| -------- | ------ | ----- | ------------ | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| The rest | of the | paper | is organized |     | as follows: | Section |     | II  |     |     |     |     |     |     |     |     |
Particularcareistakenduringtheexperimentstoavoidbiased
formalizestheproblem;SectionIIIdefinestheapproach;Sec- results due to the dependency of samples.
| tion IV provides |        | an overview |     | of the       | collected | data; Section |     | V   |     |      |                  |     |     |     |     |     |
| ---------------- | ------ | ----------- | --- | ------------ | --------- | ------------- | --- | --- | --- | ---- | ---------------- | --- | --- | --- | --- | --- |
|                  |        |             |     |              |           |               |     |     |     | III. | PROPOSEDAPPROACH |     |     |     |     |     |
| explains in      | detail | experiments |     | and results; | finally,  | Section       | VI  |     |     |      |                  |     |     |     |     |     |
points out conclusions and future work. The main target of this work is to propose a regression
approachfortheproblemofreturnsforecastingwhosepredic-
II. PROBLEMFORMALIZATION
|                                            |     |     |     |     |     |           |     | tions                   | can be | used to     | invest | in high           | performing |              | assets during |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --------- | --- | ----------------------- | ------ | ----------- | ------ | ----------------- | ---------- | ------------ | ------------- | --- |
|                                            |     |     |     |     |     |           |     | markettrading.Thelabels |        |             | y      | indicatethechange |            |              | inthefuture   |     |
| Theproblemistimedependent.Thepredictionsyˆ |     |     |     |     |     | t aremade |     |                         |        |             |        | t                 |            |              |               |     |
|                                            |     |     |     |     |     |           |     | prices                  | of a   | given stock | and    | each              | input      | x summarizes |               | the |
at fixed and discretized time steps t relying on text published t
on dates identified as t. The labels y are defined according information derived by recent news and technical indicators
t
|                   |     |         |      |          |        |        |        | available | at  | time t. KSVR |     | and FFNN | algorithms |     | are applied |     |
| ----------------- | --- | ------- | ---- | -------- | ------ | ------ | ------ | --------- | --- | ------------ | --- | -------- | ---------- | --- | ----------- | --- |
| to the cumulative |     | returns | cr t | achieved | by the | market | during |           |     |              |     |          |            |     |             |     |
trends of length w to the regression problem. Support vector regression search
|     |     |     |     |     |     |     |     | the optimal |     | solution | through  | the minimization   |     | of  | the cost | L .      |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | -------- | ------------------ | --- | --- | -------- | -------- |
|     |     |     | p   | −p  |     |     |     |             |     |          |          |                    |     |     |          | (cid:15) |
|     |     |     |     | t+w | t   |     |     |             |     |          |          |                    |     |     |          |          |
|     |     | cr  | t = |     |     |     |     |             |     |          | (cid:88) |                    | 1   |     |          |          |
|     |     |     |     | p   |     |     |     |             |     | L        | =C       | (cid:96)(cid:15) + | ||w | ||2 |          |          |
|     |     |     |     | t   |     |     |     |             |     | (cid:15) |          | t                  | m   |     |          |          |
2
|           | R+  |     |          |       |         |      |       |     |     |     |     | t   |     |     |     |     |
| --------- | --- | --- | -------- | ----- | ------- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| where p t | ∈   | is  | the open | price | at time | step | t and |     |     |     |     |     |     |     |     |     |
cr ∈[−0.2,0.2]inourexperiments.Thetaskofstockmarket where C is a regularization parameter that controls the trade
t
prediction regards forecasting in t the change in the future off between the dimension of the model’s weights w and
m
|                                                        |     |     |     |     |     |     |     | (cid:96)(cid:15) =|y | −f(x | )| . The   | latter | measures | the | differences | bigger |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | -------------------- | ---- | ---------- | ------ | -------- | --- | ----------- | ------ | --- |
| stockpricesduring[t+1,t+1+w].Thereforefortheregression |     |     |     |     |     |     |     | t                    | t    | t (cid:15) |        |          |     |             |        |     |
problem, y can be defined as the value of the price change than (cid:15) between the truth y t and the output of the model
t
|     |     |     |     |     |     |     |     | f(x | ). In this | paper, | f(x | ) is computed |     | through | the use | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --- | ------------- | --- | ------- | ------- | --- |
|     |     |     |     |     |     |     |     | t   |            |        | t   |               |     |         |         |     |
y =cr
|           |                    |     | t    | t+1 |            |             |     | theGaussiankernel.Nonetheless,FFNNmodelsforregression |         |        |     |                  |     |         |         |     |
| --------- | ------------------ | --- | ---- | --- | ---------- | ----------- | --- | ----------------------------------------------------- | ------- | ------ | --- | ---------------- | --- | ------- | ------- | --- |
|           |                    |     |      |     |            |             |     | are often                                             | trained | using  | the | back propagation |     | of Mean | squared |     |
| while for | the classification |     | task | the | aim of the | predictions |     | is                                                    |         |        |     |                  |     |         |         |     |
|           |                    |     |      |     |            |             |     | error                                                 | (MSE)   | cost L | .   |                  |     |         |         |     |
m
| only on its | direction | (’up’ | or    | ‘down’) |     |     |     |     |     |            |            |           |       |        |     |     |
| ----------- | --------- | ----- | ----- | ------- | --- | --- | --- | --- | --- | ---------- | ---------- | --------- | ----- | ------ | --- | --- |
|             |           |       |       |         |     |     |     |     |     | 1 (cid:88) |            |           |       |        |     |     |
|             |           |       |       |         |     |     |     |     |     |            | (cid:96)m, | (cid:96)m |       | ))2    |     |     |
|             |           |       | =1(cr |         |     |     |     |     |     | L m =      |            |           | =(y t | −f(x t |     |     |
|             |           |       | y t   | t+1     | )   |     |     |     |     | n          | t          | t         |       |        |     |     |
t
1:R→{0,1}
where represents the unit step function. where n is the number of samples.
|     |     |     |     |     |     |     |     | - 2 - |     |     |     |     |     | paper | N-19019.pdf |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | ----- | ----------- | --- |
Authorized licensed use limited to: Università Bocconi. Downloaded on June 17,2026 at 12:12:10 UTC from IEEE Xplore.  Restrictions apply.

Ensemble Application of Transfer Learning and Sample Weighting for Stock Market Prediction
In the formulation of L and L all samples contribute
(cid:15) m
equally to the cost value but this assumption is not adequate
for stock market prediction. In market trading, the loss or
gain derived by financial decisions is not always equal but
depends on the value of the price fluctuations. With small
fluctuations such as 0.01%, even if the investment leads to a
decrease in the value of the portfolio, it would be marginal.
But, trading on high fluctuations is more risky because the
loss or the gain derived can be considerable. In the proposed
regressionexperiments,samplesareweightedaccordingtothe
price changes cr so that data points related to bigger returns
t
contribute more to the cost value, thus are considered more
important by the models. In particular, the weighted costs are
defined as:
(cid:96)w(cid:15) =cr2·(cid:96)(cid:15), (cid:96)wm =cr2·(cid:96)m
t t t t t t
andareusedrespectivelyinsteadof(cid:96)(cid:15),(cid:96)m fortheoptimization
t t
process. Moreover, (cid:96)wm is used during model selection with
t
the purpose of choosing the best values for the hyperparame-
ters of the regressors.
The results are compared with a classification approach Fig. 1. FFNN architecture used for the experiments. The last layer is the
pursued through similar models. KSVM is used to select onlyoneaffectedbytransferlearningandhisactivationfunctionistheonly
changeinthestructurebetweenclassificationandregressiontask.
the optimal maximum-margin hyperplane that separates the
classes while FFNN algorithm is optimized through the back
propagation of the binary cross entropy cost. In this setting,
Instead, the regression task is pursued through the Hyper-
balancingtheclassesisfundamentaltoavoidbiasedresults.In
bolic activation tanh(·) ∈ [−1,1]. The latter is considered
accordancewith[28],SMOTEalgorithm[30]isappliedonthe
reasonable since it behaves linearly in the domain of the
training and validation set since weights or hyperparameters
regression labels y = cr ∈ [−0.2,0,2]. Furthermore,
optimized on screwed classes often lead to predictions biased t t+1
tanh(·) is used to infer the prior knowledge that predictions
towards the most frequent class. For the same reason, the
above |yˆ|>1 must be avoided since these are not likely and
modelselectionofclassifiersisheldwithMatthewcorrelation t
the trading decision derived would be the same.
coefficient (MCC).
The last layer is the only one affected by transfer learning.
tp·tn−fp·fn
MCC = Firstly, a single FFNN is trained over different stocks to cap-
(cid:112)
(tp+fp)(tp+fn)(tn+fp)(tn+fn) ture the general relations between news, technical indicators
where tp: True positive, fp: False positive, tn: True negative, and price fluctuations. Training a model over multiple stocks
fn: False negative extracted from the Confusion matrix. implies the assumption that the samples behave similarly and
The architecture of the FFNN is depicted in Fig. 1. Four are drawn from the same distribution. This assumption is
dense layers are applied whose parameters were trained with considered feasible since the features x t are made up of the
Adam optimizer [31] algorithm. In each layer, batch nor- sametechnicalindicatorsandnewspublishedbysamesources.
malization [32] is inserted to stabilize the distribution of the Moreover, y t , defined in accordance with the returns cr t , can
internal representation of samples and speed up the training be considered related to the same market portfolio returns
phase. in accordance to Capital asset pricing model theorem [34].
Batch normalization guarantees to output samples dis- Secondly, the model is fine tuned on the specific stocks
tributed with mean zero and unit variance so that the pa- separately since some alteration between news of different
rameters of the next layer are not required to adapt to the companies are expected, e.g., “AAPL” news will probably
changing distribution of the input during training. In the first more related to words such as “Apple”, “iPhone” and “Tim
three layers, the normalized samples are directly fed into a Cook” with respect to “FB”.
Leaky ReLu activation function. Dropout [33] is applied on Our experiments propose two different settings from
the output of the first and the second layer together with the the point of view of the input. Firstly, a representation
use of Max-norm regularization over all layers to avoid co- of each news article n is obtained through the use of
t
adaptationofneuronsandimprovingthegeneralizationpower Loughran/McDonald dictionary as it represents a simple
of the network. The activation function of the last layer is source specific for finance. Secondly, the concepts present
the only change in the structure between classification and in news articles are extracted and used with AffectiveSpace
regression task. The Sigmoid function σ(·)∈[0,1] is selected to obtain a representation of the concept-related sentiment
to perform the classification. contained inside the financial writings.
- 3 - paper N-19019.pdf
Authorized licensed use limited to: Università Bocconi. Downloaded on June 17,2026 at 12:12:10 UTC from IEEE Xplore. Restrictions apply.

IJCNN 2019. International Joint Conference on Neural Networks. Budapest, Hungary. 14-19 July 2019
The results are evaluated in three steps on a set of different TABLEI
stocks. Firstly, the length w of the trend cr is chosen TECHNICALANALYSISINDICATORS
t
accordingly to the best average performance of the models.
Name Formula
Secondly, The behavior of the two approaches in predicting
fluctuations of increasing strength is discussed. Momentum pt −1
pt−s
A threshold is applied to consider Accuracy and MCC SMA pt −1
metrics over [100%,80%,60%,40%,20%] of returns accord- 
pt,s
ing to their intensity. The evaluation over different subsets  1 if p t >ub t b
is necessary since a model that has low performance on Bollinger Bands 0 if p t ∈[ub t b,db t b]
small fluctuations but good results on higher returns can

−1 if p <dbb
t t
lead to considerable profits. Finally, the performance of the
Differentiated v v −v
t t t
predictions is tested with a trading simulation performed with
a specific tool1.
Aninvestmentstrategyisconsideredthroughtheapplication
Different features were extracted from the raw data. For
ofthresholdsonthevalueofthepredictions.Stocksarebought
whatconcernstechnicalanalysis,theextractionofmeaningful
orsoldintonlyiftheassociatedvalueisabovethethreshold.
values from past prices p and volumes v is complicated by
Since at time step t all the previous predictions are available, t t
the non-stationarity of these. Therefore, several differentiated
thetradingactionsintarebasednotonlyonthepredictionsin
metrics computed on the recent past were used as measures
t but also on the previous k values [yˆ,yˆ ,..,yˆ ] through
t t−1 t−k of the changes in the past financial values. I ∈Rf (f =10)
a simple average. Considering multiple predictions represents t
wasmadeupofMomentumindicator,Simplemovingaverage
acarefulbehaviorwhichavoidsfinancialdecisionsbasedonly
(SMA)basedontheaveragevalueofthepreviousspricesp ,
ononesignal.k isempiricallychosenas2intheexperiments. t,s
Bollinger Bands [ubb,dbb] crossing signal and a differentiated
Sharperatio[35]andAnnualizedgainareexaminedasresults t t
measure of v based on the average of the previous values v .
of the trading performance. t t
In the experiments, s was chosen as s∈{30,50,100,150}.
Different representations for the news n were considered.
IV. AVAILABLEDATA t
Firstly, features were extracted using the Loughran/McDonald
In this section, the two kinds of data used for the experi- dictionary [17]. It was constructed on annual reports of US
ments are described: stock data and textual data. The problem enterprises considering also companies quoted in NASDAQ
of stock market forecasting was mapped to the prediction and since the focus of this work is on the same market, it was
of the price movements of the top 10 stocks in capital considered highly related to our task.
size of NASDAQ, respectively ‘AAPL’, ‘AMZN’, ‘GOOGL’, The dictionary includes positive, negative, litigious,
‘MSFT’, ‘FB’, ‘INTC’, ‘CSCO’, ‘CMCSA’, ‘NVDA’ and interesting, uncertainty and other categories of words specific
‘NFLX’.Previousworkhadalreadyfocusedonsimilarexper- for finance and recently updated. Accordingly, n ∈ Rd
t
iments [24]. Some of the stocks traded there are well known was made up of numerical counts of the words spotted
fortheirpopularityandconsequentlyahugeamountoftextual in a news belonging to the different categories of the
information regarding them is constantly published. dictionary (d=7). Secondly, n was defined according to the
t
Textual data were extracted from aggregated news services embeddings of AffectiveSpace to obtain a representation of
that gather the information from various professional periodi- the concept-oriented sentiment contained in financial writings
cals2,3. The stock prices were collected from public sources4 (d = 100). The news articles were parsed to retrieve the
and only the periods in which the market was open were con- contained concepts and the AffectiveSpace embeddings of
sideredastimestepst.Thetimespanbetweentwosubsequent different concepts found in a news were averaged to obtain
samples was selected as hourly. One hour represented a lower its representation.
bound from the point of view of the available news published
for each time step and allowed the creation of a significant
amount of samples for the experiments.
V. EXPERIMENT
The information regarding prices and published news of A. Experiment Setup
all the selected stocks was available during the time span
Model selection was performed using cross validation on
considered. Approximately eleven months of data were used
time dependent data. As depicted in Fig. 2, the folds were
for training, from 2017-04-03 to 2018-02-23 and four months
selected so that the last fold took into account all the training
were used for testing, from 2018-02-24 to 2018-06-21.
points, but the validation points were left out to ensure the
temporal independence between Train and Test.
In our experiments, points used for evaluation were always
1http://backtrader.com
chosen ahead the training set in time so that a possible look
2http://finance.yahoo.com
3http://nasdaq.com/news aheadbiaswasavoidedsincetheinformationcontainedinthe
4http://finance.google.com/finance past samples cannot depend on the future.
- 4 - paper N-19019.pdf
Authorized licensed use limited to: Università Bocconi. Downloaded on June 17,2026 at 12:12:10 UTC from IEEE Xplore. Restrictions apply.

Ensemble Application of Transfer Learning and Sample Weighting for Stock Market Prediction
FortheFFNNmodels,thenumberofepochsoftrainingwas
considered as an hyperparameter optimized on the validation
set during model selection. The computation of the optimal
value involved only the last fold since the dimension of the
others was different from the training set used for testing.
In a first test Accuracy and MCC achieved by the models
were evaluated on average above all the considered stocks.
Averaging on different stocks from the finance point of view
means considering the overall performance of the predictions
over a portfolio of different financial assets as if earnings
or losses were obtained by all of them betting on their
performance.Furthermore,consideringdifferentstocksappear
fundamental to generalize the result and to avoid specific
conclusions for the single stock.
A second test was performed to evaluate the predictions in
a real trading simulation. The output of the trading simulation
depended on the selection of which stocks to trade (trading
Fig.3. MCCvaluesaveragedoverthetestedmodels.Differentexperiments
strategy) but also from the the amount of capital to invest in
regard the prediction of different trends crt. Trends lasting 1 hour, 1, 4, 5
each trade (sizing strategy). The trading strategy was defined and7daysareevaluated.
according to the trading signal s computed as average of the
t
last three predictions s =
1(cid:80)2
yˆ . A threshold T was
t 3 i=0 t−i
used to trade only on the most performing stocks for which According to Fig. 3, the MCC value relative to the trend
|s |>T. Every trade started in t lasted until time step t+w length of seven trading days (49 hours) achieved the best
t
accordingly to the prediction target. The sizing strategy was score. This result is considered significant since most of the
selectedsothatgiventheportfoliovalueP eachtimesteptan state-of-the-art papers on return classification focus on daily
t
a th m e o n u u n m t b w e · P r n t a o , f t a w ct a i s on in s v ( e b s u t y ed or on se t l h l) e s s u i g n g g e le ste a d ss b et y . t n h a e ,t m d o e d n e o l te in s t r r e e s n u d lts p o re f d t i h c i t s io e n xp [ e 1 r 0 im ], e [ n 2 t 4 h ] ig w h i l t i h g o h u t t th a a p t r d o a p il e y r p e r x e p d l i a c n t a io ti n on is . s T u h b e -
t. Thus, if in t many stocks are traded, only a small amount optimal with respect to other choices of the trend length.
of capital can be invested in each asset. According to the average performance of the tested mod-
A commission rate of 0.01% was considered and the risk els, predicting trends lasting seven or four days allowed
free rate required by the computation of the Sharpe ratio was approximately to double the MCC score (0.084 and 0.074,
setastheinterestrateofthree-monthU.S.Treasurybillinthe respectively) in comparison to the daily prediction (MCC
period of evaluation. 0.042). For the rest of the experiments, the trend length at
seven open market days was used for the evaluations.
B. Optimal trend classification
Thedefinitionofthelabelsy dependonthelengthwofthe C. Comparison Regression-Classification
t
trendcr consideredthus,ourfirstachievementwasneededto
t The comparison between regression and classification ap-
fix an optimal value for it. Several experiments were done to
proachwasdividedintwosteps.Duringthefirststep,thecom-
predict in t trends startingat t+1 and ending [1,7,28,35,49]
parison was held on MCC and Accuracy scores computed on
hours later.
differentsubsetsoffluctuations.Athresholdwasusedtoselect
That means, predicting the trend of the next hour, the next
onlythehighestreturns,respectivelydifferentevaluationstook
tradingdaybutalsothenextfour,fiveandseventradingdays.
inaccountthe100%80%,60%,40%,and20%ofthehighest
The optimal window was selected according to the average
returns. To highlight the tendency of the evaluation scores,
MCC score achieved by all models described in Section III.
Fig. 4 shows the evaluation metrics computed considering the
valuerelativetothe100%ofreturnssetaszeroandsubtracted
from the other results. Fig. 5 shows the MCC and Accuracy
metrics.
During the second step, the predictions of the models were
usedinatradingsimulationandwereevaluatedusingfinancial
measures. The Annualized gain and the Sharpe ratio were
computed considering to perform buy or sell actions in t only
if the trading signal s was bigger than a threshold |s |>T.
t t
T represents the threshold set so that in different experiments
the100%80%,60%,40%,and20%ofthehighestpredictions
Fig.2. Datasetdivision. were taken in account for trading.
- 5 - paper N-19019.pdf
Authorized licensed use limited to: Università Bocconi. Downloaded on June 17,2026 at 12:12:10 UTC from IEEE Xplore. Restrictions apply.

IJCNN 2019. International Joint Conference on Neural Networks. Budapest, Hungary. 14-19 July 2019
Fig.4. MCCandAccuracyvaluesofthemodelsareevaluatedondifferent
| subsets of | the returns. | Dashed | lines | represent | classification |     | models while |     |     |     |     |     |     |     |     |
| ---------- | ------------ | ------ | ----- | --------- | -------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
continuouslinesarerelativetoregressionmodels.
| Fig. 6    | shows    | the evaluation |          | metrics | computed    |     | considering |     |     |     |     |     |     |     |     |
| --------- | -------- | -------------- | -------- | ------- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| the value | relative | to             | the 100% | of      | predictions | set | as zero and |     |     |     |     |     |     |     |     |
subtractedfromtheotherresults.Fig.7showstheAnnualized
| gain and        | the Sharpe |        | ratio. |               |      |                |             |     |     |     |     |     |     |     |     |
| --------------- | ---------- | ------ | ------ | ------------- | ---- | -------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| For what        | concerns   |        | MCC    | and Accuracy, |      | Fig.           | 4 shows how |     |     |     |     |     |     |     |     |
| the performance |            | of the | models | trained       | with | the regression | ap-         |     |     |     |     |     |     |     |     |
proachincreasedconsideringhigherfluctuations.Nonetheless,
| this property | seems | to  | hold | with only | one | model | trained with |     |     |     |     |     |     |     |     |
| ------------- | ----- | --- | ---- | --------- | --- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
theclassificationapproach.AccordingtoFig.5,theMCCand
| Accuracy     | values       | computed |             | on the      | whole | returns        | (100%) were   |     |     |     |     |     |     |     |     |
| ------------ | ------------ | -------- | ----------- | ----------- | ----- | -------------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| often higher | for          | the      | classifiers | rather      | than  | the            | values of the |     |     |     |     |     |     |     |     |
| regressors.  | Augmenting   |          | the         | threshold   | and   | thus           | considering   |     |     |     |     |     |     |     |     |
| only higher  | fluctuations |          | the         | performance |       | of models      | trained       |     |     |     |     |     |     |     |     |
| with the     | regression   | approach |             | increased   |       | and frequently | over-         |     |     |     |     |     |     |     |     |
cometheclassificationscores.Itisopinionoftheauthorsthat
| the application |     | of weights | to        | samples | proportional    |     | to cr t was |     |     |     |     |     |     |     |     |
| --------------- | --- | ---------- | --------- | ------- | --------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| fundamental     | to  | feed       | the model |         | the information |     | that higher |     |     |     |     |     |     |     |     |
fluctuationsweremoreimportantandthus,toachieveagrowth Fig.5. MCCandAccuracyvaluesofthebenchmarkedmodelsevaluatedon
differentsubsetsofthereturns.
| on the performance |                    | relative |             | to higher | fluctuations.   |           |             |        |              |     |           |      |     |         |           |
| ------------------ | ------------------ | -------- | ----------- | --------- | --------------- | --------- | ----------- | ------ | ------------ | --- | --------- | ---- | --- | ------- | --------- |
| During             | the trading        |          | simulation, |           | the differences |           | between re- |        |              |     |           |      |     |         |           |
|                    |                    |          |             |           |                 |           |             | In our | experiments, |     | the model | able | to  | achieve | best per- |
| gression           | and classification |          | approach    |           | were            | even more | stressed.   |        |              |     |           |      |     |         |           |
Fig.6showshowtheperformanceofregressorsincreasedtrad- formance from both the points of view of Sharpe ratio and
|                       |           |              |     |              |      |        |             | Annualized | gain   | was             | the FFNN | that | exploited  | the      | features |
| --------------------- | --------- | ------------ | --- | ------------ | ---- | ------ | ----------- | ---------- | ------ | --------------- | -------- | ---- | ---------- | -------- | -------- |
| ing only              | on higher | predictions. |     | Nonetheless, |      | the    | performance |            |        |                 |          |      |            |          |          |
|                       |           |              |     |              |      |        |             | extracted  | though | AffectiveSpace, |          | the  | regression | approach | and      |
| of the classification |           | approach     |     | increased    | less | or not | at all.     |            |        |                 |          |      |            |          |          |
During a generic time step t, the optimal investment and that was trained through transfer learning. The application of
|                 |              |        |            |                    |            |               |              | this technique | is  | discussed | in  | the next | Section. |     |     |
| --------------- | ------------ | ------ | ---------- | ------------------ | ---------- | ------------- | ------------ | -------------- | --- | --------- | --- | -------- | -------- | --- | --- |
| sizing strategy |              | would  | bet        | the whole          | capital    |               | on the stock |                |     |           |     |          |          |     |     |
| corresponding   |              | to the | highest    | future             | return.    | The           | regression   |                |     |           |     |          |          |     |     |
| models          | were able    | to     | supply     | an                 | estimation | of            | the strength |                |     |           |     |          |          |     |     |
| of the          | fluctuation  | thus,  | augmenting |                    | the        | threshold     | over the     |                |     |           |     |          |          |     |     |
| predictions     | allowed      | to     | select     | more               | carefully  | on            | which stocks |                |     |           |     |          |          |     |     |
| to trade.       | Since        | during | the        | trading            | simulation | the           | amount of    |                |     |           |     |          |          |     |     |
| capital         | was limited, |        | trading    | on less            | stocks     | implied       | to invest    |                |     |           |     |          |          |     |     |
| more on         | the single   | stock  | that       | the                | regressor  | models        | estimated    |                |     |           |     |          |          |     |     |
| as the most     | valuable.    |        | With       | the classification |            | approach      | instead,     |                |     |           |     |          |          |     |     |
| this behavior   |              | could  | not be     | exploited          |            | since, higher | values       |                |     |           |     |          |          |     |     |
| of the          | predictions  | were   | not        | necessarily        |            | related       | with higher  |                |     |           |     |          |          |     |     |
| fluctuations    | thus,        | during | trading    | classification     |            | models        | did not      |                |     |           |     |          |          |     |     |
supplyenoughinformationtochoosethemostworthstocksin
|     |     |     |     |     |     |     |     | Fig. 6. The | Annualized | gain | and | the Sharpe | ratio | of the trading | simula- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ---- | --- | ---------- | ----- | -------------- | ------- |
whichtoinvest.AsdepictedinFig.7,thehighestSharperatio
tionsconsideringdifferentsubsetsofthepredictions.Dashedlinesrepresent
| and the | three highest |     | annualized |     | gains achieved |     | were related |     |     |     |     |     |     |     |     |
| ------- | ------------- | --- | ---------- | --- | -------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
classificationmodelswhilecontinuouslinesarerelativetoregressionmodels.
| to the regression |     | approach. |     |     |     |     |     |       |     |     |     |     |     |       |             |
| ----------------- | --- | --------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | ----- | ----------- |
|                   |     |           |     |     |     |     |     | - 6 - |     |     |     |     |     | paper | N-19019.pdf |
Authorized licensed use limited to: Università Bocconi. Downloaded on June 17,2026 at 12:12:10 UTC from IEEE Xplore.  Restrictions apply.

Ensemble Application of Transfer Learning and Sample Weighting for Stock Market Prediction
|     |     |     |     |     |     |     | For all         | the       | models           | that used      | transfer | learning,      |             | the optimal   |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --------- | ---------------- | -------------- | -------- | -------------- | ----------- | ------------- |
|     |     |     |     |     |     |     | number          | of epochs | of               | training       | was      | estimated      | as          | 0 for several |
|     |     |     |     |     |     |     | stocks.         | Thus,     | fine-tuning      | of             | these    | stocks         | was         | not helpful   |
|     |     |     |     |     |     |     | in increasing   |           | the performance  |                | on       | the validation |             | set but the   |
|     |     |     |     |     |     |     | optimal         | minimum   | was              | reached        | with     | the            | model       | trained over  |
|     |     |     |     |     |     |     | all the stocks. |           |                  |                |          |                |             |               |
|     |     |     |     |     |     |     | To quantify     |           | the contribution |                | of the   | transfer       | learning    | on the        |
|     |     |     |     |     |     |     | problem         | of stock  | market           | prediction     |          | an additional  |             | experiment    |
|     |     |     |     |     |     |     | was based       | on        | the model        | that           | achieved |                | the highest | trading       |
|     |     |     |     |     |     |     | results.        | Two FFNN  |                  | AffectiveSpace |          | regressors     |             | trained with  |
|     |     |     |     |     |     |     | and without     | transfer  |                  | learning       | were     | compared.      |             | Since in this |
experimentthefinancialdecisionwasnotthemaininterestand
theevaluatedmodelswerebasedonregression,thecomparison
|     |     |     |     |     |     |     | was based | on       | the Normalized |                | MSE.      | Fig.      | 8 shows | how using   |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | -------------- | -------------- | --------- | --------- | ------- | ----------- |
|     |     |     |     |     |     |     | transfer  | learning | FFNN           | AffectiveSpace |           | regressor |         | was able to |
|     |     |     |     |     |     |     | achieve   | better   | performance    |                | improving | on        | all the | considered  |
|     |     |     |     |     |     |     | subsets   | of the   | returns.       |                |           |           |         |             |
Fig.7. AnnualizedgainandSharperatiovaluesofthebenchmarkedmodels
evaluatedondifferentsubsetsofthereturns.
| D. Transfer | learning | evaluation |               |           |           |     |                                                                  |     |     |     |     |     |     |     |
| ----------- | -------- | ---------- | ------------- | --------- | --------- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|             |          |            |               |           |           |     | Fig.8. NormalizedmeansquareerroroftheFFNNAffectiveSpaceregressor |     |     |     |     |     |     |     |
| Transfer    | learning | can        | be considered | effective | if during | the |                                                                  |     |     |     |     |     |     |     |
withandwithouttransferlearning.Resultsareevaluatedondifferentsubsets
ofthereturns.
| pretraining  | phase      | the model       | is able | to reach    | a good minimum |      |     |     |     |     |     |     |     |     |
| ------------ | ---------- | --------------- | ------- | ----------- | -------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| which result | a          | useful starting | point   | for further | optimization   |      |     |     |     |     |     |     |     |     |
| process      | during the | fine-tuning.    | Table   | II shows    | for each       | FFNN |     |     |     |     |     |     |     |     |
and for each stock the number of epochs of fine-tuning VI. CONCLUSIONANDDISCUSSION
| optimized | on the | validation | set in | the range | [0,200]. |     |           |        |            |          |      |                 |            |            |
| --------- | ------ | ---------- | ------ | --------- | -------- | --- | --------- | ------ | ---------- | -------- | ---- | --------------- | ---------- | ---------- |
|           |        |            |        |           |          |     | In this   | paper, | we have    | shown    | that | the predictions |            | of returns |
|           |        |            |        |           |          |     | generated | by a   | regression | approach |      | are more        | meaningful | with       |
TABLEII
NUMBEROFEPOCHSOFFINE-TUNINGFOREACHSTOCKOFTHEFFNNS respect to ‘buy’ or ‘sell’ signals provided by classification
MODELS,RESPECTIVELYCLASSIFICATIONANDREGRESSIONAPPROACHES approachesduringtrading.Thisgapofinformationcanbeused
WITHFEATURESBASEDONAFFECTIVESPACE(AS)AND
|     |     |     |     |     |     |     | to augment | financial |     | profits | through | an  | investment | strategy |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | ------- | ------- | --- | ---------- | -------- |
LOUGHRAN/MCDONALDDICTIONARY(LM-DICT).
|     |     |                |     |            |     |     | able to | focus only | on  | the most | performing |     | assets. |     |
| --- | --- | -------------- | --- | ---------- | --- | --- | ------- | ---------- | --- | -------- | ---------- | --- | ------- | --- |
|     |     | classification |     | regression |     |     |         |            |     |          |            |     |         |     |
Accordingtoourresults,theapplicationoftransferlearning
|     |       | AS  | LM-Dict | AS LM-Dict |     |     |                |           |            |             |              |        |              |              |
| --- | ----- | --- | ------- | ---------- | --- | --- | -------------- | --------- | ---------- | ----------- | ------------ | ------ | ------------ | ------------ |
|     |       |     |         |            |     |     | and sample     | weighting |            | over        | different    | market | fluctuations | has          |
|     | AAPL  | 0   | 14      | 200        | 0   |     |                |           |            |             |              |        |              |              |
|     |       |     |         |            |     |     | been effective |           | to enhance | the         | performance, |        | especially   | on the       |
|     | AMZN  | 0   | 200     | 79         | 200 |     |                |           |            |             |              |        |              |              |
|     |       |     |         |            |     |     | biggest        | and most  | important  |             | returns.     |        |              |              |
|     | GOOGL | 0   | 44      | 19         | 0   |     |                |           |            |             |              |        |              |              |
|     |       |     |         |            |     |     | Our paper      | does      | not        | contemplate |              | some   | aspects      | that will be |
|     | MSFT  | 0   | 54      | 200        | 0   |     |                |           |            |             |              |        |              |              |
FB 149 0 200 0 undertakeninfutureresearch.Firstly,theapplicationofsample
INTC 26 0 32 0 weights should be studied more in depth starting from their
|     | CSCO | 185 | 173 | 190 | 200 |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
applicationwiththeclassificationapproachtoacomparisonof
|     | CSMA | 29  | 0   | 0   | 47  |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
differentformulations.Secondly,thebenefitsoftheregression
|     | NVDA | 200 | 24  | 0   | 0   |     |          |        |                |     |     |                  |     |         |
| --- | ---- | --- | --- | --- | --- | --- | -------- | ------ | -------------- | --- | --- | ---------------- | --- | ------- |
|     |      |     |     |     |     |     | approach | should | be benchmarked |     | on  | state-of-the-art |     | methods |
|     | NFLX | 193 | 55  | 0   | 200 |     |          |        |                |     |     |                  |     |         |
tobetterquantifytheimprovementsoftheproposedtechnique.
|     |     |     |     |     |     | -   | 7 - |     |     |     |     |     | paper | N-19019.pdf |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----------- |
Authorized licensed use limited to: Università Bocconi. Downloaded on June 17,2026 at 12:12:10 UTC from IEEE Xplore.  Restrictions apply.

IJCNN 2019. International Joint Conference on Neural Networks. Budapest, Hungary. 14-19 July 2019
REFERENCES
|     |     |     |     |     |     | [19] P. Saleiro, | E.  | M. Rodrigues, |            | C. Soares, | and E.   | Oliveira,     | “Feup at |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------- | ---------- | ---------- | -------- | ------------- | -------- |
|     |     |     |     |     |     | semeval-2017     |     | task 5:       | Predicting | sentiment  | polarity | and intensity | with     |
[1] F.Xing,E.Cambria,andR.Welsch,“Naturallanguagebasedfinancial
financialwordembeddings,”arXivpreprintarXiv:1704.05091,2017.
forecasting:Asurvey,”ArtificialIntelligenceReview,vol.50,no.1,pp.
49–73,2018. [20] P.-F. Pai and C.-S. Lin, “A hybrid arima and support vector machines
modelinstockpriceforecasting,”Omega,vol.33,no.6,pp.497–505,
[2] E.F.Fama,“Efficientcapitalmarkets:Areviewoftheoryandempirical
2005.
work,”ThejournalofFinance,vol.25,no.2,pp.383–417,1970.
[3] G.Loewenstein,“Emotionsineconomictheoryandeconomicbehavior,”
[21] A.A.Adebiyi,A.O.Adewumi,andC.K.Ayo,“Comparisonofarima
Americaneconomicreview,vol.90,no.2,pp.426–432,2000. andartificialneuralnetworksmodelsforstockpriceprediction,”Journal
[4] F. Xing, E. Cambria, L. Malandri, and C. Vercellis, “Discovering ofAppliedMathematics,vol.2014,2014.
bayesianmarketviewsforintelligentassetallocation,”inECML,2018.
|     |     |     |     |     |     | [22] Y. Bengio, | “Training |     | a neural | network with | a financial | criterion | rather |
| --- | --- | --- | --- | --- | --- | --------------- | --------- | --- | -------- | ------------ | ----------- | --------- | ------ |
[5] C.-H. Parkand S. H. Irwin,“The profitability of technicalanalysis: A than a prediction criterion,” in Decision Technologies for Financial
review,”AgMASProjectResearchReport2004-04,2004.
|                |         |                       |     |               |           | Engineering: |          | Proceedings | of the  | Fourth  | International | Conference | on         |
| -------------- | ------- | --------------------- | --- | ------------- | --------- | ------------ | -------- | ----------- | ------- | ------- | ------------- | ---------- | ---------- |
| [6] J. Bollen, | H. Mao, | and X. Zeng, “Twitter |     | mood predicts | the stock |              |          |             |         |         |               |            |            |
|                |         |                       |     |               |           | Neural       | Networks | in the      | Capital | Markets | (NNCM’96),    | World      | Scientific |
market,”Journalofcomputationalscience,vol.2,no.1,pp.1–8,2011.
Publishing,1997,pp.36–48.
| [7] F. Xing, | E. Cambria, | and R. Welsch, | “Intelligent | asset | allocation via |     |     |     |     |     |     |     |     |
| ------------ | ----------- | -------------- | ------------ | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[23] J.W.Lee,“Stockpricepredictionusingreinforcementlearning,”inIn-
| market | sentiment views,” | IEEE Computational |     | Intelligence | Magazine, |     |     |     |     |     |     |     |     |
| ------ | ----------------- | ------------------ | --- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
vol.13,no.4,pp.25–34,2018. dustrialElectronics,2001.Proceedings.ISIE2001.IEEEInternational
[8] S. R. Das and M. Y. Chen, “Yahoo! for amazon: Sentiment extraction Symposiumon,vol.1. IEEE,2001,pp.690–695.
from small talk on the web,” Management science, vol. 53, no. 9, pp. [25] T.H.NguyenandK.Shirai,“Topicmodelingbasedsentimentanalysis
onsocialmediaforstockmarketprediction,”inAnnualMeetingofthe
1375–1388,2007.
|     |     |     |     |     |     | Association | for | Computational |     | Linguistics | and the | International | Joint |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ------------- | --- | ----------- | ------- | ------------- | ----- |
[9] L.Malandri,F.Xing,C.Orsenigo,C.Vercellis,andE.Cambria,“Public
mood–driven asset allocation: the importance of financial sentiment in ConferenceonNaturalLanguageProcessing,2015.
portfoliomanagement,”CognitiveComputation,2019.
|     |     |     |     |     |     | [26] V. S. | Pagolu, | K. N. | Reddy, | G. Panda, | and B. | Majhi, | “Sentiment |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | ----- | ------ | --------- | ------ | ------ | ---------- |
[10] Z. Hu, W. Liu, J. Bian, X. Liu, and T. Y. Liu, “Listening to chaotic analysis of twitter data for predicting stock market movements,” in
whispers: A deep learning framework for news-oriented stock trend InternationalConferenceonSignalProcessing,Communication,Power
prediction,”inACMInternationalConferenceonWebSearchandData
andEmbeddedSystem,2016.
Mining,2018.
|     |     |     |     |     |     | [27] Y. Peng | and H. | Jiang, | “Leverage | financial | news | to predict | stock price |
| --- | --- | --- | --- | --- | --- | ------------ | ------ | ------ | --------- | --------- | ---- | ---------- | ----------- |
[11] F.Xing,E.Cambria,andR.Welsch,“Growingsemanticvinesforrobust
|     |     |     |     |     |     | movements | using | word | embeddings | and | deep neural | networks,” | arXiv |
| --- | --- | --- | --- | --- | --- | --------- | ----- | ---- | ---------- | --- | ----------- | ---------- | ----- |
assetallocation,”Knowledge-BasedSystems,2019.
preprintarXiv:1506.07220,2015.
[12] E.Cambria,S.Poria,A.Gelbukh,andM.Thelwall,“Sentimentanalysis
is a big suitcase,” IEEE Intelligent Systems, vol. 32, no. 6, pp. 74–80, [28] A.Picasso,S.Merello,Y.Ma,L.Oneto,andE.Cambria,“Ensembleof
2017. technicalanalysisandmachinelearningformarkettrendprediction,”in
[13] S. Poria, E. Cambria, G. Winterstein, and G.-B. Huang, “Sentic pat- IEEESymposiumSeriesonComputationalIntelligence(SSCI),2018.
| terns: | Dependency-based | rules for concept-level |     | sentiment | analysis,” |     |     |     |     |     |     |     |     |
| ------ | ---------------- | ----------------------- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
[29] J.L.KellyJr,“Anewinterpretationofinformationrate,”inTheKelly
Knowledge-BasedSystems,vol.69,pp.45–63,2014. Capital Growth Investment Criterion: Theory and Practice. World
| [14] J. Pennington, | R. Socher, | and C. Manning, |     | “Glove: | Global vectors |     |     |     |     |     |     |     |     |
| ------------------- | ---------- | --------------- | --- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Scientific,2011,pp.25–34.
| for word | representation,” | in Proceedings | of  | the 2014 | conference | on  |     |     |     |     |     |     |     |
| -------- | ---------------- | -------------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
empiricalmethodsinnaturallanguageprocessing(EMNLP),2014,pp. [30] N.V.Chawla,K.W.Bowyer,L.O.Hall,andW.P.Kegelmeyer,“Smote:
syntheticminorityover-samplingtechnique,”Journalofartificialintel-
1532–1543.
ligenceresearch,vol.16,pp.321–357,2002.
| [15] T. Mikolov, | I. Sutskever,   | K. Chen, | G. S.       | Corrado, | and J. Dean,   |     |     |     |     |     |     |     |     |
| ---------------- | --------------- | -------- | ----------- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| “Distributed     | representations | of words | and phrases | and      | their composi- |     |     |     |     |     |     |     |     |
[31] D.P.KingmaandJ.Ba,“Adam:Amethodforstochasticoptimization,”
tionality,”inAdvancesinneuralinformationprocessingsystems,2013, arXivpreprintarXiv:1412.6980,2014.
pp.3111–3119.
|     |     |     |     |     |     | [32] S. Ioffe | and | C. Szegedy, | “Batch | normalization: |     | Accelerating | deep |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | ------ | -------------- | --- | ------------ | ---- |
[16] E.Cambria,J.Fu,F.Bisio,andS.Poria,“AffectiveSpace2:Enabling
|     |     |     |     |     |     | network | training | by  | reducing | internal covariate |     | shift,” arXiv | preprint |
| --- | --- | --- | --- | --- | --- | ------- | -------- | --- | -------- | ------------------ | --- | ------------- | -------- |
affectiveintuitionforconcept-levelsentimentanalysis.”inAAAI,2015, arXiv:1502.03167,2015.
pp.508–514.
[17] T. Loughran and B. McDonald, “When is a liability not a liability? [33] N.Srivastava,G.Hinton,A.Krizhevsky,I.Sutskever,andR.Salakhut-
textual analysis, dictionaries, and 10-ks,” The Journal of Finance, dinov, “Dropout: a simple way to prevent neural networks from over-
vol.66,no.1,pp.35–65,2011. fitting,”TheJournalofMachineLearningResearch,vol.15,no.1,pp.
1929–1958,2014.
[18] E.HenryandA.J.Leone,“Measuringqualitativeinformationincapital
marketsresearch,”TheAccountingReview,vol.91,no.1,pp.153–178,
|     |     |     |     |     |     | [34] R. C. | Merton, | “An intertemporal |     | capital | asset pricing | model,” | Econo- |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | ----------------- | --- | ------- | ------------- | ------- | ------ |
2009.
metrica:JournaloftheEconometricSociety,pp.867–887,1973.
| [24] Y. Xu | and S. B. Cohen, | “Stock movement | prediction | from | tweets and |     |     |     |     |     |     |     |     |
| ---------- | ---------------- | --------------- | ---------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
historical prices,” in Annual Meeting of the Association for Computa- [35] W. F. Sharpe, “The sharpe ratio,” Journal of portfolio management,
| tionalLinguistics,vol.1,2018. |     |     |     |     |     | vol.21,no.1,pp.49–58,1994. |     |     |     |     |     |                   |     |
| ----------------------------- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | ----------------- | --- |
|                               |     |     |     |     |     | - 8 -                      |     |     |     |     |     | paper N-19019.pdf |     |
Authorized licensed use limited to: Università Bocconi. Downloaded on June 17,2026 at 12:12:10 UTC from IEEE Xplore.  Restrictions apply.