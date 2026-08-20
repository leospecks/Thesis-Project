Journal of Monetary Economics 112 (2020) 41–56
Contents lists available at ScienceDirect
Journal of Monetary Economics
journal homepage: www.elsevier.com/locate/jmoneco
Commodity-price comovement and global economic activity
Ron Alquist a, Saroj Bhattarai b, Olivier Coibion b , c , ∗
a AQR Capital Management, Two Greenwich Plaza, Greenwich, CT 06830, United States
b University of Texas at Austin, 2225 Speedway, Austin TX 78712, United States
c National Bureau of Economic Research, 1050 Massachusetts Ave., Cambridge, MA 02138, United States
a r t i c l e i n f o a b s t r a c t
Article history: Guided by a macroeconomic model with endogenous commodity prices, we apply a new
Received 28 April 2016 factor-based identification strategy to decompose the historical sources of changes in com-
Revised 24 January 2019 modity prices and global economic activity. The model yields a factor structure for com-
Accepted 19 February 2019
modity prices and identification conditions that provide an economic interpretation: one
Available online 20 February 2019
factor captures the combined contribution of shocks that affect commodity markets only
JEL codes:
through general-equilibrium forces. Applied to a cross-section of commodity prices since
E3 1968, the theoretical restrictions are consistent with the data and yield structural inter-
F4 pretations of the common factors in commodity prices. Commodity-related shocks have
contributed modestly to global economic fluctuations.
Keywords: ©2019 Elsevier B.V. All rights reserved.
Commodity prices
Factor models
Business cycles
1. Introduction
Between January 2003 and July 2008, the prices of most major commodities grew rapidly: wheat by 120%, copper by
363%, aluminum by 100% and nickel by 138%. Many observers concluded that the simultaneous rise in prices across such
a broad cross-section of commodities reflected a common cause—an increase in the global demand for commodities due
to growth in emerging Asia and especially China. Other episodes of widespread comovement in commodity prices have
similarly suggested that global demand is a common source of movements in commodity prices, such as the early 1970s or
the late 1990s. But this explanation is not necessarily the only one: exogenous changes in the prices of oil and other energy
products could simultaneously drive the prices of many non-energy commodities because of the important role played by
transportation costs in their distribution. In addition, changing preferences on the part of consumers could shift the demand
for commodity-intensive products, as could technological changes that affect the relative importance of raw materials in the
production of consumption goods. Decomposing the sources of commodity price comovement is therefore inextricably linked
to identifying the sources of global business cycle fluctuations.
In this paper, we develop and implement a new methodology for decomposing the sources of commodity price comove-
ment and global business cycle fluctuations. Underlying this methodology is a general-equilibrium model of global business
cycles with commodities that predicts a factor structure for real commodity prices. The predicted factor structure decom-
poses the sources of global business cycle fluctuations and commodity price movements, and the theory suggests several
ways to recover a structural interpretation to the common factors extracted from commodity prices. In other words, this
∗ Corresponding author at: University of Texas at Austin, 2225 Speedway, Austin TX 78712, United States.
E-mail address: ocoibion@austin.utexas.edu (O. Coibion).
https://doi.org/10.1016/j.jmoneco.2019.02.004
0304-3932/©2019ElsevierB.V.Allrightsreserved.

42 R. Alquist, S. Bhattarai and O. Coibion / Journal of Monetary Economics 112 (2020) 41–56
methodology provides a way to use the comovement in commodity prices to disentangle the simultaneous determination
of commodity prices and business cycles.
The factor structure in commodity prices predicted by the model separates exogenous forces (or “shocks”) into two types.
The first set of shocks includes those that directly shift the supply and demand curves for commodities and thus would
affect commodity prices even in the absence of general-equilibrium changes in aggregate income, though such forces may
also have general-equilibrium effects on aggregate income and therefore additional indirect effects on commodity prices.
We refer to these factors as direct factors. They potentially reflect a variety of common shocks to the prices of inputs
used to produce commodities, such as labor or energy, common productivity shocks, or demand factors such as changes
in the relative need for commodities to produce final consumption goods. The second set of shocks includes those that
affect commodity prices only indirectly through their effects on aggregate output. We refer to these as indirect factors. The
indirect effects can come through two channels. One is the standard demand channel. When aggregate economic activity is
high, the demand for commodities used to produce the final good is also high, thereby raising the prices of all commodities.
The second is a supply-side channel. When aggregate income is high, agents may be less willing to supply the inputs used
to produce commodities because of income effects, thereby pushing up the prices of commodities. Both channels induce
positive comovement in the prices of commodities.
The theory predicts a new result about indirect shocks. Because their effects on commodity prices are summarized en-
tirely by their effects on aggregate output, each of the indirect shocks induces the same comovement among commodity prices .
As a result, their combined effect on commodity prices can be aggregated into a single factor. Furthermore, this factor has
a precise structural interpretation in the model. It corresponds to the counterfactual level of global economic activity that
would have been obtained without direct commodity shocks. Identifying this factor therefore provides a new way to recover
historical changes in global economic activity and commodity prices that reflect endogenous responses to non-commodity-
related shocks.
However, because standard empirical factor decompositions identify factors only up to a rotation, one cannot immediately
recover the indirect common factor from a simple factor decomposition of commodity prices. The second element of our
approach is to impose identification conditions, again grounded in the predictions of the theoretical model, to recover the
direct and indirect factors underlying commodity price movements. The theoretical model provides two ways to do this:
sign restrictions on factor loadings of the indirect common factor and orthogonality conditions with respect to a set of
instruments for either the direct or indirect factors. Using a cross-section of 40 non-energy commodity prices available
since 1968, we apply both identification strategies to identify the indirect factor and find similar results across specifications,
indicating that the results are robust to the choice of identification strategy and instruments.
Our main empirical finding is that the vast majority of historical commodity price movements are associated with the
indirect factor, i.e., broad-based changes in commodity prices can largely be attributed to a general-equilibrium response to
aggregate non-commodity shocks rather than direct shocks to commodity markets. While there are a number of historical
episodes during which direct shocks to commodity markets played some role in accounting for commodity price movements
and changes in global production (e.g., 1979–80, the run-up in commodity prices in the 20 0 0s and the decline in prices
in 2008–09), the primary source of commodity price movements is their endogenous response to non-commodity-related
shocks.
Our approach is related to the literature on the macroeconomic effects of shocks to oil and commodity prices ( Bosworth
and Lawrence 1982; Hamilton 1983; Barsky and Kilian 2002; Hamilton 2009; Blinder and Rudd 2012; Stuermer 2017 ) as
well as a growing body of recent research on identifying the sources of oil price movements following Kilian (2009) . We
differ from this line of research in that we focus on a broad range of non-energy commodities (rather than just oil), which
is essential to implement our identification strategy. Second, our identification strategy is new: we apply factor methods
that decompose the comovement across different commodity prices then exploit the predictions about this decomposition
from a microfounded model to identify the structural sources of fluctuations in commodity prices and aggregate output. 1
Third, while identification in VARs of commodity markets decomposes shocks into supply and demand shocks, our general-
equilibrium model allows for the fact that exogenous forces should tend to have both supply and demand effects.
Our model provides a structural interpretation of a factor representation for commodity prices along with the requisite
identification conditions, so that we are able to disentangle the different economic channels underlying commodity price
movements. In this respect, our approach is related to work that uses economic theory to assign factors an economic inter-
pretation (e.g. Forni and Reichlin 1998 ). Other work identifies the factors driving macroeconomic aggregates common to all
countries and specific subsets of countries ( Stock and Watson 2005 ; Kose et al., 2012 ). Factor methods have also been used
to identify relative price changes for specific goods and the absolute price changes common to all goods ( Reis and Wat-
son 2010 ) and the relative importance of aggregate and sector-specific shocks for U.S. industrial production ( Foerster et al.,
2011 ). Our paper differs from this line of research in that we use commodity price dynamics to identify the sources of global
1 We are not the first to apply factor methods to commodity prices. Some papers have examined whether there is excess comovement among unrelated
commodities—that is, price comovement in excess of what one would expect, conditional on macroeconomic fundamentals (e.g. Pindyck and Rotemberg
1990 ). Other papers have investigated the forecasting performance of the common factor in metals prices for individual metals prices ( West and Wong
2014 ) and commodity convenience yields for inflation ( Gospodinov and Ng 2013 ). But there has been little attempt at interpreting the resulting factors in
a structural sense.

