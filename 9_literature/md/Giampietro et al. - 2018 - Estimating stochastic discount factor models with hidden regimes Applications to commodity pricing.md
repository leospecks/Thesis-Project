European Journal of Operational Research 265 (2018) 685–702
Contents lists available at ScienceDirect
European Journal of Operational Research
journal homepage: www.elsevier.com/locate/ejor
Innovative Applications of O.R.
Estimating stochastic discount factor models with hidden regimes:
Applications to commodity pricing
Marta Giampietro a, Massimo Guidolin b , ∗, Manuela Pedio a
a Bocconi University, Italy
b IGIER, Bocconi University, Italy
a r t i c l e i n f o a b s t r a c t
Article history: We develop new likelihood-based methods to estimate factor-based Stochastic Discount Factors (SDF) that
Received 30 November 2015 may accommodate Hidden Markov dynamics in the factor loadings. We use these methods to investigate
Accepted 13 July 2017 whether it is possible to find a SDF that jointly prices the cross-section of eight U.S. portfolios of stocks,
Available online 2 August 2017
Treasuries, corporate bonds, and commodities. In particular, we test a range of possible different speci-
Keywords: fication of the SDF, including single-state and Hidden Markov models and compare their statistical and
Finance pricing performances. In addition, we assess whether and to which extent a selection of these models
Commodities replicates the observed moments of the return series, and especially correlations. We report that regime-
Stochastic discount factor switching models clearly outperform single-state ones both in term of statistical and pricing accuracy.
Hidden Markov model However, while a four-state model is selected by the information criteria, a two-state three-factor full
Vector Autoregression model outperforms the others as far as the pricing accuracy is concerned.
©2017ElsevierB.V.Allrightsreserved.
1. Introduction ize the estimation of HMM stochastic discount factors (hence-
forth, HMM SDF) that relies on variations of standard Expectations-
The interest of institutional investors in commodities has signif- Maximization algorithms to maximize the log-likelihood function. 1
icantly increased over the last two decades. Over the same period, When applied to commodities, the classical asset pricing re-
due to the appearance of exchange traded funds, retail investors search issues—for instance the nature of the factors driving risk
have developed a growing taste for this asset class. This is due to premia and volatility—have been approached in a number of ways:
the fact that commodities can generate equity-like returns in the some researchers have employed commodity-specific factors (see,
long-run, act as risk diversifiers both in the short- and in the long- e.g., Szymanowska, de Roon, Nijman, & Van den Goorbergh, 2012 ;
run, and serve as an inflation hedge (see, e.g., Erb & Harvey, 2006; Yang, 2013; BGR, 2014 ); others have used models designed to price
Gorton & Rouwenhorst, 2006 ). Despite their growing importance all assets (see, e.g., Asness, Moskowitz, & Pedersen, 2013; Koijen,
in institutional and retail portfolios, our understanding of this as- Moskowitz, Pedersen, & Vrugt, 2013 ). The former approach consid-
set class remains unsatisfactory. While the literature is extensive as ers commodities as a separate asset class for which specific pricing
far as traditional asset classes, especially where equities are con- factors are needed; the latter assumes that financial markets are
cerned, there is no consensus on whether there is an asset pricing perfectly integrated and hence that a unique measure able to price
model which can effectively explain both the cross-sectional and all assets can be found. Moreover, most studies have tested asset
the time series variation in commodity returns (see, e.g., the dis- pricing models on commodity return data in a stand-alone fashion
cussion in Bakshi, Gao, & Rossi, 2014 , henceforth BGR). while few others have augmented the test asset menu with other
Part of the reason of this lack of in-depth understanding of asset classes (see e.g., Asness et al., 2013 ).
commodities, is that they require the development of new meth- Amid this heterogeneity of approaches, a conclusion as to the
ods and operational approaches. Our paper explores such combi- best asset pricing model for commodities has not been found yet.
nation of novel methods, i.e., Hidden Markov chain models (HMM), Following the second strand of literature, we develop a range of
to describe time heterogeneity (see Dias, Vermunt, & Ramos, 2015 ) different specifications of SDFs based on macroeconomic factors,
in the fundamental pricing measure governing the cross-section
of asset returns. We also develop a methodology to operational-
1 SDF models are based on the result that in the absence of arbitrage, the price
of an asset at time t is the expected discounted value of the asset payoffin period
∗ Corresponding author. t + s , based on information available at time t , when discounting and integration are
E-mail address: massimo.guidolin@unibocconi.it (M. Guidolin). performed under the risk neutral measure implied by the SDF.
http://dx.doi.org/10.1016/j.ejor.2017.07.045
0377-2217/©2017 Elsevier B.V. All rights reserved.

686 M. Giampietro et al. / European Journal of Operational Research 265 (2018) 685–702
constructed by extracting three, five (and to some limited extent, commodity returns has risen dramatically since mid-2008 (see,
ten) principal components from a broad set of variables concern- e.g., Büyüksahin & Robe, 2014; Tang & Xiong, 2012 ). 2
ing prices, production, and the labor and housing markets, as in Our empirical results can be summarized as follows. First, we
Ludvingson and Ng (2009) . Our objective is to assess whether there find strong evidence that HMMs outperform their single-state
exist one or more specifications of the SDF that jointly prices the counterparts both in terms of statistical and pricing accuracy. In-
cross-section of stock, bond, and (spot) commodity returns and deed, not only all the information criteria select HMMs over their
that replicates the empirically observed moments of returns, with (more parsimonious) single state counterparts, but also the latter
a specific interest for the matrix of correlations among pairs of strongly underperforms the former with respect in the pricing per-
commodities as well as across asset classes. Our tested models in- formance space. Indeed, standard chi-square tests on the differ-
clude both standard linear projections of latent SDFs on the pric- ences between model-implied and observed returns leads to re-
ing factors and a set of different specification of HMM SDFs which jection of the null of equal values for all the single-state SDF spec-
incorporate latent regime shifts governed by one ergodic and irre- ification. On the contrary, for four different specifications of HMM
ducible Markov chain that drives shifts in the coefficients that map SDF we fail to reject the null that the predicted returns are differ-
the K priced factors into the SDF. ent from the observed ones. In particular, a two-state three-factor
In our application to commodity research, we use a cross sec- full MSVAR model seems to rank first in terms of pricing accu-
tion of eight portfolios of stocks, Treasuries, corporate bonds, and racy. In addition, although single-state and HMM models seem to
commodity indices (the S&P-GS Agriculture and livestock, precious deliver similar performances in terms of matching the empirically
metals, industrial metals, and energy indices) over the period Jan- observed moments of the asset returns, the two-state HMM model
uary 1989–December 2011 as test assets. To test which, if any, more accurately matches the pair-wise correlations between com-
model specification(s) is best able to price the cross-section of the modities and traditional asset classes.
returns of our test assets, we employ a number of different tests. Second, despite some models (i.e., regime-switching ones) are
First, we conduct a standard specification search by comparing the closer to HJ’s bound than others, when we formally test the null
values of three different information criteria that provide a mea- of a zero distance, all models—both single-state and HMM—are re-
sure of the statistical accuracy of the different models. Second, we jected. This result may be read in the light of the claim of many
test the pricing accuracy of our alternative specifications. In par- researches (see, e.g., Szymanowska et al., 2012 ; BGR, 2014 ) that
ticular, we assess whether the in-sample differences between the commodities are segmented from other asset classes and needs to
observed and predicted returns implied by each model are statisti- be priced using commodity specific factors. Therefore, we test the
cally significant using a standard Chi-squared test. In addition, we robustness of our top performing model (namely a two-state three
adopt Hansen–Jagannathan’s (henceforth HJ) distance measure to factor full MSVAR) against an SDF-version (with obvious goals of
quantify the distance between the candidate SDFs and what is em- comparability) of the linear factor model proposed by BGR based
pirically required to price our assets. Finally, we explore whether on three commodity-specific factors: Average, Carry, and Momen-
model-implied moments (mean, standard deviation, skewness, kur- tum. We find that the pricing performance of our model dominates
tosis, and, above all, correlations) are able to match empirical the one of the benchmark in terms of HJ distance. This establishes
ones. that a large HJ distance does not exclusively plague our modeling
To the best of our knowledge, our contribution is original for efforts and appears to be pervasive even to important benchmarks
(at least) two reasons. First, when we extend our model to in- in the literature.
clude latent regime shifts governed by one ergodic and irreducible The rest of the paper has the following structure. Section 2 in-
Markov chain, we test whether there is evidence of a need of ad- troduces SDF models. Linear factor SDF models are presented in
ditional parametric flexibility to price a range of asset classes that Section 2.1 and are generalized to the HMM case in Section 2.2 .
includes commodities. It is generally accepted that financial mar- Section 2.3 presents the maximum likelihood estimation strategy
kets follow boom-and-bust cycles that involve both the mean and and explains in detail how the Baum–Welch algorithm can be used
the volatility of asset returns (see Guidolin, 2011 ). Recently, the to implement it. Section 3 introduces the data used in our applica-
awareness that also correlations between returns on different as- tion. Section 4 contains our application and key empirical findings.
set classes would undergo massive changes has emerged (see Bae, Section 5 concludes.
Kim, & Mulvey, 2014 ). While the literature has mainly focused on
stocks and bonds (see, e.g., Guidolin & Timmermann, 2006 ), the 2. The methodology: factor-based SDF models
number of researchers who has applied Hidden Markov models
(HMM) to commodities is limited (see, e.g., Alizadeh, Nomikos, & SDF models provide a general framework for pricing assets:
Pouliasis, 2008; Bae et al., 2014; Lee & Yoder, 2007 ). We contribute many existing asset pricing methods, such as the capital asset
to this strand of research even though our focus is not simply on pricing model, the general equilibrium, consumption-based, inter-
the modeling of regimes and time-varying moments in commodity temporal capital asset pricing model, and also Black and Scholes’
returns, but the on-time variation that is induced by the presence formula, can all be shown to be specializations of SDF models to
of regime shifts in the relationships between the SDF and an inter- reflect specific assumptions. One SDF is defined by a simple propo-
pretable set of priced risk factors. sition: the price of an asset at time t is equal to the expected pay-
Our second contribution is that we look for an SDF that not off of the asset in t + 1, based on information available at time t:
only prices the cross-section of stock, bond, and commodity re-
turns, but also replicates their observed correlations. This is partic- p i,t = E [M t +1 X i,t+1 | (cid:3) t ] i = 1 , . . . , n, (1)
ularly useful in the light of the recent developments in the com-
modity markets. While there is some evidence that prior to the where p i,t is the price of the i th asset at time t , X i,t+1 is the asset
early 20 0 0s, commodities shared co-movements with stocks (see payoff in t + 1 (inclusive of future sale prices and any cash flows
Gorton & Rouwenhorst, 2006 ) or each other (see Erb & Harvey, paid between t and t + 1), M t +1 is the SDF (a random variable), and
2006 ), it seems well established in the minds of investors and re- E[ ·| (cid:3) t ] indicates the expectation based on the information available
searchers that the commodity markets have recently undergone
deep changes: commodity prices have experienced booms fol-
2 There is no consensus as to the explanations for this evidence but many com-
lowed by significant busts and the correlation between stock and
mentators agree on the financialization of commodities as a cause (see, e.g., Basak
and Pavlova, 2013; Büyük s¸a hin and Robe, 2014 ).

