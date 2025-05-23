---
title: 第06回 2025 年度開講 駒澤大学 心理学特講 IIIA
author: 浅川 伸一
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">
<div align="center">
<font size="+1" color="navy"><strong>ディープラーニングの心理学的解釈</strong></font><br/><br/>
</div>

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 23/May/2025<br/>
Appache 2.0 license<br/>
</div>

* [課題提出用フォルダ<img src="/2025assets/Google_Drive_icon_2020.svg" style="width:02%">](https://drive.google.com/drive/u/3/folders/1EdOL_Wz1656fWqD0RmmKgLmf_fUsl2QY){:target="_blank"}

Transfer learning の話をして, BIT シミュレーションを紹介する予定

休講案内


## 実習

* [ResNet 実習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_0603ResNet_with_Olivetti_faces_.ipynb)
* [セグメンテーション実習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_0603Image_segmentation_demo.ipynb)

* [BIT 線分二等分課題 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_1210bit_line_bisection.ipynb#scrollTo=moT9LtTZDV-J)

# 1. 経路仮説と残差ネット

* 腹側経路 ventral pathways ("what" 経路)
* 背側経路 dorsan pathways ("where" 経路)

<center>
<img src="/assets/1982Ungerleider_Mishkin.jpg" width="49%"><br/>
Ungerleider and Mishkin (1982) より
</center>

<center>
<img src="/assets/LNCS2766_Chapter_2_fig2_4.jpg" width="49%"><br/>
Behnke (2003) より
</center>

> 同様の 2 経路による処理は 聴覚 (Romanski et al., 1999) や 触覚(Reed et al., 2005)でも発見されている。

発展的な話題としては，このような 2 種類の処理経路は，処理される情報の種類の問題ではないくて，機能に関与した区別であるとの仮説もある。

* 腹側経路は物体に関する情報の知覚 (知覚のための視覚) 
* 背側経路は行動を導くための情報処理 (行動のための視覚) 

さらに，背側経路は 背外側経路 (dorsolateral) と背中側経路 (dorsomedial) に細分化できることが示唆されている（Binkofski and Buxbaum, 2013, Grafton, 2010, Rizzolatti and Matelli, 2003)。

* 背外側側経路 前頭頂内溝（aIPS）と前頭前皮質の腹側部分（PMv）, 古典的に到達運動の計画に寄与 （Davare ら, 2015; Davare ら, 2012; Vesia and Crawford,2012）
* 背中側経路は V6A と内側頭頂内溝 を介して背側前頭前皮質（PMd）へ. 把持に関連する情報を統合する（Davare ら, 2007; Davare ら,2010; Tunik ら, 2005）

最近では、これら 2 つの 副回路が 行動によって要求されるオンライン制御の程度に応じて相互作用することも発見されている (Grol et al., 2007, Verhagen et al., 2013)。

### 二段階モデル

<center>
<img src='/assets/2013Girshick_RCNN_Fig1.svg' style='width:74%'><br>
Girshick (2013) より
</center>

## 残差ネット (ResNet, He et. al, 2015)

<center>
<img src='/assets/ResNet_Fig2.svg' style='width:39%'><br>
<img src='/assets/2015ResNet30.svg' style='width:94%'><br>
He (2015) より
</center>


## Fast R-CNN と Faster R-CNN (2014)

<center>
<img src='/assets/2015Fast_R-CNN_Fig1.svg' style='width:74%'><br/>
Fast R-CNN
</center>

### 意味的切り分け (セマンティックセグメンテーション) と 実体切り分け (インスタンスセグメンテーション)

- 完全畳み込みネットワーク (Fully Convolutional Network:FCN) と呼ばれるセマンティックセグメンテーションを実現するネットワーク
- FCN とは文字通り全ての層が畳込み層であるモデル

<center>
<img src='/assets/2015Long_FCN.svg' style='width:94%'></br>
Long (2017) FCN
</center>

- 通常のCNN は，出力層のユニット数が識別すべきカテゴリー数であった。一方 FCN では入力画像の画素数だけ出力層が必要になる。
- すなわち各画素がそれぞれどのカテゴリーに属するのかを出力する必要があるため出力層には，縦画素数 $\times$ 横画素数 $\times$ カテゴリー数の出力ニューロンが用意される。
- 図 では，識別すべきカテゴリー数 が 20 であったたま，どのカテゴリーにも属さない，すなわち背景を指示するもう1 つのカテゴリーを加えた計 21 カテゴリーの分類を行うことになる。

- CNN では畳込演算によって畳込みのカーネル幅(受容野) だけ近傍の入力刺激を加えて計算することになるため，上位層では下位層に比べて受容野が大きくなることの影響で画像サイズは小さく(あるいは粗く) なってしまう
- このため，最終出力層に入力層と同じ解像度の画素数を得るためには，畳込みと反対方向の解像度を細かくする工夫が必要となる。
- これを解決する一つの方法がアンサンプリング(unsampling) と呼ばれる方法

### 意味的切り分け (セマンティックセグメンテーション)

* 意味的切り分け (セマンティックセグメンテーション) とは画像中の各画素をあるクラスに分類する画像解析課題のこと。
* 我々人間が常に行っていることと同じで，見ているものを画像と見なすと，画像の各画素がどのクラスに属しているかがわかる。
* 意味的切り出し (セマンティック・セグメンテーション semantic segmentation) はコンピュータでこれを実現するための技術である。

* セグメンテーションには他にもいくつかの種類がある。
詳しくは [こちら](https://www.learnopencv.com/image-segmentation/) 参照。
ここではセマンティック・セグメンテーションに焦点を当てる。

## セグメンテーションの応用
### 1. 自動運転

<center>
<img src="https://cdn-images-1.medium.com/max/1600/1*JKmS08bllQ8SCajIPyiBBQ.png" width="39%"><br/>
<small> Source: CityScapes Dataset </small>
</center>  

自律走行ではカメラから送られてくる画像を意味的に分割し，画像内の各画素をクラスに分類する。
これによりコンピュータは周囲に何があるのかを理解し，それに応じて自動車が行動できるようになる。


### 2. 顔セグメンテーション

<center>
<img src="https://i.ytimg.com/vi/vrvwfFej_r4/maxresdefault.jpg" width="39%"><br/>
<small> Source: https://github.com/massimomauro/FASSEG-repository/blob/master/papers/multiclass_face_segmentation_ICIP2015.pdf </small>
</center>

顔セグメンテーションは，唇や目など，顔の各部分をカテゴリーに分類するために使用されます。
この技術は性別の推定，年齢推定，顔の表情分析，感情分析など，様々な目的で使用される。

### 3. 室内物体セグメンテーション

<center>
<img src="https://cs.nyu.edu/~silberman/rmrc2014/header_semantic_segmentation.jpg" width="39%"><br/>
<small> Source: http://buildingparser.stanford.edu/dataset.html </small>
</center>

AR (拡張現実) や VR (仮想現実) などで用いられる。
AR は屋内全体をセグメントして，椅子やテーブル，人，壁，障害物などがどこにあるのかを把握するために必要な応用である。

### 4. ジオ・ランド・センシング

<center>
<img src="https://ars.els-cdn.com/content/image/1-s2.0-S0924271616305305-fx1_lrg.jpg" width="39%"><br/>
<small> Source: https://www.sciencedirect.com/science/article/pii/S0924271616305305 </small>
</center>

ジオ・ランド・センシングは衛星画像の各画素をカテゴリに分類し，各領域の土地被覆を追跡する方法である。
例えば，ある地域で森林破壊が進んでいるとすれば，適切な対策を講じることができる。
<!-- Geo Land Sensing is a way of categorizing each pixel in satellite images into a category such that we can track the land cover of each area. 
So, say in some area there is a heavy deforestation taking place then appropriate measures can be taken. -->

## U-Net 

画像分割の SOTA (State of the arts)

<center>
<img src="/assets/2015Ronneberger_U-Net_Fig1_ja.svg" style="width:66%"><br/>
Ronnenberger et. al (2015) Fig. 1 より
</center>

<!-- <img src="/assets/2014Friston_Fig1.svg" style="width:99%"><br/> -->
<!--  <img src="../assets/2009Friston_box3.svg" style="width:99%"><br/> -->

## 背骨 （バックボーン）ネットワーク と 周辺ネット

<center>
<img src="/assets/2017Lin_FPN_teaser_ja_b.svg" style="width:33%">
<img src="/assets/2017Lin_FPN_teaser_ja_c.svg" style="width:39%">
<img src="/assets/2017Lin_FPN_teaser_ja_d.svg" style="width:66%">
</center>

<!-- detectron2 の実習をしてみましょう。 -->


<center>
<iframe width="800" height="600" src="https://www.youtube.com/embed/pW6nZXeWlGM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
<!-- <iframe width="600" height="300" src="https://www.youtube.com/embed/pW6nZXeWlGM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen> -->
</iframe><br>
Realtime Multi-Person 2D Human Pose Estimation using Part Affinity Fields, CVPR 2017 Oral
</center>

---

<center>
<iframe width="800" height="600" src="https://www.youtube.com/embed/PCBTZh41Ris" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
<!-- <iframe width="800" height="600" src="https://www.youtube.com/embed/PCBTZh41Ris" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen> -->
</iframe><br>
論文: <https://arxiv.org/pdf/1808.07371.pdf><br>
プロジェクトサイト: <https://carolineec.github.io/everybody_dance_now/>
</center>

---

<center>
<img src="/2022assets/2007Patterson_HubFig2.png" width="66%"><br/>
<div style="text-align:left;width:88%;background-color:cornsilk">

図 2. 意味性認知症患者における意味課題の成績低下例。
この図は意味性認知症 (SD) における障害のクロスモーダルな性質と，特定情報に対する一般情報の相対的な保存を示す。
a. 健常対照者と軽度，中等度，重度の SD(72) 患者の 4 群における絵のカテゴリー化課題での目標刺激と妨害刺激の識別の正確さ。
参加者は，カテゴリーラベルとカラー写真を見て，その写真がラベルと一致しているかどうかを問われた。
ラベルは一般的なもの （例えば動物)，基本レベル （例えば犬)，具体的なもの (例えばラブラドール) のいずれかであった。
b. 縦断的に評価された 1 人の SD 患者の絵画命名反応(68)。+ は正しい反応を表す。
c. 2 つの認識課題における刺激と成績の例 (対照群，軽度および重度SD患者)。
最初の課題では，参加者は 2 つの項目のうちどちらの色が正しいかを判断した。
軽度の SD 患者は，対象がカテゴリーに典型的な色である場合 (例えば，緑のセロリ) には良い成績を示したが，対象が珍しい色である場合 (例えばオレンジ色のかぼちゃ) には悪い成績を示した。
より重度の SD 患者の判断は，いずれの条件でも偶然 (50％) より優れていなかった(80)。
2 番目の課題では，参加者は 2 枚の絵のうちどちらが本物の動物を描いているかを判断した。
ここでは，軽度の SD 患者も重度の SD 患者も，比較的原型的な特徴をもつ標的 (たとえば，多くの動物と同様に小さな耳をもつサル) に対しては，正常レベルの成功を収めた。
しかし，正しい選択肢に通常とは異なる特徴がある場合 (たとえば耳が非常に大きいゾウ)，軽度の SD 患者は障害を受け，重度のSD患者は偶然水準で得点した (70)。
d. SD 患者が作成した遅延模写絵画 (71)。
患者に模型の絵を見せ，それを取り除いてから 10 秒間の遅延の後，この絵を記憶から再現するよう求めた。
目や尻尾など，多くの動物に共通する性質は，遅延描画でも保持されていた。
ラクダのコブやアザラシのヒレなど，他の動物と区別するための特殊な性質は，しばしば省略された。
また，アヒルの 4 本足やカエルの尻尾のように，ある動物に共通する性質が誤って付け加えられることもあった。

