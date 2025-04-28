---
title: 第04回 2025 年度開講 駒澤大学 心理学特講 IIIA
author: 浅川 伸一
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">
<div align="center">
<font size="+1" color="navy"><strong>ディープラーニングの心理学的解釈</strong></font><br/><br/>
</div>

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 09/May/2025<br/>
Appache 2.0 license<br/>
</div>

# 実習ファイル

* [顔検出 <img src="/assets/colab_icon.svg" alt="顔検出">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2025notebooks/2025_0428opencv_face_detect_recognizer.ipynb){:target="_blank"}
* [課題提出用フォルダ](https://drive.google.com/drive/u/3/folders/1aenqcvlAQ7T-hv9-zsbrfntqpTbUj2EP){:target="_blank"}

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

