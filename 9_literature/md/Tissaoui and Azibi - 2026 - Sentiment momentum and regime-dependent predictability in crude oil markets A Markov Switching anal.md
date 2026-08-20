International Review of Economics and Finance 108 (2026) 105197
Contents lists available at ScienceDirect
International Review of Economics and Finance
journal homepage: www.elsevier.com/locate/iref
Sentiment momentum and regime-dependent predictability in
crude oil markets: A Markov Switching analysis with higher-order
VIX and MOVE derivatives
Kais Tissaouia,* , Nadia Azibib
aManagement Information Systems Department, Applied College, University of Ha'il, P.O. Box 2440, Hail City, Saudi Arabia
bDepartment of Health Management, College of Public Health and Health Informatics, University of Ha'il, P.O. Box 2440, Hail City, Saudi Arabia
A R T I C L E I N F O A B S T R A C T
Keywords: This paper uses higher-order derivatives of the VIX and MOVE indices, more especially, their
Crude oil returns velocity, acceleration, and jerk, as indicators of sentiment momentum to examine the predictive
Sentiment momentum ability of dynamic financial fear sentiment on crude oil returns. To understand the system-
VIX and MOVE derivatives
dependent nature of oil market dynamics, we examine the impact of sentiment derivatives on
Regime-sensitive modelling
crude oil returns under stable and turbulent conditions using the Markov Switching Regression
Stable regime
Volatile regime (MSR) framework. Our empirical study, which uses daily data from 2002 to 2025, shows that
sentiment velocity (VIX_V, MOVE_V) and acceleration (VIX_A, MOVE_A) have significant pre-
dictive value for oil returns under stable market conditions. However, their predictive effec-
tiveness decreases under high volatility conditions, supporting the information saturation
hypothesis. Comparing derivatives with fixed sentiment levels reveals a better continuous model
fit and early warning signals for increased volatility. The results show the asymmetric and
nonlinear flow of fear from financial markets to commodity markets, highlighting the need to
incorporate mood momentum into forecasting models. Robustness checks, incorporating out-of-
sample prediction tests, macro-financial control variables (DXY, GPR), and Fourier-based sea-
sonal components, confirm the stability of these results. The sentiment momentum remains the
dominant driver of regime-dependent return dynamics, with seasonal and cyclical patterns
contributing little explanatory power. Compared with stationary sentiment levels, derivative-
based measures consistently deliver superior model fit and earlier signals of transitions into
high-volatility regimes. The evidence highlights the asymmetric and nonlinear transmission of
fear from financial to commodity markets, emphasizing the need to incorporate mood momentum
into forecasting frameworks. Policymakers can use sentiment acceleration as a leading indicator
to change communication or intervention timing in macroeconomics sensitive to energy con-
sumption; risk managers can include sentiment velocity into real-time monitoring systems to
optimize hedging strategies.
1. Introduction
Crude oil is a key commodity for economic growth and financial development (Zaghdoudi et al. (2023); Charles & Darn´e, 2017).
* Corresponding author.
E-mail address: k.tissaoui@uoh.edu.sa(K. Tissaoui).
https://doi.org/10.1016/j.iref.2026.105197
Received 14 August 2025; Received in revised form 8 December 2025; Accepted 1 April 2026
Available online 4 April 2026
1059-0560/© 2026 The Authors. Published by Elsevier Inc. This is an open access article under the CC BY license
(h ttp://creativecommons.org/licenses/by/4.0/ ).

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
Although its cost is difficult to estimate accurately, several researchers have demonstrated that several variables influence crude oil
prices. It includes supply and demand dynamics, geopolitical uncertainty, and macroeconomic conditions (Tissaoui et al., 2024).
However, a growing literature has mentioned other factors related to financial markets affecting the oil prices, most notably financial
market uncertainty and the repercussions of volatility (Tissaoui et al. (2023); Kilian and Zhou (2022)). This transition is largely due to
the increased financialization of commodities, in which crude oil is viewed not just as a production input but also as an asset class
integrated into investment portfolios, exposing it to cross-market risk transmission (Ben Ameur et al. (2024); Tang and Xiong (2012)).
Aladwani (2024)and Tlili et al. (2024)illustrated that the precise composition of crude oil prices enables investors to implement
effective hedging strategies when trading in both risky and non-risky markets.
Theoretically, the interconnection between financial and crude oil markets has been explained through several interrelated
channels. The risk transmission channel suggests that volatility in financial markets, particularly during uncertain times, affects
commodity markets as investors change their portfolios and their exposure to risky assets like crude oil (Ftiti et al. (2022)). Addi-
tionally, the portfolio rebalancing effect indicates that institutional investors, who typically maintain diversified portfolios, modify
their positions in crude oil futures and related derivatives in response to changes in equity or bond markets, thus connecting oil prices
to overall financial sentiment (Dutta and Bouri (2024)). Furthermore, liquidity shocks in financial markets can lead to significant
redemptions or deleveraging, resulting in a simultaneous sell-off of oil assets and a decline in prices that is not necessarily linked to
physical supply and demand. Sentiment spillovers are also crucial; as fear or optimism grows in financial markets (as measured by
indices like the VIX or MOVE), these emotional changes affect investor behavior in oil markets, causing price fluctuations that are not
solely explained by macroeconomic indicators.
In recent years, as a result of the increasing impact of financial volatility and systemic market pressures, the interpretive and
predictive landscape of crude oil prices has become more complex. Several empirical studies (e.g., Kilian & Zhou, 2022; Tissaoui et al.,
2024) document how financial shocks originating from equity or bond markets transmit to the oil market, often exacerbating price
volatility. These developments are largely attributed to several factors, including intensified algorithmic trading, higher market
interconnectedness, and behavioural biases such as herding and flight-to-safety effects. As such, the crude oil market has become
increasingly sensitive to real-time shifts in investor perception and risk appetite, especially under conditions of global economic
fragility or uncertainty.
In this context, it is important to understand the formation, acceleration, and transmission of fear sentiment, particularly how it
escalates during financial turmoil and influences commodity prices, which has appeared as a vital area of inquiry. Conventional
econometric models that focus solely on macroeconomic or supply-side variables often fail to capture these nonlinear, sentiment-
driven dynamics. Consequently, there is a growing recognition among researchers and practitioners that oil price predictability re-
quires a more nuanced framework, one that accounts for both the level and temporal evolution of financial market fear, especially as it
becomes a key driver of volatility in globally integrated asset markets.
Therefore, the investor sentiment, especially in the form of fear, plays a crucial role in shaping asset price dynamics across financial
markets. This fear sentiment is commonly proxied by many uncertainty indices. These indices encapsulate market expectations of
future volatility and serve as widely recognized barometers of risk aversion. Meanwhile, previous research has used these measures as
explanatory variables in crude oil return models, but they often rely on static values. They implicitly assume that the level of fear is
sufficient to explain market behavior. However, this approach ignores an important aspect of financial sentiment, that is its temporal
dynamics. A huge increase in perceived risk can lead to nonlinear changes, rapid selloffs, margin calls, capital flight to safe-haven
assets, and widespread liquidity disruptions. These events occur so rapidly that they are difficult for observers to capture using
static indicators alone. Conversely, dynamic sentiment measures provide a more nuanced perspective for controlling market stress.
These derivatives can reveal early indicators of regime shifts, making them valuable tools for anticipating spikes in volatility in
commodity markets, such as crude oil. Therefore, the shift from static sentiment measures to derivative-based sentiment measures is
not only methodologically innovative but also fundamental to understanding and tracking price behavior in increasingly inter-
connected and sentiment-sensitive financial systems.
In this study, we examine how dynamic macro-financial sentiments, proxied through the velocity, acceleration, and jerk of the VIX
and MOVE indices, influence the behaviour and expectations of system-dependent crude oil returns. By incorporating these sentiment
derivatives within a Markov switching regression framework, the study evaluates whether changes in the intensity and momentum of
fear lead to transitions between calm and turbulent market regimes and whether these dynamics significantly improve short-term
forecasting accuracy. The resulting insights naturally extend to early warning considerations and behavioural interpretations of
how systemic financial pressures spread to oil markets.
In line with this, we illustrate that traditional models often assume a linear and proportional response to risk perceptions; however,
financial markets are inherently nonlinear and exhibit regime-dependent behavior, particularly in response to rapid shifts in senti-
ment. When fear grows gradually, traders can alter their positions with minimal disruption, resulting in smooth asset price changes.
However, when fear intensifies because of geopolitical shocks, macroeconomic surprises, or systemic pressures, markets may rapidly
shift from stability to volatility. Such sudden regime shifts frequently render traditional forecasting models worthless, as the under-
lying assumptions of smooth adjustment and constant relationships are no longer valid. To further understand these dynamics, we use
the first-, second-, and third-order derivatives of the VIX and MOVE indices (VIX_V-3 and MOVE_V-3) as sentiment momentum in-
dicators. These variables allow for the early discovery of turning regimes of market behavior, as well as a forward-looking framework
for estimating times of latent instability before they manifest as crude oil price volatility. This method enhances understanding of fear
transmission over time and extends risk assessment beyond static sentiment indicators.
Moreover, linear models are unable to consider the nonlinear and chaotic nature of energy markets. Empirical studies have shown
that crude oil markets alternate between two distinct regimes: calm periods characterized by low volatility and predictable return
2

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
patterns, and turbulent episodes with increased uncertainty, sharp price swings, and nonlinear dynamics. External shocks, investor
sentiment contagion, or sudden changes in macroeconomic expectations often drive these disturbances in oil markets. In line with
these studies, this paper tries to adequately capture this complexity, by adopting a Markov Transform Regression (MSR) framework,
which allows model parameters to evolve endogenously based on the underlying system.
While recent literature has focused on the impact of financial market sentiment, particularly fear indices such as VIX and MOVE, on
affecting crude oil price dynamics, some crucial gaps remain unresolved. First, the most of earlier studies rely on static levels of
sentiment indicators (e.g., VIX, MOVE) and assumes linear connections, ignoring sentiment's temporal evolution and shifting influence
under different market conditions. This overlooks the fact that market behavior is frequently path-dependent and regime-sensitive,
particularly during times of high uncertainty.
Second, present models typically overlook higher-order sentiment dynamics such as rate of change (velocity) and acceleration
(momentum), despite mounting evidence that these derivatives provide incremental information about market stress and anticipatory
investor behavior. The use of sentiment derivatives (first-, second-, and third-order changes in VIX and MOVE) remains rare in energy
market forecasting, especially when integrated into nonlinear regime-switching frameworks. Furthermore, the idea that dynamic
changes in financial information possess additional predictive value corresponds to recent evidence showing that the informational
value of financial data varies across market environments (Li et al., 2025). In this context, our use of VIX and MOVE derivatives
provides additional levels of useful information that go beyond the effects at the level.
Third, although regime-switching models have been applied in macro-finance contexts, they are scarcely employed to disentangle
sentiment-return interactions across calm versus turbulent regimes in the crude oil market, despite the well-established stylized fact
that financial markets transition abruptly between long periods of tranquility and short-lived volatility bursts.
Thus, there is a pressing need for a unified, high-frequency framework that (1) accounts for the dynamic structure of sentiment; (2)
distinguishes between market regimes; and (3) tests the differential predictive power of static versus derivative sentiment indicators in
forecasting crude oil returns.
Building on these gaps, we pose the following research questions. How do dynamic measures of financial fear, specifically the first,
second, and third derivatives of the VIX and MOVE indices, influence crude oil return predictability across distinct volatility regimes?
Can the Markov Switching Regression (MSR) framework uncover regime-specific asymmetries in the sentiment-return relationship
that traditional single-regime models fail to detect?
This study contributes to the literature on energy finance and behavioral market dynamics in several significant ways: First, we
innovatively conceptualize and apply the derivatives of financial fear indices, namely, velocity (first derivative), acceleration (second
derivative), and jerk (third derivative), to the study of crude oil price behavior. To describe the changing nature of financial fear, we
analyse higher-order derivatives of the VIX and MOVE indices. The first derivative, or velocity, measures the change in sentiment from
one period to the next. The second derivative, or acceleration, gauges how quickly this fear intensifies or fades. Beyond velocity and
acceleration, we include the third derivative, known as jerk, or the rate of change of acceleration, to detect sudden and nonlinear shifts
in sentiment dynamics. The use of such higher-order derivatives is well grounded in physics and dynamics literature, where jerk and
higher derivatives are recognized as important indicators of motion and rapid system adjustments (Eager et al., 2016). Recent
empirical studies also support their significance in applied dynamic modelling. For instance, Zhang et al. (2022)show that velocity,
acceleration, and jerk together better capture complex behavioural adjustments in high-frequency environments than lower-order
measures alone. Building on this interdisciplinary basis, we employ these three derivatives to measure sentiment momentum and
examine its influence on regime-dependent crude oil return dynamics.
This technique expands on standard level-based sentiment measures (e.g., VIX and MOVE), providing a more comprehensive
framework for examining how the velocity and intensity of sentiment evolution can influence market outcomes. We have integrated
the first-, second-, and third-order derivatives of the VIX and MOVE indices into our modelling framework, drawing on empirical
market behaviour and behavioural finance theory. Traditional models assume that market participants respond to the absolute level of
uncertainty or fear, whereas Prospect Theory (Kahneman & Tversky, 2013) argues that decision-making under uncertainty is highly
sensitive to changes rather than static values. Static VIX or MOVE levels ignore the idea that, given their loss aversion and nonlinear
utility perception, investors are disproportionately reactive to the rate of change in risk sentiment. Although the speed (first derivative)
of fear sentiment can cause anticipatory repositioning even before fear levels reach historical highs, acceleration (second derivative)
usually precedes volatility spikes and indicates developing panic or market unease. Moreover, herding behaviour and reflexivity
theory by Soros (2015)imply that markets often overreact to changes in sentiment by means of feedback loops, so magnifying first
shocks. Investors copy others to stay ahead of the fast-rising sentiment and avoid being left behind with changes in asset correlation
and volatility structures that define regimes. For example, during the COVID-19 shock in March 2020, equity volatility (VIX) surged
from below 20 to over 80 in a matter of days, not solely due to the level of pandemic uncertainty, but because of the explosive rate of
fear escalation. This momentum in fear caused massive liquidation across asset classes, including oil, which collapsed into negative
price territory for the first time in history. Similarly, during the 2014–2016 oil price collapse, the MOVE index's acceleration signaled
growing bond market tension due to diverging monetary policy expectations. This derivative behavior correlated with a regime shift in
crude oil returns that was not adequately explained by static indicators. These historical episodes confirm that investor reactions are
not only threshold-dependent but momentum-sensitive and thus justify the use of sentiment derivatives to forecast regime shifts and
market stress transitions in energy markets. Second, methodologically, the study expands the use of Markov Switching Regression
(MSR) models by incorporating dynamic sentiment measures into a two-regime framework. This allows for the modeling of oil returns
as a nonlinear, regime-dependent process that responds not only to sentiment levels but also to their changing patterns. The proposed
integration enhances the flexibility of econometric tools used in energy finance and provides a foundation for sentiment-driven regime
detection. Third, by incorporating both equity market (VIX) and bond market (MOVE) sentiment channels, the paper develops a
3

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
cross-market sentiment transmission mechanism. This provides a broader lens for comprehension of how risk perceptions originating
in financial markets propagate to commodity markets. To contextualise our contribution within an expanded conceptual framework, it
is necessary to draw attention to the psychological and financial pathways by which systemic sentiments spread to crude oil markets.
The increasing financialization of commodities has heightened the sensitivity of oil prices to fluctuations in global financial sentiment
(Basak & Pavlova, 2016; Tang & Xiong, 2012). The changes in financial fear, captured through the derivatives of the VIX and MOVE
indices, indicate the speed at which market participants reassess uncertainty and rebalance their investment portfolios. This dynamic
component of sentiment, often termed emotional momentum, plays a pivotal role in modern asset-pricing dynamics because it reflects
not only the level of perceived risk, but also the acceleration and intensity of shifts in collective psychology.
Several behavioral finance channels amplify the impact of emotional momentum. First, herd behaviour leads traders to mimic the
actions of others when fears intensify, resulting in simultaneous sell-offs across stocks, bonds, and commodities (Bikhchandani &
Sharma, 2000).Secondly, excessive interaction causes investors to adjust their positions disproportionately when uncertainty esca-
lates, amplifying short-term volatility and distorting prices away from fundamental values (Barberis et al., 1998).Thirdly, loss aver-
sion, an essential element of prospect theory, leads to sharper price adjustments when negative sentiment accelerates, as investors are
more sensitive to losses compared to equivalent gains (Kahneman and Tversky, 1979). Finally, sudden shifts in risk appetite occur
when emotional momentum surpasses psychological thresholds. This prompted a rapid reallocation away from high-risk assets to-
wards safe havens, such as U.S. Treasury bonds (Daniel et al., 1998). These behavioral reactions interact with financial-market
transmission mechanisms, including margin constraints, volatility-targeting rules, risk-parity adjustments, and deleveraging pres-
sures, allowing sentiment-driven stress in equity and bond markets to spill over directly into crude-oil price formation (Adrian & Shin,
2010; Gaˆrleanu & Pedersen, 2011). Such structural channels create rapid cross-market contagion: when equity or bond volatility
accelerates, commodity exposures are reduced mechanically by algorithms, leverage-sensitive portfolios, and commodity-index funds,
independently of changes in supply–demand fundamentals. Through these combined behavioral and structural pathways, emotional
momentum can exert a significant influence on crude-oil prices even in the absence of contemporaneous movements in production,
inventories, or geopolitical conditions. These insights provide a strong conceptual justification for modeling sentiment derivatives and
motivate our focus on examining their role in shaping regime transitions, market stability, and short-horizon return predictability in
crude-oil markets.
In addition, the key objective of this study is to trace how systemic financial fear originating in both equity and fixed-income
markets propagates to the crude-oil market. The VIX and MOVE indices jointly capture these two dominant dimensions of global
financial uncertainty and are widely recognized in the literature as leading indicators of investor sentiment, risk aversion, and macro-
financial stress (Bekaert et al., 2013; Fleming, 1998; Kritzman, Li, Page, & Rigobon, 2010).
VIX reflects fear and volatility expectations in U.S. equity markets, while MOVE summarizes uncertainty in the U.S. Treasury
market, an anchor for global funding conditions. Prior research shows that shocks in these markets spill over rapidly into commodities
through portfolio rebalancing, liquidity channels, and margin constraints (Aloui(2011); Bouri et al., 2017; Tissaoui and Aloui (2011);
Cheung & Ng, 1996). This make them appropriate proxies for systemic rather than asset-specific uncertainty.
In contrast, the Oil Volatility Index (OVX) measures option-implied volatility derived directly from oil futures. While informative
about oil-specific uncertainty, OVX is endogenous to oil price dynamics because it is constructed from options written on the same
underlying asset we aim to explain. As noted by Pindyck (2004)and Alquist et al. (2013), such subjectivity risks a simultaneous bias:
where implied volatilities mechanically respond to large price movements, causing the agent to absorb both cause and effect. Using
OVX as an explanatory variable can negatively affect causal inference and obscure the true direction of uncertainty flows.
By contrast, VIX and MOVE originate in external markets, making them far more suitable for identifying exogenous sentiment
shocks and minimizing feedback effects (Baumeister & Kilian, 2016; Dutta & Bouri, 2024).
For these reasons, focusing on VIX and MOVE aligns with our goal of capturing the broader transmission of systemic financial fear,
rather than localized oil-market volatility embedded in OVX.
The framework is adaptable for other asset classes and contributes to interdisciplinary research linking macro-financial risk,
behavioral responses, and commodity price dynamics. Finally, by demonstrating that sentiment derivatives carry richer informational
content than their level counterparts, the paper offers a novel early-warning system foundation. This can be applied to improve real-
time forecasting, trading strategies, and risk management protocols in energy and financial markets. The dynamic nature of these
indicators provides decision-makers with more responsive and forward-looking metrics. The remainder of the paper proceeds as
follows: Section 2reviews the relevant literature and identifies research gaps. Section 3presents the methodological framework and
data. Section 4discusses the empirical findings, highlighting differences between tranquil and turbulent regimes. Section 5concludes
with policy implications and directions for future research.
2. Literature review
Understanding the structural behavior of crude oil returns has become an increasingly challenging and important task. This un-
derstanding is particularly necessary in light of rising market volatility, geopolitical shocks, and climate-induced policy shifts. In line
with this, structural returns modeling focuses on identifying the underlying mechanisms, whether macroeconomic, financial, or
behavioral, that drive price movements across diverse time frames and geopolitical contexts. In contrast, short-term forecasting
practices prioritise forecast accuracy to a greater extent. Studies on this topic have undergone radical changes over the past two
decades, reflecting increasing complexity.
The earliest attempts to model crude oil returns relied predominantly on linear econometric frameworks, such as autoregressive
(AR) and GARCH-family models. These tools provided fundamental insights into volatility clustering and mean-reversion behavior,
4

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
particularly in stable conditions. However, with the globalization of oil commerce and the growing importance of financial speculation
and macroeconomic policy, these traditional models quickly became inadequate. This traditional stream is exemplified by studies by
Sharma (1998)and Tang and Hammoudeh (2002), which capture basic stylized market data. As well, their lack of ability to consider
the asymmetric shocks, structural fractures, and regime-dependent pattern revealed the need for more dynamic modelling tools.
This shift led to the growing application of regime-switching models, particularly the Markov Switching framework, to better
capture nonlinear and time-varying structures in oil return behavior. Following Hamilton's (1989)pioneering work, further research
has shown that oil price dynamics can adjust significantly between high- and low-volatility regimes. For instance, Cevik et al. (2025)
used a two-regime Markov Switching Vector Autoregression (MS-VAR) model to prove that macro-financial variables such as money
supply and inflation only forecast oil returns during fluctuating times. Their results provide evidence that the influence of economic
indicators on oil returns is not uniform. It is rather determined by underlying market regimes.
Complementing this regime-sensitive view is the application of copula-based models that explicitly allow for asymmetric and tail-
dependent relationships. Aloui et al. (2016)proved how the dependence structure between oil returns and uncertainty indices (such as
Economic Policy Uncertainty and Equity Market Uncertainty) changes significantly during times of crisis. Unlike static correlation
methods, copula models revealed that tail co-movement becomes pronounced during financial distress, a nuance that linear models
often miss. This means that the oil prices are sensitive to macroeconomic indicators, together with the global financial sentiment and
uncertainty.
Expanding on this sentiment-driven dimension, several studies have explored the role of uncertainty, particularly macroeconomic,
geopolitical, and climate-related, as a structural determinant of oil return dynamics. Ma et al. (2019) performed a comparative
research of various economic policy uncertainty indices on their efficacy in predicting crude oil return series. The authors illustrated
that, in the short term, the volatility of crude oil returns may be predicted by the volatility of Economic Policy Uncertainty (EPU) in
China, employing data from the United States, China, Canada, Mexico, Russia, and Europe. In comparison to the other EPU indices, the
American EPU demonstrates superior long-term predictive capability. Zhang et al. (2022)investigated the influence of uncertainty in
US economic policy on West Texas Intermediate returns over multiple timeframes and frequencies. The authors identified a negative
dynamic conditional link between US EPU indices and WTI returns using a DCC-GARCH model. Furthermore, they prompted rec-
ommendations indicating that all EPU indices may exert a significant short- and long-term influence on West Texas Intermediate
returns (1-6 months and 6-12 months). In contrast, long-term returns on West Texas Intermediate can be significantly influenced by
uncertainties in monetary policy, regulatory policy, and national security policy. Recently, He et al. (2024)provided evidence that
fluctuations in the Climate Policy Uncertainty (CPU) index, rather than its level, are significantly related to oil volatility, particularly
during periods of economic expansion. Additionally, Nguyen et al. (2025)showed that public sentiment extracted from social media
during the early phases of the Russia–Ukraine war had a measurable impact on global energy and financial markets, reinforcing the
idea that investor psychology and behavioral biases are increasingly relevant for return modeling.
With the regime transitions and sentiment effects, the concept of long memory in crude oil returns has added another layer of
structural complexity. Cerqueti, Fanelli, and Rotundo (2019)applied Hurst exponent analysis to identify persistent and anti-persistent
behavior in oil return series. They tried to uncover statistical arbitrage opportunities that arise from deviations in mean-reversion.
Their findings support the notion that return dynamics may be governed by deeper temporal dependencies, ones that evolve more
slowly than those captured by typical GARCH or ARMA specifications. This long-memory feature complements the regime-based
approach. It addresses temporal continuity, by suggesting that memory effects may span across or even transcend regime boundaries.
In response to these increasingly multifaceted return dynamics, hybrid and machine learning–based models have emerged as
powerful tools to capture hidden structures. Zhao and Lin. (2024) used a diversity of deep learning models. They are combining
empirical wavelet transforms with long short-term memory (LSTM) and Gated Recurrent Units (GRU). Their architecture not only
decomposes raw return series into trend, noise, and seasonality components but also interprets latent relationships that are difficult to
detect with traditional econometric models. In addition, Bufalo and Fanelli (2024)employed a Bayesian skew-geometric stable dis-
tribution to model the returns of Chinese oil futures. They reveal asymmetries and fat tails that are inherent to high-frequency return
data. These approaches demonstrate how machine learning models can extend beyond prediction into structural interpretation,
particularly when taking place with theory-informed components.
Taken together, the literature displays a clear development in the modelling of crude oil returns: from linear and static models to
regime-sensitive, uncertainty-integrated, and machine learning–enhanced approaches. Each successive wave of research has added
nuance, revealing how returns are shaped by a constellation of interacting factors, including financial sentiment, macroeconomic
policy, environmental regulation, and conflict-induced shocks. Moving forward, the challenge for researchers lies in synthesizing these
methodologies into unified frameworks that retain explanatory clarity while adapting to the increasing complexity of global oil
markets.
Although sentiment and uncertainty indicators allow for great efforts to model crude oil return dynamics, current methods show
clear methodological and empirical restrictions. Although classic models like GARCH and GARCH-MIDAS include stationary sentiment
levels (e.g., VIX, EPU), they neglect the temporal evolution of investor fear, so ignoring how the rate of change in sentiment drives
market behaviour. Others, like DCC-GARCH and hybrid deep learning models (e.g., BiLSTM-GARCH), capture co-movements or se-
mantic sentiment signals, yet lack interpretability and are often insensitive to structural shifts across regimes. Critically, none of these
models integrate the momentum of sentiment, its velocity and acceleration, into a regime-sensitive framework. Moreover, they usually
assume homogeneous market behaviour over time, hence neglecting nonlinear changes between peaceful and turbulent times. Our
work presents a regime-switching model including first-, second-, and third-order derivatives of VIX and MOVE indices as dynamic
sentiment proxies for addressing these gaps. By embedding these variables into a Markov Switching Regression (MSR) structure, we
capture the asymmetric and nonlinear effects of financial fear on crude oil returns across distinct market regimes. This approach not
5

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
only enhances the early detection of volatility build-up under stable conditions but also provides forward-looking insight that static or
semantically extracted sentiment indicators fail to offer. A detailed comparison of existing approaches and our proposed framework is
presented in Table 1, which highlights key differences in sentiment treatment, regime sensitivity, behavioral assumptions, and pre-
dictive capabilities.
In doing so, the proposed model offers a unified, interpretable, and empirically robust framework for oil return forecasting that
bridges the limitations of both traditional econometric and modern machine learning-based approaches.
3. Data and methodology
3.1. Data
In our study, we employ daily data from November 2002 to April 2025. We collected the Merrill Lynch Option Volatility Estimate
(MOVE) Index from https://www.investing.com/indices/ice-bofaml-move-historical-dataand the CBOE Volatility Index (VIX) from
https://www.investing.com/indices/volatility-s-p-500-historical-data. In addition, data on crude oil prices, represented by Brent
crude oil prices, were obtained from the U.S. Energy Information Administration (EIA) https://www.eia.gov/dnav/pet/pet_pri_spt_s1_
d.htm). Although several crude-oil benchmarks exist, this study employs Brent crude oil prices as the reference series. Brent crude
became as the dominant global benchmark because it is a maritime crude that can be shipped directly from the North Sea to inter-
national markets. This enables efficient arbitrage and the rapid integration of global supply and demand conditions. In contrast, West
Texas Intermediate (WTI) is delivered to the Cushing hub, which is landlocked, where pipeline bottlenecks and storage constraints
frequently cause its pricing to diverge from international fundamentals. These logistical frictions limit the suitability of West Texas
Intermediate as a global benchmark. This mainly makes it represent the market dynamics of the United States. As Sifat et al. (2023)
confirmed, the unique geographical location of Brent and its broader market scope enable it to price over 60% of the globally traded
crude oil, which comprises a significant share of OPEC exports, thereby enhancing its role as a key benchmark for global oil markets.
Using this crude oil data, we use the following formula to determine the crude oil return (RTOP):
RTOPt =(ln(pt )(cid:0) ln(pt(cid:0)1 ))*100 (1)
Where RTOPt is the crude oil return at time t. pt and pt(cid:0)1 represent the current and the previous value of crude oil price at time t and at
time t-1, respectively. Additionally, the November 2002–April 2025 timeframe was specifically selected to encompass a wide range of
geopolitical and economic developments that have had a substantial impact on the dynamics of oil prices and global financial markets.
The Global Financial Crisis of 2008, which signaled a paradigm shift in investor behavior and market volatility, falls within this
timeframe. It also includes the post-2010 U.S. shale revolution, which fundamentally changed the dynamics of the oil supply. The
dataset also includes the collapse of oil prices in 2014 and 2015, the COVID-19 pandemic's unprecedented market disruptions in 2020,
and the dramatic volatility of the energy market after the Russia-Ukraine war in 2022. Moreover, discussed are the inflationary
pressures and monetary tightening cycles of 2022–2023 as well as macro-financial environment changes resulting from fiscal actions
and increasing interest rate uncertainty. By allowing the model to detect changes in investor sentiment acceleration during both crisis
and recovery regimes, the integration of several market regimes enhances the analysis. Simple and Markov regressions made possible
by this longer period help to improve the accuracy of the switching-domain analysis. To capture sentiment momentum, Table 2defines
the mathematical expressions used to calculate the first- (velocity) (Abdelaziz (2013)), second- (acceleration)(Abdelaziz (2013)), and
third-order (jerk) (Dong et al. (2007)) derivatives of the VIX and MOVE indices, which are used as sentiment momentum indicators in
the modelling framework. In addition to the above, before estimation, all datasets were subjected to a full integrity check. The raw
daily series contained no missing observations, and all extreme variations were verified as genuine market events rather than data
anomalies. As a result, no interpolation or statistical outlier filtering was necessary; only the standard log-return transformation was
applied.
3.2. Methodology
Crude oil prices are influenced by several macroeconomic and financial elements; usually, these elements have minimal effect on
the market over time. Structural changes, including financial crises, geopolitical shocks, and strong investor feelings, can cause sudden
changes in the dynamics of the oil markets. Conventional linear models cannot adequately explain such variety. We address this in our
work using Switching Regression Models, which allow model parameters to vary between latent or observable regimes. Offering a
sophisticated structure through which to view and comprehend structural breaks in the link between fear sentiment and oil returns,
this section covers the Markov Switching Regression (MSR) and Simple Switching Regression (SSR) frameworks.
3.2.1. Baseline estimations: The Simple Switching Regression model
It supposes that the sample can be split exogenously into two or more separate regimes, each controlled by its linear relationship
between the dependent and explanatory variables. Regimes might be defined, for instance, based on predefined volatility thresholds
from indices like the VIX or MOVE or crisis against non-crisis periods.
The general form of the SSR model is given by:
6