<!-- Figure 2 | Examples of impaired performance on semantic tasks in patients with semantic dementia. 
This figure illustrates the cross-modal nature of the impairment and the preservation of general relative to specific information in semantic dementia (SD). 
a. Accuracy at discriminating targets from distractors in a picture-categorization task for four groups of participants: healthy controls and patients with mild, moderate and severe SD(72). 
Participants viewed a category label followed by a colour photograph and were asked whether the picture matched the label. 
Labels were either general (for example, ‘animal’), basic-level (for example, ‘dog’) or specific (for example, ‘Labrador’). 
b | Picture naming responses for one SD patient who was assessed longitudinally(68). 
+ denotes a correct response. 
c | Examples of stimuli and performance (for controls, mild and severe SD patients) on two recognition tasks. 
In the first task, participants judged which of two items was coloured correctly. 
Patients with milder SD performed well when the targets had a category-typical colour (for example, the green celery) but poorly when the items had an unusual colour (for example, the orange pumpkin). 
The judgements of patients with more severe SD were no better than chance (50%) in either condition(80). 
In the second task, participants judged which of two drawings depicted a real animal. 
Here, both the patients with mild SD and the patients with severe SD achieved normal levels of success for targets with relatively prototypical features (for example, the monkey which, like most animals, has small ears). 
For stimulus pairs in which the correct choice had unusual features (for example, the elephant, which has very large ears), the patients with mild SD were impaired and the patients with severe SD scored at chance levels70. 
d | Delayed-copy drawings produced by SD patients(71). 
The patients were shown a model picture which was then removed and, after a 10-second delay, they were asked to reproduce this picture from memory. 
Properties that are common to most animals, such as eyes and a tail, were preserved in the delayed drawings. 
Unusual properties that distinguish one animal from others — for example, the hump on the camel and the flippers on the seal — were frequently omitted. Some common properties were also incorrectly added to animals that lack them (for example, the four legs on the delayed drawing of the duck and the tail on the delayed drawing of the frog).  -->
</div>
</center>


