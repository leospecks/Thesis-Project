Proceedings of the 6th International Conference on Data Intelligence and Cognitive Informatics (ICDICI-2025)
IEEE Xplore Part Number: CFP25VL6-ART; ISBN: 979-8-3315-0313-0
Transfer Learning for Cross-Market Predictions:
Applications in Emerging and Volatile Economies

Purna chander Mashetty                         Sirish Gangabathula                             Naga Venkatesh Gangabathula
51053111.5202.77466ICIDCI/9011.01 :IOD | EEEI 5202© 00.13$/52/0-3130-5133-8-979 | )ICIDCI( scitamrofnI evitingoC dna ecnegilletnI ataD no ecnerefnoC lanoitanretnI ht6 5202
            Senior Frontend Developer                   Senior DevOps Engineer                            Sr Software Engineer
                Omnicom Media Group                Texas A&M University, Kingsville                       Austin, Texas
   purnachander.mashetty@gmail.com                  sirishgan20@gmail.com                  Naga.Gangabathula@gmail.com

Neeraja Pullalarevu                              Koushik Reddy Chaganti                                   Sathvik Reddy Chaganti
Solution Specialist                                  Research Scholar                                                        Software Engineer
  Houston Texas USA                           University of the Cumberlands                           Computer Science- Atlanta, Georgia
Neeraja.Pullalarevu@gmail.com        koushikreddyc370@gmail.com                          Sathvikreddyc1998@gmail.com

Abstract - The procedure of financial forecasting faces  I. INTRODUCTION
tough challenges in growing unstable markets because
The problems into predictive model are introduced,
these regimes bring a shortage of accessible data and
such as limited data sampling, the inherent market volatility
unstable markets held back by multiple of translating
and the abrupt transitions of different market states in the
systems. Such environments are hard for deep learning
financial markets of the emerging economies and volatile
| and  traditional  |     | models  | because  | they  | require  | large  |     |     |     |     |     |
| ----------------- | --- | ------- | -------- | ----- | -------- | ------ | --- | --- | --- | --- | --- |
market conditions. those markets which have data scarcity &
amounts of high-quality training data to work correctly.
limited historical data availability, cannot be handled by
The proposed method creates a sophisticated transfer
traditional machine learning & deep learning algorithms
| learning  | framework  | that  | employs  | fixed  | models  | pre- |     |     |     |     |     |
| --------- | ---------- | ----- | -------- | ------ | ------- | ---- | --- | --- | --- | --- | --- |
because traditional algorithms are based on generalization
trained in well-established markets which it then adapts
and follows generalized solution in such environments. Such
| to  developing  | countries  |     | using  | domain  | adaptation  |     |     |     |     |     |     |
| --------------- | ---------- | --- | ------ | ------- | ----------- | --- | --- | --- | --- | --- | --- |
economies with nonlinear dynamic economies often result in
techniques coupled with the process of fine-tuning the
poor model fit and poor performance when whey it come to
| models.  | The  proposed  |     | scheme  | accomplishes  |     | data  |     |     |     |     |     |
| -------- | -------------- | --- | ------- | ------------- | --- | ----- | --- | --- | --- | --- | --- |
volatile market condition. Transfer learning gives an efficient
distribution minimizing functions from Maximum Mean
way to treat these sorts of problems via the use of domain-
Discrepancy, in addition to supervised fine-tuning that
specific learning from source data field by employing it into
targets realizing predictions under the suppressed target
order to boost such performance in other related though
information. The model suggested above scored better
different target domain. This predictive approach allows
| performance  | by  | experiment  | testing  | across  |     | emerging  |     |     |     |     |     |
| ------------ | --- | ----------- | -------- | ------- | --- | --------- | --- | --- | --- | --- | --- |
developers to build with well-developed economies such as
market indices in terms of all metric metrics including
the U.S. and Europe for improving performance in emerging
| mean  absolute  | error,  | root  | mean  | squared  | error  | and  |     |     |     |     |     |
| --------------- | ------- | ----- | ----- | -------- | ------ | ---- | --- | --- | --- | --- | --- |
markets like India, Brazil and South Africa. The pattern and
| direction  | accuracy   | of  | compared  | models.  |     | Transfer  |                 |                 |     |                |                         |
| ---------- | ---------- | --- | --------- | -------- | --- | --------- | --------------- | --------------- | --- | -------------- | ----------------------- |
|            |            |     |           |          |     |           | representation  | understanding   |     | can            | pass  on  from  mature  |
| learning   | is  found  | to  | perform   | well     | in  | solving   |                 |                 |     |                |                         |
|            |            |     |           |          |     |           | market          | to  developing  |     | market,  this  | brings  significant     |
generalization issues in cross-market and hence can be
opportunities which downplay time consuming local data set
considered as a great method for financial prediction in
and bring about better stability model.
data-scarce volatile environments.
Despite its success in other domains such as image
| Keywords  | -  Transfer  |     | learning,  | financial  | forecasting,  |     |     |     |     |     |     |
| --------- | ------------ | --- | ---------- | ---------- | ------------- | --- | --- | --- | --- | --- | --- |
recognition and natural language processing, the application
| emerging  | markets,  | domain  |     | adaptation,  | cross-market  |     |               |           |     |                  |                      |
| --------- | --------- | ------- | --- | ------------ | ------------- | --- | ------------- | --------- | --- | ---------------- | -------------------- |
|           |           |         |     |              |               |     | of  transfer  | learning  | in  | financial  time  | series  forecasting  |
prediction, time-series analysis, volatility modelling.
remains relatively underexplored. Existing studies primarily
  focus on intra-market or cross-asset transfer, with limited
attention to cross-market adaptation, especially in the context

|     |     |     |     |     |     |     | of  high-volatility  |      | and       | low-resource   | environments.  |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | ---- | --------- | -------------- | -------------- |
|     |     |     |     |     |     |     | Furthermore,         | the  | temporal  | and  economic  | heterogeneity  |
between markets introduces domain shifts that challenge the
|     |     |     |     |     | 979-8-3315-0313-0/25/$31.00 ©2025 IEEE |     |     |     |     |     | 621 |
| --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 10:56:55 UTC from IEEE Xplore.  Restrictions apply.

Proceedings of the 6th International Conference on Data Intelligence and Cognitive Informatics (ICDICI-2025)
IEEE Xplore Part Number: CFP25VL6-ART; ISBN: 979-8-3315-0313-0
effectiveness of naive model transfer. This paper addresses Neural Networks (DANN) possesses some great time in
these challenges by proposing a transfer learning-based crossing domain sentiment analysis whereas risk
framework specifically designed for cross-market financial classification difficulties. In financial sector, S&P 500 or
prediction in emerging economies. The contributions of this NASDAQ trained models are fine-tuned to predict results in
work are as follows: (1) we design a robust domain smaller or international market, demonstrate the prospective
adaptation strategy that aligns the source and target market cross-market restart.
distributions while preserving temporal dependencies; (2) we
Cross-pollinating ideas from both macroeconomic
implement a fine-tuning process using limited target-market
signal processing, vascular interventions on sentiment
data to improve adaptability and accuracy; and (3) we
analysis and entirely appropriate technical indicators and
evaluate our framework on multiple emerging market
transfer learning mechanisms has started making a multitude
datasets, demonstrating its superiority over baseline models
signs of superior concrete robustness and interpretability [8].
in terms of prediction accuracy, directional correctness, and
Furthermore, Reinforcement Learning has been used along
resilience to volatility.
with Transfer Learning in order to dynamically adapt trading
The proposed method enables financial forecasting strategies to the market volatility, even though these
pipelines to use domain knowledge for developing predictive applications are mainly under experimental phase.
systems in financial markets that lack sufficient data
Although significant studies have provided
resources and study.
improvements towards mainstream, still very little work is
II. LITERATURE SURVEY attempted towards the deep underlying challenges of transfer
learning in regime changing environments especially in the
Machine learning applications in financial
whole domain changing between markets [9]. Numerous
forecasting have experienced growing popularity during the
empirical studies have demonstrated the effect of political
last few years because these models extract sophisticated
occurrences, currency fluctuations, as well as sudden
nonlinear market data patterns [1]. Time series forecasting
economic policy changes in emerging market to result in
methods such as ARIMA and GARCH face challenges to
non-stationarity which hinders model transfer [10]. In
perform financial forecasting because of the constrain in
addition, deficits in well-rounded frameworks that institutes
their required premises of stationarity and limited tuning
domain adaptation, fine-tuning, and volatility-contrived
ability to respond to changing market situation especially in
adaptations hinder the best possible deployment of transfer
data rich noisy dynamic markets like emerging economy or
learning models in actual emerged market scenarios.
abnormally changing economic situations [2].
This paper extends prior researches by designing an
However, fundamental limitation of using deep
exclusive framework of domain adaptation and strategic
learning based forecasting models is carried out in terms of
fintuning using the pre-trained model from the developed
its excessive demand of labelled data while emerging
markets. By handling the discrepancy in data distributions
markets remains to suffer from less amount of the labelled
and resorting to volatility-resilient modelling methodologies,
data due to poor infrastructure and regulatory impediments
the proposed approach significantly enhances the insufficient
[3]. Transfer learning is a useful approach to transferring
area of cross-market transfer learning in financial
massive amount of information in the information abundant
forecasting.
source domains to the information scarce target domains,
benefiting from its ability of knowledge transfer. Transfer III. METHODOLOGY
learning was born of research in computing areas like vision
The proposed framework aims to forecast financial metrics
and natural language processing [4] but shifted towards
in the EMs by leveraging knowledge from developed,
meeting banking demands of stock market prediction and
information abundant markets. It is implemented in three
credit risk in conventional markets as stated in [5] and [6].
core stages: (A) Source Model Pre-Training, (B) Domain
Several methods have been adopted in domain Adaption, (C) Fine-Tuning and Target Prediction. This
adaptation such as adversarial training or discrepancy architecture guarantees that the system discovers generic
minimization to fool realign feature spaces between source financial components in calm environments and
and target markets, [7]. For instance, title usage of Maximum accommodate them to turbulent, hard to reflect markets
Mean Discrepancy (MMD) and internet Domain-Adversarial observed at figure 1.
979-8-3315-0313-0/25/$31.00 ©2025 IEEE 622
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 10:56:55 UTC from IEEE Xplore. Restrictions apply.

Proceedings of the 6th International Conference on Data Intelligence and Cognitive Informatics (ICDICI-2025)
IEEE Xplore Part Number: CFP25VL6-ART; ISBN: 979-8-3315-0313-0

Figure 1: System Architecture
A. Source Model Pre-Training  To ensure generalizability, the source model is trained
using early stopping, dropout regularization, and time-series
|     | The  initial  | part  of  | the  proposed  framework  |     |     |     |     |     |     |
| --- | ------------- | --------- | ------------------------- | --- | --- | --- | --- | --- | --- |
cross-validation. The trained model captures latent patterns
comprises making a good high quality resource model skilled
|     |     |     |     |     | and  temporal  | dependencies  |     | from  the  developed  | market,  |
| --- | --- | --- | --- | --- | -------------- | ------------- | --- | --------------------- | -------- |
at a sound monetary market. In general, the source domain
which serve as a transferable foundation for subsequent
DS={(xs(i),ys(i))}i=1nis a big size set of the history data of
domain adaptation to the target market.
developed countries' stock markets, for instance, United
States stock markets (e.g. S & P 500 index), for which the  The quality of the source model is critical, as its
market efficiency and data availability have been of great  internal  representations  and  feature  abstractions  are
high.  leveraged  during  transfer.  Consequently,  the  pre-training
phase aims not only for low in-sample error but also for the
Each input sample xs(i) takes the shape of a multi-
extraction of domain-agnostic financial knowledge that can
feature vector, where the inputs involve all sorts of technical
generalize across market regimes and geographies.
| indicators  | (e.  g.  | moving  average,  | RSI),  macroeconomic  |     |     |     |     |     |     |
| ----------- | -------- | ----------------- | --------------------- | --- | --- | --- | --- | --- | --- |
variables  (e.  g.  inflation,  interest  rates)  and  sentiment  B. Domain Adaptation
analysis scores. The corresponding target label ys(i) may
Once the source model fS(x;θS) is pre-trained on
refer to nextday price direction (classification) or return
|     |     |     |     |     | data-rich  | developed  | markets,  | the  next  | step  is  domain  |
| --- | --- | --- | --- | --- | ---------- | ---------- | --------- | ---------- | ----------------- |
value (regression), according to the prediction task.
adaptation, which addresses the distributional divergence
A trained deep learning model fS(x;θS), e.g., a Long  between the source domain DSD_SDS and the target domain
Short-Term  Memory  (LSTM)  network  or  a  Temporal  DTD_TDT (i.e., emerging market data). Direct application
Convolutional  Network  (TCN)  is  utilized  to  reduce  the  of the source model to the target market is suboptimal due to
prediction error for the source data. The learning objective is  this domain shift, which arises from structural, economic,
| stated as:  |     |     |     |     | and temporal differences across markets.  |     |     |     |     |
| ----------- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- |
1 ∑𝑛 l(𝑓(𝑥(𝑖);𝜃 ),𝑦(𝑖))---1  To  mitigate  this,  the  proposed  framework
ℒ =
|     | 𝒮   | 𝑛 𝑖=1 𝑆 𝑠 | 𝑆 𝑠 |     |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
incorporates a domain adaptation module designed to align
where:  the feature space of the source and target domains while
preserving predictive performance. We adopt a distribution
•  ℓ(⋅) is the loss function—mean squared error (MSE)  matching  technique  using  Maximum  Mean  Discrepancy
|     | for regression         | tasks  or  | binary  cross-entropy  | for  |                         |               |      |                    |               |
| --- | ---------------------- | ---------- | ---------------------- | ---- | ----------------------- | ------------- | ---- | ------------------ | ------------- |
|     |                        |            |                        |      | (MMD)                   | to  minimize  | the  | distance  between  | the  encoded  |
|     | classification tasks.  |            |                        |      | feature distributions.  |               |      |                    |               |
•  θS denotes the trainable parameters of the source  Formally, let ϕ(x) denote the hidden representation
model.
of input data extracted from an intermediate layer of the
|     |     |     |     |     | neural  | network.  | The  domain  | adaptation  | loss  LDA  is  |
| --- | --- | --- | --- | --- | ------- | --------- | ------------ | ----------- | -------------- |
•  fS(x) is the output of the source model.
computed as:
|     |     |     | 979-8-3315-0313-0/25/$31.00 ©2025 IEEE |     |     |     |     |     | 623 |
| --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 10:56:55 UTC from IEEE Xplore.  Restrictions apply.

Proceedings of the 6th International Conference on Data Intelligence and Cognitive Informatics (ICDICI-2025)
IEEE Xplore Part Number: CFP25VL6-ART; ISBN: 979-8-3315-0313-0
1 ∑𝑛 𝜙(𝑥(𝑖))− 1 ∑𝑚 (𝑗) )|2----2  dataset from the target domain 𝐷𝑇 ={(𝑥𝑡(𝑗),𝑦𝑡(𝑗))}𝑗=
| ℒ   | =|  |       |       | 𝜙(𝑥 |     |     |     |        |           |          |     |            |         |       |       |
| --- | --- | ----- | ----- | --- | --- | --- | --- | ------ | --------- | -------- | --- | ---------- | ------- | ----- | ----- |
| 𝒟𝒜  | 𝑛   | 𝑖=1 𝑠 | 𝑚 𝑗=1 | 𝑡   |     |     |     |        |           |          |     |            |         |       |       |
|     |     |       |       |     |     |     | 1𝑚  | Since  | emerging  | markets  |     | typically  | suffer  | from  | data  |
where:  scarcity, this phase is critical for calibrating the model to the
|     |     |     |     |     |     |     | unique  | characteristics  |     |     | of  the  | target  | economy  |     | without  |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------------- | --- | --- | -------- | ------- | -------- | --- | -------- |
𝑥(𝑖)
|     | •   | ∼𝐷  are samples from the source domain,  |     |     |     |     | overfitting.  |     |     |     |     |     |     |     |     |
| --- | --- | ---------------------------------------- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑠 𝑆
|     | (𝑗)  |                                          |     |     |     |     |     | The  | learned  | source  |     | pre-training  |     | base  | model  |
| --- | ---- | ---------------------------------------- | --- | --- | --- | --- | --- | ---- | -------- | ------- | --- | ------------- | --- | ----- | ------ |
|     | •  𝑥 | ∼𝐷  are samples from the target domain,  |     |     |     |     |     |      |          |         |     |               |     |       |        |
𝑡 𝑇
parameters θS and partially adapted via domain alignment,
•  ϕ(x) maps the input to a reproducing kernel Hilbert  constitute a prior for the target model fT(x;θT)). Fine-tuning
space (RKHS),
|     |     |     |     |     |     |     | changes  | these  | parameters  |     | by  | directly  | optimizing  |     | the  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ----------- | --- | --- | --------- | ----------- | --- | ---- |
supervised task loss on the target domain:
•  n and mmm are the number of source and target
|     | samples respectively.  |                   |      |        |            |         |     |     | 1   |        | (𝑗) |        | (𝑗)     |     |     |
| --- | ---------------------- | ----------------- | ---- | ------ | ---------- | ------- | --- | --- | --- | ------ | --- | ------ | ------- | --- | --- |
|     |                        |                   |      |        |            |         |     | ℒ   | =   | ∑𝑚 l(𝑓 | (𝑥  | ;𝜃 ),𝑦 | )----5  |     |     |
|     |                        |                   |      |        |            |         |     |     | 𝒯 𝑚 | 𝑗=1    | 𝑇 𝑡 | 𝑇      | 𝑡       |     |     |
|     | This                   | loss  encourages  | the  | model  | to  learn  | domain- |     |     |     |        |     |        |         |     |     |
where:
| invariant  | representations,  |     | ensuring  | that  | the  latent  | space  |     |     |     |     |     |     |     |     |     |
| ---------- | ----------------- | --- | --------- | ----- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
embeddings of source and target data become statistically
•  ℓ(⋅) is the task-specific loss (e.g., binary cross-
similar.  To  incorporate  both  prediction  accuracy  and  entropy for classification or mean squared error for
distribution alignment, the total loss function becomes:
regression),
|     |     | ℒ   | =ℒ +𝜆ℒ | ---3  |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝒯ℴ𝓉𝒶ℓ 𝒯 𝒟𝒜 •  θT are the updated parameters adapted specifically
| where:  |     |     |     |     |     |     |     | for the target domain.  |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |
The overall objective function combines prediction loss
|     | •  LT  | is  the  task-specific  |     | prediction  |     | loss  (e.g.,  |     |     |     |     |     |     |     |     |     |
| --- | ------ | ----------------------- | --- | ----------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
with domain adaptation regularization:
classification or regression) computed on labeled
|     | target domain data,  |     |     |     |     |     |     |     | ℒ   |       | =ℒ +𝜆ℒ | ---6  |     |     |     |
| --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ----- | --- | --- | --- |
|     |                      |     |     |     |     |     |     |     |     | 𝒯ℴ𝓉𝒶ℓ | 𝒯      | 𝒟𝒜    |     |     |     |
•  λ is a hyperparameter balancing task performance  Gradient descent is then employed to minimize
and domain alignment.
LTotal with respect to θT:
During training, gradients are propagated not only to
|     |     |     |     |     |     |     |     |     | 𝜃   | ←𝜃  | −𝜂∇ | ℒ     | ---7  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- |
|     |     |     |     |     |     |     |     |     | 𝑇   | 𝑇   | 𝜃𝑇  | 𝒯ℴ𝓉𝒶ℓ |       |     |     |
minimize LT, but also to reduce LDA, effectively forcing the
model  to  adapt  its  internal  parameters  to  fit  the  target  where η is the learning rate.
domain's characteristics.
In practice, the fine-tuning process involves one of the
In  some  configurations,  an  adversarial  domain  following strategies:
discriminator D may also be introduced to form a Domain-
•  Full fine-tuning: all layers of the model are updated.
Adversarial Neural Network (DANN), enhancing the domain
adaptation by using a min-max game:
•  Partial fine-tuning: only the last few layers (or
|           |     |           |     |       |         |     |     | domain-specific           |     |     | layers)  | are  | updated  | to  | prevent  |
| --------- | --- | --------- | --- | ----- | ------- | --- | --- | ------------------------- | --- | --- | -------- | ---- | -------- | --- | -------- |
| minmax. 𝐸 |     | [log𝐷(𝜙(𝑥 |     | ))]+𝐸 | [log(1− |     |     |                           |     |     |          |      |          |     |          |
|           |     | 𝑥𝑠∼𝐷𝑆     |     | 𝑠     | 𝑥𝑡∼𝐷𝑇   |     |     | catastrophic forgetting.  |     |     |          |      |          |     |          |
𝑓 𝐷
|     |       | 𝐷(𝜙(𝑥        | )))]---4  |     |          |           |     |                                                         |     |            |        |        |       |             |     |
| --- | ----- | ------------ | --------- | --- | -------- | --------- | --- | ------------------------------------------------------- | --- | ---------- | ------ | ------ | ----- | ----------- | --- |
|     |       |              | 𝑡         |     |          |           |     | •  Layer freezing: lower layers (which extract general  |     |            |        |        |       |             |     |
|     |       |              |           |     |          |           |     | features)                                               |     | are  kept  | fixed  | while  | only  | high-level  |     |
|     | This  | adversarial  | training  |     | further  | improves  |     |                                                         |     |            |        |        |       |             |     |
features are adapted.
alignment by ensuring that the model cannot distinguish
between source and target features.
Early stopping and dropout regularization are applied
during this phase to avoid overfitting due to the limited target
Ultimately, this stage ensures that the foundational
|            |     |            |                 |     |           |          | data.  | Once  | training  | converges,  |     | the  | resulting  | model  | is  |
| ---------- | --- | ---------- | --------------- | --- | --------- | -------- | ------ | ----- | --------- | ----------- | --- | ---- | ---------- | ------ | --- |
| knowledge  |     | from  the  | source  domain  | is  | adjusted  | to  the  |        |       |           |             |     |      |            |        |     |
deployed for real-time prediction of market movements or
| statistical  |     | and  behavioural  | characteristics  |     | of  | the  target  |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ----------------- | ---------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
asset returns in the target (emerging) economy.
(emerging) market, enabling more accurate predictions even
with limited labelled data.
The effectiveness of this stage is evaluated using metrics
such as directional accuracy, mean absolute error (MAE),
C. Fine-Tuning and Prediction
|     |     |     |     |     |     |     | and  | root  mean  |     | squared  | error  | (RMSE)  | on  | a  withheld  |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | --- | -------- | ------ | ------- | --- | ------------ | --- |
After performing domain adaptation, the final stage  validation set from the target domain. This provides insight
|     |     |     |     |     |     |     | into  | how  well  | the  | model  | has  | transferred  |     | and  | adapted  |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | ---- | ------ | ---- | ------------ | --- | ---- | -------- |
involves fine-tuning the adapted model using a small labelled
|     |     |     |     |     | 979-8-3315-0313-0/25/$31.00 ©2025 IEEE |     |     |     |     |     |     |     |     | 624 |     |
| --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 10:56:55 UTC from IEEE Xplore.  Restrictions apply.

