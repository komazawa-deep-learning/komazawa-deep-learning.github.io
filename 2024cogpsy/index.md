---
title: 2024年度 駒澤大学 認知心理学研究 II (b) 浅川担当分
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

* N400 への PDP approach:
  * [Simulating Event-Related Potential Reading Data in a Neurally Plausible Parallel Distributed Processing Model](/Users/_asakawa/study/2022documents/2011LaszloPlaut_CogSciConf_ERPmodel.pdf)
  * Laszlo, S., & Federmeier, K.D. (2009). A beautiful day in the neighborhood: An event-related potential study of lexical relationships and prediction in context. Journal of Memory and Language, 61, 326-338.
* 竹市先生ご指定の文献:


[Empirically Identifying and Computationally Modeling the Brain–Behavior Relationship for Human Scene Categorization](https://doi.org/10.1162/jocn_a_02043)

<div class="abstract">

Humans effortlessly make quick and accurate perceptual decisions about the nature of their immediate visual environment, such as the category of the scene they face.
Previous research has revealed a rich set of cortical representations potentially underlying this feat.
However, it remains unknown which of these representations are suitably formatted for decision-making.
Here, we approached this question empirically and computationally, using neuroimaging and computational modeling.
For the empirical part, we collected EEG data and RTs from human participants during a scene categorization task (natural vs. man-made).
We then related EEG data to behavior to behavior using a multivariate extension of signal detection theory.
We observed a correlation between neural data and behavior specifically between ∼100 msec and ∼200 msec after stimulus onset, suggesting that the neural scene representations in this time period are suitably formatted for decision-making.
For the computational part, we evaluated a recurrent convolutional neural network (RCNN) as a model of brain and behavior.
Unifying our previous observations in an image-computable model, the RCNN predicted well the neural representations, the behavioral scene categorization data, as well as the relationship between them.
Our results identify and computationally characterize the neural and behavioral correlates of scene categorization in humans.
</div>

<div class="figcenter">
<img src="/2024assets/2023Karapetian_fig1.jpg" style="width:59%"><br/>
</div>

図 1. 刺激セット，パラダイム，距離-平面アプローチ。
* A) 解析アプローチ。神経データと行動データを結びつけるために，多変量空間における信号検出理論の拡張である距離-超平面アプローチを用いた。
* B) 刺激セット。Places-365  (Zhou+2018) から刺激を選択し，30 個の自然情景と 30 個の人工情景の集合を作成した。
* C) 実験パラダイム。参加者はブロックの半分で情景分類課題を行い，残りの半分で直交固視 + 字色検出課題 (妨害課題と呼ぶ) を行った。
* D) 距離-超平面アプローチ。距離と RT の相関が有意に負になったときに起こる，神経表象が意思決定に適した形になるタイミングを決定するために，すべての時点において分析を適用した。
<!-- Figure 1. Stimulus set, paradigm, and distance-to-hyperplane approach.
* (A) Analysis approach. To link neural and behavioral data, we used the distance-to-hyperplane approach, an extension of signal detection theory in a multivariate space.
* (B) Stimulus set. We selected stimuli from Places-365 (Zhou+2018), creating a set of 30 natural and 30 man-made scenes.
* (C) Experimental paradigm. Participants performed a scene categorization task on half of the blocks and an orthogonal fixation cross color detection task (referred to as distraction task) on the other half.
* (D) Distance-to-hyperplane approach. We applied the analysis at every time point to determine when neural representations are suitably formatted for decision-making, which occurs when the correlation between distances and RTs is significantly negative. -->


<div class="figcenter">
<img src="/2024assets/2023Karapetian_fig2.jpg" style="width:39%">
</div>

Figure 2. Scene identity and category decoding.

* (A) Pairwise scene identity decoding results on EEG data from the categorization task (blue), distraction task (magenta), and their difference (black).
The vertical dashed gray line at 0 msec represents the stimulus onset.
The shaded area around the curves indicates the SEM.
Significant time points (right tailed, p<0.01, FDR-adjusted) are indicated with asterisks.
* (B) Scene category decoding (natural vs. man-made) results for both tasks and their difference.
* (C) Multidimensional scaling results for scene identity decoding from the categorization and distraction tasks at the scene identity decoding peak and
* (D) scene category decoding peak.
* (E) Results from the searchlight analysis performed in channel space in both tasks at peak decoding latency for scene identity decoding and
* (F) scene category decoding.
Significant channels (right-tailed, p < 0.01, FDR-adjusted) are depicted with black dots.

<div class="figcenter">
<img src="/2024assets/2023Karapetian_fig4.jpg" style="width:39%">
</div>