# 実習ファイル

* [Olivetti 顔データを用いた簡単な CNN <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_1112Olivetti_CNN.ipynb#scrollTo=YJZrdGnR4Sr7){:target="_blank"}

* [最小限のニューラルネットワーク <img src="/assets/colab_icon.svg" alt="最小限のニューラルネットワーク">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_0929miniam_XOR.ipynb){:target="_blank"}
* [画像認識モデル実習 <img src="/assets/colab_icon.svg" alt="画像認識モデル実習">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021komazawa_cogsy000_CNN_demo.ipynb#scrollTo=3LVOKnq2NuPj){:target="_blank"}
* [顔検出 <img src="/assets/colab_icon.svg" alt="顔検出">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2025notebooks/2025_0428opencv_face_detect_recognizer.ipynb){:target="_blank"}

* [畳み込みニューラルネットワークの事前訓練済モデルによる中間表現の可視化 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_1024CNN_layer_visualization.ipynb){:target="_blank"}
- [LeNet PyTorch <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0528LeNet_pytorch.ipynb){:target="_blank"}
* [特徴点検出アルゴリズム 画像フィルタ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2020Sight_visit_feature_extractions_demo.ipynb){:target="_blank"}
* [DOG などのフィルタと Harr 特徴による顔検出 a.k.a ビオラ＝ジョーンズ アルゴリズム <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0528edge_and_face_detection_algorithm_not_cnn.ipynb){:target="_blank"}


## デモ

- [グーグルによるニューラルネットワークの遊び場 (プレイグランド)](https://project-ccap.github.io/tensorflow-playground/){:target="_blank"}

---

<center>
<img src="/2023assets/xor.svg">
<img src="/2023assets/xor-graph.svg">
</center>

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



## 従来モデルと深層学習との対比

<div class="figcenter">
<img src='/assets/2013LeCun-tutorial-icml_15.svg' style="width:66%"><br/>

LeCun (2013)
</div>

我々人間は，外界を認識するために必要な計算を，生物種としての発生の過程と，個人の発達を通しての経験に基づく認識系を保持していると見ることができる。
従って我々の視覚認識には化石時代に始まる光の受容器としての眼の進化の歴史と発達を通じた個人の視覚経験が反映された結果でもある。
人工知能の目標は，この複雑な特徴検出過程をどうやったらコンピュータが獲得できるかということでもある。
外界を認識するために今日まで考案されてきたモデル（例えば，ニューラルネットワーク，サポートベクターマシンなどは）は複雑である。
だが，モデルを訓練するための学習方法はそれほど難しくない。
この意味で画像認識課題が正しく動作するためのポイントは，認識系が問題を解く事が可能なほど複雑であるかどうかではなく，十分に複雑が視覚環境，すなわち画像認識の場合，外部の艦橋を反映するために十分な量の像データを容易すことができるか否かにある。
今日の CNN による画像認識性能の向上は，簡単な計算方法を用いて複雑な外部環境に適応できる認識系を構築する方法が確立したからであると言うことが可能であろう。

下図 <!--[fig:2012Ng_01](#fig:2012Ng_01){reference-type="ref"reference="fig:2012Ng_01"} -->
に画像処理の例を挙げた。

<center>
<img src="/assets/2012Ng_ML_and_AI_01.png" style="width:66%">
</center>

## Sutton のブログより

<center>
<div style="text-align: left;width: 88%;background-color: powderblue;">
人工知能の長年の目標は，困難な領域でも超人的な能力をタブラ・ラサ方式で学習するアルゴリズムである。
最近では AlphaGo が囲碁の世界チャンピオンを破った初めてのプログラムとなった。
AlphaGo の木探索は，深層ニューラルネットワークを用いて局面の評価と手の選択を行う。
このニューラルネットワークは，人間の熟練した手からの教師付き学習と， 自分自身の競技からの強化学習によって訓練されている。
ここでは，人間のデータやガイダンス，ゲームルール以外の領域の知識を必要としない，強化学習のみに基づいたアルゴリズムを導入する。
AlphaGo は自分自身の教師となり AlphaGo 自身の手の選択や AlphaGo のゲームの勝敗を予測するようにニューラルネットワークが学習される。
このニューラルネットワークは，木探索の強度を向上させ，その結果，より質の高い手の選択が可能となり，次の反復ではより強力な自己対戦が可能となる。
タブララサからスタートした私たちの新しいプログラム AlphaGo Zero は，既発表のチャンピオンに敗れた AlphaGo に対して 100-0 で勝利するという超人的な成績を達成した。
</div>
</center>

* [David Silver homepage](https://www.davidsilver.uk/){:target="_blank"}

1. [計算論的認知神経科学 Kriegeskorte and Douglas, 2018, Cognitive computational neuroscience](https://project-ccap.github.io/2018Kriegeskorte_Douglas_Cognitive_Computational_Neuroscience.pdf){:target="_blank"}
1. [視覚系の畳み込みニューラルネットワークモデル，過去現在未来 Lindsay, 2020, Convolutional Neural Networks as a Model of the Visual System: Past, Present, and Future](https://project-ccap.github.io/2020Lindsay_Convolutional_Neural_Networks_as_a_Model_of_the_Visual_System_Past_Present_and_Future.pdf){:target="_blank"}
1. [計算論的視覚と正則化理論 Poggio, Torre, Koch, 1985](https://komazawa-deep-learning.github.io/2021cogpsy/1985Poggio_Computational_Vision_and_Regularization_Theory.pdf){:target="_blank"}
1. [皮質における物体認識の階層モデル Riesenhuber and Poggio (1999) Nature](https://komazawa-deep-learning.github.io/2021cogpsy/1999Riesenhuber_Poggio_Hierarchical_models_of_object_recognition_in_cortex.pdf){:target="_blank"}




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

