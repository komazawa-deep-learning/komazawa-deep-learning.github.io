---
title: "第08回 2024年度開講 駒澤大学 認知心理学研究"
author: "浅川 伸一"
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="right">
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 15/Nov/2024<br/>
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