図 4. 人間の神経情景表現を RCNN と FCNN とでモデル化
<!-- Figure 4. Modeling human neural scene representations with an RCNN versus an FCNN. -->

* A）解析に用いたリカレントCNN，BLnet (Spoerer+2020) のアーキテクチャ。
ネットワークは 7 層からなり，ボトムアップ (緑の矢印) とラテラル (黒の矢印) 接続で結ばれている。
特徴量は 3 つの層 (1, 4, 7) から 8 つの異なる時間ステップで抽出され，RT は読み出し層から収集された。
* B) すべての情景，自然情景，人工的情景について，ヒトの神経表現と 3 つの異なる層からの RCNN 特徴量 (8 つの時間ステップの中央値) に対して RSA を実行した結果。
0 ミリ秒の垂直破線は刺激開始を表す。
曲線の周りの斜線部分は SEM を表す。
有意な時点をアスタリスクで示す (右側検定 p＜0.05，FDR 補正)。
破線の縦線はピークを示す。
灰色の斜線はノイズの上限を示す。
* (C) BLnet の フィードフォワード，パラメータマッチ版である B-Dnet (Spoerer+2020) の特徴量を用いた RSA 結果。
* (D) RCNN と FCNN の結果の差の波 (両側, p < 0.05, FDR 補正)。

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


- 授業名: 認知心理学研究 II (b)
- 担当者名: 永田 陽子, 竹市 博臣, 浅川 伸一 (アサカワ シンイチ)
- 電子メールアドレス: <educ20233@komazawa-u.ac.jp>, <asakawa@cis.twcu.a.jp>
- 開講年度・期:　2024年 後期
- 開講曜日・時限: 金曜日 2 限 10:40-12:10
- 教室: 2 号館 研-001 教場
- 単位数　2

## 授業概要

認知心理学・神経生理学・人工知能のリレー講義です。認知を情報処理過程として捉え，共通トピックとして「多感覚統合」を取り上げます。
認知心理学・神経生理学・人工知能の３領域の結びつきがわかるように，幅広くお話ししてゆく予定です。理解を深めるためのハンズオンを取り入れます。

## 到達目標(ねらい)

本講義の到達目標は、受講生各自が、①認知心理学と関連する神経生理学および人工知能のキーワードを理解し，関係を説明できるようになること，
②心理学と関連する分野の話題を理解し，多様な見方を持った実践ができるようになることです。


## 授業計画

* [第01回 (Sep.20)](2023cogpsy_lect01)
  * 永田：オリエンテーション 授業の概要について説明します。
  * 竹市：脳波の基礎 脳波を用いた研究の基礎的な事項（脳波の発見、覚醒水準、誘発反応と事象関連電位：CNV・N100・MMN・P300・N170・N400・ERN、周波数分析：帯域・τとμ、定常反応、同期、BCIなど）について説明します。
* 第02回 (Sep.27)
  * 竹市：脳波の計測と解析】Karapetian+(2023) で報告されている脳波実験を題材に、脳波の計測と解析の実際、脳波がどのような神経活動に対応づくか、脳波を測ることでどのような認知過程について調べられるかについて説明します。
* 第03回 (Oct.04)
  * 竹市：脳波実験と計算モデル】Karapetian+(2023) で報告されている脳波実験を題材に、行動や生理学的なデータがどのように計算モデルに結びつくのか，計算モデルによって認知心理学のどのような問題が解かれるかについて説明します。
* 第04回 (Oct.11)
  * 浅川：クラウドコンピューティング Google Colaboratory を用いて基礎的な使い方を確認します。
* 第05回 (Oct.18)
  * 竹市：脳磁図の基礎 脳磁図を用いた研究の基礎的な事項（生体磁気、脳神経系の解剖、逆問題、他の計測法：fMRI・ECoG・NIRSとの比較、ニューロデコーディング、最近の話題：超伝導・光と量子）について説明します。
* 第06回 (Oct.25)
  * 竹市：音声言語と文字の知覚 言語の知覚認知の心理学・認知神経科学（言語音の音響特性・包絡追跡・音韻修復、言語の神経心理学、言語の起源と発達、難読、単語の知覚認知、視線解析）など、音声言語と文字の知覚に関する最近の話題について説明します。
* 第07回 (Nov.08)
  * 竹市：音声言語知覚の脳磁図実験 Gwilliams&King(2020) で報告されている読字の脳磁図実験を題材に、言語に関する脳磁図計測と解析について説明します