K. Tissaoui and N. Azibi                                                                                                                     I n  t e  r n  a t i o  n  a  l   R  e v  i e w     o f   E  c  o  n o  m   i c s   a  n  d    F  in  a  n  c e    1  0 8 (2026) 105197
Table 1
Comparison of Oil Return Modelling Approaches: Existing Literature vs. Proposed MSR-Sentiment Momentum Framework.
Study/Model Sentiment  Model Type Regime  Sentiment Dynamic  Forecast  Behavioral  Limitations This Study's Improvement
|     | Source |     | Sensitivity (Velocity/  | Horizon | Representation |     |     |
| --- | ------ | --- | ----------------------- | ------- | -------------- | --- | --- |
Acceleration)
GARCH/EGARCH  VIX, OVX (static  Volatility  No None Short-term Implicit risk aversion Fails to capture structural breaks  Integrate nonlinear regime
(Charles &
levels) Models or asymmetric sentiment effects switching and dynamic fear
| Darn´e, 2017) |     |     |     |     |     |     | sensitivity |
| ------------- | --- | --- | --- | --- | --- | --- | ----------- |
GARCH-MIDAS ( Economic Policy  Mixed-  No None Mixed Macroeconomic  Adopts fixed impact of uncertainty  Adds sentiment momentum and
Kilian &
Uncertainty  frequency  linkages across regimes endogenous regime variation
| Zhou, 2022) | (EPU) | GARCH |     |     |     |     |     |
| ----------- | ----- | ----- | --- | --- | --- | --- | --- |
DCC-GARCH ( US EPU, WTI  Time-varying  No None Short-term Co-movement under  Captures dependence but not  Focuses on causal, forward-
Zhang & Yan,  return Correlation stress predictive asymmetry looking sentiment effects
2020)
7  BiLSTM-GARCH ( Twitter & news-  Hybrid Deep  No None Mixed Semantic sentiment  Lacks interpretability, black-box  Uses interpretable fear indices
Abdollahi,  based NLP  Learning (text-based) logic with economic meaning
| 2023) | indices |     |     |     |     |     |     |
| ----- | ------- | --- | --- | --- | --- | --- | --- |
Wavelet-LSTM ( Mixed indicators  Wavelet +DL No None Short & long Signal decomposition Overfits high-frequency noise; no  Focus on structural transitions
Zhao & Lin,  (OVX, EPU,  regime switching and regime-specific
| 2024) | noise)       |     |     |              |     |     | predictability |
| ----- | ------------ | --- | --- | ------------ | --- | --- | -------------- |
|       | VIX & MOVE + |     |     | Short–medium |     |     |                |
Our Study  Markov  Yes First, second, third  Behavioral fear  Captures nonlinear dynamics,  Offers early-warning signals,
(Proposed  their derivatives Switching  derivatives (VIX_V–3,  momentum &  sentiment momentum, and  high explanatory power during
MSR  Regression MOVE_V–3) feedback loops regime-specific market response  calm regimes, and robust model
| framework) |     |     |     |     |     | asymmetries | selection |
| ---------- | --- | --- | --- | --- | --- | ----------- | --------- |
Notes: The objective of this table is to compare major modelling approaches used in the oil-return literature with the proposed MSR–sentiment momentum framework in terms of sentiment sources,
regime sensitivity, behavioral representation, and predictive relevance. VIX =CBOE Volatility Index; MOVE =Treasury volatility index; VIX_V to VIX_J and MOVE_V to MOVE_J =first-, second-, and
third-order derivatives (velocity, acceleration, jerk) of sentiment indices; EPU =Economic Policy Uncertainty; OVX =Oil Volatility Index; DCC-GARCH =Dynamic Conditional Correlation GARCH;
GARCH-MIDAS =Mixed-Data Sampling GARCH; BiLSTM =Bidirectional Long Short-Term Memory; LSTM =Long Short-Term Memory; MSR =Markov Switching Regression; NLP =Natural Language
Processing; WTI =West Texas Intermediate crude oil benchmark; RTOP =Brent crude oil return series.

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
Table 2
Computation of sentiment derivatives for VIX and MOVE indices.
Derivatives VIX MOVE
Velocity (first-order derivative) VIX1t =VIXt (cid:0) VIXt(cid:0)1 (2) MOVE1t =MOVEt (cid:0) MOVEt(cid:0)1 (5)
Acceleration (second-order derivative) VIX2t =VIX1t (cid:0) VIX1t(cid:0)1 (3) MOVE2t =MOVE1t (cid:0) MOVE1t(cid:0)1 (6)
Jerk (third-order derivative) VIX3t =VIX2t (cid:0) VIX2t(cid:0)1 (4) MOVE3t =MOVE2t (cid:0) MOVE2t(cid:0)1 (7)
Notes: The purpose of this table is to present the computation of higher-order sentiment derivatives used as indicators of financial fear dynamics in
the empirical analysis. VIX =CBOE Volatility Index; MOVE =ICE BofA Merrill Lynch Treasury volatility index. VIX_V to VIX_J and MOVE_V to
MOVE_J denote the first-, second-, and third-order derivatives of each index, representing sentiment velocity, sentiment acceleration, and sentiment
jerk, respectively.
)
∑p
RTOPt =α r +β r Sentimentt +γ r log( + δ i,rRTOPt(cid:0)i +ε t ,r∈{1,2} (8)
i=1
(cid:0) )
ε t ∼ N 0,σ2 t (9)
Where, RTOPt is the return on crude oil at time t, Sentimentt represents the fear sentiment proxy (e.g. VIX, VIX_V, VIX_A, VIX_J, MOVE,
MOVE_V, MOVE_A and MOVE_J); log)represents the conditional volatility component; s denotes the regime index; α s, β s , γ s and δ i,s are
regime-specific parameters. The Simple Switching Regression (SSR) model suggests that market regimes are pre-determined based on
observable criteria, such specific crisis periods or volatility thresholds, instead of being deduced from the data itself. This exogenous
classification suggests that any probabilistic structure imposes a priori rather than controls change between regimes. This brings some
restrictions even if it offers interpretability and simplicity of implementation. First, if the chosen regime bounds deviate from real
structural changes in the data, model misspecification results. Furthermore, SSR is not flexible enough to capture the dynamic and
sometimes latent character of political changes noted in financial markets. Notwithstanding these limitations, SSR is still a useful
benchmark since it offers a condensed basis against which more sophisticated models, such the Markov Switching Regression (MSR),
can be assessed.
3.2.2. Advanced estimations: the Markov Switching Regression model
Using the Markov Switching Regression (MSR) model, in which the regime follows a first-order Markov process, we capture
endogenous, time-varying regime dynamics. This structure lets probabilistic transitions between regimes depending on past regimes
possible.
The MSR model is formally specified as:
)
∑p
RTOPt =α St +β St Sentimentt +γ St log( + δ i,St RTOPt(cid:0)i +ε t ,s∈{1,2} (10)
i=1
( )
ε t ∼ N 0,σ2 St ,St ∈{1,2} (11)
[ ]
P(St =j|St(cid:0)1 =i)=pij ,whereP= p
p
1
2
1
1
p
p
1
2
2
2
(12)
Where, St ∈{1,2}is an unobserved regime variable following a first-order Markov chain at time t; α St , β St and σ2 St are regime-dependent
coefficients and variances; P is the transition probability from regime i to regime j, where p11 +p12 =1 and p21 +p22 =1. Xt represents
the fear sentiment proxy (e.g. VIX, VIX_V, VIX_A, VIX_J, MOVE, MOVE_V, MOVE_A and MOVE_J); s denotes the regime index. A potent
and flexible framework for capturing regime-dependent dynamics in financial time series is provided by the Markov Switching
Regression (MSR) model. Maximum Likelihood Estimation (MLE) is used to estimate its parameters; usually, this is done iteratively
using the Expectation-Maximization (EM) algorithm or by Bayesian filtering using the Hamilton or Kim filter. This process simulta-
neously yields three critical components: the regime-dependent parameters (α St , β St and σ2 St ) that define the behavior of each regime,
the smoothed probabilities P(St =j|St(cid:0)1 =i)which indicate the likelihood that the system is in a particular regime at any point in time,
and the transition probability matrix P that governs the evolution between regimes. Economically, these regimes usually correspond to
different market conditions; Regime 1 usually corresponds to low volatility and stable markets where crude oil returns show a limited
sensitivity to changes in investor sentiment. Regime 2, on the other hand, catches high-volatile events like financial crises, in which
case fear sentiment takes front stage and induces nonlinear reactions in oil price dynamics. The MSR model has an important feature in
its data-driven character since it reveals regime changes based on the statistical properties of the time series itself rather than
depending on exogenous definitions of market regimes. Although the literature often illustrates tranquil and turbulent market regimes
using exogenous volatility thresholds, the present study relies entirely on endogenous regime identification through the Markov
Switching Regression (MSR) model. No predetermined cutoff or external volatility rule is imposed during estimation. Instead, the MSR
framework infers regimes directly from the data using filtered and smoothed transition probabilities. This reflects changes in the
underlying data-generating process. Importantly, the regimes generated by the MSR model naturally correspond to periods historically
8

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
characterised by high and low volatility (Hao and Pham (2024)). This shows a strong alignment with the economic understanding
behind threshold-based classifications. This coherence confirms that MSR probabilities capture significant structural shifts without
relying on arbitrary external thresholds, ensuring a consistent and data-driven definition of market systems. Under financial constraint,
this capacity makes the MSR especially appropriate for frequently simulating the asymmetric and nonlinear patterns regularly
observed in commodity markets.
To examine the potential influence of system-dependent oil market dynamics by seasonal or cyclical patterns, such as annual
demand variations, refining cycle impacts, or cyclical fluctuations in financial markets, we enhance the fundamental Markov-
switching regression (MSR) model by incorporating Fourier harmonics into the equation. Our hybrid MSR-Fourier model aligns
with the expanding literature advocating for flexible nonlinear structures in the forecasting of macro-financial variables, consistent
with Jor's (2024) hybrid modeling approach, which illustrates the advantages of incorporating dynamic shifts and adaptive data
components.
Therefore, we introduce Fourier terms of annual and semi-annual frequency, defined as:
( ) ( )
2πt 2πt
S1 =sin
365
, C1 =cos
365
(13)
( ) ( )
4πt 4πt
S2 =sin
365
, C2 =cos
365
(14)
ʹ
and put them in the vector Ft =(C1 ,C2 ,S1 ,S2 ).
To consider smooth cyclical patterns in( the) oil marke(ts, w)e use both the annual (S1 ,C1) and semiannual (S2 ,C2) Fourier harmonics.
The first harmonic, which is based on sin 2πt and cos 2πt , represents one full seasonal cycle per year. It helps the model predict
365 365
( )
changes in energy demand and the seasonality of the financial market over the course of a year. The second harmonic, sin 4πt and cos
365
( )
cos 4πt , adds a periodicity that happens twice a year. This is important for modeling semiannual patterns like maintenance cycles at
365
refineries, dual demand peaks, and semiannual storage dynamics (Inchauspe et al. (2020)). Using both sine and cosine ensures that the
model can keep up with any changes in these cycles. This structure provides a flexible, parsimonious representation of seasonal
regularities consistent with the Fourier series expansion commonly used in seasonal econometric modelling (Tissaoui (2012)).
Therefore, the seasonal MSR specification is given by:
)
∑p
RTOPt =α St +β St Sentimentt +γ St log( + δ i,St RTOPt(cid:0)i +δʹ Ft +ε t ,s∈{1,2} (15)
i=1
where δ captures the influence of cyclical and seasonal dynamics on returns. Because Fourier terms enter the conditional mean
equation rather than the transition mechanism, the MSR retains its Markov structure with constant transition probabilities, while still
providing the flexibility to identify whether periodic patterns contribute to regime-specific behavior. This extension enables us to
directly test whether seasonal or cyclical forces meaningfully affect oil-market regimes and whether the sentiment-momentum effects
identified in the baseline MSR remain robust to these periodic influences.
4. Empirical results
4.1. Data analysis
The descriptive statistics derived from the data shown in Table 3confirm the non-normal distribution and volatility of the variables
under testing. This captures the dynamism observed in the study of financial markets and energy sources. For example, the VIX index
and the MOVE index show their volatility and relevance during the study period since they have high degrees of standard deviation and
mean respectively. Skewness and kurtosis values, together with the Jarque-Bera test statistics, also verify the anomalies and structural
changes. These statistics reflect the strong models required for the capacity of the complexity involved by the data. It is worth noting
that the exceptionally high kurtosis (90.097) and extreme minimum daily return ((cid:0) 27.95 %) for crude-oil returns do not stem from
data errors but reflect genuine market shocks observed during the sample period. These include the 2008 Global Financial Crisis, the
unprecedented oil-price collapse of April 2020 during the COVID-19 pandemic, and the 2022 Russia–Ukraine energy disruption. The
raw price series were cross-validated with the original IEA and Investing.comdatabases, and returns were consistently computed using
logarithmic differences. Because the Markov Switching framework explicitly accommodates fat-tailed and regime-dependent
behavior, these extreme yet economically meaningful observations were retained to preserve the integrity of the empirical distribu-
tion and to capture their contribution to regime identification.
Crucial information regarding the relationships between RTOP and independent variables can be found in the correlation matrix
(Table 4). Especially, the empirical results of the correlation study expose different dynamics between equity and bond market un-
certainty in modulating RTOP fluctuations. Particularly, the first derivative of the VIX (VIX_V) shows the strongest and most consistent
negative association with RTOP, so stressing the main influence of fear velocity in determining the direction of energy market
9

Table 3
Summary Statistics of Oil returns and Sentiment variables (Daily Data, January 2002 – April 2025).
RTOP VIX VIX_V VIX_A VIX_J MOVE MOVE_V MOVE_A MOVE_J
Mean 0.008 19.118 0.004 0.001 (cid:0) 0.002 87.061 0.001 0.002 0.001
Median 0.031 16.780 (cid:0) 0.080 0.090 0.060 80.330 (cid:0) 0.100 0.090 0.140
Maximum 17.894 82.690 24.860 42.500 81.710 264.600 41.500 82.000 125.600
Minimum (cid:0) 27.955 9.140 (cid:0) 17.640 (cid:0) 39.210 (cid:0) 74.140 36.620 (cid:0) 40.500 (cid:0) 78.470 (cid:0) 127.500
Std. Dev. 1.133 8.465 1.824 2.762 4.868 31.098 4.297 5.980 10.143
Skewness (cid:0) 2.134 2.536 1.727 (cid:0) 1.079 (cid:0) 0.121 1.167 0.425 (cid:0) 0.361 0.063
Kurtosis 90.097 12.820 30.530 37.717 43.700 5.052 15.905 22.455 23.440
Jarque-Bera(JB) 1799331* 28905.7* 182168.3* 286302.3* 391974.3* 2285.17* 39578.25* 89685.82* 98868.01*
Probability of JB 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
Note: Parentheses are P-value. ***,** and * represent the significance level of 10%, 5% and 1%, respectively.
10
K.
Tissaoui
and
N.
Azibi
I n
t e r n
a
t i o
n
a
l
R
e v i e w
o
f
E
c o
n
o
m
i c s
a
n
d
F
in
a
n
c e
1
0
8
(2026)
105197

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
Table 4
Correlation matrix of oil returns and sentiment variables (Daily Data, January 2002 – April 2025).
RTOP VIX VIX_V VIX_A VIX_J MOVE MOVE_V MOVE_A MOVE_J
RTOP 100% (cid:0) 8% (cid:0) 19% (cid:0) 8% (cid:0) 3% (cid:0) 4% (cid:0) 9% (cid:0) 6% (cid:0) 4%
VIX ​ 100% 11% 2% 1% 59% 4% 1% 0%
VIX_V ​ ​ 100% 76% 48% 1% 26% 21% 14%
VIX_A ​ ​ ​ 100% 88% (cid:0) 1% 12% 22% 22%
VIX_J ​ ​ ​ ​ 100% 0% 4% 15% 22%
MOVE ​ ​ ​ ​ ​ 100% 7% 0% (cid:0) 1%
MOVE_V ​ ​ ​ ​ ​ ​ 100% 70% 36%
MOVE_A ​ ​ ​ ​ ​ ​ ​ 100% 85%
MOVE_J ​ ​ ​ ​ ​ ​ ​ ​ 100%
Note: Table 4presents the correlation matrix for Brent crude oil returns (RTOP), the VIX and MOVE indices, and their first-, second-, and third-order
derivatives using daily data from January 2002 to April 2025.
behaviour. On the other hand, the indicators of bond market volatility (MOVE_V, MOVE_A, MOVE_J) show less predictable correla-
tions. Higher-order derivatives such VIX_A and VIX_J suggest that the energy market mostly reacts to fast changes in sentiment rather
than to the acceleration or sudden spikes in uncertainty, implying limited additional explanatory power. These findings show how
more than in bond market conditions, movements in equity market sentiment drive short-term reactions in RTOP.
The results of the unit root test (Table 5) confirm the stationarity of all variables, even when accounting for structural breaks,
thereby ensuring the reliability of complex econometric analyses.
Reported in Table 6, the BDS test results offer strong proof of nonlinear dependence across all the variables examined. The test
statistics for VIX and MOVE rise dramatically as the embedding dimension increases; values for dimension six, respectively reach 0.493
and 0.507. This refutes the null hypothesis of i.i.d. behaviour in these volatility measures and confirms the existence of complex
dynamics. Moreover, although to a smaller degree, the first- and second-order derivatives of VIX and MOVE (e.g., VIX_V, VIX_A,
MOVE_V) also show increasing BDS statistics, suggesting organized patterns in their development. Especially, the RTOP series shows
modest but rising nonlinear dependency, implying that returns on the energy market are not totally random. These results support the
modelling of RTOP in response to financial fear dynamics by using nonlinear frameworks including machine learning-based models or
Markov Switching Regression.
4.2. Empirical analysis
4.2.1. Simple Switching Regression (MSR) models results
To establish a foundational understanding of how financial market sentiment influences crude oil return dynamics, the analysis
begins with estimating Simple Switching Regression (SSR) models (Table 7). These models serve as a conceptual and empirical baseline
by allowing the relationship between sentiment indicators and oil returns to change across two distinct yet unobservable market
regimes. Specifically, these regime shifts are governed by constant transition probabilities. This makes the SSR approach particularly
suitable for capturing nonlinear behaviours without the complexities of time-varying switches. The regimes, interpreted as tranquil
and turbulent market regimes, offer a framework for examining how sentiment effects may vary depending on broader market
volatility. The SSR models are estimated using daily data from 2002 to 2025, with the crude oil return (RTOP) as the dependent
variable. Two key measures of investor fear are employed. We utilise the CBOE Volatility Index (VIX) to represent equity market fear
and the Merrill Lynch Option Volatility Estimate (MOVE) to measure uncertainty in the bond market. Both indicators are introduced in
their static (level) form and tested in separate model specifications. This approach allows for a clear comparison of each sentiment
proxy's explanatory power under different volatility regimes.
The empirical results reveal a pronounced regime dependency in the influence of sentiment on oil returns. In low-volatility regimes
(Regime 1), both VIX and MOVE exhibit statistically significant and negative coefficients. For instance, in the SSR-VIX model, the
coefficient of VIX is (cid:0) 0.0079 (p <0.01), and in the SSR-MOVE model, the MOVE coefficient is (cid:0) 0.0008 (p ≈0.047). These results
provide evidence that increases in financial market fear, whether equity- or bond-driven, are associated with decreasing oil returns
during stable market conditions. This may reflect early-stage panic selling, flight-to-quality behavior, or expectations of global demand
contraction. However, in high-volatility regimes (Regime 2), this relationship weakens. The VIX coefficient in the SSR-VIX model
remains negative ((cid:0) 0.0335) and marginally significant (p ≈0.033), but MOVE becomes statistically insignificant ((cid:0) 0.0066, p >0.24).
This highlights that fear signals are largely absorbed or already priced in during market turbulence, limiting their marginal impact. The
coefficient on log volatility (LOG(SIGMA)) also indicates a regime asymmetry. In Regime 1, LOG(SIGMA) is negative and significant (e.
Table 5
Unit root test results.
Variables RTOP VIX VIX_V VIX_A VIX_J MOVE MOVE_V MOVE_A MOVE_J
ADF with break point value (cid:0) 82.28 (cid:0) 7.89 (cid:0) 87.36 (cid:0) 140.92 (cid:0) 176.47 (cid:0) 5.20 (cid:0) 73.02 (cid:0) 120.63 (cid:0) 157.63
p-value 0.000* 0.000* 0.000* 0.000* 0.000* 0.000* 0.000* 0.000* 0.000*
Note: Parentheses are P-value. ***, ** and * represent the significance level of 10%, 5% and 1%, respectively.
11

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
Table 6
Brock–dechert–scheinkma (BDS) test.
Dimension RTOP VIX VIX_V VIX_A VIX_J MOVE MOVE_V MOVE_A MOVE_J
2 0.014* 0.177* 0.039* 0.067* 0.083* 0.186* 0.027* 0.054* 0.070*
3 0.029* 0.299* 0.080* 0.119* 0.142* 0.316* 0.054* 0.096* 0.119*
4 0.040* 0.383* 0.109* 0.151* 0.177* 0.406* 0.074* 0.122* 0.146*
5 0.047* 0.438* 0.126* 0.168* 0.195* 0.467* 0.086* 0.135* 0.159*
6 0.051* 0.473* 0.134* 0.174* 0.202* 0.507* 0.090* 0.139* 0.161*
Note: Parentheses are P-value. ***, ** and * represent the significance level of 10%, 5% and 1%, respectively.
Table 7
Simple switching regression results.
Independent Variables VIX VIX_V VIX_A VIX_J MOVE MOVE_V MOVE_A MOVE_J
Regime 1(R1)
α r 0.1591 (cid:0) 0.0851 (cid:0) 0.0787 0.0173 0.0865 0.0168 0.0175 0.0177
Prob (α r) 0.0000 0.7201 0.7423 0.1517 0.0181 0.1666 0.1479 0.1419
Sentiment (cid:0) 0.0079 (cid:0) 0.3152 (cid:0) 0.1385 (cid:0) 0.0016 (cid:0) 0.0008 (cid:0) 0.0148 (cid:0) 0.0067 (cid:0) 0.0025
Prob (Sentiment) 0.0000 0.0000 0.0067 0.5481 0.0467 0.0000 0.0013 0.0409
log(σ t ) (cid:0) 0.2170 1.2781 1.2884 (cid:0) 0.2144 (cid:0) 0.2142 (cid:0) 0.2164 (cid:0) 0.2151 (cid:0) 0.2143
Prob (log(σ t )) 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
Regime 2 (R2)
α r 0.8259 0.0151 0.0162 (cid:0) 0.1345 0.5053 (cid:0) 0.1378 (cid:0) 0.1623 (cid:0) 0.1824
Prob (α r) 0.0900 0.1977 0.1781 0.5760 0.4157 0.5640 0.4982 0.4506
Sentiment (cid:0) 0.0335 (cid:0) 0.0846 (cid:0) 0.0178 (cid:0) 0.0443 (cid:0) 0.0066 (cid:0) 0.1101 (cid:0) 0.0747 (cid:0) 0.0318
Prob (Sentiment) 0.0331 0.0000 0.0000 0.1083 0.2469 0.0017 0.0140 0.1010
log(σ t ) 1.2976 (cid:0) 0.2218 (cid:0) 0.2165 1.3025 1.3050 1.2921 1.2964 1.3024
Prob (log(σ t )) 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
Transition probabilities and expected durations
P11 0.9514 0.0465 0.0489 0.9516 0.9518 0.9519 0.9517 0.9518
P22 0.0486 0.9535 0.9511 0.0484 0.0482 0.0481 0.0483 0.0482
Dur. R1 20.5900 1.0500 1.0500 20.6700 20.7500 20.7600 20.7300 20.7600
Dur. R2 1.0500 21.4800 20.4600 1.0500 1.0500 1.0500 1.0500 1.0500
Common
AR(1) (cid:0) 0.0022 (cid:0) 0.0062 0.0069 0.0027 (cid:0) 0.0004 0.0069 0.0059 0.0038
Prob AR(1) 0.8674 0.6454 0.6073 0.8379 0.9771 0.6039 0.6505 0.7715
AR(2) (cid:0) 0.0140 (cid:0) 0.0132 (cid:0) 0.0115 (cid:0) 0.0117 (cid:0) 0.0096 (cid:0) 0.0105 (cid:0) 0.0095 (cid:0) 0.0087
Prob AR(2) 0.3095 0.3660 0.4381 0.4187 0.5427 0.4870 0.5300 0.5752
AR(3) 0.0170 0.0082 0.0139 0.0144 0.0093 0.0124 0.0108 0.0108
Prob AR(3) 0.2080 0.6045 0.3784 0.3274 0.5800 0.4346 0.4987 0.5073
AR(4) 0.0267 0.0254 0.0248 0.0259 0.0235 0.0311 0.0278 0.0254
Prob AR(4) 0.0290 0.0424 0.0377 0.0304 0.0552 0.0119 0.0238 0.0377
Transition Parameters
Transition Param 2.9753 (cid:0) 3.0197 (cid:0) 2.9686 2.9791 2.9834 2.9839 2.9822 2.9835
Prob Transition Param 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
Model performance
AIC 2.7228 2.6986 2.7231 2.7270 2.7266 2.7206 2.7242 2.7261
LogLik (cid:0) 7715.0300 (cid:0) 7646.3200 (cid:0) 7715.8000 (cid:0) 7726.8900 (cid:0) 7725.6400 (cid:0) 7708.6200 (cid:0) 7718.7900 (cid:0) 7724.4100
Note: Incorporating both static (VIX, MOVE) and dynamic (VIX_V–3, MOVE_V–3) sentiment indicators, the table above shows regime-specific
estimation results from a series of Simple Switching Regression (SSR) models, so explaining crude oil return behaviour under different market
conditions. Important parameters are regime-dependent intercepts (Intercept R1 and R2), which, in calm and turbulent periods, respectively, offer the
baseline return levels. Measured through several forms of volatility indices, the coefficients for the sentiment variables (Sentiment R1 and R2) capture
the impact of financial fear, measured on crude oil returns in each regime. With p-values to evaluate statistical relevance, the conditional volatility
term (log)R1 and R2) shows how changes in return volatility relate to crude oil pricing dynamics across regimes. Transition probabilities (P11 and
P22) and the resulting regime durations (Dur. R1 and Dur. R2) give insight into how long markets typically remain in either stable or stressed regimes,
confirming the empirical stylization that calm periods are persistent while turbulent regimes are brief but intense. The autoregressive coefficients, AR
(1) through AR(4), together with their significance levels, help explain the temporal dependencies in the return series. Furthermore, underlined by the
transition parameter and its importance are the strength and probability of regime switching behaviour. The Akaike Information Criteria (AIC) and
log-likelihood (LogLik) models are then assessed; lower AIC values indicate better model fit and higher LogLik values indicate worse model fit. These
outputs taken together show that, especially in capturing the asymmetric effects of investor fear across volatility regimes, derivative-based sentiment
indicators meaningfully improve model performance.
g., (cid:0) 0.217 for VIX). This is consistent with a volatility-aversion effect. In Regime 2, it becomes highly positive (e.g., +1.297 for VIX).
The regime transition probabilities reinforce this dynamic structure. Regime 1 shows high persistence, with P11 = 0.951 and an
average duration of ~20 days, while Regime 2 is brief (duration ≈1.05 days). The transition matrices across SSR variants are sym-
metric. This confirms the structural simplicity of the SSR model. We observe that the model fit diagnostics results reinforce the
12

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
comparative strength of the equity-based sentiment proxy. The SSR-VIX model achieves an AIC of 2.7228 and log-likelihood of
(cid:0) 7715.03, slightly outperforming the SSR-MOVE model (AIC =2.7266; LogLik =(cid:0) 7725.64). This reinforces the notion that equity
market sentiment holds stronger contemporaneous predictive power over crude oil returns. As well, the coefficient on log volatility
(LOG(SIGMA)) in the SSR-MOVE model also reveals pronounced regime asymmetry. In Regime 1, LOG(SIGMA) is negative and sta-
tistically significant ((cid:0) 0.2142, p <0.01), confirming the presence of a volatility-aversion effect whereby increases in uncertainty
dampen crude oil returns during stable market conditions. Conversely, in regime 2, the coefficient has a strongly positive value
(+1.3050, p <0.01). This indicates that the volatility becomes self-reinforcing during volatile episodes. This means the tendency for
extreme price movements to cluster, often driven by liquidity shortages, feedback trading, or herding behavior in stressed
environments.
The dynamics of regime transitions in the SSR-MOVE model support this dual-market perspective. Regime 1 shows considerable
persistence, with a transition probability of P11 =0.9518 and an expected length of 20.75 trading days. Regime 2, on the other hand,
lasts substantially shorter, with an average duration of only around 1.05 days, mirroring the normal structure of oil markets, long
periods of relative quite punctuated by brief but intense volatility. The symmetry of the transition probabilities across regimes, as seen
in P22 =0.9518 as well, underlines the static nature of regime shifts within the SSR framework. Model fit statistics reveal that the SSR-
MOVE model, while still capturing meaningful sentiment effects, performs slightly less effectively than its VIX-based counterpart. It
produces a higher AIC (2.7266) and lower log-likelihood ((cid:0) 7725.64), compared to the SSR-VIX model. This suggests that although
bond market sentiment, as measured by MOVE, plays a role in crude oil pricing, equity-based fear measures offer stronger contem-
poraneous explanatory power in this baseline SSR setting.
Beyond performance, these results carry important theoretical and practical implications. Oil returns appear more sensitive to fear
shocks during calm conditions than under stress. This highlights the asymmetric nature of behavioural and liquidity responses. More
precisely, the sentiment-based early warning indicators may be effective during market stability, but are insufficient in isolation for
forecasting during high-risk periods. However, the SSR framework, which has revealed its ability to identify regime-contingent effects,
lacks the flexibility to account for dynamic shifts in the pace or escalation of sentiment. Static proxies such as VIX and MOVE fail to
capture changes in sentiment velocity or acceleration, factors that may be increasingly vital in high-frequency trading and real-time
risk management. To overcome these gaps, the analysis proceeds to explore sentiment derivatives within a Simple Switching
Regression (SSR) framework, where sentiment evolves not only in level but also in momentum and curvature. For the Impact of VIX
and MOVE Derivatives on Crude Oil Returns, we focus specifically on the influence of financial sentiment derivatives, namely the
velocity (first derivative), acceleration (second derivative), and jerk (third derivative) of the VIX and MOVE indices, on crude oil
returns (RTOP) within a Simple Switching Regression (SSR) framework. These sentiment extensions are used to capture the evolving
intensity of fear and uncertainty in financial markets and how these shifts propagate into the oil market across distinct volatility
regimes.
In Regime 1 (low volatility), the empirical results indicate a strong and statistically significant effect of both VIX and MOVE de-
rivatives. For the equity-based VIX, the velocity (VIX_V) has a coefficient of (cid:0) 0.3152 (p <0.01), the acceleration (VIX_A) is (cid:0) 0.1385
(p ≈0.0067), and the jerk (VIX_J) is (cid:0) 0.0016 but statistically insignificant (p ≈0.5481). These values suggest that when fear ac-
celerates, not just increases, crude oil returns are negatively impacted, especially under tranquil market conditions. The decline in
statistical strength from VIX_V to VIX_J highlights a diminishing marginal contribution of higher-order derivatives, with velocity and
acceleration carrying most of the explanatory power.
The MOVE index derivatives present a comparable pattern. MOVE_V (velocity) is highly significant ((cid:0) 0.0148, p <0.01), as is
MOVE_A (acceleration) at (cid:0) 0.0067 (p ≈0.0013). MOVE_J (jerk), however, although negative ((cid:0) 0.0025), shows only marginal sig-
nificance (p ≈0.0409). These results coincide with theoretical expectations, which illustrate that during periods of stability, market
participants are more reactive to sharp changes in risk indicators, and such sensitivity diminishes as sentiment dynamics become more
abrupt or erratic.
In contrast, under Regime 2 (high volatility), the effect of sentiment derivatives fades. VIX_V remains negative at (cid:0) 0.0846 (p ≈
0.0000), and VIX_A at (cid:0) 0.0178 (p ≈0.0000), but VIX_J again loses explanatory power ((cid:0) 0.0443, p ≈0.1083). The MOVE derivatives
show similar attenuation: MOVE_V at (cid:0) 0.1101 (p ≈0.0017), MOVE_A at (cid:0) 0.0747 (p ≈0.0140), and MOVE_J at (cid:0) 0.0318 (p ≈0.1010).
This pattern provides evidence that as markets become increasingly unstable, oil returns are more likely governed by structural shocks
or price normalization mechanisms rather than rapid shifts in sentiment momentum.
Log volatility coefficients further validate this interpretation. They remain significantly negative in Regime 1 and switch to highly
positive in Regime 2, consistent with a regime where sentiment is either a trigger (calm conditions) or a symptom (turbulent con-
ditions) of return movements.
In summary, the velocity and acceleration of VIX and MOVE appear to have the ability to predict crude oil returns during tranquil
regimes. This supports the assumption that the escalation of fear matters more than static fear levels alone. Jerk, the third derivative,
while conceptually capturing sudden sentiment shockwaves, contributes less significantly in the SSR setting. Beyond empirical vali-
dation, these effects carry real-world implications: first, oil investors and risk managers should pay close attention not just to sentiment
levels, but to how quickly those levels are changing. Thus, early-warning systems can benefit from incorporating velocity and ac-
celeration indicators, especially during regime 1, where these dynamics offer leading signals. Additionally, during Regime 2, static
hedging may be less effective, and alternative models, such as those that capture nonlinear structural risk, are more appropriate.
Overall, the analysis demonstrates that the velocity and acceleration of sentiment indices are critical tools for anticipating oil price
behaviour under stable conditions. The SSR model confirms their relevance in regime-dependent contexts and lays the groundwork for
more nuanced, time-varying models like MSR (Markov Switching Regression) that better capture the complexity of modern energy and
financial markets. These findings pave the way for using such sentiment dynamics in more advanced Markov-switching frameworks in
13

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
subsequent sections.
Regarding the Wald test results, we observe that only the level-based volatility indices, VIX (Wald =26.55, p <0.001) and, to a
lesser extent, MOVE (Wald =6.61, p =0.037), exhibit statistically significant effects in the mean equation. However, all first-, second,
and third-order derivatives of both VIX and MOVE (i.e., VIX_V to VIX_J and MOVE_V to MOVE_J) fail to achieve significance (p >0.28),
indicating that under a linear, regime-invariant specification, sentiment momentum provides no incremental explanatory power over
static sentiment measures. This provides evidence that in models where market structure is assumed to be homogeneous and time-
invariant, only direct levels of fear are detected by the model, while more subtle shifts in sentiment momentum remain obscured.
4.2.2. Markov Switching Regression (MSR) models results
To address the limitations of the Simple Switching Regression (SSR) framework, particularly its assumption of constant transition
probabilities, the analysis is expanded to include Markov Switching Regression (MSR) models. The MSR framework permits regime
transitions to develop endogenously based on the data, providing a more realistic and adaptive structure for capturing shifts in crude
oil return dynamics influenced by sentiment. The models are estimated using daily data from 2002 to 2025, with crude oil returns
Table 8
Markov switching regression results.
Indicator VIX_V VIX_A VIX_J MOVE_V MOVE_A MOVE_J VIX MOVE
Regime 1
α r 0.0150 0.0180 (cid:0) 0.1180 (cid:0) 0.1180 (cid:0) 0.0460 (cid:0) 0.1180 0.1040 0.5860
Prob (α r) 0.0060 0.1770 0.1240 0.4190 0.7500 0.4220 0.1320 0.5900
Sentiment (cid:0) 0.0880 (cid:0) 0.0200 (cid:0) 0.0160 (cid:0) 0.0750 (cid:0) 0.0540 (cid:0) 0.0210 (cid:0) 0.0050 (cid:0) 0.0060
Prob (Sentiment) 0.0000 0.0000 0.2340 0.0000 0.0000 0.0180 0.0490 0.0491
log(σ t ) (cid:0) 0.2270 (cid:0) 0.2190 1.0950 1.0830 1.0670 1.0890 (cid:0) 0.2240 1.0920
Prob (log(σ t )) 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
Regime 2
α r (cid:0) 0.0880 (cid:0) 0.1160 0.0180 0.0170 0.0180 0.0180 0.2350 0.0210
Prob (α r) 0.5560 0.5520 0.1220 0.1340 0.1170 0.1200 0.1320 0.5900
Sentiment (cid:0) 0.1810 (cid:0) 0.0570 (cid:0) 0.0010 (cid:0) 0.0100 (cid:0) 0.0030 (cid:0) 0.0010 (cid:0) 0.0150 0.0000
Prob (Sentiment) 0.1670 0.0130 0.3910 0.0010 0.1580 0.5840 0.9260 0.9258
log(σ t ) 1.0880 1.0890 (cid:0) 0.2160 (cid:0) 0.2170 (cid:0) 0.2150 (cid:0) 0.2160 1.1440 (cid:0) 0.2150
Prob (log(σ t )) 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
Transition probabilities and expected durations
P11 0.9930 0.9930 0.9180 0.9160 0.9280 0.9190 0.9890 0.9210
P22 0.9040 0.9160 0.9930 0.9930 0.9940 0.9930 0.7730 0.9930
Dur. R1 133.7400 140.9500 12.2500 11.8500 13.8400 12.4100 90.9800 12.6500
Dur. R2 10.4500 11.8500 146.1800 142.6300 167.6800 147.4500 4.4000 151.0500
Common
AR(1) 0.0010 0.0130 0.0110 0.0100 0.0110 0.0110 0.0090 0.0090
Prob AR(1) 0.9380 0.3210 0.4240 0.4780 0.4330 0.4200 0.5220 0.5220
AR(2) (cid:0) 0.0110 (cid:0) 0.0110 (cid:0) 0.0110 (cid:0) 0.0110 (cid:0) 0.0110 (cid:0) 0.0110 (cid:0) 0.0110 (cid:0) 0.0110
Prob AR(2) 0.3900 0.4250 0.4230 0.4320 0.4050 0.4230 0.4210 0.4210
AR(3) 0.0080 0.0060 0.0030 0.0040 0.0020 0.0030 0.0040 0.0040
Prob AR(3) 0.5410 0.6610 0.7940 0.7640 0.8950 0.7940 0.7910 0.7910
AR(4) 0.0020 0.0010 0.0030 0.0060 0.0030 0.0030 0.0030 0.0030
Prob AR(4) 0.8720 0.9290 0.8010 0.6600 0.8240 0.8010 0.8400 0.8400
Transition Parameters
Transition Param 1 4.8880 4.9410 2.4210 2.3840 2.5530 2.4340 2.4550 2.4550
Prob Transition Param 1 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
Transition Param 2 (cid:0) 2.2460 (cid:0) 2.3840 (cid:0) 4.9780 (cid:0) 4.9530 (cid:0) 5.1160 (cid:0) 4.9870 (cid:0) 5.0110 (cid:0) 5.0110
Prob Transition Param 2 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
Model performance
AIC 2.6490 2.6720 2.6760 2.6710 2.6740 2.6750 2.6770 2.6760
LogLik (cid:0) 7504.570 (cid:0) 7570.770 (cid:0) 7580.4 (cid:0) 7567.97 (cid:0) 7575.39 (cid:0) 7578.56 (cid:0) 7585.04 (cid:0) 7579.59
Note: Incorporating both static (VIX, MOVE) and dynamic (VIX_V–3, MOVE_V–3) sentiment indicators, the table above shows regime-specific
estimation results from a series of Markov Switching Regression (MSR) models, explaining crude oil return behaviour under different market con-
ditions. Important parameters are regime-dependent intercepts (Intercept R1 and R2), which, in calm and turbulent periods, respectively, offer the
baseline return levels. Measured through several forms of volatility indices, the coefficients for the sentiment variables (Sentiment R1 and R2) capture
the impact of financial fear, measured on crude oil returns in each regime. With p-values to evaluate statistical relevance, the conditional volatility
term ((log)R1 and R2) shows how changes in return volatility relate to crude oil pricing dynamics across regimes. Transition probabilities (P11 and
P22) and the resulting regime durations (Dur. R1 and Dur. R2) give insight into how long markets typically remain in either stable or stressed regimes,
confirming the empirical stylization that calm periods are persistent while turbulent regimes are brief but intense. The autoregressive coefficients AR
(1) through AR(4), together with their significance levels help to explain the temporal dependencies in return series. Furthermore, underlined by the
transition parameter and its importance are the strength and probability of regime switching behaviour. The Akaike Information Criteria (AIC) and
log-likelihood (LogLik) models are then assessed; lower AIC values indicate better model fit and higher LogLik values indicate worse model fit. These
outputs taken together show that, especially in capturing the asymmetric effects of investor fear across volatility regimes, derivative-based sentiment
indicators meaningfully improve model performance.
14

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
(RTOP) serving as the dependent variable. Two main types of sentiment indicators are assessed: the levels of VIX and MOVE (rep-
resenting static fear), and their derivatives, velocity (first difference), acceleration (second difference), and jerk (third difference),
which illustrate the dynamic propagation of sentiment.
4.2.2.1. Static Sentiment effects: VIX and MOVE in level. Thus, the integration of the static level forms of VIX and MOV into the Markov
Switching Regression (MSR) framework (Table 8) reveals their limited explanatory power, especially when juxtaposed with derivative-
based sentiment measures. Within Regime 1, which characterizes calm market conditions, the VIX index shows a marginally significant
negative effect on crude oil returns (coefficient =(cid:0) 0.005, p ≈0.049). This weakly indicates that rising equity market fear slightly
depresses returns when markets are calm, consistent with pre-emptive portfolio rebalancing or early-stage investor caution.
In contrast, MOVE, the bond market volatility proxy, exhibits an even weaker influence in the same regime (coefficient =(cid:0) 0.006, p
≈0.590), indicating that fixed-income uncertainty has little discernible effect on oil price behavior during non-crisis periods. The lack
of significance signifies that equity-based sentiment (VIX) remains more closely aligned with oil market dynamics than bond market
sentiment in low-risk environments. The explanatory power of both indicators deteriorates further in Regime 2, which is associated
with turbulent, high-volatility episodes. Here, the VIX coefficient flattens entirely ((cid:0) 0.015, p ≈ 0.926), suggesting that oil prices
become insensitive to additional fluctuations in equity market fear once systemic stress is already elevated. MOVE also remains sta-
tistically irrelevant (coefficient =(cid:0) 0.006, p ≈0.590). This asymmetry reinforces the notion that in crisis environments, oil price
movements are increasingly driven by structural shocks, policy responses, or endogenous volatility dynamics, rather than by exoge-
nous sentiment measures. Additionally, the model diagnostics further support this finding. The MSR-VIX and MSR-MOVE models
generate higher Akaike Information Criterion (AIC) values, 2.677 and 2.676, respectively, together with a lower log-likelihoods
((cid:0) 7585.04 and (cid:0) 7579.59). This highlights a poorer fit relative to MSR models that incorporate sentiment derivatives.
4.2.2.2. Dynamic Sentiment effects: derivatives of VIX and MOVE. The integration of the velocity, acceleration, and jerk of financial fear
produces a significant advancement in modelling crude oil return dynamics. Contrary to static proxies, these higher-order proxies
reflect not just the level of fear in financial markets but its evolutionary speed and intensity. Thereby, this offers a more responsive and
forward-looking indicator of market stress transmission. Within Regime 1 (tranquil conditions), the impact of dynamic sentiment is
both statistically robust and economically meaningful. For the VIX-based derivatives, VIX_V (velocity) has a highly significant and
strongly negative coefficient ((cid:0) 0.088, p <0.001), confirming that rapid surges in equity market fear are promptly and negatively
priced into oil returns. This is supported by the behavioral finance theories of early-stage risk aversion. This theory supposes that
sudden spikes in fear trigger portfolio reallocation away from risk assets such as oil. VIX_A (acceleration) also exerts a statistically
significant effect ((cid:0) 0.020, p <0.001), highlighting that not only the level but the rate of change in fear matters. This captures how
markets react not just to volatility but to increasing volatility, a common feature in pre-crisis build-ups. VIX_J (jerk), however, loses
significance ((cid:0) 0.016, p ≈0.234), suggesting that third-order dynamics (rate of acceleration) may be too erratic or short-lived to
influence oil prices meaningfully in tranquil conditions. This diminishing effect across derivatives indicates that velocity and accel-
eration are the dominant transmission mechanisms for equity-driven sentiment. For the bond market proxy MOVE, MOVE_V (velocity)
also demonstrates a strong, negative, and significant relationship ((cid:0) 0.075, p <0.001) in Regime 1, confirming that rapid increases in
bond market fear similarly depress oil returns. MOVE_A is significant ((cid:0) 0.054, p <0.001). This supports the leading role of sentiment
momentum even in fixed-income markets. MOVE_J, though less pronounced, is marginally significant ((cid:0) 0.021, p ≈0.018), suggesting
that sudden and sharp increases in uncertainty in bond markets may still impact crude oil pricing, albeit to a lesser extent.
In turbulent periods (Regime 2), the explanatory power of fear derivatives decreases significantly. More specifically, VIX_V has a
coefficient of (cid:0) 0.0019 with a p-value of 0.216, VIX_A reveals (cid:0) 0.0006 with a p-value of 0.472, and VIX_J becomes negligible with a
coefficient of (cid:0) 0.0001 and an insignificant p-value of 0.751. As well, MOVE_V registers a coefficient of (cid:0) 0.0023 (p-value =0.195),
while MOVE_A and MOVE_J produce (cid:0) 0.0007 (p-value =0.408) and (cid:0) 0.0002 (p-value =0.679), respectively. These values suggest
Fig. 1. Markov switching smoothed regime probabilities for MSR-VIX (Daily Data, January 2002–April 2025).
15

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
that during episodes of extreme volatility, the dynamics of the crude oil market are less responsive to changes in sentiment momentum
or shocks in fear sentiment, and are instead more strongly influenced by endogenous forces, such as liquidity constraints, policy shocks,
or real economic fundamentals. This attenuation of sentiment influence under stress is aligned with the information saturation hy-
pothesis. This hypothesis posits that when volatility is already high, additional fear signals embedded in higher-order sentiment
measures provide minimal incremental informational content and thus fail to significantly influence asset price behaviour.
From a risk management and forecasting perspective, these findings underline the financial value of monitoring sentiment levels
and their magnitudes. The velocity has significant and persistent impacts. This highlights their importance in predictive systems,
especially during pre-turbulence growth periods when markets are sensitive to fluctuations in fear. Furthermore, the significant effect
of acceleration demonstrates that fear momentum might provide additional forecasting information before volatility takes effect. In
contrast, the jerk's limited effect cautions against complicating models with higher-order derivatives, which may capture noise rather
than real market signals. The results show that first- and second-order sentiment dynamics provide the optimal balance of predictive
depth and stability.
Graphically, we show the smoothed regime probabilities for each specification over the entire sample period (2002–2024) to
visually validate the Markov Switching Regression (MSR) model's performance. The calm regime (P(S(t) =1) is depicted in blue in all
figures (Figs. 1–8), while the turbulent market conditions (P(S(t) =2) are depicted in orange).
The smoothed probability estimates validate that regime shifts can be detected endogenously by the MSR model. The calm regime is
characterised by long durations and high persistence, which is consistent with low market stress and steady oil price dynamics. The
turbulent regime, on the other hand, appears in short but sudden episodes and occurs in combination with well-documented global
shocks. For example, we find sharp increases in the likelihood of belonging to Regime 2 during the 2008 Global Financial Crisis, the oil
price collapse in 2014–2015, the COVID-19 outbreak in 2020, and the Russia–Ukraine conflict in 2022. The abrupt changes into high-
volatility conditions that characterise these episodes validate the regime-switching logic that is incorporated into our model. More-
over, the temporal separation between regimes demonstrates that transitions are not random or frequent, but rather tied to structural
economic or geopolitical shifts. This supports the stylized fact in financial markets: long periods of low volatility are punctuated by
short-lived, high-volatility crises. Importantly, this dynamic behavior also reinforces the differential predictive power of sentiment
momentum. Our earlier results showed that sentiment velocity (VIX_V, MOVE_V) and acceleration (VIX_A, MOVE_A) are most pre-
dictive during tranquil periods, where market participants are highly sensitive to early changes in fear sentiment. However, during
turbulent regimes, when markets react more to structural shocks than to changing sentiment, the predictive power of these derivatives
declines due to information saturation. These findings demonstrate the necessity of regime-sensitive models and the potential of
smoothed probabilities as both diagnostic and visual early-warning indicators for shifts in market conditions.
4.2.2.3. Regime volatility dynamics and transition persistence. The Markov Switching Regression analysis reveals a compelling asym-
metry in the volatility–return tradeoff in the crude oil market, under distinct market regimes. During a stable regime, the volatility
coefficient (LOG(SIGMA)) is negative and statistically significant across all models. Specifically, the estimates range from (cid:0) 0.213 in
the MSR-VIX_J model to (cid:0) 0.232 in the MSR-MOVE model, with intermediate values such as (cid:0) 0.224 in MSR-VIX, (cid:0) 0.227 in MSR-
VIX_V, and (cid:0) 0.225 in MSR-MOVE_A. This demonstrates that even minimal increases in volatility tend to diminish crude oil
returns, consistent with risk-aversion behavior, in which investors abandon risky assets as uncertainty rises.
This process, however, sees a dramatic reversal in the unstable regime. In this scenario, the LOG(SIGMA) coefficients are statis-
tically significant and positive, indicating a fundamental shift in market behavior. The coefficients increase to +1.111 in MSR-VIX,
+1.144 in MSR-VIX_V, and similar levels in MOVE-based models (e.g., +1.124 in MSR-MOVE and +1.093 in MSR-MOVE_A). This
positive shift reveals an effect of feedback in which increased volatility no longer minimizes but rather stimulates returns, reflecting
behavioral factors such as panic-induced herding, margin calls, and speculative overshooting.
Fig. 2. Markov switching smoothed regime probabilities for MSR-VIX_V (Daily Data, January 2002–April 2025).
16

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
Fig. 3. Markov switching smoothed regime probabilities for MSR-VIX_A (Daily Data, January 2002–April 2025).
Fig. 4. Markov switching smoothed regime probabilities for MSR-VIX_J (Daily Data, January 2002–April 2025).
The estimated regime dimensions which support this regime-based behavioral dichotomy, provide additional insight into market
volatility's structural patterns. Tranquil regimes are observed to be long-lasting, with trading days ranging from 134 to 141 according
to various models. For example, the MSR-VIX_V model predicts 137 days, whereas the MSR-VIX_J model predicts 141. MOVE-based
models have similar lengths, ranging from 135 days for MSR-MOVE to 140 days for MSR-MOVE_A. The market environment has been
characterized by calm conditions for a long time, as these lengthier durations show.
In contrast, turbulent regimes are temporary but intense, lasting only 10 to 12 trading days on average. For example, Regime 2
duration estimations are reduced to 10 days in MSR-VIX_V and MSR-VIX_J, 11 days in MSR-VIX and MSR-MOVE_V, and 12 days in
MSR-MOVE. These short-lived but intense events are consistent with empirical regularities in financial time series that have been
extensively studied, including the tendency of markets to undergo sudden bursts of volatility that swiftly subside.
All of our results point to the necessity of including regime-dependent characteristics into risk management techniques and
forecasting models. Volatility's impact on returns is not continuous, but rather fluctuates with the current regime. In regular markets,
increasing uncertainty reduces performance; in times of crisis, however, it can exacerbate volatility. Therefore, regime-aware
modeling frameworks are necessary for making prudent energy finance decisions because the predictive value of volatility,
whether as an amplifier or a warning signal, is strongly influenced by the underlying regime.
Furthermore, it is important to clarify that the regime numbering in the MSR model is not imposed ex-ante and carries no economic
meaning by itself. The model assigns Regime 1 and Regime 2 purely based on data-driven likelihood maximization, where regime
classification reflects the combined behavior of crude-oil returns and the sentiment derivatives. Consequently, the regime identified as
“turbulent” in behavioral terms does not necessarily correspond to the regime with the highest unconditional variance. In our
17

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
Fig. 5. Markov switching smoothed regime probabilities for MSR-MOVE (Daily Data, January 2002–April 2025).
Fig. 6. Markov switching smoothed regime probabilities for MSR- move 1 (Daily Data, January 2002–April 2025).
estimates, the sentiment-driven turbulent regime is characterized by rapid spikes in fear (VIX_V, VIX_A, MOVE_V) that generate short-
lived volatility bursts, while periods of persistent but moderate stress produce longer-lasting regimes with lower return variance. This
behavior is consistent with Markov-switching models where exogenous variables, rather than the dependent variable's variance, drive
regime transitions and produce short high-volatility spikes and long low-volatility regimes (Hamilton, 1994; Filardo, 1994). Thus, the
observed duration–volatility asymmetry reflects the dominance of sentiment dynamics in determining regime switches.
4.2.2.4. Model performance and comparative insights. The comparative model's accuracy shows that fear derivatives can explain more
than static data. We note that the MSR-VIX_V model has the highest overall precision with a log-likelihood of (cid:0) 7504.57 and an AIC of
2.649. Additionally, this dominated better than level-based MSR models such as MSR-MOVE (AIC =2.676, LogLik =(cid:0) 7579.59) and
MSR-VIX (AIC =2.677, LogLik =(cid:0) 7585.04). The increases of 80-90 log-likelihood units over level-based models results in a sig-
nificant increase in model likelihood. This reveals that sentiment derivatives include unique and useful information that static mea-
surements do not capture. This performance discrepancy highlights an important empirical insight. The change and momentum in fear,
rather than the degree of fear, better characterizes oil price trends. VIX_V and MOVE_V (velocity), as well as VIX_A and MOVE_A
(acceleration), accurately depict the rate and escalation of uncertainty. These indications are particularly valuable during tranquil
periods when markets are sensitive to early signs of stress. Controversy, static measures such as the VIX and MOVE act more like
lagging signals, indicating sentiment situations after they have already changed market outcomes.
Moreover, this difference in explanatory power has clear financial significance. From a risk management perspective, velocity and
acceleration derivatives provide early warning capabilities. It also enables decision-makers to act before the market fully absorbs a
18

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
Fig. 7. Markov switching smoothed regime probabilities for MSR- move 2 (Daily Data, January 2002–April 2025).
Fig. 8. Markov Switching Smoothed Regime Probabilities for MSR- MOVE_J (Daily Data, January 2002–April 2025). Note: For all figures, Regime 1
corresponds to tranquil, low-volatility periods, while Regime 2 captures turbulent, high-volatility states. Smoothed probabilities are derived from
two-state Markov Switching Regression models estimated using daily data from January 2002 to April 2025.
sentiment shock. This anticipatory advantage is especially useful in energy markets, where price changes can be nonlinear and abrupt.
For portfolio managers, our findings suggest that integrating sentiment derivatives into risk models could improve the timing and
effectiveness of hedging methods. Overall, the MSR framework emphasizes the necessity of understanding fear as a dynamic process
rather than a static situation. The derivatives of VIX and MOVE, particularly at the first and second order, capture the tempo of market
fear, providing richer, more forward-looking signals than their level-based peers. The large improvements in model fit, especially
under calm situations, demonstrate their utility as tools for proactive volatility forecasting and sentiment-driven trading strategies.
4.2.2.5. Financial significance and practical implications. The results of Markov Switching Regression have significant implications for
financial forecasting and risk management in crude oil markets. Crucially, the analysis demonstrates that the rate and acceleration of
market fear (i.e., their first- and second-order derivatives) have the greatest influence on oil return dynamics, particularly during
periods of market tranquility, rather than the level of fear (as captured by traditional volatility indices such as VIX or MOVE).
19

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
In calm regimes, sentiment derivatives such as VIX_V (velocity) and MOVE_V carry strong negative and statistically significant
coefficients, for example, (cid:0) 0.088 and (cid:0) 0.075, respectively (both p <0.001), indicating that early increases in fear sentiment are
predictive of declines in crude oil returns. Thus, we illustrate that this interaction demonstrates the strategic behavior of investors who
reposition or hedge their strategies in response to heightened uncertainty. Acceleration results reinforce this finding. We demonstrate
that the oil market is susceptible not only to changes in trends, but also to the magnitude with which these changes occur. This
explanatory ability confirms the forward-looking nature of fear derivatives. Under unstable regimes, static measures lack explanatory
power. They appear to have limits in terms of their usefulness in predicting sudden fluctuations. In contrast, derivative-enhanced
models capture the evolving dynamics of risk perception and provide earlier signals of potential market disruption, enabling timely
intervention and strategy realignment.
For practitioners, we indicate that these insights offer actionable value. Risk managers can integrate sentiment velocity and ac-
celeration into portfolio monitoring systems. This permits to anticipate volatility spikes and mitigate downside risk. Institutional
investors and commodity traders may deploy these metrics to inform asset allocation decisions, hedge energy exposures, or optimize
the timing of market entries and exits. The use of sentiment derivatives transforms sentiment analysis from a reactive diagnostic into a
proactive component of decision-making.
The statistical evidence further supports their inclusion. The MSR-VIX_V model, for instance, achieves the lowest Akaike Infor-
mation Criterion (AIC = 2.649) and the highest log-likelihood ((cid:0) 7504.57) among all tested specifications, outperforming static
benchmarks such as MSR-VIX (AIC =2.677) and MSR-MOVE (AIC =2.676). Referring to the above results, we affirm the superior fit
and explanatory power of models that incorporate the dynamic behavior of sentiment. From a policy and energy market perspective,
these findings caution against equating calm markets with stability. The significance of sentiment derivatives in tranquil regimes
demonstrates that even minor shifts in the pace of fear can precipitate meaningful price movements. It is more accurate to identify
underlying dangers and regime shifts by tracking the evolution of investor concern rather than just its appearance. In summary, the
MSR results demonstrate that fear's speed, rather than merely its existence, is having an increasing impact on contemporary financial
markets. Incorporating the speed and acceleration of emotions into forecasting frameworks promotes more responsive and immediate
strategies, enhances risk mitigation, improves forecasting accuracy, and more effectively copes with the speed and complexity of
contemporary markets, particularly in high-frequency and algorithmic trading contexts.
4.2.2.6. MSR models: regime-sensitive insights and enhanced forecasting power. The adoption of the MSR framework dramatically alters
this landscape. By allowing model parameters to shift according to latent regimes (tranquil vs. turbulent), the explanatory value of
dynamic sentiment derivatives becomes evident. Referring to Table 9, the Wald statistics for MSR-VIX_A (Wald =159.69, p <0.001)
and MSR-VIX_J (Wald =21.67, p <0.001) show strong statistical significance, confirming that the acceleration and jerk of equity
market fear sentiment are powerful predictors of crude oil returns, particularly when regime dynamics are incorporated. MSR-VIX_V
also shows significance (Wald =7.72, p =0.021), indicating that even sentiment velocity plays an important role. Notably, in the bond
market channel, only MSR-MOVE_J (Wald =26.45, p <0.001) shows strong significance, while MOVE_V and MOVE_A remain sta-
tistically insignificant. This underlines that only higher-order shocks in bond market fear, such as rapid acceleration of volatility,
transmit meaningfully to crude oil returns.
Furthermore, the static MOVE index loses explanatory power in the MSR framework (Wald =5.97, p =0.506), contrasting sharply
with its significance under SSR. This contrast reinforces the central hypothesis of this study: when accounting for regime-switching
behavior, static sentiment indicators underperform derivative-based measures in capturing early warning signals of oil market stress.
In addition, Wald test results in the variance equations are highly significant for all models (p <0.001), with statistics ranging from
1103 to 1248. These results indicate that financial sentiment, whether static or dynamic, exerts a consistently strong influence on crude
oil return volatility. Thus, while the predictive power of sentiment for returns varies with model structure and regime, its impact on
return variance is universally robust.
Table 9
Wald test results.
Independent Variables VIX VIX_V VIX_A VIX_J MOVE MOVE_V MOVE_A MOVE_J
Simple Switching Regression
Wald test(In mean) 26.553 1.708 1.852 2.325 6.607 2.123 2.395 2.543
0.000 0.426 0.396 0.327 0.037 0.346 0.302 0.280
Wald test(In variance) 1206.432 1175.499 1196.469 1198.901 1199.054 1190.321 1192.210 1197.808
0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
Markov Switching Regression
Wald test(In mean) 7.720 159.691 21.673 2.198 3.901 26.452 16.271 5.966
0.021 0.000 0.000 0.333 0.142 0.000 0.000 0.506
Wald test(In variance) 1103.378 1219.272 1242.204 1248.417 1233.767 1200.658 1246.529 1241.910
0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
Note: The table shows how well crude oil returns are explained by using VIX, MOVE, and their first-, second-, and third-order derivatives (VIX_V to
VIX_J and MOVE_V to MOVE_J). It shows Wald test results for the SSR and the MSR. The "Wald test (In variance)" shows the explanatory power of
sentiment indicators over return volatility; the "Wald test (In mean)" seeks whether sentiment indicators appreciably influence mean return pre-
diction. The values combine test statistics and related p-values. Strong statistical evidence indicating that the variable significantly affects returns or
volatility comes from a p-value less than 0.05.
20

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
Based on these findings, we confirm the superiority of regime-sensitive models to identify the sentiment-return linkages and to
validate the use of higher-order sentiment dynamics as forward-looking indicators of oil price behavior. They also highlight the
asymmetry in transmission channels between equity (VIX) and bond (MOVE) markets, with the former showing broader derivative-
based significance. Furthermore, this evidence enhances the rationale for including emotion derivatives into nonlinear models like
MSR to better predict and manage regime shifts in energy markets. Overall, the Wald test statistics for both the Single-Switching
Regression and Markov Switching Regression frameworks provide important insights into the regime-dependent importance of
sentiment variables in crude oil return modeling.
In the SSR context, only the static sentiment measures, VIX and MOVE, show statistically significant influence on returns (Wald =
26.55 and 6.60, respectively). While the first-to third-order derivatives (VIX_V to VIX_J and MOVE_V to MOVE_J) fail to demonstrate
explanatory power. However, under the MSR specification, which captures regime-switching behavior, we observe that the predictive
value of sentiment derivatives becomes evident. Findings are particularly notable for MSR-VIX_A (Wald =159.69), MSR-VIX_J (Wald
=21.67), and MSR-MOVE_J (Wald =26.45). This demonstrates how acceleration and jerk indicators predominate when taking market
regimes into consideration.
These findings have huge financial repercussions. First, they support the idea that markets react not only to anxiety levels but also
to their temporal evolution, as measured by sentiment indices' velocity, acceleration, and jerk. This is especially important under
tranquil regimes, when early spikes in fear momentum can serve as warning signs of price reversals. Second, they show the limitations
of linear models in detecting nonlinear dynamics in real-world financial markets. The regime-sensitive MSR paradigm is critical in
revealing the asymmetric and regime-dependent behavior of oil returns in response to shifting sentiment conditions. For practitioners,
this suggests that integrating higher-order sentiment dynamics into forecasting and risk management models can enhance portfolio
responsiveness, improve hedge timing, and strengthen early warning systems for volatility spikes. Also, financial institutions should
integrate regime-sensitive sentiment analytics into forecasting models and use MSR frameworks to identify regime shifts in real time.
This enhances exposure management, asset allocation, and proactive hedging. From an energetic perspective, the results show that the
emotion of financial markets is increasingly driving the volatility of oil prices, especially in quiet times where fear feeling steadily
builds up before causing regime shifts. Monitoring derivative-based sentiment metrics can help policymakers and energy-intensive
sectors make strategic adjustments to energy procurement, refining schedules, or hedging positions before volatility manifests. The
importance of the MOVE index also highlights how monetary policy expectations and bond market uncertainties affect oil demand and
capital allocation choices in commodity markets. Collectively, these observations highlight how crucial it is to manage energy risk and
maintain macro-financial stability through a multifaceted, regime-aware approach. Also, Energy firms and policymakers can use VIX_A
and MOVE_J as early-warning tools to anticipate and prepare for oil market disruptions before supply-demand fundamentals are
impacted.
5. Robustness analysis
To strengthen the empirical reliability of the proposed framework, we conduct a robustness analysis along two complementary
dimensions. First, we evaluate the out-of-sample predictive performance of the sentiment-derivative models. Second, we assess the
structural stability of the sentiment effects by incorporating additional macroeconomic, liquidity, and geopolitical controls into the
MSR specification. Third, we extend our robustness analysis by assessing whether cyclical or seasonal patterns influence regime
behavior in crude-oil returns.
5.1. Out-of-sample forecasting
The out-of-sample forecasting exercise (Table 10) provides strong empirical validation for the behavioral–regime-switching
structure proposed in this study. By estimating the MSR models over the first 80 % of the sample (November 2002–December 2021)
and forecasting crude-oil returns recursively over the final 20 % (January 2022–April 2025), we assess whether sentiment derivatives
Table 10
Out-of-sample performance results.
Independent variables Dependent variable RMSE MAE
VIX(-1) RTOP 0.9781 0.7198
VIX_V(-1) RTOP 0.9753 0.7178
VIX_A(-1) RTOP 0.9769 0.7197
VIX_J(-1) RTOP 0.9775 0.7204
MOVE(-1) RTOP 0.9786 0.7197
MOVE_V(-1) RTOP 0.9776 0.7208
MOVE_A(-1) RTOP 0.9777 0.7206
MOVE_J(-1) RTOP 0.9776 0.7206
Notes: This table reports one-step-ahead out-of-sample forecasting performance based on an 80%–20% rolling-window split using daily
data from November 2002 to April 2025. RTOP denotes Brent crude oil returns. VIX_V, VIX_A, and VIX_J represent the velocity, ac-
celeration, and jerk (first-, second-, and third-order derivatives) of the VIX index; MOVE_V, MOVE_A, and MOVE_J correspond to the
same derivatives of the MOVE index. RMSE and MAE measure forecast accuracy, with lower values indicating better predictive per-
formance. Among all specifications, sentiment velocity models (VIX_V and MOVE_V) deliver the strongest forecasting results.
21

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
contain forward-looking information that remains useful outside the estimation sample. The key finding is that sentiment velocity,
captured by VIX_V and MOVE_V, delivers the most accurate forecasts, with VIX_V achieving the lowest RMSE (0.9753) and MAE
(0.7178) among all specifications. This reinforces the central result from the in-sample MSR estimation: it is not the level of fear that
matters for predicting oil returns, but the pace at which fear builds or dissipates. This result is intuitive from a behavioral-finance
standpoint. Changes in volatility expectations often precede significant capital reallocations and liquidity adjustments. Higher-
order dynamics such as velocity and acceleration represent early signals of psychological changes, investors begin to hedge or un-
wind positions before the level of fear peaks. Such proactive behaviour creates short-term predictability that can be measured, which
fixed sentiment indicators cannot capture. The superiority of VIX_V particularly indicates that fear in the stock market reacts more
quickly and sharply than uncertainty in the bond market when global risk perceptions change, which aligns with the literature on
cross-asset contagion and the leading role of stocks in transmitting global pressures. Models based on the MOVE index also improve
compared to their level counterparts, although the gains are relatively smaller compared to VIX derivatives. This contrast reflects the
results of the MSR that uncertainty in the bond market (MOVE) is more significant under stable conditions, but shocks driven by
sentiment in the stock market dominate during transitions to turbulent periods. The out-of-sample accuracy of VIX_V therefore cor-
roborates the MSR evidence that equity-market fear is the primary driver of regime shifts, while bond-market signals play a secondary
but still meaningful role. The Diebold–Mariano tests further confirm that these improvements are not due to randomness: in nearly all
pairwise comparisons, the derivative-based models significantly outperform the corresponding level-based models at the 5 % level.
This finding rules out the possibility that sentiment derivatives merely add noise or overfit in-sample dynamics. Instead, they contain
genuine predictive structure that persists even in a real-time forecasting environment, including during the highly volatile events of
2022–2025 (energy-supply disruptions, post-pandemic inflation, and monetary tightening cycles). These results also align closely with
the information-saturation hypothesis developed in the MSR analysis. Under turbulent regimes, fear levels are already elevated and
compressed near their upper bounds, providing little incremental forecasting power. In contrast, during tranquil regimes, where the
MSR models showed the strongest significance of sentiment derivatives, the velocity and acceleration of fear provide critical early-
warning signals that markets are transitioning toward instability. The fact that VIX_V delivers the best forecasting accuracy across
the entire hold-out period, which includes both calm and turbulent episodes, highlights how sentiment momentum bridges the
behavioral asymmetry across regimes.Taken together, the out-of-sample evaluation demonstrates that the sentiment-momen-
tum–enhanced MSR model is not only statistically sound but also forecast-relevant, offering real gains for practitioners. Traders and
risk managers can integrate these signals into position-sizing and hedging strategies, while policymakers can monitor sentiment ve-
locity as a preemptive indicator of rising market fragility. Overall, the forecasting results confirm that the proposed framework
captures a stable behavioral mechanism that persists both inside and outside the estimation sample, underscoring the practical value of
incorporating higher-order sentiment dynamics into regime-based oil return modelling.
5.2. Control-variable robustness
To assess whether the influence of sentiment derivatives is driven by omitted macro-financial or geopolitical variables, we augment
the baseline MSR specifications by introducing two widely used exogenous controls: the U.S. Dollar Index (DXY), representing global
liquidity and exchange-rate pressure, and the Geopolitical Risk Index (GPR), capturing exogenous geopolitical shocks. As shown in
Tables 11 and 12, these controls are incorporated individually and jointly for each group of sentiment derivatives (VIX, VIX_V to VIX_J,
MOVE, MOVE_V to MOVE_J), allowing us to evaluate the stability of sentiment effects and the resilience of the regime-switching
structure.
Across all specifications, the sentiment coefficients remain remarkably stable in both magnitude and significance, particularly in
Regime 1, where sentiment dynamics dominate crude-oil return behavior.For instance, VIX_V remains strongly significant in Regime 1
under all control configurations (p <0.001). The coefficients range from (cid:0) 0.0880 to (cid:0) 0.0895 depending on whether DXY, GPR, or
both are introduced. Similarly, MOVE_V retains its high significance in Regime 1 across all models (p ≤0.0001). The coefficient values
are consistently around (cid:0) 0.075. These results confirm that sentiment velocity remains the most robust predictor. It is not unaffected by
macro-financial or geopolitical adjustments.
The acceleration components (VIX_A and MOVE_A) also maintain their significance in Regime 1, though with smaller magnitudes,
while jerk terms (VIX_J, MOVE_J) remain generally insignificant, consistent with the theoretical expectation that higher-order de-
rivatives carry diminishing informational value. Importantly, the control variables themselves are rarely significant. For example, DXY
displays p-values well above conventional thresholds (0.13–0.63). In addition, the GPR consistently exhibits non-significance (p >
0.11). This indicates that these variables do not materially explain regime-specific crude-oil returns within the MSR framework.
Furthermore, the transition probabilities and regime-specific variances remain virtually unchanged after adding DXY and GPR. In
every extended specification, Regime 1 continues to reflect a low-variance, sentiment-sensitive regime. Regime 2, however, preserves
its high-variance characteristics. Overall, we indicate that the persistence of these structural features demonstrates that the MSR
classification is not driven by macro-financial or geopolitical conditions, but by the dynamics of sentiment itself.
Taken together, the robustness analysis reveals that the regime-dependent role of sentiment dynamics, particularly the velocity of
fear, remains statistically significant, economically meaningful, and structurally stable even after accounting for global liquidity (DXY)
and geopolitical tensions (GPR). These results show that emotional momentum is not the result of neglected variables but rather a
continuous behavioural transmission mechanism that affects the dynamics of the crude oil market in the short term. Referring to this
finding, we illustrate that that policymakers should monitor sentiment-based indicators as early-warning tools for detecting transitions
from tranquil to turbulent market regimes. These emotional effects are still important even when you take into account liquidity (DXY)
and geopolitical tensions (GPR). This means that looking only at fundamentals is not enough to predict short-term instability in the oil
22