M. Giampietro et al. / European Journal of Operational Research 265 (2018) 685–702  687
at time t . The existence of an SDF is equivalent to the law of one  At this point, if we assume that the random vector y  t + 1 [ m  t + 1 ,
(cid:4)
price, its positivity is equivalent to the absence of arbitrage oppor-  f  1,t + 1 , f  2,t + 1 , … f  K ,t + 1 , r  1,t + 1 , r  2,t + 1 , … r n ,t + 1 ]  expanded to include
tunities, and its uniqueness is equivalent to market completeness.  the factors driving the SDF, has a stationary multivariate Gaussian
, we obtain
If w e divide both  sides of Eq. (1) by p  i,t  distribution, then Appendix A shows that the asset pricing model
| (cid:2) |     | (cid:3)     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|         | X   |   i,t + 1 | |     | |   |     |     |     |     |     |     |     |     |     |     |     |
1 = E M  +1   (cid:3) t   = E [M   +1  (  1 + R  )    (cid:3) t  ],   (2)  | (cid:2) | (cid:2) 1   σ 2  1   σ  −σ
t p   t i,t+1  E [r   i,t+1    t ] = −E [ m  +1    t ] −   − 2 i,m  (5)
|           |               | i, t       |                     |                                 |                            |                 |       |               |           | t        | 2              | m 2        | i             |                  |                 |
| --------- | ------------- | ---------- | ------------------- | ------------------------------- | -------------------------- | --------------- | ----- | ------------- | --------- | -------- | -------------- | ---------- | ------------- | ---------------- | --------------- |
| w h e r e |   1   +   R   | =   X      | /   p   i s   t h e |   g r o s s   r e t u r n   o f |   a s s e t   i  .   ( 2 ) |   i s   t h e   |       |               |           |          |                |            |               |                  |                 |
|           | i , t         | + 1   i ,t | + 1   i , t         |                                 |                            |                 |       |               |           | σ 2   ≡  |                |  , σ 2   ≡ | 1             |  ,               | σ ≡             |
|           |               |            |                     |                                 |                            |                 | o b t | a i n s ,   w | h e r e   | m   V  a | r [  m t   + 1 |  ]         |  V   a r [  r |   i , t + 1  ]   | a n d   i , m   |
s t a n d a r d   E u l e r   c o n d i t i o n   u n d e r   a   g e n e r i c   S D F ,   M   t  +  1  ,   d e r i v e d   i n   a   , i 2
|     |     |     |     |     |     |     | C o v |  [  r   i, t + 1     m | t  + 1   ]  .   B | e c a u s e   | i t   i s   w | e l l   k n o w | n   t h a t   | t h e   t i m | e   t   p r i c e   o f   |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------------------- | ----------------- | ------------- | ------------- | --------------- | ------------- | ------------- | ------------------------- |
r e p r e s e n t a t i v e   a g e n t   f r a m e w o r k .   W e   d e fi n e   m   t  +  1   l n  M   t  +  1  ,   r   i  ,t   +  1   l n ( 1   |  (cid:2)
+ + a   r i s k l e s s ,   o n e - p e r i o d   z e r o   c o u p o n   b o n d   e q u a l s   1 /   E [  M t   + 1   t  ]  ,   a n d
|  R   i  , t  +  1 |   )   a n d   u |   i  ,t  +  1   m |   t  +  1     r   i ,t  +  1  .   I | f   t h e   r a n d o m   v | e c t o r   y   t  +  1   | [  m   t  +  1  ,   |     |     |     |     |     |     |     |     |     |
| ----------------- | --------------- | ----------------- | ----------------------------------- | --------------------------- | ------------------------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:4)   (cid:2) { } th a t   a s   a   r e s u l t ,   t h e   c o n t i n u o u s ly   c o m p o u n d e d   r i s k l e s s   r e t u r n   i s
| r   t +  1  ,   | r    +  1  ,   … | r  n    + |  1   ]   ,   w i t h   t |   ≡  y t  − s      ≥   ⊂ (cid:3) | t    ,   h a s   a   s t | a t i o n -   |     |     |     |     |     |     |     |     |     |
| --------------- | ---------------- | --------- | ------------------------ | -------------------------------- | ------------------------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 ,             | 2 , t            | , t       |                          | s 0                              |                          |               |     |     |     |     |     |     |     |     |     |
a ry ,  h o m o s kedastic multivariate Gaussian distribution, Appendix A   = −E [m  | 1   σ
|          |           |     |     |     |     |     | r  f |     |  +1    (cid:2) t ] − | 2     | ,   |     |     |     | (6)  |
| -------- | --------- | --- | --- | --- | --- | --- | ---- | --- | -------------------- | ----- | --- | --- | --- | --- | ---- |
| sh o w s |   th a t  |     |     |     |     |     | t    |     | t                    | 2   m |     |     |     |     |      |
1
E [r   | (cid:2) t ] = −E [m  | (cid:2) t ] − V ar [m  the model is equivalently re-written as:
| i,t+1  |     | t  +1  |     | t  +1 ]  |     |     |     |     |     |     |     |     |     |     |     |
| ------ | --- | ------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
1
|     |     | 1   |     |     |     |     |     | | (cid:2) t ] +  | σ   | 2  −r  f  = −σ |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------------- | --- | --- | --- | --- | --- |
− V ar [r   i,t+1 ] −Cov [r   i,t+1  , m  +1 ],   (3)  E [r   i,t+1    i   t   i,m  (7)
|                                                                    |     | 2   |     | t   |     |     |              |     | 2                                                       |     |     |     |     |     |     |
| ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| which establishes a functional link between conditional risk pre-  |     |     |     |     |     |     |              | σ2  |                                                         |     |     |     |     |     |     |
|                                                                    |     |     |     |     |     |     | where 0 . 5  |     |   is a standard Jensen’s inequality correction and the  |     |     |     |     |     |     |
|                                                                    |     |     |     |     |     |     |              |     | i  behind the risk premium is therefore −σ              |     |     |     |     |     |     |
mia on any asset or portfolio, the corresponding first and second  driving forc e i,m , as one
moments of the assumed SDF, and the covariance between such  would expect: the higher the covariance between asset returns and
an operator and the net returns on the very asset. Moreover, this  the SDF (hence, the higher the covariance between asset returns
general expression can be specialized further when assumptions  and marginal utility that is high in bad states), the lower the risk
are imposed on the SDF functional form. In the following, we dis-  premium on the asset.
tinguish between two cases, the single- vs. the multi-state, HMM  Appendix A also shows that under a rather standard stationary
case. Moreover, we do not take a stance as to whether the SDF is  VAR( P ) representation for the process followed by the factors, the
unique or not, but we focus—under any assumed model structure—
full joint model for the SDF and asset returns is:
to the SDF that maximizes some statistical criterion and therefore
e m e r g e s   fr o m   t h e  d a t a.   T h e re f o r e ,  i n   t he   c a s e   o f   m a r ke t   in c o m -   (cid:5)K
|     |     |     |     |     |     |     |     | =  γ | +   | γ + w |     | (   | ≡m  | −E [m  | | (cid:2) ) |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ----- | --- | --- | --- | ------ | ----------- |
p let e n e s s   (a s  i n   M a rr o q u ì n - M a r ti n e z   &   M o r e n o ,   2 0 1 3 ) ,  w e   a ss u m e   m t  +1  0  j f  j,t+1  t  +1   w t  +1  t  +1  t  +1    t ]
j=1
that the portfolios are replicable, so that their equilibrium return
(cid:5)K  (cid:5)P
| does not depend on the SDF selected.  |     |     |     |     |     |     |        | ϕ       |           | ϕ                     |                | δ       |                    |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | ------- | --------- | --------------------- | -------------- | ------- | ------------------ | --- | --- |
|                                       |     |     |     |     |     |     | f      | =       | +         |   j,k,p f             |                | +       | j = 1 , . . . , K  |     |     |
|                                       |     |     |     |     |     |     | j,t+1  | j, 0    |           |                       | k,t+1 −p       | j,t+1   |                    |     |     |
| 2.1. Linear factor SDF models         |     |     |     |     |     |     |        |         | k =1 p=1  |                       |                |         |                    |     |     |
|                                       |     |     |     |     |     |     |        | (cid:7) |           |                       |                | (cid:8) |                    |     |     |
|                                       |     |     |     |     |     |     |        |         | σ         | σ                     | σ              |         |                    |     |     |
|                                       |     |     |     |     |     |     | r      | = −     | 0 . 5  2  | +  0  . 5             | 2  +           | −m  +1  | + v                |     |     |
|                                       |     |     |     |     |     |     | i,t+1  | (cid:9) | m         |   (cid:10) (cid:11) i |   i,m(cid:12)  | t       | i,t+1              |     |     |
Suppose t (cid:4) he SDF has the lo (cid:6) g-linear structure,
|     |     |            |     |     |     |     |     |     |     | μ   |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | (cid:5)K   |     |     |     |     |     |     |     | i   |     |     |     |     |     |
μ
M  +1  = exp  γ +  γ j f  > 0 ,  (4)  =  i  −m  +1  + v   i,t+1  ,  i = 1 , . . . , n  (8)
| t   |     | 0   | j,t+1  |     |     |     |     |     | t   |     |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j=1  which can also be represented as ( In d {·} is a standard indicator
| where f  | 1,t + 1 , f  | 2,t + 1 , …, f  | K ,t + 1 are K systematic factors driving the  |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ------------ | --------------- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
function):
w a y   i n   w h i c h   a ll   a ss e t s  a re   p ri c e d .   I n   t h e  f o l l o w in g ,   a ls o  fo r  id e n t i-   (cid:13) (cid:14)
|             |               |               |                    |                                   |                  |             |       | (cid:4)  | (cid:4)  |        |     |     |     |     |     |
| ----------- | ------------- | ------------- | ------------------ | --------------------------------- | ---------------- | ----------- | ----- | -------- | -------- | ------ | --- | --- | --- | --- | --- |
|             |               |               |                    |                                   |                  |             | 1     | 0  K     | 0  n     |        |     |     |     |     |     |
| fic a t i o | n   p u r p o | s e s   w h e | n   th e   m o d e | l   i s   g e n e r a l i z ed  t | o   t h e  H M M |   ca s e ,  |       |          |          |        |     |     |     |     |     |
|             |               |               |                    |                                   |                  |             | 0  K  | I  K     | O  K×n   | y  +1  |     |     |     |     |     |
we assume that the K factors are observable. Positivity of M t  +1 en-  t
|     |     |     |     |     |     |     | 0  n  | O    ×   | I n  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ---- | --- | --- | --- | --- | --- | --- |
s u r e s   t h e   a b s e n c e   o f   a r b i t r a g e   o p p o r t u n i t i e s .   N o t i c e   t h a t   t h e   v e c -   n K (cid:13)   (cid:14)
γ ≡ γ , γ , γ ,  .  .  . γ (cid:4)  0 γ ¨ (cid:2)  In  d { 0 (cid:4)
t o r   [   0     1     2     K   ]   r e s t r ic t s   t h e   r e l a t i o n s h ip   b e t w e e n   t h e   P(cid:15) − 1      l   l =0 }    n
|     |     |     |     |     |     |     | =  μ | +   |     |     | (cid:3) |     |     | +  η | (9)  |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ------- | --- | --- | ---- | ---- |
p r i c e s   o f   a l l   a s s e t s   a n d   t h e   p r i c e d  r i s k   f a c t o r s   to   b e   h o m o g e n e o u s     0   K   l  O   K × n  y t  +1 −l  t+1 or
|     |     |     |     |     |     |     |     | l=0  | −ι  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
across assets according to the fundamental Euler condition in ( 2 ).  n In d {l =0 }  O  n ×K  O n ×n
(cid:15)
T h e r e   i s  o f   c ou r s e   c o n s i d e r a b l e   l a t it u d e   i n   th e   d e fi n it io n   o f  w h a t  μ+  P − 1  η (cid:3)
|     |     |     |     |     |     |     | A  0 y |  +1  =  |     | A  l y  +1 −l  | +  t+1 with  |     | 0  = O  | K×K  |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | --- | -------------- | ------------ | --- | ------- | ---- | --- |
ar e   t h e   p ri c e d  r i s k   fa c t o r s   t h a t   e n t e r   M    .  E it h e r   ex p a n d in g   th e ir   t t
|     |     |     |     | t + 1 |     |     |     |     | l = 0 |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
number ( K → ∞ ) or by carefully selecting their identity, these will
|     |     |     |     |     |     |     |     | μ   | γ   | ϕ ϕ |     | ϕ −( 0 . 5  | σ 2  (  | γ) + 0 . 5  | σ  +  σ ) ,  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ----------- | ------------ |
i m p ro v e   t h e  fi t  o f   t h e   m o d e l . 3   A l t h o u g h   it  w o u l d   b e   i n t e r e s ti n g  to   w h ere   ≡ [     ,      ,  0  ,    2 ,  0   ,  .  .  .    ,  0     2 1 ,m
|     |     |     |     |     |     |     |     | σ   | 2  γ 0 | 1 σ  + | σ   | (cid:4)   K | m   |     | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | --- | ----------- | --- | --- | --- |
d er iv e  (  4  )   f ro m   a   g e n e r al   e q u il i b r i u m   f ra m e w o r k ,  i n   t h i s   p a p e r  w e   . .  . − ( 0  .  5  (   )   +  0  .  5   2   ,   ) ]  ,  o r
|     |     |     |     |     |     |     |     |     | m   | n   | n m |     |     |     |       |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     | ⎡   |   ⎤   |
t a k e   s u c h   a   s tr u c t u re   o f   t h e  S D F   a s   a   p r i m i t i v e   b u t  e s t i m a b l e   f u n c -   (cid:13) (cid:14) γ
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t io n a l   fo r m   a n d   d i s c u s s   i n s t e a d   t h e   i d e n t it y ,   t h e   n u m b e r   o f   t h e   f a c -   γ ⎢ γ ⎥
|     |     |     |     |     |     |     |     |     |     |     | 0   |     |     | ⎢   |   2   ⎥   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
t o r s ,   a n d   ( in   S e c ti o n  2 . 2  )   t h e   n u m b e r   o f  h i d d e n   s t a t e s   a f f e c t i n g   t h e   μ≡ ϕ   γ ¨ ≡
|     |     |     |     |     |     |     |     |     |     |     | 0   |     |     | l  ⎣ |   . .     ⎦   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------- |
lo a d i n g s .   − 0 . 5  σ 2  ( γ)  −0 . 5  d i a  g  ( (cid:7))  −(cid:7) e  .
|     |     |     |     |     |     |     |     |     | m     |     | 2: n +1  |     | 1   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | -------- | --- | --- | --- | --- |
γ
|     |     |     |     |     |     |     |     | ⎡   |     |     |     | ⎤   |     |     | K   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3   |     |     |     |     |     |     |     |  ϕ  | ϕ   |     | ϕ   |     |     |     |     |
A few special cases may provide meaningful benchmarks. Clearly, when in ( 4 )      ···
|     |     |     |     |     |     |     |     | l, 1 , 1  | l, 1 , 2  |     | l, 1 ,K  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | -------- | --- | --- | --- | --- |
K  =  1   a n d   f   1 ,t  +  1   i s  t h e   g r o s s   r e t u r n   o n   t h e   m a r k e t   p o r t fo l i o ,   t h e n   t h e   S D F   b e c o m e s   ⎢   ϕ   ϕ   · · · ϕ   ⎥
          =          t      r ,  γ   (cid:3) ⎢ l,  2  , 1  l,  2  , 2  l,  2  ,K  ⎥
t h e s t a n d a r d C A P M . W h e n K 1 a n d f 1 ,t  +  1   i s h e l o g - c o n s u m p t i o n g r o w t h a t e 0   is l  ≡ ⎣   .   .   .  .   ⎦
t h e   s u b j e c t i v e   r a t e   o f  d i s c o u n t ,   a n d   γ   i s   t h e   o p p o s i t e   o f  t h e   c o n s t a n t   c o e ffi c i e n t   o f    .   .   . . .
|     |     |     | 1   |     |     |     |     | .   |     | .     | .   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
re l a tiv e   r is k   a v e r s io n ,  w e   ob t a i n   t h e   cl as s ic a l  c o n s u m p ti o n  ( C )C A P M .   D e   R o o n  a n d   ϕ ϕ ϕ
|             |                    | )  t               |                           |   s   v                              |                              | y              |     |   l,K, 1  |   l,K, 2  | ···  |   l,K,K    |     |      |     |            |
| ----------- | ------------------ | ------------------ | ------------------------- | ------------------------------------ | ---------------------------- | -------------- | --- | --------- | --------- | ---- | ---------- | --- | ---- | --- | ---------- |
| S z y m a n | o w s k a ( 2 0    | 1 0 te s w         | h e t h e r c o m m o     | d i ty fu t u r e re t u rn s        | a ry cr o s s -s e c         | t io n a ll    |     |           |           |      |            |     |      |     |            |
| du e  t o   | d i ff e r e n c e | s  i n   c o n s u | m p t io n  r i s k   a n | d   t h e y   fi n d   t h a t  a t  | q u a r te r l y   h o r i z | o n ,  t h e   |     |           |           |      |            |     |      |     |            |
|             |                    |                    |                           |                                      |                              |                |     | η ≡[ w    | ,         | δ ,  | δ , . . .  | δ   | , v  | −w  | , . . . v  |
C CA P M   e x p l a i n s  a b o u t   5 0 %   of  t h e  c r o s s - s e ct i o n a l   v ar i a t io n   in   m e a n   f u t u r e s   r e tu r n s ,  and  t+1  t  +1  1 ,t+1  2 ,t+1  K,t+1  1 ,t+1  t  +1  n,t+1
|                                                    |     |     |     |     |     |     | −w  | (cid:4) ∼I I D N( 0 , (cid:7)) .  |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| while the conditional version explains up to 60%.  |     |     |     |     |     |     |     | t  +1 ]                           |     |     |     |     |     |     |     |

688 M. Giampietro et al. / European Journal of Operational Research 265 (2018) 685–702
2.2. HMM factor SDF models r i,t+1 = μ i ( S t +1 ) −E [m t +1 ( S t +1 )| (cid:2) t , S t ] + v i,t+1
= μ i + m t +1 + v i,t+1 , i = 1 , . . . , n (12)
One of the explanations sometimes reported for the negative
correlation between commodities and other asset classes is the dif- where the vector of K factors follow a VAR (P) process and that
ferent behavior of stocks, bonds and commodities over the busi- can also be represented as:
(cid:13) (cid:14)
n
G
e
o
s
r
s
t on
cy
a
cl
n
e
d
(
R
s
o
e
u
e,
w
e
e
.
n
g
h
.,
or
Je
st
n s
(
e
2
n
0
,
0 6
M
)
e
fi
r
n
ce
d
r ,
t h
&
a t
J
c
o
o
h
m
ns
m
on
o
,
d i
2
ty
0 0
fu
2
t
)
u
.
r
I
e
n
s
d
p
ee
e
d
r-
,
1 0
(cid:4)
K
0
(cid:4)
n
form well in the early stages of a recession, a time when stock 0 K I K O K×n y t +1
returns generally disappoint; in later stages of recessions, com- 0 n O n ×K I n (cid:13) (cid:14)
m eq o u d it i i t e y s . r e T t h u i r s n s s u fa g l g l e o s f t f s , b th u a t t th a i s w is e ll g - e s n p e e r c a ifi ll e y d a m ve o r d y e l g o f o o d r t t i h m e e S f D o F r = μ( S t +1 ) + (cid:5)P−1 0 0 K
γ
¨ l
(cid:4)
, St +1(cid:3) In l d {l =0 } O 0 K
(cid:4)
n × n y t +1 −l + η t+1
ought to account for persistent, good and bad states. Moreover, l=0
−ι
n In d {l =0 } O n ×K O n ×n
BGR (2014) have noted that conditional pricing models that allow
(13)
for state dependence in the sensitivity of the stochastic discount
f
c
a
o
c
u
t
n
or
te
t
r
o
p a
t
r
h
t
e
s.
r
F
is
o
k
ll o
fa
w
c
i
t
n
o
g
r s
th
ca
e
n
ir
o
le
ft
a
e
d
n
,
o
su
u
p
tp
p
e
o
r
s
f
e
o r
t
m
he
t h
S
e
D
i
F
r u
h
n
a
c
s
o
i
n
n
d
st
it
e
i
a
o
d
n a
a
l w
. .
h
. −
ere
( 0 .
μ
5 σ
≡
m 2 (
[
γ
γ
S
0
t
,
+ 1 )
ϕ
+
1
0
, 0
.
,
5 σ
.
n 2
. .
+ σ
ϕ
n
K
,
,
m
0 ,
) ] (cid:4) ,
−
o
(
r
0 . 5 σ m 2 ( γ St +1 ) +0 . 5 σ 1 2 + σ 1 ,m ) ,
regime switching log-linear structure: (cid:13) (cid:14)
(cid:4) (cid:6) γ
0
M t +1 ( S t +1 ) = exp γ 0 , St +1 + (cid:5)
j=
K
1
γ j, St +1 f j,t+1 > 0 , (10) μ( S t +1 )
⎡
≡ −0 .
⎤
5 σ m 2 (cid:7) γ St +1 (cid:8) −
⎡
0 . 5 ϕ d 0 ia g 2: n +1 −(cid:7) (cid:7) γ St +1 (cid:8) e 1
⎤
w
f f l [ a a o γ t c
h
l 0 i l t ,
e
o o S o
r
t w n r +
e
s s 1 s h ,
f
d i
1
a p γ
,
r
t +
i 1 v J b ,
1
- S i e s
,
n t + t t g w a
f
1
2
t ,
,
e e
t
t
+
e h γ
1
n e M 2
,
, S t a w t
…
h + rk 1 e a
,
, o y p . v
f
.
K
r i . i n
, t
c c
+
γ h e
1
w s K a , i S h o n
a
t i
r
f + . c
e
1 a h T ] l (cid:4) h
a
l a r
g
e a e l
a
l s s
i
s s
n
t t a e r a s t i t c s s
K
e t e s - a t s
o
n s t p
b
d h e a
s
e c
e
r t i e h
r
w fi
v
e c
a
p i t p
b
r h v i
l
r c i
e
e i n c e
,
c - e d t r
s
o d e
y
r a g
s
r n i
t
i γ m s
e
d k S
m
t e + S f
a
1 a r t
t
+ e c ≡
i
1
c
- - γ ¨ l, St +1 ≡
⎢
⎢ ⎣ γ
γ
γ
K
1
2
,
, , . . .
S
S S
t
t t
+
+ +
1
1 1
⎥
⎥ ⎦ (cid:3) l ≡
⎢
⎢ ⎣ ϕ
ϕ
ϕ
l
l
l ,
,
, . . . K
1
2
,
, ,
1
1 1 ϕ
ϕ
ϕ
l
l
l ,
,
, . . . K
1
2
,
, ,
2
2 2
·
·
· .
·
·
· . .
·
·
· ϕ
ϕ
ϕ
l
l
l ,
,
, . . . K
1
2
,
, ,
K
K K
⎥
⎥ ⎦
tors to be homogeneous across assets according to the standard and η t+1 ≡[ w t +1 , δ 1 ,t+1 , δ 2 ,t+1 , . . . δ K,t+1 , v 1 ,t+1 −w t +1 , . . . v n,t+1
Euler condition in ( 1 ). By construction the same regime shifts af- −w t +1 ] (cid:4) ∼I I D N( 0 , (cid:7) St +1 ) . 4 For simplicity, we assume a time ho-
fect the mapping between all factors and the SDF and as such mogeneous Markov chain, although a literature shows that gener-
these are transmitted to all priced assets or portfolios. Because of alizations may be fruitful (see e.g., Dias et al., 2015 ). However, in
the MS structure in ( 9 ), the empirical fit of the model to the cross- our case, an element of time heterogeneity is already impressed
section of asset returns may be improved not only by carefully se- by the fact that the SDF depends on factors characterized by po-
lecting/expanding the K factors, but also the number of regimes tentially rich dynamics, while the HMM modeling truly affects not
(say, J ) or the features of the Markov chain driving the shifts in the directly the factors, but the loadings with which the factors appear
coefficients loading the factors on the SDF. in the SDF, in Eq. (10) .
Following steps analogous to those in Appendix A and condi-
tioning on both the state S t + 1 , and the past of observable returns 2.3. Maximum likelihood estimation strategy
and factors, if the random vector y t + 1 [ m t + 1 , f 1,t + 1 , f 2,t + 1 , … f K ,t + 1,
r 1,t + 1 , r 2,t + 1 , … r n ,t + 1 ] (cid:4) , with (cid:2) t ≡( { yt −s } s ≥0 , St ) ⊂(cid:3) t , has a condi- Our estimation strategy is based on the principle of maximum
tional multivariate Gaussian distribution then the conditional asset
likelihood under parametric assumptions concerning the joint nor-
pricing model,
mal distribution of random vector y t + 1 [ m t + 1 , f 1, t + 1 , f 2, t + 1 ,…f K , t + 1 ,
E [r i,t+1(cid:7) | (cid:2) t , S t ] (cid:8) r 1, t + 1 , r 2, t + 1 , … r n , t + 1 ] (cid:4) and, when appropriate, the Markov state
= (cid:9) − 0 . 5 σ m 2 ( S t +1 ) + (cid:10) 0 (cid:11) . 5 σ i 2 + σ i,m ( S t +1 ) (cid:12) −E [m t +1 ( S t +1 )| (cid:2) t , S t ] v th a e ri a in b v le e r S s t e . I o n f t t h h e e s ( i n n g + le K - s + ta 1 te ) , c × ov ( a n ri + an K c e + s 1 ta ) t i m on a a tr r i y x c A a 0 s e o , b b v e i c o a u u s s ly e
μ i ( St +1 ) exists (its determinant is 1), and the corresponding Jacobian is
= μ i ( S t +1 ) −E [m t +1 ( S t +1 )| (cid:2) t , S t ] i = 1 , . . . , n (11) u ti n o i n t e y
(cid:7)
, d t o h n e t l h o e g i o n f i t t ia h l e v j a
(cid:8)
o lu in e t s d o e f n t s h i e ty v a fu ri n a c b t l i e o s n ( y o
0
f ) t , h is e g s i a v m en p l b e y , 5 c ondi-
i
fl
s
e c
o
t
b
e
t
d
a in
in
e d
e
.
x
T
p
h
e
i
c
s
t e
i
d
s a
a s
m
se
o
t
d
r
e
e
l
tu
in
r n
w
s
h
b
i
o
ch
th
re
d
g
ir
im
ec
e
tl
s
y
in
th
t
r
h
o
e
u g
S
h
D F
th
a
e
r e
o n
r
e
e
-
- ln f y
1
, y
2
, . . . , y
T
;θ
(cid:4) (cid:6)
s a t s e s p e t- a s h p e e a ci d fi c f o t r e e r c m as s t μ E i [ ( m S t t + + 1 1 ( ) S ≡ t + − 1 ) 0 | (cid:2) . 5 t σ , m 2 S t ( ] S t + a 1 n ) d − i 0 n . d 5 i σ re i 2 c − tly σ , i, v m i ( a S t + th 1 e ) = − T 2 ln det ( (cid:7)) − 2 1 (cid:5)T A 0 y t +1 −μ− (cid:5)P−1 A l y t +1 −l (cid:4)
that also reflect state-dependent covariances between asset returns (cid:4) t=1 (cid:6) l=0
and the SDF. Also in this case, even though the forcing, observable (cid:5)P−1
state variables, f 1, t + 1 , f 2, t + 1 , …, f K , t + 1 , follow a linear process and ×(cid:7)−1 A 0 y t +1 −μ− A l y t +1 −l (14)
may enter linearly the model, the latter becomes non-linear be-
l=0
cause of the role played by the latent Markov state, St , that gov-
erns the switches in the parameters appearing in the process of (up to an omitted constant term), when the matrices are replaced
the factors. For instance, the full model may be written as: by the appropriate objects. Maximizing such a log joint density
(cid:5)K
function with respect to the components of θ≡[ γ ϕ
0
{ (cid:3)
l
} P
l=
−
0
1 (cid:9)] (cid:4)
m t +1 = γ 0 ,S + γ j,S f j,t+1 + w t +1 ( w t +1 ≡m t +1 −E [m t +1 | (cid:2) t , S t ] )
j=1 4 HMM dynamics in the covariance matrix of η t+1 derives from regimes in the
(cid:5)K (cid:5)P SDF loadings and therefore occurs residually. The assumption of normal shocks is
f j,t+1 = ϕ j, 0 + k =1 p=1 ϕ j,k,p f k,t+1 −p + δ j,t+1 , j = 1 , . . . , K t
th
yp 5
e
ic I
fi
n a
r
l
s
w
t
o h f
e l
a t
e
h t
m
e fo
e
l l
n
i l t o
t
e w r
o
a s
f
t u
b
η¨ r
o
t e +
t
,
h
1 s a e
v
n e
e c
d B
t o
a y¨
r
e t
s
+ 1 e
a
t
s
a a r
t
e l
h
.
e
( t 2 h
S
0 e
D
1 s 4
F
a ) m
i
.
s
e
b y
a s
c o
η
n
t+
s
1
t r
a
u
n
ct
d
i o
y
n
t +
u
1
n
b
o
u
b
t
s e
fa
rv
il
a b
to
le
i
.
nclude

M. Giampietro et al. / European Journal of Operational Research 265 (2018) 685–702  689
θ
will deliver the ML estimates of  . Note that the (conditional)  the perils of multiple, local maxima, as in Bae et al. (2014) , we use
residuals used by the MLE program,  randomly selected initial parameters and repeat the parameter es-
(cid:5)P−1   timation for each seed, where each new set of initial parameters
η ¨ ≡A¨  0 y¨  +1  −μ ¨ − A¨  l y¨  +1 −l  is drawn from the results of the previous estimation run, assuming
| t+1  |     | t   |     | t   |     |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a normal distribution with mean equal to the estimate and vari-
|     | (cid:2) | (cid:3) | l=0  | (cid:2) |     |     | (cid:3) |     |     |     |     |     |
| --- | ------- | ------- | ---- | ------- | --- | --- | ------- | --- | --- | --- | --- | --- |
ance equal to the square of the standard error obtained from the
|     | I    | O       |           |              |                 | ϕ                |              | previous run of the algorithm. 7  |     |     |     |     |
| --- | ---- | ------- | --------- | ------------ | --------------- | ---------------- | ------------ | --------------------------------- | --- | --- | --- | --- |
| =   | K    | K × n   | y¨  +1  − |              |                 | 0                |              |                                   |     |     |     |     |
|     | O    | I  n    | t         | −0 . 5  σ 2  | ( γ)  −0 . 5 di | a  g  ( (cid:7)) |  −(cid:7) e  |                                   |     |     |     |     |
|     | n  × | K       |           | m            |                 | 2: n +1          | 1            |                                   |     |     |     |     |
|     |      | (cid:2) | (cid:3)   |              |                 |                  |              |                                   |     |     |     |     |
(cid:5)P −
|     | 1   | (cid:3) | O       |            |     |     |       | 3. T h e   d | a t a   |     |     |     |
| --- | --- | ------- | ------- | ---------- | --- | --- | ----- | ------------ | ------- | --- | --- | --- |
|     | −   | l       | K × n   | y¨  +1 −l  |     |     | (15)  |              |         |     |     |     |
|     |     | O       | O  n ×  | t          |     |     |       |              |         |     |     |     |
|     |     | n × K   | n       |            |     |     |       |              |         |     |     |     |
l= 0   W e   u s e   a  cross-section of eight portfolios of stocks, Treasuries,
imply the impossibility to concentrate the parameters of the log-  corporate bonds and commodity indices as test assets throughout.
likelihood function to separate the estimable elements of (cid:9) from  In particular, we consider the monthly excess returns of these port-
those appearing in the conditional residuals  η t+1 .  folios over the one-month Treasury bill rate from January 1989 to
December 2011.
In the case of the HMM extension introduced in Section 2.2 , be-
The stock portfolio is proxied by the CRSP value-weighted index
| cause the inverse of the matrix A  |     |     |     | 0 still exists, and the correspond-  |     |     |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
(VW CRSP), which includes all the firms incorporated in the U.S.
ing Jacobian is unity, the log of the joint density function of the
and listed on the NYSE, AMEX, or NASDAQ, obtained from Fama
sample, conditioned on the initial values of the variables,
|     | (cid:7) |     |     |     | (cid:8) |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
;θ and French’s data library. Treasuries are proxied by the 10-year
| ln f y  | 1  , y  | 2  , . . . , y  | T  , S  0  , S  | 1  , . . . , S  T  |     |     |     |     |     |     |     |     |
| ------- | ------- | --------------- | --------------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
constant maturity Treasury yields, that is, yields on actively traded
|     |     | (cid:7) | (cid:7) | (cid:8)(cid:8) |     |     |     |     |     |     |     |     |
| --- | --- | ------- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
T   (cid:7) γ n o n - in fl a t io n   i n d e x e d   is s u e s   a d j u s t e d   to   c o n s t an t   m a t u ri ti e s ,   r e -
|     | = − | ln  det  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2   St +1 tr ie v e d  f r o m   t h e   F e d e ra l  R e s e r v e   o f   S t.  L o u is   F R E D   d at a   re p o s i t o r y .
|     |     | (cid:4)   |     |     |     | (cid:6)  (cid:4)  |     |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
(cid:7) (cid:8) T h e  t w o   c o r p o r a t e   b o n d   p o r t f o l i o s   a r e   p r o x i e d   b y   t h e   M o o d y ’ s   s e a -
|     | 1  (cid:5)T   |     |     | (cid:5)P−1   |     |     |     |     |     |     |     |     |
| --- | ------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
− −μ γ − s o n e d   A a a   c o r p o r a t e  b o n d  p o r t f o l i o   a n d   t h e   M o o d y ’s   s e a s o n e d   B a a
|     |     | A  0 y t  +1  |     | St     | A  l y t  +1 −l  |     |     |     |     |     |     |     |
| --- | --- | ------------- | --- | ------ | ---------------- | --- | --- | --- | --- | --- | --- | --- |
2   +1 c o r p o r a t e   p a p e r   p o r t f o l i o ,   r e s p e c t i v e l y ,   o b t a i n e d   f r o m   t h e   F e d e r a l
|     | t=1  | (cid:4) |     | l=0  |     | (cid:6) |     |     |     |     |     |     |
| --- | ---- | ------- | --- | ---- | --- | ------- | --- | --- | --- | --- | --- | --- |
    Reserve of St. Louis FRED data repository. In order to transform
|     | (cid:7) | (cid:8) |     | (cid:7) (cid:8) | (cid:5)P−1   |     |     |     |     |     |     |     |
| --- | ------- | ------- | --- | --------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
−1  y i e ld s   i n to   r e t u r n s   w e   u se   S h il le r’ s   ( 1 97 9 )   a p p r o x im at i o n ,   w h i ch
|     | ×(cid:7) γ |     |     | −μ γ | −   | ,   |     |     |     |     |     |     |
| --- | ---------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
St     A  0 y t  +1  St     A  l y t  +1 −l  (16)  d e fi n e s   th e   h o l d i n g   pe r io d  y i e ld   in   t e r m s  o f   y ie l d   to  m a t u r i t y.  T h e
|     |     | +1  |     | +1  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
l=0  one-month Treasury Bill return series is obtained from the Ibbot-
(up to an omitted constant term) is the same as the log-  son SBBI Classic Yearbook.
η
likelihood function for  t+1 . It turns out that maximizing such a  Similarly to research by Bae et al. (2014) , the four commod-
θ≡
log joint density function with respect to the components of  ity indices included among the test assets are all Standard &
| { γ | }   | ϕ {  (cid:3) } | −  , {  (cid:7) | ( γ ) }   (cid:4) |     |     |     |     |     |     |     |     |
| --- | --- | -------------- | --------------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[    s   J ,       ,   l   P 1     s     J ]  w i ll   d e l i v e r   t h e   M L   e s t im a t e s  P o o r ’s -G ol d m a n   S a c h s   ( S & P G S )   S p o t  C o m m o d it y   In d i c e s ,  n a m e l y
|     | θ s  = 1   | 0   | l = 0   | s  = 1  |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
o f   .  B e c a u s e   t he   s t a t e s   ar e   l a t e n t ,  a n   a p p l i c a t i o n   o f  t h e   it e ra t iv e   th e   S & PG S   Ag r i cu l t u r e   a n d   Li v e s t o ck ,  t h e  S& P G S   P re c i o u s   M e ta l s ,
Expectation-Maximization (EM) algorithm in which the maximiza-  the S&PGS Industrial Metals, and the S&PGS Energy indices. The
tion is applied to  S&PGS Spot Commodity Indices are built using front-end futures to
exploit the proximity of traded future prices to spot prices. How-
(cid:5)T  (cid:5)J
1    | (cid:2) (cid:7)( γ e v e r ,  w e   a r e   a w a r e  t h a t   a n   i n d e x   o f  c o m m o d i t y   sp o t   p r ic e s   si m p l y
| −   |     | Pr (  S t   = s  |   T  ) |  ln det (   |   s  )   )  +  |     |     |     |     |     |     |     |
| --- | --- | ---------------- | ------ | ----------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
2   tr a c k s  t h e   e v o l u ti o n   of   t h e   s p o t   p r ic e s ,  an d  i g n o r e s  a l l  c o s ts   a s so c i -
t=1 s =1
(cid:4) (cid:6) ated with the holding of physical commodities (storage, insurance,
|     |                     |     |     |     |     |              |  (cid:4)  |     |     |     |     |     |
| --- | ------------------- | --- | --- | --- | --- | ------------ | --------- | --- | --- | --- | --- | --- |
|     | (cid:5)T  (cid:5)J  |     |     |     |     | (cid:5)P−1   |           |     |     |     |     |     |
1  Pr ( | (cid:2) ) −μ( γ ) e tc .) .  I t   is   th er e fo r e   a n   u p p e r   b o u n d   o n  t h e   r e tu r n  t h a t an investor
| −   |     |  S t   | =: s    | T    A  0 y  +1  |     | s   − A  l y  +1 −l  |     |     |     |     |     |     |
| --- | --- | ------ | ------- | ---------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
2   t t in  s p o t   c o m m o d it i e s   w o u l d   h a v e   ea r n e d   in   r e a l  t im e .
|     | t=1 s =1  |     |     |     |     | (cid:6)l=0  |     |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
(cid:4) The macro-based pricing factors are built following an approach
|     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:7) (cid:8) (cid:5)P−1   s i m il a r   t o   L u d v i n g s o n   a n d   N g   (2 0 0 9 )  .  W e  s ta r t   fr o m   t h e ir   r i c h
| ×(cid:7) | γ   | −1  | −μ( | γ )  − |     | ,   |     |     |     |     |     |     |
| -------- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
    A  0 y  +1    s  A  l y  +1 −l  (17)  d a ta b a s e ,   c o n ta i n i n g   1 3 2  U . S .  m a cr o e c o n om ic   v a r ia b l es   m e a s u r e d