Proceedings of the 6th International Conference on Data Intelligence and Cognitive Informatics (ICDICI-2025)
IEEE Xplore Part Number: CFP25VL6-ART; ISBN: 979-8-3315-0313-0
knowledge  from  the  source  market  to  the new,  volatile  •  Directional  Accuracy  (DA):  Measures  the
environment.  percentage of times the model correctly predicted
the direction of market movement.
IV. RESULTS AND DISCUSSION
Table I: Prediction Performance Comparison
| To  evaluate  | the  effectiveness  | of  the  proposed  |     |     |     |     |     |
| ------------- | ------------------- | ------------------ | --- | --- | --- | --- | --- |
transfer  learning  framework,  we  conducted  experiments  Model  MAE  RMSE  Directional
using  historical  financial data  from  both developed  and  Accuracy (%)
emerging markets. The source market used for model pre-
|     |     |     | Traditional ML  |     | 0.134  0.201  | 61.2  |     |
| --- | --- | --- | --------------- | --- | ------------- | ----- | --- |
training was the S&P 500 index (United States), and the
target markets were the NIFTY 50 (India) and BOVESPA
|     |     |     | Deep Learning  |     | 0.120  0.185  | 64.5  |     |
| --- | --- | --- | -------------- | --- | ------------- | ----- | --- |
(Brazil), representing emerging and volatile economies.
|     |     |     | Proposed Transfer  |     | 0.098  0.142  | 72.3  |     |
| --- | --- | --- | ------------------ | --- | ------------- | ----- | --- |
Three models were benchmarked:
Learning
1.  A traditional machine learning model trained only

