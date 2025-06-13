---
title: 第07回 2025 年度開講 駒澤大学 心理学特講 IIIA
author: 浅川 伸一
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">
<div align="center">
<font size="+1" color="navy"><strong>ディープラーニングの心理学的解釈</strong></font><br/><br/>
</div>

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 06/Jun/2025<br/>
Appache 2.0 license<br/>
</div>

<!-- Transfer learning の話をして, BIT シミュレーションを紹介する予定 -->

* [課題提出用フォルダ<img src="/2025assets/Google_Drive_icon_2020.svg" style="width:02%">](https://drive.google.com/drive/folders/1S_gz5J2NmuLcrIiLxUOoEaphpfD1e8IF?usp=drive_link){:target="_blank"}

# 実習ファイル

* [DETR と Detectron2 とによる領域切り出しデモ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_0625DETR_demo.ipynb){:target="_blank"}


## 画像切り出し

1. 物体位置
3. 物体認識 object recognition
2. 意味的切り出し semantic segmentation
4. 対象切り出し instance segmentation
5. 特徴点抽出 keypoint
6. パノプティック切り出し

<div align="center">
<img src="/assets/2017DangHa_History_Of_Object_Recognition_ja.svg" style="width:66%"><br/>
Dang and Ha (2017) より
</div>

<!-- # 転移学習

<div align="center" style="width:29%">
<img src="/assets/2017Li_Deeper_Broader_fig1ja.svg" style="width:84%"><br/>
</div> -->

### 残差ネット (ResNet, He et. al, 2015)

<center>
<img src='/assets/ResNet_Fig2.svg' style='width:19%'>
<img src='/assets/2015ResNet30.svg' style='width:66%'><br>
He (2015) より
</center>

### Fast R-CNN と Faster R-CNN (2014)

- R-CNN によって，位置 where 情報と 物体 what 情報 とを多層畳み込みニューラルネットワークで表現する試みが，発展。実時間で物体の切り出しと認識とが行えるようになった。[Faster R-CNN](https://arxiv.org/pdf/1506.01497.pdf){:target="_blank"}, [YOLO](https://arxiv.org/pdf/1506.02640.pdf){:target="_blank"}, [SSD](https://arxiv.org/pdf/1512.02325.pdf){:target="_blank"},

<center>
<img src="/assets/2015Fast_R-CNN_Fig1.svg" width="49%">
<img src="/assets/2015Faster_RCNN_RPN.svg" width="44%"><br/>
左: Fast R-CNN の模式図。
右: Faster RCNN の領域提案ネットワーク
</center>

### 意味的切り分け (セマンティックセグメンテーション) と 実体切り分け (インスタンスセグメンテーション)

- 完全畳み込みネットワーク (Fully Convolutional Network:FCN) と呼ばれるセマンティックセグメンテーションを実現するネットワーク
- FCN とは文字通り全ての層が畳込み層であるモデル

<center>
<img src='/assets/2015Long_FCN.svg' style='width:49%'><br/>
Long (2017) FCN
</center>

- 通常のCNN は，出力層のユニット数が識別すべきカテゴリー数であった。一方 FCN では入力画像の画素数だけ出力層が必要になる。
- すなわち各画素がそれぞれどのカテゴリーに属するのかを出力する必要があるため出力層には，縦画素数 $\times$ 横画素数 $\times$ カテゴリー数の出力ニューロンが用意される。
- 図 では，識別すべきカテゴリー数 が 20 であったたま，どのカテゴリーにも属さない，すなわち背景を指示するもう1 つのカテゴリーを加えた計 21 カテゴリーの分類を行うことになる。

- CNN では畳込演算によって畳込みのカーネル幅(受容野) だけ近傍の入力刺激を加えて計算することになるため，上位層では下位層に比べて受容野が大きくなることの影響で画像サイズは小さく(あるいは粗く) なってしまう
- このため，最終出力層に入力層と同じ解像度の画素数を得るためには，畳込みと反対方向の解像度を細かくする工夫が必要となる。
- これを解決する一つの方法がアンサンプリング(unsampling) と呼ばれる方法

<!-- ### 意味的切り分け (セマンティックセグメンテーション)

* 意味的切り分け (セマンティックセグメンテーション) とは画像中の各画素をあるクラスに分類する画像解析課題のこと。
* 我々人間が常に行っていることと同じで，見ているものを画像と見なすと，画像の各画素がどのクラスに属しているかがわかる。
* 意味的切り出し (セマンティック・セグメンテーション semantic segmentation) はコンピュータでこれを実現するための技術である。 -->

### 姿勢検出 key point detection

<center>
<div style="width:77%">
<video controls src="https://learnopencv.com/wp-content/uploads/2022/10/yolov7-vs-mediapipe-dance.mp4" muted="false" style="width:77%"></video><br/>
<br/><br/>
<video controls src="https://learnopencv.com/wp-content/uploads/2022/10/yolov7-gpu-vs-mediapipe-difficult-pose.mp4" muted="true" style="width:77%"></video>
<!-- <video controls src="https://learnopencv.com/wp-content/uploads/2022/10/yolov7-256-vs-960p-yoga-1.mp4" muted="false"></video> -->
<div class="figcaption">
from `https://learnopencv.com/yolov7-pose-vs-mediapipe-in-human-pose-estimation/`
</div></div>
</center>

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