R. Alquist, S. Bhattarai and O. Coibion / Journal of Monetary Economics 112 (2020) 41–56 43
business cycle fluctuations and in our identification strategy, which relies on the use of sign restrictions and orthogonality
conditions rather than zero restrictions on the factor loadings.
Finally, our factor-based method can help with forecasting commodity prices. Using recursive out-of-sample forecasts,
we find that a bivariate factor-augmented VAR with each commodity’s price and the first common factor extracted from the
cross-section of commodities generates improvements in forecast accuracy relative to the no-change forecast, particularly at
short horizons. This result extends to broader commodity price indices as well as real oil prices. An additional advantage
of our approach is that it relies only on commodity prices that can be readily updated at monthly or quarterly frequencies
and does not require information about production and inventory data that are often unavailable at these frequencies. Our
approach thus provides a unified framework to forecast commodity prices in real-time as well as a structural interpretation
of these forecasts.
The remainder of the paper is organized as follows. Section 2 presents a general-equilibrium business cycle model with
commodities and shows how the model can be used to assign a structural interpretation to the common factors in com-
modity prices. The section also shows how to recover the economic factors from typical factor decompositions through
identification restrictions. Section 3 applies these results to a historical cross-section of commodity prices. Section 4 uses
the indirect common factor in a recursive out-of-sample forecasting exercise. Section 5 concludes.
2. The sources of commodity price comovement: theory
In this section, we present a model that characterizes the sources of commodity price comovement. In particular, we
show that the model yields a tractable factor structure for a cross-section of commodity prices, which permits an economic
interpretation of the factors.
2.1. Model of commodity prices
The baseline model consists of households, an energy-producing sector, a continuum of heterogeneous primary com-
modities, a sector that aggregates these commodities into a single intermediate commodity input, and a final goods sector
that combines commodities, labor and technology into a final good.
2.1.1. The household
A representative consumer maximizes expected discounted utility over consumption (C ), labor supplied to the final good
sector ( N s ) and labor supplied to the energy sector ( N e ):
(cid:3) (cid:4)
max E t
(cid:2)
i =
∞
0 βi 1
C
t −
1
+
−
i
σ
σ −e −ε t n + i ϕ n
N
1 t
s
+ + i
1 +
η 1
η1
−ϕ e
N
1 t
e
+ + i
1 +
η 1
η1
w
an
h
d
e r
ϕ
e
e
β
>
i
0
s
,
th
w
e
e l
d
fa
is
r
c
e
o u
is
n
d
t
e
fa
c
c
re
to
a
r
s
.
i n
W
g
e
i n
re
h
fe
o
r
u
t
r
o
s
t
w
he
o r
t
k
w
ed
o t
i
y
n
p
e
e
i
s
t h
o
e
f
r
l a
s
b
e
o
c
r
to
a
r
s
. T
fi
h
n
e
a l
e
-g
ε t n
o o
t
d
er
s
m
la b
is
o r
a n
an
e
d
x o
e
g
n
e
e
n
rg
o
y
u
-
s
s p
s
e
h
c
o
i
c
fi
k
c
t
l
o
ab
t
o
h
r
e
. W
di
i
s
t
u
h
t i
ϕ
li
n
t y
>
o
0
f
hours worked in the final goods sector. 2
The household pays a price Pt for the consumption good, receives wage Wt for each unit of labor supplied to the final
goods sector and wage W
t
e for labor in the energy sector. The household also can purchase risk-free bonds Bt that pay a gross
nominal interest rate of Rt . The budget constraint is Pt Ct + Bt = B t −1 R t −1 + Wt N t s + W t e N t e + Tt where Tt represents payments
from owning firms.
2.1.2. The energy production sector
A representative energy firm produces a total supply of the energy good ( (cid:7) t ) subject to an exogenous energy-specific pro-
ductivity shock ( (cid:8) t ) and a decreasing returns production function that uses energy-specific labor ( N t d ,e ): (cid:7) t = (cid:8) t ( N t d ,e ) 1 −γ .
This representative firm takes the price of the energy good ( St ) as given and therefore chooses how much labor to hire to
maximize its profits which are given by St (cid:8) t ( N t d ,e ) 1 −γ −W t e N t d ,e . Equilibrium in the labor market for energy requires that
N
t
d ,e = N
t
e .
2.1.3. The primary commodity-production sector
There is a continuum of primary commodities of mass 1. Each primary commodity j is produced by a representative
price-taking firm which uses energy (cid:7) t (j) to produce an amount of the commodity Qt (j) using a decreasing returns in en-
ergy production function Qt (j) = At (j ) (cid:7) t (j ) 1 −α j where At (j ) is the exogenously determined level of productivity for com-
modity j. The value 1 −α
j
( 0 < α
j
< 1 ) determines the commodity-specific degree of diminishing returns to energy and is
in equilibrium equal to the ratio of firm j ’s expenditures on energy to its total revenues. Given the price of commodity j
Pt (j) and the price of energy St , the firm chooses the amount of energy input to maximize profits.
2 One could alternatively model the household as providing a single type of labor which can be used in both the final goods and energy sector. This
would not change the qualitative results. One could also introduce a preference shock to the household’s willingness to supply labor to the energy sector
but this would have the same qualitative effects as the productivity shock in the energy sector.

44  R. Alquist, S. Bhattarai and O. Coibion / Journal of Monetary Economics 112 (2020) 41–56
W e   a s su m e   t he   s t e a d y - st a te   le v e l   o f  pr o d u c ti v it y  A  ( j )   is   s u c h   t h a t   th e  s t(cid:5)e a d y - s t a te   level of production in each sector is

(cid:7)  = 1   (cid:7) (  )
equ al .  E q u il ibr i u m   i n   t h e  s u p p ly   a n d   d e m a n d  f o r  e n e rg y   r e q u i r e s  t h a t   t   0   t   j  d j .
2.1.4. The intermediate commodity
(j) of each primary commodity j and aggregates it into an intermediate com-
A perfectly competitive sector purchases Yt

