d
e
w
Forecasting Asset Returns with Sentiment-Enhanced
FIGARCH Models
e
,
i
a, , , , ,
v
e
Abstract
r
This paper introduces a novel sentiment-driven framework for forecasting as-
set returns and modeling volatility by integrating machine learning and time-
r
series econometric techniques. Leveraging a dataset of over 347,000 asset-
e
specific news headlines and financial data spanning from March 2022 to Jan-
uary 2025, we first develop a Random Forest classifier to assess the likelihood
e
that daily news headlines will significantly impact asset returns positively or
negativelyacrossfourkeytimeframes: Open-to-Close, Open-to-Open, Close-
to-Close, and Close-to-Open.pIn parallel, we utilize the FinBERT model to
extract average sentiment scores from headlines and construct sentiment-
based exogenous variables. These features are incorporated into an extended
FIGARCH(1,1) model tto examine their predictive contributions to return
volatility. Empiricaloresults across 37 assets from stock, cryptocurrency, and
commodity markets demonstrate that the inclusion of sentiment and impact
probability features improves model performance (measured by AIC, BIC,
n
and log-likelihood), particularly in time frames sensitive to market openings
and overnight news. Our findings underscore the value of combining tex-
tual sentiment indicators produced by the FinBERT model, which is specif-
t
ically trained on financial data, alongside directional time frame-based im-
n
pact probabilities computed by the Random Forest model with advanced
volatility modeling to enhance financial forecasting and support informed
i
decision-making in dynamic markets.
r
Keywords:
p
Sentiment Analysis, Random Forest Model, FinBERT, FIGARCH, Returns
Prediction
e
r
∗
P Email addresses: (), ()
Preprint submitted to The Journal of Finance and Data Science December 19, 2025
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
1. Introduction
Profitablefinancialmarketdecisionslargelyrelyonpredictiengfutureprice
movements of risky assets. Making such accurate predictions is difficult be-
cause they are influenced by many factors, and many of thiese factors and
their effects on markets are still unknown, especially thvose that are qualita-
tive or behavioral. The collective behavior of market participants, commonly
e
called market sentiment, is a crucial factor in price movements and short-
term deviations from assets’ intrinsic value [? ]. Studying, quantifying, and
modeling market sentiment to improve the accruracy of asset-price models
has become a significant challenge and area of research in this field.
Financialnewsplatformspublishanextensivearrayofarticleseachdayto
r
report on global macroeconomic events and company-specific developments
e
that significantly impact overall market trends and the price movements of
individual companies. Market participants scan the released news and ad-
e
just their decisions based on the information they interpret. Consequently,
market sentiment or the collective behavior of market participants can be
p
shaped and influenced by the information or even the tone of financial news.
Recently, the number of sources and availability of financial news data have
grown significantly, makin g it essential for market participants to have an
automated system for cotllecting, processing, and analyzing their impacts on
financial assets to poroduce valuable insights that support decision-making
processes [? ? ].
Scholarly rensearch increasingly explores how news and media sentiment
influence financial markets, going beyond traditional fundamental analysis.
Early work by Antweiler and Frank [? ] analyzed Internet stock message
boards, revealing that message activity predicts market volatility and has
t
a statistically significant, albeit economically small, effect on stock returns,
n
with disagreement among messages associated with increased trading vol-
ume. Complementing this, Baker and Wurgler [? ] demonstrated that broad
i
investor sentiment, derived from various market proxies, disproportionately
r
affects stocks with subjective valuations and limited arbitrage opportunities,
p
influencing the cross-section of returns. Further advancing the methodologi-
cal landscape, Kelly and Ahmad [? ] highlighted the importance of domain-
especific dictionaries for extracting sentiment from financial news, showing
that negative sentiment in financial news could predict next-day stock and
rcrude oil returns, thereby enhancing trading strategies. More recently, with
the advent of advanced natural language processing techniques, studies have
P
2
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
leveraged BERT-based models for sentiment analysis. Case and Clements [?
] found that financial news sentiment published pre-trading is predictive of
e
daily S&P 500 price changes, while longer-term economic news sentiment ex-
hibits a statistically significant negative relationship with monthly returns.
i
Building on this, Costola et al. [? ] utilized a financial market-adapted
v
BERT model to examine COVID-19 news, concluding that a statistically
significant positive relationship exists between news sentiment scores and
e
S&P 500 market returns, with negative news serving as the primary driver
of market expectations during crises and business news identified as a key
r
sentiment driver. Specifically for crude oil markets, Sahut et al. [? ] demon-
strated that news-based sentiment, when int egrated into machine learning
forecasting models, significantly improvedrcrude oil price prediction during
periods of high volatility such as theeCOVID-19 pandemic, contrasting its
influence in other crisis periods.
Numerous natural language processing (NLP) techniques have been pro-
e
posed to extract sentiment metrics from financial news and examine their
influence on asset price dynamics. Overall, sentiment analysis methods can
p
be categorized into lexicon-based and machine learning-based approaches [?
]. These methods quantify sentiment polarity and assign sentiment scores to
textual content by leveraging historical data patterns.
t
Previous studies have compared lexicon-based approaches, which rely on
o
predefineddictionariesofpositiveandnegativewords,withmachinelearning-
basedapproachestrainedonlargefinancialtextcorpora. Whilelexicon-based
methods providne interpretability and quick deployment, machine learning
models, such as transformer-based models, tend to perform better at cap-
turing comp lex sentiment patterns, especially within domain-specific lan-
guage. Indteed, recent research further underscores the effectiveness of ad-
vancend computational methods in quantifying and leveraging market senti-
ment for financial forecasting [? ? ? ? ? ]. Research shows that sentiment
analiysis used as a pre-processing step to extract informative features can
srignificantly reduce feature dimensions and improve prediction accuracy for
stock market trends, even outperforming deep learning models that rely on
p
high-dimensional raw text features [? ? ]. For example, SVM-based models
combined with sentiment-related features, such as polarity and subjectiv-
e
ity extracted using NLP libraries, have demonstrated better performance
and computational efficiency in predicting abnormal returns [? ]. Likewise,
r
the inclusion of sentiment scores as exogenous factors has been shown to
Pimprove the goodness-of-fit of regression models for forecasting stock open-
3
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
ing prices, with polynomial autoregressions often providing a better fit than
linear ones [? ]. In the context of the volatile cryptocurrency market, Natu-
e
ral Language Processing (NLP) has been applied to convert news data into
numerical sentiment data, and it has demonstrated that both positive and
i
negative streams of information exert significant influence on the returns
v
and volatility of Bitcoin futures, challenging efficient market hypotheses [?
]. Furthermore, when comparing various deep learning and machine learn-
e
ing sentiment analysis models, transformer-based models such as BERT and
their derivatives (e.g., RoBERTa, used by Pysentimento) have consistently
r
shown better accuracy in sentiment tagging from social media content than
traditionalSVMandCNN-LSTMmodelsinpr edictingcryptocurrencyprices
and directions [? ]. Specialized domain senrtiment models, such as SKEP on
financial corpora, as well as novel revieew weighting methods, have also been
shown to significantly improve short-term stock trend forecasts, clearly illus-
trating the effectiveness of feature engineering and specialized training for
e
extracting fine-grained investor sentiment [? ]. This collection of work col-
lectively points to the growing complexity and increasingly important role
p
that sentiment analysis plays in uncovering complex market configurations
and enhancing forecasting capacity across a variety of financial assets.
The numerical outputs generated by these sentiment models have been
t
incorporated into various financial forecasting frameworks as exogenous vari-
o
ables to improve their predictive accuracy and practical applicability [? ].
Among machine learning-based models, FinBERT stands out as a specialized
sentiment analynsis framework trained specifically on financial texts, thereby
achieving greater accuracy within the financial domain [? ]. Beyond assess-
ing sentimen t metrics, a more critical question is how sentiment expressed
during diffterent time intervals affects price dynamics across various intraday
time fnrames. The traditional view suggests that positive sentiment leads to
positive returns, while negative sentiment results in negative returns. How-
everi, does this assumption hold consistently across all return horizons within
artrading day for both positive and negative directions? Currently, there is
limited research that explicitly explores this question [? ].
p
Financial return time series exhibit special characteristics such as asym-
metry, volatility clustering, and long-term memory, which require the de-
e
velopment of models to capture these features. Traditional models such as
GARCH [? ] and its extensions have been widely used to capture volatility
r
clustering in return series. However, these models often fall short in captur-
Ping long-memory effects, prompting the adoption of fractionally integrated
4
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
GARCH (FIGARCH) models [? ]. FIGARCH is a well-known and robust
model designed to represent financial time series by modeling volatility and
e
providing accurate estimates. Recently, many studies have attempted to
improve this model’s performance by incorporating exogenous variables or
i
considering regime-switching structures based on sentiment analysis.
v
Ampountolas [? ] found Support Vector Regression (SVR) to be supe-
rior for short-run volatility forecasting of gold, cocoa, and S&P500 relative
e
to ordinary GARCH models. Feng et al. [? ] found that macroeconomic
news sentiment significantly affects the states of Japanese stock volatility, as
r
measured by the MRS-LMGARCH, with negative news increasing volatility
and positive news decreasing it. Ho et al. [? ] found that firm-specific news
sentiment has a significant effect of reducinrg intraday asset volatility persis-
tence, especially with negative news haeving the greatest impact, especially in
high volatility states. Shi and Ho [? ] established a Two-State Three-State
FIGARCH (3S-FIGARCH) model incorporating Markov Regime-Switching
e
to estimate economic volatility states, offering better long-memory estimates
and structural change detection. Shi and Ho [? ] developed an MRS-
p
FIEGARCH model to show that macroeconomic and negative firm-specific
news sentiment have strong effects on volatility states, increasing the likeli-
hood of higher volatility. Xu et al. [? ] further found that incorporating
t
investor sentiment and regime switching significantly improves the forecast-
o
ing performance of realized range-based volatility (RRV) for the S&P 500
index. Xu et al. [? ] also quantified Chinese official media sentiment (with
BERT) as beinng important and negatively forecasting short-to-long horizon
Chinese crude oil futures (SC) but not WTI volatility, indicating Chinese
market-speci fic information.
Despitetadvances in volatility models and sentiment analytics, to the best
ofournknowledge, noresearchhasfocusedonimprovingtheFIGARCHmodel
for return series estimation while considering the potentially different effects
of fiinancial news headlines on price dynamics across different directions and
mrultiple time frames. This paper aims to bridge this gap by developing a
sentiment-driven FIGARCH framework informed by a Random Forest-based
p
news impact probabilities.
In this paper, we have developed a machine learning-based framework
e
using the Random Forest model [? ] to assess the likelihood that news
headlines affect asset daily returns across different time frames, including
r
Open-to-Close, Open-to-Open, Close-to-Open, and Close-to-Close, in both
Ppositive and negative directions. In this framework, news headlines collected
5
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
within a day are classified as impactful or non-impactful based on their effect
on return deviations. If published news during a day causes significant fluc-
e
tuations in returns, we classify them as impactful, and vice versa. We have
incorporated the bag-of-words feature representation into the Random For-
i
est model to compute the probability that news headlines are impactful on
v
returns across various time frames. Additionally, we used impact probabili-
ties alongside sentiment variables derived from FinBERT scores, and we in-
e
cluded news frequency as an exogenous variable in the FIGARCH time-series
prediction model to examine their contributions to predictive accuracy and
r
goodness-of-fit. We also compared the performance of our method through
empirical studies on financial assets from differ ent markets. A comprehensive
dataset was compiled, including 347,500 assret-specific news headlines and fi-
nancial data from March 1, 2022, toeJanuary 31, 2025, covering 36 assets
from the stock, cryptocurrency, and commodity markets. The results indi-
cate that, using the Random Forest model, we can accurately classify news
e
headlines as impactful or non-impactful in the subsequent period. However,
the accuracy varies across different time frames and directions; on average,
p
the model for classifying positive impacts over the Close-to-Open time frame
achieves the highest accuracy. Furthermore, the FIGARCH model with ex-
ogenous variables such as sentiment metrics and impact probabilities out-
t
performs traditional FIGARCH models in terms of data fit. Therefore, our
o
proposed sentiment analysis framework could serve as a broadly useful tool
for modeling financial volatility and enhancing prediction accuracy.
This paper cnontributes to the literature in three ways. First, it introduces
a novel sentiment-enhanced FIGARCH framework that integrates machine-
learning–base d news-impact probabilities with FinBERT-derived sentiment
scores. Setcond, it explicitly examines how news sentiment affects returns
acrossnfour distinct intraday horizons (Open-to-Close, Open-to-Open, Close-
to-Close, and Close-to-Open), an aspect that has received little attention
in pirior FIGARCH research. Third, by evaluating 37 assets from stock,
crryptocurrency, and commodity markets, the study provides comprehensive
empirical evidence of the value of sentiment-driven exogenous variables in
p
improving volatility modeling and forecasting.
The remainder of this paper is organized as follows. Section 2 describes
e
the collected news and financial data, as well as the methodology and models
implemented in this study. Section 3 discusses the empirical results. Finally,
r
Section 4 presents the conclusion and directions for future research.
P
6
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
2. Methodology
| 2.1. | Data |     |     |     |     |     |     |     | e   |
| ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Our proposed approach is based on comprehensive data obtained from
i
AlphaVantage [? ] covering the period from March 1, 2022, to January 31,
v
2025. Thisdatasetconsistsofasset-specificnewsheadlinesandfinancialdata
for a broad range of assets across the stock, commodity, and cryptocurrency
e
markets, including the 23 largest companies in the Dow Jones Industrial
Index (DJI), the 12 largest companies in the NASDAQ index, Brent Oil,
r
and the two largest cryptocurrencies, Bitcoin and Ethereum. AlphaVantage
aggregates news headlines from premier globa l news outlets related to spe-
cific firms or topics. The collected news heradlines pertain to the stock and
cryptocurrency markets, while those related to commodities cover macroe-
e
conomic issues, monetary policy, and energy transportation topics. Alpha-
Vantage provides both the headlines and article summaries, along with their
e
precise publication times from the outlet that reports the news before any
other sources. Therefore, the collected headlines are considered novel, and
p
it is assumed that the effect of the news on prices has not yet been reflected
at the time of publication. Table 1 summarizes the number of headlines