on target data (e.g., Random Forest).
B. Analysis
2.  A deep learning model trained solely on target data
(e.g., LSTM).  As shown in Table I and the accompanying graphs. The
|                    |                     |                   | Proposed  | Transfer  | Learning  | model  significantly  |     |
| ------------------ | ------------------- | ----------------- | --------- | --------- | --------- | --------------------- | --- |
| 3.  The  proposed  | transfer  learning  | model  utilizing  |           |           |           |                       |     |
outperformed the baselines, achieving the lowest MAE and
source knowledge and domain adaptation.
|     |     |     | RMSE,     | indicating    | superior  numerical  | accuracy.  | It  also  |
| --- | --- | --- | --------- | ------------- | -------------------- | ---------- | --------- |
|     |     |     | achieved  | the  highest  | Directional          | Accuracy   | (72.3%),  |
A. Performance Metrics
|     |     |     | highlighting  | its  | ability  to  correctly  | forecast  | market  |
| --- | --- | --- | ------------- | ---- | ----------------------- | --------- | ------- |
We evaluated the models using three key metrics:  movements,  which  is  crucial  in  real-world  financial
applications.
•  Mean Absolute Error (MAE): Measures average
prediction error magnitude.

| •  Root Mean Squared Error (RMSE): Penalizes larger  |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
errors more heavily.

