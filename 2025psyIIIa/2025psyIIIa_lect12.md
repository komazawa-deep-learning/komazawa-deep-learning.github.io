---
title: 第12回 2025 年度開講 駒澤大学 心理学特講 IIIA
author: 浅川 伸一
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="center">
<font size="+2" color="navy"><strong>ディープラーニングの心理学的解釈</strong></font><br/><br/>
</div>

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br/>
Date: 11/Jul./2025<br/>
Appache 2.0 license<br/>
</div>

* [課題提出用フォルダ](https://drive.google.com/drive/u/3/folders/1w70ys8I6HejtPlmHgkwB_O4aKvk_eTH1){:target="_blank"}

# 第 12 回

* [文字音読モデル <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2025notebooks/2025_0626psylex71_CDP%2Bja1.ipynb){:target="_blank"}
* [百人一首の上の句とエンコーダによって符号化し，下の句をデコーダで生成する自作 Transformer モデル <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2023notebooks/2023_1113chihaya_Transformer.ipynb){:target="_blank"}


<!-- <center>
<img src="http://www.newscientist.com/wp-content/uploads/2003/03/dn3488-1_602.jpg" width="49%"><br/>
</center> -->

## 先週の補足 意味ベクトルの応用例

<center>
<img src="/assets/2008Mitchell_fig1ja.svg" style="width:77%"><br/>
Mitchell et al (2008) Fig. 1 を改変
</center>


<center>
<img src="/assets/2019Jat_Mitchell_fig1.svg" style="width:74%;"><br/>
<img src="/assets/2019Jat_Mitchell_fig4.svg" style="width:84%"><br/>
</center>

<div class="figcaption">
上：MEG データの符号化モデル。1  単語あたり 306 チャンネルで  500ms 間の MEG 信号は、100ms 区間のデータを平均して 306x5 に圧縮された。この MEG 脳記録データは、リッジ回帰を用いてテキスト表現ベクトルから脳活動に符号化された。評価は  5 交差検証を用いて行われた。<br/>
下: いくつかの選択された深層ニューラルネットワークモデル層からのさまざまな脳領域対ごとの精度。言語理解の中心と考えられている脳の左側が、特に左側頭葉で高い精度で予測されている。（L = 左、R = 右）
</div>

### NIC (Neural Caption Generation)

<center>
<img src="/assets//17VISIOn-slide-WBE2-jumbo.jpg" width="49%"><br/>
- 人間: A group of men playing Frisbee in the park.
- 機械: A group of young people playing a game of Frisbee.
</center>

<img src="/assets/2014Vinyals_Fig5_left.jpg" width="44%">
<img src="/assets/2014Vinyals_Fig5_right.jpg" width="44%"><br/>
Vinyals et. al (2014) より

### 画像生成技術 GAN, VAE, etc

<center>
<img src="/assets/Tenn_deepdream.jpg" width="88%"><br/>
天安門前広場の夢 (撮影は自民解放軍の兵士に依頼した)
</center>
<!--![天安門前広場の夢(撮影は自民解放軍の兵士に依頼した)](https://komazawa-deep-learning.github.io/assets/Tenn_deepdream.jpg){#fig:deep_dream style="width:49%"}-->

#### GAN 

<center>
<img src="/assets/2016Reed_GAN_Text2Image1.svg" style="width:84%"><br>
Generative Adversarial Text to Image Synthesis <arXiv:1605.05396v2>
</center>

<center>
<img src="/assets/2016Reed_GAN_Text2Image.svg" style="width:84%"><br>
Generative Adversarial Text to Image Synthesis arXiv:1605.05396v2
</center>

---

<!-- - 2016 アメリカ合州国大統領候補の一人の発言を模倣する「ディープトランプ」がツィッター上で注目を集める -->

<center>
<img src="/assets//DeepTrumpf.jpg" style="width:39%">
<img src="/assets//DeepTrumpf2.png" style="width:59%"><br>
<img src="/assets/DeepTrumpfTweet.png" style="width:99%"></br>
</center>


## フェイク画像の生成

<div align="center">
<img src="/assets/2018Chen_CartoonGAN.svg" style="width:94%">
</div>


<center>
<iframe width="480" height="300" src="https://www.youtube.com/embed/o46fcRl2yxE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

<div align="center">
<!--<iframe width="805" height="453" src="https://www.youtube.com/embed/G06dEcZ-QTg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>-->
<iframe width="480" height="300" src="https://www.youtube.com/embed/G06dEcZ-QTg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
source: <https://youtu.be/G06dEcZ-QTg>
</div>