| collected |     | for each | market. |     |     |     |     |     |     |
| --------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- |
t
Table 1: Overview of iondividual assets and the corresponding number of news headlines
| collected | from | AlphaVantage |     | for | each | market. |     |     |     |
| --------- | ---- | ------------ | --- | --- | ---- | ------- | --- | --- | --- |
nAssets
| Market |       |        |       |       |       |       |       | # of | News Headlines |
| ------ | ----- | ------ | ----- | ----- | ----- | ----- | ----- | ---- | -------------- |
| Stock  |       |        | AAPL, |       | AMGN, |       | AMZN, |      | 307,200        |
|        |       |  AXP,  |       |       | AVGO, | BA,   |       | CAT, |                |
|        |       | tCOST, |       |       | CRM,  | CSCO, |       | CVX, |                |
|        | nDIS, |        |       | GOOG, |       | GS,   | HD,   | HON, |                |
|        |       |        | IBM,  |       | JNJ,  | KO,   | META, |      |                |
|        |       |        | MCD,  |       | MMM,  |       | MSFT, |      |                |
i
| r   |     |     | NFLX, |     | NKE, | NVDA, |      | PG, |     |
| --- | --- | --- | ----- | --- | ---- | ----- | ---- | --- | --- |
|     |     |     | SHW,  |     | TRV, | TSLA, | UNH, | V,  |     |
p
|                |     |     | VZ,      | WMT |          |     |     |     |        |
| -------------- | --- | --- | -------- | --- | -------- | --- | --- | --- | ------ |
| Cryptocurrency |     |     | Bitcoin, |     | Ethereum |     |     |     | 49,972 |
e
| Commodity |     |     | Brent |     | Oil |     |     |     | 71,747 |
| --------- | --- | --- | ----- | --- | --- | --- | --- | --- | ------ |
r
P
7
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
2.2. Sentiment Variables from FinBERT
In this research, we utilized the FinBERT model API, integrated by the
e
Hugging Face community [? ], to analyze the sentiment polarity of each
news headline and to evaluate the corresponding sentiment scores and the
i
frequencies of headlines in each sentiment class. Before extracting senti-
v
ment, noise in the collected news headlines was removed. Specifically, we
removed common prefixes and suffixes in headlinees that do not convey an-
alytical or sentiment-bearing information. For instance, stylistic or source
markers such as “Breaking:”, “Update:”, and “Report:”, and publisher identi-
r
fiers (e.g., “Reuters –” and “CNBC:”), as well as redundant stock ticker tags
placed in parentheses (e.g., “(AAPL)” and “(TSLA)”). These terms, identified
r
via manual inspection of numerous headlines, were discarded as they pertain
solely to formatting or metadata ratheer than to the semantic content neces-
sary for sentiment analysis. Furthermore, some texts mistakenly classified as
headlines due to data-collection eerrors were identified and removed.
Using the positive, negative, and neutral sentiment scores, along with
the frequency of polarized hpeadlines provided by the FinBERT model, we
constructed several variables for each trading day. These variables are used
as exogenous variables in the models in subsequent steps to evaluate the
effect of news sentiment on price predictions. They are defined as follows:
t
o
(cid:80)N t + S+ (cid:80)N t − S− (cid:80)N t O SO
AS+ = i=1 t,i , AS− = i=1 t,i , ASO = i=1 t,i , (1)
t N+ t N− t NO
nt t t
where S+, S−, and SO are, respectively, positive, negative, and neutral
t,i t,i t,i
sentiment sco res of the ith news headline at time t. N+, N−, and NO are,
t t t
respectivelty, the number of positive, negative, and neutral news headlines at
time t.
n
2.3. Bag-of-Words Model
i
rAs discussed in the introduction, asset-specific news headlines may be
impactful on financial returns in some time frames but not impactful in
p
others. For instance, they may push up the Open-to-Close return of a par-
ticular asset but pull down its Close-to-Close return. Generally, collected
e
news headlines related to any financial asset on a given day can be classified
into three main categories: positively impactful, negatively impactful, and
r
non-impactful on financial returns. In this part, we fit the Random Forest
Pmodel using the generated bag-of-words from news headlines as features to
8
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
e
i
v
e
r