|     | St  | +1  | t   |     | t   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
l=0  at monthly frequency (see Appendix B). We remove all financial
|        |                  |            |                                                        |     |     |     |     | r e t u r n   s er | i es   a n d   a d d   | th r e e  t o p i c a l   se | r i es :   th e   G o ld | m a n   S a c h s   F i -   |
| ------ | ---------------- | ---------- | ------------------------------------------------------ | --- | --- | --- | --- | ------------------ | ---------------------- | ---------------------------- | ------------------------ | --------------------------- |
| where  | {  Pr ( St  = s  | |  (cid:2) | )}    T   1 ( s = 1, 2, …, J ) are the smoothed prob-  |     |     |     |     |                    |                        |                              |                          |                             |
T  t = n a n c i a l  C o n d i ti o n s   In d e x   (G S - F C I ) ,  t h e   H is t o ri c a l  N e ws - B a s e d   P o l -
abilities derived with the classical, Hamilton-Kim smoothing algo-
icy Index (see Baker, Bloom, & Davis, 2012 ) and the Liquidity Fac-
| rithm ( Hamilton, 1994 ). Maximizing such a smoothed probab   |     |     |     |     |     |     | ility-  |                                         |     |     |                          |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --------------------------------------- | --- | --- | ------------------------ | --- |
|                                                               |     |     |     |     |     |     |         | tor of Pastor and Stambaugh (2003) . 8  |     |     | We end up with a set of  |     |
| weighted log joint density function delivers ML estimates of  |     |     |     |     |     |     | θ .     |                                         |     |     |                          |     |
The assumption of normality of returns and finite number of
states allows us to employ the Baum–Welch algorithm to estimate  ponentially with the number of observations, which makes this algorithm imprac-
θ
. The Baum–Welch algorithm is an expectation–maximization  tical. Indeed, for HMM, the special variant of the EM algorithm referred to as the
forward–backward or Baum–Welch algorithm is needed because the model contains
(EM) algorithm typically applied to HMM. Given an initial set of
θ {  yt  ,} a  v e ry   l a rg e   n u m b e r   o f  e n tr ie s   in   th e  j o in t   p o s t e r ior   l a t e n t  d i s t ri b u ti o n   ge n e r a t e d
| parameters  |     | 0 and the realized series of observations,  |     |     |     |     |   , the re-  |                      |                                  |                              |                              |                                     |
| ----------- | --- | ------------------------------------------- | --- | --- | --- | --- | ------------ | -------------------- | -------------------------------- | ---------------------------- | ---------------------------- | ----------------------------------- |
|             |     |                                             |     |     |     |     |              | b y   th e   T  +  1 |   l at e nt   v a r ia b l es .  | B a u m – W e l ch   a l g o | r it h m   c i r c u m v e n | t s   th e   c o m p u t a t io n   |
sult of this algorithm always converges to a local maximum of the  of this joint posterior distribution making use of the conditional independencies
likelihood function. In the E-step, we compute the expected value  implied by the model, see Dias et al. (2015) for a discussion.
of the T + 1 latent Markov states (one at each point in the sample)  7  Random draws of the starting parameter values that violated basic admissibility
given the observed data and the current, provisional estimates of  conditions (e.g., combinations of elements in the { A  l } matrices that made the VAR
system non-stationary) were rejected.
the parameters. In the M-step, standard ML methods are used to
|     |     |     |     |     |     |     |     | 8  The GS Financial Stability Index is a weighted average of US real short-term  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------------------------------- | --- | --- | --- | --- |
update the unknown parameter estimates using an expanded data
interest rates, real long-term corporate bond yields, the real trade-weighted dollar
matrix with previous expectations as weights. 6
To protect against  index, and the ratio of equity market capitalization to nominal GDP (see Dudley
and Hatzius, 20 0 0 ). An increase in the GS-FCI indicates tightening of financial con-
ditions, while a decrease indicates easing. The Historical News-Based Policy Index
6
Because the EM algorithm needs to store the JT entries of expectations over  measures economic policy uncertainty in the U.S. by counting the number of arti-
the latent space for each data pattern, computation time and storage increases ex-  cles published every month that contains the words “uncertain”or “uncertainty”in