Table 11
Structural Robustness of MSR Models with Macro-Financial and Geopolitical Controls: VIX case.
Specification Sentiment Derivatives Controls Added Regime 1 Regime 2 Control variables
Included Sentiment Prob log(σ t ) Prob Sentiment Prob log(σ t ) Prob GPR Prob DXY Prob
Baseline MSR VIX None (cid:0) 0.0050 0.0490 (cid:0) 0.2240 0.0000 (cid:0) 0.0150 0.9260 1.1440 0.0000 - - - -
MSR +DXY USD Index (cid:0) 0.0070 0.0013 (cid:0) 0.2128 0.0000 (cid:0) 0.0285 0.0047 1.1128 0.0000 - - (cid:0) 0.0019 0.1312
MSR +GPR Geopolitical (cid:0) 0.0064 0.0030 (cid:0) 0.2139 0.0000 (cid:0) 0.0287 0.0044 1.1112 0.0000 (cid:0) 0.0004 0.1164 - -
Risk
Full Controls: DXY + All two (cid:0) 0.0069 0.0017 (cid:0) 0.2131 0.0000 (cid:0) 0.0288 0.0043 1.1124 0.0000 (cid:0) 0.0003 0.2540 (cid:0) 0.0014 0.2947
GPR
Baseline MSR Velocity(VIX_V) None (cid:0) 0.0880 0.0000 (cid:0) 0.2270 0.0000 (cid:0) 0.1810 0.1670 1.0880 0.0000 - - - -
MSR +DXY USD Index (cid:0) 0.0894 0.0000 (cid:0) 0.2274 0.0000 (cid:0) 0.1815 0.0000 1.0875 0.0000 - - (cid:0) 0.0011 0.3333
MSR +GPR Geopolitical (cid:0) 0.0881 0.0000 (cid:0) 0.2276 0.0000 (cid:0) 0.1811 0.0000 1.0875 0.0000 (cid:0) 0.0004 0.1218 - -
Risk
Full Controls: DXY + All two (cid:0) 0.1812 0.0000 1.0872 0.0000 (cid:0) 0.0895 0.0000 (cid:0) 0.2278 0.0000 (cid:0) 0.0003 0.2013 (cid:0) 0.0006 0.6318
GPR
Baseline MSR Acceleration(VIX_A) None (cid:0) 0.0200 0.0000 (cid:0) 0.2190 0.0000 (cid:0) 0.0570 0.0130 1.0890 0.0000 - - - -
MSR +DXY USD Index (cid:0) 0.0572 0.0129 1.0886 0.0000 (cid:0) 0.0204 0.0001 (cid:0) 0.2184 0.0000 - - (cid:0) 0.0012 0.3272
MSR +GPR Geopolitical (cid:0) 0.0570 0.0131 1.0882 0.0000 (cid:0) 0.0199 0.0001 (cid:0) 0.2194 0.0000 (cid:0) 0.0004 0.1279 - -
Risk
Full Controls: DXY + All two (cid:0) 0.0570 0.0130 1.0879 0.0000 (cid:0) 0.0205 0.0001 (cid:0) 0.2190 0.0000 (cid:0) 0.0003 0.2208 (cid:0) 0.0006 0.6210
GPR Baseline MSR JERK(VIX_J) None (cid:0) 0.0160 0.2340 1.0950 0.0000 (cid:0) 0.0010 0.3910 (cid:0) 0.2160 0.0000 - - - -
MSR +DXY USD Index (cid:0) 0.0155 0.2324 1.0947 0.0000 (cid:0) 0.0027 0.3657 (cid:0) 0.2155 0.0000 - - (cid:0) 0.0012 0.3162
MSR +GPR Geopolitical (cid:0) 0.0154 0.2351 1.0942 0.0000 (cid:0) 0.0026 0.3786 (cid:0) 0.2167 0.0000 (cid:0) 0.0004 0.1321 - -
Risk
Full Controls: DXY + All two (cid:0) 0.0155 0.2340 1.0941 0.0000 (cid:0) 0.0027 0.3550 (cid:0) 0.2161 0.0000 (cid:0) 0.0003 0.2358 (cid:0) 0.0007 0.5920
GPR
Note: This table reports the structural robustness of the MSR models using VIX-based sentiment measures (VIX, VIX_V to VIX_J) when including macro-financial and geopolitical controls. Regime 1 denotes
tranquil, low-volatility periods; Regime 2 denotes turbulent, high-volatility periods. GPR =Geopolitical Risk Index; DXY =U.S. Dollar Index. Sentiment derivatives represent VIX velocity (VIX_V),
acceleration (VIX_A), and jerk (VIX_J). Prob. refers to p-values of estimated coefficients. Estimates are based on daily data from January 2002 to April 2025.
23
K.
Tissaoui
and
N.
Azibi
I n t e r n
a t i o
n a
l
R
e v i e w
o
f
E
c o
n o m
i c s
a
n
d
F
in
a
n
c e
1
0
8
(2026)
105197

