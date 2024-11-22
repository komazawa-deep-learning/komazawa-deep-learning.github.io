---
title: "第09回 2024年度開講 駒澤大学 認知心理学研究"
author: "浅川 伸一"
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="right">
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 22/Nov/2024<br/>
Appache 2.0 license<br/>
</div>

$$
\newcommand{\of}[1]{\left(#1\right)}
\newcommand{\Of}[1]{\left[#1\right]}
\newcommand{\KL}[2]{\operatorname{KL}\left(\left.{#1}\right\|{#2}\right)}
\newcommand{\given}[1]{\left|{#1}\right.}
\newcommand{\mb}[1]{\mathbf{#1}}
$$

## 本日のメニュー

1. 畳み込みニューラルネットワークの歴史と技法
2. 畳み込みニューラルネットワークの技法
3. 画像切り分け技術
4. トップダウン，ボトムアップ，再帰結合

## 実習ファイル

* [AlexNet による Karapetian+(2023) データの転移学習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_1122Karapetian_AlexNet_transfer_learning.ipynb){:target="_blank"}
* [ResNet 実習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_0603ResNet_with_Olivetti_faces_.ipynb){:target="_blank"}
* [ニューラルネットワークモデルの定義 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_1028komazawa_neural_networks_primer.ipynb){:target="_blank"}
* [3 層パーセプトロンと確率的勾配降下法のデモ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/2015corona/blob/master/2021notebooks/2021_0521mlp_Adam_SGD.ipynb){:target="_blank"}

<!-- * [ソフトマックス関数解題 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_1107softmax.ipynb){:target="_blank"}
また，ソフトマックス関数は，エネルギー関数とみなすことも可能である。 -->
<!-- * [ccap 資料初心者のためのニューラルネットワーク <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/project-ccap/project-ccap.github.io/blob/master/2022notebooks/2022_0418ccap_neural_networks_for_primer.ipynb){:target="_blank"}
* [画像認識 PyTorch の基礎編 AlexNet <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2020_0515komazawa_step_by_step_CNN_Pytorch.ipynb){:target="_blank"} -->

<!-- * [[Karapetian+(2023)](https://direct.mit.edu/jocn/article/35/11/1879/117201/Empirically-Identifying-and-Computationally) <img src="/assets/colab_icon.svg"> ](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_115Karapetian_demo.ipynb) -->
* [はじめての colab による画像認識 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021komazawa_cogsy000_CNN_demo.ipynb){:target="_blank"}
* [画像認識 PyTorch の基礎編  <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2020_0515komazawa_step_by_step_CNN_Pytorch.ipynb){:target="_blank"}
* [畳み込み演算の実習と DOG 関数 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_1024convolution_exercise.ipynb){:target="_blank"}
* [CNN 畳み込み層の可視化 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_1024CNN_layer_visualization.ipynb){:target="_blank"}
* [3 層パーセプトロンと確率的勾配降下法のデモ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/2015corona/blob/master/2021notebooks/2021_0521mlp_Adam_SGD.ipynb){:target="_blank"}
* [実習 MLP Adam SGD <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0521mlp_Adam_SGD.ipynb){:target="_blank"}
* [実習 LeNet PyTorch 版 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0528LeNet_pytorch.ipynb){:target="_blank"}
* [セグメンテーション実習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_0603Image_segmentation_demo.ipynb){:target="_blank"}
* [DETR  <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_0625DETR_demo.ipynb)
* [実装 Bottom-up Top-down model <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_0105royabel_BU_TD_multi_mnist.ipynb){:target="_blank"}

<!-- * [実習 3 つの MNIST <img src='/assets/colab_icon.svg'>](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0514komazawa_3mnists.ipynb){:target="_blank"}
* [実習 いくつかの画像フィルタ 特徴点検出アルゴリズム <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2020Sight_visit_feature_extractions_demo.ipynb){:target="_blank"}
* [実習 DOG などのフィルタと Harr 特徴による顔検出 a.k.a ビオラ＝ジョーンズ アルゴリズム <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0528edge_and_face_detection_algorithm_not_cnn.ipynb){:target="_blank"} -->


# 視覚モデルの歴史

人間の視覚処理のモデリングは，Hubel&Wiesel にさかのぼることができる。
Hubel&Wiesel では，視覚野 V1 の単純な細胞の応答特性はエッジの特徴検出として形式化され，複雑な細胞の特性は視野上で空間的に繰り返される一連の操作として概念化された（Hubel&Wiesel1962，translationaly invariant 並進不変）。
この計算原理は，コンピュータビジョンに霊長類の視覚系の特性を取り入れる試みとして Neocognitron（Fukushima1980）に取り入れられた。
さらに HMAX モデルファミリー（Riesenhuber&Poggio1999, Serre+2007）にも影響を与えた。
これらは，今日の特徴検出器とプーリング演算子を交互に用いた物体認識の深層学習モデルとして用いられれている。
(ただし，画像切り分けでは，プーリングを除外する傾向にある。)
AlexNet (Russakovsky+2015) 以前は，ネットワークをどのように組み込むか，あるいは他の方法で訓練するか，明確ではなかった（Olshausen&Field1996, Lowe1999, Torralba&Oliva2003）。
深層ニューラルネットワークを訓練する少なくとも 1 つの方法が示された 。同時に，このような不変
ImageNet 画像認識コンテストで優勝したモデルでは，視覚野 V4 と IT のニューロンの応答を圧倒的によくモデル化した内部「神経」表現を生成することが実証された（Yamins+2013, Cadieu+2014, Yamins+2014）。
ヒトの fMRI や MEG といった，より高度な実験レベルでの説明力の向上が確認された（Khaligh-Razavi&Kriegeskorte2014, Güçlü&van Gerven2015, Cichy+2016）。
<!-- Modeling human visual processing traces back at least to Hubel and Wiesel where response properties of simple cells in visual area V1 were formalized as feature detection of edges and properties of complex cells were conceptualized as a set of operations that were spatially repeated over the visual field (Hubel&Wiesel1962, i.e., translationally invariant).
These computational principles inspired the first models of object recognition, most notably, the Neocognitron (Fukushima1980) and the HMAX model family (Riesenhuber&Poggio1999; Serre+2007), where feature detectors and pooling operators were used in turns to build deep hierarchical models of object recognition.
However, such models lacked robust feature representations as it was not clear at the time how to either build in or otherwise train these networks to learn their spatially-repeated operations from input statistics – particularly for areas beyond visual area V1 (Olshausen&Field1996, Lowe1999, Torralba&Oliva2003).
These issues were first addressed by the AlexNet ANN (Krizhevsky+2012) in that it demonstrated at least one way to train a deep neural network for a large-scale invariant object recognition task (Russakovsky+2015).
Concurrently, deep networks optimized for such invariant object recognition tasks were demonstrated to produce internal "neural" representations that were by far the best models of the responses of neurons in non-human primate visual areas V4 and IT (Yamins+2013, Cadieu+2014, Yamins+2014).
Later work in humans confirmed these gains in explanatory power at the courser experimental level of fMRI and MEG (Khaligh-Razavi&Kriegeskorte2014; Güçlü&van_Gerven2015, Cichy+2016), with detailed measures of behavioral response patterns in both humans and non-human primates (e.g., Rajalingham+2015, Kubilius+2016, Rajalingham+2018), and with non-human primate neural spiking measures from the cortical area V1 (Cadena+2017). -->

#  BLnet (Spoerer+2020)

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


## 畳込みニューラルネット(CNN)

<div class="figcenter">
<img src='/assets/imagenet_result2017.png' style='width:74%'><br/>
イメージネットコンテストの結果
<!-- 画像認識の進歩 -->
</div>

深層学習 (ディープラーニング) の中で **畳み込みニューラルネットワーク** CNN と呼ばれるニューラルネットワークについて解説する。

最初に画像処理の概略を述べる CNN が，それまで主流であった従来の手法の性能を凌駕したことはすでに述べました。
CNN の特徴の一つに **エンドツーエンド** と呼ばれる考え方があります。
エンドツーエンドとは，従来手法によるパターン認識システムでは，専門家による手の込んだ詳細な作り込みを必要としていたことと異なり，面倒な作り込みをせずとも性能が向上したことを指します。

エンドツーエンドなニューラルネットワークにより，次のことが実現しました。

- ニューラルネットワークの層ごとに，特徴抽出が行われ，抽出された特徴がより高次の層へと伝達される
- ニューラルネットワークの各層では，比較的単純な特徴から次第に複雑な特徴へと段階的に変化する
- 高次層にみられる特徴は低次層の特徴より大域的，普遍的である
- 高次層のニューロンは，低次層で抽出された特徴を共有している

このことを簡単に説明してみます。

我々人間は，外界を認識するために必要な計算を，生物種としての発生の過程と，個人の発達を通しての経験に基づく認識システムを保持していると見ることができます。
従って我々の視覚認識には化石時代に始まる光の受容器としての眼の進化の歴史と発達を通じた個人の視覚経験が反映された結果でもあります。
人工知能の目標は，この複雑な特徴検出過程をどうやったらコンピュータが獲得できるかということでもあります。
外界を認識するために今日まで考案されてきたモデル（例えば，ニューラルネットワークサポートベクターマシンなどは）は複雑です。
ですがモデルを訓練するための学習方法はそれほど難しくありません。
この意味で画像認識課題が正しく動作するためのポイントは，認識システムが問題を解く事が可能なほど複雑であるかどうかではなく，十分に複雑が視覚環境，すなわち画像認識の場合，外部の艦橋を反映するために十分な量の像データを容易すことができるか否かにあります。
今日の CNN による画像認識性能の向上は，簡単な計算方法を用いて複雑な外部環境に適応できる認識システムを構築する方法が確立したからであると言うことが可能です。

下図<!--[fig:2012Ng_01](#fig:2012Ng_01){reference-type="ref"reference="fig:2012Ng_01"} -->に画像処理の例を挙げました。

<center>
<img src="/assets/2012Ng_ML_and_AI_01.png" style="width:66%">
</center>
<!-- 図[[fig:2012Ng_01]](#fig:2012Ng_01){reference-type="ref"reference="fig:2012Ng_01"} -->

<center>
<img src='/assets/2013LeCun-tutorial-icml_15.svg' style="width:66%"><br/>

**LeCun (2013) より**
</center>

## 福島のネオコグニトロン (Fukushima, 1980)

* S 細胞と C 細胞との繰り返し。最初の多層（深層）化された物体認識モデルととらえることが可能
    - S 細胞：生理学の単純細胞 simple cells に対応。受容野 receptive fields の概念を実現。特徴抽出，特徴検出。<br/>
    - C 細胞：複雑細胞 complex cells に対応。広い受容野。位置，回転，拡大縮小の差異を吸収<br>

<div class="figure figcenter">
<img src="/assets/Neocognitron.jpeg" width="55%">
<img src="/assets/Fukushima.jpeg" style="width:24%"><br>
<div class="figcaption">

ネオコグニトロンの模式図
</div></div>

## LeNet5 (LeCun1998)

* **LeNet**. Yann LeCun (現 Facebook AI 研究所所長)による CNN 実装
 [LeNet](http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf){:target="_blank"} 手書き数字認識

<center>
<img src="/assets/1998LeNet5.png" width="84%"><br/>
<div style="text-align:left; width:77%;background-color:cornsilk">

LeNet5 の論文より改変
</div>
</center>

- 畳込層とプーリング層（発表当初はサブサンプリング）との繰り返し
  - 畳込とプーリングは<font color="green">局所結合</font>
- MNIST を用いた１０種類の手書き文字認識
- 最終２層は全結合層をつなげて最終層１０ニューロン，最終層の各ニューロンの出力がそれぞれの数字（０から９までの１０種）に対応する



## AlexNet

<img src="/2023assets/alex_net_block_diagram.png"><br/>


## 畳み込み演算

<center>
<img src="/assets/dmoulin_gif/full_padding_no_strides.gif" style="width:33%">
<img src="/assets/dmoulin_gif/same_padding_no_strides_transposed.gif" style="width:33%"><br/>
<div style="text-align=:left; width:66%; background-color:cornsilk">

左:入力層 5x5青，出力層緑，カーネルサイズ3x3, フルパディング，ストライド=1.<br/>
右:入力層 5x5青，出力層緑，カーネルサイズ3x3, フルパディング，ストライド=1. トランスポーズド畳み込み
</div>
<img src="/assets/dmoulin_gif/numerical_max_pooling.gif" style="width:33%">
<img src="/assets/dmoulin_gif/numerical_average_pooling.gif" style="width:33%"><br/>
<div style="text-align=:left; width:66%; background-color:cornsilk">

左: 最大値プーリング。
右: 平均値プーリング
</div>
<div style="text-align=:left; width:44%; background-color:cornsilk">
Dmoulin and Visin (2020) より
</div>

<img src="/assets/dmoulin_gif/padding_strides.gif" style="width:33%">
<img src="/assets/dmoulin_gif/padding_strides_odd.gif" style="width:33%">
<img src="/assets/dmoulin_gif/padding_strides_odd_transposed.gif" style="width:33%"><br/>
<div style="text-align=:left; width:44%; background-color:cornsilk">

左: padding_strides, 中:padding_strides_odd, 右:padding_stride_transposed
</div>
<img src="/assets/dmoulin_gif/same_padding_no_strides.gif" style="width:33%">
<img src="/assets/dmoulin_gif/same_padding_no_strides_transposed.gif" style="width:33%">
<div style="text-align=:left; width:44%; background-color:cornsilk">

右:same_padding_no_strides, 左: same_padding_no_strides_transposed
</div>
<img src="/assets/dmoulin_gif/arbitrary_padding_no_strides.gif" style="width:33%">
<img src="/assets/dmoulin_gif/arbitrary_padding_no_strides_transposed.gif" style="width:33%">
<div style="text-align=:left; width:44%; background-color:cornsilk">
右:arbitrary padding no strides, 左: artibtrary padding no stride transposed
</div>
</center>

<div class="figcenter">

<iframe src="/conv-demo/index.html" width="140%" height="640px;" style="border:none;"></iframe>
</div>


## HMAX 最大値プーリング Riesenhuber&Poggio(1999)

<div class="figcenter">
<img src="/assets/1999Riesenhuber_Poggio_fig2.svg" style="width:49%">
<div class="figcaption" style="width:66%;">

<font style="font-weight:bold">モデルのスケッチ</font><br/>
単純細胞から作られた複雑細胞の古典的なモデルを拡張したもので，線形演算 (福島の表記法では `S` ユニット，テンプレート・マッチング 図中の実線) と非線形演算 (`C`プーリングユニット，最大値 MAX 演算を行う 図中破線) を持つ層の階層で構成。
細胞入力の最大値を選択，その値を用いてセルを駆動する非線形の MAX 演算は複雑細胞に対して，線形入力の合計とは異なりモデルの特性の鍵となる概念である。
この 2 種類の操作は 異なる位置にチューニングされた求心性結合をプールすることでパターン特異性と並進不変性を，また異なるスケールにチューニングされた求心性結合をプールすることで、スケール不変性をもたらした (図示せず)。<br/>
Riesenhuber&Poggio(1999) Fig. 2 より
</div></div>


<div class="figcenter">
<img src="/assets/1999Riesenhuber_Poggio_fig3a.svg" style="width:44%">
<img src="/assets/1999Riesenhuber_Poggio_fig3b.svg" style="width:44%"><br/>
<div class="figcaption" style="width:99%">

MAX 機構 高度に非線形な形状調整の特性。<br/>
「最適」特徴を決定するために考案された「単純化手順」を用いて得られた下側頭葉細胞の応答（選好刺激に対する反応が等しくなるように正規化された反応)。
実験では，もともと細胞は「水のボトル」の画像 (一番左の物体) に非常に強い反応を示した。
その後，刺激を単色の輪郭に単純化したところ，細胞の発火が増加し，さらに，楕円を支える棒からなるパドルのような物体に変化した。
この物体が強い反応を引き起こすのに対し，棒や楕円だけではほとんど反応しなかった。
Riesenhuber&Poggio(1999) Fig 3A.
</div></div>

実験とモデルの比較。
白棒はの実験用ニューロンの反応を示す。
黒と灰色の棒は 選好刺激の 幹-楕円 の基部の遷移に合わせてチューニングしたモデル細胞の反応を示している。
モデル細胞は 直上図に示したモデルを簡略化したもの。
受容野の各位置に 2 種類の S1 特徴があり，それぞれが遷移領域の左側または右側にチューンしていて，その出力が C1 ユニットに入力され MAX 関数 (黒棒) または SUM 関数 (灰色棒) を用いてプールされている。
モデル細胞は 実験ニューロンの 選好刺激が受容野内にあるときに反応が最大になるよう，C1 ユニットに接続されていた。

図 3. MAX 機構の高度に非線形な形状チューニング特性。
(a) `最適` 特徴を決定するために考案された `単純化手続`(26) を用いて得られた，実験的に観察された IT 細胞の応答 (好ましい刺激に対する応答が 1 に等しくなるように正規化された応答)。
実験では，細胞はもともと「水瓶」 (一番左の物体) の画像にかなり強く反応した。
その後，刺激は単色の輪郭に「単純化」され，細胞の発火が増加し，さらに楕円を支える棒からなるパドルのような物体に変化した。
この物体は強い反応を引き起こしたが，棒や楕円だけではほとんど全く反応を起こさなかった (図は許可を得て使用)。
(b) 実験とモデルの比較。
白棒は (a) の実験ニューロンの反応。
黒棒と灰色棒は，優先刺激の幹-楕円底遷移に同調させたモデルニューロンの反応を示す。
このモデルニューロンは，図 2 に示したモデルの単純化された版の最上部にあり，受容野の各位置に 2 種類の S1 特徴のみが存在し，それぞれが遷移領域の左側または右側に同調し，MAX 関数 (黒棒グラフ) または SUM 関数 (灰色棒グラフ) のいずれかを用いてそれらをプールする C1 ユニットに供給される。
モデルニューロンは，実験ニューロンの好ましい刺激がその受容野にあるときに，その反応が最大になるように，これらの C1 ユニットに接続された。
<!-- Fig. 3. Highly nonlinear shape-tuning properties of the MAX mechanism.
(a) Experimentally observed responses of IT cells obtained using a `simplification procedure`(26) designed to determine `optimal` features (responses normalized so that the response to the preferred stimulus is equal to 1).
In that experiment, the cell originally responded quite strongly to the image of a `water bottle` (leftmost object).
The stimulus was then `simplified` to its monochromatic outline, which increased the cell’s firing, and further, to a paddle-like object consisting of a bar supporting an ellipse.
Whereas this object evoked a strong response, the bar or the ellipse alone produced almost no response at all (figure used by permission).
(b) Comparison of experiment and model.
White bars show the responses of the experimental neuron from (a).
Black and gray bars show the response of a model neuron tuned to the stem-ellipsoidal base transition of the preferred stimulus.
The model neuron is at the top of a simplified version of the model shown in Fig. 2, where there were only two types of S1 features at each position in the receptive field, each tuned to the left or right side of the transition region, which fed into C1 units that pooled them using either a MAX function (black bars) or a SUM function (gray bars).
The model neuron was connected to these C1 units so that its response was maximal when the experimental neuron’s preferred stimulus was in its receptive field. -->


<!-- MAX 機構に対する追加的な間接的支持は，IT 細胞の好ましい特徴，つまり細胞を駆動するための刺激成分を決定するために，「単純化手順」(26 )または「複雑性減少」(27) を用いた研究から得られている。 -->
MAX 機構に対する追加的な間接的支持は，IT 細胞の好ましい特徴，つまり細胞を駆動するための刺激成分を決定するために，「単純化手順」または「複雑性減少」を用いた研究から得られている。
これらの研究では一般的に，IT 細胞の高度に非線形な同調を発見している (図 3a)。
このような同調は MAX 応答関数 (図 3b 黒棒) と一致する。
線形モデル (図 3b 灰色棒) では，入力画像のわずかな変化に対す るこの強い応答の変化を再現できないことに注意。
<!--Additional indirect support for a MAX mechanism comes from studies using a `simplification procedure`(26) or `complexity reduction`(27) to determine the preferred features of IT cells, that is, the stimulus components that are responsible for driving the cell.
These studies commonly find a highly nonlinear tuning of IT cells (Fig. 3a).
Such tuning is compatible with the MAX response function (Fig. 3b, black bars).
Note that a linear model (Fig. 3b, gray bars) could not reproduce this strong change in response for small changes in the input image.-->


## 経路仮説と残差ネット

* 腹側経路 ventral pathways ("what" 経路)
* 背側経路 dorsan pathways ("where" 経路)

<center>
<img src="/assets/1982Ungerleider_Mishkin.jpg" width="49%">
<div style="text-align:left;width:88%;color:teal">

* 下左: 物体弁別課題と下側頭回損傷。
* 下右: 目印課題と頭頂葉損傷。
Ungerleider&Mishkin1982 より。
</div></center>

<center>
<img src="/2023assets/2004Hickok_dorsal_ventral_language_fig1a.jpg" width="49%">
<img src="/2023assets/2004Hickok_dorsal_ventral_language_fig1b.jpg" width="49%">
<div style="text-align:left;width:94%;color:teal">
左: 言語の機能解剖学的枠組み。Hickok&Poeppel2000 より

右: 脳の側面図に示したモデル構成要素の一般的な場所。
モデル内のある機能に関連する皮質領域は，その機能に特化しているという仮説ではない。
調音に基づく音声符号を支援すると考えられる前頭葉領域の定義は，物品の命名と調音リハーサル処理の機能画像研究にお
ける活性化領域の一般的な分布から得られる (例えば Awh+1996, Hickok+2003, Indefrey&Levelt)。
帯状の領域 (上側頭溝) は，音素レベルの表現を支援すると思われる領域。
</div>
</center>

## ResNet におけるスキップ結合

<img src="/assets/ResNet_Fig2.svg" width="33%"><br/>
<img src="/assets/2015ResNet30.svg" width="94%"><br/>

#### R-CNN

<img src="/2023assets/2015Ren_Faster_R-CNN_fig2.svg">

<!--<img src="/assets/2017He_MaskRCNN_41.svg">
<img src="/assets/2015Fast_R-CNN_Fig1.svg">
<img src="/assets/2015Faster_RCNN_RPN.svg">
<img src="/assets/1998LeCun_Fig2_CNN.svg">
<img src="/assets/2017He_MaskRCNN_02SemSeg.svg">
<img src="/assets/2017He_MaskRCNN_08.svg">
<img src="/assets/2017He_MaskRCNN_02Oject.svg">
<img src="/assets/2013Girshick_RCNN_Fig1.svg"> -->


# CORnet [Kubilius+2018](https://doi.org/10.1101/408385){:target="_blank"}

<div class="figcenter">
<img src="/2024assets/2018Kubillus_CORnet_fig1.svg" width="77%">
</div>
<div class="figcaption" style="width:77%;">

**図 1. CORnet 族のアーキテクチャ**<br/>
この族のすべてのモデルには，皮質領域 V1, V2, V4, IT にあらかじめ写像された 4 領域がある。
網膜と LGN の処理は現在のところモデル化されていない (灰色で塗りつぶされた領域)。
すべての領域はフィードフォワードかリカレント (領域内) のどちらかであるが，現在のところ，領域間のスキップ接続やフィードバック接続を持つモデルは考慮していない (灰色で塗りつぶした破線の矢印)。
本論文では，3  種類の CORnet を検討し，それぞれ異なる機能を提供する： CORnet-Z は軽量な AlexNet 代替モデル，CORnet-R は生物学的に説得力のある時間的アンロールを持つ単純なリカレントモデル，そしてCORnet-S は Brain-Score で現時点で最も高い性能を発揮するモデルである。
下段の図は各モデルの領域内の回路を表している。
<!-- Fig. 1. CORnet family of architectures.
All models in this family have four areas that are pre-mapped to cortical areas V1, V2, V4, and IT.
Retinal and LGN processing is currently not modeled (greyed-out areas).
All areas can be either feedforward or recurrent (within area) but currently we do not consider models with skip or feedback connections between areas (grayed-out dashed arrows).
In this paper, we consider three flavors of CORnet, each serving distinct functions: CORnet-Z is a lightweight AlexNet alternative, CORnet-R is a simple recurrent model with biologically-plausible unrolling in time, and CORnet-S is our highest-performing model on Brain-Score at the moment.
Diagrams in the bottom panel depict circuitry within an area of each model. -->
</div>

<div class="figcenter">
<img src="/2024assets/2018Kubillus_CORnet_tab1.svg">
</div>

モデルの復号化部は，単純な線形分類器 (各物体カテゴリに対して 1 つの総和を持つ重み付き線形和の集合) を実装する。
ImageNet で学習する場合，最後のモデル領域 (再帰の場合は最後の時間ステップ) の応答は，さらにソフトマックス非線形に渡され，1000 通りの分類が実行される。
この分類器に投影される神経応答の量を減らすために，まず特徴地図ごとの受容野全体の応答を平均化する。
現在の CORnet 族の定義では，領域横断バイパス接続や領域横断フィードバック接続は存在しない。
網膜と LGN の処理は省略されている (考察参照)。
また，計算要求が高いため，CORnet-S の第 1 領域は簡略化され，2 つの畳み込みのみが含まれる (下記参照)。
<!-- The decoder part of a model implements a simple linear classifier – a set of weighted linear sums with one sum for each object category.
When training on ImageNet, responses of last model area (and last time step in the case of recurrence) are further passed through a softmax nonlinearity to perform a 1000-way classification.
To reduce the amount of neural responses projecting to this classifier, we first average responses over the entire receptive field per feature map.
There are no across-area bypass or across-area feedback connections in the current definition of CORnet family.
Retinal and LGN processing are omitted (see Discussion).
Also, due to high computational demands, the first area in CORnet-S is simplified to only include two convolutions (see below). -->

**CORnet-Z** (通称 Zero) は我々の最も単純なモデルであり，(i) AlexNet は既に深いモデル(Schrimpf+2018) とほぼ同程度に神経応答を予測しており，(ii) VGG (Simonyan&Zisserman2014) 以降に提案されたほとんどのアーキテクチャが 1 つの 1000-way 線形分類層のみを含むため，ImageNetの良好な性能を達成するために複数の完全連結層は必要ないようであることを観察することによって導き出された。
従って，CORnet-Z の面積回路は単一の畳み込み，それに続く ReLU 非線形と最大プーリングのみで構成される。
<!-- CORnet-Z (a.k.a. "Zero") is our simplest model, derived by observing that (i) AlexNet is already nearly as good in predicting neural responses as deeper models (Schrimpf+2018) and (ii) multiple fully-connected layers do not appear necessary to achieve good ImageNet performance, as most architectures proposed after VGG (Simonyan&Zisserman2014) contain only a singe 1000-way linear classification layer.
Thus, CORnet-Z’s area circuits consist of only a single convolution, followed by a ReLU nonlinearity and max pooling. -->

**CORnet-R** (通称 Recurrent) は，生物学的に妥当な方法でネットワークを伝播するリカレントダイナミクスを導入する (生物学的ネットワーク・アンローリングと非生物学的ネットワーク・アンローリングの比較については図 2 参照)。
CORnet-R では，リカレンスは領野内でのみ導入される (エリア間のフィードバック接続はない) ため，アンロールの特殊な方法は (より多くのメモリを消費することを除けば) ほとんど影響を及ぼさないが，それでもこのモデルを神経ダイナミクスの調査に役立てるため，生物学的に妥当なアンロールを使用することにした。
<!-- CORnet-R (a.k.a. "Recurrent") introduces recurrent dynamics that would propagate through the network in a biologically-valid manner (see Fig. 2 for a comparison between biological and non-biologicall network unrolling).
In CORnet-R, recurrence is introduced only within an area (no feedback connections between areas), so the particular way of unrolling has little effect (apart from consuming much more memory), but we chose to use biologically-valid unrolling nonetheless to make this model useful for investigating neural dynamics. -->

入力はまず，畳み込みを通すことでチャンネル数を 2 倍に増やしながら 2 倍にダウンスケールされ，続いて正規化と非線形化が行われる。
状態 (最初はゼロ) が結果に追加され，別の畳み込み，正規化，非線形性を経て，結果が領域の新しい状態として保存される。
我々は，群正規化 (Wu&He2018) と ReLU 非線形性を使用した。
<!-- The input is first downscaled twofold while increasing the number of channels twofold by passing it through a convolution, followed by normalization and a nonlinearity.
The state (initially zero) is added to the result and passed through another convolution, normalization, and nonlinearity, and the result is saved as a new state of the area.
We used group normalization (Wu and He, 2018) and ReLU nonlinearity -->

**CORnet-S** (通称 Skip) は，非常に深いフィードフォワードアーキテクチャを浅いリカレントモデルに変換することで，Brain-Score の最高モデルに匹敵することを目指している。
具体的には，CORnet-S は我々の行動ベンチマークで最も優れたモデルのいくつかである ResNets からインスピレーションを得ている (Rajalingham+2018, Schrimpf+2018)。
Liao&Poggio(2016) は ResNet 構造をアンロール型リカレントネットワークと考えることができると提案し，さらに最近の研究では CIFAR や ImageNet の性能に大きな損失を与えることなく重み共有が実際に可能であることを実証した (Jastrzebski+2017, Leroux+2018)。
<!-- CORnet-S (a.k.a. "Skip") aims to rival the best models on Brain-Score by transforming very deep feedforward architectures into a shallow recurrent model.
Specifically, CORnet-S draws inspiration from ResNets that are some of the best models on our behavioral benchmark (Rajalingham+2018, Schrimpf+2018).
Liao&Poggio(2016) proposed that ResNet structure could be thought of as an unrolled recurrent network and recent studies further demonstrated that weight sharing was indeed possible without a significant loss in CIFAR and ImageNet performance (Jastrzebski+2017, Leroux+2018). -->

CORnet-S は CORnet-R の回路の上にさらに 2 つの畳み込み（それぞれ正規化と非線形化が続く）を積み重ねる。
さらに，ResNet のボトルネックブロック構造に従い，2 回目の畳み込みでチャンネル数を4倍に拡大し，最後の畳み込みでチャンネル数を減少させる。
また，入力に状態を追加した結果が非線形を適用する直前に最後の畳み込みの出力と結合されるように，スキップ接続も含めた。
CORnet-S が領域内リカレント接続のみを有することを考慮し，メモリフットプリントを最小化するために，時間的にネットワークのアンロールを利用することなくこのモデルを訓練した (すなわち 図 2 に描かれているようなアンロールはないが，繰り返される計算にわたって重みは依然として共有される)。
特に，最初に情報が処理されるとき，3 回目の畳み込みとスキップ畳み込みは，入力をダウンスケールするために 2 のストライドを使用する。
そして，その出力は，さらなるリカレント処理（図 1 では gate と呼ばれる）のために，元の入力の代わりに使われる。
このモデルではバッチ正規化 (Ioffe&Szegedy2015) と ReLU 非線形性を使用し，バッチ正規化は (Jastrzebski+2017) が示唆するように経時的に共有されなかった。
<!-- CORnet-S stacks two more convolutions (each followed by a normalization and nonlinearity) on top of CORnet-R’s circuit.
Moreover, following ResNet’s bottleneck block structure, the second convolution expands the number of channels fourfold while the last one decreases them back.
We also included a skip connection, such that the result of adding the state to the input is combined with the output of the last convolution just prior to applying a nonlinearity.
Given that CORnet-S only has within-area recurrent connections, in order to minimize memory footprint we trained this model without making use of any network unrolling in time (i.e. no unrolling as depicted in Fig. 2, but weights are still shared over repeated computations).
In particular, the first time information is processed, the third convolution and the skip convolution use a stride of two to downscale inputs.
The output is then used instead of the original input for further recurrent processing (referred to as "gate" in Fig. 1).
We used batch normalization (Ioffe and Szegedy, 2015) and ReLU nonlinearity in this model, and batch normalization was not shared over time as suggested by (Jastrzebski+2017). -->

