---
title: "第12回 2024年度開講 駒澤大学 認知心理学研究"
author: "浅川 伸一"
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="right">
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 13/Dec/2024<br/>
Appache 2.0 license<br/>
</div>

$$
\newcommand{\of}[1]{\left(#1\right)}
\newcommand{\Of}[1]{\left[#1\right]}
\newcommand{\KL}[2]{\operatorname{KL}\left(\left.{#1}\right\|{#2}\right)}
\newcommand{\given}[1]{\left|{#1}\right.}
\newcommand{\mb}[1]{\mathbf{#1}}
$$


## Colab 実習ファイル

* [2024_1213royabel_BU_TD_multi_mnist.ipynb <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_1213royabel_BU_TD_multi_mnist.ipynb)
* [2024_1220Karapetian_demo.ipynb <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_1220Karapetian_demo.ipynb)

# 先週の話題の補足

* 時系列予測モデルには，自己回帰モデル (AR)，移動平均モデル (MA), 自己回帰移動平均モデル (ARMA)，自己回帰和分移動平均モデル (ARIMA) などを紹介した。
* 上記モデルは，観測データに誤差が含まれないモデルである。
* 一方，脳波や心理実験データなどを含む，一般に「観測」には誤差が含まれていると考える場面が多い。
* 誤差を含む観測データから真の値を推測することを考える。
* 心理学との関連で言えば，古くは，川人ら (Kawato+1993) の「順逆光学モデル」などが挙げられる。
* 川人らの「順逆光学モデル」では，標準正則化理論の枠組みを用いた評価関数 (目的関数) に対して，反復推定を繰り返すことを提案している。
* Wolpert+(1995) はカルマンフィルタモデルを用いて，内部状態を推定するモデルを提案した。

### 復習，標準正則化理論

色，動き，形などの異なる視覚的手がかりを表現する複数の視覚野 (van_Essen+1990) と，網膜から視覚連合野 (Hubel&Livingstone1987) に至るまで並列に組織化されていることに関する最近の発見は，どのように並列視覚モジュール (Julesz1971) を統合すれば，短時間で首尾一貫した情景知覚が可能になるのかという計算問題を提起した。
<!-- Recent findings on multiple visual cortical areas (van_Essen+1990) which represent distinct visual cues such as colour, motion and shape, and their parallel organization all the way through from the retina to the visual association cortices (Hubel&Livingstone1987) pose a difficult computational problem: how are parallel visual modules (Julesz1971) integrated to allow a coherent scene perception within a short time? -->

### 順逆光学モデル (Kawato+1993)

視覚画像 $I$ は，視覚世界に存在する物体から反射された光線が，網膜，CCD，フィルムなどの画像センサーに当たって生成される。
「光学」すなわち，画像処理 $R$ は物体を画像に圧縮するため，情報が失われたと仮定。
その結果，2 次元画像から 3 次元世界の幾何学的構造の様々な側面 $S$ を推定する初期視覚問題は，1 対 1 の写像であるため，あらかじめ何らかの制約が与えられない限り正しく解くことができない (Marr1982, Poggio+1985)。
すなわち，初期の視覚問題は，それぞれ光学の逆過程として計算的に特徴付けられ，視覚世界に関する先験的知識が必要な制約として導入される。
従って，多くの計算視覚アルゴリズムでは，以下の 2 つの目的関数の和 $J$ を最小化して，画像データ $I$ を説明し，かつア・プリオリな識を満たす最良の視覚世界表現 $S$ を求める (Ballard+1983, Poggio+1985)：
<!-- Visual images I are generated when light rays reflected from 30 objects in the visual world hit a 20 image sensor such as the retina, CCD or film.
The imaging process R, which we call 'optics', compresses 30 objects into 20 images and thus loses information; hence a many-to-one mapping.
Consequently, the early vision problems which estimate different aspects S of the geometrical structure in the 3D world from 2D images cannot be properly solved unless some constraints are given beforehand (Marr1982, Poggio+1985) because they are one-to-niany mappings.
That is, the early vision problems are each computationally characterized as an inverse process of optics and a priori knowledge about the visual world is introduced as the constraint required.
Accordingly, in many computational vision algorithms, the following sum J of two objective functions is minimized to find the best visual-world representation S which explains the image data I as well as satisfies the a
priori knowledge (Ballard+1983, Poggio+1985): -->
<br/>

$$\tag{1}
J = \left\|R(S)-I\right\|^{2} + \left\|Q(S)\right\|^{2},
$$
<br/>

ここで，第 1 項は光学演算子 $R$ を用いた表現 $S$ からの画像 $R(S)$ の再構成が実データ $I$ と適合することを要求し，第 2  項は表現の滑らかさなど視覚世界に関する先験的知識を課す。
$R$ や $Q$ が強い非線形性を持つ場合，最小化は特に困難である。
<!-- が，確率的緩和アルゴリズム (Geman&Geman1984, Poggio+1985) や，そのリカレントニューラルネットワーク (平均場近似) 版 (Koch+1986) など，一種の急降下法によって行うことができる。
しかし，多くの反復回数 (通常数百回以上) が必要であり，人間の典型的な視覚情報処理時間 (100～400 ミリ秒) に対する説明は存在しない (Potter1976，Inui&Miyamoto1981)。
そのため，これまでリカレント神経回路網モデルは，高速な視覚計算機構として否定されてきた (Marr&Poggio1979, Thorpe&Imbert1989, Rolls1989)。 -->
<!-- where the first term requires that the reconstruction of the image R(S) from the representation S using the optics operator R be compatible with the real data I, and the second term imposes the a priori knowledge about the visual world, such as smoothness of the representation.
Minimization is especially difficult when R or Q is strongly nonlinear; it can, however, be done by a kind of steepest descent method: the stochastic relaxation algorithm (Geman&Geman1984, Poggio+1985) or its recurrent neural network (mean-field approximation) version (Koch+1986).
However, a large number of iterations (usually more than a few hundred) is required, and no explanation exists  for the typical visual information processing time in humans (100-400 ms) (Potter1976, Inui&Miyamoto1981).
Thus, hitherto, recurrent neural network models have been rejected as fast visual computational mechanisms (Marr&Poggio1979, Thorpe&Imbert1989, Rolls1989). -->

<div class="figcenter">
<img src="/2024assets/1993Kawato_Fig1.svg" style="width:44%">
<!-- <img src="/2024assets/1993Kawato_fig2.svg" style="width:44%">
<!-- <img src="/2024assets/1993Kawato_fig3_.svg" style="width:44%"><br/> -->
<!--<img src="/2024assets/1993Kawato_fig3all.jpg" style="width:66%"><br/> -->
<div class="figcaption">

**左. 順逆光学モデル**<br/>
(A) V1 と高次視覚野 (HVC) の相互作用モデル。
図の下半分では，外界の光学操作 R が下位部分 R1 と上位部分 R2 に分解されている。
この脳内階層構造のモデルを図の上半分に示す。<br/>
(B) V1 と HVC の階層的相互作用の層状神経回路モデル。
塗りつぶされたニューロンは興奮性，空洞のニューロンは抑制性。
<!-- Figure 1. Fundamental forward-inverse optics model.
(A) Model for reciprocal interactions between VI and the higher visual cortex (HVC).
In the lower half of the figure, the optics operation R in the outer world is decomposed into a lower and a higher part, R1 and R2.
A model of this hierarchy in the brain is shown in the upper half of the figure.
(8) Layered-neural circuit model of the hierarchical interaction between VI and HVC.
Filled neurons are excitatory and a hollow neuron is inhibitory. -->

</div></div>

Kawato+(1993) は， 逆投射接続が光学処理過程のフォワードモデルを提供し，2 つの領域間のフィードフォワード接続がその光学処理過程の近似された逆モデルを提供することを提案した。
上図 の順逆光学モデルは，下図 のようなより現実的なモデルに拡張される。
独自の逆光学演算は存在しないが，式 (1) の 2 つの項をある程度考慮することで，画像データ I から S の大まかな推定値を一撃計算で算出する近似的な逆光学演算を，フィードフォワード神経接続の形で導出することは常に可能である。


<div class="figcenter">
<img src="/2024assets/1993Kawato_fig2.svg" style="width:44%">
<!-- <img src="/2024assets/1993Kawato_fig3_.svg" style="width:44%"><br/> -->
<!--<img src="/2024assets/1993Kawato_fig3all.jpg" style="width:66%"><br/> -->
<div class="figcaption">

**図 2. 視覚野の並列・階層構造に適応した順逆光学モデル**<br/>
各領域が純粋に物理的に識別可能な量を表すということを文字通り提案しているわけではない。
矢印のない接続は相互神経接続を示す。不連続性 (Poggio+1988) を利用することで，色，立体，形，運動を集中的に統合することができる。
記号の定義は以下の通り。
<!-- Figure 2. The forward-inverse optics model adapted to a parallel and hierarchical structure of visual cortices.
We do not literally propose that each area represents purely a physically identifiable quantity.
Connections without arrows show reciprocal neural connections. Intensive integration of colour, stereo, shape and motion could take place by using discontinuity (Poggio+1988) possibly represented in interstripes of V2.
Definitions of symbols are as follows. -->
$\Delta G\star I$画像のラプラシアン・ガウス関数との畳み込み積分<br/>
$dI$ と $d^{2}$: 特定の方向に沿った画像の1次微分と 2 次微分<br/>
$v^{\bot}$: 画像強度の変化が最大となる方向の局所速度成分<br/>
$sd$：ステレオ視差から計算した表面深度<br/>
$r(\lambda)$：波長 $\lambda$ の光の可視面上の点の反射率<br/>
$L$: 輪郭や異なる物体の接合部などの不連続面<br/>
$md$：様々な単眼的手がかりから計算される可視面の奥行きと方位<br/>
$\nu$: 光源の位置と波長分布<br/>
$C$: $L$ で分離された物体の 3D 位置<br/>
$A$：色や質感など、物体の様々な属性<br/>
$V$：物体の並進と回転を表す速度ベクトル<br/>
$N$：観察者の体、頭、目の速度ベクトル<br/>
$O$：記憶された3次元物体の画像<br/>
<!-- $\Delta G\star I$ : convolution integral of the image with the Laplacian Gaussian function.<br/>
$dI$ and $d^{2}$: first and second derivatives of the image along with specific directions.<br/>
$v^{\bot}$: local velocity component in the direction with the maximum change of image intensity.<br/>
$sd$: surface depth calculated from stereo disparity.<br/>
$r(\lambda)$: reflectance of points on the visible surface of a light of wavelength $\lambda$.<br/>
$L$: discontinuities such as occluding contours and junctions of different objects.<br/>
$md$: depth and orientation of the visible surface calculated by various monocular cues.<br/>
$\nu$: location of the light source and its wavelength distribution.<br/>
$C$: JD locations of objects segregated by $L$.<br/>
$A$: various attributes of a distinct object such as colour and texture.<br/>
$V$: velocity vector representing translation and rotation of objects.<br/>
$N$: velocity vectors of the body, head and eyes of the observer.<br/>
$O$: memorized images of 3D objects. -->
</div></div>

### カルマンフィルタモデル (感覚運動統合の内部モデル, Wolpert+1995)

測定信号 $x(t)$ から推定しなければならない未知信号を $s(t+a)$ とする。
a は調整可能なパラメータである。
* a>0 は予測，
* a=0 はフィルタ，
* a<0 はスムージングと呼ばれる

<div class="figcenter">
<img src="/2024assets/1995WolpertGhahramaniJordan_fig2m.svg">
<img src="/2024assets/1995WolpertGhahramaniJordan_fig2a.svg">
<div class="figcaption">

**カルマンフィルタモデルの概要**<br/>
A: カルマンフィルタのモデルを模式的に示しており，2 つの処理過程で構成される。
1 つ目の処理 (上) は 運動指令と現在の状態推定値を用いて，順モデルによる状態推定値を実現し，腕のダイナミクスをシミュレートする。<br/>
2 つ目の処理 (下) は 期待される感覚フィードバックと実際の感覚フィードバックの差を利用して，順モデルの状態推定値を修正する。この 2 つの処理の相対的な重み付けは，カルマンゲインを介して行われる。<br/>
(B～E) センサー運動統合過程のカルマンフィルタモデルによる偏りと分散の伝播を，実データに即してシミュレートしたもの
</div></div>

カルマンフィルタは，ベイズ推論による推定値の逐次更新とみなしうる。

##### カルマンフィルタ

<div class="figcenter">
<img src="/2024assets/2024_1213Kalman_residual_chart_ja.svg"><br/>
</div>
<div class="figcenter">
フィルタリングの考え方の模式図
</div>

<div class="figcenter">
<img src="/2024assets/2024_1213Kalman_chart_ja.svg" style="width:44%;">
<img src="/assets/2015Greff_LSTM_ja.svg" style="width:39%;">
<div class="figcaption">
左: 状態空間モデル (カルマンフィルタ)の模式図.<br/>
右: LSTM の模式図
</div></div>

##### LSTM におけるゲートの生理学的対応物 <!--Physiological correlates of gates in LSTM-->

以下の画像は <http://kybele.psych.cornell.edu/~edelman/Psych-2140/week-2-2.html> よりの引用。
ウミウシのエラ引っ込め反応時に，ニューロンへの入力信号ではなく，入力信号を修飾する結合が存在する。下図参照。

<center>
<img src="/assets/2016McComas_presynaptic_inhibition.jpg" style="width:24%">
<img src="/assets/C87-fig2_24.jpg" width="17%">
<img src="/assets/C87-fig2_25.jpg" width="33%"><br>
アメフラシ (Aplysia) のエラ引っ込め反応(a.k.a. 防御反応)の模式図[^seaslang]
<!-- <img src="/assets/shunting-inhibition.jpg" width="29%"> -->
</center>

* [注意機構の補足説明 大門他 (2023) <img src="https://www.adobe.com/content/dam/cc/en/legal/images/badges/PDF_32.png">](/2023/2023cnps注意機構の補足説明.pdf){:target="_blank"}

<!--
<img src="/2024assets/2024_1213Kalman_chart_ja.svg">
<img src="/2024assets/2024_1213Kalman_residual_chart_ja.svg"> -->

### 自由エネルギーモデル (Friston+2014 他)

<div class="figcenter">
<img src="/assets/2014Friston_Fig1.svg" style="width:44%">
<img src="/assets/2009Friston_box3.svg" style="width:44%">
</div>

<!-- <img src="/2023assets/2018Higgins_SCAN_fig1.svg" style="width:66%;">
<img src="/2023assets/2017Higgins_SCAN_fig1ja_.svg" style="widht:66%;">

<img src="/2024assets/1993Kawato_Fig1.svg" style="width:44%">
<img src="/2024assets/1993Kawato_fig2.svg" style="width:44%">
<img src="/2024assets/1993Kawato_fig3_.svg" style="width:44%"><br/>
<img src="/2024assets/1993Kawato_fig3all.jpg" style="width:66%"><br/> -->


##### Bayes の定理

$$
P(X,Y) = P(X|Y)P(Y) = P(Y|X) P(X)
$$

$$\begin{aligned}
P(Y|X) &= \frac{P(X|Y)P(Y)}{P(X)} &= \frac{\text{尤度 $\times$ 事前確率}} {\text{証拠}}\\
&= \frac{P(X|Y)P(Y)}{P(X|Y)P(\neg Y)+ P(X|Y)P(Y)}
\end{aligned}$$

* [Puppy book, ベイズ統計モデリング: R,JAGS, Stan によるチュートリアル](https://www.amazon.co.jp/dp/4320113160/){:target="_blank"} を超えて

* [原著 Doing Bayesian Data Analysis: A Tutorial Introduction with R, JAGS, and STAN](https://www.amazon.com/dp/0124058884/){:target="_blank"}
* [原著 A Tutorial Introduction with R](https://www.amazon.com/dp/B004QOB460/){:target="_blank"}


#### KL ダイバージェンス

KL ダイバージェンスは，2 つの分布間の距離に相当する量を与える。
だが KL ダイバージェンスは通常の距離と異なり非対称で，どちらの分布を基準に考えるかによって値が異なる。
すなわち $\KL{P}{Q}\ne\KL{Q}{P}$ です。
下図 (fig:forward_reverse_KL) にその関係を示した。
青い曲線は真の事後分布とします，例えば双峰性の分布であるとする。
緑の分布は最適化を介して青い密度に適合させる変分近似による分布を表すものとする。
これを **フォワード KL** と呼ぶ。
図 (fig:forward_reverse_KL) 右のように，双峰性の真の分布を単峰性の分布で近似することを考える。
このとき，一方の峰に当てはまるように調整すると，もう一方の峰の値についての当てはまりが悪くなり結果として右下図のような裾野の広い分布を得ることになる。
反対に，緑の単峰性の分布を青の双峰性の分布で近似しようとする **リバース KL** を考える。
このとき基準となる真の分布である単峰性の分布の確率密度がほとんど 0 の領域では，推定する分布がどのような値を取ろうとも KL ダイバージェンスの値に影響を与えないため，いずれか一方の峰が真の分布と重なるような値を得ることになる。

<div class="figcenter">
<img src="/assets/forward-KL.png" width="33%">
<img src="/assets/reverse-KL.png" width="33%">
<div class="figcaption">

左: フォワード KL, 右: リバース KL

KL ダイバージェンスの非対称性
[A Beginner's Guide to Variational Methods: Mean-Field Approximation](https://blog.evjang.com/2016/08/variational-bayes.html) より
</div></div>

分布が 近い とはどういう意味かというと
平均場変分ベイズ（最も一般的なタイプ）は，2 つの分布間の距離として 逆 KL ダイバージェンスを使用する。
<!-- % Reverse KL divergence measures the amount of information (in nats, or units of $\frac{1}{\log(2)}$ bits) required to "distort" $P(Z)$ into $Q_\phi(Z)$.
% We wish to minimize this quantity with respect to $\phi$.-->
条件付き分布の定義により，$p\of{z\given{x}}=p\of{x,z}p\of{x}$
この式を，オリジナルの KL ダイバージェンスの定義式に代入すれば，
<!-- % By definition of a conditional distribution, $p\of{z\given{x}}=p\of{x,z}p\of{x}$.
% Let's substitute this expression into our original KL expression, and then distribute: -->

このようなフォワード，リバース KL ダイバージェンスの値から VAE の表現性能などを考えることが可能です。

<!--
## Colab 実習ファイル

* [2024_1205Karapetian_RNN.ipynb <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_1205Karapetian_RNN.ipynb){:target="blank"} -->


## 参考資料

* [7–1 リカレントニューラルネットワーク](/2022/6657.pdf){:target="_blank"}
* [7–1 リカレントネットワークによる文法学習](/2022/6685.pdf){:target="_blank"}

* [Bahdanau and Loung attentions <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_1022Two_attentions_additive_and_multiplicative_Seq2seq.ipynb)

* [系列探索と逆行流: 視覚野における双方向情報フローの計算モデル](/2023cogpsy/2021Ullman_bu_td_ja.pdf){:target="_blank"}
* [ボトムアップ・トップダウンの反復処理による画像解釈](/2023cogpsy/1995Ullman_bidirectional_cortex_ja.pdf){:target="_blank"}


### A. 最大事後確率法：貧乏人の Bayes 推論
<!-- ### MAXIMUM A POSTERIORI: POOR MAN’S BAYESIAN INFERENCE-->

統計的信号処理の文献で最もよく使われる手法の 1 つが最大事後確率法 (MAP: Maximum A Posteriori 法) である。
MAP は，パラメータベクトル $\theta$ を確率変数と仮定し，$\theta$ に事前分布 $p(\theta)$ を課すことから，しばしばベイズ的と呼ばれる。
ここでは，MAP 推定とベイズ推定との類似点と相違点を明らかにする。
$x$ を観測値，$\theta$ を未知量とすると，MAP 推定は次のように定義される。
<!-- One of the most commonly used methodologies in the statistical signal processing literature is the maximum a posteriori (MAP) method.
MAP is often referred to as Bayesian, since the parameter vector θ is assumed to be a random variable and a prior distribution pθ is imposed on θ.
In this appendix, we would like to illuminate the similarities and differences between MAP estimation and Bayesian inference.
For x the observation and θ an unknown quantity the MAP estimate is defined as -->

$$ \hat{\theta}_ {\text{MAP}} = \arg\max_ {\theta} p(\theta\vert x)\tag{A.1} $$

Bayes 則を用いて， MAP 推定は次式より得られる:
<!-- Using Bayes’ theorem, the MAP estimate can be obtained from  -->

$$
\hat{\theta}_{\text{MAP}} = \arg\max_{\theta} p(x|\theta)\,d\theta
\tag{A.2}$$

ここで $p(x|\theta)$ は観測値の尤度である。
MAP 推定値は (A.1) よりも (A.2) から求めた方が簡単である。
ベイズの定理に基づく (A.1) の事後確率は次式で与えられる:
<!-- where p(x|θ) is the likelihood of the observations.
The MAP estimate is easier to obtain from (A.2) than (A.1).
The posterior in (A.1) based on Bayes’ theorem is given by -->

$$ p(\theta\vert x) = \frac{p(x\vert\theta)p(\theta)}{\int p(x\vert\theta)p(\theta) d\theta}\tag{A.3} $$

であり 式 (A.3) の分母にベイズ積分を計算し，$\theta$ を周辺化する必要がある。
<!-- and requires the computation of the Bayesian integral in the denominator of (A.3) to marginalize θ.-->

以上より，MAP 推定量も Bayes 推定量も $\theta$ を確率変数と仮定し，Bayes の定理を用いることは明らかであるが，その類似性はそこに止まっている。
ベイズ推定では事後分布を用いるため，$\theta$ を周辺化する必要がある。
これに対して，MAP では事後値の最頻値を用いる。
ベイズ推定は，MAP と異なり，$\theta$ に関する利用可能なすべての情報を平均化すると言える。
したがって MAP は「貧乏人の Bayes 推論」と言える。
<!-- From the above, it is clear that both MAP and Bayesian estimators assume that θ is a random variable and use Bayes’ theorem, however, their similarity stops there.
For Bayesian inference, the posterior is used and thus θ has to be marginalized.
In contrast, for MAP the mode of the posterior is used.
One can say that Bayesian inference, unlike MAP, averages over all the available information about θ.
Thus, it can be stated that MAP is more like “poor man’s” Bayesian inference. -->

EM は $\theta$ の MAP 推定値も得るために用いることができる。
Bayes の定理を用いて，次のように書くことができる:
<!-- The EM can be used to also obtain MAP estimates of θ.
Using  Bayes’ theorem we can write -->

$$ \begin{aligned}
\ln p(\theta\vert x) & = \ln p(x,\theta) − \ln p(x)\\
&= \ln p(x\vert\theta) + \ln p(\theta) − \ln p(x).
\end{aligned}\tag{A.4} $$

上式は，下記のように書くことができる:
<!-- 「EM アルゴリズムの別見解」節 の ML-EM の場合と同様の枠組みで，次のように書くことができる: -->
<!-- Using a similar framework as for the ML-EM case in the section “An Alternative View of the EM Algorithm,” we can write-->

$$\begin{aligned}
\ln p(\theta\vert x) &= F(q,\theta) + D_ {\text{KL}}(q\vert\vert p) + \ln p(\theta) − \ln p(x)\\
&\ge F(q,\theta) + \ln p(\theta) − \ln p(x),
\end{aligned}\tag{A.5}$$

ここで，$\ln p(x)$ は定数である。
(A.5) 式右辺は，EM アルゴリズムと同様に交互に最大化することができる。
$q(z)$  に関して最適化すると，先に説明した ML の場合と同じ E-step が得られる。
$\theta$ に関して最適化すると，目的関数が $\ln p(\theta)$  の項を含むので，異なるM-step が得られる．
<!-- 一般に MAP-EM アルゴリズムの M-ステップは，ML の場合よりも複雑であり，例えば  [30]  や [31] を参照されたい。
厳密に言えば，このようなモデルでは，MAP  推定は $\theta$ 確率変数のみに使用され，ベイズ推定は隠れ変数 $z$ に使用される。 -->
<!-- where in this context ln p(x) is a constant.
The right-hand side of (A.5) can be maximized in an alternating fashion as in the EM algorithm.
Optimization with respect to q(z) gives an identical E-step as for the ML case previously explained.
Optimization with respect to θ gives a different M-step since the objective function now contains also the term ln p(θ).
In general, the M-step for the MAP-EM algorithm is more complex than in its ML counterpart, see for example [30] and [31].
Strictly speaking, in such a model MAP estimation is used only for the θ random variables, while Bayesian inference is used for hidden variables z.-->