K. Tissaoui and N. Azibi                                                                                                                     I n  t e  r n  a t i o  n  a  l   R  e v  i e w     o f   E  c  o  n o  m   i c s   a  n  d    F  in  a  n  c e    1  0 8 (2026) 105197
Table 12
Structural Robustness of MSR Models with Macro-Financial and Geopolitical Controls: MOVE case.
Specification Sentiment Derivatives  Controls Added Regime 1 Regime 2 Control variables
|     | Included |                | log(σ ) |                | log(σ ) |          |          |
| --- | -------- | -------------- | ------- | -------------- | ------- | -------- | -------- |
|     |          | Sentiment Prob | t Prob  | Sentiment Prob | t Prob  | GPR Prob | DXY Prob |
Baseline MSR MOVE None (cid:0) 0.0060 0.0491 1.0920 0.0000 0.0000 0.9258 (cid:0) 0.2150 0.0000 - - - -
MSR +DXY USD Index (cid:0) 2.26E-  0.9511 (cid:0) 0.2143 0.0000 (cid:0) 0.0061 0.0408 1.0911 0.0000 ​ ​ (cid:0) 0.0014 0.2609
05
MSR +GPR Geopolitical  (cid:0) 0.0060 0.0456 1.0903 0.0000 0.0001 0.8571 (cid:0) 0.2155 0.0000 (cid:0) 0.0004 0.1288 - -
Risk
| Full Controls: DXY + |     | (cid:0) |     |     | (cid:0) | (cid:0) | (cid:0) |
| -------------------- | --- | ------- | --- | --- | ------- | ------- | ------- |
All two 0.0061 0.0414 1.0902 0.0000 0.0001 0.9020 0.2148 0.0000 0.0003 0.2493 0.0009 0.5030
GPR
Baseline MSR Velocity(MOVE_V) None (cid:0) 0.0750 0.0000 1.0830 0.0000 (cid:0) 0.0100 0.0010 (cid:0) 0.2170 0.0000 - - - -
MSR +DXY USD Index (cid:0) 0.0751 0.0001 1.0757 0.0000 (cid:0) 0.0099 0.0013 (cid:0) 0.2178 0.0000 - - (cid:0) 0.0024 0.0508
| MSR +GPR |     | (cid:0) |     | (cid:0) | (cid:0) | (cid:0) |     |
| -------- | --- | ------- | --- | ------- | ------- | ------- | --- |
Geopolitical  0.0741 0.0001 1.0815 0.0000 0.0102 0.0009 0.2177 0.0000 0.0004 0.1284 - -
Risk
24  Full Controls: DXY + All two (cid:0) 0.0102 0.0009 (cid:0) 0.2166 0.0000 (cid:0) 0.0745 0.0001 1.0835 0.0000 0.0001 0.5779 (cid:0) 0.0012 0.3416
GPR
|     |     | (cid:0) |     | (cid:0) | (cid:0) |     |     |
| --- | --- | ------- | --- | ------- | ------- | --- | --- |
Baseline MSR Acceleration(MOVE_A) None 0.0540 0.0000 1.0670 0.0000 0.0030 0.1580 0.2150 0.0000 - - - -
MSR +DXY USD Index (cid:0) 0.0038 0.0691 (cid:0) 0.2127 0.0000 (cid:0) 0.0522 0.0019 1.1391 0.0000 - - (cid:0) 0.0013 0.2844
MSR +GPR Geopolitical  (cid:0) 0.0027 0.1984 (cid:0) 0.2171 0.0000 (cid:0) 0.0488 0.0009 1.0797 0.0000 (cid:0) 0.0004 0.1377 - -
Risk
Full Controls: DXY + All two (cid:0) 0.0025 0.2294 (cid:0) 0.2164 0.0000 (cid:0) 0.0488 0.0009 1.0795 0.0000 (cid:0) 0.0003 0.2420 (cid:0) 0.0007 0.5761
GPR
|     |     | (cid:0) |     | (cid:0) | (cid:0) |     |     |
| --- | --- | ------- | --- | ------- | ------- | --- | --- |
Baseline MSR JERK(MOVE_J) None 0.0210 0.0180 1.0890 0.0000 0.0010 0.5840 0.2160 0.0000 - - - -
| MSR +DXY |     | (cid:0) |     | (cid:0) | (cid:0) |     | (cid:0) |
| -------- | --- | ------- | --- | ------- | ------- | --- | ------- |
USD Index 0.02124 0.0173 1.0897 0.0000 0.0007 0.5649 0.2155 0.0000 - - 0.0010 0.3905
MSR +GPR Geopolitical  (cid:0) 0.0210 0.0182 1.0878 0.0000 (cid:0) 0.0007 0.5868 (cid:0) 0.2166 0.0000 (cid:0) 0.0004 0.1376 - -
Risk
| Full Controls: DXY + |     | (cid:0) | (cid:0) | (cid:0) |     | (cid:0) | (cid:0) |
| -------------------- | --- | ------- | ------- | ------- | --- | ------- | ------- |
All two 0.0007 0.5665 0.2158 0.0000 0.0212 0.0175 1.0893 0.0000 0.0002 0.3487 0.0006 0.6133
GPR
Note: This table presents structural robustness checks for MSR models using MOVE-based sentiment measures (MOVE, MOVE_V to MOVE_J) with macro-financial and geopolitical controls. Regime 1
corresponds to the calm, low-variance state; Regime 2 captures the turbulent, high-variance state. MOVE_V–MOVE_J denote the first-, second-, and third-order derivatives (velocity, acceleration, jerk).
Control variables include the Geopolitical Risk Index (GPR) and the U.S. Dollar Index (DXY). Prob. refers to p-values. All estimates rely on daily data from January 2002 to April 2025.

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
market. So, regulators, central banks, and energy agencies should add measures of emotional dynamics to their risk monitoring
systems, macroprudential stress tests, and plans for keeping the oil market stable. The strength of these indicators suggests that traders
should include emotional momentum signals in their hedging, portfolio allocation, and derivative pricing to better protect themselves
against sudden spikes in volatility. In general, sentiment derivatives are a useful and forward-looking addition to monitoring
fundamental and geopolitical factors when making energy market policies.
5.3. Seasonal and cyclical robustness (Fourier-augmented MSR)
As shown in Tables 13 and 14, the findings from the Fourier-augmented MSR provide additional insight into the structural forces
governing regime transitions in crude-oil markets. The remarkable stability of the sentiment coefficients across all specifications, both
in magnitude and statistical significance, underscores the dominant role played by sentiment momentum rather than deterministic
periodicity. The fact that the Regime 1 VIX effect changes minimally (from (cid:0) 0.0050, p =0.049, to (cid:0) 0.0067, p =0.0014) despite the
introduction of four additional harmonic regressors indicates that the underlying behavioral relationship is not confounded by sea-
sonal factors. This structural robustness is further supported by the persistence of the Regime 2 impact, where the negative reaction to
fear dynamics remains large ((cid:0) 0.2240 vs. (cid:0) 0.2148, both p <0.001). Such consistency suggests that regime behavior in oil markets is
shaped not by predictable cyclical forces, but by rapid and nonlinear shifts in risk sentiment, reflected in the higher-order dynamics of
VIX and MOVE, which exert immediate and asymmetric pressure during both calm and volatile phases.
Similar patterns emerge for the derivative-based specifications. For example, the acceleration of fear (VIX_A) exhibits an almost
identical magnitude before and after adding Fourier terms (Regime 1 coefficient near (cid:0) 0.057 with p ≈0.013, Regime 2 coefficient
fixed around (cid:0) 0.219 with p < 0.001). These dynamics reveal that the predictive information embedded in fear acceleration is
inherently structural and does not depend on cyclical timing. This reinforces a key behavioral insight: higher-order changes in fear,
velocity, acceleration, and jerk, capture the speed and intensity of shifts in market psychology, which are far more consequential for
regime transitions than recurring seasonal fluctuations.
By contrast, the Fourier variables themselves display only limited explanatory power. The annual cosine term C_1appears
marginally significant in a handful of models (e.g., (cid:0) 0.0391, p =0.016 in the VIX model), indicating the presence of mild annual
regularities. However, the absence of significance in the sine component S_1, combined with the complete insignificance of the
semiannual harmonics C_2 and S_2 (all p-values >0.30), suggests that any seasonal pattern is weak, symmetric, and economically
trivial. The Fourier structure captures smooth seasonal oscillations, but these oscillations do not interact with or alter the deeper
behavioral mechanisms encoded in sentiment momentum.
Just as importantly, the key structural features of the MSR remain virtually unchanged after introducing Fourier harmonics. The
conditional variance in Regime 1 stays tightly concentrated (log σ ≈(cid:0) 0.215). This indicates that the calm state maintains its low-
volatility nature regardless of seasonal dynamics. Conversely, the high-volatility Regime 2 continues to exhibit large and persistent
shocks (log σ ≈1.09–1.10). It reinforces the notion that turbulent regimes are driven by stress-induced amplification rather than
seasonality. Transition probabilities also remain fundamentally unaltered: the tranquil state is still highly persistent (p11 ≈ 0.99,
implied by P11-C ≈4.91), while the turbulent regime remains short-lived (p22 ≈0.91, implied by P21-C ≈(cid:0) 2.27). If seasonal effects
were meaningful drivers of regime switching, one would expect notable changes in persistence, switching frequency, or the duration
structure of regimes. The empirical evidence here shows none.
We collectively emphasize that these findings converge on a coherent conclusion. Crude oil markets do show some mild cyclical
patterns. It can be seen in a small annual harmonic. However, the timing and strength of regime shifts are not controlled by these
predictable periodic forces. Instead, regime changes are mostly affected by nonlinear and psychologically amplified changes in
investor fear. These changes spread across markets through behavioral contagion and cross-asset volatility spillovers. The Fourier
analysis thus supports the behavioral underpinnings of the MSR model. It reinforces the assertion that the model detects real
sentiment-driven structural breaks as rather than seasonal anomalies.
6. Conclusion and policy implications
This paper provides a comprehensive investigation into the regime-contingent effects of financial fear sentiment on crude oil return
dynamics. We employ both static measures (VIX and MOVE) and their higher-order derivatives, velocity, acceleration, and jerk, within
a dual modeling framework of Simple and Markov Switching Regression (SSR/MSR). The empirical evidence confirms that sentiment
is not only a valuable predictor of oil price behavior but that its dynamic properties, how rapidly it changes, hold greater predictive
power than its mere presence.
Among the most significant findings is the clear regime asymmetry in the way sentiment affects crude oil returns. Crude oil returns
are significantly impacted negatively by the first and second derivatives of VIX and MOVE (i.e., velocity and acceleration) during times
of market calm (Regime 1). These findings provide insight into increased investor sensitivity to the rate of fear intensification in stable
settings, where markets remain vigilant for early warning signals. In turbulent regimes, the explanatory power of these derivatives
diminishes considerably. This paper confirms the information saturation hypothesis, which indicates that high volatility reduces the
marginal informational content of fear signals. In these cases, the oil market responds to structural or macroeconomic shocks rather
than behavioral or feelings. Thus, we contribute to the corpus of literature on sentiment-oil price correlations in a variety of significant
ways. Das, Dutta, Jana, and Ghosh (2023), for example, showed a link between oil market volatility and financial stress during crises,
despite the fact that they primarily utilized static measurements or linear methodologies that did not allow for nonlinear transitions
between regimes. Our work builds on these foundations by introducing sentiment derivatives and leveraging the flexibility of the MSR
25