| modity Q |  C using the Dixit-Stiglitz aggregator  |     |     |     |     |     |     |     |     |     |
| -------- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t
|     | (cid:6)  |               | (cid:8)        |     |     |     |     |     |     |     |
| --- | -------- | ------------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
|     | (cid:7)  |               | θ c            |     |     |     |     |     |     |     |
|     |          | 1  θcθ        |  −   θc  − 1   |     |     |     |     |     |     |     |
|     | Q  c  =  | Y t   ( j )   |  1 dj          |     |     |     |     |     |     |     |
|     | t        |               | c              |     |     |     |     |     |     |     |
0
θ
w h e re     i s   th e   e la st i c i ty   o f   s u b s t itu t i o n   a c r o s s   c o m m o d it i e s  a nd   t h e   p r ic e   o f  th e   in te rm e d i at e   c o m m o d i t y   a g g r eg a t e   i s
|     | c (cid:5) |            |                  |     |     |     |     |          |     |     |
| --- | --------- | ---------- | ---------------- | --- | --- | --- | --- | -------- | --- | --- |
|     |   =  (    | 1   ( )  1 |  − θ    )  − 1 θ |     |     |     |     | ( )  = ( | )   |     |
giv e n  b y   P   C       P t   j c d j  1 c  .  M a r k e t  c l e a r i n g   fo r  e ac h   c o m m o d i ty   s e c to r   j  re q u ir es  Q t   j  Y t    j  . T h is   s e t u p   i m p li c i tl y
|     | t   | 0   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
assumes that no storage of commodities takes place, since all commodities produced must be used in the same period. We
discuss the rationale for this assumption and its implications in more detail in Appendix I.
2.1.5. The final goods sector
A perfectly competitive sector combines purchases of the intermediate commodity good Y  C   and labor N  d   (at prices P  C
|     |     |     |     |     |     |     |             | t   | t   | t   |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
|     |     |     |     |     |     |     |  α t   1 −α | t   |     |     |
and Wt  respectively) according to the Cobb-Douglas production function Yt  = At  Y  C   N  d   to maximize profits, taking all
prices as given and where At  is an exogenously determined aggregate productivity process. 3  t t
Since all of the final good is
|     |     |     |     |     |     |     |     |     |  = N    = Y |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
purchased  by the household, equilibrium in the final goods market requires Ct  = Yt  as well as N  D  S and Q  C  C . The
|     | α   |     |     |     |     |     |     | t   | t   t   | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
fact that  t may be time-varying allows for exogenous variation in the relative demand for commodities and labor in the
production of the final good.
2.1.6. The linearized model
A detailed solution of the model is provided in Appendix A. We assume that exogenous processes are stationary around
their steady-state levels, so that all real variables are constant in the steady state. Lower-case letters denote log deviations
from steady state (e.g., ct  ≡log Ct  −log C¯ ), and we normalize the nominal variables by the price level of final goods (e.g.,
(j) ≡log Pt   (j ) / Pt  −log ( P (j ) /P ). We normalize commodity-specific productivity as v (j) ≡at   (j) ( 1 + (  ε θ )−  1 ) −1 ( 1 +  ε  − 1 )
| pt   |     |     |     |     |     |     | t   |     |   j  c  |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
j
to simplify the aggregation across commodities, where  ε   ≡( 1 −α ) /  α . 4  We assume that the productivity process for each
|     |     |     |     |     | j  j  j  |     |     |         |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | ------- | --- | --- |
|     |     |     |     |     |          |     |     | ( j)  + |     |     |
c o m m od i t y   s e c to r   h a s   a n   id i o s y n cr at ic   c o m p o n e n t  a n d   a  c o m m o n   c o m p o n e n t   s u c h   t h at  v t      =   v  a  v  j ,  w h i c h   i m p l ie s   th a t
|     |     |     |     | (cid:5) |     |     |     | t   | t   |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
 s      a  c s    v t   ≡ 1   v t  ( j)  d  =  v  a   .   i c  s   o   s
th e um o f p r o d u c t iv i t y c r o s s o m m o d i t ie is 0     j t   T h e d io s y n c r a t i c o m p o n e n t a r e rt h o g o n a l a cr o s c o m -
|     |     |     |  j     | ∀   |     | α   |     |     | α   |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
modity sectors, such that E[ v   v  k   ] = 0   j (cid:6) = k and E[ v t  ] = 0 . The log deviation of  t from its steady-state value of  is denoted
t t
by  α ˇt and similarly for (cid:8)ˇ. Each of the exogenous processes ( v t  , v  j  ,  α ˇt , (cid:8)ˇ t ,  ε  n   ) is stochastic, persistent, and assumed to be sta-
|     |     |     |     |     | t   | t   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tionary, but we do not need to otherwise specify the specific process followed by each. 5
As shown in Appendix 1, the aggregate level of production of final goods can be expressed in terms of exogenous forces:
|     | (cid:9)    |           |                   | (cid:10)       |     |     |     |     |     |      |
| --- | ---------- | --------- | ----------------- | -------------- | --- | --- | --- | --- | --- | ---- |
|     | =  ω       | +  δ ε    |  +  δ (cid:8)ˇ +  | δ +  δ α       |     |     |     |     |     |      |
|     | y t    y a | t   n   n |   (cid:8) t       | v v t   α ˇ t  |     |     |     |     |     | (1)  |
t
where  ω  y > 0 (as long as  σ > 1 ),  δ n > 0 ,  δ (cid:8)> 0 and  δ v > 0 : output rises with aggregate productivity as well as energy-
specific and commodity-specific productivity shocks. Whether output rises when the relative demand for commodities in-
creases ( ˇt ) depends on specific parameter values.  α
2.2. Comovement and the factor structure of commodity prices
As shown in Appendix 1, the supply of commodity j can be written in reduced form as:
|     | (  j ) ε | (  j ) | α α |  +  α (cid:8)ˇ α | α α  .  |     |     |     |     |     |
| --- | -------- | ------ | --- | ---------------- | ------- | --- | --- | --- | --- | --- |
p t    =    j y t    +  y y t   +  v v  a (cid:8) t  + +  αˇ ˇ t  +  v j  v  j (2)
|     |     |     |     | t   | t   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Because different commodities have different returns to energy in the production process, the slope of their supply curves
(given by  ε   j ) will generally differ. The supply curve of each commodity shifts up with increases in aggregate income yt
regardless of its source: greater aggregate production raises the price of energy and therefore the price of commodity j
α y > 0 ). The price of energy is higher when aggregate income rises because that higher income induces the household to
(
 e
reduce its supply of labor to the energy sector (which raises W t   and therefore the price of energy) and because higher
3  One could allow the final goods sector to also use energy in its production process without changing any of the qualitative results in the factor structure
of commodity prices.
4
The rescaling of the commodity-specific productivity process ensures that a 1% increase in productivity in each commodity sector raises the equilibrium
level of production of that commodity by equal amounts for each commodity. This would not be the case without the rescaling because each primary
commodity sector’s supply curve has a different slope.
5  Because we do not need to specify the specific time series process followed by each exogenous variable, we will frequently refer to these exogenous
variables as “shocks”with obvious abuse of terminology, instead of referring explicitly to the innovations that generate variation in each exogenous variable.

R. Alquist, S. Bhattarai and O. Coibion / Journal of Monetary Economics 112 (2020) 41–56  45
aggregate income implies a greater aggregate demand for energy which also causes the price of energy to rise. Hence,
any shock that affects aggregate income in this model is a supply shock from the point of view of a given commodity. In
addition, productivity shocks in the commodity sector or productivity shocks to the energy sector will induce an additional
shift of the supply curve, holding constant their effect on aggregate production, as will shocks to the relative demand for
commodities (which affect energ y prices and therefore change cost of producing commodities). Hence, these shocks have a
direct effect on the supply of commodities, above and beyond the general equilibrium effects that all shocks have on supply
via their effects on aggregate income.
The demand for commodity j can similarly be written in reduced form as:
|     | (  j ) |  = − | 1  (  j )  +  | β +     | β v v  a  +  | β (cid:8)ˇ +  | β α .  |      |
| --- | ------ | ---- | ------------- | ------- | ------------ | ------------- | ------ | ---- |
|     | p t    |      | θ y t         | y y t   |              | (cid:8) t     | α ˇ t  | (3)  |
|     |        |      | c             |         | t            |               |        |      |
Given the setup of the model, all commodities have the same elasticity of demand. In addition, all commodities expe-
β y > 0 ) which simply reflects
rience a rise in demand from an increase in aggregate production, regardless of its source (
the role of commodities as an input into the production of final goods. This term therefore captures general-equilibrium
demand effects, and all macroeconomic shocks that affect aggregate production in the model result in an equal upward or
downward shift in the demand for each commodity. Thus, all shocks in the model other than idiosyncratic shocks are both
demand and supply shocks. However, in addition to these general-equilibrium shifts in commodity demand, the demand
for commodity j rises with changes in the relative demand for commodities ( ˇt ), holding aggregate output constant. It also  α
shifts, holding aggregate output constant, with exogenous common commodity productivity shocks (which increase the de-
mand for all commodities on the part of the final goods sector) and exogenous shocks to energy (which affect the relative
demand for all commodities).
As can be seen from the supply and demand curves above, there are two aggregate shocks that affect aggregate output
ε  n
but do not directly impact commodity prices other than through general equilibrium effects on output: at  and    . We will
t
refer to these variables as “indirect” shocks that affect commodity prices only through their general equilibrium effects on
output. It’s helpful to decompose movements in output coming from these variables vs other exogenous forces:
|     |           |             |             | (cid:9)        |             |        | (cid:10) |     |
| --- | --------- | ----------- | ----------- | -------------- | ----------- | ------ | -------- | --- |
|     |           | c (         | ε  ) ω      | δ (cid:8)ˇ     | δ  +        | δ α    |          |     |
|     | y t   = y |  n    a t   | ,   n    +  |  y  (cid:8) t  | +  v v  a   | α ˇ t  |          |     |
|     |           | t           | t           |                | t           |        |          |     |
|     | c =       | ω           | δ ε         |                |             |        |          |     |
where y  n  y [ at  +  n   n ] is the level of aggregate output coming exclusively from changes in aggregate productivity and
|     | t   |     | t   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
changes in the willingness of households to supply labor to the final goods sector.
As shown in Appendix A, we can then rewrite the equilibrium price of commodity j as
|     |              | λ           |   ε                          | λ (cid:8)               | λ                   | λα        | α 1    (                                       |     |
| --- | ------------ | ----------- | ---------------------------- | ----------------------- | ------------------- | --------- | ---------------------------------------------- | --- |
|     | p t   (  j ) |  =  y       | y  n c  (  a (cid:13)t    ,  |  n  )   +               | (cid:8)ˇ t  +  v    |  v  a  +  | ˇ (cid:14)t  − v   j  j  )                     |     |
|     |              | (cid:11) j  | t   (cid:12)                 | t  (cid:14) (cid:11) j  | (cid:12) j(cid:13)  | t   j     | θ t                                            |     |
|     |              |             |                              |                         |                     |           |   (cid:11)  c   (cid:12) (cid:13)   (cid:14)   |     |
|     |              |             | indirect ( IC )              |                         | direct ( DC )       |           | idiosyncratic                                  |     |
j
|     |     | =  λ j F | t   +  ξ |     |     |     |     | (4)  |
| --- | --- | -------- | -------- | --- | --- | --- | --- | ---- |
t
∂λ(cid:8)
|        | λy  > 0 and ∂( 1 − |     | j      | < 0 when  | σ > 1 and  | θ   | ( 1 −α) −1 > 0 .  |     |
| ------ | ------------------ | --- | ------ | --------- | ---------- | --- | ----------------- | --- |
| where  | j                  |     | α j )  |           |            |     | c                 |     |
Eq. (4) provides a factor structure for real commodity prices with three distinct and orthogonal components. 6  The last
term on the right-hand side reflects idiosyncratic shocks to commodity j that have no aggregate real effects. The second
set of terms on the right-hand side consist of a factor for each exogenous force that has both direct and indirect effects on
the commodity market (i.e., that shifts the supply or demand for commodities, holding aggregate output constant, but also
ultimately leads to changes in aggregate output). For this reason, we refer to these factors as “direct common” (DC)factors.
In this setup, there are three such factors: exogenous shocks to energy sector, a common productivity shock to commodities,
and a shock to the relative demand for commodities in the production of final goods. Because these forces have both direct
and indirect effects on the market for commodity j , there is, in general, no guarantee that their respective loadings have
the same signs across commodities. However, it should be the case that commodities which are more intensive in energy
(larger  α j ) should have prices which respond more strongly to exogenous energy price shocks.
The most interesting component of the factor structure is the first term on the right-hand side of (4) , which reflects
the combined contribution on the price of commodity j from all shocks whose effects on commodity prices operate only
indirectly through aggregate output (i.e., only through general-equilibrium effects). We refer to this common factor as the
“indirect common”(IC) factor. It captures the fact that, because some shocks affect commodity markets only through changes
in aggregate output, they all have identical implications for the price of a given commodity, conditional on the size of their
effect on aggregate output, and induce the same comovement across different commodity prices. As a result, they can be
represented as a single factor. Furthermore, this factor has a well-defined interpretation: it is the counterfactual level of
6  The differences in factor loadings across commodities in Eq. (4) stem only from differences in slopes of commodity supply curves, which are them-
selves a reflection of the different energy intensities of production across commodities. Appendix 2 considers a version of the model where industrial and
agricultural commodities are aggregated into two different intermediate commodity bundles, both of which are used in final production, but in which the
aggregation occurs with different elasticities of substitution. The factor structure is preserved, even though commodities now differ in both the slopes of
their supply curves as well as their demand curves. This alternative representation of the model also illustrates that the aggregation of shocks underlying
the factor structure of commodity prices does not hinge on the use of CES aggregation of all commodities into a single commodity intermediate input.

46  R. Alquist, S. Bhattarai and O. Coibion / Journal of Monetary Economics 112 (2020) 41–56
global output that would have occurred in the absence of any direct commodity shocks . Thus, this common factor represents a
way to reconstruct the counterfactual history of aggregate output without direct commodity shocks, as well as to decompose
historical commodity price changes into those components reflecting direct commodity shocks versus all other aggregate
economic forces captured by the IC factor. Unlike the DC factors, another key characteristic of the IC factor is that all the
loadings on this factor must be positive (  λy > 0  ∀  j). This prediction reflects the fact that the shocks incorporated in the IC
j
factor raise commodity demand when the shock is expansionary and simultaneously restrict the commodity supply through
income effects, which unambiguously increases commodity prices. 7
In short, this factor decomposition provides a new way
to separate causality in the presence of simultaneously determined prices and production levels.
2.3. Recovering a structural interpretation of the factors
A key limitation of factor structures is that, empirically, factors are identified only up to a rotation. For example, if one
estimated a factor structure on commodity prices, one could not directly associate the extracted factors with the structural
interpretation suggested by (4) . However, the theory developed in this section has implications that can be used to identify
the unique rotation consistent with those predictions and permits us to assign an economic interpretation to the factors
driving commodity prices.
To see this, suppose that, as in the theory above, the N variables in vector Xt  ( N by 1) of real commodity prices have
| a factor structure Xt  = L Ft  +  |     |     |     | ε   |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t  where Ft  is a K by 1 vector of unobserved variables, and L is an N by K matrix of factor
|     |     |     |     | ε   |     | ϕ   |     | ε i be cov (ε) = diag(  | ϕ ) = (cid:17) | ε   |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | -------------- | --- |
loadings. Let the variance of    i be given by    i and the covariance matrix of      i  such that the    i ’s
are uncorrelated with one another. We make the typical assumptions underlying factor analysis: (a) E(F ) = 0 , (b) E(  ε ) = 0 ,
  i
(c) E( F  ε ) = 0 and (d) cov (F ) = I, so that the factors are orthogonal to one another and have variance normalized to one.
  i
(cid:7) + (cid:17). The identification problem is that for
Then, letting (cid:7)≡cov (X) be the covariance matrix of X , it follows that (cid:7)= LL
|     |     |     |     |     |     | (cid:7) = I, we can define L˜  = LT and F˜ |     | (cid:7)  |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | -------- | --- | --- |
any K by K orthogonal matrix T such that T T  t   = T  Ft  such that Xt  = L˜  F˜ t   +  ε t  . As a result, an
empirical estimate of the factors underlying Xt  does not, in general, permit the economic identification of the factors Ft  but
| rather some rotation F˜ |     |     | t   .  |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
However, the model provides additional restrictions on the factor structure that can be used to assign an economic in-
|     |     |     |     |     |     |     | factors Ft  from the estimated factors F˜ |     | t   . For example, consider the  |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | -------------------------------- | --- |
terpretation to the factors and identify the “structural”
factor structure of Eq. (4) in Section 2.2 in which real commodity prices reflect two underlying factors, an exogenous en-
| ergy shock ( (cid:8)ˇ |     |     |     |     |     |     |     |     |     | c   |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t ) and the level of aggregate production that would have occurred in the absence of this shock ( y  n   ), thus
|     | (cid:7) = [ y |     | (cid:7)  |     |     |     |     |     |     | t   |
| --- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Ft  = [ F  1   F  2   ]   n c (cid:8)ˇ t ]  . As we discuss below, this two-factor structure is the most empirically relevant case. A factor de-
|     | t   t   | t   |     |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
composition of co mmodity p rices would  yield a rotation o f these factors F˜ t   such that
|     |       | (cid:15)              |                 | (cid:16)        | (cid:15) |        | (cid:16)               |          |     |     |
| --- | ----- | --------------------- | --------------- | --------------- | -------- | ------ | ---------------------- | -------- | --- | --- |
|     |       |                       |                 | (cid:7) (cid:9) | (cid:10) |        | (cid:9)                | (cid:10) |     |     |
|     |       |                       |                 |                 | (cid:7)  | θ      | θ                      | (cid:7)  |     |     |
|     | = T   | (cid:7)  F˜ t    =  t |   11   t   12   |   F˜   1   F˜   |   2   =  | co s   | s in   F˜   1   F˜   2 |          |     |     |
|     | F t   |                       |                 |                 |   −      | θ      | θ                      |          |     |     |
|     |       | t                     |   2 1   t   2 2 |   t             | t        | si n   | c o s   t t            |          |     |     |
where the last equality reflects the properties of rotation matrices. Recovering the “structural” factors Ft  corresponds to
(cid:7)
| identifying the parameter  |     |     | θ   | and the rotation matrix T such that Ft  = T  |     |     |     | F˜ t   .  |     |     |
| -------------------------- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --------- | --- | --- |
The theory imposes three types of conditions that can be used to identify  θ . The first is that y  n c  (the IC factor) is or-
t
thogonal to commodity-related shocks (DC factors). Therefore, if one had a S by 1 vector of instruments zt  that is correlated
with the energy shocks (cid:8)ˇ  n c   n c  zt  ] = 0 . The conditions can be
|               |                 |                                                 | t , the orthogonality of y |             |                   | t      | would deliver S moment conditions E[ y |     | t   |      |
| ------------- | --------------- | ----------------------------------------------- | -------------------------- | ----------- | ----------------- | ------ | -------------------------------------- | --- | --- | ---- |
| rewritten as  |                 | (cid:9)(cid:17)                                 |                            |             | (cid:18) (cid:10) |        |                                        |     |     |      |
|               |  n c            | t  ] = E                                        | F˜   1                     | θ+ F˜   2   | θ                 | = 0 .  |                                        |     |     |      |
|               | E [y  t   z     |                                                 | t   cos                    | t   sin     | z t               |        |                                        |     |     | (5)  |
|               | If S = 1, then  | θ would be uniquely identified. If S > 1, then  |                            |             |                   |        | θ                                      |     |     |      |
is overidentified, and one could estimate it using generalized
method of moments (GMM) by writing the moment conditions as
|     | J ( θ)  = E [y  |  n c  |               |  n c  (cid:7)   |     |     |     |     |     |      |
| --- | --------------- | ----- | ------------- | --------------- | --- | --- | --- | --- | --- | ---- |
|     |                 | t   z | t  ]W   E [y  | t   z t  ]      |     |     |     |     |     | (6)  |
θˆ = argmin J(θ) . Letting W be the inverse of the variance-covariance matrix
where W is a weighting matrix, such that
θ
associated with the moment conditions, standard GMM asymptotic results apply, including standard errors for  and tests
of the over-identifying conditions for N and T large enough for the factors to be considered as observed variables rather
than generated (e.g., Stock and Watson 2002; Bai and Ng 2002 ).
A second approach would be to make use of the theoretical prediction that y  n c  is a linear combination of exogenous
t
variables that have only indirect effects on the commodity sector such as the productivity shocks or labor supply shocks
considered in the model. If one had a S by 1 vector of instruments zt  for each period correlated with one or more of these
 2   zt  ] = 0 . As in the