690 M. Giampietro et al. / European Journal of Operational Research 265 (2018) 685–702
Table 1
Summary statistics (January 1989–December 2011).
The following tables refer to all the series used in the parts of the paper based on the sample January 31, 1989–December 30, 2011. Panel A shows mean, median, standard
deviation, skewness, excess kurtosis, and the p -value of the Jarque–Bera (JB) test. The JB statistic is used to test the hypothesis of normality of the series, hence a p -value
lower than α% implies the rejection of the null hypothesis at α% confidence level. Panel B shows the correlations among the series.
Panel A
Mean Median Std. dev. Skewness Excess Kurtosis JB p -value
Factor 1 0.0 0 0 0 0.0080 0.4385 −1.6940 4.8482 0.0 0 0 0
Factor 2 0.0 0 0 0 0.0014 0.3080 −0.7455 4.2518 0.0 0 0 0
Factor 3 0.0 0 0 0 −0.0 0 01 0.2568 0.6517 2.5557 0.0 0 0 0
HP Factor 0.0036 0.0049 0.0442 −0.1246 1.0115 0.0019
Basis Factor 0.0098 0.0109 0.0448 −0.0093 1.3934 0.0 0 0 0
Momentum Factor 0.0088 0.0091 0.0503 0.3528 3.3293 0.0 0 0 0
Agriculture and livestock −0.0 0 02 0.0 0 03 0.0428 −0.0876 1.5607 0.0 0 0 0
Precious metals 0.0030 −0.0024 0.0469 0.0980 1.2784 0.0 0 01
Industrial metals 0.0 0 08 −0.0 0 07 0.0606 −0.1039 1.4521 0.0 0 0 0
Energy 0.0071 0.0086 0.0904 0.3851 1.5595 0.0 0 0 0
10Y treasury bonds 0.0023 0.0020 0.0019 0.0016 −0.7515 0.0389
Aaa corporate bonds 0.0033 0.0031 0.0019 −0.0 0 05 −0.7615 0.0356
Baa corporate bonds 0.0042 0.0039 0.0019 0.0104 −0.7375 0.0437
Value-weighted equity CRSP 0.0054 0.0110 0.0447 −0.6165 1.0217 0.0 0 0 0
Panel B
Factor 1 Factor 2 Factor 3 AL PM IN EN Treasuries Aaa bonds Baa bonds VW CRSP
Factor 1 1.00 0.00 0.00 0.08 −0.05 0.19 0.10 −0.08 −0.08 −0.07 0.09
Factor 2 1.00 0.00 0.08 0.24 0.16 0.27 0.03 0.04 0.06 0.04
Factor 3 1.00 0.00 −0.09 0.14 −0.04 0.12 0.13 0.15 0.10
Agriculture and livestock 1.00 0.29 0.31 0.16 0.12 0.12 0.13 0.22
Precious metals 1.00 0.26 0.21 0.21 0.21 0.21 0.03
Industrial metals 1.00 0.29 0.09 0.10 0.12 0.38
Energy 1.00 −0.01 0.00 0.01 0.09
10Y treasury bonds 1.00 1.00 1.00 −0.02
Aaa corporate bonds 1.00 1.00 −0.01
Baa corporate bonds 1.00 0.00
Value-weighted equity CRSP 1.00
112 variables and we use principal component analysis to sum- from normality, as discussed in Buckley, Saunders, and Seco (2008)
marize their covariance structure. We extract three, five or ten or- and Dias et al. (2015) . Interestingly, commodities show high return
thogonal factors that summarize 31.4%, 36%, and 52.9% of the vari- volatility not always associated to a high mean return: in fact, the
ance, respectively. To gain insight on the economic meaning of the Agriculture and livestock class displays a negative mean return de-
factors we investigate the sign of the factor loadings and the R - spite a standard deviation close to that of stocks.
squares from univariate regressions of each of the factors on the Table 1 also shows the correlations among the series. Inter-
macroeconomic variables (see Appendix C). estingly, F2 is the pricing factor showing the highest correlations
The first principal component (F1) is a business cycle, pro- with the commodity series, implying that inflation tends to simul-
cyclical factor, the value of which increases with industrial produc- taneously correlate with all the commodity returns. This finding
tion, “help wanted”, and employment growth, and decreases with is consistent with a literature that considers commodities as infla-
changes in the unemployment rate. The second principal compo- tion hedges (see, e.g., Erb & Harvey, 2006 ). The correlations among
nent (F2) can be defined as an inflation factor that positively loads the test assets and the remaining pricing factors are generally low,
with relatively high R -squares on most types of price indices (in- except for Industrial Metals that significantly correlates with Pre-
cluding consumers’, producers’, and personal consumption expen- cious Metals and Agriculture and Livestock. However, the range of
diture deflators). The third principal component (F3) can be de- correlations between pairs of commodities indices is wide, from
fined as an inventory and new orders factor. 0.16 between agricultural and energy commodities to 0.31 between
Table 1 shows summary statistics. The three macro factors are agricultural and industrial commodities.
characterized by a mean equal to zero and by considerable volatil-
ity. This finding is explained by the fact that all factors are char-
4. Empirical results
acterized by large and positive excess kurtosis and non-zero (and
highly statistically significant, based on unreported tests) skew-
4.1. Statistical model selection criteria
ness. The evidence of non-normality (non-zero skewness and ex-
cess kurtosis) extends to all the portfolios considered, consistently
In Table 2 , we conduct a formal specification search by com-
with the fact that for all the series is possible to reject the null of
paring the values of three different information criteria—Akaike
normality in a Jarque–Bera (JB) test. However, bonds are character-
(AIC), Bayes–Schwarz (BIC), and Hannan–Quinn (HQIC)—to select
ized by negative excess kurtosis and essentially symmetric empir-
the model that most likely represents the unknown data generat-
ical distributions, and the rejection of the null of normality tends
ing process. The table is organized around four panels. In the first
to be relatively weak, with p -values between one and five percent.
panel, we present single-state models with three and five pricing
Of course, the HMM methods developed in Section 2 can be con-
factors and different VAR structures. In particular, with reference
sidered as ways to capture and forecast such pervasive departures to the (cid:3)
1
matrix shown in Eq. (9) , we present model specifications
that consist of a full VAR(1) where (cid:3)
1
is a full matrix (each fac-
association with terms related to the economic cycle. Finally, Pastor–Stambaugh’s
tor depends on its own lags, and on past values of both the other
Liquidity Factor is a cross-sectional average of individual stock liquidity measures. factors and of the test assets); a block factor VAR(1), where each

M.
Giampietro
et
al.
/
European
Journal
of
Operational
Research
265
(2018)
685–702
691
Table 2
Model selection.
In the table, SIC is the Bayes–Schwarz information criterion, AIC is the Akaike information criterion, and HQIC is the Hannan–Quinn information criterion. The Chi-squared test is a joint test applied to the Euler conditions ( Eq.
(2) in the text) of the null that they are simultaneously satisfied. We have boldfaced the best fitting model according to each of the information criteria and all models not rejected by the Chi-squared pricing test. HJ represents
the Hansen–Jagannathan distance under the null of correct specification of the SDF. All models are specified with a VAR order of 1.
Max Log- Avg. Log- No. Obs. No. Saturation BIC AIC HQIC Pricing Chi-squared p -value HJ
Likelihood Likelihood parameters ratio RMSE test distance
SINGLE STATE 3 factors, single state, full VAR model 8056.37 2.66 3025 40 75.63 −5.22 −5.30 −5.27 0.0096 149.14 0.0 0 0 6.832
3 factors, single state, block Factor VAR 7964.23 2.63 3025 16 189.06 −5.22 −5.26 −5.24 0.0091 11,913 0.0 0 0 6.687
3 factors, single state, diagonal Factor VAR 7828.44 2.59 3025 10 302.50 −5.15 −5.17 −5.16 0.0092 9392.8 0.0 0 0 6.687
5 factors, single state, full VAR model 7537.22 2.11 3575 76 47.04 −4.04 −4.17 −4.13 0.0090 215.92 0.0 0 0 6.645
5 factors, single state, block Factor VAR 7432.32 2.08 3575 36 99.31 −4.08 −4.14 −4.12 0.0092 10,932 0.0 0 0 6.691
5 factors, single state, diagonal Factor VAR 7187.82 2.01 3575 16 223.44 −3.98 −4.01 −4.00 0.0092 8801.2 0.0 0 0 6.687
2 STATES 3 factors, 2 states, full VAR model 8228.45 2.72 3025 82 36.89 −5.22 −5.39 −5.33 0.0054 7.72 0.461 5.791
3 factors, 2 states, block Factor VAR 8218.11 2.72 3025 34 88.97 −5.34 −5.41 −5.39 0.0093 1937.4 0.0 0 0 6.718
3 factors, 2 states, diagonal Factor VAR 8080.99 2.67 3025 22 137.50 −5.28 −5.33 −5.31 0.0093 2080.0 0.0 0 0 6.726
5 factors, 2 states, full VAR model 7866.04 2.20 3575 154 23.21 −4.05 −4.31 −4.22 0.0132 6.87 0.551 7.697
5 factors, 2 states, block Factor VAR 7720.26 2.16 3575 74 48.31 −4.15 −4.28 −4.23 0.0092 2111.9 0.0 0 0 6.699
5 factors, 2 states, diagonal Factor VAR 7513.10 2.10 3575 34 105.15 −4.13 −4.18 −4.16 0.0091 2454.9 0.0 0 0 6.670
3 STATES 3 factors, 3 states, full VAR model 8344.14 2.76 3025 126 24.01 −5.18 −5.43 −5.34 0.0075 4.03 0.854 6.0 0 0
3 factors, 3 states, block Factor VAR 8301.35 2.74 3025 54 56.02 −5.35 −5.45 −5.41 0.0086 2663.5 0.0 0 0 6.778
10 factors, 3 states, block Factor VAR 6987.68 1.41 4950 133 37.22 −2.59 −2.77 −2.71 0.0094 1474.6 0.0 0 0 NA
3 factors, 3 states, diagonal Factor VAR 8182.93 2.71 3025 36 84.03 −5.31 −5.39 −5.36 0.0092 2857.3 0.0 0 0 6.712
5 factors, 3 states, full VAR model 7978.98 2.23 3575 234 15.28 −3.93 −4.33 −4.19 0.0092 4.50 0.809 6.135
5 factors, 3 states, block Factor VAR 7821.17 2.19 3575 114 31.36 −4.11 −4.31 −4.24 0.0093 1918.9 0.0 0 0 6.784
5 factors, 3 states, diagonal Factor VAR 7609.88 2.13 3575 54 66.20 −4.13 −4.23 −4.19 0.0095 5871.4 0.0 0 0 6.794
4 STATES 3 factors, 4 states, full VAR model 8006.54 2.65 3025 172 17.59 −4.84 −5.18 −5.06 0.0179 14.35 0.073 9.742
3 factors, 4 states, block Factor VAR 8376.91 2.77 3025 76 39.80 −5.34 −5.49 −5.43 0.0102 3085.2 0.0 0 0 6.849
3 factors, 4 states, diagonal Factor VAR 7932.80 2.62 3025 52 58.17 −5.11 −5.21 −5.17 0.0099 3231.6 0.0 0 0 6.926
5 factors, 4 states, full VAR model 7682.41 2.15 3575 268 13.34 −3.68 −4.15 −3.98 0.0110 7.52 0.482 7.076
5 factors, 4 states, block Factor VAR 7593.78 2.12 3575 108 33.10 −4.00 −4.19 −4.12 0.0090 1409.6 0.0 0 0 6.636
5 factors, 4 states, diagonal Factor VAR 7433.85 2.08 3575 68 52.57 −4.00 −4.12 −4.08 0.0099 24 4 4.9 0.0 0 0 6.930

