---
title: 第10回
date: 2021年11月26日
layout: home
---

## 実習ファイル

* [DeepLabV3 によるセマンティックセグメンテーション <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_1126semantic_segmentation_pytorch_deeplabv3_resnet50.ipynb)
* [Detectron2  <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2020_0605Detectron2.ipynb)
* [顔のキーポイント <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/project-ccap/project-ccap.github.io/blob/master/2021notebooks/2021_1010facial_keypoints_detection.ipynb)

<!-- 
1. R−CNN から位置情報と物体情報とを切り分けて，実時間処理が可能に
2. YOLO, SSD 
3. Squeeze-and-Extention など分岐して結合する流れ
4. EfficientNet
5. 対比学習 によりトップ 1 精度でも性能向上

- R-CNN によって，位置 where 情報と 物体 what 情報 とを多層畳み込みニューラルネットワークで表現する試みが，発展。
実時間で物体の切り出しと認識とが行えるようになった。
* [Faster R-CNN](https://arxiv.org/pdf/1506.01497.pdf){:target="_blank"}, 
* [YOLO](https://arxiv.org/pdf/1506.02640.pdf){:target="_blank"}, 
* [SSD](https://arxiv.org/pdf/1512.02325.pdf){:target="_blank"},
-->

# 2 経路仮説
- 腹側経路 ventral pathways ("what" 経路)
- 背側経路 dorsan pathways ("where" 経路)

<center>
<img src="/assets/1982Ungerleider_Mishkin.jpg" width="39%" hspace="30px">
<img src="/assets/LNCS2766_Chapter_2_fig2_4.jpg" width="54%" hspace="1cm"><br/>
左: Ungerleider and Mishkin (1982) より, 右: Behnke (2003) より<br/>
</center>

<font color="indigo">同様の 2 経路による処理は 聴覚 (Romanski et al., 1999) や 触覚(Reed et al., 2005)でも発見されています。</font>

<center>
<div style="text-align: left;width: 88%;text-color:teal">

発展的な話題としては，このような 2 種類の処理経路は，処理される情報の種類の問題ではないくて，機能に関与した区別であるとの仮説もあります。すなわち

* 腹側経路は物体に関する情報の知覚 (知覚のための視覚) 
* 背側経路は行動を導くための情報処理 (行動のための視覚) 

さらに，背側経路 は背外側経路 dorsolateral と背中側経路 dorsomedial に細分化できることが示唆されています（Binkofski and Buxbaum, 2013, Grafton, 2010, Rizzolatti and Matelli, 2003)。

* 背外側側経路 前頭頂内溝（aIPS）と前頭前皮質の腹側部分（PMv）, 古典的に到達運動の計画に寄与 （Davareら、2015、Davareら、2012、Vesia and Crawford、2012）
* 背中側経路は V6A と内側頭頂内溝 を介して背側前頭前皮質（PMd）へ. 把持に関連する情報を統合する（Davareら、2007、Davareら、2010、Tunikら、2005）

最近では、これら2つの 副回路が 行動によって要求されるオンライン制御の程度に応じて相互作用することも発見されている (Grol et. al., 2007, Verhagen et al., 2013)。
</div>
</center>

# 二段階モデル

## R-CNN

<center>
<img src='/assets/2013Girshick_RCNN_Fig1.svg' style='width:74%'><br>
Girshick (2013) より
<!-- 
<img src='/assets/2014SPP.svg' style='width:74%'><br>
Girshick (2013) より
-->
</center>

<center>
<img src='/assets/2013Uijings_Selective_Search_Fig1.svg' style='width:66%'><br>
Selective Search (2015) より
</center>

## Fast R-CNN と Faster R-CNN (2014)

<center>
<img src='/assets/2015Fast_R-CNN_Fig1.svg' style='width:74%'><br>
Fast R-CNN

<img src='/assets/2015Faster_RCNN_RPN.svg' style='width:74%'><br>
Faster R-CNN
</center>


### 画像切り出し

1. 物体位置
3. 物体認識 object recognition
2. 意味的切り出し semantic segmentation
4. 対象切り出し instance segmentation
5. 特徴点抽出 keypoint
6. パノプティック切り出し

<div align="center">
<img src="/assets/2017DangHa_History_Of_Object_Recognition_ja.svg" style="width:88%"><br/>
Dang and Ha (2017) より
</div>

<!-- ## セマンティックセグメンテーション(意味的切り出し)，インスタンスセグメンテーション(実体切り出し) 及び パノプティックセグメンテーション(汎光学的切り出し)

- 完全畳み込みネットワーク(Fully Convolutional Network:FCN) と呼ばれるセマンティックセグメンテーションを実現するネットワーク
- FCN とは文字通り全ての層が畳込み層であるモデル
-->

<center>
<img src='/assets/2015Long_FCN.svg' style='width:94%'></br>
Long (2017) FCN
</center>

- 通常のCNN は，出力層のユニット数が識別すべきカテゴリー数であった。一方 FCN では入力画像の画素数だけ
出力層が必要になる。
- すなわち各画素がそれぞれどのカテゴリーに属するのかを出力する必要があるため出力層には，縦画素数 $\times$ 横画
素数 $\times$ カテゴリー数の出力ニューロンが用意される。
- 図 では，識別すべきカテゴリー数 が 20 であったたま，どのカテゴリーにも属さない，すなわち背景を指示するもう1 
つのカテゴリーを加えた計 21 カテゴリーの分類を行うことになる。

- CNN では畳込演算によって畳込みのカーネル幅(受容野) だけ近傍の入力刺激を加えて計算することになるため，
上位層では下位層に比べて受容野が大きくなることの影響で画像サイズは小さく(あるいは粗く) なってしまう
- このため，最終出力層に入力層と同じ解像度の画素数を得るためには，畳込みと反対方向の解像度を細かくする工夫が必
要となる。
- これを解決する一つの方法がアンサンプリング(unsampling) と呼ばれる方法
- 下位のプーリング層の情報を用いて詳細な解像度を得る
- 図 はアンサンプリングにより詳細な画像，すなわち最終的には入力画像と等解像度の出力を得る仕組みを示している。

<center>
<img src='/assets/2015Long_FCN2J.svg' style='width:94%'><br>
</center>



# ELBO

<center>
<video width="720" height="480" controls>
<source src="https://komazawa-deep-learning.github.io/assets/ELBO.mp4" type="video/mp4" controls autoplay> <br/>
Your browser does not support the video tag.
</video>
</center>

# EM アルゴリズム

$\theta$ を未知パラメータ，$x$ を既知のデータとすると，$\theta$ と $x$ とを含む全体の尤度を計算することを考える。

* 未知パラメータの期待値を計算する $\theta^{* }$


# 固有顔
<!-- # Eigenfaces -->

与えられた画像表現の問題点は， その高い次元性です。
pxq の 2 次元濃淡画像は pq 次元のベクトル空間に属しているので，100x100 画素の画像はすでに 10,000 次元の画像空間に存在していることになります。
問題は， すべての次元が同じように役に立つのかということです。
私たちは， データに分散がある場合にのみ判断を下すことができます。
したがって， 私たちが探しているのは， 情報の大部分を占める成分です。
主成分分析 (PCA) は Karl Pearson (1901) と Harold Hotelling (1933) によって独立に提案されたもので，相関している可能性のある変数の集合を， 相関していない変数のより小さな集合に変換するものです。
このアイデアは，高次元データセットは，しばしば相関した変数によって記述され，したがって，情報の大部分を占める意味のあるいくつかの次元だけがあるというものです。
PCA 法は， 主成分と呼ばれる， データの中で最大の分散を持つ方向を見つけます。
<!--The problem with the image representation we are given is its high dimensionality. 
Two-dimensional pxq grayscale images span a pq-dimensional vector space, so an image with 100x100 pixels lies in a 10000-dimensional image space already. 
The question is: Are all dimensions equally useful for us? 
We can only make a decision if there's any variance in data, so what we are looking for are the components that account for most of the information. 
The Principal Component Analysis (PCA) was independently proposed by Karl Pearson (1901) and Harold Hotelling (1933) to turn a set of possibly correlated variables into a smaller set of uncorrelated variables. 
The idea is, that a high-dimensional dataset is often described by correlated variables and therefore only a few meaningful dimensions account for most of the information. 
The PCA method finds the directions with the greatest variance in the data, called principal components.
-->

## 固有顔法の数学的記述
<!-- ## Algorithmic Description of Eigenfaces method -->

$\mathbf{X}=\left(x_{1},x_{2},\ldots,x_{n}\right)$ を観測データ $x_{i}\in\mathbb{R}^{d}$ からのランダム抽出されたデータだとします。

1. 平均 $\mu$ を計算する
$$
\mu = \frac{1}{n}\sum_{i=1}^{n}x_{i}.
$$

2. 共分散行列 $\mathbf{S}$ を計算する
$$
\mathbf{S}=\frac{1}{n}\sum_{i=1}^{n}\left(x_{i}-\mu\right)\left(x_{i}-\mu\right)^{\top}.
$$

3. 固有値 $\lambda_{i}$ と対応する固有ベクトル $\nu_{i}$ を $\mathbf{S}$ から計算する:
$$
\mathbf{S\nu}_ {i},\hspace{1cm}\text{$i=1,2,\ldots,n$}
$$

4. 固有値に従って固有ベクトルを降順に並べ，$k$ 番目の成分は，$k$ 番目に大きい固有値に対応する固有ベクトルとする。
第 $k$ 主成分に対応する 観測データ $x$ の固有ベクトルは，次式で求めることができる

$$
\mathbf{y} = \mathbf{W}^{\top}\left(\mathbf{x}-\mathbf{\mu}\right).
$$

ここで $\mathbf{W}=\left(\nu_{1},\nu_{2},\ldots,\nu_{k}\right)$ である。

PCA 基底に基づくデータの再構成は次式で与えられる

$$
\mathbf{x} = \mathbf{Wy} + \mathbf{\mu}
$$

固有顔法は以下の方法で顔認識を行います。

* すべての学習サンプルを PCA 部分空間に射影する
* クエリ画像を PCA 部分空間に射影すう
* 射影された学習画像と射影されたクエリ画像の間の最近傍を見つける

しかし，まだ解決しなければならない問題が 1 つ残っています。
$100\times100$ 画素の画像が $400$ 枚与えられたとします。
主成分分析では，共分散行列 $\mathbf{S}=\mathbf{XX}^{\top}$ を解きます。
この例では $\text{size}(\mathbf{X})=10000\times400$ となります。
$10000\times10000$ 行列の場合，およそ 0.8 GB になってしまいます。
この問題を解決することは不可能なので，あるトリックを適用する必要があります。
線形代数の授業で $M>N$ の $M\times M$ 行列は $N-1$ 個の非ゼロの固有値しか持たないことを知っているでしょう。
そこで，サイズが $M\times N$ の固有値分解 $S=X^{t}X$ を代わりに取ることができます。

<!-- The Eigenfaces method then performs face recognition by:

* Projecting all training samples into the PCA subspace.
* Projecting the query image into the PCA subspace.
* Finding the nearest neighbor between the projected training images and the projected query image.

Still there's one problem left to solve. 
Imagine we are given 400 images sized 100x100 pixel. 
The Principal Component Analysis solves the covariance matrix $\mathbf{S}=\mathbf{XX}^{\top}$, where $\text{size}(\mathbf{X})=10000\times400$ in our example. 
You would end up with a 10000x10000 matrixx, roughly 0.8GB. 
Solving this problem isn't feasible, so we'll need to apply a trick. 
From your linear algebra lessons you know that a MxM matrix with M>N can only have N-1 non-zero eigenvalues. 
So it's possible to take the eigenvalue decomposition S=X^tX of size MxN instead:
-->

$$
\mathbf{X}^{\top}\mathbf{X}\mathbf{\nu}_{i}=\lambda_{i}\mathbf{\nu}_ {i}
$$

元の行列 $S=XX^{\top}$ の固有ベクトルはデータ行列の積

$$
\mathbf{XX}^{\top}\left(\mathbf{X\nu}_{i}\right)=\lambda_{i}\left(\mathbf{X\nu}_ {i}\right)
$$

結果として得られる固有ベクトルは直交していますが、直交する固有ベクトルを得るためには、単位長さに正規化する必要があります。
これを出版物にしたくないので、方程式の導出と証明は[62]を見てください。
<!-- The resulting eigenvectors are orthogonal, to get orthonormal eigenvectors they need to be normalized to unit length. 
I don't want to turn this into a publication, so please look into [62] for the derivation and proof of the equations.
 -->

* [62] Richard O Duda, Peter E Hart, and David G Stork. Pattern classification. John Wiley & Sons, 2012.


## フィッシャー顔
<!-- ## Fisherfaces -->

鼓友顔法の中核である主成分分析（PCA）は、データの全分散を最大化する特徴の線形結合を見つけます。
これはデータを表現する強力な方法であることは間違いありませんが、クラスを考慮していないため、成分を捨てる際に多くの識別情報が失われる可能性があります。
データの分散が外部から発生している状況を想像してみてください。
それを光とします。
PCA で同定された成分は， 必ずしも識別情報を全く含んでいないので， 投影されたサンプルは一緒に塗りつぶされ，分類は不可能になります (例として http://www.bytefish.de/wiki/pca_lda_with_gnu_octave を参照)。
線形判別分析は， クラス固有の次元削減を行うもので， 偉大な統計学者フィッシャー（Sir R. A. Fisher）によって考案されました。
フィッシャーは 1936 年に発表した論文 The use of multiple measurements in taxonomic problems （分類学上の問題における複数の測定値の使用）の中で,， 花の分類にこの手法を用いることに成功しました [77]。
線形判別分析は， クラス間で最もよく分離する特徴の組み合わせを見つけるために， 全体の散らばりを最大化する代わりに， クラス間の散らばりとクラス内の散らばりの比率を最大化します。
その考え方は簡単で， 同じクラスはしっかりとクラスター化し， 異なるクラスは低次元の表現の中でできる限り離れているべきだというものです。
このことは， Belhumeur, Hespanha and Kriegman も認識しており [18] では顔認識に判別分析を適用しています。
<!--
The Principal Component Analysis (PCA), which is the core of the Eigenfaces method, finds a linear combination of features that maximizes the total variance in data. 
While this is clearly a powerful way to represent data, it doesn't consider any classes and so a lot of discriminative information may be lost when throwing components away. 
Imagine a situation where the variance in your data is generated by an external source, let it be the light. 
The components identified by a PCA do not necessarily contain any discriminative information at all, so the projected samples are smeared together and a classification becomes impossible (see http://www.bytefish.de/wiki/pca_lda_with_gnu_octave for an example). 
The Linear Discriminant Analysis performs a class-specific dimensionality reduction and was invented by the great statistician Sir R. A. Fisher. 
He successfully used it for classifying flowers in his 1936 paper The use of multiple measurements in taxonomic problems [77]. 
In order to find the combination of features that separates best between classes the Linear Discriminant Analysis maximizes the ratio of between-classes to within-classes scatter, instead of maximizing the overall scatter. 
The idea is simple: same classes should cluster tightly together, while different classes are as far away as possible from each other in the lower-dimensional representation. 
This was also recognized by Belhumeur, Hespanha and Kriegman and so they applied a Discriminant Analysis to face recognition in [18].
-->

* [10] Peter N. Belhumeur, João P Hespanha, and David Kriegman. Eigenfaces vs. fisherfaces: Recognition using class specific linear projection. Pattern Analysis and Machine Intelligence, IEEE Transactions on, 19(7):711–720, 1997.
* [77] Ronald A Fisher. The use of multiple measurements in taxonomic problems. Annals of eugenics, 7(2):179–188, 1936.


## フィッシャー顔法のアルゴリズムの説明
<!-- ### Algorithmic Description of Fisherfaces method -->

クラスからサンプルを抽出したランダムなベクトルを指定します。
<!-- Let be a random vector with samples drawn from classes: -->

$$
\mathbf{X} = \left\{X_{1},X_{2},\ldots,X_{c}\right\}
$$

$$
\mathbf{X}_i = \left\{x_{1},x_{2},\ldots,x_{n}\right\}
$$

分散行列 $S_{B}$ と $S_{W}$ とは以下のように計算されます:

$$
\begin{aligned}
S_{B} &= \sum_{i=1}^{c} N_{i}\left(\mu_{i}-\mu\right)\left(\mu_{i}-\mu\right)^{\top}\\
S_{W} &= \sum_{i=1}^{c}\sum_{x_{j}\in X_{i}}\left(x_{j}-\mu_{j}\right)\left(x_{j}-\mu_{j}\right)^{\top}
\end{aligned}
$$

ここで $\mu$ は全平均を表します:

$$
\mu=\frac{1}{N}\sum_{i=1}^{N}x_{i}.
$$

そして $\mu_i$ は群平均 $\in\left(1,\ldots,c\right)$ を表します。

$$
\mu_{i}=\frac{1}{\left|X_{i}\right|}\sum_{x_{j}\in X_{i}} x_{j}.
$$

Fisher の古典的なアルゴリズムでは，クラスの分離可能性の基準を最大化する射影を探すことになります。
<!-- Fisher's classic algorithm now looks for a projection , that maximizes the class separability criterion: -->

$$
W_{opt}=\arg\max_{W}\frac{\left|W^{\top}S_{B}W\right|}{\left|W^{\top}S_{W}W\right|}
$$

[18] によれば，この最適化問題の解は，一般固有値問題を解くことで与えられます。
<!-- Following[18], a solution for this optimization problem is given by solving the General Eigenvalue Problem: -->

$$
\begin{aligned}
S_{B}\nu_{i} &=\lambda_{i}S_{w}\nu_{i}\\
S_{W}^{-1}S_{B}\nu_{i} &= \lambda_{i}\nu_{i}
\end{aligned}
$$

問題が 1 つ残っています。
$S_w$ のランクは， サンプル数 N, クラス数 c の場合，最大でも (N-c) です。
パターン認識の問題では，サンプル数 N は，ほとんどの場合，入力データの次元 (画素数) よりも小さいので，散布行列 $S_w$ は特異となります ([200]参照)。
[18]では，データに対して主成分分析を行い，サンプルを (N-c) 次元の空間に投影することで，この問題を解決しました。
その後， $S_w$ が特異点でなくなったので，縮小されたデータに対して線形判別分析を行いました。
最適化問題は次のように書き換えられます。
<!-- There's one problem left to solve: 
The rank of S_w is at most (N-C), with N samples and c classes. 
In pattern recognition problems the number of samples N is almost always samller than the dimension of the input data (the number of pixels), so the scatter matrix S_w becomes singular (see [200]). In [18] this was solved by performing a Principal Component Analysis on the data and projecting the samples into the (N-c) -dimensional space. 
A Linear Discriminant Analysis was then performed on the reduced data, because S_w isn't singular anymore.
The optimization problem can then be rewritten as:
-->

$$
\begin{aligned}
W_{pca} &= \arg\max_{W} \left|W^{\top}S_{T}W\right|\\
\end{aligned}
$$


$$
\begin{aligned}
W_{fld} &= \arg\max_{W}\frac{\left|W^{\top}W_{pca}^{\top}S_{B}W_{pca}W\right|}{\left|W^{\top}W_{pca}^{\top}S_{W}W_{pca}W\right|}\\
\end{aligned}
$$

そして，サンプルを（c-1）次元の空間に投影する変換行列 W は、次のように与えられます:
<!-- The transformation matrix W, that projects a sample into the (c-1)-dimensional space is then given by: -->

$$
W=W_{fld}^{\top}W_{pca}^{\top}
$$

* [18] Peter N. Belhumeur, João P Hespanha, and David Kriegman. Eigenfaces vs. fisherfaces: Recognition using class specific linear projection. Pattern Analysis and Machine Intelligence, IEEE Transactions on, 19(7):711–720, 1997.
* [200] Sarunas J Raudys and Anil K. Jain. Small sample size effects in statistical pattern recognition: Recommendations for practitioners. IEEE Transactions on pattern analysis and machine intelligence, 13(3):252–264, 1991.


# 機械学習に現れるベイズ推論

確率論の根底には 2 つの簡単な規則があります。

* **和の規則**: <!-- There are two simple rules that underlie probability theory: the sum rule: -->
$\displaystyle P(x)=\sum_ {y\in Y} P(x,y)$ 
* **積の規則**:  <!-- and the product rule: -->
$\displaystyle P(x,y) = P(x) P(y\mid x) $


ここで　$x$ と $y$ とは，観測された量または不確実な量に対応し，それぞれいくつかの集合 $X$ と $Y$ の中で値をとります。
例えば $x$ と $y$ は，それぞれケンブリッジとロンドンの天気に関連しており，どちらも $X= Y=$ {雨，曇り，晴れ} という集合の中で値をとります。
$P(x)$ は $x$ の確率に相当し，特定の値が観測される頻度を表す文，またはその値に関する主観的な信念のいずれかになります。
$P(x,y)$ は，$x$ と $y$ を観測する同時確率で $P(y\mid x)$ は $x$ の値を観測したことを条件に $y$ を観測する確率です。
和の規則では $x$ の周辺値は $y$ に対する結合を総和（連続変数の場合は積分）することで得られるとしています。
積の法則とは，周辺と条件付きの積として同時分布を分解できるというものです。
ベイズ則は この 2 つの法則の従属関係にあります。
<!-- Here $x$ and $y$ correspond to observed or uncertain quantities, taking values in some sets $X$ and $Y$, 
respectively. 
For example, $x$ and $y$  might relate to the weather in Cambridge and London, respectively, both taking value
s in the set $X = Y =$ {rainy,cloudy,sunny}. 
$P(x)$ corresponds to the probability of $x$, which can be either a statement about the frequency of observing
 a particular value, or a subjective belief about it. 
$P(x,y)$ is the joint probability of observing $x$ and $y$, and $P(y|x)$ is the probability of $y$ conditioned
 on observing the value of $x$. 
The sum rule states that the marginal of $x$ is obtained by summing (or integrating for continuous variables) 
the joint over $y$. 
The product rule states that the joint can be decomposed as the product of the marginal and the conditional. 
Bayes rule is a corollary of these two rules:
-->
$$
P(y\mid x)=\frac{P(x\mid y)P(y)}{P(x)}=\frac{P(x\mid y)P(y)}{\sum_{y\in Y}P(x,y)}
$$

確率論を機械学習に応用するには、上記の記号を置き換えることで $x$ を $\mathcal{D}$ に置き換えて観測データを表し，$y$ を $\theta$ に置き換えてモデルの未知のパラメータを表し，すべての項を $m$ (検討している確率論的モデルのクラス) で条件付けすることができます。
学習については， 次のようになります:
<!-- We can apply probability theory to machine learning by replacing the symbols above: we replace $x$ by $D$
 to denote the observed data, we replace $y$ by $\theta$ to denote the unknown parameters of a model, and we c
ondition all terms on $m$, the class of probabilistic models we are considering. 
For learning, we thus get:
-->

$$
P(\theta\mid \mathcal{D},m)=\frac{P(\mathcal{D}\mid \theta,m) P(\theta\mid m)}{P(\mathcal{D}\mid m)},
$$

ここで $P(\mathcal{D}\mid\theta,m)$ はモデル $m$ におけるパラメータ $\theta$ の尤度， $P(\theta\mid m)$ は $\theta$ の事前確率，$P(\theta\mid \mathcal{D}, m)$ はデータ $\mathcal{D}$ が与えられたときの $\theta$ の事後確率
です。
<!-- where $P(D\vert\theta,m)$ is the likelihood of parameters $\theta$ in model $m$, $P(\theta\vert m)$ is th
e prior probability of $\theta$ and $P(\theta\vert D, m)$ is the posterior of $\theta$ given data $D$.
-->

例えば， データ $\mathcal{D}$ は，ケンブリッジとロンドンの天気を 1 時間ごとに観測した時系列データであり，モデルは，時間と空間の相関関係をモデル化したパラメータ $\theta$ を用いて， 連続した時間における両地点の共同の天気パターンを捉えようとするものである。
学習とは，データ $\mathcal{D}$ を通じて，パラメータ $P(\theta\mid m)$ に関する事前の知識や仮定を， パラメータに関する事後の知識 $P(\theta\mid\mathcal{D},m)$ に変換することです。
この事後知識は，将来のデータに使用される事前知識となります。
学習したモデルを使って，新しい未見のテストデータ $D_\text{test}$ を予測・予想するには，和と積の法則を適用するだけで予測値が得られます。
<!-- For example, the data $D$ might be a time series of hourly observations of the weather in Cambridge and L
ondon, and the model might attempt to capture the joint weather patterns at both locations over successive hou
rs, with parameters $\theta$ modelling correlations over time and space. 
Learning is the transformation of prior knowledge or assumptions about the parameters $P(\theta\vert m)$, thro
ugh the data $D$, into posterior knowledge about the parameters, $P(\theta\vert D,m)$. 
This posterior is now the prior to be used for future data. 
A learned model can be used to predict or forecast new unseen test data, $D_\text{test}$, by simply applying t
he sum and product rule to get the prediction:
-->

$$
P(\mathcal{D}_{\text{test}}\vert \mathcal{D},m) = \int P(\mathcal{D}_{\text{test}}\vert \theta, \mathcal{D}, m
) P(\theta\vert \mathcal{D},m)\,d\theta
$$

最後に $m$ のレベルでベイズ則を適用することで，異なるモデルを比較することができます。
<!-- Finally, different models can be compared by applying Bayes rule at the level of m:-->

$$
\begin{aligned}
P(m\mid \mathcal{D}) &= \frac{P(\mathcal{D}\mid m)P(m)}{P(\mathcal{D})}\\
P(\mathcal{D}\mid m) &= \int P(\mathcal{D}\mid \theta,m) P(\theta\mid m)\,d\theta
\end{aligned}
$$

$P(\mathcal{D}\mid m)$ は，周辺尤度またはモデルの証拠であり，ベイズ流の **オッカムの剃刀** として知られる，よ
り単純なモデルへの優先順位を実装しています。
<!-- The term $P(D\mid m)$ is the marginal likelihood or model evidence, and implements a preference for simpl
er models known as Bayesian Ockham’s razor. -->

## カルバック・ライブラー・ダイバージェンスについて

カルバック・ライブラーダイバージェンスは 2 つの確率密度 $p$, $q$ の乖離を表す指標である。
教科書によっては，カルバック・ライブラーの偽距離と記載されている場合もある。
また，表記として $KL\left(p\vert\vert q\right)$ あるいは $D_{KL}\left(p\vert\vert q\right)$ と表記する文献も存在する。

カルバック・ライブラーダイバージェンスは，非対称であることに注意が必要である。
すなわち $KL[p\vert\vert q] \ne KL[q\vert\vert p]$ である。
カルバック・ライブラーのダイバージェンスの非対称性は，定義を見れば納得できる。

$$
KL\left(p\vert\vert q\right)= - \int p \log\left(\frac{p}{q}\right)\;dp = -\left[\int p\log p\;dp + \int p\log q\;dp\right]
$$

上式最右辺，第一項は，エントロピーの定義式であり，分布 $p$ の負の対数の平均である。
一方，上式最右辺第二項は，分布 $q$ を，$q$ の確率密度を使って平均を求めている。
このため，$\log q$ に大きな値を取る領域や部分があっても，$p$ が 0 に近ければ，両分布の乖離度合いとして計算されないことを意味している。

<!-- KL ダイバージェンスは通常の距離と異なり非対称で，どちらの分布を基準に考えるかによって値が異なります。
すなわち $\KL{P}{Q}\ne\KL{Q}{P}$ です。-->

KL ダイバージェンスの非対称性を説明する図を下に示します。

青い曲線は真の事後分布とします，例えば双峰性の分布であるとします。
緑の分布は最適化を介して青い密度に適合させる変分近似による分布を表すものとします。
これを **フォワード KL** と呼びます。
図左のように，双峰性の真の分布を単峰性の分布で近似することを考えます。
このとき，一方の峰に当てはまるように調整すると，もう一方の峰の値についての当てはまりが悪くなり結果として右下図のような裾野の広い分布を得ることになります。

反対に，緑の単峰性の分布を青の双峰性の分布で近似しようとする **リバースKL** を考えます。
このとき基準となる真の分布である単峰性の分布の確率密度がほとんど 0 の領域では，推定する分布がどのような値を取ろうとも KL ダイバージェンスの値に影響を与えないため，いずれか一方の峰が真の分布と重なるような値を得ることになります。

<center>
<img src="/assets/forward-KL.png" width="48%">
<img src="/assets/reverse-KL.png" width="48%"><br/>

左: フォワード KL, 右： リバース KL
KL ダイバージェンスの非対称性 
[A Beginner's Guide to Variational Methods: Mean-Field Approximation}]((https://blog.evjang.com/2016/08/variational-bayes.html) より
</center>

大抵の場合，現実は複雑(怪奇) で（図中の青色で描かれた分布），モデル (図中の緑で描かれた分布) は素朴で単純です。
図左は，現実が双峰性分布でモデルが単峰性分布のときに，現実(青色)からみたモデル(緑色)の乖離ですから，
現実（青）の存在する領域に，モデルが存在しない状況 （左上図）では KL ダイバージェンスは大きく，したがって，両分布の乖離は大きくなります。
したがって，現実を最もよく推定することを試みた場合 (左下図) モデル（の推定）は，裾野の広い分布と推定することになります。

一方，単峰性分布モデル(緑)から，双峰性分布である現実（青）を見た場合，モデルと現実があっていない状況(右上図)になります。
この状態で，モデルから，無理やり現実を推定しようとする リバース KL (右下図) では，現実を最もよく推定すると，
双峰性分布の，どちらかのピークと重なる形で，モデル（緑色）は，現実 （青色）を推定してしまいます。

現実の分布からみたモデルの分布の KL ダイバージェンスと，モデルからみた現実の KL ダイバージェンスが異なることは，上記の説明を理解することが肝要です。