exogenous drivers, then another set of orthogonality conditions imposed by the theory would be E[ F t
θ
previous case, one could estimate  using GMM, given these orthogonality conditions, and test over-identifying restrictions
if S > 1.
7
The prediction that all commodities have the same sign loading on the common factor is sensitive to the assumption of diminishing returns to scale
in production of commodities, which generates upward-sloping supply curves. Downward sloping supply curves (coming from increasing returns) would
imply that when global production is high, the increased demand would now reduce commodity prices (since supply slopes down), while the income
effect would raise it (as before). Whether commodity prices went up would therefore depend on the relative strengths and slopes of each effect.

R. Alquist, S. Bhattarai and O. Coibion / Journal of Monetary Economics 112 (2020) 41–56 47
In both of these cases, the econometrician must take a stand on whether the chosen instruments should be correlated
with commodity-related shocks or with y
t
n c . While economic theory may provide clear guidance in some cases, this choice
may be problematic when one is interested in whether an exogenous variable affects commodities only through general-
equilibrium effects or more directly. Within our framework, this question amounts to whether the exogenous variable should
be considered part of y
t
n c or one of the commodity-related shocks. For example, in the case of commodity prices, monetary
policy shocks could potentially have direct effects on commodity markets in the presence of storage motives but would
otherwise not be expected to have direct effects on commodity markets if the speculative channel is absent or sufficiently
small, as discussed in Appendix I.
be p
A
o
t
s
h
it
i
i
r
v
d
e
a
(
p
si
p
n
r
c
o
e
a c
λ
h
y
i
>
s t
0
o
∀
m
j
a
i
k
n
e
E
u
q
s
.
e
( 4
o
)
f
) .
s
L
ig
e
n
tt i
r
n
e
g
s t
L˜
r ic
b
t
e
i o
t
n
h
s
e
o
N
n
b
t
y
h e
2
l
m
oa
a
d
t
i
r
n
ix
g s
o
.
f
T
u
h
n
e
r o
th
ta
e
t
o
e
r
d
y
f
p
a
r
c
e
to
d
r
ic
l
t
o
s
a
t
d
h
i
a
n
t
g s
th
, t
e
h
l
e
o a
ro
d
t
i
a
n
t
g
e
s
d
o
o
n
r
y
“ t
n
s
c
t r
m
uc
u
t
s
u
t
r a
a
l
l
”
l
j
I
lo
m
a
p
d
o
in
si
g
n
s
g
a
t
r
h
e
a
L
t
=
al l
L˜ T
o f
=
t h
[ L
e
˜ 1
e
L˜
l e
2 ]
m
T
e
.
n
T
t
h
s
e
o
l
f
o a
L
d
1
in
b
g
e
s
p
o
o
n
s it
t
i
h
v
e
e
fi
w
rs
o
t
u
r
ld
o t
t
a
h
te
e
d
re
f
f
a
o
c
r
t
e
o r
c o
(
r
c
r
o
e
r
s
r
p
e
o
sp
n
o
d
n
t
d
o
i n
id
g
e
t
n
o
t i
y
f t
n
y
c
i
)
n g
a r
t
e
h
t
e
h
r
e
a
n
n
L
g
1
e
=
of
L ˜
v
1
a
c
l
o
u
s
e
θ
s
+
of
L˜
θ
2 s
s
i
u
n
c
θ
h
.
that min ( L˜ 1 cos θ+ L˜ 2 sin θ) > 0 . In general, this leads only to a set of admissible values of θ and associated rotation matrices
without uniquely identifying the rotation matrix. This approach is conceptually similar to the set identification of VARs by
sign restrictions ( Uhlig, 2002 ).
In short, the theoretical model of commodity prices yields not only a factor structure for commodity prices but also a set
of conditions that can be used to identify (or, in the case of sign restrictions, limit the set of) the rotation matrix necessary
to recover the underlying factors. Furthermore, the factors have economic interpretations. The IC factor corresponds to the
level of production and income net of commodity-related shocks, while other factors correspond to one or more of these
commodity-related shocks. The identification of the rotation matrix, and thus the underlying economic factors, follows from
orthogonality conditions implied by the model, as well as sign restrictions on the loadings predicted by the theory. The
implied factor structure of the model combined with the ability to recover an economic interpretation of the factors thus
provides a new method for separating fluctuations in aggregate output into those driven by commodity-related shocks and
those driven by non-commodity-related shocks.
3. The sources of commodity price comovement: empirical evidence
In this section, we implement the factor decomposition of real commodity prices suggested by the theory. We first
construct a historical cross-section of real commodity prices for the commodities that conform to the theoretical structure
of the model along several dimensions. We then implement a factor decomposition and identify the factors suggested by
the theory. After considering a wide range of robustness checks, we argue that commodity-related shocks have contributed
only modestly to fluctuations in global economic activity.
3.1. Data
Guided by the theoretical model, we use four criteria to decide which commodities to include in the data set and which
to exclude. First, commodities must not be vertically integrated. 8 Second, the main use of commodities must be directly
related to the aggregate consumption bundle, and they should not be primarily used for the purposes of financial specula-
tion. 9 Third, commodities must not be jointly produced. 10 Finally, the pricing of commodities must be determined freely in
spot markets and must not display the price stickiness associated with the existence of long-term contractual agreements. 11
Applying these criteria leaves us with 40 commodities in the sample. It includes 22 commodities that we refer to as
agricultural or food commodities, five food oils, and 13 industrial commodities (see Appendix C for a detailed list). We
compiled monthly data from January 1957 to January 2013 (as available) from a number of sources, including the CRB
Commodity Yearbooks, the CRB InfoTech CD, the World Bank GEM Commodity Price Data, the IMF’s Commodity Price Indices
and the U.S. Bureau of Labor Statistics. While most of the data are consistently available from January 1968 until January
2013, in some cases, there are a number of missing observations in the underlying data, as well as periods when we treat the
8 Vertically integrated commodities would introduce the possibility of price comovement resulting from idiosyncratic shocks to one commodity affecting
prices in other commodities through the supply chain. For example, an exogenous shock to the production of sorghum would affect the price of non-grass-
fed beef because sorghum is primarily used as feed. Thus, this shock could ultimately affect the price of milk and hides as well.
9 Some commodities, such as precious metals, have long been recognized as behaving more like financial assets than normal commodities ( Chinn and
Coibion 2014 ). Thus, we exclude gold, silver, platinum and palladium from the cross-section of commodities.
10 Some commodities are derivative products of the production of other commodities. This is particularly the case for minerals, which are commonly
recovered during the mining for metal commodities, making the assumption of orthogonal productivity shocks clearly inapplicable. We drop any such
commodities.
11 While many commodities have long been traded on liquid international spot markets, this is not always the case. For example, the price measure of
tung oil tracked by the Commodity Research Bureau (CRB) Commodity Yearbooks varies little over time and is often fixed for periods lasting as long as one
year. Because we want to focus on commodities whose prices reflect contemporaneous economic conditions, we exclude commodities such as tung oil that
systematically display long periods of price invariance. For some commodities in the sample, prices were not determined in flexible markets until much
later than others; for these commodities, we treat early price data as missing values. For mercury, the reverse is true, since its use has declined over time
and its price began to display long periods with no price changes starting in 1995. We treat its prices after March 1995 as missing. Appendix B provides
more details on these adjustments.

48 R. Alquist, S. Bhattarai and O. Coibion / Journal of Monetary Economics 112 (2020) 41–56
Table 1
Contribution of common factors to commodity prices.
Number of Common Factors: Cumulative variance explained by common factors
1 2 3 4 5
Complete Sample:
Cumulative eigenvalue shares 0.59 0.69 0.75 0.79 0.82
Mean across commodity-specific R 2 s 0.60 0.69 0.74 0.78 0.81
Median across commodity-specific R 2 s 0.70 0.76 0.78 0.84 0.85
R 2 across all commodities 0.62 0.71 0.75 0.79 0.82
Subset of Commodities:
R 2 across agricultural/food commodities 0.64 0.72 0.75 0.77 0.80
R 2 across oils 0.72 0.74 0.76 0.82 0.85
R 2 across industrial commodities 0.55 0.68 0.75 0.80 0.83
Notes : The table provides metrics of the cumulative variance associated with using additional factors, as
indicated by each column. The first row provides the cumulative sum of eigenvalues associated with each
factor normalized by the sum of all eigenvalues. The second row provides the mean across the R 2 of each
commodity for each given factor, using the specific sample associated with each commodity. The third row
provides the median R 2 across all commodity-specific R 2 s. The fourth row provides the joint R 2 constructed
using all commodities. In addition, the top panel presents joint R 2 s for subsets of commodities (as defined
in Table 1). Each R 2 omits imputed values. See Section 3.2 for details.
available data as missing because spot trading was limited. Appendix C provides details on the construction of each series,
their availability and any periods over which we treat the data as missing because of infrequent price changes. Furthermore,
while we can construct price data going back to at least 1957 for many commodities, we restrict the empirical analysis to
the period since 1968, in light of the numerous price regulations and government price support mechanisms in place during
the earlier period. 12
3.2. Common factors in commodity prices
Before conducting the factor analysis, we normalize each price series by the U.S. CPI, take logs of all series and nor-
malize each series by its standard deviation. Because there are missing observations in the data, we use the expectation-
maximization (EM) algorithm of Stock and Watson (2002) . 13 We follow Kilian (2009) in focusing on the (log) level of real
commodity prices but document in our robustness checks that our results are qualitatively unchanged if we take the first
difference of real commodity prices or use linearly detrended series.
We consider several metrics to characterize the contribution of the first five factors in accounting for commodity price
movements, summarized in Table 1. 14 The first row presents the sum of eigenvalues associated with each number of factors
normalized by the sum across all eigenvalues, a simple measure of variance explained by common factors. In addition, we
present additional metrics based on R 2 s that explicitly take into account missing values associated with some commodities:
the average across the individual R 2 s computed for each commodity, the median across these same commodity-specific
R 2 s, the R 2 constructed across all commodities. The key result from this table is that the first common factor explains a
large share of the price variation across commodities, ranging from 60% to 70% depending on the specific measure used. In
contrast, all of the additional factors explain smaller percentages of the variance in commodity prices. The second factor, for
example, accounts for between 6% and 10%, while the third factor contributes another 5% of the variance. Thus, the first two
factors jointly account for approximately 70–75% of the variance in commodity prices. 15
The ability of the first two factors, and the first common factor in particular, to account for so much of the variance
holds across commodity groups. Table 1 includes the contribution of different factors to explaining the variance across the
three subsets of commodities in the sample—agricultural/food, oils and industrials. Differences across subsets of commodities
are quite small: the contribution of the first factor ranges from 55% (pooled R 2 across all commodities in this subset) for
industrial commodities to 64% for agricultural/food commodities and 72% for oils (see Appendix E for commodity-specific
results). The decomposition does not suggest that one needs different factors for different types of commodities. This point
is worth stressing because a common concern with factor analysis is that different factors are needed to explain different
subsets of the data. As illustrated in Table 1 , this is not the case for these commodities.
12 Appendix D provides detail on the geographic variation in where commodities are produced and how they are used.
13 Specifically, we first demean each series and replace missing values with zeroes before recovering the first K factors. We use these K factors to impute
the value of missing observations, and then do the factor analysis again, iterating on this procedure until convergence. We use K = 5 factors for the
imputation; however, the results are not sensitive to the specific number of factors used.
14 Following Connor and Korajczyk (1993) and Bai and Ng (2002) , we use principal components on the variance-covariance matrix of commodity prices
to estimate the approximate factors.
15 Statistical tests of the number of factors point toward parsimonious factor specifications. For example, the PC2 and IC2 criteria of Bai and
Ng (2002) each select one factor. The same result is obtained using the test suggested by Onatski (2010) or the two criteria proposed in Ahn and Horen-
stein (2013) .

R. Alquist, S. Bhattarai and O. Coibion / Journal of Monetary Economics 112 (2020) 41–56 49
Table 2
GMM estimates of the rotation matrix.
GMM estimates of rotation parameter Implied rotation coefficients
θ se( θ) p (over-id) N t 11 95% CI( t 11 ) t 21 95% CI( t 21 )
Baseline GMM Estimates: −0.10 (0.31) 1.00 505 1.00 [0.75 1.00] −0.10 [ −0.65 0.49]
(Iterative GMM, L = 36)
Robustness of GMM Estimates:
More moments: ( L = 48) −0.15 (0.27) 1.00 493 0.99 [0.77 1.00] −0.15 [ −0.63 0.39]
Fewer moments: ( L = 24) −0.13 (0.35) 1.00 517 0.99 [0.67 1.00] −0.13 [ −0.73 0.54]
Fewer moments: ( L = 12) −0.23 (0.50) 1.00 529 0.97 [0.32 1.00] −0.23 [ −0.94 0.69]
Two-step GMM −0.10 (0.31) 1.00 505 1.00 [0.75 1.00] −0.10 [ −0.65 0.47]
Continuous GMM −0.07 (0.31) 1.00 505 1.00 [0.76 1.00] −0.07 [ −0.62 0.52]
Alternative normalization −0.08 (0.31) 1.00 505 1.00 [0.75 1.00] −0.08 [ −0.64 0.50]
Notes : The table presents nonlinear GMM estimates of parameter θ from Eq. (7) in the text, along with Newey and
West (1987) standard errors (se( θ)), the p -value for over-identifying restrictions ( p (over-id)), and the number of obser-
vations used in the estimation ( N ). The panel on the right presents the implied parameters of the first row of the rota-
tion matrix, along with the 95% confidence interval implied from the estimated distribution of θ. The baseline estimates
are based on iterative GMM until convergence, using a constant as well as the contemporaneous value and 36 lags of
OPEC production shocks for moment conditions. Subsequent rows present robustness to using more or fewer lags of OPEC
production shocks as moment conditions, a two-step GMM procedure, a continuously updated GMM procedure and an
alternative normalization of moment conditions. See Section 3.3 for details.
3.3. Identification of the rotation matrix and the underlying economic factors
To implement a structural interpretation of the factors as suggested by the model, we interpret the results of Table 1 as
indicating that a two-factor representation adequately characterizes the data. First, additional factors beyond the first two
add relatively little in explanatory power and can be omitted. Second, under the null of the model, it is a priori unlikely
for there to be fewer than two factors. Indeed, such a finding would imply that there are no shocks that directly affect
commodity prices and that all movements in commodity prices reflect either the level of aggregate economic activity or id-
iosyncratic commodity factors. We can rule this possibility out immediately because there exists at least one common shock
to the supply of commodities: exogenous energy price movements. Because commodities require energy in production and
distribution, exogenous shocks to energy prices necessarily induce some comovement in commodity prices, as commodities
are produced in different parts of the world but consumption occurs disproportionately in advanced economies, thereby
generating significant shipping and distribution costs.
S
o
p
f
e
t
T
c
h
o
i
e
fi
e
c
K
a
s
i
t
l
l
l
i
i
y
m
a
,
n
a
w
t
(
e
e
2 0
t
t
h
0
a
e
8
k
)
e
r o
s
ε
e
t
t
a
o
r
p
t
ie
e
io
c
s
,
n
a
t
n
m
h
d
e
a t
d
m
r
e
ix
e
fi
a
,
n
s
o
e
u
u
r
t
r
e
h
b
e
o
a
f
o
s
r
e
O
t
l
h
P
in
o
E
e
g
C
o
is
n
p
a
r
t
o
l
o
i
d
t y
u
im
c
c
t
p
o
io
o
n
n
s
d
e
i
s
ti
h
o
o
r
o
n
t
c
h
s
k
o
s
a
g
s
o
f r
n
E
o
a
[
m
F
l
t
i
1
t
z
y
B
t
a
]
c
,
s
o
t
w
n
ia
d
h
n
i
e
i
t
n
r
i
e
o n
a
z
n
s
t
d
≡
o n
M
[ 1
t
a
h
n
ε
e
e
t o p
r
i
e
a
n
c
’
d
s
.
i
.
r
(
.
e
2
c
ε
0
t
t o
1
− p
4
c
e L
)
o
c ]
m
u
i
p
m
s
d
t
o
a
h
n
t
e
e d
f
v
a
e
c
v
c
t
e
o
t
r
o
r
s
r
i
F
o
t
o
1
n
f
.
instruments that consists of a constant, the contemporaneous value of the production shock series as well as L lags of the
shock. The IC factor F
t
1 ( y
t
n c in the model) is a rotation over the two estimated factors Fˆ
t
1 and Fˆ
t
2 , i.e., F
t
1 = t
11
Fˆ
t
1 + t
21
Fˆ
t
2 wher
θ
e
the orthogonal rotation parameters t
11
and t
21
can be expressed as a function of a single underlying rotation parameter
such that t
11
= cos θ and t
21
= sin θ . Given that there are more moment conditions ( L + 2) than parameters ( θ ), we can
estimate the rotation parameter
θ
using GMM by minimizing
J(θ)
:
(cid:15) (cid:16) (cid:15) (cid:16)
J ( θ) =
T
1
(cid:2) (cid:17)
F
t
1 ( θ)z
t
(cid:18)
W
T
1
(cid:2) (cid:17)
F
t
1 ( θ)z
t
(cid:18) (cid:7)
(7)
t t
We set L = 36 months for the baseline estimation to capture the fact that the OPEC production shocks have long-lived
effects on commodity prices, although the results are robust to both shorter and longer lag specifications as well, as we
document below. W is the Newey-West (1987) heteroskedasticity and autocorrelation HAC robust estimate of the inverse
of the variance-covariance matrix of moment conditions. We iterate over minimizing
J(θ)
and then computing the implied
weighting matrix until the estimate of θ has converged ( W = I in the first step). Table 2 presents the resulting estimate of
θ and its associated standard error. With θˆ = −0 . 10 and a standard error of 0.31, we cannot reject the null hypothesis that
θ=
0. From this estimate of
θ
, we construct estimates of the rotation parameters t
11
and t
21
: t
11
is close to 1, and we cannot
reject the null hypothesis that t
21
= 0 , so the estimated rotation matrix is not statistically different from the identity matrix.
Furthermore, the over-identification conditions cannot be rejected.
The reason why the estimated rotation matrix is close to the identity matrix is that, while the first unrotated factor
is largely uncorrelated with OPEC production shocks, this condition is not satisfied for the second unrotated factor, which
responds strongly to OPEC production shocks. Because the unrotated factors are already largely consistent with the theoret-
ically predicted orthogonality conditions (namely, that the first factor is orthogonal to oil shocks, but the second is not), the
estimation procedure yields only a slight rotation of the original factors.
While the fact that we cannot reject the over-identifying conditions is consistent with the theory, we can further assess
the extent to which the estimated rotation satisfies the theoretical predictions of the model. For example, an additional
theoretical prediction is that the loadings on the indirect factor will all be the same sign. To assess this prediction, we

50  R. Alquist, S. Bhattarai and O. Coibion / Journal of Monetary Economics 112 (2020) 41–56
Table 3
Rotated commodity-specific factor loadings.
| Commodity              | Factor loadings  |                         | Factor loadings  |
| ---------------------- | ---------------- | ----------------------- | ---------------- |
|                        | IC  DC           | Commodity               | IC  DC           |
| Agr./Food Commodities  |                  | Oils                    |                  |
| Apples                 | 0.46  0 .13      | Coconut oil             | 0.82  0. 02      |
| Bananas                | 0.57  0 .22      | Groundnut oil           | 0.86  0. 13      |
| Barley                 | 0.75  0 .41      | Palm oil                | 0.89  0. 13      |
| Beef                   | 0.87  −0 .09     | Rapeseed oil            | 0.53  0. 39      |
| Cocoa                  | 0.89  −0 .12     | Sun/Safflower oil       | 0.83  0. 22      |
| Coffee                 | 0.85  −0 .17     |                         |                  |
| Corn                   | 0.95  0 .09      | Industrial Commodities  |                  |
| Fishmeal               | 0.91  0 .15      | Aluminum                | 0.80  0. 05      |
| Hay                    | 0.86  −0 .04     | Burlap                  | 0.85  −0. 00     |
| Oats                   | 0.88  0 .11      | Cement                  | 0.21  0. 06      |
| Orange juice           | 0.74  −0 .22     | Copper                  | 0.60  0. 69      |
| Onions                 | 0.53  −0 .39     | Cotton                  | 0.92  −0. 20     |
| Pepper                 | 0.56  −0 .62     | Lead                    | 0.73  0. 58      |
| Potatoes               | 0.73  −0 .05     | Lumber                  | 0.53  −0. 23     |
| Rice                   | 0.93  0 .09      | Mercury                 | 0.46  0. 75      |
| Shrimp                 | 0.44  −0 .75     | Nickel                  | 0.20  0. 74      |
| Sorghums               | 0.95  0 .08      | Rubber                  | 0.79  0. 45      |
| Soybeans               | 0.95  0 .02      | Tin                     | 0.90  0. 18      |
| Sugar                  | 0.78  0 .11      | Wool                    | 0.87  0. 16      |
| Tea                    | 0.87  −0 .22     | Zinc                    | 0.60  0. 36      |
| Tobacco                | 0.84  −0 .33     |                         |                  |
| Wheat                  | 0.92  0 .13      |                         |                  |
Notes : The table presents the rotated loadings from factor analysis using the GMM esti-
mates of the rotation matrix. See Section 3.3 for details.
present in Table 3 the estimated factor loadings for each rotated factor. The loadings on the IC factor are positive for all
commodities, as predicted by the theory. In contrast, the loadings on the commodity-related factor are of mixed signs.
There are no systematic patterns across commodity groups, again confirming that the factors explaining commodity prices
are common across commodity subsets. Without imposing any restrictions on the loadings as part of the identification
strategy for the rotation matrix, we find that the estimated rotation satisfies theoretical predictions on the factor loadings
and those implied by the over-identifying restrictions. 16
| θ   |     |     |     |
| --- | --- | --- | --- |
Given the estimate of  and the rotation matrix, we construct the rotated factor F  1   that, according to the model, corre-
t
sponds to the level of aggregate output and income that would have occurred in the absence of commodity-related shocks.
λ= 129,600, the typical value
This factor is presented in Fig. 1 , after being detrended with a Hodrick-Prescott (HP) filter with
for monthly data, to highlight variation at business cycle frequencies. In addition, we draw from the estimated distribution
of  θ , construct F  1   for each new draw and use this distribution to characterize the 99% confidence interval of the HP-filtered
t
factor.
This factor displays a sharp rise in 1973–74 before falling sharply during the 1974–75 recession in the United States. This
drop is followed by a progressive increase over the course of the mid- to late 1970s, with the factor peaking in 1979 before
falling sharply during each of the “twin” recessions of 1980–82, and then rebounding sharply after the end of the Volcker
disinflation. Thus, over the course of the 1970s, this structural factor displays a clear cyclical pattern. During the mid-1980s,
the factor drops sharply before rebounding in the late 1980s, and then falls gradually through the 1990–91 U.S. recession
before rebounding through the mid-1990s. It experiences a large decline in the late 1990s, before the 20 0 0–01 U.S. recession
and then rebounds shortly thereafter. After a brief decline in the mid-20 0 0s, the factor displays a sharp increase from 2005
to 2008, the period when many commodity prices boomed, and then falls sharply in late 2008 and 2009 before rebounding
strongly in 2010. In short, there is a clear procylical pattern to the IC factor relative to U.S. economic conditions.
3.4. Robustness of the estimation
θ
To assess the sensitivity of our results, we vary some of the specific choices made for the estimation of  . For example,
we report in Table 2 results from using fewer moment conditions ( L = 12 and 24 months) as well as more moment condi-
tions ( L = 48 months). Neither changes the estimates significantly. Similarly, we repeat the GMM estimates using a two-step
16  The model developed in Section 2 also predicts that commodities that are more energy intensive in production have larger (in absolute value) loadings
on the DC factor. Using the 2007 benchmark input-output tables to characterize energy intensity of production for 13 commodity groupings (which jointly
include 34 of the commodities in our cross-section), we find a positive relationship between the loadings and the energy intensity of production. These
results are reported in Appendix K. This suggestive evidence is consistent with the model’s predictions and lends credibility to the framework we use to
characterize the common variation in commodity prices. Unfortunately, the input tables are not sufficiently detailed to allow us to test this prediction for
a more differentiated set of commodities.

R. Alquist, S. Bhattarai and O. Coibion / Journal of Monetary Economics 112 (2020) 41–56 51
Panel A: Indirect Common Factor (GMM Approach)
5
4
3
2
1
0
-1
-2
-3
-4
-5
1970 1975 1980 1985 1990 1995 2000 2005 2010
Panel B: Indirect Common Factor (Factor Loading Sign Restrictions)
5
4
3
2
1
0
-1
-2
-3
-4
-5
1970 1975 1980 1985 1990 1995 2000 2005 2010
naeMmorf.veD.dtS
US Recessions 99% CI for Rotated Common Factor (GMM) Min and Max Values for Rotated Common Factor (Factor Sign Restrictions
Fig. 1. Indirect common factor in commodity prices.
Notes : The figure in Panel A presents the IC factor from the factor analysis in Section 3.3 . The IC factor is HP-filtered ( λ= 129,600) in the figure. The
light grey shaded areas are recessions dated by the National Bureau of Economic Research. The dark grey shaded areas are 99% confidence intervals of
HP-filtered rotated factors constructed from the estimated distribution of rotation parameters. The figure in Panel B plots the 99% confidence interval of
the IC factor as estimated by GMM (shaded areas), and the minimum and maximum range for admissible values of the IC factor using sign restrictions on
factor loadings (solid blue lines). See Section 3.3 for details. (For interpretation of the references to color in this figure legend, the reader is referred to the
web version of this article.)

52 R. Alquist, S. Bhattarai and O. Coibion / Journal of Monetary Economics 112 (2020) 41–56
θ
procedure, in which is first estimated using a weighting matrix equal to the identity matrix with no subsequent iterations
θ
after updating the weighting matrix, and second using a continuously updated GMM in which we minimize over and W
jointly until convergence. In both cases, the results are qualitatively similar. Finally, because non-linear GMM can be sen-
sitive to normalizations, we replicate the baseline estimation after rewriting moment conditions as E[ ( Fˆ t 1 + Fˆ t 2 c s o in s θ θ ) zt ] = 0 ,
and the results are again unchanged. 17
A more interesting robustness check is to consider the alternative identification strategy suggested in section 2.3 , namely
to exploit the theoretical predictions for signs of factor loadings: loadings on the IC factor should all be positive. Thus, one
can characterize the set of admissible rotation matrices by restricting them to be consistent with the sign restrictions im-
θ
plied by the theory, in the spirit of Uhlig (2002) . In our case, this procedure consists of identifying the set of such that
min ( L˜ 1 cos θ+ L˜ 2 sin θ) > 0 , where L˜ i for i = {1, 2} are the loading vectors associated with the unrotated factors and min is
with respect to the elements of L 1 . We consider values of θ ∈ [ −π, π ] (at increments of 0.001) and, for each θ , determine
whether the restriction is satisfied. This yields a set of admissible rotation matrices and therefore a set of possible IC factors.
We apply the HP filter to each of these and plot the resulting minimum and maximum values for each month in Panel B of
Fig. 1 , along with the 99% confidence interval for the rotated IC factor from the baseline GMM estimation. There is signifi-
cant overlap between the two approaches, with the minimum and maximum values from the sign restriction typically being
within the 99% confidence interval of the GMM-estimated IC factor. Thus, despite the fact that the two identification strate-
gies are quite different, they point toward a remarkably consistent characterization of the non-commodity-related structural
factor.
In Appendix F, we provide a number of additional robustness checks on these results. For example, we replicate our
results dropping either all commodities whose primary use is as food or as feed, or those commodities disproportionately
produced in the U.S.S.R., China or India through much of the sample. We verify that our results are robust to alternative
assumptions about stationarity and find similar results using first differences or linearly detrended real commodity prices
(Appendix G). We also find little sensitivity to dropping commodities for which imputation was needed or to decomposing
the correlation matrix rather than the covariance matrix for the factor analysis.
3.5. Factor contributions to commodity prices, comovement and global real activity
We now turn to using the factor structure to better understand the historical sources of commodity price movements
and global real activity. For prices, we decompose the average annual percentage change in commodity prices into the com-
ponents driven by indirect and direct common factors. The decomposition follows directly from the rotated factor structure,
yielding
(cid:17) (cid:18) (cid:17) (cid:18) (cid:17) (cid:18)
p t −p t −12 = λ IC F t I C −F t I − C 12 + λ DC F t D C −F t D − C 1 2 + ε t −ε t −12
where the bar denotes averages across all commodities in the cross-section. The first term on the right-hand side of the
equation represents the contribution of the IC factor to average commodity price changes, the second represents the contri-
bution of the DC factor, and the third reflects average idiosyncratic effects. The results of this decomposition are presented
in the top panel of Fig. 2 , in which we plot the contributions from the IC and DC factors each month as well as the actual
annual average price change across commodities. The IC factor, which captures the endogenous response of prices to non-
commodity shocks, explains the vast majority of historical commodity price changes. To the extent that income effects on
inputs into the production of commodities are likely weak, the IC factor can be interpreted as primarily reflecting changing
demand for commodities due to changes in global economic activity. During the commodity boom of 1973–74, for example,
indirect shocks to commodity markets accounted for almost all of the rise in commodity prices, with the remainder reflect-
ing direct commodity-related shocks. Every other historical episode of large changes in average commodity prices is also
accounted for by the indirect factor, i.e., as an endogenous response of commodity prices to global business cycle conditions
not driven by commodity-related shocks.
We can also quantify how changes in each factor have contributed to the time variation in comovement among commod-
ity prices. Specifically, we can decompose, each month, annual changes in real commodity prices as follows:
(cid:9) (cid:10) (cid:9) (cid:10)
p t ( j ) −p t −12 ( j ) = λI j C F t I C −F t I − C 12 + λD j C F t D C −F t D − C 1 2 + ε t j −ε t j − 12
From this, we can construct each month the cross-sectional R 2 coming from both factors (i.e., the ability of changes in
both factors to explain commodity price movements through common forces) as well as the partial R 2 coming from the
IC factor. These series are plotted in Panel B of Fig. 2 . There is significant variation over time in the overall comovement
of commodity prices, as captured by both factors, with the highest degrees of comovement in commodity prices occurring
between 1973 and 1975, in the early to mid-1980s, in the late 1990s, and in the mid- to late 20 0 0s continuing to 2013.
The time variation in comovement is again primarily explained by changes in the indirect factor. Periods in which com-
modity prices co-move most strongly have also been periods in which commodity price changes have been driven by the
endogenous response of commodity prices to non-commodity shocks.
17 While we rely on standard asymptotics which apply for large N and T, adjusting standard errors to account for smaller N would only strengthen the
main result that one cannot reject the null that the estimated rotation matrix is not different from the identity matrix.

R. Alquist, S. Bhattarai and O. Coibion / Journal of Monetary Economics 112 (2020) 41–56 53
Panel A:Contributions to Average Annual Commodity Price Changes
1
0.8
0.6
0.4
0.2
0
-0.2
-0.4
-0.6
-0.8
-1
1969 1973 1977 1981 1985 1989 1993 1997 2001 2005 2009 2013
Panel B:Contributions to Comovement in Commodity Price Changes
Panel C:Contributions to Annual Changes in Global Industrial Production
etaRhtworGlaunnA
Contribution of DC Factor Contribution of IC Factor Average Annual Commodity Price Change
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0
-0.1
1970 1975 1980 1985 1990 1995 2000 2005 2010
segnahcecirpraey-1fos2RgnilloR
Total contribution of factors
Contribution of indirect factor
0.15
0.1
0.05
0
-0.05
-0.1
-0.15
1971 1975 1979 1983 1987 1991 1995 1999 2003 2007
etaRhtworGlaunnA
Contribution of DC Factor Contribution of IC Factor Annual Growth in World IP
Fig. 2. The contribution of indirect and direct factors to changes in commodity prices.
Notes : Panel A plots the contributions of the direct and indirect factors (DC and IC, respectively) to the average annual price changes across all commodities.
Panel B plots the contribution of the two factors to cross-sectional variation in 1-year commodity price changes (black line) and that coming solely from IC
factor (blue shaded area). See Section 3.4 for details. Panel C plots the equivalent contributions to the annual growth rate of global industrial production.
(For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

54 R. Alquist, S. Bhattarai and O. Coibion / Journal of Monetary Economics 112 (2020) 41–56
We now assess the contribution of each factor to global economic activity, using the global industrial production (IP)
constructed by Baumeister and Peersman (2013) from 1947Q1 until 2010Q4.
Unlike with commodity prices, the factor structure does not immediately lend itself to a decomposition of historical
changes in global industrial production. To do so, we first rely on the theory presented in Section 2 in which the IC factor
corresponds to the level of global activity that would have occurred in the absence of direct commodity shocks ( y
t
n c ). Because
the scale of the IC factor is not identified, we normalize it such that the standard deviation of quarterly changes in the IC
is equal to the standard deviation of quarterly percent changes in global IP and treat the resulting historical changes in the
IC as the contribution of indirect shocks to global IP. The difference between the demeaned quarterly growth rate of global
IP and the demeaned change in the IC (defined as δ t ≡(cid:19)yt −(cid:19)y t n c ) should reflect the contribution of direct commodity
shocks, potentially omitted factors, and mismeasurement in global production levels. To evaluate the contribution of direct
commodity shocks to global IP, we regress δ t on 4 lags of itself and 8 lags of the direct commodity factor ( F t D C ) at a quarterly
frequency and construct the contribution of the DC factor to global IP net of the contribution of the IC factor. This approach
leaves a component of global activity unaccounted for, potentially reflecting measurement error, omitted variables or model
misspecification.
We plot the resulting contributions of the IC and DC factors to global IP growth in Panel C of Fig. 2 , again showing only
the annual changes to filter out the high-frequency variation in the measurement of global IP. The correlation between the IC
factor and global IP is high (0.59) so that historical changes in global IP are primarily attributed to indirect non-commodity
shocks. This is particularly true from the early 1970s through the mid-1980s, although commodity-related shocks deepened
the decline in global IP during late 1974 and early 1975. As was the case with the decomposition of commodity prices,
the decline in economic activity during the Volcker disinflation is accounted for by the IC factor. The dynamics of global
activity from the late 1980s to mid-1990s are also largely attributed to the IC factor, although actual changes in global
IP exceeded those predicted by the two factors. Growth in the IC factor during the 20 0 0s also coincides with the growth
in global IP during this time period, while commodity-related shocks in the DC contributed modest downward pressure
on economic activity in 2002 and 2003, then again in 2007–10. To the extent that the DC factor reflects exogenous energy
price fluctuations, the negative contribution of the DC factor from late 2007 through 2010 (subtracting 1–2% from the annual
growth rate of global IP) is broadly consistent with Hamilton (2009) , who argues that oil price shocks contributed to the
severity of the Great Recession of 2007–09. Nonetheless, most of the decline in the growth rate of global IP from late 2007
to the depth of the recession can be attributed to declines in the IC factor.
4. Forecasting applications
We examine whether the IC factor contains real-time information relevant for predicting commodity prices, broad com-
modity price indices and the price of oil in a recursive out-of-sample forecasting exercise. The forecasting model is a
monthly linear bivariate FAVAR( p ) model for the real price of commodity j and the IC factor. 18 The lag length p is cho-
sen recursively using the BIC. We assess the ability of the IC factor to forecast the 40 individual real commodity prices used
to compute the IC factor, three widely used real commodity price indices—the CRB spot index, the World Bank non-energy
index and the IMF non-fuel index –and the real price of oil. 19 The forecast performance of the FAVAR is evaluated over two
periods. One is commodity-specific and begins either in January 1968 or at the earliest possible date subject to the condi-
tion that the initial estimation window contains at least 48 observations. The second one begins in January 1984 and ends
in December 2012, with the initial estimation window ending in December 1983. We evaluate the recursive mean-squared
prediction error (MSPE) of the FAVAR-based forecast at the 1-, 3-, 6-, and 12-month horizons. All forecast accuracy compar-
isons are conducted relative to the no-change benchmark. Multiple step-ahead forecasts are computed iteratively using the
FAVAR.
Table 4 summarizes the results obtained from the forecasting exercise for the commodity-specific and common sample
periods. A summary measure across all commodities is given by the Aggregate M SP E Ratio ≡
(cid:19)
(cid:19) N j=
N j=
1
1
M
M
SP
SP
E
E
F j A
R j
V
W
A R where M SP E F
j
AVAR
is the mean-squared prediction error of the FAVAR-based forecast for commodity j; MSP E RW is the mean-squared prediction
j
error of the random walk forecast for commodity j.
For both the commodity-specific and the common forecast evaluation periods, forecasts based on a common factor gen-
erate improvements in forecast accuracy between 2% and 8% relative to the no-change forecast up to the 6-month horizon.
The FAVAR-based forecasts improve on the no-change forecast for most commodities at short-horizons but performance
deteriorates over longer horizons. 20 The FAVAR does best at predicting the World Bank non-energy index and the IMF
18 Because we are unable to reject the null that the rotation matrix equals the identity matrix in Section 3 , we use the unrotated first factor in the
forecasting exercises.
19 The IMF non-fuel commodity price index begins in February 1980. The price index was backcast to January 1957 using the IMF agricultural raw
material, beverage, food and metals sub-indices with weights obtained from regressing the non-fuel index on the individual sub-indices. The real price of
oil is the U.S. refiner’s acquisition cost of imported oil. All variables are deflated by U.S. CPI. We apply the EM algorithm recursively to fill in the missing
observations.
20 Appendix J provides commodity-specific results. FAVAR-based forecasts generate improvements in forecast accuracy for some agricultural commodities
and oils up to 12 months ahead. For the common sample period, 10 (out of 15) of the agricultural commodities and 2 (out of 3) oils achieve improvements

R. Alquist, S. Bhattarai and O. Coibion / Journal of Monetary Economics 112 (2020) 41–56 55
Table 4
Summary of recursive forecast accuracy diagnostics for real commodity prices.
Forecast Evaluation Period: Commodity-Specific
Aggregate MSPE Ratio Distribution of MSPE Ratios
[0,0.9) [0.9,0.95) [0.95,1) [0,1) [1, ∞ ) CRB WB IMF Crude Oil
1 month 0.921 10 11 11 32 8 0.974 0.834 0.874 0.805
3 months 0.922 4 5 11 20 20 1.057 1.023 0.990 0.977
6 months 0.938 5 4 4 13 27 1.127 1.125 1.072 1.143
12 months 1.096 5 6 5 16 24 1.187 1.214 1.155 1.324
No. of commodities 40 24 (15) 39 (17) 45(17)
Forecast Evaluation Period: January 1984—December 2012
Aggregate MSPE Ratio Distribution of MSPE Ratios
[0,0.9) [0.9,0.95) [0.95,1) [0,1) [1, ∞ ) CRB WB IMF Crude Oil
1 month 0.931 8 7 8 23 5 0.964 0.863 0.888 0.790
3 months 0.944 7 5 6 18 10 0.991 0.982 0.928 0.951
6 months 0.985 8 3 3 14 14 1.068 1.106 1.008 1.114
12 months 1.106 9 2 5 16 12 1.128 1.256 1.112 1.314
No. of commodities 28 24 (15) 39 (17) 45 (17)
Notes : For the commodity-specific forecast evaluation period, the initial estimation window depends on the commodity. It begins either in January
1968 or at the earliest date that allows the initial estimation window to contain at least 48 observations. The maximum length of the recursive
sample is restricted by the end of the data sample for each commodity and the forecast horizon. The “Aggregate MSPE Ratio”is the ratio of the sum
of the MSPEs for the bivariate FAVAR forecasts of the real commodity prices relative to the sum of the MSPEs for the no-change forecast. The MSPE
ratios of the individual forecasts of real commodity prices are also computed relative to the benchmark no-change forecast. For the FAVAR-based
forecasts, the lag length is chosen recursively using the BIC. The number of commodities included in the commodity price indices but not in the
cross-section of 40 commodities used to extract the factor is in parentheses.
non-fuel index, with improvements in forecast accuracy up to 17% over short horizons. It also delivers significant improve-
ments relative to the random walk at predicting real oil prices at short horizons. 21
These findings show that the prices of internationally traded commodities are forecastable in a way suggested by the
model presented in Section 2 . Improvements in forecast accuracy can be economically important at short horizons, and
agricultural commodities and oils tend to be more predictable than industrial commodities. Thus, the factor structure in
commodity prices serves a dual purpose for policy-makers and practitioners: it both provides a structural decomposition of
the forces driving commodity prices and helps forecast commodity price fluctuations.
5. Conclusion
We propose a new empirical strategy, grounded in a microfounded business cycle model with commodities, to identify
the driving forces of global economic activity and commodity prices. The model provides a set of orthogonality conditions
and sign restrictions that can be used to identify the parameters of the rotation matrix that yield a structural interpretation
of the common factors behind commodity prices, with the “indirect” factor representing the counterfactual level of global
economic activity that would have occurred without direct shocks to commodity markets. The IC factor we identify accounts
for about 60–70% of the variance in commodity prices, and we cannot reject the theoretical restrictions implied by the
model. Its behavior during the 1970s and 1980s suggests that the macroeconomic fluctuations observed during that era were
not driven primarily by commodity-related shocks. Nevertheless, there are episodes during which the direct commodity
shocks contributed negatively to global economic activity, particularly in the early 1990s and during the Great Recession.
The IC factor can also be used to forecast real commodity prices, some commonly used commodity price indices and
the real price of crude oil with a bivariate FAVAR in real-time. Because our identification strategy relies only on commodity
prices themselves, it can be implemented for commodities for which market fundamentals are unavailable in real time. In
sum, we provide a new conceptual framework for identifying the sources and implications of commodity price comovement
and its relationship to global macroeconomic conditions.
in forecast accuracy at the 12-month horizon. The improvements in forecast accuracy in the industrial commodities are concentrated at shorter horizons
(i.e., 1- and 3-months).
21 Additional results on the ability of the commodity price factor to forecast the real price of oil are in Appendix Table J.3. It compares the bivariate
FAVAR with a VAR model of the global oil market that performs well at forecasting the real price of oil out of sample ( Baumeister and Kilian 2012; Alquist
et al. 2013 ). The FAVAR model based on the IC factor does well relative to the oil market VAR model at the 1- and 3-month horizons when the BIC is used
but it is dominated by the VAR model when a fixed lag length of 12 is used, although the IC factor model still delivers improvements in forecast accuracy
up to about 14% relative to the no-change forecast.

56 R. Alquist, S. Bhattarai and O. Coibion / Journal of Monetary Economics 112 (2020) 41–56
Acknowledgments
For helpful comments, the authors are grateful to Yuriy Gorodnichenko, Lance Bachmeier, John Baffes, Olivier Blanchard,
John Bluedorn, Zeno Enders, Julian di Giovanni, Lutz Kilian, Peter Nagle, Serena Ng, Hashem Pesaran, Martin Stuermer, Ben-
jamin Wong and Choongryul Yang; seminar participants at the Bank of France; the Bundesbank; the Board of Governors of
the Federal Reserve System; the Centre for Applied Macro and Petroleum Economics conference “Oil and Macroeconomics”;
the European Central Bank; the Norges Bank; the Toulouse School of Economics; UC Irvine; the Federal Reserve Banks of
Dallas, Minneapolis and San Francisco; the Reserve Bank of Australia; the Reserve Bank of New Zealand; the FEEM con-
ference “Oil and Commodity Price Dynamics”; and the Barcelona GSE Summer Forum. Data for the project were kindly
provided by Andrea Bastianin, Christiane Baumeister, Lutz Kilian and the trade associations of the aluminum (EEA), copper
(ICSG), tin (ITRI) and nickel (INSG) industries. The paper was previously distributed under the title “Commodity Price Co-
movement: Sources and Implications” while Alquist was at the Bank of Canada and Coibion was a visiting scholar at the
International Monetary Fund. The support of both organizations is greatly appreciated. AQR Capital Management is a global
investment management firm that may or may not apply similar investment techniques or methods of analysis described
in this paper. The views expressed in the paper are authors’ and should not be interpreted as reflecting the views of AQR
Capital Management, the Bank of Canada, or the International Monetary Fund.
Supplementary materials
Supplementary material associated with this article can be found, in the online version, at doi: 10.1016/j.jmoneco.2019.
02.004 .
References
Ahn, S.C. , Horenstein, A.R. , 2013. Eigenvalue ratio test for the number of factors. Econometrica 81 (3), 1203–1227 .
Alquist, R. , Kilian, L. , Vigfusson, R. , 2013. Forecasting the price of oil. In: Elliott, G., Timmermann, A. (Eds.), Handbook of Economic Forecasting. North-Hol-
land, Amsterdam .
Bai, J. , Ng, S. , 2002. Determining the number of factors in approximate factor models. Econometrica 70, 191–221 .
Barsky, R.B. , Kilian, L. , 2002. “Do we really know that oil caused the great stagflation? A monetary alternative. In: Bernanke, B., Rogoff, K. (Eds.), Proceedings
of the NBER Macroeconomics Annual 2001, pp. 137–183 May 2002 .
Bastianin, A. , Manera, M. , 2014. “How does stock market volatility react to oil shocks? In: Proceedings of the FEEM Working Paper No. 70.2014 .
Baumeister, C. , Kilian, L. , 2012. Real-time forecasts of the real price of oil. J. Bus. Econ. Stat. 30 (2), 326–336 .
Baumeister, C. , Peersman, G. , 2013. The role of time-varying price elasticities in accounting for volatility changes in the crude oil market. J. Appl. Econom.
28 (7), 1087–1109 .
Blinder, A.S. , Rudd, J.B. , 2012. “The supply shock explanation of the great stagflation revisited. The Great Inflation: The Rebirth of Modern Central Banking
NBER .
Bosworth, B.P. , Lawrence, R.L. , 1982. Commodity Prices and the New Inflation. The Brookings Institution, Washington D.C .
Chinn, M. , Coibion, O. , 2014. The predictive content of commodity futures. J. Futures Mark. 34 (7), 607–636 .
Connor, G. , Korajczyk, R.A. , 1993. A test for the number of factors in an approximate factor model. J. Finance 48 (4), 1263–1291 .
Foerster, A. , Sarte, P.G. , Watson, M. , 2011. Sectoral versus aggregate shocks: a structural factor analysis of industrial production. J. Polit. Econ. 119 (1), 1–38 .
Forni, M. , Reichlin, L. , 1998. Let’s get real: a factor analytical approach to disaggregated business cycle dynamics. Rev. Econ. Stud. 65 (3), 453–473 .
Gospodinov, N. , Ng, S. , 2013. Commodity prices, convenience yields, and inflation. Rev. Econ. Stat. 95 (1), 206–219 .
Hamilton, J.D. , 1983. Oil and the Macroeconomy since World War II. J. Polit. Econ. 91 (2), 228–248 .
Hamilton, J.D. , 2009. Causes and consequences of the oil shock of 2007-2008. Brook. Pap. Econ. Act. 2009 (2), 215–259 .
Kilian, L. , 2008. Exogenous oil supply shocks: how big are they and how much do they matter for the U.S. economy? Rev. Econ. Stat. 90 (2), 216–240 .
Kilian, L. , 2009. Not all oil price shocks are alike: disentangling demand and supply shocks in the crude oil market. Am. Econ. Rev. 99 (3), 1053–1069 June
2009 .
Kose, M.A. , Otrok, C. , Prasad, E. , 2012. Global business cycles: convergence or decoupling? Int. Econ. Rev. 53 (2), 511–538 .
Newey, W.K. , West, K.D. ,1987. A simple,positive semi-definite,heteroskedasticity and autocorrelation consistent covariance matrix. Econometrica 55 (3),
703–708 .
Onatski, A. , 2010. Determining the number of factors from empirical distribution of eigenvalues. Rev. Econ. Stat. 92 (4), 1004–1016 .
Pindyck, R.S. , Rotemberg, J.J. , 1990. The excess comovement of commodity prices. Econ. J. 100 (403), 1173–1189 .
Reis, R. , Watson, M.W. , 2010. Relative goods’ prices, pure inflation, and the phililips correlation. Am. Econ. J. Macroecon. 2 (July), 128–157 .
Stock, J. , Watson, M.W. , 2002. Macroeconomic forecasting using diffusion indexes. J. Bus. Econ. Stat. 20, 147–162 .
Stock, J. , Watson, M.W. , 2005. Understanding changes in international business cycle dynamics. J. Eur. Econ. Assoc. 3 (5), 968–1006 .
Stuermer, M. , 2017. Industrialization and the demand for mineral commodities. J. Int. Money Finance 46, 16–27 .
Uhlig, H. , 2002. What are the effects of monetary policy on output? Results from an agnostic identification procedure. J. Monet. Econ. 52 (2), 381–419 .
West, K.D. , Wong, K. , 2014. A factor model for comovements of commodity prices. J. Int. Money Finance 42, 289–309 .