Figure 1: A system diagram of the classification mrodel developed to compute time series
|     | of news | headlines’ | impact probabilities. |     |     |     |     |
| --- | ------- | ---------- | --------------------- | --- | --- | --- | --- |
e
calculate the probabilities that collected news headlines are positively or neg-
e
atively impactful on different financial returns. The overall architecture of
|     | this | model is shown | in Figure | 1.  |     |     |     |
| --- | ---- | -------------- | --------- | --- | --- | --- | --- |
p
We define four types of returns according to their time frames as follows:

|     |     |      | (cid:18)      | (cid:19) |      | (cid:18)       | (cid:19) |
| --- | --- | ---- | ------------- | -------- | ---- | -------------- | -------- |
|     |     |      | Close         |          |      | Open           |          |
|     |     | r =  | ln tt         | ,        | r    | = ln           | t ,      |
|     |     | OC,t |               |          | OO,t |                |          |
|     |     |      | Open          |          |      | Open           |          |
|     |     |      | ot            |          |      |                | t−1      |
|     |     |      | (cid:18) Open | (cid:19) |      | (cid:18) Close | (cid:19) |
t
|     |     | r =  | ln    | t , | r    | = ln  | ,   |
| --- | --- | ---- | ----- | --- | ---- | ----- | --- |
|     |     | CO,t |       |     | CC,t |       |     |
|     |     | nt−1 | Close |     |      | Close |     |
t−1
where r , r , r , and r represent, respectively, the Open-to-Close,
|     |     | OC,t OO,t | CO,t | CC,t |     |     |     |
| --- | --- | --------- | ---- | ---- | --- | --- | --- |
Open-to-Ope n, Close-to-Open, and Close-to-Close returns at time t (mea-
sured in trtading days). Furthermore, Open and Close denote the opening
t
t
|     | and | clnosing prices | at time | t, respectively. |     |     |     |
| --- | --- | --------------- | ------- | ---------------- | --- | --- | --- |
The binary response variables for the classification problems are defined
as follows:
i
|     | r   |     |     | (cid:40) |          |       |     |
| --- | --- | --- | --- | -------- | -------- | ----- | --- |
|     |     |     |     | 0        | if r ≤ Q | (r ), |     |
|     |     |     |     |          | w,t 0.75 | w     |     |
I+ = (2)
|     | p   |     | w,t |     |          |       |     |
| --- | --- | --- | --- | --- | -------- | ----- | --- |
|     |     |     |     | 1   | if r > Q | (r ), |     |
|     |     |     |     |     | w,t 0.75 | w     |     |
(cid:40)
|     |     |     |     | 0   | if r ≥ Q | (r ), |     |
| --- | --- | --- | --- | --- | -------- | ----- | --- |
| e   |     |     |     |     | w,t 0.25 | w     |     |
I− = (3)
w,t
|     |     |     |     | 1   | if r < Q | (r ), |     |
| --- | --- | --- | --- | --- | -------- | ----- | --- |
|     |     |     |     |     | w,t 0.25 | w     |     |
r
wherew denotes thereturn time window, such thatw ∈ {OC,OO,CO,CC},
Pand
Q (r ) and Q (r ) represent the 75th and 25th percentiles of the
|     |     | 0.75 w | 0.25 | w   |     |     |     |
| --- | --- | ------ | ---- | --- | --- | --- | --- |
9
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
entire sample of returns, r , with the time frame w, respectively. As follows
w
from (2) and (3), the returns above the 75th percentile are considered signif-
e
icantly positive, while the returns below the 25th percentile are considered
significantly negative.
i
To generate the bag-of-words dataset for the Random Forest model, we
v
first removed noise and stop words from the news headlines. After tokenizing
the headlines, parts of speech were detected using the spacy 3.6 library in
e
Python, and lemmatization was performed to extract word roots. In the next
step, the tokens were converted to vectors using the Term Frequency–Inverse
r
Document Frequency (TF-IDF) vectorizer from the scikit-learn library in
Python, which measures not only how freque ntly a word appears in a doc-
ument, but also how rare the word is acrosrs all documents. This technique
helps reduce the impact of common woerds while emphasizing distinctive key-
words.
TofittheRandomForestmodel, wespliteachasset’sdatasetintotraining
e
and testing sets, with 80% of the samples used for training and 20% for
testing. The model’s hyperparameters were tuned using cross-validation. We
p
fit eight distinct Random Forest models for each asset, each corresponding
to a different response variable. The outputs for each asset, which can be
considered predictive insights for the next steps, are defined as follows:
t
o
IP+ = P(I+ = 1) = P(r > Q (r )), (4)
w,t w,t w,t 0.75 w
n IP− = P(I− = 1) = P(r < Q (r )). (5)
w,t w,t w,t 0.25 w
In other word s, for each asset and for each time frame w, we build and train
twoRandotmForestclassificationmodelsthatestimatetheprobabilitiesIP−
w,t
and InP+ that the news headlines posted over the news collection window
w,t
(as shown in Figure 2) have, respectively, negative and positive impacts on
the asset return r . These estimates are then used as exogenous variables
i w,t
inrthe return forecasting model, as explained in the next section.
To make our approach practically feasible, the news data used for the
p
response variables correspond to a specific time interval preceding the return
prediction window. In particular, we use the news data from the previous 24
e
hours before the relevant return window. This rule is illustrated in Figure 2.
Performance metrics of the Random Forest classification models across
r
differentreturnhorizonsandpositive/negativeimpactclassificationsaresum-
Pmarized in Table 2. Each metric is averaged over all investigated financial
10
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
e
i
v
e
r

