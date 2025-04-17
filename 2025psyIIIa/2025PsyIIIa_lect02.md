---
title: 第01回 2025 年度開講 駒澤大学 心理学特講 IIIA
author: 浅川 伸一
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">
<div align="center">
<font size="+1" color="navy"><strong>ディープラーニングの心理学的解釈</strong></font><br/><br/>
</div>

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 18/Apr/2025<br/>
Appache 2.0 license<br/>
</div>

# 実習

- [ロジスティック回帰実習 オリベッティ顔データベース <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_0419Logistic_regression_of_Olivetti_face_dataset.ipynb){:target="_blank"}
- [課題提出用 Google ドライブフォルダ](https://drive.google.com/drive/u/5/folders/1UMly9H3WvHX-VewKX9XvDJs-xT6P2bYu){:target="_blank"}

<!-- - [はじめての colab による画像認識 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021komazawa_cogsy000_CNN_demo.ipynb){:target="_blank"}
- [画像処理における特徴量抽出 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2020Sight_visit_feature_extractions_demo.ipynb){:target="_blank"}
- [DOG 等エッジ検出と顔検出の従来手法 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0528edge_and_face_detection_algorithm_not_cnn.ipynb){:target="_blank"} -->

# 歴史的背景

カハール Cajal ゴルジ染色

* 1891年 (明治 24 年) カハールが神経細胞の構造を発見。日清戦争 (1894-1895, 明治 27-28 年)
* 1906年 (明治 39 年) ゴルジとカハールがノーベル生理学賞を受賞。 日露戦争 (1904-1905, 明治 37-38 年)

**[カハール (Santiago Ramón y Cajal)](https://ja.wikipedia.org/wiki/%E3%82%B5%E3%83%B3%E3%83%86%E3%82%A3%E3%82%A2%E3%82%B4%E3%83%BB%E3%83%A9%E3%83%A2%E3%83%B3%E3%83%BB%E3%82%A4%E3%83%BB%E3%82%AB%E3%83%8F%E3%83%BC%E3%83%AB)**:
スペインの神経科学者・組織学者。ニューロン説を提唱し、神経細胞が独立した単位であることを示した。この説は現在の神経科学の基礎を築くものとなった。<br/>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Santiago_Ram%C3%B3n_y_Cajal_%281852-1934%29_portrait_%28restored%29.jpg/500px-Santiago_Ram%C3%B3n_y_Cajal_%281852-1934%29_portrait_%28restored%29.jpg" style="width:14%"><br/>


**[ゴルジ (Camillo Golgi)](https://bsd.neuroinf.jp/wiki/%E3%82%B4%E3%83%AB%E3%82%B8%E6%9F%93%E8%89%B2){:target="_blank"}**:
イタリアの内科医・病理学者。ゴルジ染色法を開発。この方法は、神経細胞の微細構造を可視化する上で重要な役割を果たし、カハールのニューロン説の研究に大きく貢献した。<br/>
<img src="https://bsd.neuroinf.jp/w/images/c/cf/Golgi1.png" style="width:14%"><br/>

心理学史としては，ブント (Wundt) 1879 年 (明治 12 年) に心理学実験室を開設。ブントの師匠はヘルムホルツ (Hermann von Helmholtz)。


# 第 1 次ニューロブーム

## 1950年代:
- ウォーレン・マッカロックとワイルダー・ピッツによる **形式ニューロン** の提案
(サイバネティクスの創始者ノーバート・ウィーナーの集めた研究者集団)

<div class="figcenter">
<img src="/assets/mcculloch.jpg" style="width:38%">
<img src="/assets/pitts.jpg" style='width:50%'><br>
ウォーレン・マッカロック と ワイルダー・ピッツ<br>
</div>

形式ニューロンは，シナプス結合荷重ベクトルと出力を決定するための伝達関数とで構成される(次式)

$$\tag{eq:formal_neuron}
y_i=\phi\left(\sum_jw_{ij}x_j\right),
$$

ここで $y_i$ は $i$ 番目のニューロンの出力，$x_j$ は $j$ 番目のニューロンの出力，$w_{ij}$ はニューロン $i$ と
$j$ との間の **シナプス結合荷重**。
$\phi$ は活性化関数。

<div class="figcenter">
<img src="/assets/Formal_r.svg" style="width:84%"><br/>
形式ニューロン
</div>


<div class="figcenter">
<img src="/assets//Neuron_Hand-tuned.png" style="width:69%"><br/>
ニューロンの模式図 wikipedia より
</div>

# 用語の整理

* 人工知能 Artificial Intelligence: AI
* ニューラルネットワーク Neural Networks: NN
* ディープラーニング (深層学習) Deep Learning: DL
* データサイエンス Data Science: **データサイエンティストは 21 世紀で最もカッコいい (the sexist) 職業だ** というハーバードビジネスレビューの [ポジショントーク記事 (2012年)](https://hbr.org/2012/10/data-scientist-the-sexiest-job-of-the-21st-century) が話題になって久しい。
* ビッグデータ Big Data: こちらも[ポジショントークらしく学術論文は存在しない](https://bits.blogs.nytimes.com/2013/02/01/the-origins-of-big-data-an-etymological-detective-story/)。
ただし [データが増え続けている](http://www.uvm.edu/pdodds/files/papers/others/2011/hilbert2011a.pdf) ことは事実なので社会的な傾向とも言える。