692 M. Giampietro et al. / European Journal of Operational Research 265 (2018) 685–702
factor depends on its own lags and on past values of the pricing Fig. 1 . Regime 1 is characterized by high variances and a low im-
factors; and lastly, a diagonal factor VAR(1) where each factor de- plied duration (on average 3 months). Fig. 1 shows some spikes in
pends only on its own past values, which is equivalent to stacking the smoothed probabilities of this state in correspondence to the
K different AR(1) processes (that may be cross-serially correlated). first half of the 1990s (when a short recession took place) and at
In the remaining three panels we entertain non-linear, three- the beginning of the new millennium, characterized by the burst
and five-factor HMM VAR(1) (i.e., MSVAR) models with two, three, of the dot-com bubble. Therefore, we interpret Regime 1 as a “pre-
and four regimes. Also in this case, we present three compet- financialization crisis regime”, referring to the fact that most of
ing structures of the (cid:3)
1
matrix (as defined in Eq. (13) ): full its occurrences tend to precede the process of “financialization” of
MSVAR, block factor MSVAR, and diagonal factor MSVAR. In ad- commodities, i.e., the change in their relationships with traditional
dition, we also display the information criteria for a HMM model assets classes that has (allegedly) occurred over the last decade
with ten factors to assess whether including a higher number of (see, e.g., Büyüksahin & Robe, 2014; Tang & Xiong, 2012 ). Regime 2
macro-related components (which are indeed able to explain more is instead a tranquil regime, characterized by a lower variance and
than 50% of the total variability of the series in the face of 31.4% a longer implied duration (approximately 10 months) vs. regime
and 36% of the three- and five-component sets) enhance the ac- 1, consistently with the bulk of the empirical asset pricing liter-
curacy of the model. However, because a ten-factor HMM requires ature (see e.g., Dias et al., 2015 , and references therein), that de-
the estimation of a huge number of parameters, we limit this ex- scribes the “good”, state as highly persistent. Because regime 2
ercise to a three-state block MSVAR model, where “only” 133 pa- seems to characterize most of the time before 20 0 0, we define it as
rameters need to be estimated. 9 the “pre-financialization bull regime”. Interestingly, regimes 3 and
The rationale behind information criteria is to provide a mea- 4 are similar to regimes 2 and 1, respectively, but almost exclu-
sure of statistical accuracy that strikes a balance between good- sively occur after the new millenium. Regime 3 is less volatile and
ness of fit and parsimonious specifications of the model. 10 The more persistent, with average duration of 5 months, than regime 2,
most parsimonious BIC selects a three-state, three-factor block while regime 4 is a deeply turbulent state that tends to character-
MSVAR(1) model, which requires the estimation of only 54 param- ize the period of 2008-2010, i.e., the recent financial crisis. Accord-
eters and has a saturation ratio (number of observations per pa- ingly, we interpret these two states as the “post-financialization
rameter) of 56. However, both the AIC and the BIC point towards a bull regime” and the “post-financialization crisis regime”, respec-
more richly parameterized four-state three-factor block MSVAR(1) tively.
model. Although this model requires the estimation of 76 param- In Table 3 , the estimated SDF loads negatively on the business
eters (i.e., 22 parameters more than its three-state counterpart se- cycle factor during the crises regimes 1 and 4. On the opposite, the
lected by BIC), it has a saturation ratio of approximately 40, which SDF load coefficient is low but positive in regime 2 and not pre-
is still considered acceptable in the literature. cisely estimated in regime 3. This has some intuitive sense: if we
Interestingly, all the criteria select HMM models, in which good interpret it as a reflection of the marginal utility of future wealth
and bad states are reflected in the dynamics of a non-linear SDF, (e.g., m t + 1 = U (cid:4) (W t + 1 )/U (cid:4) (W t ) where U( •) is a utility function), the
over single-state models. In a statistical perspective, the only un- SDF tends to be relatively low during economic booms and thus,
certainty concerns whether three or four regimes should be spec- in general, a positive shock to the business cycle in good times
ified. Furthermore, additional factors do not seem to improve the should decrease the SDF. However, the impact of a positive shock
statistical accuracy of the model. In particular, the ten-factor model in the business cycle is much more pronounced during recession
does not provide any improvement of the fit to the data. periods than in an already booming economy, when it can even be
To provide an idea of the resulting estimates, Table 3 shows the interpreted as a sign of overproduction and lead to an anticipation
empirical results for the four-states, three-factor block MSVAR(1) of a bubble burst. Not surprisingly, the single-state benchmark pre-
model. As a benchmark, Appendix D presents the estimates for the sented in Appendix D, that cannot empirically separate across dif-
single-state counterparty of this model. For the sake of brevity, we ferent states, shows a precisely estimated but small, negative load-
do not report the estimates of the three-state, three factor block ing on the business cycle factor that intuitively “averages” across
MSVAR(1) model that is selected by the BIC, but these are available the regime-specific values in Table 3 .
upon request from the authors. In particular, Table 3 shows the Finally, we observe that the intercept of the SDF is negative
AR(1) coefficients and the intercept for each of the factors in the across all regimes, and this represents no problem given that ( 10 )
VAR(1) that describes their dynamics, the loadings of the SDF on expresses the SDF in log-exponential form. However, the magni-
γ
the factors and its intercept
0
in any of the four regimes, and the tude (in absolute terms) of this coefficient seems to have struc-
residual covariance matrix of the factors and test assets. Interest- turally increased after the “financialization” of the commodities
ingly, in such model the majority of the coefficients is statistically kicked in, from −0.0014 and −0.0029 in regimes 1 and 2, to
significant at all standard levels of confidence. More precisely, the −0.0 099 and −0.0 074 in regimes 3 and 4, respectively. This sug-
SDF strongly depends on the three factors and the corresponding gests that, net of other systematic influences, state prices may
loadings in all regimes are precisely estimated with small, practi- have decreased as a result of the financialization process and this
cally zero p -values, except for the loading on the first factor (that may reflect structural, systemic contagion risks across different as-
we have interpreted as a business cycle proxy in Section 3 ), but set markets. Not surprisingly, the SDF intercept of the single-state
only in the third regime. benchmark model is negative and equal to −0.0043, which is close
The four regimes can be interpreted looking at their estimated to an average of the values observed in each of the four regimes in
(residual) variances and at the smoothed probabilities presented in Table 3 . This clearly shows the limitations of a single-state model.
4.2. Pricing performance
9 We have also estimated VAR and MSVAR models with more than one autore-
gressive lag but, due to the high number of parameters to be estimated, these mod- In this section, we compare the pricing performance of the
els are never competitive with their one-lag counterparties. Therefore, also to save competing SDFs presented in Table 2 . Indeed, along with the infor-
space, we refrain from including them in Table 2 . mation criteria, Table 2 reports the Root Mean Square Error (RMSE)
10 All the information criteria are based on a formula built on −2 times the aver-
age log likelihood function adjusted by a penalty function, ϕ(T ) , multiplied by the in pricing, which measures the in-sample difference between the
number of estimated parameters. In the AIC ϕ(T ) = 2 , while in the BIC ϕ(T ) = lnT ; returns predicted by the model and the observed ones. More pre-
finally, in the HQIC ϕ(T ) = 2 ln ( lnT ) . cisely, given the asset pricing model in ( 5 ), the RMSE is computed

M.
Giampietro
et
al.
/
European
Journal
of
Operational
Research
265
(2018)
685–702
693
Table 3
Model estimates- three-factor block VAR(1), four regimes.
Regime 1 Regime 2
Coefficient Std. error t -Statistic p -value Coefficient Std. error t -Statistic p -value
Factor VAR coefficients, SDF loadings and estimated transition matrix
[F1/F1] Coeff. 0.4220 0.028 15.327 0.0 0 0 Transition matrix 0.3501 0.044 7.911 0.0 0 0
[F1/F2] Coeff. −0.0662 0.027 −2.437 0.015 0.6972 0.0544 0.0709 0.0840 0.0757 0.087 0.869 0.385
[F1/F3] Coeff. −0.2126 0.035 −5.994 0.0 0 0 0.1715 0.8983 0.0 0 0 0 0.0 0 0 0 −0.5066 0.055 −9.258 0.0 0 0
F1: Intercept −1.2489 0.136 −9.186 0.0 0 0 0.1312 0.0238 0.8002 0.2880 1.3299 0.157 8.455 0.0 0 0
[F2/F1] Coeff. 0.0049 0.035 0.139 0.889 0.0 0 02 0.0235 0.1288 0.6280 −0.0747 0.021 −3.485 0.0 0 0
[F2/F2] Coeff. −0.5612 0.039 −14.431 0.0 0 0 Implied durations −0.1975 0.043 −4.632 0.0 0 0
[F2/F3] Coeff. 0.0369 0.049 0.753 0.451 Regime 1: 3.30 −0.0484 0.027 −1.814 0.070
F2: Intercept −0.4996 0.127 −3.946 0.0 0 0 Regime 2: 9.84 0.2989 0.073 4.083 0.0 0 0
[F3/F1] Coeff. −0.3382 0.023 −14.483 0.0 0 0 Regime 3: 5.01 −0.2523 0.027 −9.518 0.0 0 0
[F3/F2] Coeff. −0.1055 0.024 −4.319 0.0 0 0 Regime 4: 2.69 −0.0360 0.049 −0.727 0.467
[F3/F3] Coeff. 0.3997 0.031 12.778 0.0 0 0 Ergodic probs.: 0.0620 0.032 1.962 0.050
F3: Intercept −0.5977 0.101 −5.894 0.0 0 0 Regime 1: 0.182 0.4463 0.110 4.044 0.0 0 0
SDF: Loading on F1 −0.0014 0.0 0 01 −26.265 0.0 0 0 Regime 2: 0.306 0.0 0 02 0.0 0 0 0 4.752 0.0 0 0
SDF: Loading on F2 0.0 0 06 0.0 0 01 11.099 0.0 0 0 Regime 3: 0.366 −0.0016 0.0 0 01 −17.691 0.0 0 0
SDF: Loading on F3 −0.0015 0.0 0 01 −20.178 0.0 0 0 Regime 4: 0.146 0.0014 0.0 0 01 21.009 0.0 0 0
SDF: Intercept −0.0014 0.0 0 03 −4.774 0.0 0 0 −0.0029 0.0 0 02 −12.226 0.0 0 0
Regime 3 Regime 4
Coefficient Std. error t -Statistic p -value Coefficient Std. error t -Statistic p -value
Factor VAR coefficients and SDF loadings
[F1/F1] Coeff. 0.6864 0.041 16.816 0.0 0 0 0.8857 0.022 39.424 0.0 0 0
[F1/F2] Coeff. −0.0561 0.051 −1.102 0.271 0.2592 0.027 9.597 0.0 0 0
[F1/F3] Coeff. −0.2928 0.051 −5.768 0.0 0 0 −0.1153 0.044 −2.614 0.009
F1: Intercept 0.4702 0.128 3.673 0.0 0 0 −0.5730 0.191 −3.008 0.003
[F2/F1] Coeff. −0.1189 0.026 −4.566 0.0 0 0 −0.1162 0.040 −2.887 0.004
[F2/F2] Coeff. −0.0373 0.024 −1.533 0.125 −0.1366 0.041 −3.365 0.001
[F2/F3] Coeff. −0.0132 0.025 −0.539 0.590 0.0192 0.066 0.291 0.771
F2: Intercept 0.3016 0.124 2.437 0.015 −1.1753 0.358 −3.279 0.001
[F3/F1] Coeff. −0.4456 0.033 −13.590 0.0 0 0 −0.2054 0.022 −9.202 0.0 0 0
[F3/F2] Coeff. 0.0056 0.040 0.139 0.889 0.1718 0.026 6.607 0.0 0 0
[F3/F3] Coeff. −0.0525 0.040 −1.312 0.190 0.3054 0.042 7.195 0.0 0 0
F3: Intercept 0.4066 0.109 3.741 0.0 0 0 −0.9587 0.191 −5.013 0.0 0 0
SDF: Loading on F1 −0.0 0 01 0.0 0 01 −0.842 0.400 −0.0011 0.0 0 01 −10.943 0.0 0 0
SDF: Loading on F2 −0.0027 0.0 0 01 −42.013 0.0 0 0 −0.0024 0.0 0 01 −41.559 0.0 0 0
SDF: Loading on F3 0.0010 0.0 0 01 13.303 0.0 0 0 −0.0025 0.0 0 01 −21.225 0.0 0 0
SDF: Intercept −0.0099 0.0 0 04 −24.872 0.0 0 0 −0.0074 0.0 0 09 −7.877 0.0 0 0
Continued on next page

694
M.
Giampietro
et
al.
/ European
Journal
of
Operational
Research
265
(2018)
685–702
Table 3
Continued.
Residual covariance matrix of factors and test assets
(Regime 1 above; Regime 2 below)
Factor 1 Factor 2 Factor 3 Agr. and Livestock Precious Industrials Energy 10Y Treasuries Aaa Corporate Baa Corporate VW Equity CRSP
Factor 1 6.456|5.951 2.1495 2.5539 −0.0098 −0.0097 −0.0100 −0.0221 −0.0048 −0.0071 0.0429 0.0051
Factor 2 −0.59925 6.259|1.094 1.8393 −0.0 0 06 −0.0 0 06 −0.0011 −0.0277 −0.0263 0.0056 −0.0213 −0.0049
Factor 3 2.69437 −0.3575 3.363|3.002 −0.0059 −0.0057 −0.0062 −0.0022 −0.0125 −0.0018 0.0259 −0.0 0 08
Agriculture and livestock 0.00650 −0.0023 0.00567 0.0 0 0 03|0.0 0 0 01 0.0 0 0 03 0.0 0 0 02 0.0 0 0 02 0.0 0 0 01 0.0 0 0 0 0 −0.0 0 011 −0.0 0 0 02
Precious metals 0.00642 −0.0023 0.00560 0.0 0 0 01 0.0 0 0 03|0.0 0 0 01 0.0 0 0 02 0.0 0 0 03 0.0 0 0 0 0 −0.0 0 0 01 −0.0 0 011 −0.0 0 0 01
Industrial Metals 0.00649 −0.0023 0.00569 0.0 0 0 01 0.0 0 0 01 0.0 0 0 02|0.0 0 0 02 0.0 0 0 02 0.0 0 0 01 0.0 0 0 01 −0.0 0 010 −0.0 0 0 03
Energy −0.01368 0.0 0 05 −0.00146 −0.0 0 0 01 0.0 0 0 0 0 −0.0 0 0 02 0.0 020|0.0 015 −0.0 0 016 −0.0 0 032 0.0 0 026 −0.00136
10Y treasury bonds 0.00992 −0.0044 0.00116 0.0 0 0 01 0.0 0 0 01 0.0 0 0 02 0.0 0 0 08 0.0 0 054|0.0 013 0.0 0 0 07 −0.0 0 025 −0.0 0 033
Aaa corporate bonds −0.01413 0.0 0 07 0.00175 0.0 0 0 0 0 0.0 0 0 0 0 0.0 0 0 01 −0.0 0 0 09 0.0 0 0 05 0.0 010|0.0 011 −0.0 0 036 0.0 0 079
Baa corporate bonds 0.01123 −0.0 0 02 0.00768 0.0 0 0 02 0.0 0 0 02 0.0 0 0 02 −0.0 0 0 02 0.0 0 018 0.0 0 039 0.0 043|0.0 014 0.0 0 081
VW equity CRSP −0.00630 0.0119 −0.02114 −0.0 0 0 07 −0.0 0 0 06 −0.0 0 0 08 0.0 0 017 0.0 0 018 −0.0 0 020 −0.0 0 0 03 0.01142|0.0063
(Regime 3 above; Regime 4 below)
Factor 1 Factor 2 Factor 3 Agr. and livestock Precious Industrials Energy 10Y treasuries Aaa corporate Baa corporate Baa corporate
Factor 1 4.733|9.577 1.41151 1.13496 −0.00245 −0.00244 −0.00241 0.00116 0.00547 0.00403 0.00842 −0.00349
Factor 2 −4.32624 5.874|38.56 −1.14499 −0.01730 −0.01729 −0.01732 −0.02381 −0.00111 0.01706 0.00362 0.05725
Factor 3 7.19695 −2.44773 3.564|9.660 0.00721 0.00721 0.00719 0.01139 0.00378 −0.00863 0.0 0 042 −0.03138
Agriculture and livestock −0.01906 −0.08629 −0.02670 0.0 0 0 09|0.0 0 034 0.0 0 0 08 0.0 0 0 09 0.0 0 0 08 0.0 0 0 02 −0.0 0 0 06 0.0 0 0 01 −0.0 0 026
Precious metals −0.01884 −0.08610 −0.02673 0.0 0 034 0.0 0 0 08|0.0 0 035 0.0 0 0 09 0.0 0 0 08 0.0 0 0 02 −0.0 0 0 06 0.0 0 0 01 −0.0 0 025
Industrial metals −0.01895 −0.08652 −0.02669 0.0 0 034 0.0 0 034 0.0 0 010|0.0 0 033 0.0 0 0 08 0.0 0 0 02 −0.0 0 0 06 0.0 0 0 01 −0.0 0 028
Energy −0.01291 −0.04177 0.01790 −0.0 0 0 04 −0.0 0 0 04 −0.0 0 0 03 0.0 018|0.0 032 0.0 0 054 0.0 0 022 0.00128 −0.0 0 0 08
10Y treasury bonds −0.02481 −0.02036 0.00318 0.0 0 0 02 0.0 0 0 02 0.0 0 0 02 0.00126 0.0 017|0.0 046 0.0 0 017 0.0 0 063 −0.0 0 045
Aaa corporate bonds −0.06913 0.06665 −0.06850 0.0 0 014 0.0 0 016 0.0 0 012 0.0 0 0 02 0.00279 0.0 021|0.0 058 0.0 0 046 0.0 0 070
Baa corporate bonds 0.03823 0.05599 0.04579 −0.0 0 046 −0.0 0 044 −0.0 0 046 0.00262 0.00288 0.00243 0.0 028|0.0 081 0.0 0 091
VW equity CRSP −0.02005 0.20483 0.03212 −0.0 0 080 −0.0 0 081 −0.0 0 080 0.00237 0.00308 0.00156 0.00483 0.0 061|0.0 093
Note: Significant conditional mean coefficients are boldfaced.

