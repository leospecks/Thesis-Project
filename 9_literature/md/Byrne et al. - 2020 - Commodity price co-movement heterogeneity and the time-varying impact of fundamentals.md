EuropeanReviewofAgriculturalEconomicsVol47(2)(2020)pp.499–528
doi:10.1093/erae/jbz017
AdvanceAccessPublication7May2019
Commodity price co-movement:
heterogeneity and the time-varying impact
of fundamentals
Joseph P. Byrne
†
, Ryuta Sakemoto
‡,§
and Bing Xu
†,*
†
School of Social Sciences, Heriot-Watt University, Edinburgh, UK;
‡ YJFX, Inc., Tokyo, Japan; §Keio University, Tokyo, Japan
ReceivedAugust2017;finalversionacceptedMarch 2019
ReviewcoordinatedbyDr.GiannisKaragiannis
Abstract
Thispaperextendsthetopicalliteratureontheco-movementanddeterminantsofpri-
mary commodity prices, byconsidering heterogeneity in commodities and timevari-
ation in the impact of fundamentals. We account for heterogeneity by employing a
dynamic hierarchical factor model, which decomposes commodities into global and
sectoral factors. Using a time-varying parameter factor augmented VAR model, we
shock global and sector-specific factors over time. We present plausible impulse
responsestodemandshocks,realinterestrateshocksandtoelevatedrisksduringthe
global financial crisis. We also identify that agricultural raw materials, food and
metalsrespondheterogeneouslytotheseshocks.
Keywords: commodityprices,co-movement,dynamichierarchicalfactormodels,
time-varyingparameterfactoraugmentedVARmodels
JELclassification: E3,F3,F4,G1
1. Introduction
Synchronised surges and declines in primary commodity prices have been
the catalyst for a lively recent debate about their commonalities and determi-
nants. These studies document a significant degree of co-movement in com-
modity prices, which can be modelled by a common factor. See recent
commodity prices research by Cuddington and Jerrett (2008); Vansteenkiste
(2009), Byrne, Fazio and Fiess (2013), Alquist and Coibion (2014), West
and Wong (2014), Daskalaki, Kostakis and Skiadopoulos (2014), Yin and
Han (2015), Antonakakis and Kizys (2015) and Alam and Gilbert (2017). A
potential criticism of factor models with a single common element, however,
is that they can forsake useful information. If commodity prices display
*Correspondingauthor:E-mail:b.xu@hw.ac.uk
©OxfordUniversityPressandFoundationfortheEuropeanReviewofAgriculturalEconomics2019;allrights
reserved.Forpermissions,pleasee-mail:journals.permissions@oup.com
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

500 J.P.Byrneetal.
important heterogeneity and/or are impacted by different fundamentals, then
a single factor extracted from all commodities may not fully reflect price
dynamics (Moench, Ng and Potter, 2013). We contribute therefore to the
commodities literature by decomposing commodity prices into common and
group factors using a hierarchical factor model and examine commodities’
relationshipswithfundamentals.
To the extent that commodity prices share common determinants, the lit-
erature is ambiguous as to what drives recent movements, possibly because
heterogeneity is unaccounted for, or the relative importance of determinants
change over time. Among possible determinants, Wolf (2008), Svensson
(2008), Frankel (2014) and Ratti and Vespignani (2015) have underlined that
shifts in global demand matter for commodity prices. Interest rates have been
emphasised by Frankel (2008, 2014) and Svensson (2008). Also, Beck
(1993, 2001) indicated that uncertainty is an important determinant of pri-
mary commodity prices. A limited number of empirical studies have so far
tested these different hypotheses and they rely on a time-invariant method-
ology (e.g. Byrne, Fazio and Fiess, 2013; Poncela, Senra and Sierra, 2014;
Ratti and Vespignani, 2015; Alam and Gilbert, 2017). Hence, previous work
on the determinants of commodity prices implicitly assumed that the impact
of macroeconomic shocks on commodity prices does not vary over time and
weinvestigatethisassumption.
There are several reasons to believe that the relationship between primary
commodity prices and macroeconomics fundamentals may be unstable
(Alvarez-Ramirez et al., 2012). For example, China has significantly
increased its market shares of global commodities following its rapid devel-
opment and this may impact demand effects (e.g. Kilian, 2009; Roache,
2012). Financial investors’ risk-bearing appetite and risk premium may vary
over time (Cheng and Xiong, 2014). Another potential cause of time-varying
commodityeffect is dueto variationin commoditymarket participants. Since
the 2000s, there has been a large inflow of investment capital from specula-
tors, which has added to commodity market activity from commercial
hedgers (e.g. farmers, producers and consumers) and non-commercial traders
suchasfinancialinstitutions(e.g.ChengandXiong,2014).1
This paper therefore empirically examines the relationship between com-
modity common factors and fundamentals, while accounting for heterogen-
eity and potential instability. Our analysis incorporates important innovations
relative to previous studies. First, we fully account for the determinants of
commodity prices while allowing for price heterogeneity using a dynamic
hierarchical factor model (DHFM). The existing literature typically explored
the impact of macro fundamentals on a single aggregate common factor. But
each sector may have a heterogeneous market structure, level of competition
and concentration and a differing elasticity of demand (e.g. Yin and Han,
1 Commoditymarketsfacilitaterisksharingamongabroadsetofagents,institutionalinvestors
have recently increased their portfolio allocations to commodities (Daskalaki, Kostakis and
Skiadopoulos,2014).
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

Commoditypriceco-movement 501
2015). The DHFM allows us to assess whether agricultural raw material,
food and metal sectors respond differently to macroeconomics shocks.
Importantly, the DHFM distinguishes commodity common and sector hetero-
geneous structures, and therefore it differs from the approach that extracts
commodityfactorsfromeachcommoditysector.
Our second contribution is to employ a time-varying parameter factor aug-
mented vector autoregression (TVP-FAVAR) model with stochastic volatility
to flexibly delineate the short-run impact of fundamentals. This approach
allows all parameters to evolve continuously, informing us when, and to
what extent, changes have occurred over time; rather than imposing an arbi-
trary sample split to account for changing dynamics. Our model also allows
for time-varying heteroskedasticity in the VAR innovations to account for
changes in the magnitude of shocks. This feature is especially important
given intense commodity price and macroeconomic volatility between the
Great Moderation and Global Financial Crisis (Primiceri, 2005; Baumeister
andPeersman,2013).
Our findings can be summarised as follows. We discover an important
degree of commodity price co-movement due to common and sectoral fac-
tors, highlighting the importance of commodity heterogeneity. Commodities
can be modelled therefore by a single common factor, but there are notable
differences between commodities, especially during episodes of extreme
price volatility. Next, we report and discuss the estimation results from time-
invariant and time-varying FAVAR models. Under both approaches, we pro-
vide empirical evidence that macro fundamentals affect the returns of a large
number of commodities. The impulse responses indicate qualitative and
quantitative changes over time in commodity prices to demand, real interest
rateanduncertaintyshocks.Weprovideadditionalevidencethatfundamental
shocks relate differently to the material, foodand metal sectors. For example,
demand shocks have a more powerful impact on the metals’ sector than
others, while materials are more sensitive to uncertainty. Intuitively, and sup-
porting the use of a time-varying methodology, we alsofind Chinese demand
shockshavehadanincreasinglypositiveimpactoncommodityprices.
The rest of the paper is organised as follows. Section 2 reviews the related
literature. Section 3 formally presents our econometric methodology.
Section 4 discusses the data. Section 5 reports the empirical results and
robustnesschecks.Section6offerssomeconcludingremarks.
2. Brief literature review
Changes in commodity prices can be rapid, and large price swings severely
impact commodity importers, exporters and speculators.2 Thus, a better
understanding of the nature of commodity prices and their determinants may
2 Forexample,highercommoditypricesmayleadtoloweraggregatedemandandproduction
outputs, induce inflationary tendencies and higher interest rates for importing countries;
whereas a sustained decline in commodity prices supports the so-called ‘resource curse’
hypothesis for commodity abundant emerging economies. See, among the others, Frankel
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

502 J.P.Byrneetal.
lead to better decision making in areas such as macroeconomic policy, risk
and portfolio management. A long-standing literature focused on commodity
prices’ time series properties (e.g. Cuddington, 1992; Deaton, 1999; Cashin,
Liang and McDermott, 2000). This is related to trends in primary commodity
prices relative to the price of manufactured goods, within the context of the
Prebisch (1950) and Singer (1950) hypothesis.3 The literature has also con-
sidered commonalities in commodity prices. The seminal work by Pindyck
and Rotemberg (1990), for example, was the first to confirm that prices of
seemingly unrelated commodities tend to co-move. Deaton (1999) stressed
that it is important to consider the time series properties of individual com-
modities and their co-movement, to assess the different impact of commodity
prices on developing and industrial countries, and therefore the need for sta-
bilisation policies. Cashin, McDermott and Scott (2002) also found evidence
ofpricesynchronisationofrelatedcommodities.
The co-movement of commodity prices since the turn of the 21st century
has promoted a renewed interest in commonalities andsought to explain why
prices co-move. Alquist and Coibion (2014) employed a general equilibrium
model to decompose the sources of commodity price co-movement. They
evidenced indirect shocks that impact on commodity prices through the
changeinaggregateoutputaremainsourcesfor commoditypricecommonal-
ities. This empirical literature has, for example, employed factor models to
extract commonalities. Cuddington and Jerrett (2008) used principal compo-
nent analysis to investigate the degree of concordance between metal com-
modity prices. Panel time series methods were utilised by Byrne, Fazio and
Fiess (2013) and they found evidence of co-movement of a large number of
commodities due to one common factor. Chen et al. (2014) showed that the
movements of 51 tradeable commodities were mostly due to the first com-
mon component. Poncela, Senra and Sierra (2014) extracted a principal com-
ponent from 44 non-fuel commodity prices from 1992 to 2012. Evidence has
also been found that commodity prices consistently display a tendency to
revert towards one factor, see West and Wong (2014). The main drawback
with extracting a single common component from commodities is that the
estimated factor can be difficult to interpret and may not fully account for
heterogeneity. Recent research has sought to decompose the sources of com-
modity price co-movement using more granular methods. For example, Yin
and Han (2015) used a multilevel factor model to decompose 24 commodity
returns into global, sectoral and idiosyncratic components. They highlighted
theheterogeneousimpactsofsectoralfactorsatdifferentpointsintime.
A parallel and lively debate also spurred by the recent price boom-bust
cycle, has focused on the determinants of commodity prices. First, it is
(2008, 2014), Neftci and Lu (2008), Xu and Ouenniche (2012), Ghoshray, Kejriwal and Wohar
(2014)andOuenniche,XuandTone(2014).
3 ThePrebisch–Singerhypothesisexamineswhetherthetermsoftradeofcommodityexporters
aretrending,suchthatlivingstandardswouldbefurtherimpoverishedbyspecialisingincom-
modity extraction with a secular decline in commodity prices. The hypothesis was revisited
recentlybyHarveyetal.(2010).
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