r
Figure 2: Data collection and return prediction windows for each of the Open-to-Close
(r ),Open-to-Open(r ),Close-to-Opene(r ),andClose-to-Close(r )returns.
|     | OC,t |     | OO,t |     |     |     | CO,t |     | CC,t |     |
| --- | ---- | --- | ---- | --- | --- | --- | ---- | --- | ---- | --- |
assets. In the test sets, observatieons with predicted probabilities of 0.25 or
higher were classified as belonging to the impactful class, while those below
this threshold were assigned tpo the non-impactful class. The threshold value
was selected to maximize the average performance across both classes in an
imbalanced dataset where n on-impactful news headlines dominate. The per-
formance metrics includetoverall accuracy, F1-scores for both impactful and
|     | non-impactful | news, | o and | ROC-AUC |     | values. |     |     |     |     |
| --- | ------------- | ----- | ----- | ------- | --- | ------- | --- | --- | --- | --- |
Table 2: Average performance metrics of Random Forest classification models for predict-
n
ing positively and negatively impactful news across different return time frames.
|     |     |     |     |     |     |     | Response | Variable |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | --- |
AveragetMetric
|     |     |     |     | I+   | I−   | I+   | I−   | I+ I−     | I+   | I−   |
| --- | --- | --- | --- | ---- | ---- | ---- | ---- | --------- | ---- | ---- |
|     |     |     |     | OC,t | OC,t | OO,t | OO,t | CO,t CO,t | CC,t | CC,t |
n
|     | Accuracy     |     | 0.905 |     | 0.895 | 0.907 | 0.898 | 0.901 0.888 | 0.915 | 0.903 |
| --- | ------------ | --- | ----- | --- | ----- | ----- | ----- | ----------- | ----- | ----- |
|     | F1 Impactful |     | 0.813 |     | 0.796 | 0.815 | 0.796 | 0.809 0.783 | 0.835 | 0.807 |
i
r F1 Non-Impactful 0.936 0.929 0.938 0.932 0.933 0.924 0.943 0.935
|     | ROC-AUC |     | 0.937 |     | 0.935 | 0.930 | 0.925 | 0.940 0.933 | 0.946 | 0.940 |
| --- | ------- | --- | ----- | --- | ----- | ----- | ----- | ----------- | ----- | ----- |
p
The evaluation metrics used here are as follows. Accuracy is the propor-
e
|     | tion of instances |     | correctly | classified |     | and | is computed | as: |     |     |
| --- | ----------------- | --- | --------- | ---------- | --- | --- | ----------- | --- | --- | --- |
r
|     |     |     |          |     |     | TP  | +TN |     |     |     |
| --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | Accuracy |     | =   |     |     | ,   |     | (6) |
| P   |     |     |          |     | TP  | +TN | +FP | +FN |     |     |
11
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
where TP, TN, FP, and FN stand for true positives, true negatives, false
| positives, | and | false negatives, |     | respectively. |     |     |     |     |     |
| ---------- | --- | ---------------- | --- | ------------- | --- | --- | --- | --- | --- |
e
F1-score is the harmonic mean of recall and precision, and for the posi-
| tive (impactful) |     | class | is computed | as: |     |     |     |     |     |
| ---------------- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- |
i
Precision·Recallv
|     |     | F1-score |     | = 2· |     | ,   |     |     | (7) |
| --- | --- | -------- | --- | ---- | --- | --- | --- | --- | --- |
Precision+Recall
e
|       |           |     | TP  |     |          | TP  |     |     |     |
| ----- | --------- | --- | --- | --- | -------- | --- | --- | --- | --- |
| where | Precision | =   |     | and | Recall = |     | .   |     |     |
|       |           | TP  | +FP |     | TrP      | +FN |     |     |     |
ROC-AUC (Receiver Operating Characteristic – Area Under the Curve)

is the area under the ROC curve, obtained by plotting the true positive
|          |     | TP     |     |           | r             |     |     | FP     |     |
| -------- | --- | ------ | --- | --------- | ------------- | --- | --- | ------ | --- |
| rate TPR | =   |        | vs. | the false | positive rate | FPR | =   |        | at  |
|          |     | TP +FN |     |           |               |     |     | FP +TN |     |
e
variousthresholdsettings. GreaterROC-AUCindicatessuperiordiscriminative
performance.
e
Theprobabilitythresholdof0.25balancesclassificationperformanceacross
classesinthepresenceofimbalance. Whilethresholdtuningcanimprovepre-
p
cision–recall trade-offs, the primary objective of our classification stage is not
hard-labelpredictionbutratherthegenerationofimpactprobabilities, which

are subsequently incorporated as exogenous variables in the FIGARCH mod-
probabiltistic
| els. Within | this |     |     | framework, | the high | ROC-AUC | values | reported |     |
| ----------- | ---- | --- | --- | ---------- | -------- | ------- | ------ | -------- | --- |
tohat
in Table 2 confirm the classifier possesses strong discriminative ability,
ensuring that the probability estimates are reliable inputs for the subsequent
| volatility   | modenling. |        |            |       |     |     |     |     |     |
| ------------ | ---------- | ------ | ---------- | ----- | --- | --- | --- | --- | --- |
| 2.4. FIGARCH |            | Return | Prediction | Model |     |     |     |     |     |

In thistsection, we have adjusted the return prediction FIGARCH(1,1)
model by sentiment-driven exogenous sets of variables derived in Sections 2.2
n
and 2.3. The FIGARCH model, introduced by Baillie et al. [? ], extends
the GARCH family of models. Beyond capturing volatility clustering and
i
providing r reliable in-sample estimates [? ? ], the FIGARCH model is specif-
ically designed to account for the long-memory characteristics observed in
p
financial volatility. The auto-regressive mean equation is modified to our ap-
proach by including sentiment-driven exogenous variables. The augmented
e
r
P
12
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
| FIGARCH(p,q) |     |     | model | is described |     | as follows: |     |     |     |     |
| ------------ | --- | --- | ----- | ------------ | --- | ----------- | --- | --- | --- | --- |
|              |     |     | ℓ     |              |     |             |     |     | e   |     |
(cid:88)
+γX⊤
|     | r   | = µ+ |          | α r   |           | +ε ,   |          |      |          |     |
| --- | --- | ---- | -------- | ----- | --------- | ------ | -------- | ---- | -------- | --- |
|     |     | t    |          | i t−i |           | t t    |          |      |          |     |
|     |     |      | i=1      |       |           |        |          |      | i        |     |
|     | ε   | = σ  | ·z ,     | z ∼   | t(0,1,ν), |        |          |      | v        | (8) |
|     |     | t t  | t        | t     |           |        |          |      |          |     |
|     |     |      |          |       |           |        | (cid:32) |      | (cid:33) |     |
|     |     |      | q        |       |           | p      |          | q    |          |     |
|     |     |      | (cid:88) |       | (cid:88)  |        | (cid:88) |      |          |     |
|     | σ2  | = ω  | +        | ϕ ε2  | +         | β σ2 + |          | ϕeε2 | (1−L)d,  |     |
|     |     |      |          | i     |           | j      |          | i    |          |     |
|     | t   |      |          | t−i   |           | t−j    |          | t−i  |          |     |
|     |     |      | i=1      |       | j=1       |        | i=1      |      |          |     |
r
wherer islog-returnattimet, µisexpectedlog-returnfortheasset, α isthe
|     | t   |     |     |     |     |     |     |     |     | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
X ⊤
coefficient of ith auto-regressive (AR) term, is the vector of exogenous
t
variables at time t, γ is the corresponding croefficients vector, σ2 is the condi-
t
tional volatility at time t, ε is the shoeck term at time t, z ∼ t(0,1,ν ) is a
|     |     |     |     | t   |     |     |     |     | t   | St  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
standardized Student’s t-distributed innovation term with mean 0, variance
1, and ν degrees of freedom, ω is the constant term in the volatility equation,
e
α is the impact of past squared shocks (ARCH term), β is the persistence of
past volatility (GARCH term), L is the lag operator, and d is the fractional
p
| differencing |     | parameter. |     |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
In what follows, we set p = 1, q = 1, and ℓ = 1 in (8). This choice is based

