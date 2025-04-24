---
title: 第02回 2025 年度開講 駒澤大学 心理学特講 IIIA
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

- [はじめての colab による画像認識 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021komazawa_cogsy000_CNN_demo.ipynb){:target="_blank"}
- [ロジスティック回帰実習 オリベッティ顔データベース <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_0419Logistic_regression_of_Olivetti_face_dataset.ipynb){:target="_blank"}

- [課題提出用 Google ドライブフォルダ](https://drive.google.com/drive/u/5/folders/1UMly9H3WvHX-VewKX9XvDJs-xT6P2bYu){:target="_blank"}


# 取り上げる話題

* 相貌失認
* 販促空間無視
* ストループ効果
* 談話

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

$$
y_{i}=\phi\left(\sum_jw_{ij}x_{j}\right),
$$\tag{eq:formal_neuron}

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


# 2. ヒューベルとウィーゼルによる視覚野の生理学研究

<center>
<img src="/assets/1968Hubel_Wiesel_1.svg" style="width:74%"><br/>
Hubel と Wiesel(1959, 1962, 1968)の実験の模式図

<img src="/assets/1968Hubel_Wiesel_2.svg" style="width:74%"><br/>
Hubel と Wiesel の実験結果 (Hubel & Wiesel, 1968 の Fig.2.7 をトレーシングしたもの)
</center>




# ヒューベルとウィーゼル Hubel and Wiesel (1969)
<center>
<iframe width="1024" height="768" src="https://www.youtube.com/embed/4nwpU7GFYe8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br/> 
<!-- <iframe width="450" height="300" src="https://www.youtube.com/embed/4nwpU7GFYe8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br/>  -->
source: https://youtu.be/4nwpU7GFYe8
</center>

- トポグラフックマッピング topographic mappings (地形図):  網膜や皮膚などの体制感覚，筋肉系のような効果器系を、中枢神経系の 1 つ以上の構造物に整然と投影した地図。
地形図は、すべての感覚系と多くの運動系で観察される。
- トノトピー tonotopy（ギリシャ語のtono=周波数、topos=場所）とは、異なる周波数の音が脳内で処理される場所の空間的配置のこと。
周波数が近い音は、脳内の場所的に隣接する領域で表現される。トノトピック地図とも呼ばれる <!--は 視覚系のレチノトピーに似た地形的な組織の特殊な例である。-->
- ソマトピー somatopy: 中枢神経系上の特定の点へ身体領域の照射，投影のこと。 身体領域は 第一次体性感覚皮質 (後腹回) に投影される。 典型的には 特定の身体部位と そのそれぞれの位置を ホムンクルス homunclus (小人)
 上に配置する 感覚ホムンクルスとして表現される。
 細かく制御されている部位 (指，舌) は体性感覚野の面積が大きい。一方 粗く制御されている部位 (体幹) は面積が小さい。内臓のような領域は体性感覚野の位置を持たない。
- レティノトピー retinotopy: 網膜からの視覚入力を神経細胞 にマッピングすること。哺乳類の脳に多く見られる。
この地図の大きさ、数、空間的配置は種間で異なる。
視野の隣接する点 が 同じ領域 の 隣接する 領域で 表現される とは限らないという意味で、複雑な地図となる。
例えば 第 2 次視覚野 (V2) での視覚地図は 視野の上半分に応答する網膜の部分が 視野の下半分に応答する部分から分離されて表現されている。
第３次視覚野 (V3) や 第4次視覚野 (V4) では下位の視覚野に比べて より複雑な表現がなされている


## ブレイクモア と クーパー Blackmore and Cooper (1970)

<center>
<iframe width="1024" height="768" src="https://www.youtube.com/embed/QzkMo45pcUo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<!-- <iframe width="450" height="300" src="https://www.youtube.com/embed/QzkMo45pcUo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> -->
<!--<iframe width="845" height="676" src="https://www.youtube.com/embed/QzkMo45pcUo" frameborder="0"
 allow="ac
celerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>-->
<br/>
source:` https://youtu.be/QzkMo45pcUo`
</center>

<center>
<img src='/assets/1970BlackmoreCooper_Fig1.svg' style='width:39%'>
<img src='/assets/1970BlackmoreCooper_Fig2.svg' style='width:49%'>
</center>


<center>
<iframe width="1024" height="768" src="https://www.youtube.com/embed/RSNofraG8ZE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br/>
<!-- <iframe width="450" height="300" src="https://www.youtube.com/embed/RSNofraG8ZE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br/> -->
source: https://youtu.be/RSNofraG8ZE
</center>


# 心理学的対応

## セルフリッジ (Selfridge) のパンデモニウム (pandemonium) モデル

<center>
<img src="/assets/1958Selfridge_fig3.svg" style="width:74%"><br>
セルフリッジ (1958) ``Mechanisation of Thought Processes'' より

<img src="/assets/1958Selfridge_fig7.svg" style="width:84%"><br>
セルフリッジ (1958) ``Mechanisation of Thought Processes'' より
</center>


<!-- <center>
<img src='../assets/1958Selfridge_fig4.svg' style='width:49%'><br>
<img src='../assets/1958Selfridge_fig5.svg' style='width:74%'><br>
<img src='../assets/1958Selfridge_fig6.svg' style='width:49%'><br>
セルフリッジ (1958) ``Mechanisation of Thought Processes'' より
</center> -->

# 生理学，視覚心理学との対応

- Julesz(1981) Textons, the elements of texture perception, and their interactions, Nature

<center>
<img src="/assets/1981Julesz-texton-Fig2.svg" style="width:84%"><br/>
Julesz (1981) Fig. 2 より
</center>


## 生理学との対応 (Hubel and Wiesel のネコとサル, Blackmore のネコ, ヴァンエッセン)

- 層間の結合の仕方, アーキテクチャ
- forward/backward 役割，機能，実現方法
- 側抑制 lateral inhibition (これについては多層化して回避できる可能性あり)
- shape from X は正しかったのか？ ただし発達心理学におけるシェイプバアスは言語発達において重要な意味を持つはず。
だからと言って乳幼児はそのように強制(脅迫？)，矯正されて育つわけではないだろう。

    - Ritter (2017) Cognitive Psychology for Deep Neural Networks: A Shape Bias Case Study
    - Landau, Smith, Jones (1992) Syntactic Context and the Shape Bias in Childrens and Adults Lexical Learning
    - Yamins (2016) Using goal-driven deep learning models to understand sensory cortex

    - Julez のアプローチは視覚研究者 Haar, SIFT, DoG などのアルゴリズム開発者と対応
    - Poggio (1985) Computational Vision and Regularization Theory


## ローゼンブラット Rosenblatt のパーセプトロン

<center>
<img src='/assets/rosenblatt.jpg' style="width:29%">
<img src='/assets//perceptron.png' style="width:66%"><br/>

左: フランク・ローゼンブラット。
右: パーセプトロンの模式図。ミンスキーとパパート「パーセプトロン」より
</center>

<!--
$$\mathbf{w}\leftarrow\mathbf{w}+\left(y-\hat{y}\right)\mathbf{x}$$
-->


<center>
<img src='/assets//Neuron_Hand-tuned.png' style="width:44%">
<img src='/assets/neuron_model.jpeg' style="width:44%"><br/>

左: ニューロンの模式図 wikipedia より。
右: 左と等価なニューロンの表現
<!-- <img src='/assets/neuron.png' style="width:49%"><br/> -->
</center>


## パーセプトロンの学習

$$
\mathbf{w}\leftarrow\mathbf{w}+\left(y-\hat{y}\right)\mathbf{x}
$$
パーセプトロン perceptron は 3 層の階層型ネットワークでそれぞれ S(sensory layer), A(associative layer), R(response layer) と呼ぶ。
$S\rightarrow A \rightarrow R$ のうち パーセプトロンの本質的な部分は $A\rightarrow R$ の間の学習にある。

入力パターンに $P^+$ と $P^-$ とがある。
パーセプトロンは $P^+$ が入力されたとき $1$, $P^-$ のとき $0$ を出力する
パーセプトロンは $P^+$ が入力されたとき $1$, $P^-$ のとき $0$ を出力する
機械である。
出力層($R$) の $i$ 番目のニューロンへの入力(膜電位の変化) $u_i$は
$$
u_{i} = \sum_{j} w_{ij}x_j - \theta_i = \left(w\right)_i\cdot\left(x\right)_i-\theta_i.
$$
ここで中間層($A$)の $j$ 番目のニューロンの出力 $y_i$とこのニューロンとの
結合係数を$w_{ij}$、しきい値を$\theta_i$ とした。
このニューロンの出力$y_i$(活動電位、スパイク) 次式で表される:

$$
\left\{\begin{align}
1 & & \mbox{ if $u_i \ge 0$,}\\
0 & & \mbox{ otherwize }\end{align}\right\}
$$



$$
y_i = \lceil u_i\rceil
\qquad\left\{
\begin{array}{ll}
 1 & \mbox{if $u_i \ge 0$,}\\
 0 & \mbox{otherwize}
\end{array} \right.
$$



<!-- 式(\ref{eq1})の意味を理解するために以下の図を参照

\footnote{
Minsky and Papert はパーセプトロンのベクトル表示について
悲観的な考え方を持っているようですが、ここでは理解のしやすさを
優先します。}%
$$
\mathbf{w}\rightarrow\mathbf{w}+\left(y-\hat{y}\right)\mathbf{x}
$$
 -->


# 用語の整理

* 人工知能 Artificial Intelligence: AI
* ニューラルネットワーク Neural Networks: NN
* ディープラーニング (深層学習) Deep Learning: DL
* データサイエンス Data Science: **データサイエンティストは 21 世紀で最もカッコいい (the sexist) 職業だ** というハーバードビジネスレビューの [ポジショントーク記事 (2012年)](https://hbr.org/2012/10/data-scientist-the-sexiest-job-of-the-21st-century) が話題になって久しい。
* ビッグデータ Big Data: こちらも[ポジショントークらしく学術論文は存在しない](https://bits.blogs.nytimes.com/2013/02/01/the-origins-of-big-data-an-etymological-detective-story/)。
ただし [データが増え続けている](http://www.uvm.edu/pdodds/files/papers/others/2011/hilbert2011a.pdf) ことは事実なので社会的な傾向とも言える。