Commoditypriceco-movement 503
frequently argued that commodity prices are primarily driven by global eco-
nomicactivity(e.g.Svensson,2008;Wolf,2008;Kilian,2009;Abhyankar,Xu
and Wang, 2013). This argument is related to increases in demand due to the
unexpectedly strong economic growth in emerging economies after 2000 and
their rapid recovery from the global financial crisis (Singleton, 2013; Frankel,
2014). The impact on commodity prices of rapid Chinese economic growth
can similarly be understood as a demand shock. This has been highlighted in
work by Dwyer, Gardner and Williams (2011), Roache (2012) and Frankel
(2014) and is especially topical since recent commodity price collapses are
relatedtofearsaboutChina’sgrowthslowdown.
Monetary policy believed to have played an important role for commodity
prices. For instance, Barsky and Kilian (2004) pointed out that high prices
for oil and other commodities in the 1970s was because of an expansionary
monetary policy. Frankel (2008, 2014) argued that a substantial increase in
US real interest rates drove commodity prices down in the early 1980s.
According to asset pricing models, commodity prices are determined by the
expected discount rate and expected future returns.4 Therefore, an increase in
real interest rates will raise the discount factor, so the present value of future
returns will fall and subsequently lead to lower commodity prices. Higher
ratesofreturnonfixedincomeassetswillalsooffersubstitutionopportunities
and reduce speculative demand for commodities. In addition, high interest
rates increase the supply for storable commodities by increasing extraction
incentives today, and/or by decreasing firms’ desire to carry inventories.
Gruber and Vigfusson (2012) showed that lower interest rates can reduce
commodity prices’ volatilities and interest rates can impact commodities
heterogeneously.
Uncertaintymay also be important for commodityprices. According to the
standard option theory, given investment in primary commodities is irrevers-
ible (or at leastpartially irreversible), an increase in the varianceof the distri-
bution of investment returns would increase the option value of waiting for
newinformation,causingdelaysinsuchinvestmentandpossiblepriceeffects
(Dixit and Pindyck, 1994). Consequently, uncertainty will play a negative
role in effecting the price of commodities. Beck (2001), for example, found
someevidenceontherelationshipbetweenriskandagriculturalcommodities.
Byrne, Fazio and Fiess (2013) suggested a role for macroeconomic uncer-
tainty in affecting the movements of commodity prices. While uncertainty
may negatively affect commodity prices by encouraging investors to delay
investments, it may also lead producers to lower their supply and production
level and push prices up (Alam and Gilbert, 2017). Hence, it becomes an
empiricalquestionastowhichuncertaintyeffectdominates.
In reviewing the literature, we have identified several empirical studies on
investigating the determinants of commodity price fluctuations. For example,
Vansteenkiste (2009) showed that the commodity common factor was
affected by oil price, global demand, the US dollar effective exchange rate
4 Ifweassumecommoditypricesaredeterminedlikeotherassets,seeSvensson(2008).
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

504 J.P.Byrneetal.
and the real interest rate. Using a FAVAR approach, Byrne, Fazio and Fiess
(2013) related the common factor in commodity prices to their macroeco-
nomic fundamentals. They found real interest rate and uncertainty were both
negatively related to the common factor. Poncela, Senra and Sierra (2014)
also applied a FAVAR to assess the impact of real interest rates, the US real
effective exchange rate, VIX, world industrial production and an energy
index.They found uncertainty after 2003has playeda more important rolein
explaining price fluctuations than real fundamentals, such as the real
exchangeandtherealinterestrate. WestandWong(2014)computedthefirst
principal component correlation with fundamentals and found that commod-
ities were positively related to industrial production and negatively related to
the exchange rate. Alam and Gilbert (2017) extracted a common factor using
principal components and found that monetary policy, demand and the US
exchange rates significantly affected agricultural commodity prices. A com-
mon feature of all these empirical studies is that they rely on time-invariant
regressions. Therefore, the impact of demand shocks on the commodity
pricesisassumedtobetime-invariantorunconditional.
To summarise, our study extends the literature on the co-movement and
determinants of primary commodity prices for the following reasons. While
previous studies focused on a single common factor in a wide range of com-
modities, we account for heterogeneity by employing a dynamic hierarchical
factor model to decompose commodities into global, sectoral and idiosyn-
cratic components. Next, using a time-varying parameter factor augmented
vector autoregressive model with stochastic volatility, we examine determi-
nants of commonalities over time and across sectors. We now turn to for-
mallylayingoutoureconometricmethodology.
3. Methodology
3.1. Dynamichierarchicalfactormodel
We adopt a four-level dynamic hierarchical factor model (DHFM) following
Moench, Ng and Potter (2013). Let X be commodity price series
b,s,n,t
(n = 1, ⋯,N), at each period t = 1,⋯,T, in a given sub-sector s
(s = 1, ⋯,j) of sector b (b = 1, ⋯,i) has four sources of variations:
commodity-specific, sub-sector (H ), sector (G ) and common (F). Our
b,s,t b,t t
dynamicfactormodelissetoutasfollows:
X = λ (L)H + e (1)
b,s,n,t H b,s,t X,t
H = λ (L)G + e (2)
b,s,t G b,t H,t
G = λ (L)F + e (3)
b,t F t G,t
where λ , λ and λ denote parameters for sub-sector factors, sector-factors
H G F
and common factors, respectively. Error terms e , e and e denote
X,t H,t G,t
commodity-specific,sub-sectorandsector-levelresidualvariations,respectively.
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

|     |     |     |     |     |     | Commoditypriceco-movement |     | 505 |     |
| --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- |
Note thate ,e , e and F are assumed to be stationary, normally distribu-
|     | X,t | H,t | G,t | t   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tedautoregressiveprocessesoforderone,AR(1),andevolveasfollows:
|     |     |     |     | e =   | ψ e       | + ε   |     | (4) |                                                                                                                   |
| --- | --- | --- | --- | ----- | --------- | ----- | --- | --- | ----------------------------------------------------------------------------------------------------------------- |
|     |     |     |     | X,t   | X X,t−1   | X,t   |     |     |                                                                                                                   |
|     |     |     |     | e =   | ψ e       | + ε   |     | (5) |                                                                                                                   |
|     |     |     |     | H,t   | H H,t−1   | H,t   |     |     | Downloaded from https://academic.oup.com/erae/article/47/2/499/5486456 by Università Bocconi user on 30 June 2026 |
|     |     |     |     | e =   | ψ e       | + ε   |     | (6) |                                                                                                                   |
|     |     |     |     | G,t   | G G,t−1   | G,t   |     |     |                                                                                                                   |
|     |     |     |     | F t = | ψ F t−1 + | ε F,t |     | (7) |                                                                                                                   |
F
where ψ , ψ , ψ and denote the coefficient of the AR(1) dynamics. ε ,
|      |      |        | ψ    |       |                                 |     |     | X,t |     |
| ---- | ---- | ------ | ---- | ----- | ------------------------------- | --- | --- | --- | --- |
|      | X H  | G      | F    |       | =X,H,GandF,whichareuncorrelated |     |     |     |     |
| ε ,ε | andε | follow | N(0, | σ2),j |                                 |     |     |     |     |
| H,t  | G,t  | F,t    |      |       | j                               |     |     |     |     |
across time and sectors. We assume that the factor loading matrix is constant
and estimate one common factor per sector, and one factor per sub-sector. A
standard method to estimate latent factors from a large number of data series
is principal component analysis. However, principal component analysis
wouldnotaccountforpotentialrelationsbetweencommonandsectorfactors,
nor the AR(1) time series structure described in equations (4)–(7). Moench,
Ng and Potter (2013) propose a Markov Chain Monte Carlo (MCMC) meth-
od to overcome these problems. Following Moench, Ng and Potter (2013),
we first employ principal components to obtain the initial values of factors,
first
then run the MCMC method and discard the 20,000 draws as burn-in
andsaveevery100thoftheremaining50,000draws.5
3.2. Factoraugmentedvectorautoregression(FAVAR)models
Now we set out the basic Bayesian Factor Augmented VAR model to exam-
ine the determinants of commodity commonalities and explain how it can be
extendedtoatime-varyingparameter(TVP)model.TheTVP-FAVARmodel
with stochastic volatility allows us to understand how changes in macroeco-
nomicfundamentalsaffectrealcommoditypricesovertime.
3.2.1. BayesianFAVARmodel
ThebasicBayesianFAVARmodelcanbewrittenasfollows:
p
|     |     | AY  | = ∑ΓY |       | + u , t | = p + 1,…,T |     | (8) |     |
| --- | --- | --- | ----- | ----- | ------- | ----------- | --- | --- | --- |
|     |     |     | t     | i t−i | t       |             |     |     |     |
i=1
where Y is a K × 1 vector of endogenous variables and divided into two
t
first
blocks: the block includes the growth rate of real US industrial produc-
tion (Demand), the real interest rate (R) and a risk term (Risk ); the second
|     |     | t   |     |     | t   |     | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5 We followed the recommended number of iterations provided by Moench, Ng and Potter
(2013). The detailed estimation procedures for the dynamic hierarchical factor model are
reportedinAppendixC.1(insupplementarydataatERAEonline)..