on both theoretical and empirical reasons. From a modeling standpoint,
t
the FIGARCH(1,1) framework is seen as the most efficient and empirically
o
reliable option, capturing the key long-memory features of financial volatility
| without | adding | unnecessary |     |     | complexity. |     |     |     |     |     |
| ------- | ------ | ----------- | --- | --- | ----------- | --- | --- | --- | --- | --- |
Returnprednictiontime-seriesmodelstypicallyassumethattheerrorterms
follow a normal distribution with stationary deviations, enabling the use of
the ordinary least squares (OLS) method to estimate parameters [? ]. In
this study,twe have considered a fat-tailed distribution, specifically Student’s
| t-distrnibution, |     | to  | better | fit the | data | samples. |     |     |     |     |
| ---------------- | --- | --- | ------ | ------- | ---- | -------- | --- | --- | --- | --- |
The parameters of the FIGARCH model were estimated using maximum
likeliihood estimation (MLE). We employed the arch 7.2.0 Python library,
wrhich optimizes the joint log-likelihood function of the conditional mean
equation(includingARtermsandsentiment-drivenexogenousvariables)and
p
the time-varying variance equation. The optimization was performed using
the Sequential Least Squares Programming (SLSQP) algorithm implemented
e
in the scipy.optimize v1.15.3 module. This algorithm enforces standard
parameter constraints, including bound restrictions on the fractional differ-
r
encing parameter (d ∈ [0,1]), non-negativity constraints on the volatility
Pequation
parameters (ω ≥ 0, ϕ ≥ 0, β ≥ 0), and stationarity constraints
|     |     |     |     |     | i   | j   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
13
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
for the mean process. In our implementation, estimation reliability was fur-
ther ensured by relying on the convergence diagnostics provided by the arch
e
7.2.0 library. Robust covariance estimation (cov_type="robust") is com-
puted only when the optimizer converges successfully, which guarantees that
i
the reported results are based on valid solutions. The arch_model.fit()
v
routine also provides detailed convergence information, including the opti-
mizer’s exit status, the number of iterations, and the number of function
e
evaluations. In addition, our code explicitly excluded any cases where con-
vergence was not achieved through error handling, ensuring that all results
r
presentedinthisstudyarebasedexclusivelyonsuccessfullyconvergedmodels
without parameter boundary violations.
r
3. Empirical Results e
In this section, we present the empirical evaluation of the proposed senti-
e
ment-driven FIGARCH(1,1) model for return prediction. The objective is
to assess the predictive power of incorporating news-based sentiment metrics
p
and impact probabilities into financial time-series modeling. Using a dataset
that includes 347,500 asset-specific news headlines and corresponding finan-
cial data from March 1, 2022, to January 31, 2025, we conduct a series of
t
experiments across 36 assets from the stock, cryptocurrency, and commodity
markets using the eontire dataset.
For each asset, we begin by defining the sets of exogenous variables pro-
duced in Sectionns 2.2 and 2.3. The time series from Section 2.2 are the
proposed average sentiment scores for each group of positive, negative, and
neutral daily published news headlines. The variables from Section 2.3 are
probabilityttime series representing the likelihood that positive or negative
news nheadlines influence financial returns across various time frames. After
verifying the stationarity of all exogenous time series using the Dickey–Fuller
unit root test, we fit augmented FIGARCH models that incorporate these
i
erxogenous variables, alongside a traditional FIGARCH model used as a
benchmark. We then evaluate their performance by comparing goodness-
p
of-fit metrics and predictive accuracy across the full dataset for different
assets and return horizons. In addition, we examine the proportion of sta-
e
tistically significant coefficients across model specifications. The augmented
FIGARCH(1,1) model and sets of exogenous variables are defined as follows:
r
P
14
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
|     |     |     | r = µ | +α  | r       | +γXs⊤ | +ε  |     |     |     |
| --- | --- | --- | ----- | --- | ------- | ----- | --- | --- | --- | --- |
|     |     |     | w,t   | w   | w w,t−1 |       | t t |     |     |     |
e
|       |     |        | ε = σ  | ·z ,  | z ∼      | t(0,1,ν), |            |         |              |     |
| ----- | --- | ------ | ------ | ----- | -------- | --------- | ---------- | ------- | ------------ | --- |
|       |     |        | t      | t t   | t        |           |            |         |              | (9) |
|       |     |        |        |       |          |           | (cid:0)    | (cid:1) |              |     |
|       |     |        | σ2 = ω | +ϕ    | ε2 +β    | σ2        | + ϕ ε2     | (1−L)d, |              |     |
|       |     |        | t      | 1     | t−1      | 1 t−1     | 1 t−1      |         | i            |     |
| where |     |        |        |       |          |           |            |         | v            |     |
|       | X1  | = {IP+ | ,IP−   | },    |          |           |            |         |              |     |
|       |     |        | OC     | OC    |          |           |            | e       |              |     |
|       | X2  | {IP+   | ,IP−   |       |          |           |            |         |              |     |
|       |     | =      |        | },    |          |           |            |         |              |     |
|       |     |        | OO     | OO    |          |           |            |         |              |     |
|       | X3  | = {IP+ | ,IP−   | },    |          |           | r          |         |              |     |
|       |     |        | CC     | CC    |          |           |            |         |              |     |
|       | X4  | {IP+   | ,IP−   |       |          |           |            |         |              |     |
|       |     | =      |        | },    |          |           |            |         |              |     |
|       |     |        | CO     | CO    |          |           |            |         |              |     |
|       | X5  | = {IP+ | ,IP−   | ,IP+  | ,IP−     |           | ,IrP+ ,IP− |         | ,IP+ ,IP− }, |     |
|       |     |        | OC     | OC    | OO       | OO        | CC         | CC      | CO CO        |     |
|       | X6  | {AS+,  | AS−,   | ASO}, |          |           |            |         |              |     |
|       |     | =      |        |       |          | e         |            |         |              |     |
|       |     |        | t      | t     | t        |           |            |         |              |     |
|       | X7  | {IP+   | ,IP−   |       | IP+ ,IP− |           | AS+, AS−,  |         | ASO},        |     |
|       |     | =      |        | ,     |          | ,         |            |         |              |     |
|       |     |        | OC     | OC    | OO       | OO        | t          | t       | t            |     |
e
|     | X8  | = {IP+ | ,IP− | ,IP+  | ,IP− |     | ,IP+ ,IP− |     | ,IP+ ,IP− , |     |
| --- | --- | ------ | ---- | ----- | ---- | --- | --------- | --- | ----------- | --- |
|     |     |        | OC   | OC    | OO   | OO  | CC        | CC  | CO CO       |     |
|     |     | AS+,   | AS−, | ASO}, |      |     |           |     |             |     |
|     |     |        | t    | t     | tp   |     |           |     |             |     |
and
(cid:40)
|     |     |     |     | {1 ,2,6,7}   |     | if  | w ∈ {OC,OO}, |     |     |      |
| --- | --- | --- | --- | ------------ | --- | --- | ------------ | --- | --- | ---- |
|     |     |     | s ∈ |              |     |     |              |     |     | (10) |
|     |     |     |     | t{1,2,...,8} |     | if  | w ∈ {CC,CO}. |     |     |      |
o
The parameter s defined in (10) determines the exogenous set included
in the model based on the prediction time frame. The assumption is that for
predictinng
models returns in Open-to-Close and Open-to-Open time frames,
we do not use impact probability variables for Close-to-Close and Close-to-
Open time fr ames. The reason is that the data collection window for com-
puting thetvariables in the Close-to-Close and Close-to-Open time frames
overlanps with the prediction window for returns in the Open-to-Close and
Open-to-Open time frames. In other words, for predicting returns in a spe-
cificiperiod of time, we do not use any information from that period itself,
| arnd | all information |     | used | for | forecasting | comes | from | past | periods. |     |
| ---- | --------------- | --- | ---- | --- | ----------- | ----- | ---- | ---- | -------- | --- |
The augmented model in (9) is fitted for all 37 assets in each of the four
p
time frames, as well as for every set of exogenous variables (8 exogenous sets)
in addition to the benchmark FIGARCH model without exogenous variables
e
(the base model). Considering that we only have Open-to-Open data for
Brent Oil in the commodity market, in total, we have estimated parameters
r
for a total of 1011 variants, including the augmented model in (9) and the
Pbenchmark
|     |     | model | obtained |     | by setting | γ   | in (9) equal | to  | zero. |     |
| --- | --- | ----- | -------- | --- | ---------- | --- | ------------ | --- | ----- | --- |
15
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
Table 3 summarizes the number of times each coefficient was statistically
significant across all model estimations, considering various sets of exoge-
e
nous variables and time frames. Among the core FIGARCH parameters,
the degrees of freedom parameter (ν) and the long-memory component (d)
i
exhibit the highest levels of significance, with ν significant at the 1% level
v
in 689 out of 1000 estimations. The GARCH term (β) is also frequently
significant, while the ARCH term (ϕ) shows relatively limited significance,
e
indicatingthatvolatilitypersistenceplaysamorecriticalrolethanshort-term
shocks. Regarding the exogenous variables, the impact probability features
r
(IP+ ,IP− ,IP+ , etc.) demonstrate strong statistical relevance, partic-
OO OC OC
ularly in the Open-to-Open and Close-to-Ope n return windows. Sentiment
score aggregates (AS+ and AS−) are also frerquently significant, whereas neu-
tral sentiment coefficients (ASO) wereerarely significant across model spec-
ifications (only 19 out of 353 at the 1% level). Nevertheless, we included
neutral sentiment to ensure transparency and robustness of the analysis.
e
Since the FinBERT model produces positive, negative, and neutral senti-
ment scores, evaluating all categories avoids potential bias from selective
p
exclusion of variables ex ante. Empirically, our findings confirm that neu-
tral sentiment provides little explanatory power compared to positive and
negative sentiment, which is consistent with the theoretical expectation that
t
market behavior is primarily driven by polarized sentiments. These results
o
highlight the importance of incorporating sentiment into volatility model-
ing frameworks. Furthermore, sentiment with positive and negative impacts
may exhibit diffnerent predictive power, and their contributions to volatility
models vary depending on the time frame.
t
n
i
r
p
e
r
P
16
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
Table3: Numberofstatisticallysignificantcoefficientsatdifferentconfidencelevelsacross
models estimated for all assets, using various sets of exogenous variables in the Open-to-
Open,Open-to-Close,Close-to-Close,andClose-to-Opentimeframes. Foereachcoefficient,
thetableshowsthetotalnumberoftimesitwasincludedandhowoftenitwasstatistically
| significant | at the 10%, | 5%, and | 1% confidence | levels, respectively. |     |
| ----------- | ----------- | ------- | ------------- | --------------------- | --- |
i
v
| Coefficient | Number |     |     | Confidence | Level |
| ----------- | ------ | --- | --- | ---------- | ----- |
of models
e
|     |      |     | 10%         | 5%            | 1%          |
| --- | ---- | --- | ----------- | ------------- | ----------- |
| µ   | 1000 |     | 582 (58.2%) | 534 r (53.4%) | 479 (47.9%) |
| ω   | 1000 |     | 430 (43.0%) | 383 (38.3%)   | 330 (33.0%) |
| ϕ   | 1000 |     | 105 (10.5%) |  86 (8.6%)    | 69 (6.9%)   |
| d   | 1000 |     | 619 (61.9%) | r582 (58.2%)  | 514 (51.4%) |
| β   | 1000 |     | 570 (57.0%) | 540 (54.0%)   | 490 (49.0%) |
e
| ν   | 1000 |     | 784 (78.4%) | 761 (76.1%) | 689 (68.9%) |
| --- | ---- | --- | ----------- | ----------- | ----------- |
| α   | 144  |     | 50 (34.7%)  | 46 (31.9%)  | 43 (29.9%)  |
OC
| α   | 140 |     | 36 e(25.7%) | 35 (25.0%) | 31 (22.1%) |
| --- | --- | --- | ----------- | ---------- | ---------- |
OO
| α CC | 287 |     | 107 (37.3%) | 101 (35.2%) | 88 (30.7%) |
| ---- | --- | --- | ----------- | ----------- | ---------- |
| α    | 285 |     | 81 (28.4%)  | 77 (27.0%)  | 64 (22.5%) |
CO
p
IP+
|     | 424 |     | 212 (50.0%) | 184 (43.4%) | 150 (35.4%) |
| --- | --- | --- | ----------- | ----------- | ----------- |
OC
| IP− | 424 |     | 213 (50.2%) | 197 (46.5%) | 156 (36.8%) |
| --- | --- | --- | ----------- | ----------- | ----------- |
OC
| IP+ |     |  246 |         |             |             |
| --- | --- | ---- | ------- | ----------- | ----------- |
|     | 423 |      | (58.2%) | 228 (53.9%) | 193 (45.6%) |
OO
| IP− | 423 | t256 | (60.5%) | 239 (56.5%) | 207 (48.9%) |
| --- | --- | ---- | ------- | ----------- | ----------- |
OC
| IP+ | 216 |     | 121 (56.0%) | 115 (53.2%) | 100 (46.3%) |
| --- | --- | --- | ----------- | ----------- | ----------- |
o
IP− CC
|     | 216 |     | 120 (55.6%) | 108 (50.0%) | 86 (39.8%) |
| --- | --- | --- | ----------- | ----------- | ---------- |
CC
| IP+ | 216 |     | 123 (56.9%) | 111 (51.4%) | 93 (43.1%) |
| --- | --- | --- | ----------- | ----------- | ---------- |
CO
| IP− | n216 |     |             |             |            |
| --- | ---- | --- | ----------- | ----------- | ---------- |
|     |      |     | 110 (50.9%) | 101 (46.8%) | 91 (42.1%) |
CO
| AS+ | 353 |     | 190 (53.8%) | 177 (50.1%) | 156 (44.2%) |
| --- | --- | --- | ----------- | ----------- | ----------- |
ASO
|     |  353 |     | 24 (6.8%)   | 23 (6.5%)   | 19 (5.4%)   |
| --- | ---- | --- | ----------- | ----------- | ----------- |
| AS− | 353  |     | 212 (60.1%) | 188 (53.3%) | 169 (47.9%) |
t
n
To evaluate the predictive performance of the proposed FIGARCH mod-
els,iwe estimate separate models that incorporate various sets of sentiment-
drriven exogenous variables, X1,...,X8. These models are compared against
a benchmark FIGARCH model without any exogenous inputs (denoted as
p
Base) to determine the added value of including external information. The
evaluation relies on three standard performance metrics: the Akaike Infor-
e
mation Criterion (AIC), the Bayesian Information Criterion (BIC), and the
Log-Likelihood Function (LLF). Both AIC and BIC are likelihood-based cri-
r
teria that balance model fit and complexity by penalizing the inclusion of
Pextra
variables, with lower values indicating better performance. The LLF,
17
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
on the other hand, measures the likelihood of observing the data given the
model parameters, with higher values signifying a better fit. Collectively,
e
these criteria provide a comprehensive assessment of model quality, captur-
| ing | both in-sample fit | and | parsimony. |     |     |     |     |
| --- | ------------------ | --- | ---------- | --- | --- | --- | --- |
i
v
150000
Open-to-Open
| CIA    |     |     |     |     | e   |     | Open-to-Close |
| ------ | --- | --- | --- | --- | --- | --- | ------------- |
| 100000 |     |     |     |     |     |     | Close-to-Open |
Close-to-Close
50000
|     | 0   |     |     |     | r   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
150000
| CIB 100000 |       |     |     |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- | --- | --- |
|            | 50000 |     |     | r   |     |     |     |
0
|     | 0   |     |     | e   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
FLL −20000
−40000
| −60000 |     |     | e   |     |     |     |      |
| ------ | --- | --- | --- | --- | --- | --- | ---- |
|        | 1 2 | 3   | 4   | 5   | 6   | 7 8 |      |
|        | X X | X   | X   | X   | X   | X X | Base |
Exogenous Variables Set
p
Figure 3: Model performance across different exogenous variable sets for stocks. The
metrics include average AIC, average BIC, and average LLF. Lower AIC/BIC and higher
mod el
| LLF | values indicate better |     | fit. |     |     |     |     |
| --- | ---------------------- | --- | ---- | --- | --- | --- | --- |
t
Figure 3 illustratoes the performance of the FIGARCH model across vari-
ous sets of exogenous variables corresponding to stock market assets. For the
Close-to-Closentimeframe, modelsincorporatingvariables fromallexogenous
sets show significant improvements over the benchmark Base model for as-
sets in the stock market. However, nearly all models with sentiment-driven