Figure 2: MAE and RMSE Comparison
Figure 2 shows a side-by-side comparison of MAE and
RMSE for the three models, where the proposed method
clearly results in lower error rates.
|     |     | 979-8-3315-0313-0/25/$31.00 ©2025 IEEE |     |     |     | 625 |     |
| --- | --- | -------------------------------------- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 10:56:55 UTC from IEEE Xplore.  Restrictions apply.

Proceedings of the 6th International Conference on Data Intelligence and Cognitive Informatics (ICDICI-2025)
IEEE Xplore Part Number: CFP25VL6-ART; ISBN: 979-8-3315-0313-0
Figure 3: Directional Accuracy Comparison
Figure 3 illustrates the improvement in directional REFERENCES
accuracy, demonstrating the effectiveness of transferring
learned knowledge from developed markets to enhance 1. Adewale, Tunmise. "Transfer Learning Applications in Cross-
prediction in volatile markets. The results underscore that: Market Investment Strategies." (2024).
2. Wang, Yide, Zan Chen, and Xiaodong Ji. "Cross-market
Transfer learning significantly enhances prediction
information transmission and stock market volatility
performance in low-resource target domains. Domain prediction." The North American Journal of Economics and
adaptation aligns latent feature spaces across market Finance 68 (2023): 101977.
regimes, allowing for knowledge transfer despite underlying 3. Bhattacharjee, Biplab, Rajiv Kumar, and Arunachalam
Senthilkumar. "Unidirectional and bidirectional LSTM models
distribution shifts. Fine-tuning with even limited labelled
for edge weight predictions in dynamic cross-market equity
data from the target market substantially improves networks." International Review of Financial Analysis 84
forecasting reliability during periods of economic (2022): 102384.
uncertainty and volatility. 4. Feng, Ling, and Ananta Sinchai. "Transfer learning model for
cash-instrument prediction adopting a Transformer
derivative." Journal of King Saud University-Computer and
V. CONCLUSION Information Sciences 36, no. 3 (2024): 102000.
5. Pankwaen, Kansuda, Sukrit Thongkairat, and Worrawat Saijai.
"Global Cross-Market Trading Optimization Using Iterative
This paper proposed a transfer learning based framework to
Combined Algorithm: A Multi-Asset Approach with Stocks and
improve a financial market prediction in the context of
Cryptocurrencies." Mathematics 13, no. 8 (2025): 1317.
emerging and volatile economy by using the knowledge of 6. Fu, Pingping, Honghao Yang, Wenhao Qian, ELsiddig Idriss
developed, data rich market. The proposed method is based Mohamed, Wafa Ali J. Almohri, and Huda M. Alshanbari.
on the pre-training of the source model, the domain "Financial engineering and the digital economy: The
adaptation using distribution matching methods, and the implementations of machine learning algorithms." Alexandria
Engineering Journal 125 (2025): 311-319.
fine-tuning on limited amount of target domain data. The
7. Sheng, Yuan. "Market Return Prediction via Variational Causal
results from various financial indices proved that the
Representation Learning." Journal of Computer Technology and
proposed method surpasses the standard machine learning Software 3, no. 8 (2024).
and target-only deep learning models significantly in the 8. Patel, Manali, Krupa Jariwala, and Chiranjoy Chattopadhyay.
measurement of mean absolute error, root mean squared "Deep Learning techniques for stock market forecasting: Recent
error, and directional accuracy. Notably, the model trends and challenges." In Proceedings of the 2023 6th
international conference on software engineering and
demonstrated to be the robustness on the data scarcity and
information management, pp. 1-11. 2023.
structural volatility, which are features of emerging markets.
9. Shen, Junjie, and Shupei Huang. "Copper cross-market volatility
The results show that transfer learning can be used as
transition based on a coupled hidden Markov model and the
effective method for cross-market generalization, supporting complex network method." Resources Policy 75 (2022): 102518.
higher accuracy and reliability of predictions when 10. Huang, Wei-Qiang, and Peipei Liu. "Cross-market risk spillovers
traditional methods fail. This has far-reaching implications among sovereign CDS, stock, foreign exchange and commodity
for investors, politicians and money managers doing markets: An interacting network perspective." International
Review of Financial Analysis 90 (2023): 102875.
business in changing economic conditions.
979-8-3315-0313-0/25/$31.00 ©2025 IEEE 626
Authorized licensed use limited to: Università Bocconi. Downloaded on June 14,2026 at 10:56:55 UTC from IEEE Xplore. Restrictions apply.