506 J.P.Byrneetal.
block includes the common factors in commodity prices (F);6 Γ is a K × K
t i
|           | coefficients, |     |      |         |        |                    | coefficient |     |
| --------- | ------------- | --- | ---- | ------- | ------ | ------------------ | ----------- | --- |
| matrix of |               |     | A is | a K × K | matrix | of contemporaneous |             |     |
of Y, and u captures the structural shocks in the commodity market and
| t   | t   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
macroeconomic conditions. We assumeu t to be i.i.d.andN(0, ΣΣ). The lag
| lengthistwo(i.e. |     | p = | 2),7whereΣ |     | isthediagonalmatrix: |     |     |     |
| ---------------- | --- | --- | ---------- | --- | -------------------- | --- | --- | --- |
Downloaded from https://academic.oup.com/erae/article/47/2/499/5486456 by Università Bocconi user on 30 June 2026
|     |     |     |     | ⎛   | σ 0 ⋯ | 0 ⎞ |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- |
1
|     |     |     |     | ⎜   |     | ⎟   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | ⎜0  | ⋱⋱  | ⋮⎟  |     |     |
Σ =
|     |     |     |     | ⎜⋮  | ⋱⋱  | 0⎟  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | ⎜   |     | ⎟   |     |     |
|     |     |     |     | ⎝0  | ⋯ 0 | σ ⎠ |     |     |
k
To specify the simultaneous relations of the structural shock, we employ
its reduced-form representation by multiplying both sides by A−1, resulting
in:
p
|     |     | Y = | ∑BY | + A−1Σε, | ε   | ∼ N(0, I ) |     | (9) |
| --- | --- | --- | --- | -------- | --- | ---------- | --- | --- |
|     |     | t   |     | i t−i    | t   | t k        |     |     |
i=1
coefficients
| where B | = A−1Γ | for | i = 1,…,p. | We  | can stack | all the VAR |     | (B) |
| ------- | ------ | --- | ---------- | --- | --------- | ----------- | --- | --- |
|         | i      | i   |            |     |           |             |     | i   |
into a K2p × 1 vector to form B and define X = I ⊗ (Y′ ,…,Y′ ), where
|     |     |     |     |     |     | t k | t−1 t−p |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- |
⊗ denotestheKroneckerproduct.Werewriteequation(9)as:
|     |     |     |     | Y = X B | + A−1Σε |     |     | (10) |
| --- | --- | --- | --- | ------- | ------- | --- | --- | ---- |
|     |     |     |     | t t     |         | t   |     |      |
Note that the reduced-form residuals ε are correlated between each
t
equation and can be viewed as a weighted average of the structural shocksu
t
in equation (8). In order to orthogonalise the shocks, we impose a recursive
structure on the contemporaneous terms and assuming that A is lower-
triangular,
|     |     |     |     | ⎛        |     | ⎞   |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- |
|     |     |     |     | 1        | ⋯ ⋯ | 0   |     |     |
|     |     |     |     | ⎜        |     | ⎟   |     |     |
|     |     |     |     | a        | ⋱ ⋱ | ⋮   |     |     |
|     |     |     |     | A = ⎜ 21 |     | ⎟   |     |     |
|     |     |     |     | ⋮        | ⋱ ⋱ | 0⎟⎟ |     |     |
⎜⎜
|     |     |     |     | ⎝a  | ⋯a  | 1⎠  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
k1 k,k−1
The ordering of the variables is as follows:Y = [Demand, R, Risk, F].
|     |     |     |     |     |     | t   | t t | t t |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thestructural shocksu areidentifiedbydecomposingthereduced-formerrors
t
ε t asfollows:
6 WhenaccountingforcommodityheterogeneitywereplacethecommonfactorF withsectoral
t
factorsGb,t(Sectoralb,t).
7 Mostlaglengthspecificationtests(e.g.FinalPredictionError;AkaikeInformationCriterion;and
Hannan-QuinnInformationCriterion)suggestthattwolagsshouldbeincludedforourmodel
withquarterlydata.

|     |     |         |     |        | Commoditypriceco-movement |     |     | 507  |
| --- | --- | ------- | --- | ------ | ------------------------- | --- | --- | ---- |
|     |     | ⎛       | ⎞   |        | ⎛                         | ⎞   |     |      |
|     |     | Demand  |     |        | Demand                    |     |     |      |
|     |     | ⎜ ε     | ⎟   | ⎡      | ⎤⎜ u                      | ⎟   |     |      |
|     |     | t       |     | 1 0    | 0 0 t                     |     |     |      |
|     |     | ⎜ εR    | ⎟   | ⎢      | ⎥⎜ uR                     | ⎟   |     |      |
|     |     |         |     | a 1    | 0 0                       |     |     |      |
|     |     | ε = ⎜   | t ⎟ | = ⎢ 21 | ⎥⎜                        | t ⎟ |     | (11) |
|     |     | t       |     | ⎢a a   | 1 0⎥⎜                     |     |     |      |
|     |     | ⎜ εRisk | ⎟   | 31 32  | uRisk                     | ⎟   |     |      |
|     |     | t       |     | ⎣⎢     | 1⎦⎥⎜ t                    |     |     |      |
|     |     | ⎜       | ⎟   | a a    | a                         | ⎟   |     |      |
⎝ εF ⎠ 41 42 43 ⎝ uF ⎠ Downloaded from https://academic.oup.com/erae/article/47/2/499/5486456 by Università Bocconi user on 30 June 2026
|     |     |     | t   |     |     | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
In the global macroeconomic block, uDemand denotes the aggregate
t
demand shock that captures the shift in the demand for all commodities dri-
ven by the global business cycle. Next,uR is the real interest rate shock that
t
reflects deviations from the expected or average monetary policy, whether
inflation,
via changes in the nominal interest rate, expected or both (e.g.
Frankel,2008). Finally,uRisk denotesthe risk shockthatcaptures innovations
t
| agents’ |              |     |       |                 |     | financial |             |     |
| ------- | ------------ | --- | ----- | --------------- | --- | --------- | ----------- | --- |
| to      | expectations |     | about | future economic | and |           | conditions. |     |
Intuitively, this can also be thought of as precautionary trading arising from
revisions to commodity market expectations. These expectations may arise
|               |       | financial |     |          |                  | financial |         |     |
| ------------- | ----- | --------- | --- | -------- | ---------------- | --------- | ------- | --- |
| from elevated | risks | in        |     | markets, | as in the global |           | crisis. | In  |
the commodity market block,uF is the shock to the common factor in com-
t
modityprices.
The restrictions on A−1 are based on the following assumptions and eco-
nomic intuition. The first assumption is that global real economic activity
does not respond immediately to real interest rate shocks, uncertainty shocks
and commodity markets, but does so with a delay of at least a quarter. Our
second exclusion restriction imposed in the VAR is that increases in uncer-
financial
tainty regarding the economic and outlook will not affect real inter-
est rates immediately. Our third assumption is that innovations to risk
respondtodemandandpolicyshockswithoutadelay.Theseassumptionsare
based on Bernanke, Boivin and Eliasz (2005) and Stock and Watson (2005),
whohaveclassifiedtheseriesintoslow-movingvariables,suchasrealoutput
and income, wages and spending; and fast-moving variables such as stock
prices, money and credit. Global real economic activity is considered slow-
firms
moving: it is plausible that consumers and slowly revise their spending
plans after a monetary policy or financial market shocks. In contrast, com-
modity price volatility is considered as a fast-moving variable, responding
shocks.8
contemporaneously to slow-moving variables and policy For the
commodity market block, we assume that uF does not affect global real
t
activity, the real interest rates and uncertainty within a given quarter, but
instead with a delay of at least one quarter. This is imposed through the
exclusion restrictions in the last column of A−1. This assumption is implied
by the standard approach of treating innovations to the price of commodities
aspredeterminedwithrespecttotheeconomy(e.g.KilianandPark,2009).
8 AsimilaridentificationstrategyincommoditypriceliteratureisalsofollowedbyAkram(2009),
Lombardi et al. (2012), Byrne et al. (2013), Hammoudeh et al. (2015), and Alam and Gilbert
(2017)’sfirstidentificationstrategy.