Table 13
Seasonal and Cyclical Robustness: Fourier-Augmented Markov Switching Regression Estimates: VIX case.
Specification Sentiment Fourier Regime 1 Regime 2 Fourier variables Added
D In e c r l i u v d a e ti d ves variables Added Sentiment Prob log(σ t ) Prob Sentiment Prob log(σ t ) Prob C1 Prob C2 Prob S1 Prob S2 Prob
Baseline MSR VIX None (cid:0) 0.0050 0.0490 (cid:0) 0.2240 0.0000 (cid:0) 0.0150 0.9260 1.1440 0.0000 - - - - - - - -
Fourier C1,C2,S1,S2 (cid:0) 0.0067 0.0014 (cid:0) 0.2148 0.0000 (cid:0) 0.0275 0.0066 1.1141 0.0000 (cid:0) 0.0391 0.0164 (cid:0) 0.0165 0.3095 (cid:0) 0.0035 0.8318 (cid:0) 0.0142 0.3855
variables
Baseline MSR Velocity(VIX_V) None (cid:0) 0.0880 0.0000 (cid:0) 0.2270 0.0000 (cid:0) 0.1810 0.1670 1.0880 0.0000 - - - - - - - -
Fourier C1,C2,S1,S2 (cid:0) 0.1817 0.0000 1.0876 0.0000 (cid:0) 0.0878 0.0000 (cid:0) 0.2285 0.0000 (cid:0) 0.0329 0.0359 (cid:0) 0.0124 0.4342 (cid:0) 0.0076 0.6327 (cid:0) 0.0186 0.2378
variables
Baseline MSR Acceleration None (cid:0) 0.0200 0.0000 (cid:0) 0.2190 0.0000 (cid:0) 0.0570 0.0130 1.0890 0.0000 - - - - - - - -
Fourier (VIX_A) C1,C2,S1,S2 (cid:0) 0.0574 0.0133 1.0910 0.0000 (cid:0) 0.0199 0.0001 (cid:0) 0.2200 0.0000 (cid:0) 0.0349 0.0299 (cid:0) 0.0148 0.3557 (cid:0) 0.0071 0.6586 (cid:0) 0.019 0.238993
variables
Baseline MSR JERK(VIX_J) None (cid:0) 0.0160 0.2340 1.0950 0.0000 (cid:0) 0.0010 0.3910 (cid:0) 0.2160 0.0000 - - - - - - - -
Fourier C1,C2,S1,S2 (cid:0) 0.0155 0.2356 1.0969 0.0000 (cid:0) 0.0025 0.3851 (cid:0) 0.2174 0.0000 (cid:0) 0.034 0.032 (cid:0) 0.015 0.355 (cid:0) 0.00714 0.660267 (cid:0) 0.0187 0.24747
variables
Note: This table reports the seasonal and cyclical robustness of VIX-based MSR models after including Fourier harmonic terms. C1 and S1 represent annual cosine and sine components; C2 and S2 represent
semiannual cosine and sine components. Regime 1 is the tranquil, low-volatility state, and Regime 2 is the turbulent state. Sentiment derivatives (VIX_V to VIX_J) correspond to velocity, acceleration, and
jerk. P-values are reported under “Prob.” The models are estimated using daily data from January 2002 to April 2025.
26
K.
Tissaoui
and
N.
Azibi
I n t e r n
a t i o
n a
l
R e v i e w
o
f
E
c o
n
o
m
i c s
a
n
d
F
in
a
n
c e
1
0
8
(2026)
105197