M. Giampietro et al. / European Journal of Operational Research 265 (2018) 685–702  695
Fig. 1. Smoothed state probabilities from three-factor block VAR(1), four regimes.
as  where  ι I is a n × 1 vector of ones and V is the covariance matrix
(cid:22)
|        |     |                           |               |       | of the pricing errors, i.e.,  |     |                       |     |                 |     |         |
| ------ | --- | ------------------------- | ------------- | ----- | ----------------------------- | --- | --------------------- | --- | --------------- | --- | ------- |
|        |     | (cid:5)T   − 1    (cid:7) | (cid:8)       |       |                               |     |                       |     |                 |     |         |
|        | 1   |                           | 2             |       |                               |     | (cid:5)T −1   (cid:7) |     | (cid:8) (cid:7) |     | (cid:8) |
| RMSE ≡ |     | rˆ  M                     | −r  i,t+1  ,  | (18)  |                               | 1   |                       |     |                 |     |         |
T − 1  i ,t+ 1  Vˆ  =  ι −Mˆ  M   ( ι + R ) ι −Mˆ  M   ( ι + R ) (cid:4) .
=   T − I  t   +1     I  t  +1    I  t   +1     I  t  +1    (22)
|     |     | t 1 |     |     |     |     | 1   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t=1
| where rˆ M  |   is the fitted asset i ’s return on the basis of model M ,  |     |     |     |     |     |     |     |     |     |     |
| ----------- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i,t+1
Noticeably, under mild conditions of stationarity of both asset
i.e.,
returns and the SDF and of existence of moments of the moment
|     |     | 1   | 1   |     | c o | n d it i o n | s ,   i t  t u rn | s   o u t   t h a t |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------ | ----------------- | ------------------- | --- | --- | --- |
rˆ  M    =   − m ˆ     M   − σ 2  ,  M  − σ 2   − σ M   ( 1 9 )   (cid:4) (cid:6)
| i ,t+ 1   | t + 1   | m   | i   i , m   |     |     |           |                |                   |                    |     |     |
| --------- | ------- | --- | ----------- | --- | --- | --------- | -------------- | ----------------- | ------------------ | --- | --- |
|           |         | 2   | 2           |     |     | (cid:5)T  | − 1    (cid:7) |                   | (cid:8)            |     |     |
|           |         |     |             |     |     | 1         | ι              | M   ( ι           | ) (cid:4)  Vˆ  −1  |     |     |
|           |         |     |             |     |     |           | I  − M         | ˆ        I  +   R |  +1                |     |     |
C l e a r ly ,  t h e   l ow e st   t he  RM SE ,   th e  l es s the predicted values d if f e r   T   − 1   t + 1 t
t=1
from the observed ones and the highest the pricing accuracy of the  (cid:4)   (cid:6)
m od e l.   T h e  t w o - st a te s ,   th r ee -f a c t o r   f u ll   M SV A R   tu r n s  o u t  t o   b e  t h e  (cid:5)T −1   (cid:7) (cid:8)
|     |     |     |     |     |     | × 1  | ι   | −Mˆ  M   ( ι | + R ) T  →→∞ |  χ  .  |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | ------------ | ------------ | ------ | --- |
top  p e r f o r m i ng   m o d e l   a cc o rd i n g   t o   t h e   RM S E ,  b ei n g   th e   o n e   w i th   I    +1     I  t  +1      2   (23)
|     |     |     |     |     |     | T − | 1   | t   |     | I   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the minimal average distance between observed and predicted val-  t=1
ues.
Observing the p -values for the test, reported in Table 2 to-
Moreover, to test whether or not the difference between fitted
gether with the test statistic, we notice that the null of equality
and observed values is statistically different from zero, we per-
between observed and fitted values cannot be rejected for five al-
form a two-tailed chi-squared test. In particular, the test statistic
ternative HMM models: the two-state, three- and five-factor full
reported in Table 2 is defined as follows. Given the n Euler condi-
MSVAR models, the three-state, three- and five-factor full MSVAR
tions expressed as
models, and the four-state, five-factor MSVAR model.
1 = E [M   +1  (  1 + R  )|   (cid:3) t  ],   i = 1 , 2 , . . . , n  (20)  These results are interesting in several ways. First, we notice
|     | t   | i,t+1  |     |     |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
that in the single-state case, the null of no difference between pre-
a Wald-type test of the joint validity of the I conditions is:  dicted and observed returns is always rejected at any conventional
(cid:4)   (cid:6)   level of significance (the p -values are equal to zero). This signals
|     | (cid:7) |     | (cid:8) |     |     |     |     |     |     |     |     |
| --- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
1  (cid:5)T −1   t h a t  t he   u s e  o f   a   n o n - li n e a r  S D F s  r e a ll y  m a k e s  t h e  d if f e r e n c e   w h e n
|     | ι −Mˆ  | M   ( ι | + R ) (cid:4)  Vˆ  −1  |     |     |     |     |     |     |     |     |
| --- | ------ | ------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
I    +1     I  t  +1    it   c o m e s   to   p r i c i n g   p e r fo r m a n c e .  S e c o nd ,   th e   m o d e l s   t h a t   w e r e
| T − 1  |     | t   |     |     |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:4) t=1  (cid:6) selected by the information criteria are both rejected when their
|     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:5)T −1   (cid:7) (cid:8) p ri c i n g   p e r f o rm a n c e   is   co n s id e r e d .  In d e e d ,  t h e  h y p o t h e s i s  o f   a c -
1
| ×   |     | ι −Mˆ  M |   ( ι + R ) ,  |     |     |     |     |     |     |     |     |
| --- | --- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
T − I  t   +1     I  t  +1    (21)  cu r a t e   p r ic i n g  p e rf o r m a n ce   ( n o   d if fe re n c e   b e tw e e n   o b s e r v e d   a n d
1
t=1  predicted returns) is rejected for both the three-state, three-factor

696  M. Giampietro et al. / European Journal of Operational Research 265 (2018) 685–702
Table 4
Reality check results.
Model  HJ-distance  P-value H  0 : HJ = 0  T  Reality check p-value
|     |     |     | 3 factors, 2 states, full VAR(1)          |     |     |     | 5.7915    |     | 0.0 0 01   |     | −40. 937  | 0.9568  |     |     |
| --- | --- | --- | ----------------------------------------- | --- | --- | --- | --------- | --- | ---------- | --- | --------- | ------- | --- | --- |
|     |     |     | 3 factors, 3 states, full VAR(1)          |     |     |     | 6.0 0 04  |     | 0.0 0 01   |     | 40 .937   | 0.8827  |     |     |
|     |     |     | 5 factors, 3 states, full VAR(1)          |     |     |     | 6.1350    |     | 0.0 0 01   |     | 68 .070   | 0.8395  |     |     |
|     |     |     | 5 factors, 4 states, block Factor VAR(1)  |     |     |     | 6.6365    |     | 0.0 0 0 0  |     | 174 .469  | 0.3889  |     |     |
|     |     |     | 5 factors, single state, full VAR(1)      |     |     |     | 6.6448    |     | 0.0 0 0 0  |     | 176 .297  | 0.3148  |     |     |
block MSVAR and the four-state, three-factor block MSVAR mod-  cise than others are, none of them could be characterized by in-
els. More generally, as far as the pricing performance is concerned,  significant overall violations of the set of Euler conditions on which
the full MSVAR models are strongly preferred over their more par-  our paper was based. This is of course unsurprising in the light
simonious block MSVAR counterparts. In fact, a full VAR structure,  of the results in the literature that tend to report that empirical
where each pricing factor also depends on the lags of the test asset  SDF based on macroeconomic variables have a hard time fitting
returns, appears to be required to accurately predict future asset  the cross-section of asset returns.
returns.  However, it may be also interesting to ask—given that all esti-
Because our empirical efforts  are devoted to find an SDF that  mated SDFs appear to have been rejected—whether any models are
correctly prices a medium-sized cross-section of asset returns that  at least superior, i.e., rejected with a statistically significant differ-
includes commodities, it also seems natural to adopt Hansen and  ence turning in their favor. Unfortunately, the distribution of H J M
Jagannathan’s (1997) distance measure to quantify (in the appro-  under the null hypothesis is not the same regardless of the model
priate SDF mean-variance space) the distance between the can-  considered. Therefore, to make comparisons possible, we have se-
didate SDFs and what is required by our asset return data. In  lected the five models with the lowest HJ distance and applied
particular, HJ propose an in-sample measure of fit defined as a  the test proposed by Chen and Ludvingson (2009) and based on
quadratic function of observed pricing errors (here, the n x 1  White’s (20 0 0) “reality check” method. For each of the five mod-
ι −Mˆ   M   (  ι + R ) for t = 1, 2, …, T − s i = 1, 2, 3, 4, 5
vector  I  +1   I  t  +1  1) weighted by  els, labeled a , the null hypothesis is:
|     |     | t   |     |     |     |     |     |     |     | (cid:26)  (cid:7) | (cid:8) | (cid:27) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ------- | -------- | --- | --- |
the inverse of the second moment matrix of gross asset returns,
|     |  ( ι |     | )(  ι | )  (cid:4)  |     |     |     |     |     | H J i 2  | −(  | H J j )2   ≤0  |     |     |
| --- | ---- | --- | ----- | ----------- | --- | --- | --- | --- | --- | -------- | --- | -------------- | --- | --- |
S M  ≡ E [     +  R  +1  I  + R  +1  ] , which is positive definite by con-  H o :  m a x     (25)
|     |     | I   t | t   |     |     |     |     |     | j= 2 , 3 |  ,  4 ,  5  |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | --- | --- | --- |
st ru cti o n :  1 1
(cid:23)
(cid:24)   (cid:4)   (cid:6)  (cid:4)  I n   w o r d s ,   u n d e r   t h e   n u ll ,   t h e   m o d e l e d   la b e l e d   a s   i   =   1 ,  2 ,   3 ,   4 ,
|     | (cid:24) |     | (cid:7) |     | (cid:8) |     |     |     |     |     |     |     |     |     |
| --- | -------- | --- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:25)   1  (cid:5)T −1   5 ,  h a s   a   s m a l l e r   ( m a x i m u m )   p r i c i n g   e r r o r  v s .  a l l  o t h e r   m o d e l s .   B e -
| M ≡  |     |     | ι −Mˆ  |  M   ( ι | + R ) S M −1  |     |     |     |     |     |     |     |               |                |
| ---- | --- | --- | ------ | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------------- |
| H J  |     | T − | I      | +1       | I  t  +1      |     |     |     |     |     |     |     |  ( i  ) 2   − | (  j   ) 2   > |
1  t ca u s e   t h   e   a l t e r n a t i v e   h y p o t h e s i s   is   t h a t   m a x   [  H  J     H  J   ]
|     |     |          | t=1  |     |     |     |     |     |     |     |     | j=2 , 3 , 4 , 5  |     |     |
| --- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- |
|     |     | (cid:23) |      |     |     |     |     |     |  ,  |     |     |                  |     |     |
(cid:24)   (cid:4)   (cid:6)   0   t h i s   i s   a   o n e - s id e d   t e st.   Th e   v a lue of the test statistic for m o d e l
|     |                                              | (cid:24)      | (cid:7)           |           | (cid:8)         |             |     |         |                                                                |                     |                  |                 |     |           |
| --- | -------------------------------------------- | ------------- | ----------------- | --------- | --------------- | ----------- | --- | ------- | -------------------------------------------------------------- | ------------------- | ---------------- | --------------- | --- | --------- |
|     |                                              | (cid:25)   1  | (cid:5)T   − 1    |           |                 |             |     |         | i   i s   si m                                                 | p l y :             |                  |                 |     |           |
|     | ×                                            |               | ι                 | −Mˆ   M   | ( ι + R )       |             |     |         |                                                                |                     | (cid:26)         | (cid:27)        |     |           |
|     |                                              | T −           | I                 | +1        |     I  t  +1    |             |     | (24)    |                                                                | √                   |  (cid:7) (cid:8) |                 |     |           |
|     |                                              |               | 1                 | t         |                 |             |     |         | ≡                                                              |                     |  i  2            | − (  J j  ) 2   |     |           |
|     |                                              |               | t = 1             |           |                 |             |     |         | T     m                                                        | a x   T             |   H  J           | H               |     | ( 2 6 )   |
|     |                                              |               |                   |           |                 |             |     |         | i j = 2                                                        |  ,  3  ,  4  ,  5   |                  |                 |     |           |
|     | The parameter of each SDF model enter H J M  |               |                   |           |                 | through Mˆ  |     |  M   .  |                                                                |                     |                  |                 |     |           |
|     |                                              |               |                   |           |                 |             |     | t +1    | The p -value of the test is computed considering the quantile  |                     |                  |                 |     |           |
Hansen and Jagannathan show that for a given set of parame-  of the distribution of T  i simulated according to the reality check
ters characterizing ( 24 ), H J M
|     |     |     |     | equals the maximum pricing error  |     |     |     |     | procedure with a block bootstrap.  |     |     |     |     |     |
| --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- |
generated by the model. Obviously, lower values of H J M
|     |     |     |     |     |     |     | are then  |     | Table 4 shows that the 3-factor, full VAR(1) HMM with two  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- |
preferable. Such values are reported in the rightmost column of
regimes provides a superior pricing accuracy in the SDF space:
Table 2 and reveal that the minimal HJ distance in the SDF mean-
when this model is used as a benchmark, the test statistic is
variance space are achieved by two- and three-state HMM models.  negative ( −40.9) and the null that the corresponding HJ distance is
In particular, a three-factor, two-state full VAR(1) achieves a H J M
lower than all other models in the Table, cannot be rejected with a
value of 5.791. More generally, both three- and five-factor models
very high p -value in excess of 95%. Interestingly, also in this case,
with two and three regimes appear to minimize the distance from
an unrestricted full VAR(1) dynamics is required for an HMM SDF
the SDF that the data imply.
to yield accurate pricing. 12
For each of the models in Table 2 (i.e., as M changes), we also
Therefore a relatively simple, 3-factor, full VAR(1) HMM with
test the null hypothesis that H J M = 0. However, the distribution
two regimes is rejected in the HJ SDF space, but is at least the
of H J M
under the null fails to be standard because the weighting  most accurate across all of our models. As already mentioned, this
matrix that appears in ( 24 ) is not optimal in the sense of Hansen
(1982) . Therefore, the p -value of the null H J M = 0 has been com-  model has in fact the lowest possible pricing RMSE and the null
hypothesis of correct pricing as expressed by a zero overall RMSE
puted using 10,0 0 0 simulations for a weighted sum of chi-squared
cannot be rejected by a chi-square test based on moment condi-
distributions, exploiting Jagannathan and Wang’s (1996) finding
tions and the covariance matrix of pricing errors. Table 5 shows the
that such a weighted sum represents the asymptotic distribution of
estimates for such a two-regime model. Also in this case, to save
( H J M  ) 2  . The results of such a test are not reported in Table 2 be-
cause all the corresponding p -values turned out to be essentially
| nil, an indication that even though some models may be more pre-  |     |     |     |     |     |     |     |     | 12  |     |     |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
We have also used Chen and Ludvigson (2009) -style reality check methodology
to test whether we can reject the null of a smaller HJ distance of two-, three-,
and four-state HMM SDF models vs. their single regime counterparts, given a fixed
| 11  | Clearly, SM ≡E[ ( ι |     | +1 )( ι | +1 ) (cid:4)  |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------- | --- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
I + Rt   I + Rt   ] , must be estimated by some empirical,  choice of number of macroeconomic factors. In the cases of two- and three-state
sample construct. In any event, such an estimator will differ from Vˆ  because based  HMM SDFs, we report that the null of smaller HJ distance vs. the single-state case
only on asset return data and not on pricing errors. The 10-factor model HJ dis-  cannot be rejected. Interestingly, the opposite occurs in the case of the four-state
tance statistic could not be computed because the number of factors exceeded the  block VAR model. This confirms that both in the pricing and in the SDF spaces, an
number of tests assets.  unrestricted full VAR dynamic structure plays a key role.