508 J.P.Byrneetal.
We estimate the FAVAR model in the context of Bayesian inference and
flexible
adopt the independent Normal-Wishart prior, which is more than the
naturalconjugateprior.Thepriordistributionsaredescribedas:
|     |     |     | B~N(B̲, | V ) |     |     |
| --- | --- | --- | ------- | --- | --- | --- |
B
Downloaded from https://academic.oup.com/erae/article/47/2/499/5486456 by Università Bocconi user on 30 June 2026
|     |     |     | Σ−1~W(S̲−1, | ν̲) |     |     |
| --- | --- | --- | ----------- | --- | --- | --- |
Where B̲ = 0, V = 10I , S̲ = I , and v̲ = 5 as in Koop and Korobilis
|     |     |     | B 4 | 4   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
(2010). The conditional posterior distributions p(B|Y, Σ−1) and p(Σ−1|Y,B)
are computed by the MCMC method. Following Primiceri (2005), we use a
first
training sample prior to obtain the initial Σ−1. The training sample is the
40 observations (1974: Q1 to 1983: Q4). Using the MCMC method, 20,000
samples are obtained after the initial 10,000 samples are used as burn-in and
discarded.9
3.2.2. Time-varyingparameterFAVARwithstochasticvolatility
Note that all parameters in equation (10) are time-invariant. Next, we adjust
themodelbyallowingtheseparameterstovaryovertime,asfollows:
A−1Σε
|     |     |     | Y = X | B +       |     | (12) |
| --- | --- | --- | ----- | --------- | --- | ---- |
|     |     |     | t     | t t t t t |     |      |
where the coefficients B, and the parameters A, and Σ are all time varying.
|     |     |     | t   |     | t t |     |
| --- | --- | --- | --- | --- | --- | --- |
Time-varying parameters allow the relationship between fundamentals and
commodities to evolve over time. Stochastic volatility allows for varying
shock intensity and improves estimation precision (see Nakajima, Kasuya
and Watanabe, 2011). We follow Primiceri (2005) and let a = (a , a ,
t 21 31
a , a , a , a )′be a stacked vector of the lower-triangular elements in A
| 32  | 41  | 42 43 |     |       |     | t   |
| --- | --- | ----- | --- | ----- | --- | --- |
|     |     |       | )′  | logσ2 |     |     |
and h t = (h 1,t ,…,h k,t with h = , for j = 1,…,k and σ is the diag-
|     |     |     | j,t | j,t | jt  |     |
| --- | --- | --- | --- | --- | --- | --- |
onal element of Σ . We assume that the parameters in (12) follow a driftless
t
random walk process, thus allowing both temporary and permanent shift in
theparameters:
|     |     |           |                   | ⎛        | ⎞⎞          |     |
| --- | --- | --------- | ----------------- | -------- | ----------- | --- |
|     |     |           | ⎛ ε ⎞             | ⎛ I 0    | 0 0         |     |
|     | B   | B         | u , t             | ⎜ K      | ⎟⎟          |     |
|     | t   | = t − 1   | + B , t ⎜ ⎟       | ⎜        |             |     |
|     |     |           | u B , t           | ⎜ ⎜ 0 Σ  | 0 0 ⎟ ⎟     |     |
|     | a   | = a       | + u , ⎜ ⎟         | ∼ N 0, B | , t = 1,…,T |     |
|     | t   | t − 1     | a , t u           | ⎜ ⎜ 0 0  | Σ 0 ⎟ ⎟     |     |
|     |     |           | ⎜ a , t ⎟         | ⎜ ⎜      | a ⎟ ⎟       |     |
|     | h t | = h t − 1 | + u h , t , ⎝ u ⎠ |          |             |     |
|     |     |           | h , t             | ⎝ ⎝ 0 0  | 0 Σ ⎠ ⎠     |     |
h
The shocks to the innovations of the time-varying parameters are assumed
uncorrelatedamongtheparameters B ,a andh .Wefurther assumeforsim-
|     |     |     |     | t t | t   |     |
| --- | --- | --- | --- | --- | --- | --- |
arealldiagonalmatrices.Ourdynamicspecification
| plicitythatΣ |     | B ,Σ a | andΣ h |     |     |     |
| ------------ | --- | ------ | ------ | --- | --- | --- |
9 NotethatforBayesianVARandTVP-FAVARmodels,wefoundthat10,000burn-inand20,000
sampledrawsaresufficientfortheMCMCalgorithmtoconverge.Asarobustnesscheck,we
haveemployedtheconsistentdrawnumberwereusedinthedynamichierarchicalfactormodel
(20,000burn-inand50,000sampledraws).Wefindthatthechangeofdrawsdoesnotaffectthe
estimationresults–seeFigureB12(AppendixinsupplementarydataatERAEonline).

Commoditypriceco-movement 509
permits the parameters to vary and the shock log variance follows a random
walk process to capture possible gradualor sudden structural changes,as dis-
cussedbyPrimiceri(2005).
For estimation, we employ a training sample prior, as shown in Section 3.2.1
andthepriordistributionsaresetasfollows:
Downloaded from https://academic.oup.com/erae/article/47/2/499/5486456 by Università Bocconi user on 30 June 2026
|     | B ∼ N(B | , 4⋅V(B     | ))     |
| --- | ------- | ----------- | ------ |
|     | 0       | OLS         | OLS    |
|     | A N(A   | 4⋅V(A       |        |
|     | 0 ∼     | OLS ,       | OLS )) |
|     | h       | ∼ N(h , 4⋅I | )      |
|     | 0       | OLS         | k      |
where B , A and h denote the OLS point estimates andV(⋅) denotes
| OLS OLS | OLS |     |     |
| ------- | --- | --- | --- |
the variance. We also need to set the hyper-parametersΣ ,Σ andΣ and we
B a h
postulatethefollowinginverse-Wishartpriordistributions:
|     | Σ ∼ IW(k2⋅40⋅V(B |     | ), 40) |
| --- | ---------------- | --- | ------ |
|     | B                | B   | OLS    |
IW(k2,
|     | Σ   | ∼   | 2)  |
| --- | --- | --- | --- |
|     |     | a a |     |
IW(k2⋅2⋅V(A
|     | Σ 1,h ∼         | h   | 1,OLS ), 2) |
| --- | --------------- | --- | ----------- |
|     | Σ ∼ IW(k2⋅3⋅V(A |     | ), 3)       |
|     | 2,h             | h   | 2,OLS       |
|     | Σ ∼ IW(k2⋅4⋅V(A |     | ), 4)       |
|     | 3,h             | h   | 3,OLS       |
where k = 0.01, k = 0.1 and k = 1; Σ , Σ and Σ denote the three
| B α |     | h 1,h | 2,h 3,h |
| --- | --- | ----- | ------- |
blocksofΣ and A for j = 1,…,3,denotesthethreecorrespondingblocks
| h j,OLS |     |     |     |
| ------- | --- | --- | --- |
first
of A OLS . The estimation procedure is the MCMC method and the 10,000
samplesarediscarded,and20,000samplesareobtainedfortheinference.10
4. Data
In this paper, we use quarterly primary commodity prices and fundamentals
data from 1974Q1 to 2014Q3. For the dynamic hierarchical factor model, we
collecta panelof38commoditypricesfromtheInternational MonetaryFund
(IMF) International Financial Statistics and World Bank commodity price
data. Following the structure of the IMF non-fuel commodity index, we
arrange the commodity data into three sectors: (i) agricultural raw materials,
(ii) food and (iii) metals. First, the materials sector includes eight commod-
ities: cotton, hides, plywood, rubber, hardwood logs, hardwood sawn wood,
fine
coarse wool and wool. Second, our dataset includes 23 food commod-
ities, and we further decomposed them into four sub-sectors; namely, cereals
10 ThedetailsoftheMCMCprocedureforTVP-FAVARmodelarereportedinAppendixC.2(insup-
plementarydataatERAEonline).(Primiceri,2005;KoopandKorobilis,2010;Nakajima,Kasuya
andWatanabe,2011).

510 J.P.Byrneetal.
Table1. Dataandmodelstructure
| Sector | Sub-sector |     |     | N   |
| ------ | ---------- | --- | --- | --- |
| Food   | Cereals    |     |     | 5   |
|        | Meat       |     |     | 3   |
Downloaded from https://academic.oup.com/erae/article/47/2/499/5486456 by Università Bocconi user on 30 June 2026
|           | Vegetableoilandproteinmeals(non-fueloil) |     |     | 9   |
| --------- | ---------------------------------------- | --- | --- | --- |
|           | Others                                   |     |     | 6   |
| Materials |                                          |     |     | 8   |
| Metals    |                                          |     |     | 7   |
| Total     |                                          |     |     | 38  |
Notes:Thistablesummarisesthedifferentsectorsinourdataset.Thesearefood,agriculturalrawmaterialsand
metalsectors.Sub-sectorsforrealcommoditypricesarealsoincluded.Ndenotesthenumberofseriesineachsec-
tor/sub-sector.
(i.e. barley, maize, rice, sorghum and wheat); meat (i.e. beef, lamb and
chicken), vegetable oil and protein meals (i.e. coconut oil, copra, groundnuts,
groundnut oil, linseed oil, palm oil, soybeans, soybeans meal, and soybeans
fishmeal,
oil) and others (i.e. cocoa beans, coffee, tea, banana, sugar).
Finally, we include seven metal commodities: aluminium, copper, gold, lead,
silver,tinandzinc.Table1summarisesourdataandmodelstructureofcom-
modity prices. Quarterly data is preferred when estimating our time-varying
parameter model: TVP-FAVAR estimation at a monthly frequency would
require many lags to capture data dynamics, and hence would be computa-
tionally intensive (Nakajima, Kasuya and Watanabe, 2011). Before the factor
deflate
analysis, we the nominal commodity prices using US CPI. Before the
factoranalysis,wedeflatethenominalcommoditypricesusingUSCPI.Note
that our factor model requires all the data are stationary, hence we employed
|               | Dickey–Fuller | Phillips–Perron | Kwiatkowski– |     |
| ------------- | ------------- | --------------- | ------------ | --- |
| the Augmented |               | (ADF),          | (PP) and     |     |
Phillips–Schmidt–Shin (KPSS) teststoascertain whetherreal commodity prices
are stationary (Stock and Watson, 2009; Moench, Ng and Potter, 2013). The
null hypotheses for ADF and PP are the existence of a unit root I(1), so if the
series is stationary I(0), the ADF and PP tests should reject the null hypothesis.
In contrast, the null hypothesis of the KPSSstatistic is that the series is station-
ary, i.e. I(0). In terms of the processes under study, we have found evidence
that the level of real commodity prices contains a unit root. Hence, we have
taken the logarithmic transformation for all real commodity prices series. A
detailed description of the commodity price series is presented in Table A1
(AppendixinsupplementarydataatERAEonline).
Next, we gather macroeconomic fundamentals data from the Federal
Reserve Bank of St. Louis and Datastream. We first use US industrial pro-
duction as our proxy for global economic activity (Demand). The rationale
t
for using this proxy is that the growth of industrial production will reflect
changes in the demand for industrial commodities (e.g. copper, lumber) and
itwillalsoimpactdemandfornon-industrialcommodities(e.g.cocoa,wheat)

Commoditypriceco-movement 511
asincomechanges,seePindyckandRotemberg(1990).Giventhepotentially
increasing importance of the Chinese economy for commodities, we also
proxy demand using the growth rate of Chinese industrial production.11
Second, we consider the role of the real short-term interest rate based on the
three-month US Treasury Bill as a proxy for monetary policy shocks (e.g.
Primiceri, 2005). The real rate (R), is obtained by subtracting US CPI infla-
t
tion from the nominal interest rate, based on the Fisher equation. Note that
we also test the robustness of our approach by using the federal fund rate as
an alternative interest rate proxy (e.g. Bernanke, Boivin and Eliasz, 2005;
Frankel,2014).
Inordertoexaminetheriskeffectsoncommodityprices’growth,wemod-
el commodity markets’ risks that arise from agents’ perspectives on future
outcomes (Risk ). To that end, we fit a GARCH model of the log difference
t
ofthedailyS&PGSCI(GoldmanSachsCommodityIndex)tocovertheperi-
odfromJanuary1970toSeptember2014.12Weshouldnotethatpriortoesti-
mating this model, we confirmed the presence of ARCH effects in the GSCI
using the Lagrange Multiplier test. We also check whether the standardised
residuals exhibit higher order autocorrelation and ARCH effects.
Ascertaining that the selected model is well specified, we take the within
quarter averageof the estimatedconditionalvariances to match the frequency
of the commodity data. This series is then used as a measure of uncertainty
in the market. Here, higher levels of conditional variance imply higher per-
ceived uncertainty. In such an environment, decision makers (e.g. fund man-
agers and commodity producers) will not be able to predict the viability nor
returns of projects. Thus, one may behave more conservatively and opt to
postpone the investment to avoid potentially large losses when the project
outcome is unfavourable. To check for the robustness of our investigation,
we also proxy uncertainty using the within quarter standard deviation of the
GSCI non-energy spot index and a GARCH model fitted to the stock market.
Using ADF, PP and KPSS tests, we test for all series involved including
macroeconomic variables, common and sectoral factors. We find that the real
US industrial production rate and the real Chinese industrial production rate
are non-stationary in levels, and we have used the first difference of these
11 Asafurtherrobustnesscheck,weconsiderKilian’s(2009)globaleconomicactivityindexasan
alternative proxyfor demand. Note thatKilian’sseries is ameasurefrom an equal-weighted
indexofthepercentagegrowthratesofapanelofsingledrycargooceanshippingfreightrates
indollarspermetricton.Giventhesupplyofocean-goingvesselsislikelytobeinelasticinthe
short-run,shippingratesshallreflectglobaldemandforcommodities.Oneofadvantagesofthe
Kilianindexisthatitcanbeconstructedasfarbackas1968,theprimarydatasourceunderlying
the Kilian index is the report on ‘Shipping Statistics and Economics’ published by Drewry
ShippingConsultantsLtd.TheKilianindexcanbefoundfromLutzKilian’shomepage:http://
www-personal.umich.edu/~lkilian/reaupdate.txt.KilianandZhou(2018)addressseveralpoten-
tialobjectionsthathasbeenraisedintheliteraturee.g.failingtoconsiderthecostofbunker
fuel;theshipbuildingcycle(e.g.Odom,2010;RavazzoloandVespignani,2017).Theyalsopro-
videcomplementaryevidencethatsupportstheexistenceofapersistentglobaleconomicslow-
downbetween2010and2016.Wethankananonymousrefereeforthispoint.
12 ForstandardreferencestoGARCHestimationseeEngle(1982)andBollerslev(1986).
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

512 J.P.Byrneetal.
variables to remove the unit root.13 We next proceed to estimate our factor
andtime-varyingempiricalmodels.
5. Empirical results
This section presents our core results on the nature and determinants of com-
modity prices. We first report the empirical findings on commodity price co-
movement using the dynamic hierarchical factor model of Moench, Ng and
Potter (2013). Next, we discuss the results from a constant parameter
FAVAR model and those from a time-varying parameter FAVAR model
withstochasticvolatility.
5.1. Commoditypriceco-movement
The four-level dynamic hierarchical factor model allows us to capture the
aggregate common dynamics, as well as to track the developments in differ-
ent commodity sectors. Figure 1 plots the estimated global common
factor,Fˆ, plus material, food and metal sectoral factors, Gˆ. Similarities
Fig. 1. Commonalities in commodity prices. Notes: The graph presents estimated aggre-
gatecommonfactor(Common),alongwith sectoralfactorforthereturnsinfood(Food),
agricultural raw materials (Materials) and metal (Metals). The sectoral commonalities are
identified dynamic hierarchical factor model in equations (1)–(3), see Moench, Ng and
Potter(2013).
13 Tosavespace,wedonotreportthesetestresults.Theyareavailableonrequest.
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

Commoditypriceco-movement 513
between the sectors include, for instance, the commodity price peaks in mid-
2008,fallthereafterandpeakagainin2011.Therearesomeimportantdiffer-
ences between the common and sectoral factors, especially during episodes
of extreme price volatility. For example, agricultural raw material and metal
sectors react more strongly than the common factor during the striking col-
lapse of commodity prices in the global financial crisis. The growth of mate- Downloaded from https://academic.oup.com/erae/article/47/2/499/5486456 by Università Bocconi user on 30 June 2026
rials and metals also exceeds the common factor before the crisis. This may
implythat agricultural rawmaterialsandmetalsaremore sensitiveto theglo-
balbusinesscycle,comparedtofoodcommodities.
We now turn to the important question of evaluating how much of the
variationinrealcommoditypricescanbeattributedtotheaggregatecommon
(Share ), sector (Share ) and sub-sector (Share ) components and to idio-
|     | F   | G   |     | H   |     |
| --- | --- | --- | --- | --- | --- |
syncratic noise (Share ). Table 2 reports the average posterior means (μ) and
Z
standard deviations (σ) of the estimated variance shares for the four-level
first
decomposition of our data set, including all sectors and sub-sectors. Our
evidence of heterogeneity in commodities is that the aggregate common fac-
torismostimportantformetalsinwhichathirdofcommoditypricevariation
is explained by the global commonalities in commodities, while less than
1 per cent is explained for food-meats. Mirroring the latter result, idiosyncratic
variations play an important role for food-meats as it accounts for most of the
variation in this sub-sector (i.e. μ = 0.742). On the other hand, cereals, non-
fuel oils, agriculture raw materials and metals are explained to a lesser extent
by idiosyncratic variation. As mentioned above, our hierarchical model goes
beyond principal components since it accommodates sector and sub-sector
Table2. Variancedecompositionofcommodityprices
|           | Sub-     | Global   | Sector   | Sub-sector | Idiosyncratic |
| --------- | -------- | -------- | -------- | ---------- | ------------- |
| Sector    | sector   | [Share ] | [Share ] | [Share ]   | [Share ]      |
|           |          | F        | G        | H          | Z             |
| Food      | Cereals  | 0.215    | 0.177    | 0.183      | 0.424         |
|           |          | (0.017)  | (0.013)  | (0.013)    | (0.033)       |
|           | Meat     | 0.007    | 0.006    | 0.245      | 0.742         |
|           |          | (0.012)  | (0.010)  | (0.170)    | (0.182)       |
|           | Non-fuel | 0.243    | 0.200    | 0.037      | 0.520         |
|           | oil      | (0.028)  | (0.024)  | (0.006)    | (0.045)       |
|           | Others   | 0.024    | 0.020    | 0.090      | 0.866         |
|           |          | (0.016)  | (0.013)  | (0.044)    | (0.063)       |
| Materials |          | 0.207    | 0.096    |            | 0.697         |
|           |          | (0.052)  | (0.029)  |            | (0.059)       |
| Metals    |          | 0.330    | 0.098    |            | 0.572         |
|           |          | (0.062)  | (0.023)  |            | (0.069)       |
Notes:Thistablesummarisesourfour-levelvariancedecompositionofrealcommoditypricebasedonadynamic
hierarchicalfactormodel(DHFM)presentedinequations(1)–(3).Thefourlevelsaretheglobalfactor[ShareF],
sector[ShareG],sub-sector[ShareH]andidiosyncraticshocks[ShareZ].Wereportthemeansandinparentheses
model’s
standard deviations of the estimated variance shares for the four levels, including all sectors and sub-
sectorsofourdataset.Thesampleperiodis1974Q1to2014Q3.

514 J.P.Byrneetal.
level shocks. In sum, our result suggests that co-movement in commodity
prices co-exist with heterogeneousvariations between sectorsand highlightthe
importance of modelling common variations at different levels (Moench, Ng
and Potter, 2013; Yin and Han, 2015). Given these results, sectoral heterogen-
eityisthefocusofourlateranalysis.
5.2. Commonalities,fundamentalsandheterogeneity
In this section, we model commodity prices by examining the relationship
between their common factors and key macro fundamentals highlighted in
the literature. We first present impulse response functions to the shocks,
basedona BayesianFAVARmodel with common(Fˆ). Thereafter, we inves-
tigate whether FAVAR models are robust to time variation and commodity
heterogeneity, utilising findings from our TVP-FAVAR model for the com-
mon factor (Fˆ) and groups of commodities (Gˆ). As we noted above, such an
approachhasnotbeenextensivelyresearchedintheliterature.
5.2.1. ImpulseresponsesfromaFAVARmodel
Using our Bayesian FAVAR model, Figure 2 depicts impulse responses of
the common factor of commodity returns to one-standard deviation three
macroshocks(i.e.demand,realinterestrate andrisks)over threesampleper-
iods. That is the full sample period from 1974Q1 to 2014Q3; and two sub-
samples 1974Q1λ1993Q4 (period 1) and 1994Q1λ2014Q3 (period 2). We
present results for a ten-quarter response horizon. Our responses include the
posterior median as the solid line, while the dotted lines are the 16th and
84thpercentilesoftheposteriordistribution.14
We start by reporting the full sample period results in first column of
Figure 2. First, we find that demand shocks, as measured by US industrial
production growth, lead to an immediate increase in the real price of com-
modities, but the effect declines sharply after four quarters – see the top left
figure in Figure 2. We also see that commodities’ responses to demand are
important for the first four quarters, since the zero axis is not within the error
bands. Our finding is consistent with Boughton and Branson (1991);
Vansteenkiste (2009); Byrne, Fazio and Fiess (2013) and West and Wong
(2014), who also find that positive innovations to measures of the global
business cycle positively impact the price of commodities. For the full sam-
ple period, we find that an unexpected increase of 150 basis points (one
standard deviation) in the interest rate (a contractionary policy) leads to an
immediate and sizable decrease in commodity prices for the first quarter as
shownin the middle-left window ofFigure2. Thisis in linewith Scrimgeour
(2014) and Alam and Gilbert (2017). Furthermore, an uncertainty shock
causesanimmediatedropincommoditypricesandthendiesoutfivequarters
after the shock. See the bottom-left response in Figure 2. Therefore, our
14 Under normality, the 16th and 86th percentiles correspond to the bounds of one standard-
deviation(Primiceri,2005).
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

Commoditypriceco-movement 515
Fig. 2. FAVAR impulse responsesof common factor. Notes: The nine graphs in the fig-
ure plot the median responses of common factor (solid line) to each of the three macro
shocksthataffectthecommonalitiesincommodityreturnsforthreesampleperiods.Note
that the first column reports the full sample period (1974Q1λ2014Q3) result, and the
second and third columns report two sub samples; 1974Q1λ1993Q4 (i.e. period 1) and
1994Q1λ2014Q3(i.e.period2).Wealsoprovidethe16thand84thpercentileerrorbands
indashes.ThecommonfactorisextractedfromtheDHFMequation(3).
findings not only confirm the view of Frankel (2008), and Byrne, Fazio and
Fiess (2013) that interest rates have an adverse impact on commodity prices,
but also are consistent with the idea of Beck (1993), Dixit and Pindyck
(1994) and Kulatilaka and Perotti (1998) that risk is strongly associated with
movementsincommodityprices.
Next, we consider whether the impact of fundamental shocks is broadly
time varying, by splitting the sample into two sub-periods. The second and
third column of Figure 2 displays the median impulse responses of the com-
mon factor to macro shocks over the subsamples 1974Q1–1993Q4 and
1994Q1–2014Q3, respectively. We identify an evolving relationship between
primary commodity prices and macro fundamentals. To be more specific, the
response of commodity prices to the one standard deviation contractionary
monetary policy shock is more persistent in the first subsample, while the
reaction to demand and uncertainty shocks is more pronounced in the second
subsample.
In addition, we have replaced the common factor with three sectoral fac-
tors and apply our three macroeconomic shocks. We have observed the
important difference in sectoral responses to macroeconomics fundamentals
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

516 J.P.Byrneetal.
overthefullsampleperiod–seeFigureB1 (Appendixin supplementary data
atERAEonline)fordetails.15
5.2.2. TVP-FAVARmodelwithstochasticvolatility
The previous results were based on the assumption that the impact of funda-
mentals on commodity prices was time-invariant. Our subsample analysis,
with exogenously identified sub-periods, indicates that this assumption is
opentoquestion,hencewenowadoptmoreflexiblemethods.
In this section, we focus on the time evolution of the relationship between
commonalities in commodity returns and macroeconomics shocks using a
TVP-FAVAR model with stochastic volatility. Such an approach allows us
to consider the evolving impact of Chinese demand, recent monetary policy
and the role of risk during the financial crisis. Note that for a standard VAR
model whose parameters are time-invariant, we can graph one impulse
response profile for each shock – see Figure 2. For the time-varying param-
eter models, however, there will be a different set of coefficients in every
time period. So, we will have a different impulse response at each point in
time. Although one can draw a three-dimensional plot for the time-varying
impulseresponses,it iscommonpracticetopresenttheimpulseresponsesfor
a selected horizon over time and/or at a selected point in time (e.g. Primiceri,
2005; Koop and Korobilis, 2010; Nakajima, Kasuya and Watanabe, 2011;
Baumeister and Peersman, 2013). Therefore, we plot both the impulse
responses for the full sample period, and for up to a ten-quarter horizon for
threespecifictimeperiods.
Figure 3 graphs contemporaneous time-varying impulse responses of the
global commodity factor to one standard deviation increases in demand, real
interestrates andrisk. In this figure, theposteriormedian isthe solid lineand
the dotted lines are the 16th and 84th percentiles of the posterior distribution.
The top panel of Figure 3 shows that aggregate demand has a consistently
important and positive relationship with commodity prices commonalities
sincethe zeroaxis isbelowthe68percent posteriorcredible interval.This is
reasonable because an expansion in economic activity shall increase indus-
trial commodity demand and drive up commodities prices (see, Kilian, 2009;
Frankel, 2014; Byrne, Lorusso and Xu, 2018). The effect of aggregate
demand shocks on real commodity prices is evidently time varying, as we
observe a larger response in the 2000s compared to the early years of our
sample. However, this positive effect becomes smaller after the global finan-
cial crisis. This corresponds with the unexpected increase in demand in the
2000s from many emerging market economies, such as China and India, as
they became more prominent in the world trade of commodities, while the
global financial crisis triggered recessions across many countries that led to a
significantdeclineindemand(e.g.Wolf,2008;Kilian,2009).
15 Wehavealsocarriedoutthesameexerciseforallthreesectoralfactorsovertwosubsample
periods and we observed evolving relationships between sectoral commonalties and macro
fundamentals.Theseresultsareavailableonrequest.
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

Commoditypriceco-movement 517
Fig.3. TVP-FAVARcommonfactorresponse.Notes:Thethreegraphsinfigureplotthe
median impulse responses of the common factor (solid line) to each of the three macro
shocks that affect commodity returns. We also provide 16th and 84th percentile error
bandswithdashes.TheestimatesarebasedontheTVP-FAVARmodelinequation(11).
Eachpanelmeasureshowaunitimpulseofshocksimpactsthecommoditycommonfactor
overtime.Hereweusethefullsampleperiod.
Second, we find the commodity common factor responded negatively to a
one standard deviation contractionary monetary policy shock in real interest
rate–seethemiddlepanelofFigure3.16Notethatrealcommoditypricestendto
fall inresponsetohigherrealinterestrateuntilcommoditiesare‘undervalued’,
and future prices are expected to rise sufficiently to offset the higher interest
rate. Only then shall firms and investors hold inventories, despite the high car-
rying costs (Frankel, 2008). This negative effect is persistent over the entire
sampleperiodandthereisevidenceoftimevariationintheresponseofthecom-
modity prices, as the posterior intervals are narrow. The peak impact of real
16 Notethatapolicyinducedmonetarycontractioncantemporarilyraisetherealinterestratevia
ariseinthenominalinterestrate,afallinexpectedinflationorboth.
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

518 J.P.Byrneetal.
interestrateshocksoncommoditypriceswasduringthe2000s.Thiswasaperiod
ofrapidcommoditypriceinflationandtheFederalReservecarriedoutaggressive
expansionary policies to combat the dot.com bubble recession and kept interest
rates low, which sowed the seed of an asset price bubble that eventually burst in
2008(Hammoudeh,NguyenandSousa,2015).Inresponsetotheglobalfinancial
crisis, in December 2008, the Federal Reserve switched to the Zero Interest Rate
Policy (ZIRP), a seven-year period in which the target range for the Federal
Funds rate was pegged between 0 and 0.25 per cent. This was a period of low
productivitygrowthandtherealpriceofcommoditiesbecomelesselastictowards
to monetary policy shocks. With the commencement of the ZIRP, the Federal
Reserve had limited nominal interest rate ammunition to affect the economy in
general and asset prices in particular. Our result of a weaker post-crisis impact
fromrealinterestratesoncommonalitiesisconsistentwiththis.
Using our more flexible time-varying parameter methodology, the third
shock to the common factor that we consider is that of uncertainty. This
uncertainty proxy is from the commodity market, as discussed above. We
find uncertainty had a substantial negative impact on commodity commonal-
ities, see the bottom panel of Figure 3. The acutely time-varying impact is
closely associated with the Global Financial Crisis, in periods where market
volatility rose to levels that have rarely been seen since the Wall Street
Crash.17 Recall that commodities also fell sharply when uncertainty rose dur-
ing the crisis period – see Figure 1. We would like to point out that the
median value of commodity commonality reaches 0.8 in 2008Q3, which is a
much larger response than that for other shocks. For example, the median
value of the impact generated by the one standard deviation contractionary
monetary policy shock during that period was about 0.3. Hence, the Federal
Reserve needs to cut the interest rate by two to three standard deviations to
fully mitigate the negative effect on commodity price. Our finding is in line
with periods of pegged federal funds between 0 and 0.25 per cent. Although
stillimportant,we observea smaller impact oftheuncertainty shockoncom-
modities before and after the crisis in 2008. The latter reduction is consistent
with the partial success of a variety of government actions that were imple-
mented to promote the liquidity, solvency of credit markets and financial
market stability. As noted earlier, uncertainty effects are known to be short-
lived,andourtime-varyingresultshighlightthattheyareespeciallytimespe-
cific. As many economies were slow to emerge from the effects of the global
financial crisis, what we do not need is an increase in commodity market risk
that would adversely affect the price of a wide range of commodities. Our
resultsprovideanotherreasontopayattentiontocommoditymarketstability.
17 Recallthat,thereactionofsubprimemortgages andsecuritisedproductsraisedseriouscon-
cernsaboutthesolvencyandliquidityoffinancialinstitutions.Thisledin2008toafull-blown
bankingcrisisfollowingthefailuresofLehmanBrothers,andgovernmenttakeoversofFannie
Mae,FreddieMac,andAIG(IvashinaandScharfstein,2010).
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

Commoditypriceco-movement 519
5.2.3. Sector-specificcommonalitiesinaTVP-FAVARmodel
To account for heterogeneity in commodity prices, we now replace the com-
mon factor in our TVP-FAVARmodel with three sectoral factors for agricul-
ture raw materials, foodand metals. TheTVP-FAVARimpulse responsesfor
material, food and metal sectors in Figure 4 share some similarities. For
example, we find that aggregate demand shocks are positively related to the
realpriceofcommoditiesacrossallthreesectorsthroughoutmostofthesam-
ple period, while real interest rate shocks and uncertainty shocks are nega-
tivelyrelatedtocommoditypricesforcertainperiods.
There are important differences, however, among these three sectors’
responses to macro shocks that underscore heterogeneity in the commodity
market. The metal sector generally responds more positively to the global
business cycle than the material and food sector in Figure 4. One possible
Fig. 4. TVP-FAVAR sectoral factor responses. Notes: The nine graphs in the figure plot
themedianresponsesofthreesectoralfactors(Sectoral ) toeachofthethreemacroeco-
b,t
nomicshockswith16thand84thpercentileerrorbands.Thethreeshocksaretodemand,
therealinterestrateandrisk.TheestimateresponsesarebasedontheTVP-FAVARmod-
el in equation (11). Each panel measures how a unit impulse of shock impacts the com-
monalitiesofcommoditypricesovertime.Here,weusethefullsampleperiodtoconsider
thetime-varyingresponse.
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

520 J.P.Byrneetal.
explanation for this is that the unexpectedly rapid pace of industrialisation
and urbanisation of emerging economies has dramatically increased the
demand for metal commodities, such as copper, which are core materials in
constructions and electronics. Issler, Rodrigues and Burjack (2014) also pre-
sents empirical evidence that cycles in metal prices are synchronised with the
global economy. On the other hand, while greater economic activity without
commensurate increases in population raises incomes, this is less likely to
increase demand for food products overall and there may be substitution
effects between different food commodities (Carter, Rausser and Smith,
2011).
However, we observe more homogeneous responses among material, food
andmetalsectorstodemandafterthecrisis.Thisisconsistentwiththeearlier
literature on commodities moving together as an asset class (e.g. Byrne,
Fazio and Fiess, 2013, and West and Wong, 2014). A number of authors
study the cause of recent high food prices and increased cross-commodity
linkages, and they provide evidence of a positive relationship between bio-
fuel production and food prices, notably in the US (e.g. Mallory, Irwin and
Hayes, 2012; Avalos, 2014). The growth in the subsidised biofuel industry
raised concerns among stakeholders about global food shortages and food
poverty.
In terms of real interest rate shocks, the zero axes are always out with the
error bands for the agriculture raw materials andfood, unlike for metals, sug-
gesting that materials and food commodities are more sensitive to interest
rate shocks than metals – see the second column of Figure 4. In particular,
oursectoral evidence suggeststhat real interestshockshavea more persistent
impact on food prices, possibly because monetary policy is more closely
aligned with food prices than materials and metals. Furthermore, one of the
key transmission mechanisms for changes in real interest rates to commodity
pricefluctuationsis throughthe carryingcost ofinventories.Duringhighreal
interest rates periods, firms’ desire to carry food inventories decreased faster
compared to materials and metals. Food may be more interest-rate elastic
compared to other commodities, since the physical costs of food inventory
are already substantial and profit margins are therefore smaller. Our findings
are consistent with Hammoudeh, Nguyen and Sousa (2015), who also found
the effects of US monetary policy led to heterogenous responses from differ-
ent types of commodity sector prices, which depend on the characteristics of
particular commodity market (e.g. future price expectations, weather condi-
tions, storability of commodity, easiness of supply and strength of demand
forcommodityinventories).
Turning to the time-varying impact of risk, our measure of commodity
price uncertainty adversely affected the price of industrial commodities. This
effect wasparticularly acutetowardsthe endof2007,seethe thirdcolumnof
Figure4fortheresponseofthethreesectorstouncertainty.Theglobalfinan-
cial crisis caused a global recession and raised fears about future economic
conditions. The heterogeneous responses are reasonable, since a large risk
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

Commoditypriceco-movement 521
shock will reduce production activity and demand for raw materials and
metals. Food, on the other hand, is more impervious to risk and the financial
conditions more generally, possibly due to the importance of maintaining
foodconsumption,eveninacrisis.
To sum up our results so far, we provide empirical evidence that macro
fundamentals affect the returns of a large panel of commodities and these
effects vary over time. There is also important heterogeneity in the responses
oftheagriculturalrawmaterial,foodandmetalsectors.
5.3. Chinaandtheglobalcommoditymarket
Several studies suggest that strong economic growth in China since 2000 has
raised global demand for a broad range of commodities, and has resulted in
increasing commodity prices (e.g. Kilian, 2009; Roache, 2012; Frankel,
2014). Again, prior studies assumed the impact of macro determinants on
commodities has not changed over time. Therefore, we consider the extent to
which commonalities in commodity prices are affected by unexpected
increases in Chinese economic activity, accounting for heterogeneity and a
potentially evolving relationship over time. We use the real growth rate of
Chinese industrial production as a proxy for Chinese economic activity. We
focusonthemoretopicalpost2000period,duepartlytodataavailability.
Figure 5 plots time-varying impulse responses of the global commodity
factor and three sectoral factors to the one standard deviation increase in
Chinese demand immediately after the shock. The posterior median
response is once again the solid line and dotted lines are the 16th and 84th
percentiles of the posterior distribution. First, we find that unexpectedly
strong demand from China led to a persistent increase in the common fac-
tor of commodities and this effect was more substantive in 2008 and 2012.
The response of the common factor to Chinese demand is found in the top
left panel of Figure 5. When we consider the response of commodity sec-
tors to Chinese shocks, we again observe a strong positive impact on metal
commodities due to Chinese demand. Materials are only more recently
impacted by Chinese demand. Interestingly, we also find Chinese economic
activity impacted food prices. In fact, greater real economic activity leads to
higher level of incomes and rising incomes drive greater food consumption,
particularly in developing countries in which caloric intake is more responsive
to income growth (e.g. Carter, Rausser and Smith, 2011). Therefore, Chinese
economic activity, and not merely economic activity in the US, appears to
drive global food prices.18
18 Finally,wehavealsocheckedtheimpulseresponseofcommonandsectoralcommonalitiesto
Chinese demand shocks at representative points in time: 2003Q4, 2008Q4 and 2013Q4.
Consistentwiththecommonperception,weobserveapositiveresponseacrosstimeforboth
thecommonfactorandthreesectoralfactors.Theeffectistimevaryingwithapeakeffectin
2008Q4–seeFigureB1(AppendixinsupplementarydataatERAEonline).
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

522 J.P.Byrneetal.
Fig.5. TVP-FAVARfactorresponsestoChinesedemandshock.Notes:Thefourgraphs
infigureplotthemedianresponsesincommodityreturnsofcommonandthreesectorfac-
tors to Chinese demand shocks, plus 16th and 84th percentile error bands. The estimates
are based on the TVP-FAVAR model in equation (11). The sample period is based on
dataavailability.
5.4. Robustnesschecks
We have carried out several robustness check on our main results and results
are in Appendix B (in supplementary data at ERAE online). Our first robust-
ness check focuses on providing evidence that our assumptions on the identi-
fication order adopted in our impulse response analysis do not affect our
main empirical findings.19 First, we use the following Cholesky ordering:
real interest rate (R), real economic activity (Demand), risk (Risk ) and the
t t t
common factor (F). Figures B2 and B3 (in Appendix B in supplementary
t
data at ERAE online) show that the directions of the responses to the
19 Wewouldliketothankoneoftheanonymousreferees,whosuggestedconsideringtherobust-
nessofouridentificationorder.
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

Commoditypriceco-movement 523
structural shocks from both constant FAVAR and time-varying parameter
FAVAR with stochastic volatility models are qualitatively similar to our main
results (see Figures 2 and 3). Note that we also perform the same exercises for
sectoral factors(Sectoral ) and the new set of results in Figure B4 (Appendix
b,t
B in supplementary data at ERAE online) are in line with our baseline model
resultsinFigure4.Furthermore,FiguresB5–B7(AppendixBinsupplementary
data at ERAE online) report the results with four variables ordered as follows:
Y = [Risk, Demand, R, F or Sectoral ]. Again, we find that the responses
t t t t t b,t
ofcommoditycommonalitiestofundamentalshocksdonotqualitativelychange
ourmainconclusions.
Second, we re-estimate our models by replacing several variables in our
mainmodelwithalternativeproxies,suchasKilian’s(2009)globaleconomic
activity index, the federal funds rate, realised volatility of commodities and
stockmarketvolatility.WereporttheresultsinFiguresB8–B11(AppendixBin
supplementarydataatERAEonline),andwefindthattheresponsesofcommod-
ity commonalities to fundamental shocks are in line with our main results. In
addition, we have also tested the robustness of our TVP-FAVAR results by
employingdifferentdrawnumbersusedintheDHFM.FigureB12(AppendixB
in supplementary data at ERAE online) shows that the responses of commodity
commonalitiestofundamentalshocksarenotdifferentfromourmainfindings.
Furthermore, we also check the responses of commodity prices to three
macroshocksatthreedifferentpointsintimeusingtheTVP-FAVARwithsto-
chastic volatility models. Figure B13 (Appendix B in supplementary data at
ERAEonline) reportsthat theresponses of common factor areobserved at ten-
year intervals, i.e. 1988Q4,1998Q4 and2008Q4.20 Furthermore, we have also
checked the responses of both common and sector factors to Chinese demand
shocks at differenttimes – see FigureB14(AppendixB insupplementary data
at ERAE online). In sum, we find strong evidence of heterogenous responses
of commodity prices to macro shocks over time and across sector. These find-
ings underscore the importance of allowing for time variation in studying the
effectsofmacrofundamentalsoncommoditycommonalities.
6. Conclusion
Large swings in commodity prices have brought new momentum to the spirited
debate on their commonalities and determinants, and our paper extends this lit-
erature.Wefirstcontributetotheempiricalevidenceontheco-movementofreal
primary commodity prices. Unlike existing studies that extract principal compo-
nentsfromalargepanelofdata,weemployadynamichierarchicalfactormodel
fromMoench,NgandPotter(2013)todecomposetherealpriceofcommodities
intocommon,sectoral,sub-sectorandidiosyncraticcomponents.Wefindsignifi-
cant evidence of co-movement in commodity prices and, importantly, identify a
20 There are some notable differences in these responses in the representative periods for the
threeshocks.Forexample,wecanclearlyseeincreasingresponsesovertimeofcommodity
pricestodemandshock;theincreasingimpactoftherealinterestrateshockand,also,therisk
impulseresponsesbecomehighlynegativeandimportantin2008Q4.
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

524 J.P.Byrneetal.
commonfactorandthreesectoralfactors.Ourresultshighlighttheimportanceof
modelling common variations at different levels: for instance, common and sec-
toralfactorsmaysharesimilartrends,butthereisalsonotableheterogeneity.
Next, we empirically relate commodity price commonalities to (i) demand,
(ii) real interest rates and (iii) uncertainty. While existing studies often pre-
sent conflicting evidence of the impact of fundamentals using time-invariant
methodologies to examine the drivers of commodity prices co-movement,
this study uses a time-varying parameter factor augmented vector autoregres-
sion (TVP-FAVAR) model with stochastic volatility. This allows us to cap-
ture potentially unstable relationships to fundamentals and a time-varying
impactonthecommoditymarket.
The results from this analysis can be summarised as follows. First, we
show that positive innovations to the global business cycle cause a higher
price of commodities over time, especially after the 2000s. Second,real interest
rate shocks were found to have an important and negative effect on real com-
modity commonalities. Furthermore, we find that elevated risks negatively
impact commodity prices. This uncertainty effect on the real price of commod-
ities was most acute from the middle of 2007 and peaked at the end of 2008.
This finding is consistent with the idea that many asset classes suffered from
the adverse impact of the 2007–2008 global financial crisis. Last but not the
least, we extend the literature on the relationship between commodity prices
and macro determinants, while allowing for commodity heterogeneity. We find
important heterogeneity in the response of agricultural raw material, food and
metal sectors. For example, the material and metal sectors in general respond
more positively to the global business cycles and risk, while real interest rate
shockshaveamorepersistentimpactonfoodprices.
The results from this analysis can be summarised as follows. First, we
found that positive innovations to the global business cycle cause a higher
priceofcommoditiesovertime,especiallyafterthe2000s.Second,realinter-
est rate shocks were found to have an important and negative effect on real
commodity commonalities. Furthermore, we found that elevated risks nega-
tively impact commodity prices. This uncertainty effect on the real price of
commodities was most acute from the middle of 2007 and peaked at the end
of 2008. This finding is consistent with the idea that many asset classes suf-
fered from the adverse impact of the 2007–2008 global financial crisis.
Finally, we extended the literature on the relationship between commodity
prices and macro determinants, while allowing for commodity heterogeneity.
We found sectoral factors for agricultural raw material, food and metal sec-
torsrespondeddifferentlytomacroshocksatdifferentpointsintime.
In sum, our findings provide useful information for macroeconomic policy
making, consumption, capital investment, risk and portfolio management.
Our results suggest that the impact of the uncertainty shock at the global
financial crisis is large and it requires the central bank to cut the interest rate
aggressively. This finding supports the discussion of Mishkin (2009) who
proposes aggressive monetary policies during crises. Our results also imply
that the impact of the demand shock can be mitigated by monetary policies.
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

Commoditypriceco-movement 525
Moreover, our findings provide useful information for policy makers that the
effects of monetary policy vary over time and across sectors. Monetary
authorities need to take these relationships into account to ensure they pro-
duce their desired policy outcome. Recently, the US Federal Reserve began
to raise policy rates, and our empirical results indicate that this will impact
commodity prices. Our results are therefore informative for commodity
exporting and importing countries alike. They need to consider the prices of
imported and exported commodities and the effects of US monetary policy.
The spillovers of US monetary policy clearly play an important role in com-
modity orientated countries (Miranda-Agrippino and Rey, 2018). One inter-
esting question will be to find out whether our time-varying framework can
improve the predictability of commodity prices. We shall leave these issues
forfuturework.
Supplementary data
Supplementary data are available at European Review of Agricultural
Economicsonline
Acknowledgements
We are grateful for constructive comments and suggestions from three
anonymousrefereesandtheeditor.Weappreciatethefeedbackonthisarticle
from C.F. Baum for his specific comments as well as those of participants in
the 6th International Conference of the Financial Engineering and Banking
Society, 2016, Malaga, Spain. The authors are also grateful to Gary Koop,
Dimitris Korobilis and Serena Ng for sharing their MATLAB codes. The
views expressed in this paper are those of the authors and do not represent
those of the YJFX, Inc. and Keio Economic Observatory. The authors alone
areresponsibleforanyremainingerrors.
References
Abhyankar, A., Xu, B. and Wang, J. (2013). Oil price shocks and the stock market: evi-
dencefromJapan.EnergyJournal34(2):199–222.
Akram, Q. F. (2009). Commodity prices, interest rates and the dollar. Energy Economics
31(6):838–851.
Alam,M.R.andGilbert,S.(2017).Monetarypolicyshocksandthedynamicsofagricul-
turalcommodityprices:evidencefromstructuralandfactor-augmentedVARanalyses.
AgriculturalEconomics48(1):15–27.
Alquist, R. and Coibion, O. (2014). Commodity-price comovement and global economic
activity.NationalBureauofEconomicResearchWorkingPaperNo.20003.
Alvarez-Ramirez, J., Rodriguez, E., Martina, E. and Ibarra-Valdez, C. (2012). Cyclical
behavior of crude oil markets and economic recessions in the period 1986–2010.
TechnologicalForecastingandSocialChange79(1):47–58.
Antonakakis, D. and Kizys, R. (2015). Dynamic spillovers between commodity and cur-
rencymarkets.InternationalReviewofFinancialAnalysis41:303–319.
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

526 J.P.Byrneetal.
Avalos,F.(2014).Dooilpricesdrivefoodprices?Thetaleofastructuralbreak.Journal
ofInternationalMoneyandFinance42:253–271.
Barsky, R. and Kilian, L. (2004). Oil and the macroeconomy since the 1970s. The
JournalofEconomicPerspectives18(4):115–134.
Baumeister,C.andPeersman,G.(2013).Time-varyingeffectsofoilsupplyshocksonthe
USeconomy.AmericanEconomicJournal:Macroeconomics5(4):1–28.
Beck,S.E.(1993).Arationalexpectationsmodeloftimevaryingriskpremiaincommod-
ities futures markets: theory and evidence. International Economic Review 34(1):
149–168.
Beck, S. E. (2001). Autoregressive conditional heteroscedasticity in commodity spot
prices.JournalofAppliedEconometrics16(2):115–132.
Bernanke, B. S., Boivin, J. and Eliasz, P. (2005). Measuring monetary policy: a Factor
Augmented Vector Autoregressive (FAVAR) approach. Quarterly Journal of
Economics120:387–422.
Bollerslev, T. (1986). Generalized autoregressive conditional heteroscedasticity. Journal
ofEconometrics31(3):307–327.
Boughton, J. and Branson, W. (1991). Commodity prices as a leading indicator of infla-
tion.InK.LahiriandG.Moore(eds),LeadingEconomicIndicators.Cambridge,UK:
CambridgeUniversityPress,305–338.
Byrne, J. P., Fazio, G. and Fiess, N. (2013). Primary commodity prices: co-movements,
commonfactorsandfundamentals.JournalofDevelopmentEconomics101:16–26.
Byrne, J. P., Lorusso, M. and Xu, B. (2018). Oil prices, fundamentals and expectations.
EnergyEconomicshttps://doi.org/10.1016/j.eneco.2018.05.011.
Carter,C.A.,Rausser,G.C.andSmith,A.(2011).Commodityboomsandbusts.Annual
ReviewofResourceEconomics3:87–118.
Cashin, P., Liang, H. and McDermott, C. J. (2000). How persistent are shocks to world
commodityprices?IMFStaffPapers47:177–217.
Cashin,P.,McDermott,C.J.andScott,A.(2002).Boomsandslumpsinworldcommod-
ityprices.JournalofDevelopmentEconomics69:277–296.
Chen, S. L., Jackson, J. D., Kim, H. and Resiandini, P. (2014). What drives commodity
prices?AmericanJournalofAgriculturalEconomics96(5):1455–1468.
Cheng, H. and Xiong, W. (2014). Financialization of commodity markets. The Annual
ReviewofFinancialEconomics6:419–441.
Cuddington, J. T. (1992). Long-run trends in 26 primary commodity prices: a disaggre-
gated look at the Prebisch–Singer hypothesis. Journal of Development Economics 39:
207–227.
Cuddington, J. T. and Jerrett, D. (2008). Super cycles in real metals prices? IMF Staff
Papers55(4):541–565.
Daskalaki, C., Kostakis, A. and Skiadopoulos, G. (2014). Are there common factors in
individualcommodityfuturesreturns?JournalofBankingandFinance40:346–363.
Deaton, A. (1999). Commodity prices and growth in Africa. Journal of Economic
Perspectives13:23–40.
Dixit, A. and Pindyck, R. S. (1994). Investment Under Uncertainty. Princeton, NJ:
PrincetonUniversityPress.
Dwyer, A., Gardner, G. and Williams, T. (2011). Global commodity markets–price vola-
tilityandfinancialisation.RBABulletin:49–57.
Engle,R.(1982).Autoregressiveconditionalheteroscedasticitywithestimatesofthevari-
ance of United Kingdom inflation. Econometrica: Journal of the Econometric Society
50(4):987–1007.
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

Commoditypriceco-movement 527
Frankel, J. A. (2008). The effect of monetary policy on real commodity prices. In J. Y.
Campbell (ed.), Asset Prices and Monetary Policy. Chicago: NBER, University of
Chicago,andNBERWorkingPaperNo.12713.
Frankel, J. A. (2014). Effects of speculation andinterest rates ina ‘carry trade’ modelof
commodityprices.JournalofInternationalMoneyandFinance42:88–112.
Ghoshray, A., Kejriwal, M. and Wohar, M. (2014). Breaks, trends and unit roots in com-
modityprices:arobustinvestigation.StudiesinNonlinearDynamicsandEconometrics
18(1):23–40.
Gruber,J.W.andVigfusson,R.J.(2012).Interestratesandthevolatilityandcorrelation
of commodity prices. International Finance Discussion Papers 1065, Board of
GovernorsoftheFederalReserveSystem.
Hammoudeh, S., Nguyen, D. K. and Sousa, R. M. (2015). US monetary policy and sec-
toralcommodityprices.JournalofInternationalMoneyandFinance57:61–85.
Harvey, D. I., Kellard, N. M., Madsen, J. B. and Wohar, M. E. (2010). The Prebisch–
Singer hypothesis: four centuries of evidence. Review of Economics and Statistics 92
(2):367–377.
Issler,V.J.,Rodrigues,C.andBurjack,R.(2014).Usingcommonfeaturestounderstand
the behavior of metal-commodity prices and forecast them at different horizons.
JournalofInternationalMoneyandFinance42:310–335.
Ivashina,V.andScharfstein,D.(2010).Banklendingduringthefinancialcrisisof2008.
JournalofFinancialEconomics97(3):319–338.
Kilian, L. (2009). Not all oil price shocks are alike: disentangling demand and supply
shocksinthecrudeoilmarket.AmericanEconomicReview99(3):1053–1069.
Kilian, L. and Park, C. (2009). The impact of oil price shocks on the U.S. stock market.
InternationalEconomicReview50(4):1267–1287.
Kilian,L.andZhou,X.(2018).Modelingfluctuationsintheglobaldemandforcommod-
ities(No.18-4).BankofCanada.
Koop, G.andKorobilis, D. (2010).Bayesianmultivariate time series methodsfor empir-
icalmacroeconomics.FoundationsandTrendsinEconometrics3:267–358.
Kulatilaka, N. and Perotti, E. C. (1998). Strategic growth options. Management Science
44(8):1021–1031.
Lombardi, M. J., Osbat, C. and Schnatz, B. (2012). Global commodity cycles and lin-
kages:aFAVARapproach.EmpiricalEconomics43(2):651–670.
Mallory,M.L.,Irwin,S.H.andHayes,D.J.(2012).Howmarketefficiencyandthethe-
oryofstoragelinkcornandethanolmarkets.EnergyEconomics34(6):2157–2166.
Miranda-Agrippino, S. and Rey, H. (2018). US monetary policy and the global financial
cycle.NBERWorkingPaperNo.21722.
Mishkin, F. S. (2009). Is monetary policy effective during financial crises? American
EconomicReview:Papers&Proceedings99(2):573–577.
Moench, E.,Ng,S.andPotter,S.(2013).Dynamichierarchical factormodels.Reviewof
EconomicsandStatistics95(5):1811–1817.
Nakajima, J., Kasuya, M. and Watanabe, T. (2011). Bayesian analysis of time-varying
parametervectorautoregressivemodelfortheJapaneseeconomyandmonetarypolicy.
JournaloftheJapaneseandInternationalEconomies25(3):225–245.
Neftci,S.N.andLu,Y.(2008).Financialinstrumentstohedgecommoditypriceriskfor
developingcountries.InternationalMonetaryFundWorkingPaperWP/08/6.
Odom, P. (2010). Shipping indexes signal global economic trends. Annual Report,
GlobalizationandMonetaryPolicyInstitute,28–35.
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026

528 J.P.Byrneetal.
Ouenniche,J.,Xu,B.andTone,K.(2014).Relativeperformanceevaluationofcompeting
crude oil prices’ volatility forecasting models: a slacks-based super-efficiency DEA
model.AmericanJournalofOperationsResearch4(4):235–245.
Pindyck, R. S. and Rotemberg, J. J. (1990). The excess co-movement of commodity
prices.EconomicJournal100:1173–1187.
Poncela,P.,Senra,E.andSierra,L.P.(2014).Commondynamicsofnonenergycommod-
itypricesandtheirrelationtouncertainty.AppliedEconomics46(30):3724–3735.
Prebisch, R. (1950). The economic development of Latin America and its principal pro-
blems.Reprintedin:EconomicBulletinforLatinAmerica,7,1962,1–22.
Primiceri,G.E.(2005).Timevaryingstructuralvectorautoregressionsandmonetarypol-
icy.ReviewofEconomicStudies72:821–852.
Ratti,R.A.andVespignani,J.L.(2015).CommoditypricesandBRICandG3liquidity:
aSFAVECapproach.JournalofBankingandFinance53:18–33.
Ravazzolo,F.andVespignani,J.L.(2017).Worldsteelproduction:Anewmonthlyindi-
cator of global real economic activity. University of Tasmania, Tasmanian School of
BusinessandEconomicsWorkingPapersNo.2017-08.
Roache, S. K. (2012). China’s impact on world commodity markets. International
MonetaryFundWorkingPaperWP/12/115.
Scrimgeour, D. (2014). Commodity price responses to monetary policy surprises.
AmericanJournalofAgriculturalEconomics97(1):88–102.
Singer, H. (1950). The distribution of gains between investing and borrowing countries.
AmericanEconomicReview40:473–485.
Singleton,K.J.(2013).Investorflowsandthe2008boom/bustinoilprices.Management
Science60(2):300–318.
Stock, J. H. and Watson, M. W. (2005). Implications of dynamic factor models for VAR
analysis.NationalBureauofEconomicResearchWorkingPaperNo.11467.
Stock,J. H.andWatson,M.W. (2009).Forecasting indynamic factormodelssubject to
structural instability. The Methodology and Practice of Econometrics. Hendry: A
FestschriftinHonourofDavidF,173–205.
Svensson,L.E.O.(2008).Theeffectofmonetarypolicyonrealcommodityprices:com-
ment.InJ.Y.Campbell(ed.),AssetPricesandMonetaryPolicy.Chicago,IL:NBER,
UniversityofChicago.
Vansteenkiste,I.(2009).Howimportantarecommonfactorsindrivingnon-fuelcommod-
ityprices?Adynamicfactoranalysis.ECBWorkingPaper1072,July.
West, K. D. and Wong, K. F. (2014). A factor model for co-movements of commodity
prices.JournalofInternationalMoneyandFinance42:289–309.
Wolf, M. (2008). Life in a tough world of high commodity prices. Financial Times
Wednesday,March4,2008.
Xu, B. and Ouenniche, J. (2012). A data envelopment analysis-based framework for the
relative performance evaluation of competing crude oil prices’ volatility forecasting
models.EnergyEconomics34(2):576–583.
Yin, L. and Han, L. (2015). Co-movements in commodity prices: global, sectoral and
commodity-specificfactors.EconomicsLetters126:96–100.
Downloaded
from
https://academic.oup.com/erae/article/47/2/499/5486456
by
Università
Bocconi
user
on
30
June
2026