* 第08回 (Nov.15)
  * 畳み込みニューラルネットワークの基礎 浅川：畳み込みニューラルネットワークの基礎 [Spoerer+2020](https://doi.org/10.1371/journal.pcbi.1008215) での提案モデルを用いるているので，この論文を取り上げる。畳み込みニューラルネットワークの種類と技法を検討する。
* 第09回 (Nov.22)
  * 残差結合 浅川：リカレントネットワークの基礎 BL ネットワークと異なるモデルである[CORnet](https://doi.org/10.1101/408385) を取り上げる。スキップ結合，すなわち ResNet で提案された残差結合の意義を考察する([He+2015](https://arXiv.org/abs/1406.4729/)) 下記の論文をダウンロードしてアブストラクトと図の脚注に目を通しておく：[CORnet](https://doi.org/10.1101/408385) [He+2015](https://arXiv.org/abs/1406.4729/)
* 第10回 (Nov.29)
  * リカレントネットワークによる時空間表現 下記の論文をダウンロードしてアブストラクトと図の脚注に目を通しておく：[Carion+2020](https://arxiv.org/abs/:2005.12872/)
* 第11回 (Dec.06)
  * ボトムアップとトップダウン処理の相互作用 浅川：BU-TD ネットワーク [Ullman+2020](https://arxiv.org/abs/2105.05592) の BU-TD モデルを取り上げ，リカレント結合の異なる意味を考える。
下記の論文をダウンロードしてアブストラクトと図の脚注に目を通しておく：[Ullman+2020](https://arxiv.org/abs/2105.05592)
* 第12回 (Dec.13)
  * 物体認識と領域切り分けとの相互作用 【浅川：物体情報と位置情報】 前回でのモデルを考慮した上で，画像切り分けと物体同定との相互作用の問題を考える。[Neyshabur+2021](https://arxiv.org/abs/2008.11687/)* 第13回 (Dec.20)
* 第13回 (Dec.20)
  * Transformer の導入 浅川：Transformer Transformer を取り上げ，リカレント表現以外の State-of-the-arts である時間表現を取り上げる([Vaswani+2017](https://arXiv.org/abs/1706.03762/))。
下記の論文をダウンロードしてアブストラクトと図の脚注に目を通しておく：[Vaswani+2017](https://arXiv.org/abs/1706.03762/)
* 第14回 (Jan.10)
  * エンコーダ・デコーダモデル 浅川：エンコーダ・デコーダモデル [Gwilliams&King2020](https://doi.org/10.7554/eLife.56603) では，出力系まで考慮したモデルが求められる。入力と出力との相互作用に，リカレント，フィードフォワードのいずれの処理を考える。[End-to-End Object Detection with Transformers](https://arxiv.org/abs/2005.12872) 及び，その [コード](https://github.com/facebookresearch/detr) をダウンロードして眺めておく。

<center>
<div class="fig">
<img src="/2023assets/1999Shelton_Caramazza_fig1.png" width="33%">
<div class="figcaption">
図 1. 語彙系の概要
<!-- Figure 1. A general overview of the lexical system -->
</div></div>
</center>

<center>
<div class="fig">
<img src="/2023assets/1999Shelton_Caramazza_fig2.png" width="33%">
<img src="/2023assets/1999Shelton_Caramazza_fig3.png" width="33%">
<div class="figcaption">
左 図 2. モダリティ別の意味体系を仮定したモデルの例<br/>
右 図 3. 単一のアモーダルな意味体系を仮定したモデルの例。
<!-- left: Figure 2. An example of a model postulating separate modality-specific semantic systems.<br/>
right: Figure 3. An example of a model postulating a single, amodal semantic system. -->
</div></div>
</center>

<center>
<div class="fig">
<img src="/2023assets/1999Shelton_Caramazza_fig4.png" width="33%">
<img src="/2023assets/1999Shelton_Caramazza_fig5.png" width="33%"><br/>
<div class="figcaption">
左 図 4. 感覚的特徴と非感覚的特徴に基づく別々の知識特異的意味系を仮定したモデルの例<br/>
右 図 5. 意味カテゴリーに従って組織化された単一の意味系を仮定したモデルの例。
<!-- left: Figure 4. An example of a model postulating separate knowledge-specific semantic systems based on sensory features versus nonsensory features.<br/>
rigth: Figure 5. An example of a model postulating a single semantic system organized according to semantic category. -->
</div></div>
</center>

<center>
<div class="fig">
<img src="/2023assets/1999Shelton_Caramazza_fig6.png" width="33%">
<img src="/2023assets/1999Shelton_Caramazza_fig7.png" width="33%"><br/>
<div class="figcaption">
左 図 6. 音韻サポートと書記素出力の間に義務的な関係を仮定したモデルの一例。<br/>
右 図 7. 音韻サポートと書記素出力の間に非義務的な関係を仮定したモデルの例。
<!-- left: Figure 6. An example of a model postulating an obligatory relationship between phonological support and orthographic output.<br/>
right: Figure 7. An example of a model postulating a nonobligatory relationship between phonological support and orthographic output. -->
</div></div>
</center>



## 文献資料

1. [ディープラーニング概説, 2015, LeCun, Bengio, Hinton, Nature](https://komazawa-deep-learning.github.io/2021/2015LeCun_Bengio_Hinton_NatureDeepReview.pdf){:target="_blank"}
1. [ゴール駆動型深層学習モデルを用いた感覚皮質の理解 Yamins(2016) Nature](https://project-ccap.github.io/2016YaminsDiCarlo_Using_goal-driven_deep_learning_models_to_understand_sensory_cortex.pdf){:target="_blank"}
1. [ディープラーニングレビュー Storrs ら, 2019, Neural Network Models and Deep Learning, 2019](https://komazawa-deep-learning.github.io/2021/2019Storrs_Golan_Kriegeskorte_Neural_network_models_and_deep_learning.pdf){:target="_blank"}
<!-- * [Storrs ら, Neural Network Models and Deep Learning, 2019](2019Storrs_Golan_Kriegeskorte_Neural_network_models_and_deep_learning.pdf){:target="_blank"} -->
1. [深層学習と脳の情報処理レビュー Kriegestorte, 2015, Deep Neural Networks: A New Framework for Modeling Biological Vision and Brain Information Processing](2015Kriegeskorte_Deep_Neural_Networks-A_New_Framework_for_Modeling_Biological_Vision_and_Brain_Information_Processing.pdf){:target="_blank"}
1. [生物の視覚と脳の情報処理をモデル化する新しい枠組み Kriegeskorte, Deep Neural Networks: A New Framework for Modeling Biological Vision and Brain Information Processing, 2015](https://project-ccap.github.io/2015Kriegeskorte_Deep_Neural_Networks-A_New_Framework_for_Modeling_Biological_Vision_and_Brain_Information_Processing.pdf){:target="_blank"}
1. [計算論的認知神経科学 Kriegeskorte and Douglas, 2018, Cognitive computational neuroscience](https://project-ccap.github.io/2018Kriegeskorte_Douglas_Cognitive_Computational_Neuroscience.pdf){:target="_blank"}
1. [視覚系の畳み込みニューラルネットワークモデル，過去現在未来 Lindsay, 2020, Convolutional Neural Networks as a Model of the Visual System: Past, Present, and Future](https://project-ccap.github.io/2020Lindsay_Convolutional_Neural_Networks_as_a_Model_of_the_Visual_System_Past_Present_and_Future.pdf){:target="_blank"}
1. [計算論的視覚と正則化理論 Poggio, Torre, Koch, 1985](https://komazawa-deep-learning.github.io/2021cogpsy/1985Poggio_Computational_Vision_and_Regularization_Theory.pdf){:target="_blank"}
1. [皮質における物体認識の階層モデル Riesenhuber and Poggio (1999) Nature](https://komazawa-deep-learning.github.io/2021cogpsy/1999Riesenhuber_Poggio_Hierarchical_models_of_object_recognition_in_cortex.pdf){:target="_blank"}
1. [注意レビュー論文 Lindsay, 2020, Attention in Psychology, Neuroscience, and Machine Learning](https://project-ccap.github.io/2020Lindsay_Attention_in_Psychology_Neuroscience_and_Machine_Learning.pdf){:target="_blank"}


---

<center>
<img src="/2021/2008Fuster_Prefrontal_Cortex_fig8_4.svg" width="39%">
<!-- <img src="https://komazawa-deep-learning.github.io/2021/2008Fuster_Prefrontal_Cortex_fig8_4.svg" width="39%"> -->
<img src="/assets/2015Ronneberger_U-Net_Fig1_ja.svg" width="48%">
<!-- <img src="https://komazawa-deep-learning.github.io/assets/2015Ronneberger_U-Net_Fig1_ja.svg" width="48%"> -->
</center>

<br/>

<!--
1. [2020ccap 資料置き場](2020ccap)
2. [2020中央大学，緑川先生，重宗先生，研究会資料](2020chuo)
3. [2020 第2回 中央大学，緑川先生，重宗先生，研究会資料](2020chuo2)
4. [2020サイトビジット資料](2020sightvisit)

<a href="https://guides.github.com/features/pages/">Read this page to write this page.</a>
-->