M.
Giampietro
et
al.
/
European
Journal
of
Operational
Research
265
(2018)
685–702
697
Table 5
Model estimates- three-factor full VAR(1), Two regimes.
Regime 1 Regime 2
Coefficient Std. error t -Statistic p -value Coefficient Std. error t -Statistic p -value
Factor VAR coefficients, SDF loadings and estimated transition matrix
[F1/F1] Coeff. 0.5178 0.044 11.757 0.0 0 0 0.9524 0.029 33.272 0.0 0 0
[F1/F2] Coeff. −0.0093 0.068 −0.137 0.891 0.3173 0.030 10.478 0.0 0 0
[F1/F3] Coeff. −0.4335 0.062 −7.046 0.0 0 0 Transition matrix −0.3387 0.050 −6.781 0.0 0 0
F1: Intercept −2.3291 0.838 −2.779 0.005 0.9328 0.3265 −2.0790 0.900 −2.309 0.021
[F2/F1] Coeff. −0.0871 0.026 −3.384 0.001 0.0672 0.6735 −0.3484 0.037 −9.494 0.0 0 0
[F2/F2] Coeff. −0.2239 0.036 −6.270 0.0 0 0 −0.3094 0.036 −8.505 0.0 0 0
[F2/F3] Coeff. 0.0767 0.032 2.381 0.017 Implied durations 0.1776 0.060 2.983 0.003
F2: Intercept −0.8196 0.431 −1.901 0.057 Regime 1: 14.87 1.3048 1.074 1.215 0.224
[F3/F1] Coeff. −0.3077 0.033 −9.253 0.0 0 0 Regime 2: 3.06 −0.1368 0.029 −4.707 0.0 0 0
[F3/F2] Coeff. 0.0049 0.051 0.095 0.924 0.3051 0.030 10.287 0.0 0 0
[F3/F3] Coeff. 0.1083 0.046 2.342 0.019 0.3462 0.049 7.108 0.0 0 0
F3: Intercept −1.7211 0.630 −2.734 0.006 Ergodic probs.: 5.5673 0.878 6.338 0.0 0 0
SDF: Loading on F1 −0.0 0 02 0.0 0 0 −2.412 0.016 Regime 1: 0.829 −0.0 0 06 0.0 0 01 −5.753 0.0 0 0
SDF: Loading on F2 −0.0021 0.0 0 0 −17.229 0.0 0 0 Regime 2: 0.171 −0.0015 0.0 0 01 −17.103 0.0 0 0
SDF: Loading on F3 0.0 0 08 0.0 0 0 6.245 0.0 0 0 −0.0020 0.0 0 01 −15.773 0.0 0 0
SDF: Intercept −0.0049 0.0 0 0 −14.864 0.0 0 0 −0.0 0 06 0.0 0 09 −0.681 0.496
Residual covariance matrix of factors and test assets
(Regime 1 above; Regime 2 below)
Factor 1 Factor 2 Factor 3 Agr. and livestock Precious Industrials Energy 10Y treasuries Aaa corporate Baa corporate VW equity CRSP
Factor 1 5.134|8.322 0.5982 2.1685 −0.0 0 08 −0.0 0 07 −0.0 0 08 −0.0 0 09 0.0070 −0.0055 0.0167 −0.0073
Factor 2 −2.07911 2.798|19.232 0.0988 −0.0069 −0.0069 −0.0069 −0.0038 −0.0063 0.0045 0.0077 0.0252
Factor 3 4.97309 −1.2470 3.017|9.465 0.0018 0.0019 0.0018 0.0022 −0.0044 −0.0051 0.0052 −0.0192
Agriculture and livestock −0.01494 −0.0254 −0.02358 0.0 0 0 03|0.0 0 019 0.0 0 0 02 0.0 0 0 03 0.0 0 0 02 0.0 0 0 03 0.0 0 0 0 0 0.0 0 0 0 0 −0.0 0 012
Precious metals −0.01476 −0.0250 −0.02345 0.0 0 020 0.0 0 0 02|0.0 0 020 0.0 0 0 03 0.0 0 0 02 0.0 0 0 03 0.0 0 0 0 0 0.0 0 0 0 0 −0.0 0 011
Industrial metals −0.01483 −0.0260 −0.02395 0.0 0 019 0.0 0 019 0.0 0 0 03|0.0 0 018 0.0 0 0 01 0.0 0 0 04 0.0 0 0 01 0.0 0 0 01 −0.0 0 014
Energy −0.05301 −0.0717 0.03395 −0.0 0 0 07 −0.0 0 0 07 −0.0 0 0 06 0.0 015|0.0 041 0.0 0 014 −0.0 0 0 05 0.0 0 048 −0.0 0 023
10Y Treasury Bonds −0.04994 0.0077 −0.00821 0.0 0 0 01 0.0 0 0 01 0.0 0 0 01 0.00157 0.0 014|0.0 040 0.0 0 014 0.0 0 029 −0.0 0 026
Aaa Corporate Bonds −0.05562 0.1264 −0.06096 0.0 0 015 0.0 0 016 0.0 0 014 0.0 0 036 0.00259 0.0 016|0.0 051 0.0 0 051 0.0 0 045
Baa Corporate Bonds 0.01720 −0.0562 0.03608 −0.0 0 028 −0.0 0 025 −0.0 0 028 0.0 030 0 0.00278 0.00131 0.0 028|0.0 070 0.0 0 067
VW Equity CRSP −0.03731 0.0440 −0.0 0 052 −0.0 0 057 −0.0 0 060 −0.0 0 055 0.00192 0.00332 0.00160 0.00406 0.0 076|0.0 089
Note: Significant conditional mean coefficients are boldfaced.

698 M. Giampietro et al. / European Journal of Operational Research 265 (2018) 685–702
Fig. 2. Smoothed state probabilities from three-factor block VAR(1), two regimes.
space, we have omitted a large number of coefficients from the regime-specific covariance matrices confirms that estimated vari-
two 11 × 11 VAR(1), regime-specific matrices to focus only on key ances in the second state are considerably higher (up to 7 times),
coefficients concerning the factors and the dynamics of the SDF. In which is consistent with a turbulent regime characterization.
general, most reported conditional mean coefficients are statisti- Finally, with reference to the estimated of the coefficients with
cally significant and vary considerably across the two regimes esti- which the SDF loads on the three macroeconomic factors, in
mated. This also concerns the VAR structure. For instance, the first, Table 5 , we note that although the sign of only one coefficient
business-cycle related factor 1 is much more serially correlated in (on the third factor) switches across regimes, the absolute value of
the second state (coefficient of 0.95) than in the first state (0.52). the coefficients is rather different across states. In particular, the
Proceeding first with an interpretation of the two regimes, overall level—as measured by the estimated intercept—of the SDF
Fig. 2 shows that both Markov states are rather persistent, with is higher under the crisis regime, which is sensible because dur-
the second able to single out crisis periods, such as the Summer ing a crisis we do expect wealth to be lower, its certainty equiv-
1998 Asian flu crisis, the 20 01–20 02 Enron and WorldCom scan- alent to be perceived as lower (due to increased risk), and hence
dals, the 20 08–20 09 great financial crisis, a few short bouts of Eu- marginal utility of future wealth to be higher. Moreover, the log-
ropean sovereign jitters, for instance in the Fall of 2011. These im- SDF loading (hence, the semi-elasticity of the stochastic discount)
pressions are confirmed by Table 5 , where both regimes are char- is roughly three times more sensitive to business cycle conditions
acterized by “stayer” probabilities on the main diagonal of the es- under the crisis regime, which is also to be expected.
timated transition matrix well in excess of 0.5 (their implicit dura-
tions are in fact 15 and 3 months). Even though it less persistent, 4.3. Matching sample moments with estimated SDFs
regime 2 is no way irrelevant, as its ergodic, long-run probability
is 17%, which seems a sensible assessment of the frequency of cri- In this section, we assess to what extent a selection of com-
sis periods in any long sample of US data. A look at the estimated, peting SDFs are able to match the empirical mean, standard
deviation, skewness, excess kurtosis, and pair-wise cross asset cor-

M. Giampietro et al. / European Journal of Operational Research 265 (2018) 685–702 699
Table 6
Observed and implied moments –comparing different models.
The table reports the observed and the model-implied means, standard deviation, skewness, and excess kurtosis of different asset class returns. Implied values that have
been boldfaced and underlined indicate that the model-implied moment falls within the 90% confidence interval formed around the corresponding sample moment.
Lower Sample Upper Single-regime, 3 Two-regime, 3 Four-regime, 3
bound 5% observed bound 95% Factors, Full VAR(1) Factors, Full VAR(1) Factors, Block VAR(1)
Mean returns
Macro factors Factor 1 −0.4355 0.0 0 0 0 0.4355 −7.6183 −1.3904 0.5493
Factor 2 −0.3059 0.0 0 0 0 0.3059 1.3638 0.0825 −0.0874
Factor 3 −0.1040 0.0 0 0 0 0.1040 2.6199 1.1234 −0.2028
Stocks and bonds Aaa Corp. 0.0021 0.0023 0.0025 0.0051 0.0083 0.0046
Baa Corp. 0.0031 0.0033 0.0035 0.0051 0.0083 0.0046
10Y Treasuries 0.0040 0.0042 0.0044 0.0051 0.0083 0.0046
VW CRSP Equity 0.0 0 09 0.0054 0.0098 0.0044 0.0095 0.0058
Commodities Agriculture and livestock −0.0045 −0.0 0 02 0.0040 0.0041 0.0091 0.0053
Precious metals −0.0038 0.0030 0.0098 0.0039 0.0092 0.0055
Industrial metals −0.0052 0.0 0 08 0.0068 0.0036 0.0102 0.0064
Energy −0.0019 0.0071 0.0161 0.0011 0.0121 0.0083
Standard deviation of returns
Macro factors Factor 1 4.0766 4.3852 4.6937 4.9518 4.5825 3.6785
Factor 2 2.8634 3.0801 3.2968 3.0230 5.8184 3.1802
Factor 3 0.9735 1.0471 1.1208 2.7631 5.9967 2.5256
Stocka and bonds Aaa Corp. 0.0018 0.0019 0.0021 0.0028 0.0093 0.0064
Baa Corp. 0.0018 0.0019 0.0021 0.0027 0.0092 0.0062
10Y Treasuries 0.0018 0.0019 0.0021 0.0033 0.0095 0.0066
VW CRSP Equity 0.0416 0.0447 0.0479 0.0447 0.0447 0.0443
Commodities Agriculture and livestock 0.0398 0.0428 0.0458 0.0428 0.0434 0.0429
Precious metals 0.0636 0.0684 0.0732 0.0467 0.0479 0.0471
Industrial metals 0.0563 0.0606 0.0648 0.0602 0.0601 0.0598
Energy 0.0841 0.0904 0.0968 0.0903 0.0892 0.0893
Skewness
Macro factors Factor 1 −1.9452 −1.7033 −1.4613 0.0770 −0.1211 −0.2312
Factor 2 −0.9915 −0.7495 −0.5076 −0.0023 −1.5819 −0.4689
Factor 3 1.6964 1.9383 2.1803 −0.0086 2.1427 −0.1774
Stocka and bonds Aaa Corp. −0.2404 0.0016 0.2436 0.0067 1.5304 0.5880
Baa Corp. −0.2425 −0.0 0 05 0.2414 0.0092 1.6212 0.2759
10Y Treasuries −0.2315 0.0105 0.2524 0.0048 1.3824 0.8507
VW CRSP Equity −0.8619 −0.6199 −0.3779 −0.0065 0.1041 −0.0387
Commodities Agriculture and livestock −0.3300 −0.0880 0.1539 0.0070 0.1351 0.0329
Precious metals 0.0926 0.3346 0.5765 0.0072 0.1350 0.0438
Industrial metals −0.3465 −0.1045 0.1375 −0.0078 0.0727 −0.0280
Energy 0.1453 0.3872 0.6292 0.0011 0.0111 −0.0179
Excess Kurtosis
Macro factors Factor 1 4.4274 4.9593 5.4912 1.7618 5.0973 3.3287
Factor 2 3.8200 4.3519 4.8838 1.5328 15.7805 4.5131
Factor 3 46.2694 46.8013 47.3331 18.5047 9.3663 28.5483
Stocka and bonds Aaa Corp. −1.2751 −0.7432 −0.2113 −0.5312 3.1026 −0.0128
Baa Corp. −1.2853 −0.7534 −0.2215 −0.5324 3.4 4 47 −0.1128
10Y Treasuries −1.2608 −0.7289 −0.1971 −0.5226 2.5976 0.1031
VW CRSP Equity 0.5307 1.0625 1.5944 0.2034 1.1319 0.9294
Commodities Agriculture and livestock 1.0796 1.6115 2.1433 0.4289 1.5492 1.6788
Precious metals 2.4155 2.9474 3.4793 0.9636 3.4047 2.5107
Industrial metals 0.9689 1.5008 2.0327 0.3857 1.3416 1.6031
Energy 1.0783 1.6101 2.1420 0.4358 1.1673 1.2445
relations, with special emphasis on commodities. Specifically, we confidence interval have been boldfaced. As far as mean returns
check whether each model-implied moment falls within the 90% are concerned, no model clearly outperforms the others. While all
confidence interval built around the sample estimate (i.e., whether SDFs match the mean return of the equity index, the four-regime
it is lower than the 95% upper band and higher than the 5% model does particularly well at matching the means of the com-
lower band computed under standard assumptions). If this hap- modity series. Moreover, all models fail to reproduce the sample
pens, we consider this sample moment to have been matched mean of bond returns.
by a given SDF. The moments implied by an SDF are computed Similar considerations apply to standard deviations, for which
by Monte Carlo simulation, using 20,0 0 0 trials: as such they can all the three models do match the volatility of all assets apart from
be taken to represent population moments implied by any given bonds and precious metals. The situation is more heterogeneous
SDF. In particular, we compare three of the competing model for what concerns higher-order moments. The block MSVAR frame-
specifications discussed in Sections 4.1 and 4.2 and covered by work is quite weak at matching skewness, while both the two-
Tables 2–5 , namely, the four-state three-factor block MSVAR, which state full MSVAR and the single-state SDFs can replicate four and
is the winning model according to the information criteria, the five values out of eleven, respectively. Noticeably, the single-state
two-state, three-factor full MSVAR, the top performer in terms model can generate the modest (close to zero) positive skewness
of pricing accuracy, and a benchmark single-state three-factor full of bonds, while the two-state model generates too much positive
VAR model. skewness. However, the two-state model outperforms its single-
Table 6 reports sample and model-implied means, standard de- state counterpart as far as commodity series are concerned. Finally,
viations, skewness, and excess kurtosis coefficients of the returns as one would expect, both switching models are considerably bet-
on different asset classes. Implied values that fall within the 90% ter than the single-state SDF at yielding excess kurtosis, especially

