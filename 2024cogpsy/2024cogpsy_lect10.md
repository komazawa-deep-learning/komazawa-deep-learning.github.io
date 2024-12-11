---
title: "第10回 2024年度開講 駒澤大学 認知心理学研究"
author: "浅川 伸一"
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="right">
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 29/Nov/2024<br/>
Appache 2.0 license<br/>
</div>

$$
\newcommand{\of}[1]{\left(#1\right)}
\newcommand{\Of}[1]{\left[#1\right]}
\newcommand{\KL}[2]{\operatorname{KL}\left(\left.{#1}\right\|{#2}\right)}
\newcommand{\given}[1]{\left|{#1}\right.}
\newcommand{\mb}[1]{\mathbf{#1}}
$$

# 先週の復習

* 畳み込みニューラルネットワーク，ResNet によるスキップ結合，
* 畳み込みニューラルネットワークについては，カーネルサイズ，ストライド，パディング，ダイアレーション(未言及)，
* HMax 最大値プーリング，最大値プーリングが行われなくなった理由としては，画像切り分けの際に不利になるからという理由が考えられる。
* ドロップアウト (未言及)
* バッチ正規化 (未言及)
* データ拡張 (未言及)

# 本日のキーワード

* 転移学習 (transfer learning)，微調整 (fine tuning), 蒸留 (distillation, [Hinton+2015](https://arXiv.org/abs/1503.02531/){:target="_blank"}), メタ学習 [Finn+2020 MAML: Model Agnositic Meta Learning](https://arXiv.org/abs/1703.03400){:target="_blank"}
* [U-Net: Ronneberger+(2015)](https://arXiv.org/abs/1505.04597/){:target="_blank"}
* [DETR Carion+2020](https://arXiv.org/abs/2005.12872/){:target="_blank"}
* [ViT: Vision Transformer Dosovitskiy+2020](https://arXiv.org/abs/2010.11929/){:target="_blank"}
* [PANet: Path Aggregation Network for Instance Segmentation:PANet](https://arXiv.org/abs/1803.01534){:target="_blank"}

<div class="figcenter">
<img src="/2024assets/2018Liu_PANet_adaptive_feature_pooling.svg">
</div><div class="figcaption" style="width:33%;">
Liu+(2018) PANet の適応的特徴プーリング の概念図
</div>

<div class="figcenter">
<!-- <img src="/2022assets/2020Carion_DETR_fig2ja.png" style="width:66%;"> -->
<img src="/2022assets/2020Carion_DETR_fig2ja.svg" style="width:66%;">
<!-- <img src="/2022assets/2020Carion_DETR_fig2.svg" style="width:66%;"> -->
</div><div class="figcaption">
DETR の概略 Carion+(2020) Fig. 2 を改変
</div>

## 実習ファイル

- [ResNet, LeNet 実習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_1129ResNet_LeNet_with_Karapetian2023.ipynb){:target="_blank"}
- [DETR を用いた領域切り出し  <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_0625DETR_demo.ipynb){:target="_blank"}
- [フィラデルフィア絵画命名検査課題 PNT を転移学習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_0618pnt_transfer_learning.ipynb){:target="_blank"}
- [データ拡張 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2021notebooks/2021_0617plot_transforms_demo.ipynb){:target="_blank"}
- [CAM 実習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_0618CAM_demo.ipynb){:target="_blank"}
- [EfficientNet のパラメータ実習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/drive/1QpKBHsBR5yvEOz2M-pKCUpliDh1XXplS){:target="_blank"}
<!-- - [各画像の画面表示時に日本語キャプションを付与する準備 <img src="https://komazawa-deep-learning.github.io/assets/colab_icon.svg">](https://colab.research.google.com/github/project-ccap/ccap/blob/master/notebooks/2020importing_ccap_from_GitHub.ipynb){:target="_blank"} -->

* [ソフトマックス関数解題 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_1107softmax.ipynb){:target="_blank"}
また，ソフトマックス関数は，エネルギー関数とみなすことも可能である。

* [ニューラルネットワークモデルの定義 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_1028komazawa_neural_networks_primer.ipynb){:target="_blank"}
* [3 層パーセプトロンと確率的勾配降下法のデモ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/2015corona/blob/master/2021notebooks/2021_0521mlp_Adam_SGD.ipynb){:target="_blank"}

<!-- * [ccap 資料初心者のためのニューラルネットワーク <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/project-ccap/project-ccap.github.io/blob/master/2022notebooks/2022_0418ccap_neural_networks_for_primer.ipynb){:target="_blank"}
* [画像認識 PyTorch の基礎編 AlexNet <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2020_0515komazawa_step_by_step_CNN_Pytorch.ipynb){:target="_blank"} -->

<!-- * [[Karapetian+(2023)](https://direct.mit.edu/jocn/article/35/11/1879/117201/Empirically-Identifying-and-Computationally) <img src="/assets/colab_icon.svg"> ](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_115Karapetian_demo.ipynb) -->
* [ResNet 実習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_0603ResNet_with_Olivetti_faces_.ipynb){:target="_blank"}

<!-- * [ResNet 実習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_0603ResNet_with_Olivetti_faces_.ipynb) -->
<!-- * [セグメンテーション実習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_0603Image_segmentation_demo.ipynb){:target="_blank"}
* [DETR  <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_0625DETR_demo.ipynb)
* [実装 Bottom-up Top-down model <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_0105royabel_BU_TD_multi_mnist.ipynb){:target="_blank"}-->

* [はじめての colab による画像認識 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021komazawa_cogsy000_CNN_demo.ipynb){:target="_blank"}
* [画像認識 PyTorch の基礎編  <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2020_0515komazawa_step_by_step_CNN_Pytorch.ipynb){:target="_blank"}
* [畳み込み演算の実習と DOG 関数 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_1024convolution_exercise.ipynb){:target="_blank"}
* [CNN 畳み込み層の可視化 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_1024CNN_layer_visualization.ipynb){:target="_blank"}
* [3 層パーセプトロンと確率的勾配降下法のデモ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/2015corona/blob/master/2021notebooks/2021_0521mlp_Adam_SGD.ipynb){:target="_blank"}
* [実習 MLP Adam SGD <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0521mlp_Adam_SGD.ipynb){:target="_blank"}
* [実習 LeNet PyTorch 版 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0528LeNet_pytorch.ipynb){:target="_blank"}
* [実習 3 つの MNIST <img src='/assets/colab_icon.svg'>](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0514komazawa_3mnists.ipynb){:target="_blank"}
* [実習 いくつかの画像フィルタ 特徴点検出アルゴリズム <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2020Sight_visit_feature_extractions_demo.ipynb){:target="_blank"}
* [実習 DOG などのフィルタと Harr 特徴による顔検出 a.k.a ビオラ＝ジョーンズ アルゴリズム <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0528edge_and_face_detection_algorithm_not_cnn.ipynb){:target="_blank"}



## [U-Net: Ronneberger+(2015)](https://arXiv.org/abs/1505.04597/)

Project page: [https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/](https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/){:target="_blank"}
画像分割の SOTA (State of the arts)

<div class="figcenter">
<img src="/assets/2015Ronneberger_U-Net_Fig1_ja.svg" style="width:66%"><br/>
<div class="figcaption">
Ronnenberger+(2015) Fig. 1
</div>
<img src="/2024assets/2018Zhou_UNet++_slide.svg" style="width:66%"><br/>
<div class="figcaption">

[Zhou+(2018)](https://arXiv.org/abs/1807.10165/){:target="_blank"} Fig. 2
</div>
</div>


# 転移学習の定義

* 転移学習には，領域 (domain) と課題  (task) という概念がある。
* 領域は，特徴空間 $\mathcal{X}$ と特徴空間上の周辺確率分布 $P(X)$ からなり，$X = {x_{1}, \cdots, x_{n}} \in \mathcal{X}$ である。
* 文書分類課題では $\mathcal{X}$ は全ての文書表現の空間，$x_{i}$ はある文書に対応するベクトル，$X$ は学習に用いた文書サンプルなどとなる。
* 課題 $\mathcal{D} = {\mathcal{X},P(X)}$ は，ラベル空間 $\mathcal{Y}$ と条件付き確率分布 $P(Y\vert X)$ からなり，$x_{i}\in X$, $y_{i}\in Y$ の組からなる学習データを用いて学習される。

<!-- Given a domain, $\mathcal{D} = \left\{\mathcal{X},P(X)\right\}$, a task $\mathcal{T}$ consists of a label space $\mathcal{Y}$ and a conditional probability distribution $P(Y\vert X)$ that is typically learned from the training data consisting of pairs $x_{i}\in X$ and $y_{i}\in \mathcal{Y}$.
In our document classification example, $\mathcal{Y}$ is the set of all labels, i.e. *True*, *False* and $y_i$ is either *True* or *False*.-->

ソース領域 $\mathcal{D}_ {S}$ とそれに対応するソース課題 $\mathcal{T}_ {S}$，およびターゲット領域 $\mathcal{D}_ {T}$ とターゲット課題 $\mathcal{T}_ {T}$ が与えられたとき，
ソース領域 $\mathcal{D}_ {S}$ とターゲット課題 $\mathcal{T}_ {S}$ は，ターゲット課題とターゲット領域 $\mathcal{T}_ {T}$ に対応するソース課題とターゲット課題の両方を含む。
ここで，転移学習の目的は $\mathcal{D}_ {T}$ の条件付き確率分布 $P(Y_{T}\vert X_{T})$ を学習することである。
ここで $\mathcal{D}_ {S}$ と $\mathcal{T}_ {S}$ から得られる情報は $\mathcal{D}_ {S}\neq\mathcal{D}_ {T}$ または $\mathcal{T}_ {S}\neq \mathcal{T}_ {T}$ の場合である。
多くの場合，ラベル付けされた対象例は，ラベル付けされた元例より指数関数的に少ない限られた数しか利用できないと仮定する。
<!-- Given a source domain $\mathcal{D}_ {S}$, a corresponding source task $\mathcal{T}_ {S}$, as well as a target domain $\mathcal{D}_ {T}$ and a target task $\mathcal{T}_ {T}$, the objective of transfer learning now is to enable us to learn the target conditional probability distribution $P(Y_{T}\vert X_{T})$ in $\mathcal{D}_ {T}$ with the information gained from $\mathcal{D}_ {S}$ and $\mathcal{T}_ {S}$ where $\mathcal{D}_ {S}\neq \mathcal{D}_ {T}$ or $\mathcal{T}_ {S} \neq \mathcal{T}_ {T}$.
In most cases, a limited number of labeled target examples, which is exponentially smaller than the number of labeled source examples are assumed to be available. -->

<!-- 領域 $\mathcal{D}$ と課題 $\mathcal{T}$ は共にタプルとして定義されるため，これらの不等式は 4 つの転移学習シナリオを生じさせ，以下で議論する。 -->

1. $\mathcal{X}_ {S}\neq\mathcal{X}_ {T}$.
例えば，文書が 2 つの異なる言語で書かれているなど，ソース領域とターゲット領域の特徴空間が異なる場合。
自然言語処理の文脈では，一般に異言語間適応と呼ばれる。
<!-- The feature spaces of the source and target domain are different, e.g. the documents are written in two different languages.
In the context of natural language processing, this is generally referred to as cross-lingual adaptation. -->
2. $P(X_{S})\neq P(X_{T})$.
原文領域と訳文領域の周辺確率分布が異なる場合，例えば，異なる話題について議論している文書がある場合，原文領域と訳文領域の周辺確率分布は異なる。
このようなシナリオは一般にドメイン適応と呼ばれる。
<!-- The marginal probability distributions of source and target domain are different, e.g. the documents discuss different topics.
This scenario is generally known as domain adaptation. -->
3. $\mathcal{Y}_ {S}\neq\mathcal{Y}_ {T}$.
2 つの課題のラベル空間が異なる場合。例えば，ターゲット課題では文書に異なるラベルを割り当てる必要がある。
実際には 2 つの異なる課題が異なるラベル空間を持ちながら，全く同じ条件付き確率分布を持つことは極めて稀であるため，これは通常 4 で発生する。
<!-- The label spaces between the two tasks are different, e.g. documents need to be assigned different labels in the target task.
In practice, this scenario usually occurs with scenario 4, as it is extremely rare for two different tasks to have different label spaces, but exactly the same conditional probability distributions. -->
4. $P(Y_{S}\vert X_{S})\neq P(Y_{T}\vert X_{T})$.
原文と訳文の条件付き確率分布が異なる，例えば，原文と訳文がクラスに関してアンバランスである場合。
このようなシナリオは実際にはよくあることである<!-- ，オーバーサンプリング，アンダーサンプリング，あるいは SMOTE [7] などのアプローチが広く使われている。 -->

## 転移学習 transfer learning

**転移学習** transfer learning は機械学習分野のみならず，ロボット工学や実応用の分野でも応用が進められている。
シミュレーションと現実との間隙をどのように埋めるのかという大きな問題に関連する。
一方で，転移学習と **ファインチューニング** や **領域適応** domain adaptation の区別がなされる。

転移学習とは 課題 A を用いて訓練したモデルに対して，別の課題 B に適用することを指す。
DNN では転移学習は頻用される。
イメージネットで画像分類を学習したネットワークに対して，例えば顔認識を学習させるような場合である。

PyTorch のチュートリアルなどでは，学習済のネットワークに対して，最終層 (全結合層) を入れ替えて別の課題を訓練することを転移学習と呼ぶ。
このとき，最終直下層と出力層との結合を学習させ，その他の下位層の結合は固定し，訓練しない。
一方で，下位層まで含めて全結合を訓練させる場合を，**微調整 (fine tuning ファインチューニング)** と呼び，区別している。

<div align="center" style="width:99%">
<img src="/assets/2019Ruder_hard_parameter_sharing_p48.jpg" style="width:44%">
<img src="/assets/2019Ruder_soft_parameter_sharing_p49.jpg" style="width:44%"><br/>
左: ハードパラメータ共有: 転移学習,  右: ソフトパラメータ共有: ファインチューニング
</div>

<div align="center" style="width:29%">
<img src="/assets/2017Li_Deeper_Broader_fig1ja.svg" style="width:84%"><br/>
</div>

## ViT Dosovitskiy+(2020)
[AN IMAGE IS WORTH 16X16 WORDS: TRANSFORMERS FOR IMAGE RECOGNITION AT SCALE](https://arxiv.org/abs/2010.11929/){:target="_blank"}

### 3. 方法<!--3 METHOD-->

モデル設計において，我々はオリジナルのTransformer（Vaswani+2017）に可能な限り忠実に従う。
この意図的にシンプルなセットアップの利点は，スケーラブルなNLP Transformerアーキテクチャとその効率的な実装が，ほぼそのまま使えることである。
<!-- In model design we follow the original Transformer (Vaswani+2017) as closely as possible.
An advantage of this intentionally simple setup is that scalable NLP Transformer architectures – and their efficient implementations – can be used almost out of the box. -->

#### VISION TRANSFORMER (VIT)

モデルの概要を下図 に示す。
標準的な Transformer はトークン埋込みの 1 次元系列を入力として受け取る。
2 次元画像を扱うために，画像 $x\in\mathcal{R}^{H\times W\times C}$ を平坦化された 2 次元パッチの系列 $x_{p}$ に再形成する。
(H,W) は原画像の解像度，C はチャンネル数，(P,P) は各画像パッチの解像度，$N=HW/P^{2}$ は結果のパッチ数であり，これは Transformer の有効入力系列長でもある。
Transformer は全ての層で一定の潜在ベクトルサイズ D を用いるので，パッチを平坦化し，訓練可能な線形射影（式 1）を用いて D 次元に写像する。
この射影の出力をパッチ埋め込みと呼ぶ。
<!-- An overview of the model is depicted in Figure 1.
The standard Transformer receives as input a 1D sequence of token embeddings.
To handle 2D images, we reshape the image $x\in\mathcal{R}^{H\times W\times C}$ into a sequence of flattened 2D patches $x_{p}\in\mathcal{R}^{N\times(P^{2}\cdot C)}$, where (H,W) is the resolution of the original
image, C is the number of channels, (P,P) is the resolution of each image patch, and $N=HW/P^{2}$ is the resulting number of patches, which also serves as the effective input sequence length for the Transformer.
The Transformer uses constant latent vector size D through all of its layers, so we flatten the patches and map to D dimensions with a trainable linear projection (Eq. 1).
We refer to the output of this projection as the patch embeddings. -->

<div class="figcenter">
<img src="/2024assets/2020Dosovitskiy_ViT_fig1.svg" style="width:66%;">
</div>
<div class="figcaption" style="width:77%;">

**図 ViT モデル概要**<br/>
画像を固定サイズのパッチに分割し，それぞれを線形に埋め込み，位置埋め込みを追加し，得られたベクトル列を標準的な Transformer 符号化器に与える。
分類を行うために，学習可能な 「分類トークン 」を系列に追加するという標準的なアプローチを用いる。
Transformer 符号化器の図は，Vaswani+(2017) に触発された。
<!-- Figure 1: Model overview.
We split an image into fixed-size patches, linearly embed each of them, add position embeddings, and feed the resulting sequence of vectors to a standard Transformer encoder.
In order to perform classification, we use the standard approach of adding an extra learnable “classification token” to the sequence.
The illustration of the Transformer encoder was inspired by Vaswani+(2017). -->
</div>

BERT の `[class]` トークンと同様に，学習可能な埋め込みを埋め込みパッチのシーケンス($z_0^0=x_{text{class}}$) の前に付加し，Transformer エンコーダの出力 ($z_{L}^{0}$) の状態が画像表現yとなる（式 4）。
事前学習時と微調整時の両方で，分類ヘッドが $z^{0}_{L}$ に取り付けられる。
分類ヘッドは，事前学習時には 1 つの隠れ層を持つ MLP によって実装され，微調整時には 1 つの線形層によって実装される。
<!-- Similar to BERT’s `[class]` token, we prepend a learnable embedding to the sequence of embedded patches ($z_0^0=x_{\text{class}}$), whose state at the output of the Transformer encoder ($z_{L}^{0}$) serves as the
image representation y (Eq. 4).
Both during pre-training and fine-tuning, a classification head is attached to $z^{0}_{L}$.
The classification head is implemented by a MLP with one hidden layer at pre-training time and by a single linear layer at fine-tuning time. -->

位置埋め込みは位置情報を保持するためにパッチ埋め込みに追加される。
我々は標準的な学習可能な 1 次元の位置埋め込みを使用。
結果として得られる埋め込みベクトルの系列スは符号化器の入力となる。
Transformer 符号化器 (Vaswani+2017) は，多頭自己注意 (MSA) と MLP ブロックの交互の層で構成される)。
各ブロックの前には層正規化 (LN) が適用され，各ブロックの後には残差接続が適用される (Wang+2019, Baevski&Auli2019)。
MLP には GELU 非線形性を持つ 2 つの層が含まれる。
<!-- Position embeddings are added to the patch embeddings to retain positional information.
We use standard learnable 1D position embeddings, since we have not observed significant performance gains from using more advanced 2D-aware position embeddings (Appendix D.3).
The resulting sequence of embedding vectors serves as input to the encoder.
The Transformer encoder (Vaswani+2017) consists of alternating layers of multiheaded selfattention (MSA, see Appendix A) and MLP blocks (Eq. 2, 3).
Layer-norm (LN) is applied before every block, and residual connections after every block (Wang+2019, Baevski&Auli2019).
The MLP contains two layers with a GELU non-linearity. -->

**モデルの変種:**<!-- **Model Variants.**-->
表 1 にまとめたように，BERT（Devlin+2019）で使用されたものを ViT 構成のベースとしている。
Base モデルと Large モデルは BERT からそのまま採用し，より大きなHuge モデルを追加した。
以下では，モデルサイズと入力パッチサイズを示すために簡潔な表記を使用します：例えば，ViT-L/16 は 16x16 入力パッチサイズの Large バリアントを意味する。
Transformer の系列長はパッチサイズの 2 乗に反比例するので，パッチサイズの小さいモデルは計算コストが高くなることに注意。
<!--We base ViT configurations on those used for BERT (Devlin+2019), as summarized in Table 1.
The "Base" and "Large" models are directly adopted from BERT and we add the larger "Huge" model.
In what follows we use brief notation to indicate the model size and the input patch size: for instance, ViT-L/16 means the "Large" variant with 16x16 input patch size.
Note that the Transformer’s sequence length is inversely proportional to the square of the patch size, thus models with smaller patch size are computationally more expensive. -->

<div class="figcenter">
<img src="/2024assets/2020Dosovitskiy_ViT_tab1and2.svg" style="width:66%;">
</div><div class="figcaption" style="width:77%;">

**表 2：一般的な画像分類ベンチマークにおける最新技術との比較**<br/>
精度の平均と標準偏差を3回の微調整の平均値で示す。
JFT-300M データセットで事前訓練された Vision Transformer モデルは，すべてのデータセットで ResNet ベースのベースラインを上回った。
より小さなパブリック ImageNet-21k データセットで事前に訓練された ViT も良好な結果を示した。
Touvron+(2020) で報告された 88.5% の結果をわずかに改善。
<!-- Table 2: Comparison with state of the art on popular image classification benchmarks.
We report mean and standard deviation of the accuracies, averaged over three fine-tuning runs.
Vision Transformer models pre-trained on the JFT-300M dataset outperform ResNet-based baselines on all datasets, while taking substantially less computational resources to pre-train.
ViT pre-trained on the smaller public ImageNet-21k dataset performs well too.
Slightly improved 88:5% result reported in Touvron+(2020). -->
</div>

<div class="figcenter">
<img src="/2024assets/2020Dosovitskiy_ViT_fig2-3-4.svg" style="width:77%;">
</div><div class="figcaption" style="width:77%;">

**図 3：ImageNet への転移学習**<br/>
小さなデータセットで事前訓練した場合，大きな ViT モデルは BiT ResNets (斜線部分) よりも性能が劣るが，大きなデータセットで事前訓練した場合は輝く。
同様に，データセットが大きくなるにつれて，大きな ViT モデルは小さな ViT モデルを追い越す。

**図 4：ImageNet における事前訓練サイズに対する線形少数撃学習の評価**<br/>
ResNets は事前学習データセットが小さいほど良い性能を示すが，事前学習が大きいほど良い性能を示す ViT よりも早くプラトーする。
ViT-b はすべての隠れ次元を半分にした ViT-B である。
<!-- Figure 3: Transfer to ImageNet.
While large ViT models perform worse than BiT ResNets (shaded area) when pre-trained on small datasets, they shine when pre-trained on larger datasets.
Similarly, larger ViT variants overtake smaller ones as the dataset grows.

Figure 4: Linear few-shot evaluation on ImageNet versus pre-training size.
ResNets perform better with smaller pre-training datasets but plateau sooner than ViT, which performs better with larger pre-training.
ViT-b is ViT-B with all hidden dimensions halved. -->
</div>


### CAM

<div class="figcenter">
<img src="/assets/2016Zhou_CAM_fig2ja.svg" width="66%"><br/>
CAM の概念図 Zhou (2016) Fig. 2 を改変
</div>

<br/><br/><br/>
<div class="figcenter">
<img src="/assets/2016Grad-CAM_boxer_tigercat.png" style="width:20%">
<img src="/assets/2016Grad-CAM_boxer.png" style="width:20%">
<img src="/assets/2016Grad-CAM_tigercat.png" style="width:20%"><br/>
Grad-CAM の結果。Selvaraj (2016) Fig. 5 より。左: 元画像。央: ボクサー犬と判断した場合のヒートマップ。右:トラ猫と判断した場合のヒートマップ
</div>

## Spoerer+(2020)

<div class="figcenter">
<img src="/2024assets/2020Spoerer_fig1.svg" style="width:66%;">
<div class="figcaption">

<font style="font-weight:bold">図 1. パラメータを一致させたネットワークの模式図</font><br/>
白箱は畳み込み層を表し，幅は畳み込み層の空間次元，高さは特徴地図数を表す。
モデル:<br/>
<font style="font-weight:bold">(1)</font> 畳み込みカーネル (B-K) のサイズを大きくすることで，パラメータ数を一致させたモデル <br/>
<font style="font-weight:bold">(2)</font> 特徴地図の数を一致させたモデル (B-F)，<br/>
<font style="font-weight:bold">(3)</font> ネットワークの深さを一致させたモデル (B-D)<br/>
例となる素子 (黒点) は，入力カーネル (B-K では幅が異なる) を表す色つきの領域にリンクされている。
範囲は例示的なもので，縮尺通りに描かれていない。

[Spoerer+2020 Fig.1](https://doi.org/10.1371/journal.pcbi.1008215)
<!-- Fig 1. Schematic representation of the parameter-matched networks.
White boxes represent convolutional layers, with the width representing the spatial dimensions of the convolut
ional layers and the height representing the number of feature maps.
Models were matched in the number of parameters by increasing (1) the size of the convolutional kernels (B-K),
 (2) the number of feature maps (B-F), and (3) the depth of the network (B-D).
Example units (black dots) are linked to coloured regions representing their input kernels (which differ in wi
dth in B-K).
The extents are illustrative and not drawn to scale. -->
</div></div>

## 経路集約ネットワーク Path Aggregation Network (PANet)

経路集約ネットワーク (PANet) [Liu+(2018)](https://arxiv.org/pdf/1803.01534.pdf) は最近, 経路集約ネットワーク Path Aggregation Network (PANet) を発表した。
このネットワークは Masked RCNN と FPN の枠組みを ベースにしながら，情報伝播を強化している。
このネットワークの特徴抽出器は FPN アーキテクチャを使用しており，低次層の特徴の伝搬を向上させる新たな拡張ボトムアップ経路を備えている。
この第 3 経路の各ステージは，前のステージの特徴地図を入力として 3x3 の畳み込み層で処理する。
その出力は，横方向に接続されたトップダウン経路の同じステージの特徴地図に追加され，これらの特徴地図は次のステージに供給される。
<!-- S. Liu et al. (2018) have recently released the Path Aggregation Network (PANet).
This network is based on the Mask R-CNN and the FPN frameworks while enhancing information propagation.
The feature extractor of the network uses a FPN architecture with a new augmented bottom-up pathway improving the propagation of low-layer features.
Each stage of this third pathway takes as input the feature maps of the previous stage and processes them with a 3x3 convolutional layer.
The output is added to the same stage feature maps of the top-down pathway using lateral connection and these feature maps feed the next stage. -->

<div class="figcenter">
<img src="/2024assets/2018Ouaknine_fig21.jpg" width="33%">
<div class="figcaption" style="width:44%;">

**トップダウン経路と拡張されたボトムアップ経路の横の連結**<!-- Lateral connection between the top-down pathway and the augmented bottom-up pathway.  -->
出典: [Liu+(2018)](https://arxiv.org/pdf/1803.01534.pdf)
</div></div>

補強されたボトムアップ経路の特徴地図は，RoI Align 層にプールされ，すべてのレベルの特徴から提案を抽出する。
適応的な特徴プーリング層は，各段階の特徴地図を完全連結層で処理し，すべての出力を連結する。
<!-- The feature maps of the augmented bottom-up pathway are pooled with a RoIAlign layer to extract proposals from all level features.
An adaptative feature pooling layer processes the features maps of each stage with a fully connected layer and concatenate all the outputs.  -->

<div class="figcenter">
<img src="/2024assets/2018Ouaknine_fig22.jpg" width="49%">
<div class="figcaption" style="width:44%;">

**適応的特徴プーリング層**<!-- Adatative feature pooling layer. --> Source: [Liu+(2018)](https://arxiv.org/pdf/1803.01534.pdf)
</div></div>

適応型特徴プーリング層の出力は，Mask R-CNN と同様に 3 つのブランチに供給される。
最初の 2 つのブランチでは，完全連結層を使用して，バウンディングボックスの座標と関連する物体クラスの予測を生成する。
3 つ目のブランチでは FCN を用いて RoI を処理し，検出された物体の画素単位の 2 値マスクを予測する。
さらに FCN の畳み込み層の出力を完全連結層で処理することで，予測される画素の位置関係を改善している。
最後に，並列パスの出力を再形成し，2 値化マスクを生成する FCN の出力に連結する。
<!-- The output of the adaptative feature pooling layer feeds three branches similarly to the Mask R-CNN.
The two first branches uses a fully connected layer to generate the predictions of the bounding box coordinates and the associated object class.
The third branch process the RoI with a FCN to predict a binary pixel-wise mask for the detected object.
The authors have added a path processing the output of a convolutional layer of the FCN with a fully connected layer to improve the localisation of the predicted pixels.
Finally the output of the parallel path is reshaped and concatenated to the output of the FCN generating the binary mask.  -->

<div class="figcenter">
<img src="/2024assets/2018Ouaknine_fig23.jpg" width="49%">
<div class="figcaption" style="width:44%;">

**FCN と完全連結層を持つ新しいパスを用いてバイナリマスクを予測する PANet のブランチ**
<!-- Branch of the PANet predicting the binary mask using a FCN and a new path with a fully connected layer.  -->
Source: https://arxiv.org/pdf/1803.01534.pdf
</div></div>

PANet は 2016COCO 画像切り分けチャレンジにおいて，特徴抽出器に ResNeXt を用いて 42.0 % の AP 得点を達成している。
また 2017COCO 画像切り分けチャレンジでは，7 つの特徴抽出器のアンサンブルを用いて 46.7 %の AP 得点を達成している。
ResNet ([He+(2015)](https://arxiv.org/pdf/1512.03385.pdf)), ResNeXt([Xie+(2016)](https://arxiv.org/pdf/1611.05431.pdf)), SENet ([Hu+(2017)](https://arxiv.org/pdf/1709.01507.pdf)) である。
<!-- The PANet has achieved 42.0% AP score on the 2016 COCO segmentation challenge using a ResNeXt as feature extractor.
They also performed the 2017 COCO segmentation challenge with an 46.7% AP score using a ensemble of seven feature extractors: ResNet (K. He et al. (2015), ResNeXt (S. Xie et al. (2016)) and SENet (J. Hu et al.(2017)).  -->

<div class="figcenter">
<img src="/2024assets/2018Ouaknine_fig24.jpg" widht="77%">
<div class="figcaption" style="width:66%;">

**PANet Achitecture**<br/>
**(a)**: FPN アーキテクチャを用いた特徴抽出器。<br/>
**(b)**: FPN アーキテクチャに新たに追加された増強されたボトムアップ経路。<br/>
**(c)**: 適応的な特徴プーリング層．<br/>
**(d)**: バウンディングボックスとオブジェクトクラスを表現する 2 つのブランチ．<br/>
**(e)**: オブジェクトのバイナリマスクを予測するブランチ．破線は，低レベルのパターンと高レベルのパターンの間のリンクに対応しており，赤は FPN で 100 以上の層で構成されており，緑は PANet で 10 以下の層で構成されているショートカットであ
る。
出典: [Liu+(2018)](https://arxiv.org/pdf/1803.01534.pdf)
<!-- PANet Achitecture. (a): Feature extractor using the FPN achitecture. (b): The new augmented bottom-up pathway added to the FPN architecture. ©: The adaptative feature pooling layer. (d): The two branches predicting the bounding box coordinated and the object class. (e): The branch predicting the binary mask of the object. The dashed lines correspond to links between low-level and high level patterns, the red one is in the FPN and consists in more than 100 layers, the green one is a shortcut in the PANet consisting of less than 10 layers. Source: S. Liu et al. (2018)  -->
</div></div>




# `bl_net.py`

```python
'''
Keras implementation of BL network
'''

import tensorflow as tf


class BLConvLayer(object):
    '''BL recurrent convolutional layer

    Note that this is NOT A KERAS LAYER but is an object containing Keras layers

    Args:
        filters: Int, number of output filters in convolutions
        kernel_size: Int or tuple/list of 2 integers, specifying the height and
            width of the 2D convolution window. Can be a single integer to
            specify the same value for all spatial dimensions.
        layer_name: String, prefix for layers in the RCL
        '''
    def __init__(self, filters, kernel_size, layer_name):
        # initialise convolutional layers
        self.b_conv = tf.keras.layers.Conv2D(
            filters, kernel_size, padding='same', use_bias=False,
            kernel_initializer='glorot_uniform',
            kernel_regularizer=tf.keras.regularizers.l2(1e-6),
            name='{}_BConv'.format(layer_name))

        self.l_conv = tf.keras.layers.Conv2D(
            filters, kernel_size, padding='same', use_bias=False,
            kernel_initializer='glorot_uniform',
            kernel_regularizer=tf.keras.regularizers.l2(1e-6),
            name='{}_LConv'.format(layer_name))

        # layer for summing convolutions
        self.sum_convs = tf.keras.layers.Lambda(
            tf.add_n, name='{}_ConvSum'.format(layer_name))

        # holds the most recent bottom-up conv
        # useful when the bottom-up input does not change, e.g. input image
        self.previous_b_conv = None

    def __call__(self, b_input=None, l_input=None):
        conv_list = []

        if not b_input is None:
            # run bottom-up conv and save result
            conv_list.append(self.b_conv(b_input))
            self.previous_b_conv = conv_list[-1]
        elif not self.previous_b_conv is None:
            # use the most recent bottom-up conv
            conv_list.append(self.previous_b_conv)
        else:
            raise ValueError('b_input must be given on first pass')

        # run lateral conv
        if l_input is not None:
            conv_list.append(self.l_conv(l_input))

        # return element-wise sum of convolutions
        return self.sum_convs(conv_list)


def bl_net(input_tensor, classes, n_timesteps=8, cumulative_readout=False):
        '''Build the computational graph for the model

        Note that evaluations based on model outputs will reflect instantaneous
        rather than cumulative readouts

        Args:
            input_tensor: Keras tensor (i.e. output of `layers.Input()`)
                to use as image input for the model.
            classes: int, number of classes to classify images into
            n_timesteps: int, number of model time steps to build
            cumulative_readout: Bool, if True then the outputs correspond to a
                cumulative readout on each time step if True then they
                correspond to a instant readout

        Returns:
            model
        '''

        data_format = tf.keras.backend.image_data_format()
        norm_axis = -1 if data_format == 'channels_last' else -3

        # initialise trainable layers (RCLs and linear readout)
        layers = [
            BLConvLayer(96, 7, 'RCL_0'),
            BLConvLayer(128, 5, 'RCL_1'),
            BLConvLayer(192, 3, 'RCL_2'),
            BLConvLayer(256, 3, 'RCL_3'),
            BLConvLayer(512, 3, 'RCL_4'),
            BLConvLayer(1024, 3, 'RCL_5'),
            BLConvLayer(2048, 1, 'RCL_6'),
        ]
        readout_dense = tf.keras.layers.Dense(
                classes, kernel_initializer='glorot_uniform',
                kernel_regularizer=tf.keras.regularizers.l2(1e-6),
                name='ReadoutDense')

        # initialise list for activations and outputs
        n_layers = len(layers)
        activations = [[None for _ in range(n_layers)]
                       for _ in range(n_timesteps)]
        presoftmax = [None for _ in range(n_timesteps)]
        outputs = [None for _ in range(n_timesteps)]

        # build the model
        for t in range(n_timesteps):
            for n, layer in enumerate(layers):

                # get the bottom-up input
                if n == 0:
                    # B conv on the image does not need to be recomputed
                    b_input = input_tensor if t == 0 else None
                else:
                    # pool b_input for all layers apart from input
                    b_input = tf.keras.layers.MaxPool2D(
                        pool_size=(2, 2),
                        name='MaxPool_Layer_{}_Time_{}'.format(n, t)
                        )(activations[t][n-1])

                # get the lateral input
                if t == 0:
                    l_input = None
                else:
                    l_input = activations[t-1][n]

                # convolutions
                x_tn = layer(b_input, l_input)
                # batch-normalisation
                x_tn = tf.keras.layers.BatchNormalization(
                    norm_axis,
                    name='BatchNorm_Layer_{}_Time_{}'.format(n, t))(x_tn)
                # ReLU
                activations[t][n] = tf.keras.layers.Activation(
                    'relu', name='ReLU_Layer_{}_Time_{}'.format(n, t))(x_tn)

            # add the readout layers
            x = tf.keras.layers.GlobalAvgPool2D(
                name='GlobalAvgPool_Time_{}'.format(t)
                )(activations[t][-1])
            presoftmax[t] = readout_dense(x)

            # select cumulative or instant readout
            if cumulative_readout and t > 0:
                x = tf.keras.layers.Add(
                    name='CumulativeReadout_Time_{}'.format(t)
                    )(presoftmax[:t+1])
            else:
                x = presoftmax[t]
            outputs[t] = tf.keras.layers.Activation(
                'softmax', name='Sotfmax_Time_{}'.format(t))(x)

        # create Keras model and return
        model = tf.keras.Model(
            inputs=input_tensor,
            outputs=outputs,
            name='bl_net')

        return model
```

