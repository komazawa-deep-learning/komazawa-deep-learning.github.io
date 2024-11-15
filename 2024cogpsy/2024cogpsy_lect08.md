---
title: "第08回 2024年度開講 駒澤大学 認知心理学研究"
author: "浅川 伸一"
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="right">
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 11/Oct/2024<br/>
Appache 2.0 license<br/>
</div>

$$
\newcommand{\of}[1]{\left(#1\right)}
\newcommand{\Of}[1]{\left[#1\right]}
\newcommand{\KL}[2]{\operatorname{KL}\left(\left.{#1}\right\|{#2}\right)}
\newcommand{\given}[1]{\left|{#1}\right.}
\newcommand{\mb}[1]{\mathbf{#1}}
$$

#  畳み込みニューラルネットワークの基礎

先週は，お休みをいただきまして失礼しました。
日本高次脳機能障害学会に出席していたためです。

## 本日のメニュー

1. `git clone https://github.com/cjspoerer/rcnn-sat.git`, `git clone https://github.com/Agnessa14/Perceptual-decision-making.git`
2. [Spoerer+2020](https://doi.org/10.1371/journal.pcbi.1008215) での提案モデルを用いるているので，この論文を取り上げる。
3. 畳み込みニューラルネットワークの種類と技法を検討する。
4. [フレームワーク](/eco/) について

竹市先生から引き継いて，この授業を行います。
竹市先生によれば (浅川が受け止めている限りにおいて)，この授業の目標は以下だと考えます:

1. コードを書けるようにするという
2. データとモデルとの関係を考える

とりわけ，心理実験から得られる行動データを模倣するモデルと，EEG, MEG をはじめとする生理データを模倣するのか，それら両方なのかで考え方が異なります。

深層学習モデルで言えば，フィードフォワード型とリカレント型のニューラルネットワーク，さらに最近では Transformer 型のモデルを用いた実装となります。

今回から，数回で，これらモデルを概説して行きます。

## 実習ファイル

* [[Karapetian+(2023)](https://direct.mit.edu/jocn/article/35/11/1879/117201/Empirically-Identifying-and-Computationally) <img src="/assets/colab_icon.svg"> ](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_115Karapetian_demo.ipynb)
* [ResNet 実習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_0603ResNet_with_Olivetti_faces_.ipynb){:target="_blank"}
* [実習 LeNet PyTorch 版 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0528LeNet_pytorch.ipynb){:target="_blank"}


##### [Karapetian+(2023) Empirically Identifying and Computationally Modeling the Brain–Behavior Relationship for Human Scene Categorization](https://doi.org/10.1162/jocn_a_02043){:target="_blank"} 竹市先生ご指定の文献

<div class="abstract">

ヒトは，自分が直面している情景のカテゴリーなど，身近な視覚環境の性質について，早くて正確な知覚判断を難なく下している。
これまでの研究で，このような特性の基礎となる皮質表現が豊富にあることが明らかになっている。
しかし，これらの表象のうち，どの表象が意思決定に適しているかはまだわかっていない。
ここでは，ニューロイメージングと計算モデリングを用いて，経験的，計算的にこの問題にアプローチした。
経験的な部分では，情景分類課題 (自然物対人工物) 中の参加者の脳波データと RT を収集した。
そして，信号検出理論の多変量拡張を用いて，波データと行動を関連付けた。
その結果，刺激開始後約 100 ミリ秒から約 200 ミリ秒の間に特に神経データと行動の相関が観察され，この時間帯の神経情景表現が意思決定に適したフォーマットになっていることが示唆された。
計算部分については，脳と行動のモデルとしてリカレント畳み込みニューラルネットワーク (RCNN) を評価した。
RCNN は，我々のこれまでの観察を画像計算可能なモデルに統合し，神経表現，情景分類データ，およびそれらの間の関係をよく予測した。
我々の結果は，ヒトにおける情景分類の神経と行動の相関を同定し，計算によって特徴付けるものである。
<!-- Humans effortlessly make quick and accurate perceptual decisions about the nature of their immediate visual environment, such as the category of the scene they face.
Previous research has revealed a rich set of cortical representations potentially underlying this feat.
However, it remains unknown which of these representations are suitably formatted for decision-making.
Here, we approached this question empirically and computationally, using neuroimaging and computational modeling.
For the empirical part, we collected EEG data and RTs from human participants during a scene categorization task (natural vs. man-made).
We then related EEG data to behavior to behavior using a multivariate extension of signal detection theory.
We observed a correlation between neural data and behavior specifically between ∼100 msec and ∼200 msec after stimulus onset, suggesting that the neural scene representations in this time period are suitably formatted for decision-making.
For the computational part, we evaluated a recurrent convolutional neural network (RCNN) as a model of brain and behavior.
Unifying our previous observations in an image-computable model, the RCNN predicted well the neural representations, the behavioral scene categorization data, as well as the relationship between them.
Our results identify and computationally characterize the neural and behavioral correlates of scene categorization in humans. -->
</div>

<div class="figcenter">
<img src="/2024assets/2023Karapetian_fig1.jpg" style="width:66%"><br/>
</div>

**図 1. 刺激セット，パラダイム，距離-平面アプローチ**<!-- Figure 1. Stimulus set, paradigm, and distance-to-hyperplane approach.--><br/>
**A**: 解析アプローチ。神経データと行動データを結びつけるために，多変量空間における信号検出理論の拡張である距離-超平面アプローチを用いた。<br/>
**B**: 刺激セット。Places-365  (Zhou+2018) から刺激を選択し，30 個の自然情景と 30 個の人工情景の集合を作成した。<br/>
**C**: 実験パラダイム。参加者はブロックの半分で情景分類課題を行い，残りの半分で直交固視 + 字色検出課題 (妨害課題と呼ぶ) を行った。<br/>
**D**: 距離-超平面アプローチ。距離と RT の相関が有意に負になったときに起こる，神経表象が意思決定に適した形になるタイミングを決定するために，すべての時点において分析を適用した。

<!--* (A) Analysis approach. To link neural and behavioral data, we used the distance-to-hyperplane approach, an extension of signal detection theory in a multivariate space.
* (B) Stimulus set. We selected stimuli from Places-365 (Zhou+2018), creating a set of 30 natural and 30 man-made scenes.
* (C) Experimental paradigm. Participants performed a scene categorization task on half of the blocks and an orthogonal fixation cross color detection task (referred to as distraction task) on the other half.
* (D) Distance-to-hyperplane approach. We applied the analysis at every time point to determine when neural representations are suitably formatted for decision-making, which occurs when the correlation between distances and RTs is significantly negative. -->


<div class="figcenter">
<img src="/2024assets/2023Karapetian_fig2.jpg" style="width:55%">
</div>

**図 2. 情景の同一性とカテゴリの復号化**<!-- Figure 2. Scene identity and category decoding. --><br/>
**(A)** カテゴリ課題(青)，気晴らし課題(マゼンタ)，およびその差(黒)の EEG データにおける，情景同一性復号化の結果。
0 ミリ秒の灰色の縦破線は刺激の開始を表す。曲線の周囲の斜線部分は SEM を示す。
有意な時点(右側，p < 0.01, FDR 調整済み) はアスタリスクで示されている。<br/>
**(B)** 課題の結果と両者の差異における，情景カテゴリーの復号化 (自然対人工) の結果<br/>
**(C)** カテゴリー化および気晴らし課題における，情景同一性の復号化のピーク<br/>
**(D)** 情景カテゴリーの復号化ピークにおける，多次元尺度構成法の結果<br/>
**(E)** 情景の同一性復号化と情景カテゴリ復号化の頂点復号化潜時における両課題のチャネル空間で実行されたサーチライト解析の結果と<br/>
**(F)** 情景カテゴリー復号化。
有意なチャネル (右側 p < 0.01, FDR 調整済み) は黒点で示されている。

<!--**(A)** Pairwise scene identity decoding results on EEG data from the categorization task (blue), distraction task (magenta), and their difference (black).
The vertical dashed gray line at 0 msec represents the stimulus onset.
The shaded area around the curves indicates the SEM.
Significant time points (right tailed, p<0.01, FDR-adjusted) are indicated with asterisks.<br/>
**(B)** Scene category decoding (natural vs. man-made) results for both tasks and their difference.<br/>
**(C)** Multidimensional scaling results for scene identity decoding from the categorization and distraction tasks at the scene identity decoding peak and
**(D)** scene category decoding peak.
**(E)** Results from the searchlight analysis performed in channel space in both tasks at peak decoding latency for scene identity decoding and
**(F)** scene category decoding.
Significant channels (right-tailed, p < 0.01, FDR-adjusted) are depicted with black dots.-->

<div class="figcenter">
<img src="/2024assets/2023Karapetian_fig4.jpg" style="width:55%">
</div>

**図 4. 人間の神経情景表現を RCNN と FCNN とでモデル化**<!-- Figure 4. Modeling human neural scene representations with an RCNN versus an FCNN. -->

**(A)** 解析に用いたリカレントCNN，BLnet (Spoerer+2020) のアーキテクチャ。
ネットワークは 7 層からなり，ボトムアップ (緑の矢印) とラテラル (黒の矢印) 接続で結ばれている。
特徴量は 3 つの層 (1, 4, 7) から 8 つの異なる時間ステップで抽出され，RT は読み出し層から収集された。<br/>
**(B)** すべての情景，自然情景，人工的情景について，ヒトの神経表現と 3 つの異なる層からの RCNN 特徴量 (8 つの時間ステップの中央値) に対して RSA を実行した結果。
0 ミリ秒の垂直破線は刺激開始を表す。
曲線の周りの斜線部分は SEM を表す。
有意な時点をアスタリスクで示す (右側検定 p＜0.05，FDR 補正)。
破線の縦線はピークを示す。
灰色の斜線はノイズの上限を示す。<br/>
**(C)** BLnet の フィードフォワード，パラメータマッチ版である B-Dnet (Spoerer+2020) の特徴量を用いた RSA 結果。<br/>
**(D)** RCNN と FCNN の結果の差の波 (両側, p < 0.05, FDR 補正)。

<!-- * (A) Architecture of BLnet (Spoerer+2020), the recurrent CNN used in the analysis.
The network consists of seven layers, linked via bottom–up (green arrows) and lateral (black arrows) connections.
Features were extracted from three layers (1, 4, and 7) at eight different time steps, and RTs were collected from the readout layer.
* (B) Results of the RSA performed on the neural representations of humans and RCNN features from three different layers (median over eight time steps), for all scenes, natural scenes, and man-made scenes.
The vertical dashed gray line at 0 msec represents the stimulus onset.
The shaded areas around the curves represent the SEM. Significant time points are denoted with asterisks (right-tailed, p < 0.05, FDR-corrected).
The dashed vertical lines indicate the peaks.
The shaded gray area represents the noise ceiling.
* (C) RSA results with features from B-Dnet (Spoerer et al., 2020), the feedforward, parameter-matched version of BLnet.
* (D) Difference waves between RCNN and FCNN results (two-tailed, p < 0.05, FDR-corrected). -->

## 畳み込みニューラルネットワーク (CNN: Convolutional Neural Networks)

<img src="/2023assets/alex_net_block_diagram.png"><br/>

<img src="/assets/ResNet_Fig2.svg" width="33%"><br/>
<img src="/assets/2015ResNet30.svg" width="94%"><br/>
<img src="/2023assets/2015Ren_Faster_R-CNN_fig2.svg">

<!-- <img src="/assets/2017He_MaskRCNN_41.svg">
<img src="/assets/2015Fast_R-CNN_Fig1.svg">
<img src="/assets/2015Faster_RCNN_RPN.svg">
<img src="/assets/1998LeCun_Fig2_CNN.svg">
<img src="/assets/2017He_MaskRCNN_02SemSeg.svg">
<img src="/assets/2017He_MaskRCNN_08.svg">
<img src="/assets/2017He_MaskRCNN_02Oject.svg">
<img src="/assets/2013Girshick_RCNN_Fig1.svg"> -->

深層学習 (ディープラーニング) の中で **畳み込みニューラルネットワーク** CNN と呼ばれるニューラルネットワークについて解説します。

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

<div class="figcenter">
<img src="/assets/2012Ng_ML_and_AI_01.png" style="width:66%"><br/>
</div>
<!-- 図[[fig:2012Ng_01]](#fig:2012Ng_01){reference-type="ref"reference="fig:2012Ng_01"} -->

<div class="figcenter">
<img src='/assets/2013LeCun-tutorial-icml_15.svg' style="width:66%"><br/>

**LeCun (2013) より**
</div>

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

## Riesenhuber&Poggio(1999) HMAX 最大値プーリング

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
Note that a linear model (Fig. 3b, gray bars) could not reproduce this strong change in response for small changes in the input image.
-->

<div class="figcenter">

<iframe src="/conv-demo/index.html" width="140%" height="640px;" style="border:none;"></iframe>

</div>


# `bl_net.py`

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

