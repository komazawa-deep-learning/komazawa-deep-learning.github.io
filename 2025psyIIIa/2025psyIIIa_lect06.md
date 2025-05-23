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

<!-- Transfer learning の話をして, BIT シミュレーションを紹介する予定 -->

* 連絡事項： 5 月 30 日 は休講。
* [課題提出用フォルダ<img src="/2025assets/Google_Drive_icon_2020.svg" style="width:02%">](https://drive.google.com/drive/u/3/folders/1EdOL_Wz1656fWqD0RmmKgLmf_fUsl2QY){:target="_blank"}

---

* [BIT 線分二等分線試作機 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_1210bit_line_bisection.ipynb#scrollTo=UDyOZj1LLnX8){:target="_blank"}
* [2022_0604bit_faster-rcnn_fine_tuning.ipynb <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/bit/blob/main/notebooks/2022_0617bit_faster_rcnn_fine_tuning.ipynb#scrollTo=D1v9Zb5hOzsl){:target="_blank"}



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

