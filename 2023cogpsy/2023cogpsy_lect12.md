---
title: "第12回 2023年度開講 駒澤大学 認知心理学研究"
author: "浅川 伸一"
layout: home
---

<div align="right">
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 15/Dec/2023<br/>
Appache 2.0 license<br/>
</div>

$$
\newcommand{\of}[1]{\left(#1\right)}
\newcommand{\Of}[1]{\left[#1\right]}
\newcommand{\KL}[2]{\operatorname{KL}\left(\left.{#1}\right\|{#2}\right)}
\newcommand{\given}[1]{\left|{#1}\right.}
$$

<!-- codemirror_mode: python
codemirror_mime_type: text/x-cython -->
<!-- <link href="/css/asamarkdown.css" rel="stylesheet"> -->

### [Lake+2017 人間のように考える機械を作る Building machines that learned think like people](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A9535B1D745A0377E16C590E14B94993/S0140525X16001837a.pdf/building-machines-that-learn-and-think-like-people.pdf){:target="_blank"}

ニューラルネットワークが存在する限り，ニューラルネットワークに対する批判も存在する[@minsky69; @fodor88; @pinker88; @crick89; @Marcus1998; @marcus01]。
本稿ではニューラルネットワークに批判的であるが，我々の目標は，その欠点にこだわるのではなく，むしろその成功に立脚することである。
我々は，より人間に近い学習機械を開発する上で，ニューラルネットワークの役割を考えている：
ニューラルネットワークは，勾配ベースの学習と潜在変数の深い階層の力を実証し，多くの種類の機械学習問題に説得力のある方法で適用されてきた。
ニューラルネットワークはまた，認知の計算モデルとしても豊かな歴史を持っている[@Rumelhart1986; @McClelland1986]。
より基本的なレベルでは，学習の計算モデルは最終的に脳の生物学的神経回路網に基づかなければならない。

鍵となる概念

1. 発達段階の スタートアップ・ソフトウェア，すなわち発達初期に存在する認知能力。
ある要素が発達の初期に存在する場合，それは子供や大人がこの論文で取り上げたような種類の課題を学ぼうとするはるか以前から活動的であり，利用可能であることは間違いない。
これは，早期から存在する成分が，それ自体が経験から学習されたものであるか，生得的に存在するものであるかに関係なく当てはまる。
また，早期に存在する要素ほど，その後の発達や学習の基礎となる可能性が高い。
ここでは，2 つの発展的なスタートアップ・ソフトウェアに焦点を当てる (両者のレビューについては Wellman&Gelman1992 参照)。

   1. 直感的物理学 (4.1.1 節)：乳幼児は原始的な物体概念を持っており，これによって物体を経時的に追跡し，物理的にありえない軌跡を割り引くことができる。
例えば，乳幼児は物体が時間と共に持続すること，そして物体が堅固で首尾一貫していることを知っている。
このような一般原則を備えていれば，人はより早く学習し，より正確な予測をすることができる。
課題が新しくなっても，物理学の仕組みは変わらない。
   2. 直観的心理学である (4.1.2 節) ：
幼児は，他人が目標や信念のような心的状態を持っていることを理解し，この理解が学習や予測を強く制約する。
専門家が新しいビデオゲームをプレイするのを見ている子供は，アバターが主体性を持ち，罰を避けながら報酬を得ようとしていると推測できる。
この推論は直ちに他の推論を制約し，子どもはどのような物体が善で，どのような物体が悪なのかを推論できるようになる。
このような推論は，新しい課題の学習をさらに加速させる。
2. 学習
学習には様々な観点があるが，我々はモデル構築を人間レベルの学習の特徴，つまり世界の因果モデルの構築を通して観察されたデータを説明することだと考えている (4.2.2 節)。
この観点に基づけば，直観的な物理学や心理学の初期の現在の能力も，世界の因果モデルである。(4.2.2 節)
学習の主な仕事は，これらのモデルを拡張し，充実させ，他の領域の類似した因果構造理論を構築することである。
機械学習における最先端のアルゴリズムに比べ，人間の学習はその豊かさと効率性で際立っている。
子どもたちは，まばらに観測された事象の根本的な原因を解明し，その知識をデータの少なさをはるかに超えるために利用する能力と欲求を持っている。
人は非常に限られた量の経験から，このような豊かな構造を持つモデルを学習することができるというのは，逆説的に思えるかもしれない。
我々は，**構成性** と **学ぶことを学ぶこと** が，この種の迅速なモデル学習を可能にする要素であることを示唆している (4.2.1 節と 4.2.3 節)。
3. 心が構築した豊かなモデルが，リアルタイムでどのように実行に移されるか (4.3 節)。
我々の知覚と行動の速さには目を見張るものがある。
人は斬新な情景をほんの一瞬で理解し，斬新な発話を口に出して聞くのにかかる時間よりもわずかな時間で理解することができる。
マシンビジョンや音声システムにニューラルネットワークを使用する重要な動機は，脳と同じように素早く反応することである。
ニューラルネットワークは通常，モデル構築よりもパターン認識を目指しているが，このような「モデルフリー」手法が，知覚や認知における遅いモデルベースの推論を加速する方法について議論する (4.3.1 節)。
これらの推論におけるパターン認識を学習することで，コストのかかる中間ステップを経ることなく，推論の出力を予測することができる。
「推論を行うことを学習する」ニューラルネットワークと，豊富なモデル構築学習機構を統合することは，人間の心がなぜこれほど速く，これほどうまく世界を理解できるのかを説明する有望な方法を提供する。
また，強化学習 (4.3.2 節)  におけるモデルベースとモデルフリーの手法の統合についても述べる。
いったん課題の因果モデルが学習されると，人間はそのモデルを用いて，将来の報酬を最大化する行動系列を計画することができる。
モデル構築の成功の尺度として報酬が用いられる場合，これはモデルベースの強化学習として知られている。
しかし，複雑なモデルでのプランニングは面倒で時間がかかるため，スピードと精度のトレードオフはリアルタイム制御には不向きである。
対照的に，現在の深層強化学習の実体化など，モデルを用いない強化学習アルゴリズムは，高速な制御をサポートするが，柔軟性や場合によっては精度を犠牲にする。
我々は，人間がモデルベースとモデルフリーの学習アルゴリズムを競争的・協調的に組み合わせ，これらの相互作用がメタ認知処理によって監督されているという証拠をレビューする。
人間のような洗練された強化学習は，AI 系ではまだ実現されていないが，認知的アプローチと工学的アプローチのクロストークが特に有望な分野である。


### [Higgins+2018 階層的視覚的概念の学習 SCAN: Learning Hierarchical Compositional Visual Concepts](https://openreview.net/forum?id=rkN2Il-RZ){:target="_blank"}

<center>
<div style="width:88%;background-color:cornsilk;text-align:left">

一見無限に見える自然界の多様性は，物理学や化学の法則のような，比較的小さな首尾一貫したルールの集合から生じている。
我々は，これらの規則が，主に教師なしの経験を通じて発見され，抽象的な概念として表現される規則性を生み出すと推測している。
このような表現が構成的で階層的であれば，指数関数的に大きな新しい概念の集合に組み替えることができる。
本稿では，視覚領域におけるこのような抽象概念を学習するための新しいフレームワークである SCAN (Symbol-Concept Association Network) について述べる。
SCAN は，教師無しで発見される分離された視覚的プリミティブを基礎とし，高速な記号関連付けを通して概念を学習する。
最新のマルチモーダル生成モデルのベースラインとは異なり，我々のアプローチは記号と画像のペアリングをほとんど必要とせず，記号表現の形式を仮定しない。
一旦学習されれば，SCAN はマルチモーダルな双方向推論が可能であり，記号記述から多様な画像サンプルを生成し，またその逆も可能である。
また，記号命令や学習された論理的組み換え操作によって，視覚的概念の暗黙の階層を横断し，操作することができる。
このような操作により，SCAN は学習データの分布から離れ，以前に学習した概念の記号的な指示による組み替えを通じて，新しい視覚的概念を想像することができる。
</div></center>

<center>
<img src="/2023assets/2018Higgins_SCAN_fig1.svg" width="66%">
<div style="background-color:lavender;width:88%;text-algin:left">

図 1：物体識別 (I)，物体色 (O)，床色 (F)，壁色 (W) の 4 つの視覚的プリミティブのサブセットに基づいて構築された暗黙の概念階層の概略図 (この例では，情景生成に必要な他の視覚的プリミティブは無視されている)。
概念は暗黙の階層を形成し，それぞれの親はその子や元の視覚的プリミティブの集合を抽象化したものである (視覚的プリミティブの概念を定義する集合の値は太字の大文字で示されている)。
ある概念に対応する画像を生成するためには，抽象化された要素 ("_"で表されている) の値を，それぞれの事前分布からサンプリングするなどして埋める必要がある。
概念階層のあるノードが与えられると，論理演算を使って他のノードをたどることができる。
<!-- Figure 1: Schematic of an implicit concept hierarchy built upon a subset of four visual primitives: object identity (I), object colour (O), floor colour (F) and wall colour (W) (other visual primitives necessary to generate the scene are ignored in this example).
Concepts form an implicit hierarchy, where each parent is an abstraction over its children and over the original set of visual primitives (the values of the concept-defining sets of visual primitives are indicated by the bold capital letters).
In order to generate an image that corresponds to a concept, one has to fill in values for the factors that got abstracted away (represented as “_”), e.g. by sampling from their respective priors.
Given certain nodes in the concept hierarchy, one can traverse the other nodes using logical operations. -->
<!-- See Sec.3 for our formal definition of concepts. -->
</div></center>

<center>
<img src="/2023assets/2017Higgins_SCAN_fig1ja_.svg" width="66%">
<div style="width:88%;background-color:lavender;text-align:left">
(A) SCAN モデルの構成図。
(B) SCAN の損失関数の余分な KL 項のモードカバレッジ。
各青色モードは，画像 $x_ {i}$ が与えられたときに推定される視覚的潜在分布 $q(z^ {k}_  {x}\vert x_ {i})$ に対応する。
黄色い分布は学習された概念的潜在分布 $q(z^ {k}_ {y})$ に対応する。
特定の生成因子に対して高い変動性を持つ視覚的事例，例えばリンゴの事例を見るときの様々な照明条件，が提示されたとき，データ生成因子に対する事前分布に近い，対応する概念潜在量 $q(z^ {k}_ {y})$ の広範な分布を学習することが重要である。
これは，モードを選ぶ逆 KL ダイバージェンス $D_ {KL}(z_ {y}\vert\vert z_ {x})$ ではなく，順 KL ダイバージェンス $D_{KL}(z_ {x}\vert\vert z_ {y})$ により達成することができる。
C: $\beta-\text{VAE}_{\text{DAE}}$ モデルアーキテクチャ。
<!-- Figure 1: A: SCAN model architecture.
B: Mode coverage of the extra KL term of the SCAN loss function.
Each blue mode corresponds to an inferred visual latent distribution q(zk xjxi) given an image xi.
The yellow distribution corresponds to the learnt conceptual latent distribution q(zk y ).
When presented with visual examples that have high variability for a particular generative factor, e.g. various lighting conditions when viewing examples of apples, it is important to learn a broad distribution for the corresponding conceptual latent q(zk y ) that is close to the prior distribution for the data generative factor.
This can be achieved through forward KL divergence DKL(zxjjzy), rather than the mode picking reverse KL divergence DKL(zyjjzx).
C:beta-VAEDAE model architecture.-->
2017Higgins_SCAN Fig. 1, 2 を改変
</div></center>

### NIC (Neural Caption Generation)

<center>
<img src="/assets//17VISIOn-slide-WBE2-jumbo.jpg" width="49%"><br/>
- 人間: A group of men playing Frisbee in the park.
- 機械: A group of young people playing a game of Frisbee.
</center>

<img src="/assets/2014Vinyals_Fig5_left.jpg" width="44%">
<img src="/assets/2014Vinyals_Fig5_right.jpg" width="44%"><br/>
Vinyals et. al (2014) より

### 二段階仮説

* [線分二等分課題 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_1210bit_line_bisection.ipynb){:target="_blank"}

- 腹側経路 ventral pathways (what 経路)
- 背側経路 dorsan pathways (where 経路)

<center>
<img src="/assets/1982Ungerleider_Mishkin.jpg" width="33%">
<img src="/assets/LNCS2766_Chapter_2_fig2_4.jpg" width="49%"><br/>
左: Ungerleider&Mishkin1982 より，
右: Behnke2003 より
</center>

同様の 2 経路による処理は 聴覚 (Romanski+1999) や 触覚 (Reed+2005) でも発見されている。

<div style="color:lightgray">

発展的な話題としては，このような 2 種類の処理経路は，
処理される情報の種類の問題ではないくて，機能に関与した区別であるとの仮説もあります。すなわち

* 腹側経路は物体に関する情報の知覚 (知覚のための視覚)
* 背側経路は行動を導くための情報処理 (行動のための視覚)

さらに，背側経路 は背外側経路 dorsolateral と背中側経路 dorsomedial に細分化できることが示唆されている（Binkofski&Buxbaum2013, Grafton2010, Rizzolatti&Matelli2003）。

* 背外側側経路 前頭頂内溝（aIPS）と前頭前皮質の腹側部分（PMv）, 古典的に到達運動の計画に寄与 （Davare+2015, Davare+2012, Vesia&Crawford2012）
* 背中側経路は V6A と内側頭頂内溝 を介して背側前頭前皮質（PMd）へ. 把持に関連する情報を統合する（Davare+2007, Davare+2010, Tunik+2005）

最近では，これら 2 つの 副回路が行動によって要求されるオンライン制御の程度に応じて相互作用することも発見されている (Grol+2007, Verhagen+2013)。
</div>

### R-CNN (Girshich+2015)

<center>
<img src='/assets/2013Girshick_RCNN_Fig1.svg' style='width:66%'><br>
Girshick (2013) より
<!--
<img src='../assets/2014SPP.svg' style='width:74%'><br>
Girshick (2013) より-->
</center>

### Fast R-CNN と Faster R-CNN (2014)

<center>
<img src='/assets/2015Fast_R-CNN_Fig1.svg' style='width:66%'><br>
Fast R-CNN

<!-- <img src='../assets/2015Faster_RCNN_RPN.svg' style='width:74%'><br>Faster R-CNN-->
</center>


## VAE: Variational Auto-Encoders

**変分自己符号化器 VAE:Variational Auto-Encoders** は [2014Kingma&Welling](https://arXiv.org/abs/1406.5298) と [Rezende+2014](https://arXiv.org/abs/1401.4082) によって提案された 変分ベイズ に基づく **半教師ありネットワーク** である。
下図 に通常の自己符号化器と変分自己符号化器 VAE の相違を示した。
自己符号化器は，中間層での結合が潜在変数のサンプリングに置き換えられている。
潜在変数である未知の変数の確率分布を類推する手法にはいくつか存在する。
このうちベイズ推論を援用して推定を行うため変分ベイズとも呼ばれる手法を変分自己符号化器 VAE と呼ぶ。
VAE は データ $x$ が与えられたときモデルを記述する潜在変数 $z$ を類推するための符号化器，復号化器に ディープニューラルネットワーク を用いるモデルである。

<div class="figcenter">
<img src="/2023assets/rep_learning_illustrations_ja_sub.pdf.svg">
</div>

VAE の特徴を列挙すれば，以下のようになる:
1. 符号化器・復号化器モデル
2. 符号化器と復号化器とは共に DNN を用い
4. 符号化器と復号化器との間に潜在変数 $z$ を仮定し，$z$ の確率密度を推定する
5. 符号化器はデータ $x$ を潜在変数 $z$ の空間へ写像
6. 復号化器は潜在変数 $z$ の確率密度をベイズ推論によって データ $x$ を再構築する **生成モデル**
7. VAE の学習時に必要となる目的関数では **再パラメータ化トリック reprametrization trick** を用いることで勾配降下法が利用可能

<!-- % VAE では 潜在空間上の事前分布によって定義される潜在空間に入力を表現 (推論) します。
% 一方，復号化器は潜在空間上での表現から入力を再構築します。
% このとき潜在空間が解釈可能な表現，すなわち解絡化，離散化されていることが仮定されます。 -->

変分法とは歴史的には物理学でニュートンの運動法的式を一般化する過程で発展した一般的手法である。
ディープラーニングとの関連では，最適化手法や確率アルゴリズムの基盤となる考え方である。
<!-- %用いられてきた制約付き最大値 (または最小値) を求める手法です。 -->
VAE ではベイズ推論を用いて変分法による解を求める。
このために **変分ベイズ variational Bayes** または **変分推論 variational inference** と呼ばれる。
変分ベイズ法の解法には，平均場近似が主として用いられてきだが，Kingma らの提案手法により応用が広がった。


上図に即して，やや詳しく書くと次のようになる。
VAE は観測可能 (で複雑) なデータ $x$ を 経験分布 $q_\phi(x)$ と，比較的単純な分布である潜在変数 $z$ の空間との間の確率的に写像することを学習する。
**生成モデル** $p_{\theta}$ は $x$ と $z$ との同時分布 $p_{\theta}\of{x, z}$ を学習する。
この同時分布を因子分解すると $p_{\theta}(x,z)=p_{\theta}(z) p_{\theta}\of{x\given{z}}$ となる。
この式は，観察可能な変数 $x$ と潜在変数 $z$ の同時分布が，潜在変数 $z$ の事前分布と，確率的に振る舞う復号化器の出力 $p_\theta\of{x\given{z}}$ の積であることを示している。
%潜在空間の事前分布 $p_\theta\of{z}$ と確率的符号化器 $p_\theta\of{x\given{z}}$ に因数分解された同時同分布 $p_\theta\of{x,z}=p_{\theta}\of{z} p_{\theta}\of{x\given{z}}$ を学習する。
\strong{推論モデル}\footnote{inference model} $q_{\phi}$ は，確率的な符号化器 $q_{\phi}\of{z\given{x}}$ であり，生成モデルの出力である事後分布 $p_{\theta}\of{z\given{x}}$ を近似する。
それぞれの記号の対応関係を 図で確認せよ。
$\phi$, $\theta$ は原著論文 [@2014Kingma_VAE] の記号に対応していますが，慣れないうちは無視してよい。

潜在変数 $z$ の真の分布 $q\of{z}$ と入力 $x$ が与えられたときの $z$ の推定値を $p\of{z\given{x}}$ とする。
そうすると VAE の目標関数は両分布の **KL ダイバージェンス** を小さくすることが求められる。
KL ダイバージェンスは $\text{KL}\of{X\vert\vert Y}$
あるいは $D_{\text{KL}}\of{X\vert\vert Y}$ などと表記される。
KL ダイバージェンスは $X$ と $Y$ との分布間の乖離の度合い，ある種の距離と考えることも可能である。
しかし，KL ダイバージェンスは，どちらか一方から他方との乖離 (距離)を考えるかによってその値が異なる。
$$
\text{KL}\of{X\vert\vert Y}\ne\text{KL}\of{Y\vert\vert X}
$$
等号が成立するのは，両分布が等しい場合に限られる。

VAE では，この KL ダイバージェンスを直接計算することが難しいため，KL ダイバージェンスを計算することと等価な **ELBO (Evidence Lower BOund)** を最小化することが行われる。
ELBO は **変分下限 Variational Lowver bound** とも呼ぶ。

入力データ $x$ を用いたモデルの対数尤度を $\log\of{x}$ とすれば，この対数尤度を最小化するために潜在変数 $z$ を導入し，導入した $z$ を含めた関数の最適化とみなすことができる。
このため単純な最適化ではなくなり，汎関数の最適化となる。
これを **変分法 (variational method)** と呼ぶ。
変分法は，物理の分野で開発された手法ですが，広く条件付き最適化に応用可能で，経済学，社会学，統計学，でも用いられている。

$$
\log p\of{x}=\mathcal{L}\of{q}+\text{KL}\of{q\of{z}\vert\vert p\of{z\given{x}}}
$$

最適な $z$ の分布 $q^*\of{z}$ は
$$
q^*\of{z}=\arg\min_{q\of{z}\in\mathcal{L}}\text{KL}\of{q\of{z}\vert\vert p\of{z\given{x}}}
$$
と書る。
$\log p\of{x}$ を計算することは困難である。
なぜなら
$\text{KL}\of{q\of{z}\vert\vert p\of{z\given{x}}}=\mathbb{E}\Of{\log q\of{z}}-\mathbb{E}\Of{\log p\of{z\given{x}}}$ であり，

$$
\text{KL}\of{q\of{z}\vert\vert p\of{z\given{x}}} =\mathbb{E}\Of{\log q\of{z}}-\mathbb{E}\Of{\log p\of{z,x}} + \log p\of{x}.
$$

重要用語として **再パラメータ化 (リパラメトリゼーショントリック eparametrization tricks)** があある。

$$
p\of{\theta\given{\mathcal{D}}}=\frac{p\of{\theta\given{\theta}}p\of{\theta}}{p\of{\theta}}
=\frac{p\of{\theta\given{\theta}}}
{\int p\of{\theta\given{\theta}} p\of{\theta}\;d\theta}
\tag{eq:vbayes}
$$

$$
p\of{\text{潜在変数}\given{\text{データ}}}=\frac{p\of{\text{データ}\given{\text{潜在変数}}}p\of{\text{潜在変数}}}{p\of{\text{データ}}}
=\frac{p\of{\text{データ}\given{\text{潜在変数}}}}
{\int p\of{\text{データ}\given{\text{潜在変数}}} p\of{\text{潜在変数}}\;d\text{潜在変数}}
\tag{eq:vbayes}
$$

式 (eq:vbayes) の最右辺分母が事実上積分不可能なので，**平均場近似 (mean field approximation)** で置き換えるのが従来手法であった。

### VAE

* $\beta$-VAE [2017Higgins_betaVAE]
* disentangled representation [2018Higgins_disentagled_representation], total correlation, KKT condition

VAE の模式図を図 (fig:2019Kingma_Welling_fig2.2) に示した。
図 (fig:2019Kingma_Welling_fig2.2) は左から入力が与えられる。
入力データは推論モデルを通して潜在空間上の $z$ を予測する。
実際にはサンプリングがおこなわれ，さらに $z$ と入力データに基づいて生成モデルから目的関数が計算される。

<div class="figcenter">
<img src="/2023assets/2019Kingma_Welling_vae_cartoon_ja.svg">
<div class="figcaption" style="width:44%">

変分自己符号化器の目標関数 ELBO の概念図 (2019Kingma_Welling_VAE) Fig. 2.2 を改変
</div></div>

このことは，GAN と良い対比となる。

<div class="figcenter">
<img src="/2023assets/gan_illustration_ja.svg">
<div class="figcaption" style="width:44%">

<!-- %Adversarial density ratio estimation vs MMD.\label{fig:gansmmds} Figure (a): -->
GAN では生成モデルの訓練に敵対的密度比推定を使用する。
これは 2 人ゲームと見ることができる。
識別器はサンプルが実在か，または生成器が生成したデータかを予測しようとする。
生成器は実在サンプルの分布を模倣することで識別器を欺こうとする。
<!-- %GANs use adversarial density ratio estimation to train a generative model, which can be seen as a two-player game:
The discriminator tries to predict whether samples are real or generated, while the generator tries to deceive the discriminator by mimicking the distribution of the real samples.
%Figure (b): The MMD corresponds to the distance between mean feature embeddings. -->
</div></div>

### 変分法，変分下限， ELBO

<div class="figcenter">
<img src="/2023assets/2017Higgins_SCAN_fig1ja_.svg" width="66%">
<div class="figcaption" style="width:33%">

2017Higgins_SCAN Fig. 1, 2 を改変
</div></div>

図 (fig:scan) の青いモードは，データ $x_i$ が与えられた際に，視覚の潜在分布 $q(z_x^k\vert x_i)$ に対応している。
黄色の分布は，学習した概念的潜在分布 $q(z_y^k)$ である。

VAE の損失関数としては **ELBO (Evidence Lower BOund)** を用いる。
<!-- ELBO 変分下限と呼ばれていたものです。 -->
モデルの対数尤度は，データが所与のときの $z$ の潜在確率

$q\of{z\given{x}}$ と $p\of{z}$ の間の KL ダイバージェンスと $p_\theta\of{\log p\of{x\given{z}}}$ の和である。

$$
\ell = D_{\text{kL}}\of{} + \alpha\of{1-G\of{D\of{X}}}
$$

ということになる。
VAE を理解する上では，生成モデルと変分パラメータを理解する必要がある。

そもそも **平均場近似 mean field approxmation** と呼ばれてきた。
その意味はベイズの定理を使って反転させた時

$$
p\of{m\given{D}}=\frac{p\of{D\given{m}}p\of{m}}{p\of{D}}
$$
だからである。
このとき左辺の分子 $p\of{D}$ は分からない。

変分推論の背後にある考え方は次のようなものである：
簡単なパラメトリック分布 $Q_\phi\of{Z\given{X}}$ (正規分布など)で事後推論を実行する。
$Q_\phi$ が可能な限り $P$ に近くなるようにパラメータ $\phi$ を調整する。
これは以下に視覚的に図示されている。
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

### 再パラメータ化トリック

確率変数 $z$ はデータ $x$ と変分パラメータとから計算される。
ところが変分パラメータを直接微分することが難しい。
このため，誤差逆伝播法を用いた学習を行う場合に工夫が必要になる。
簡単に述べると $z$ を平均 $\mu$ 分散 $\sigma^2$ に従う正規分布だとみなしてしまうことで $q_{\phi}\of{z\given{x}}=\mathcal{N}\of{z;\mu,\sigma^2}$ と考えることにする。
データ $x$ が与えられたとき符号化器の出力を $\mu$ と $\sigma$ と誤差 $\epsilon$ とみなして潜在変数 $z$ を近似することを **再パラメータ化トリック (reparametrization trick)** と呼ぶ。
潜在変数 $z$ は多次元で複雑なはずだが，各次元が独立であると仮定すれば計算が簡単になる。
さらに $z$ の各次元の分散 $\sigma^2$ が等しいという仮定をおけば，求めるパラメータ数が減り計算が簡単になる。

本来は複雑であるはずの潜在変数を，最パラメータ化トリックによってどこまで簡略化できるかについては慎重になるべきである。
だが，仮にこのような簡略化が可能であれば，潜在変数の解釈可能性，表現可能性を議論できる。
これにより DNN の解釈可能性が広がると考えられる。
このような動向に基づき $\beta$-VAE (2017Higgins_betaVAE,2018Burgess_understanding_betaVAE)，因子化 VAE (2018KimMnih_factorVAE)，トータル相関 VAE (2018Chen_TCVAE_MIG) などが提案されている。

### 解縺表現

**解縺表現** とは disentaglement あるいは disentangled represenation の訳である。
日本語としての定訳がないためここでは仮に解きほぐしとした。
国際会議 ICRL が表現学習を標榜しているように，深層学習についての批判として，内部で行なわれていることが不明であることが挙げられる。
これに対する解答としての表現学習，多様体学習，解絡表現などについて言及されてきた。
解きほぐし表現とは，畳み込み多層ニューラルネットワークによって得られた表現が，解釈不能であった場合，より簡易で単純な表現を与えることを指す。
大量かつ多次元データを取り扱い，かつ人間に比肩しうる精度を達成してきた深層学習モデルへの要求として次に求められる課題として，如何に解釈可能な表現を提示できるかという点が挙げられる。

解絡表現，あるいは解絡学習に対する解答の一つとして変分自己符号器 variational autoencoders が挙げられる。
変分自己符号器 VAE は，入力情報を忠実に再現する **雑音除去自己符号器 denoising autoencoders (2008Vincent_denoising)** と異なる。
符号器 (encoders) と復号器 (decoder) との中間に潜在変数を仮定する。
符号器と復号器との間に潜在変数を仮定し，その潜在変数の分布をベイズ推論によって変分推定することに特徴がある。
再パラメータ化トリックの項でも説明したように，潜在変数間に直交性を仮定すれば，解釈可能な表現を得ることが期待できる。
このことに端を発して多くの研究がなされている。

とりわけゲームチェンジャーとなったのは，**変分自動符号器 (variational autoencoders)** の提案であった (2014Kingma_VAE, 2014Rezende_ICML)。
変分自動符号器では，符号器と復号器に深層学習モデルを用い，潜在変数の推定に変分ベイズモデルが用いられた。
図 (fig:2018Tschannen) には変分自動符号器モデルが示している。


#### バニラマルチモーダル変換モデル <!-- #### A Vanilla Multimodal Transformer Model-->

Transformer は，ビデオ分類 (ViViT) やオーディオ分類 (AST) を含む ML 課題において，常に最先端の結果を得ている。
画像を画素単位で処理する標準的な畳み込みアプローチとは対照的に，ViT は画像をパッチトークン (すなわち，複数の画素で構成される画像の小さな部分 (パッチ) からのトークン) の系列として扱う。
そしてこれらのモデルは，パッチ・トークンのすべての対にわたって自己注意操作を実行する。
しかし，マルチモーダル融合に Transformer を使用することは，計算コストが高く，複雑さが入力系列の長さに対して 2 次関数的にスケーリングされるため，困難である。
<!-- Transformer models consistently obtain state-of-the-art results in ML tasks, including video (ViViT) and audio classification (AST).
Both ViViT and AST are built on the Vision Transformer (ViT); in contrast to standard convolutional approaches that process images pixel-by-pixel, ViT treats an image as a sequence of patch tokens (i.e., tokens from a smaller part, or patch, of an image that is made up of multiple pixels).
These models then perform self-attention operations across all pairs of patch tokens.
However, using transformers for multimodal fusion is challenging because of their high computational cost, with complexity scaling quadratically with input sequence length. -->

Transformer は可変長系列を効果的に処理するため，ViT のような単一モダリティ Transformer をマルチモーダルなケースに拡張する最も簡単な方法は，Transformer のアーキテクチャに最小限の変更を加えるだけで，視覚と聴覚の両方のトークン系列をモデルに与えることである。
我々はこれをバニラ・マルチモーダル Transformer モデルと呼んでいる。
バニラ・マルチモーダル Transformerモデルは，画像の異なる空間領域や時間領域間，またスペクトログラムで表される音声入力の周波数や時間を超えた自由な注意の流れ (バニラ交差注意と呼ばれる) を可能にする。
しかし，音声と映像の入力トークンを連結することで簡単に実装できるが，音声と映像の入力には，課題にとって冗長である可能性のある，高密度で細かい情報が含まれているため，Transformer モデルのすべての層におけるバニラ交差注意は不要であり，複雑さが増大する。
<!-- Because transformers effectively process variable length sequences, the simplest way to extend a unimodal transformer, such as ViT, to the multimodal case is to feed the model a sequence of both visual and auditory tokens, with minimal changes to the transformer architecture.
We call this a vanilla multimodal transformer model, which allows free attention flow (called vanilla cross-attention) between different spatial and temporal regions in an image, and across frequency and time in audio inputs, represented by spectrograms.
However, while easy to implement by concatenating audio and video input tokens, vanilla cross-attention at all layers of the transformer model is unnecessary because audio and visual inputs contain dense, fine-grained information, which may be redundant for the task — increasing complexity. -->

#### Restricting Attention Flow

マルチモーダルモデルにおける長い系列の複雑化という問題は，注意の流れを減らすことで軽減できる。
我々は 2 つの方法，融合層の指定と注意のボトルネックの追加を用いて注意の流れを制限する。
<!-- The issue of growing complexity for long sequences in multimodal models can be mitigated by reducing the attention flow.
We restrict attention flow using two methods, specifying the fusion layer and adding attention bottlenecks. -->

* **融合層** (初期，中期，後期のフュージョン) ：
マルチモーダルモデルにおいて，クロスモーダルな相互作用が導入される層はフュージョン層と呼ばれる。
2 つの極端なバージョンは，初期フュージョン (Transformer 内のすべてのレイヤーがクロスモーダル)と後期フュージョン (すべての層がユニモーダルであり，Transformer 符号化器でクロスモーダル情報が交換されない)である。
その中間のフュージョン層を指定すると，ミッドフュージョンとなる。
この技法は，マルチモーダル学習における一般的なパラダイムに基づくもので，クロスモーダルなフローをネットワークの後の層に制限し，初期層がユニモーダルなパターンの学習と抽出に特化できるようにするものである。
* **注意のボトルネック**：
注意ボトルネック (下図紫色) は，モダリティ内の自由な注意の流れを許しながらも，各モダリティからの情報を他のモダリティと共有する前に，各モダリティの情報を照合し，凝縮させる。
我々は，このボトルネックバージョン (MBT) が，より低い計算コストで，制限のない対応物を上回るか，それに匹敵することを実証する。

<!-- * **Fusion layer** (early, mid or late fusion): In multimodal models, the layer where cross-modal interactions are introduced is called the fusion layer. The two extreme versions are early fusion (where all layers in the transformer are cross-modal) and late fusion (where all layers are unimodal and no cross-modal information is exchanged in the transformer encoder). Specifying a fusion layer in between leads to mid fusion. This technique builds on a common paradigm in multimodal learning, which is to restrict cross-modal flow to later layers of the network, allowing early layers to specialize in learning and extracting unimodal patterns.
* **Attention bottlenecks**: We also introduce a small set of latent units that form an attention bottleneck (shown below in purple), which force the model, within a given layer, to collate and condense information from each modality before sharing it with the other, while still allowing free attention flow within a modality. We demonstrate that this bottlenecked version (MBT), outperforms or matches its unrestricted counterpart with lower computational cost. -->

<div class="figcenter">
<img src="/2023assets/MBT Bottleneck Transformer 07.gif" width="77%">
<!-- <img src="https://lh3.googleusercontent.com/syHWoS-2bHO4qQVe4Q0I8g7pol9c_yZI63d3idE2PXL9Xgq_nBFzKVedw8GnQ181mHqzQHJ9VupJTavSqFvZ0ViGs146rkwZK8zICD-LfMzjgQtHzf2jFMjNlsB75PpDVTAE8QwHeQ=w640-h182" width="66%"> -->
<div class="figcaption">

モデルにおける様々な注意の構成。
Transformer 符号化器でクロスモーダル情報が交換されない後期融合 (左上) とは異なり，我々はクロスモーダル情報の交換のための 2 つの経路を研究している。
初期融合と中期融合 (上段中央，上段右)は，1 つの層のすべての隠れユニットにまたがる標準的なペアワイズ自己注意を介して行われる。
中期融合では，クロスモーダル注意はモデル内の後の層にのみ適用される。
ボトルネック・融合 (左下) は，注意のボトルネックと呼ばれるタイトな潜在ユニットを介して，層内の注意の流れを制限する。
ボトルネック・中期融合 (右下) は，最適な性能を得るために，両方の制限を組み合わせて適用する。
<!-- The different attention configurations in our model.
Unlike late fusion (top left), where no cross-modal information is exchanged in the transformer encoder, we investigate two pathways for the exchange of cross-modal information.
Early and mid fusion (top middle, top right) is done via standard pairwise self attention across all hidden units in a layer.
For mid fusion, cross-modal attention is applied only to later layers in the model.
Bottleneck fusion (bottom left) restricts attention flow within a layer through tight latent units called attention bottlenecks.
Bottleneck mid fusion (bottom right) applies both forms of restriction in conjunction for optimal performance. -->
</div></div>


#### ボトルネックと計算コスト <!--  #### Bottlenecks and Computation Cost-->

我々は MBT を AudioSet データセットを用いた音の分類課題に適用し，2 つのアプローチについてその性能を調べた：
(1) バニラ交差注意，(2) ボトルネック融合。
両アプローチとも，中期融合 (下の x 軸の真ん中の値で示される) は，初期融合 (融合層=0) と後期融合 (融合層=12) の両方を上回る。
このことは，このモデルが，クロスモーダルな接続を後期層に制限することで，初期層がユニモーダルな特徴の学習に特化できるようになり，利益を得ていることを示唆している。
我々は，注意のボトルネックを追加すること (ボトルネック融合) は，すべての融合層で，バニラ交差注意よりも優れているか，あるいは性能を維持していることを発見した。
<!-- We apply MBT to the task of sound classification using the AudioSet dataset and investigate its performance for two approaches:
(1) vanilla cross-attention, and (2) bottleneck fusion. For both approaches, mid fusion (shown by the middle values of the x-axis below) outperforms both early (fusion layer = 0) and late fusion (fusion layer = 12).
This suggests that the model benefits from restricting cross-modal connections to later layers, allowing earlier layers to specialize in learning unimodal features; however, it still benefits from multiple layers of cross-modal information flow.
We find that adding attention bottlenecks (bottleneck fusion) outperforms or maintains performance with vanilla cross-attention for all fusion layers, with more prominent improvements at lower fusion layers. -->

<div class="figcenter">
<img src="/2023assets/2022Nagrani_Attention_Bottlenecks_fig3.svg" width="66%">
<div class="figcaption">

融合に注意ボトルネックを使用した場合の，AudioSet 上の異なる融合層における mAP 性能 (左) と計算量 (右) への影響。
注意ボトルネック (赤) は，バニラ交差注意 (青) よりも低い計算コストで性能を向上させる。
融合層 4-10 にある中期融合は，初期融合 (融合層=0) と後期融合 (融合層=12) の両方を上回り，融合層 8 で最高性能を発揮する。
<!-- The impact of using attention bottlenecks for fusion on mAP performance (left) and compute (right) at different fusion layers on AudioSet.
Attention bottlenecks (red) improve performance over vanilla cross-attention (blue) at lower computational cost.
Mid fusion, which is in fusion layers 4-10, outperforms both early (fusion layer = 0) and late (fusion layer = 12) fusion, with best performance at fusion layer 8. -->
</div></div>
