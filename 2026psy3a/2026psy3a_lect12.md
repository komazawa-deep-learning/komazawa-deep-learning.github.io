---
title: 第 12 回 2026 年度開講 心理学特講 IIIA 駒澤大学 
author: 浅川 伸一
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="center">
<font size="+1" color="navy"><strong>計算モデルによる課題の理解：認知課題から神経心理学検査への適用</strong></font><br/><br/>
</div>

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 10/Jul/2026<br/>
Appache 2.0 license<br/>
</div>

# 07440 心理学特講ⅢA - 第 12 回

* [課題提出フォルダ](https://drive.google.com/drive/u/6/folders/1wYaBn4dovEwtlOfOhcAFP2bJdyDqM9ZL){:target="_b  lank"}

* [Karapetian+(2023) demo 1 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_115Karapetian_demo.ipynb){:target="_blank"}
* [Karapetian+(2023) demo 2 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_1220Karapetian_demo.ipynb){:target="_blank"}
* [ResNet 実習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_0603ResNet_with_Olivetti_faces_.ipynb){:target="_blank"}
* [実習 LeNet PyTorch 版 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0528LeNet_pytorch.ipynb){:target="_blank"}


## 心・脳・行動を結びつける枠組み (Bahg et al.2020 Fig.1)

<div class="figcenter">
<img src="/2025assets/2020Bahg_GP_fig1.svg" style="width:66%;">
</div>
<div class="figcaption" style="width:77%;">

**出典: Bahg et al.2020 Fig.1 心、脳、行動を結びつける枠組み**<br>
実験情報と構造情報に基づいて脳機能の生成モデルの構造を規定する、同時モデルの枠組みの概略図。
この生成モデルは、反応時間、血中酸素濃度依存反応、脳波活動など、利用可能なすべての顕在変数を共同で説明するために使用される。
<!-- 本稿では、潜在ガウス過程を用いて顕在変数を関連付け、モデルをデータに当てはめる際に最も妥当な関連付け関数を導き出すことを可能にする。 -->
<!-- Fig. 1. Framework for connecting mind, brain, and behavior. 
Shown is a schematic of the joint modeling framework, where experimental information and structural information specify the structure of a generative model of brain function. 
The generative model is used to jointly explain all available manifest variables such as response times, blood oxygenated level-dependent response, or electroencephalogram activity. 
In the present article, a latent Gaussian process is used to link the manifest variables, enabling the most plausible linking function to emerge from fitting the model to data. -->
</div>

# Glaser(2019) の 教師あり機械学習の 4 つのレベル

<!-- <div class="figure figcenter">
<img src="figures/2019Glaser_fig2.jpg" width="49%">
<div class="figcaption" style="width:44%">

Glaser+2019 による，機械学習の 4 レベル
[Glaser+2019](https://www.sciencedirect.com/science/article/abs/pii/S0301008218300856?via%3Dihub) Fig. 2 より
</div></div>-->

<div class="figcenter">
<img src="/assets/2019Glaser_fig2.jpg" style="width:74%;align:center;">
</div>

1. 工学的な問題の解決: 機械学習は，医療診断，ブレインコンピュータインターフェース，研究ツールなど，神経科学者が使用する手法の予測性能を向上させることができる。
2. 予測可能な変数の特定: 機械学習により，脳や外界に関連する変数がお互いを予測しているかどうかをより正確に判断することができる。
3. 単純なモデルのベンチマーク: 解釈可能な簡易モデルと精度の高い ML モデルの性能を比較することで，簡易モデルの良し悪しを判断するのに役立つ。
4. 脳のモデルとしての役割: 脳が機械学習システム，例えばディープニューラルネットワークと同様の方法で問題を解決しているかどうかを論じることができる。

[Glaser+2019](https://www.sciencedirect.com/science/article/abs/pii/S0301008218300856?via%3Dihub) Fig. 2 より

* N400 への PDP approach:
  * [Laszlo&Plaut (2011) Simulating Event-Related Potential Reading Data in a Neurally Plausible Parallel Distributed Processing Model](https://ni.cmu.edu/~plaut/paper
s/pdf/LaszloPlaut11CogSciConf.ERPmodel.pdf){:target="_blank"}
<!-- /Users/_asakawa/study/2022documents/2011LaszloPlaut_CogSciConf_ERPmodel.pdf){:target="_blank"} -->
  * [Laszlo, S., & Federmeier, K.D. (2009). A beautiful day in the neighborhood: An event-related potential study of lexical relationships and prediction in context](h
ttps://www.sciencedirect.com/science/article/pii/S0749596X09000692){:target="_blank"}. Journal of Memory and Language, 61, 326-338.



#### [Karapetian+(2023) 人間の情景分類における脳と行動の関係の実証的特定と計算モデル, Empirically Identifying and Computationally Modeling the Brain–Behavior Relationship for Human Scene Categorization](https://doi.org/10.1162/jocn_a_02043){:target="_blank"}

<div class="abstract">

ヒトは，自分が直面している情景のカテゴリーなど，身近な視覚環境の性質について，早くて正確な知覚判断を難なく下している。これまでの研究で，このような特性の基礎となる皮質表現が豊富にあることが明らかになっている。
しかし，これらの表象のうち，どの表象が意思決定に適しているかはまだわかっていない。ここでは，ニューロイメージングと計算モデリングを用いて，経験的，計算的にこの問題にアプローチした。経験的な部分では，情景分類課題 (自然物対人工物) 中の参加者の脳波データと RT を収集した。そして，信号検出理論の多変量拡張を用いて，波データと行動を関連付けた。その結果，刺激開始後約 100 ミリ秒から約 200 ミリ秒の間に特に神経データと行動の相関が観察され，この時間帯の神経情景表現が意思決定に適したフォーマットになっていることが示唆された。計算部分については，脳と行動のモデルとしてリカレント畳み込みニューラルネットワーク (RCNN) を評価した。CNN は，我々のこれまでの観察を画像計算可能なモデルに統合し，神経表現，情景分類データ，およびそれらの間の関係をよく予測した。我々の結果は，ヒトにおける情景分類の神経と行動の相関を同定し，計算によって特徴付けるものである。
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