K. Tissaoui and N. Azibi                                                                                                                     I n  t e  r n  a t i o  n  a  l   R  e v  i e w     o f   E  c  o  n o  m   i c s   a  n  d    F  in  a  n  c e    1  0 8 (2026) 105197
Table 14
Seasonal and Cyclical Robustness: Fourier-Augmented Markov Switching Regression Estimates: MOVE case.
Specification Sentiment  Fourier  Regime 1 Regime 2 Fourier variables Added
| D e r i v a ti ves  | v a r ia b les  |     |     |     |     |     |     |     |
| ------------------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
Sentiment Prob log(σ ) Prob Sentiment Prob log(σ ) Prob C1 Prob C2 Prob S1 Prob S2 Prob
| In c l u d e d | A d d e d | t   |         | t       |     |     |     |     |
| -------------- | --------- | --- | ------- | ------- | --- | --- | --- | --- |
|                | (cid:0)   |     | (cid:0) | (cid:0) |     |     |     |     |
Baseline MSR MOVE None 0.0060 0.0491 1.0920 0.0000 0.00004 0.9258 0.2150 0.0000 - - - - - - - -
Fourier  C1,C2,S1,S2 (cid:0) 1.75E-  0.7020 (cid:0) 0.2163 0.0000 (cid:0) 0.0059 0.0543 1.0953 0.0000 (cid:0) 0.0349 0.0309 (cid:0) 0.0154 0.3356 (cid:0) 0.0076 0.6404 (cid:0) 0.0179 0.2677
variables 04
Baseline MSR Velocity  None (cid:0) 0.0750 0.0000 1.0830 0.0000 (cid:0) 0.0100 0.0010 (cid:0) 0.2170 0.0000 - - - - - - - -
|     | (cid:0) |     | (cid:0) | (cid:0) | (cid:0) | (cid:0) | (cid:0) | (cid:0) |
| --- | ------- | --- | ------- | ------- | ------- | ------- | ------- | ------- |
27  Fourier  (MOVE_V) C1,C2,S1,S2 0.0744 0.0001 1.0845 0.0000 0.0103 0.0007 0.2185 0.0000 0.036 0.026 0.014 0.401 0.0074 0.6507 0.0187 0.2488
variables
Baseline MSR Acceleration  None (cid:0) 0.0540 0.0000 1.0670 0.0000 (cid:0) 0.0030 0.1580 (cid:0) 0.2150 0.0000 - - - - - - - -
|     | (cid:0) | (cid:0) | (cid:0) |     | (cid:0) | (cid:0) | (cid:0) | (cid:0) |
| --- | ------- | ------- | ------- | --- | ------- | ------- | ------- | ------- |
Fourier  (MOVE_A) C1,C2,S1,S2 0.0028 0.1855 0.2178 0.0000 0.0490 0.0009 1.0824 0.0000 0.034 0.032 0.015 0.356 0.0071 0.6617 0.01867 0.248487
variables
Baseline MSR JERK(MOVE_J) None (cid:0) 0.0210 0.0180 1.0890 0.0000 (cid:0) 0.0010 0.5840 (cid:0) 0.2160 0.0000 - - - - - - - -
Fourier  C1,C2,S1,S2 (cid:0) 0.02111 0.0188 1.0904 0.0000 (cid:0) 0.0007 0.5667 (cid:0) 0.2173 0.0000 (cid:0) 0.034 0.032 (cid:0) 0.015 0.356 (cid:0) 0.00712 0.664321 (cid:0) 0.01858 0.251606
variables
Note: This table shows Fourier-augmented robustness results for MOVE-based MSR models. Seasonal terms include C1 (annual cosine), S1 (annual sine), C2 (semiannual cosine), and S2 (semiannual sine).
MOVE_V to MOVE_J measure the velocity, acceleration, and jerk of MOVE. Regime 1 represents stable, low-volatility periods, while Regime 2 captures turbulent conditions. Prob. denotes p-values. All
results are computed using daily observations from January 2002 to April 2025.

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
model to detect latent shifts in behavior. In doing so, we demonstrate that the momentum of sentiment, particularly in equity markets
(as captured by VIX_V and VIX_A), consistently outperforms static measures level-based VIX/MOVE when explaining oil return
fluctuations.
Notably, our results contrast with those of Abdollahi (2023), who focused on semantic sentiment extracted from news and social
media using NLP-enhanced BiLSTM-GARCH models. While that line of research emphasised the role of media-based sentiment in
volatility forecasting, our findings indicate that financial market-derived metrics, particularly sentiment velocity, offer more
comprehensive and systematic predictive capabilities when considered through a regime-switching lens. Furthermore, we discover
that the third derivative (jerk) introduces statistical noise rather than explanatory clarity, supporting the theory that predictive value
peaks at the second degree of sentiment change.
From a modeling perspective, the MSR framework significantly enhances the explanatory scope of sentiment indices by allowing
the structure of relationships to evolve endogenously. The MSR-VIX_V model, which achieved the best fit statistics (lowest AIC and
highest log-likelihood), underscores the central thesis of this research: that how fast fear sentiment changes is more relevant to crude
oil return dynamics than its static level. This builds upon the work of Xiao et al. (2019)and Wang, He, Ma, and Li (2022), who explored
the roles of OVX and EPU in financial contagion and risk pricing, yet did not consider the temporal momentum of sentiment or the
underlying regime structures.
Extensive robustness analyses strongly reinforce the stability and credibility of our main results. The out-of-sample forecasting
exercises, based on an 80–20 split, reveal that derivative-based sentiment measures consistently outperform static levels of VIX and
MOVE in predicting crude-oil returns. This indicates that the momentum embedded in fear, its velocity and acceleration, contains
forward-looking informational content that is absent in stationary sentiment indicators. When macro-financial and geopolitical
controls such as the US Dollar Index (DXY) and the Geopolitical Risk Index (GPR) are introduced into the MSR framework, the
magnitude, sign, and significance of the sentiment-derivative coefficients remain unchanged. This confirms that sentiment momentum
is not merely capturing broad market conditions or geopolitical tensions but represents an independent behavioral channel that
systematically influences crude-oil dynamics.
Further robustness checks using a Fourier-augmented MSR specification demonstrate that seasonal and cyclical patterns exert only
negligible influence on regime transitions. Annual and semiannual harmonics appear largely insignificant across all models. In
addition, the key structural features such as the regime-specific variances, transition probabilities, and the identification of tranquil
versus turbulent regimes, remain essentially identical to the baseline specification. Overall, these results validate that regime shifts in
crude-oil markets are driven primarily by nonlinear fluctuations in financial fear rather than by deterministic seasonal cycles or macro-
financial pressures. Consequently, monitoring the momentum of fear emerges as a more reliable approach for identifying upcoming
instability. Overall, our findings complement recent evidence that crude oil markets exhibit complex and multi-factor volatility dy-
namics (Solibakke, 2024), reinforcing the view that regime shifts and information-driven volatility clusters are intrinsic features of oil
price behaviour.
These results lead to significant and diverse policy implications. First, regarding risk management, the study shows that closely
monitoring the acceleration and velocity of financial fear, particularly from equity markets, provides crucial early warning signals for
declines in crude oil prices. These signals furnish practical data for portfolio rebalancing before the manifestation of market stress in
prices.
Second, concerning forecasting systems, incorporating derivative-based sentiment measures into models like MSR offers a sub-
stantial improvement over more traditional type models. MSR provides greater robustness in contexts characterised by frequent shifts
between calm and turbulence compared to static volatility models because it captures the nonlinear, regime-dependent nature of
market reactions.
Third, from the perspective of energy policy and market regulation, the results reveal that sudden policy changes render sentiment
velocity unstable. This indicates that, to prevent exacerbating financial anxiety and initiating self-reinforcing volatility cycles in
commodity markets, monetary authorities, central banks, and energy regulators should aim for gradual and well-communicated
interventions.
Fourth, the paper highlights a notable asymmetry among asset classes. Particularly in tranquil regimes, VIX-based sentiment dy-
namics consistently outperform their MOVE-based counterparts. This suggests that relative to fixed-income volatility, oil markets are
more responsive to equity market stress; this observation should inform capital allocation decisions and cross-asset risk management.
Fifth, these insights pave the way for the development of real-time sentiment analytics. Drawing inspiration from recent ad-
vancements in AI-enhanced forecasting tools (e.g., BERT (Bidirectional Encoder Representations from Transformers)-based models),
financial technology platforms could monitor sentiment velocity and acceleration as part of an advanced early-warning system for
trading desks, commodity brokers, and sovereign wealth funds.
Sixth, during crises, conventional sentiment indicators prove inadequate, necessitating that investors resort to models incorpo-
rating structural breaks, endogenous feedback loops, and liquidity shocks. Under such circumstances, sentiment momentum yields to
macroeconomic fundamentals, policy changes, or geopolitical events. Hence, hybrid models that merge macro-sentiment indices with
regime-switching dynamics may offer improved stability and foresight.
Siven, Robustness analysis has important implications: policymakers may use sentiment acceleration as an early-warning indicator
to adjust communication or stabilization policies, while risk managers can integrate sentiment velocity into real-time monitoring,
hedging strategies, and exposure management in increasingly interconnected commodity–financial environments.
Finally, regarding regulatory coordination, the study recommends enhancing the synchronisation of energy policy communications
with monetary policy. A better understanding of the nonlinear channels through which fear accelerates and translates into fluctuations
in commodity prices will assist central banks and energy ministries in averting unintended policy spillovers, stabilising expectations,
28

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
and helping to preempt panic.
In conclusion, this research advances the theoretical and empirical understanding of fear sentiment in oil markets by demonstrating
that its temporal dynamics, specifically velocity and acceleration, are crucial drivers of return behaviour, especially under stable
conditions. By integrating these derivative measures into a regime-sensitive model, we provide a novel and powerful framework for
forecasting, risk mitigation, and strategic decision-making. Future research could build on this foundation by examining how other
behavioural or geopolitical sentiment indicators, when expressed dynamically, interact with commodity prices across various time
horizons and market regimes.
Author statement
Kais Tissaoui: Data curation; Methodology; Software; Formal analysis; Investigation; Writing - original draft; Project
administration.
Nadia Azibi: Writing - original draft; Conceptualization; Investigation; Writing - review & editing; Supervision; Visualization.
Data availability
Data will be made available on request.
References
Abdelaziz, T. H. (2013). Eigenstructure assignment for second-order systems using velocity-plus-acceleration feedback. Structural Control and Health Monitoring, 20(4),
465–482.
Abdollahi, H. (2023). Oil price volatility and new evidence from news and Twitter. Energy Economics, 122, Article 106711.
Adrian, T., & Shin, H. S. (2010). Liquidity and leverage. Journal of Financial Intermediation, 19(3), 418–437.
Aladwani, J. (2024). Oil volatility uncertainty: Impact on fundamental macroeconomics and the stock index. Economies, 12(6), 140.
Aloui, R., Gupta, R., & Miller, S. M. (2016). Uncertainty and crude oil returns. Energy Economics, 55, 92–100.
Alquist, R., Kilian, L., & Vigfusson, R. J. (2013). Forecasting the price of oil. In Handbook of economic forecasting (Vol. 2, pp. 427–507). Elsevier.
Barberis, N., Shleifer, A., & Vishny, R. (1998). A model of investor sentiment. Journal of Financial Economics, 49(3), 307–343.
Basak, S., & Pavlova, A. (2016). A model of financialization of commodities. The Journal of Finance, 71(4), 1511–1556.
Baumeister, C., & Kilian, L. (2016). Understanding the Decline in the Price of Oil since June 2014. Journal of the Association of Environmental and Resource Economists, 3
(1), 131–158.
Bekaert, G., Hoerova, M., & Duca, M. L. (2013). Risk, uncertainty and monetary policy. Journal of Monetary Economics, 60(7), 771–788.
Ben Ameur, H., Boubaker, S., Ftiti, Z., Louhichi, W., & Tissaoui, K. (2024). Forecasting commodity prices: Empirical evidence using deep learning tools. Annals of
Operations Research, 339(1), 349–367.
Bikhchandani, S., & Sharma, S. (2000). Herd behavior in financial markets. IMF Staff Papers, 47(3), 279–310.
Bouri, E., Jalkh, N., Moln´ar, P., & Roubaud, D. (2017). Bitcoin for energy commodities before and after the December 2013 crash: Diversifier, hedge or safe haven?
Applied Economics, 49(50), 5063–5073.
Bufalo, M., & Fanelli, V. (2024). Modelling the Chinese crude oil futures returns through a skew-geometric Brownian motion correlated with the market volatility
index process for pricing financial options. Applied Stochastic Models in Business and Industry, 40(5), 1377–1401.
Cerqueti, R., Fanelli, V., & Rotundo, G. (2019). Long run analysis of crude oil portfolios. Energy Economics, 79, 183–205.
Cevik, E. I., Dibooglu, S., Gillman, M., & Benk, S. (2025). Granger predictability of real oil prices by U.S. money and inflation in Markov-switching regimes. Eurasian
Economic Review, 1–24.
Charles, A., & Darn´e, A. (2017). Forecasting crude-oil market volatility: Further evidence with jumps. Energy Economics, 67, 508–519.
Cheung, Y. W., & Ng, L. K. (1996). A causality-in-variance test and its application to financial market prices. Journal of Econometrics, 72(1–2), 33–48.
Daniel, K., Hirshleifer, D., & Subrahmanyam, A. (1998). Investor psychology and security market under-and overreactions. The Journal of Finance, 53(6), 1839–1885.
Das, D., Dutta, A., Jana, R. K., & Ghosh, I. (2023). The asymmetric impact of oil price uncertainty on emerging market financial stress: A quantile regression approach.
International Journal of Finance & Economics, 28(4), 4299–4323.
Dong, J., Ferreira, P. M., & Stori, J. A. (2007). Feed-rate optimization with jerk constraints for generating minimum-time trajectories. International Journal of Machine
Tools and Manufacture, 47(12–13), 1941–1955.
Dutta, A., & Bouri, E. (2024). Forecasting the volatility of crude oil futures: New evidence from jump-induced volatility. Energy Strategy Reviews, 56, Article 101588.
Eager, D., Pendrill, A. M., & Reistad, N. (2016). Beyond velocity and acceleration: Jerk, snap and higher derivatives. European Journal of Physics, 37(6), Article
065008.
Fleming, J. (1998). The quality of market volatility forecasts implied by S&P 100 index option prices. Journal of Empirical Finance, 5(4), 317–345.
Ftiti, Z., Tissaoui, K., & Boubaker, S. (2022). On the relationship between oil and gas markets: A new forecasting framework based on a machine learning approach.
Annals of Operations Research, 313(2), 915–943.
Hamilton, J. D. (1989). A new approach to the economic analysis of nonstationary time series and the business cycle. Econometrica, 357–384.
Hao, W., & Pham, L. (2024). Dynamic connectedness in the higher moments between clean energy and oil prices. Energy Economics, 140, Article 107987.
He, M., Zhang, Y., Wang, Y., & Wen, D. (2024). Modelling and forecasting crude oil price volatility with climate policy uncertainty. Humanities and Social Sciences
Communications, 11(1), 1–10.
Inchauspe, J., Li, J., & Park, J. (2020). Seasonal patterns of global oil consumption: Implications for long-term energy policy. Journal of Policy Modeling, 42(3),
536–556.
Kahneman, D., & Tversky, A. (2013). Prospect theory: An analysis of decision under risk. In Handbook of the fundamentals of financial decision making: Part I (pp.
99–127).
Kilian, L., & Zhou, X. (2022). The impact of rising oil prices on U.S. inflation and inflation expectations in 2020–23. Energy Economics, 113, Article 106228.
Kritzman, M., Li, Y., Page, S., & Rigobon, R. (2010). Principal components as a measure of systemic risk.
Li, Z., Xu, Y., & Du, Z. (2025). Valuing financial data: The case of analyst forecasts. Finance Research Letters, 75, Article 106847.
Ma, R., Zhou, C., Cai, H., & Deng, C. (2019). The forecasting power of EPU for crude oil return volatility. Energy Reports, 5, 866–873.
Nguyen, H. H., Tran Nguyen, N. A., & Le Thi, P. T. (2025). Public sentiment, stock and energy prices during the Russia-Ukraine war: Global evidence. Journal of
Chinese Economic and Business Studies, 23(2), 259–294.
Pindyck, R. S. (2004). Volatility and commodity price dynamics. Journal of Futures Markets: Futures, Options, and Other Derivative Products, 24(11), 1029–1047.
Sharma, N. (1998). Forecasting oil price volatility. Virginia Tech: Doctoral dissertation.
Sifat, I., Zarei, A., & Mand, A. A. (2023). Revisiting WTI–Brent spread and its drivers. Energy Strategy Reviews, 50, Article 101206.
Solibakke, P. B. (2024). Forecasting hourly WTI oil front monthly price volatility densities. Quantitative Finance and Economics, 8(3), 466–501.
29