X4
exogenous variables (except the one that incorporates in the Open-to-
t
Close time frame) outperform the benchmark model in the stock market.
n
In the Open-to-Close setting shown in Figure 4, which illustrates the per-
formance of models in the cryptocurrency market, all variable sets except
i
the set X2 produce lower AIC and higher LLF than the benchmark model,
r
indicating strong predictive value from sentiment-driven features. The same
p
applies in the Close-to-Open setting, where X1 is excluded. However, cryp-
tocurrency models show relatively flat performance across all variable sets,
esuggesting
|     | that sentiment |     | signals may | be less | informative | in this | market. |
| --- | -------------- | --- | ----------- | ------- | ----------- | ------- | ------- |
Figure 5 illustrates the performance of FIGARCH models for Brent Oil
racross (X2, X6,
|     | different exogenous |     | variable sets |     | and | Base) under | the Open- |
| --- | ------------------- | --- | ------------- | --- | --- | ----------- | --------- |
to-Open time frame. Both AIC and BIC show notable improvements when
P
18
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

4000
2000
0
−2000
−4000
CIA
Open-to-Open
Open-to-Close Close-to-Open
Close-to-Close
4000
2000
0
−2000
−4000
CIB
2000
1000
0
−1000
−2000
1 2 3 4 5 6 7 8
X X X X X X X X Base
Exogenous Variables Set
FLL
d
e
w
e
i
v
e
r
r
Figure 4: Model performance across differenteexogenous variable sets for cryptocurrency
assets. Average AIC, BIC, and LLF are used as model selection criteria.
e
sentiment-based exogenous variables are included, with X2 achieving the
largest reduction, indicating ipts stronger contribution to model fit. Similarly,
LLF values are consistently higher for augmented models compared to the
benchmark (Base), further confirming the enhanced explanatory power of
sentiment information. Overall, the results demonstrate that incorporating
t
sentiment-derived exogenous variables substantially improves the goodness-
o
of-fit of FIGARCH models in the Brent Oil market, even though the analysis
is restricted to the Open-to-Open horizon due to data availability.
n
For completeness and ease of reference, the numerical results correspond-
ing to the figures presented in this section are reported in Tables A.4–A.7
in Appendix Appendix A. These tables provide the full set of model per-
t
formance metrics across assets, return horizons, and exogenous variable sets,
therebny facilitating detailed inspection and ensuring transparency and repro-
ducibility of the findings.
i
r
4. Conclusion
p
Thisstudyproposedasentiment-awareframeworkforpredictingfinancial
returns by integrating machine learning classification and volatility model-
e
ing techniques. Specifically, we employed a Random Forest classifier to assess
the likelihood that news headlines affect asset returns across multiple time
r
frames and used FinBERT sentiment scores to construct interpretable sen-
Ptiment variables. These features were incorporated as exogenous variables
19
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