700 M. Giampietro et al. / European Journal of Operational Research 265 (2018) 685–702
Table 7
Observed and implied correlations –comparing different models.
The table reports the observed and the model-implied pairwise correlations for different asset class returns. Implied values that have been boldfaced and underlined indicate
that the model-implied correlation falls within the 90% confidence interval formed around the corresponding sample moment.
Lower Sample Upper Single-regime, 3 Two-regime, 3 Four-regime, 3
bound 5% observed bound 95% factors, full VAR(1) factors, full VAR(1) factors, block VAR(1)
Agricultural commodities and livestock
Agric. and livestock –Aaa corp. 0.0233 0.1223 0.2212 0.1252 0.1946 0.0670
Agric. and livestock –Baa corp. 0.0370 0.1357 0.2345 0.1168 0.1914 0.0600
Agric. and livestock –Treasuries 0.0080 0.1071 0.2062 0.1240 0.1971 0.0731
Agric. and livestock –VW CRSP equity 0.1236 0.2209 0.3181 0.2170 0.2231 0.2095
Agric. and livestock –Precious metals 0.1969 0.2923 0.3876 0.2905 0.3137 0.2808
Agric. and livestock –Industrial metals 0.0605 0.1589 0.2573 0.3018 0.3024 0.2984
Agric. and livestock –Energy 0.2108 0.3057 0.4006 0.1476 0.1273 0.1319
Precious metals
Precious metals –Aaa corp. 0.0943 0.1921 0.2899 0.1211 0.2397 0.0884
Precious metals –Baa corp. 0.0984 0.1961 0.2938 0.1333 0.2426 0.0915
Precious metals –Treasuries 0.1001 0.1978 0.2955 0.1085 0.2373 0.0877
Precious metals –VW CRSP equity −0.0735 0.0261 0.1258 0.0254 0.0477 0.0203
Precious metals –Industrial metals 0.1136 0.2111 0.3085 0.2518 0.2632 0.2538
Precious metals –Energy 0.1610 0.2573 0.3536 0.2058 0.1926 0.1951
Industrial metals
Industrial metals –Aaa corp. −0.1106 −0.0109 0.0887 0.0010 0.0558 0.0165
Industrial Metals –Baa corp. −0.0905 0.0092 0.1089 0.0192 0.0609 0.0231
Industrial metals –Treasuries −0.1268 −0.0272 0.0724 0.0072 0.0571 0.0191
Industrial metals –VW CRSP equity −0.0094 0.0899 0.1891 0.3747 0.1693 0.3748
Industrial metals –Energy 0.1913 0.2868 0.3823 0.2802 0.2615 0.2726
Energy
Industrial metals –Aaa corp. −0.0077 0.0916 0.1908 −0.0841 −0.0681 −0.0938
Industrial metals –Baa corp. 0.0268 0.1257 0.2246 −0.0500 −0.0773 −0.0806
Industrial metals –Treasuries −0.0113 0.0880 0.1873 −0.1036 −0.0098 −0.0106
Industrial metals –VW CRSP equity 0.2882 0.3804 0.4726 0.0900 0.0647 0.0821
Lower Sample Upper Single-regime, 3 Two-regime, 3 Four-regime, 3
bound 5% observed bound 95% factors, full VAR(1) factors, full VAR(1) factors, block VAR(1)
Aaa corporate bonds
Aaa corp. –Baa corp. 0.9645 0.9828 1.0012 0.9427 0.9946 0.9890
Aaa corp. –Treasuries 0.9784 0.9914 1.0045 0.9563 0.9940 0.9883
Aaa corp. –VW CRSP equity −0.1113 −0.0116 0.0880 0.0099 0.1025 0.0157
Baa corporate bonds
Aaa corp. –Treasuries 0.9627 0.9817 1.0 0 07 0.8184 0.9789 0.9578
Aaa corp. –VW CRSP equity −0.0825 0.0172 0.1168 0.0453 0.1133 0.0292
10-Year treasury bonds
Aaa corp. –VW CRSP equity −0.1071 −0.0075 0.0922 0.2170 0.0096 0.0091
in the case of commodity returns. Indeed, while the single-state variate Bayesian dynamic conditional correlation model, which can
model matches the small and negative excess kurtosis of the bond, account for time variation in the correlation patterns, produces sta-
the two- and four-state models reproduce the positive excess kur- tistically more accurate density forecasts for equity and commodity
tosis of all the commodity returns. returns, and gives large economic gains in an asset allocation exer-
The three SDF models seem to be equally good at reproducing cise, relative to a benchmark random walk model. In addition, the
cross-asset pair-wise correlations. Indeed, the single-state model model previously selected by the information criteria, namely the
matches 18 out of 28 cross-asset pair-wise correlations, while four-state three-factor block MSVAR, is outperformed by the two-
the four-state and the two-state models 17 and 19, respectively. regime three-factor full MSVAR. This is consistent with the better
Three plots in Appendix E graphically display where the model- pricing performance of the latter already discussed in Section 4.2 .
implied correlations stand with respect to sample ones, focusing
on the pair-wise correlations of commodities with traditional as- 4.4. Comparisons with a commodity factor-based benchmark
set classes and among themselves, which are the most interest-
ing sample moments in our analysis. Interestingly, the two-state As a final robustness check, we have also estimated one
model clearly outperforms its single-state benchmark for what SDF-version of a benchmark pricing factor model proposed by
concerns the pair-wise correlations between commodities and the BGR (2014) . They propose a linear factor model based on
other asset classes, with a hit ratio of 88% (compared to the 69% three well-known, commodity-specific factors: Average, Carry, and
of the single-state model). This is not surprising considering that Momentum. The average factor is the excess return of a long po-
the relationships of commodities with traditional asset classes has sition in all available commodity futures; the carry factor is the
changed in the last decade with the so called “financialization” of return on an equally-weighted strategy that buys the five com-
commodities and only a Markov switching SDF can capture this modities that are most backwardated and shorts the ones that are
structural shift. most in contango at each point in time; the momentum factor
In conclusion, the two-state, three-factor full MSVAR model is the return on an equally-weighted portfolio that is long in the
outperforms a simple single-state benchmark when it comes to es- five commodities with the highest returns over the previous six
timate the moments of commodities and their correlations with months and short the ones with the lowest returns over the pre-
the other asset classes. This supports previous findings in the liter- vious six months. In our paper, for obvious comparability goals,
ature. For example, Lombardi and Ravazzolo (2016) find that a bi- we work with a single-state, SDF-type implementation of BGR’s

M. Giampietro et al. / European Journal of Operational Research 265 (2018) 685–702 701
model in the sense that Average, Carry, and Momentum are used nancialization” process, so that it is sensible that only a Markov
as the factors on which the SDF depends on. This strategy of try- switching SDF may be flexible enough to capture this structural
ing to explain the cross-section of commodity returns using vari- shift.
ables that capture the general conditions of the commodity market Given our result that macro factor-based HMM models outper-
has recently become popular in a strand of the literature (see, e.g., form an SDF implementation of BGR’s framework, only based on
Daskalaki and Skiadopoulos, 2011, Daskalaki, Kostakis, Skiadopou- commodity-specific factors, it would be interesting to further ex-
los, 2014 ; Szymanowska et al., 2012 ; Yang, 2013 ). 13 plore the econometric nature of the segmentation of commodities
Empirically, the BGR’s SDF yields (unreported, but available and to assess whether there exist some joint choice of factors (both
upon request) maximum likelihood estimates that are weakly sta- macroeconomic and commodity-related) able to price the cross-
tistically significant and characterized by uniformly positive load- section of returns of all assets. However, we will leave this question
ings, which is consistent with the marginal utility of future wealth for future research.
increasing as Average, Carry, and Momentum increase. However,
the loadings of the log-SDF on Momentum and especially Carry
are not estimated with sufficient accuracy (their p -values are 0.13 Supplementary materials
and 0.71, respectively). Despite the low statistical significance of
the estimated loadings, the pricing performance of BGR’s model is Supplementary material associated with this article can be
not completely amiss: for instance, the corresponding chi-square found, in the online version, at doi:10.1016/j.ejor.2017.07.045 .
test for zero pricing errors delivers a 0.168 p -value. However, such
a performance is dominated by all HMM factor-based models, re-
References
gardless of the number of regimes specified. Moreover, also BGR
is characterized by a relatively high and statistically significant HJ Alizadeh, A. H. , Nomikos, N. K. , & Pouliasis, P. K. (2008). A Markov regime switching
distance (13.20) that leads to a rejection of the model. Given that approach for hedging energy commodities. Journal of Banking and Finance, 32 ,
this had also occurred in the case of HMM models, we there- 1970–1983 .
Asness, C. A. , Moskowitz, T. J. , & Pedersen, L. H. (2013). Value and momentum ‘ev-
fore proceed to use White’s (20 0 0) “reality check” method to test erywhere’. Journal of Finance, 68 , 929–985 .
the null hypothesis that [ ( H J BGR ) 2 −(H J 2 REG ) 2 ] ≤0 , in words that Bae, G. , Kim, W. , & Mulvey, J. M. (2014). Dynamic asset allocation for varied finan-
a BGR-inspired SDF implies a a smaller (maximum) pricing er- cial markets under regime switching framework. European Journal of Operational
Research, 234 , 450–458 .
ror vs. two-state three-factor full VAR(1) model that had previ-
Baker, S. R., Bloom, N., & Davis, S. J. (2012). “Has economic policy uncertainty ham-
ously emerged as our “champion” of pricing performance. We find pered the recovery?”Chicago Booth Research Paper No. 12-06.
a one-sided test statistic T
2REG-BGR
= 2336 that strongly rejects Baks
s
h
e
i
c
,
t i
G
on
. , G
an
ao
d
,
t
X
im
. ,
e
&
s
R
er
o
i
s
e
s
s
i ,
o
A
f
.
c
(
o
2
m
0
m
14
o
)
d
.
i
A
ty
b
r
e
e
t
t
t
u
er
r n
s
s
p
.
e
U
ci
n
fi
i
e
v
d
e r
m
si
o
ty
d e
o
l
f
t o
M
e
a
x
r
p
y
l
l
a
a
i
n
n
d
t h
W
e
o
c
r
r
k
o
i
s
n
s–
g
the null hypothesis of an inferior HJ distance by the BGR’s bench-
Paper .
mark vs. the HMM two-state model, with a p -value of essentially Basak, S. , & Pavlova, A. (2013). Asset prices and institutional investors. American Eco-
zero. nomic Review, 103 , 1728–1758 .
Buckley, I. , Saunders, D. , & Seco, L. (2008). Portfolio optimization when asset returns
have the Gaussian mixture distribution. European Journal of Operational Research,
5. Conclusions 185 , 1434–1461 .
Büyük s¸ ahin, B. , & Robe, M. A. (2014). Speculators, commodities and cross-market
linkages. Journal of International Money and Finance, 42 , 37–80 .
In this paper we have investigated whether it is possible to find
Chen, X. , & Ludvigson, S. C. (2009). Land of addicts? An empirical investigation of
a SDF that jointly prices the cross-section of eight portfolios of habit-based asset pricing models. Journal of Applied Econometrics, 24 , 1057–1093 .
stocks, Treasuries, corporate bonds and commodities and replicates Cochrane, J. H. (2008). Asset pricing (Revised ed.). Princeton, N.J.: Princeton Univer-
sity Press .
the first four empirical moments of (especially, correlations among)
Daskalaki, C. , & Skiadopoulos, G. (2011). Should investors include commodities in
these assets. Importantly, besides being based on three through their portfolios after all? New evidence. Journal of Banking and Finance, 36 ,
ten principal components estimated from a large set of macroe- 2260–2273 .
Daskalaki, C. , Kostakis, A. , & Skiadopoulos, G. (2014). Are there common factors in
conomic indicators, our SDFs are further extended to include la-
commodity futures returns? Journal of Banking and Finance, 40 , 346–363 .
tent regime shifts governed by an ergodic and irreducible Markov De Roon, F. A. , & Szymanowska, M. (2010). The cross section of commodity futures
chain. returns . Erasmus University Working Paper .
We find that regime-switching models clearly outperform Dias, J. , Vermunt, J. , & Ramos, S. (2015). Clustering financial time series: New in-
sights from an extended hidden Markov model. European Journal of Operational
single-state ones both in term of statistical and pricing accuracy. Research, 243 , 852–864 .
However, while a four-state model is selected by standard infor- Dudley, W., & Hatzius, J. (20 0 0). “The Goldman Sachs financial conditions index: The
mation criteria, a two-state three-factor full VAR(1) model outper- right tool for a new monetary policy regime.”Goldman Sachs Global Economics
Paper No. 44.
forms all others as far as the pricing accuracy is concerned. Fi-
Erb, C. B. , & Harvey, C. R. (2006). The strategic and tactical value of commodity
nally, we notice that, although this model gives rather similar re- futures. Financial Analysts Journal, 62 , 69–97 .
sults to its single-state counterpart in terms of its ability to match Gorton, G. , & Rouwenhorst, K. G. (2006). “Facts and fantasies about commodity fu-
tures. Financial Analyst Journal, 62 , 47–68 .
sample moments, its Markov switching version outperforms the
Guidolin, M. , & Timmermann, A. (2006). An econometric model of nonlinear dy-
single-state model when the intra-commodity correlation are an- namics in the joint distribution of stocks and bonds returns. Journal of Applied
alyzed. This is not surprising because a literature has noticed that Econometrics, 21 , 1–22 .
Guidolin, M. (2011). Markov switching models in empirical finance. Advances in
the relationships of commodities with traditional assets classes has
econometrics, 27 , 1–86 .
changed over the last 15–20 years as a result of a so called “fi- Hamilton, J. D. (1994). Time series analysis . Princeton, NJ: Princeton University Press .
Hansen, L. P. (1982). Large sample properties of generalized method of moments
estimators. Econometrica , 1029–1054 .
13 Of course, resorting to such a commodity factor-based SDF poses some logical Hansen, L. P. , & Jagannathan, R. (1997). Assessing specification errors in stochastic
issues even though one the key points made by Bakshi et al. is that together, their
discount factor models. Journal of Finance, 52 , 557–590 .
three factors appear to also forecast economic growth, the returns of government
Jaga
e
n
x
n
p
a
e
th
ct
a
e
n
d
, R
re
. ,
t u
&
r n
W
s.
a
J
n
o
g
u
,
r n
Z
a
.
l
( 1
o
9
f
9
F
6
in
).
a n
T
c
h
e
e
, 5
c
1
o
,
n
3
d
–
it
5
io
3
n
.
al CAPM and the cross-section of
bonds and of equities. Note that Bakshi et al.’s paper is framed in terms of linear
Jensen, G. R. , Mercer, J. M. , & Johnson, R. R. (2002). Tactical asset allocation and
factor/regression representations and not in terms of a structural SDF estimation ex- commodity futures. Journal of Portfolio Management , 100–111 .
ercise. However, as explained in Cochrane (2008) , there is a clear one-to-one map- Koijen, R. S. J., Moskowitz, T. J., Pedersen, L. H., & Vrugt, E. B. (2013). “Carry”. Fama-
ping between linear factor representations and log-linear SDFs. Tabulated statistics Miller Center Working Paper.
for the time series of the three factors are available upon request. Note that our Lee, H. , & Yoder, J. (2007). A bivariate Markov regime switching GARCH approach to
analysis spans only half of the overall 1970–2011 sample employed by BGR in their estimate time varying minimum variance hedge ratios. Applied Economics, 39 ,
paper. 1253–1265 .

702 M. Giampietro et al. / European Journal of Operational Research 265 (2018) 685–702
Lombardi, M. , & Ravazzolo, F. (2016). On the correlation between commodity and Shiller, R. J. (1979). The volatility of long-term interest rates and expectations mod-
equity returns: Implications for portfolio allocations. Journal of Commodity Mar- els of the term structure. Journal of Political Economy, 87 , 1190–1219 .
kets, 2 , 45–57 . Szymanowska, M. , de Roon, F. A. , Nijman, T. E. , & Van den Goorbergh, R. (2012). An
Ludvigson, S. C. , & Ng, S. (2009). Macro factors in bond risk premia. Review of Fi- anatomy of commodity futures risk premia. Journal of Finance, 69 , 453–482 .
nancial Studies, 22 , 5027–5067 . Tang, K. , & Xiong, W. (2012). Index investments and the financialization of com-
Marroquìn Martinez, N. , & Moreno, M. (2013). Optimizing bounds on security prices modities. Financial Analyst Journal, 68 , 54–74 .
in incomplete markets. Does stochastic volatility specification matter? European White, H. (20 0 0). A reality check for data snooping. Econometrica, 68 , 1097–1126 .
Journal of Operational Research, 225 , 429–442 . Yang, F. (2013). Investment shocks and the commodity basis spread. Journal of Fi-
Pastor, L. , & Stambaugh, R. L. (2003). Liquidity risk and expected stock returns. Jour- nancial Economics, 110 , 164–184 .
nal of Political Economy, 111 , 642–685 .