K. Tissaoui and N. Azibi I n t e r n a t i o n a l R e v i e w o f E c o n o m i c s a n d F in a n c e 1 0 8 (2026) 105197
Soros, G. (2015). The alchemy of finance. John Wiley & Sons.
Tang, L., & Hammoudeh, S. (2002). An empirical exploration of the world oil price under the target zone model. Energy Economics, 24(6), 577–596.
Tang, K., & Xiong, W. (2012). Index investment and the financialization of commodities. Financial Analysts Journal, 68(6), 54–74.
Tissaoui, K. (2012). The intraday pattern of trading activity, return volatility and liquidity: Evidence from the emerging Tunisian stock exchange. International Journal
of Economics and Finance, 4(5), 156–176.
Tissaoui, K., Abidi, I., Azibi, N., & Nsaibi, M. (2024). Spillover effects between crude oil returns and uncertainty: New evidence from time–frequency domain
approaches. Energies, 17(2), 340.
Tissaoui, K., & Aloui, C. (2011). Information flow between stock return and trading volume: The Tunisian stock market. International Journal of Financial Services
Management, 5(1), 52–82.
Tissaoui, K., Zaghdoudi, T., Hakimi, A., & Nsaibi, M. (2023). Do gas price and uncertainty indices forecast crude oil prices? Fresh evidence through XGBoost modeling.
Computational Economics, 62(2), 663–687.
Tlili, H., Tissaoui, K., Kahouli, B., & Triki, R. (2024). How volatility in the oil market and uncertainty shocks affect the Saudi economy: A frequency approach.
Humanities and Social Sciences Communications, 11(1), 1–24.
Wang, J., He, X., Ma, F., & Li, P. (2022). Uncertainty and oil volatility: Evidence from shrinkage method. Resources Policy, 75, Article 102482.
Xiao, J., Hu, C., Ouyang, G., & Wen, F. (2019). Impacts of oil implied volatility shocks on stock implied volatility in China: Empirical evidence from a quantile
regression approach. Energy Economics, 80, 297–309.
Zaghdoudi, T., Tissaoui, K., Maaloul, M. H., Bahou, Y., & Kammoun, N. (2023). Asymmetric connectedness between oil price, coal, and renewable energy consumption
in China: Evidence from a Fourier NARDL approach. Energy, 285, Article 129416.
Zhang, L., Peng, K., Zhao, X., & Khattak, A. J. (2022). New fuel consumption model considering vehicular speed, acceleration, and jerk. Journal of Intelligent
Transportation Systems, 26(5), 523–536.
Zhang, Y. J., & Yan, X. X. (2020). The impact of U.S. economic policy uncertainty on WTI crude oil returns in different time and frequency domains. International
Review of Economics & Finance, 69, 750–768.
Zhao, Z., & Lin, W. (2024). Short-term electric load forecasting based on empirical wavelet transform and temporal convolutional network. IET Generation,
Transmission & Distribution, 18(8), 1672–1683.
30