2000
1000
0
−1000
−2000
CIA
Open-to-Open
2000
1000
0
−1000
−2000
CIB
1000
500
0
−500
−1000
2 6
X X Base
Exogenous Variables Set
FLL
d
e
w
e
i
v
e
r
r
Figure 5: Model performance across differenteexogenous variable sets for commodity mar-
ket (Brent Oil). Brent Oil is only investigated in Open-to-Open time frame due to data
availability. AIC, BIC, and LLF are used as model selection criteria.
e
into an extended FIGARCH(1,1) model to assess their influence on volatility
p
and return dynamics. Empirical evaluations on a large-scale dataset cover-
ing 37 financial assets from stock, cryptocurrency, and commodity markets
demonstrated that incorporating sentiment-driven variables improves model
t
performance in terms of fit and explanatory power, especially in Open-to-
o
Open and Close-to-Open time frames. Our results highlight the predictive
value of combining textual sentiment indicators with time-series modeling for
n
better capturing the long-memory behavior of financial volatility.
Beyond statistical improvements, the results have clear financial impli-
cations. The significance of negative sentiment and negative impact proba-
bilities, patrticularly in the Open-to-Open and Close-to-Open horizons, sup-
portsntheories of asymmetric volatility and loss aversion, where adverse news
triggers disproportionately strong market reactions. The stronger predictive
powier of overnight sentiment variables is consistent with market microstruc-
trure research, which shows that information released after trading hours is
abruptly incorporated at the market’s opening, resulting in volatility shocks.
p
At the same time, the negligible role of neutral sentiment confirms that mar-
kets respond primarily to salient signals rather than ambiguous news, con-
e
sistent with attention-based trading theories. Finally, differences in the pre-
dictive power of sentiment variables across asset classes, strong for equities,
r
weaker for cryptocurrencies, and macro-driven for commodities, illustrate
P
20
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
how sentiment interacts with the informational structures specific to each
market. These insights highlight the economic significance of our findings,
e
demonstrating that sentiment-enhanced FIGARCH models not only improve
statistical fit but also reveal behavioral mechanisms underlying asset volatil-
i
ity.
v
This research provides a promising tool for market participants aiming
to integrate qualitative information into quantitative forecasts. The primary
e
contribution of this study is to demonstrate how sentiment-derived variables
can be systematically integrated into FIGARCH models to improve volatility
r
forecasting across multiple return horizons. Unlike much of the recent litera-
ture that emphasizes purely machine learning approaches, our framework re-
tains the volatility clustering and long-memrory characteristics of FIGARCH,
while incorporating predictive signalsefrom FinBERT sentiment indicators
and Random Forest-derived news impact probabilities. This design choice
reflects the goal of bridging advanced NLP-based sentiment features with
e
an established econometric framework, rather than replacing it with black-
box methods. Nevertheless, recent state-of-the-art time-series models such
p
as LSTMs, Transformers, and hybrid econometric–ML structures represent
complementary directions. Future work could benchmark our framework
against such alternatives or explore richer embedding-based representations,
t
thereby extending the scope of our findings without diminishing the distinct
o
contribution of this paper.
n
Acknowledgment
This research work was supported by the discovery grant RGPIN-2020-
04782fromtheNaturalSciencesandEngineeringResearchCouncilofCanada
t
(NSERC).
n
Declaration of generative AI and AI-assisted technologies in the
i
writing process
r
pDuringthepreparationofthiswork, theauthorsusedGrammarlytocheck
spelling, grammar, andwordusage. Afterusingthistool/service, theauthors
ereviewed and edited the content as needed and take full responsibility for the
content of the published article.
r
Appendix A. Supplementary Tables
P
21
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
e
i
v
e
Table A.4: Average model goodness-of-fit metrics (AIC, BIC, and LLF) for Stock and
Cryptocurrency markets in the Open-to-Open time frame across different exogenous vari-
| able sets. |     |           |          |          | r       |         |
| ---------- | --- | --------- | -------- | -------- | ------- | ------- |
| Market     |     | Exogenous |          | Averag e | Average | Average |
|            |     | Set       |          | ArIC     | BIC     | LLF     |
|            |     | X1        |          | e-914.36 | -884.08 | 466.18  |
|            |     | X2        |          | -910.02  | -879.73 | 464.01  |
|            |     | X3        | e-906.93 |          | -876.65 | 462.47  |
|            |     | X4        |          | -908.16  | -877.88 | 463.08  |
X5
| Cryptocurrency |     | p-911.65 |     |     | -861.17 | 470.82 |
| -------------- | --- | -------- | --- | --- | ------- | ------ |
X6
|     |     |     |     | -934.03 | -897.02 | 478.02 |
| --- | --- | --- | --- | ------- | ------- | ------ |
|     |     | X7  |     | -934.46 | -883.99 | 482.23 |

|     |     | X8  |     | -937.46 | -873.53 | 487.73 |
| --- | --- | --- | --- | ------- | ------- | ------ |
t
|     |     | Base |     | -917.23 | -897.01 | 464.62 |
| --- | --- | ---- | --- | ------- | ------- | ------ |
o
|     |     | X1  |     | 348.17   | 386.74   | -165.09   |
| --- | --- | --- | --- | -------- | -------- | --------- |
|     | nX2 |     |     | 28189.22 | 28227.78 | -14085.61 |
|     |     | X3  |     | 4122.47  | 4161.03  | -2052.23  |
|     |     | X4  |     | 4602.99  | 4641.55  | -2292.49  |

| Stockt |     | X5  |     | 546.07 | 610.34 | -258.04 |
| ------ | --- | --- | --- | ------ | ------ | ------- |
X6
|     |     |     |     | 2641.35 | 2688.48 | -1309.67 |
| --- | --- | --- | --- | ------- | ------- | -------- |
n
X7
|     |     |     |     | 3624.03 | 3688.30 | -1797.02 |
| --- | --- | --- | --- | ------- | ------- | -------- |
|     |     | X8  |     | 6752.55 | 6833.96 | -3357.28 |
i
|     |     | Base |     | 22104.68 | 22130.41 | -11046.34 |
| --- | --- | ---- | --- | -------- | -------- | --------- |
r
p
e
r
P
22
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
e
Table A.5: Average model goodness-of-fit metrics (AIC, BIC, and LLF) for Stock, Cryp-
i
tocurrency, and Commodity markets in the Open-to-Close time frame across different
v
| exogenous variable sets. |           |     |         |          |         |
| ------------------------ | --------- | --- | ------- | -------- | ------- |
| Market                   | Exogenous |     | Average | Aeverage | Average |
|                          | Set       |     | AIC     | BIC      | LLF     |
r
|     | X1  |     | -1815.73 | -1775.94 | 916.86 |
| --- | --- | --- | -------- | -------- | ------ |

X6
| Commodity |     |     | -2329.56 | -2280.92 | 1175.78 |
| --------- | --- | --- | -------- | -------- | ------- |
r
|     | Base |     | 2185.93 | 2212.47 | -1086.96 |
| --- | ---- | --- | ------- | ------- | -------- |
e
|                | X1          |           | -898.40 | -868.11  | 458.20 |
| -------------- | ----------- | --------- | ------- | -------- | ------ |
|                | X2          | e-1200.46 |         | -1170.17 | 609.23 |
|                | X3          |           | -898.21 | -867.93  | 458.11 |
|                | X4 p-893.77 |           |         | -863.49  | 455.89 |
| Cryptocurrency | X5          |           | -74.12  | -23.65   | 52.06  |

|     | X6  |     | -914.36 | -877.34 | 468.18 |
| --- | --- | --- | ------- | ------- | ------ |
t
|     | X7  |     | -618.13 | -567.66 | 324.07 |
| --- | --- | --- | ------- | ------- | ------ |
o
|     | X8   |     | -1200.99 | -1137.06 | 619.50 |
| --- | ---- | --- | -------- | -------- | ------ |
|     | Base |     | -907.01  | -886.79  | 459.50 |
n
X1
|       |     |     | 5673.89  | 5712.45  | -2827.94  |
| ----- | --- | --- | -------- | -------- | --------- |
|  X2   |     |     | 4936.47  | 4975.04  | -2459.24  |
| tX3   |     |     | 3807.30  | 3845.86  | -1894.65  |
| n     | X4  |     |          |          |           |
|       |     |     | 77210.99 | 77249.55 | -38596.50 |
| Stock | X5  |     | 2288.21  | 2352.48  | -1129.11  |
i
|     | X6  |     | 3420.73 | 3467.86 | -1699.37 |
| --- | --- | --- | ------- | ------- | -------- |
r
X7
|     |     |     | 4201.82 | 4266.09 | -2085.91 |
| --- | --- | --- | ------- | ------- | -------- |
p
|     | X8   |     | 4473.58  | 4554.99  | -2217.79 |
| --- | ---- | --- | -------- | -------- | -------- |
|     | Base |     | -2265.20 | -2239.47 | 1138.60  |
e
r
P
23
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
e
i
v
e
Table A.6: Average model goodness-of-fit metrics (AIC, BIC, and LLF) for Stock and
Cryptocurrency markets in the Close-to-Open time frame across different exogenous vari-
| able sets. |     |             |          | r       |          |
| ---------- | --- | ----------- | -------- | ------- | -------- |
| Market     |     | Exogenous   | Averag e | Average | Average  |
|            |     | Set         | ArIC     | BIC     | LLF      |
|            |     | X1          | e6039.89 | 6078.45 | -3010.95 |
|            |     | X2          | 4116.86  | 4155.42 | -2049.43 |
|            |     | X3 e4326.77 |          | 4365.33 | -2154.39 |
|            |     | X4          | 1640.01  | 1678.58 | -811.01  |
X5
| Stock |     | p5761.00 |     | 5825.27 | -2865.50 |
| ----- | --- | -------- | --- | ------- | -------- |
X6
|     |     |     | 8864.42  | 8911.55  | -4421.21 |
| --- | --- | --- | -------- | -------- | -------- |
|     |     | X7  | 17671.04 | 17735.31 | -8820.52 |

|     |     | X8  | 2513.35 | 2594.76 | -1237.68 |
| --- | --- | --- | ------- | ------- | -------- |
t
|     |     | Base | 6694.02 | 6719.75 | -3341.01 |
| --- | --- | ---- | ------- | ------- | -------- |
o
|     |     | X1  | 1632.18  | 1662.47  | -807.09 |
| --- | --- | --- | -------- | -------- | ------- |
|     | nX2 |     | -3743.14 | -3712.85 | 1880.57 |
|     |     | X3  | -3741.46 | -3711.18 | 1879.73 |
|     |     | X4  | -3742.95 | -3712.67 | 1880.48 |

| Crypttocurrency |     | X5  | -3730.44 | -3679.97 | 1880.22 |
| --------------- | --- | --- | -------- | -------- | ------- |
X6
|     |     |     | -3739.26 | -3702.24 | 1880.63 |
| --- | --- | --- | -------- | -------- | ------- |
n
X7
|     |     |     | -3732.58 | -3682.10 | 1881.29 |
| --- | --- | --- | -------- | -------- | ------- |
|     |     | X8  | -3723.48 | -3659.55 | 1880.74 |
i
|     |     | Base | -3766.38 | -3746.16 | 1889.19 |
| --- | --- | ---- | -------- | -------- | ------- |
r
p
e
r
P
24
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491

d
e
w
e
i
v
e
Table A.7: Average model goodness-of-fit metrics (AIC, BIC, and LLF) for Stock and
Cryptocurrency markets in the Close-to-Close time frame across different exogenous vari-
| able sets. |     |           |           |           | r        |           |
| ---------- | --- | --------- | --------- | --------- | -------- | --------- |
| Market     |     | Exogenous |           | Averag e  | Average  | Average   |
|            |     | Set       |           | ArIC      | BIC      | LLF       |
|            |     | X1        |           | e26684.01 | 26722.57 | -13333.01 |
|            |     | X2        |           | -180.56   | -142.00  | 99.28     |
|            |     | X3        | e14906.42 |           | 14944.98 | -7444.21  |
|            |     | X4        |           | 4859.20   | 4897.76  | -2420.60  |
X5
| Stock |     | p621.37 |     |     | 685.64 | -295.68 |
| ----- | --- | ------- | --- | --- | ------ | ------- |
X6
|     |     |     |     | 7878.49 | 7925.62 | -3928.24 |
| --- | --- | --- | --- | ------- | ------- | -------- |
|     |     | X7  |     | 2623.56 | 2687.83 | -1296.78 |

|     |     | X8  |     | 333.93 | 415.34 | -147.97 |
| --- | --- | --- | --- | ------ | ------ | ------- |
t
|     |     | Base |     | 143211.75 | 143237.47 | -71599.88 |
| --- | --- | ---- | --- | --------- | --------- | --------- |
o
|     |     | X1  |     | -898.41 | -868.12 | 458.20   |
| --- | --- | --- | --- | ------- | ------- | -------- |
|     | nX2 |     |     | 4924.45 | 4954.74 | -2453.23 |
|     |     | X3  |     | -898.31 | -868.02 | 458.15   |
|     |     | X4  |     | -893.79 | -863.50 | 455.89   |

| Crypttocurrency |     | X5  |     | 1127.77 | 1178.24 | -548.88 |
| --------------- | --- | --- | --- | ------- | ------- | ------- |
X6
|     |     |     |     | -914.39 | -877.38 | 468.20 |
| --- | --- | --- | --- | ------- | ------- | ------ |
n
X7
|     |     |     |     | -1137.08 | -1086.61 | 583.54 |
| --- | --- | --- | --- | -------- | -------- | ------ |
|     |     | X8  |     | -902.68  | -838.75  | 470.34 |
i
|     |     | Base |     | -907.02 | -886.80 | 459.51 |
| --- | --- | ---- | --- | ------- | ------- | ------ |
r
p
e
r
P
25
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5943491