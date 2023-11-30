---
title: "第11回"
author: "浅川 伸一"
layout: home
---

# 2023年度開講 駒澤大学 認知心理学研究 IIB

<div align="right">
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 01/Dec/2023<br/>
Appache 2.0 license<br/>
</div>

<!-- <link href="/css/asamarkdown.css" rel="stylesheet"> -->

* [ベイズ学習](../2023_1124bayes)
* [最適化](../2023_1124optimizations)

<div class="figcenter">
<img src="/2023assets/2016Marblestone_fig1.jpg" width="77%">
</div>
<!-- <div class="figcaption"> -->

図 1. 従来のニューラルネットワークと脳のようなニューラルネットワークの設計の違い。

* **(A)** 従来の深層学習では，教師あり学習は外部から供給されたラベル付きデータに基づいて行われる。
* **(B)** 脳では，ネットワークの教師付き学習は，誤差信号に対する勾配降下によって行うことができるが，この誤差信号は内部で生成されたコスト関数から発生する必要がある。
これらのコスト関数は，遺伝と学習の両方によって指定された神経モジュールによって計算される。
内部で生成されたコスト関数は，より複雑な学習のブートストラップに使われるヒューリスティックスを作り出す。
例えば，顔を認識する領域は，まず線の上に 2 つの点があることのような単純なヒューリスティックスを使って顔を検出するように訓練され，その後，教師なし学習と社会的報酬処理に関連する他の脳領域からの誤差信号から生じる表現を使って，顕著な表情を識別するようにさらに訓練されるかもしれない。
* **(C)** 皮質深層ネットワークの内部で生成されたコスト関数と誤差駆動型訓練は，いくつかの特殊な系を含むより大きなアーキテクチャの一部を形成している。
ここでは，訓練可能な皮質領域をフィードフォワード神経回路網として図式化しているが，LSTM や他のタイプのリカレントネットワークの方がより正確なアナロジーかもしれない， 適応と恒常的可塑性，タイミング依存的可塑性，直接的電気接続，過渡的シナプス・ダイナミクス，興奮性／抑制性のバランス，自発的振動活動，軸索伝導遅延 (Izhikevich2006) など，多くの神経細胞やネットワークの特性が，このようなネットワークが何をどのように学習するかに影響を与えるだろう。

<!-- FIGURE 1.
Putative differences between conventional and brain-like neural network designs.
(A) In conventional deep learning, supervised training is based on externally-supplied, labeled data.
(B) In the brain, supervised training of networks can still occur via gradient descent on an error signal, but this error signal must arise from internally generated cost functions.
These cost functions are themselves computed by neural modules specified by both genetics and learning.
Internally generated cost functions create heuristics that are used to bootstrap more complex learning.
For example, an area which recognizes faces might first be trained to detect faces using simple heuristics, like the presence of two dots above a line, and then further trained to discriminate salient facial expressions using representations arising from unsupervised learning and error signals from other brain areas related to social reward processing.
(C) Internally generated cost functions and error-driven training of cortical deep networks form part of a larger architecture containing several specialized systems.
Although the trainable cortical areas are schematized as feedforward neural networks here, LSTMs or other types of recurrent networks may be a more accurate analogy, and many neuronal and network properties such as spiking, dendritic computation, neuromodulation, adaptation and homeostatic plasticity, timing-dependent plasticity, direct electrical connections, transient synaptic dynamics, excitatory/inhibitory balance, spontaneous oscillatory activity, axonal conduction delays (Izhikevich2006) and others, will influence what and how such networks learn. -->
<!-- </div> -->
<!-- </div> -->

<div class="figcenter">
<img src="/2023assets/1990Cohen_McClelland_stroop_fig3.svg">
<img src="/2023assets/2023_1110task_demand_conflict_ja.svg" width="49%">
</div>
<!-- <div class="figcaption"> -->

左: 図 3. 単語読解と色名学習後の接続強度を示すネットワーク図。 (強度は接続の横に示され，中間ユニットのバイアスはユニットの内側に示されている。
課題要求ユニットから中間ユニットへの注意強度は固定され，中間ユニットのバイアスも固定された。
課題要求ユニットがオンのとき，対応する経路のユニットの基本入力が 0.0 になり，もう一方の経路のユニットの基本入力が，実験によって -4.0 から -4.9 の範囲になるように選ばれた)。
<!-- Figure 3. Diagram of the network showing the connection strengths after training on the word-reading and color-naming tasks.
(Strengths are shown next to connections; biases on the intermediate units are shown inside the units.
Attention strengths-from task demand units to intermediate units-were fixed, as were biases for the intermediate units.
The values were chosen so that when the task demand unit was on, the base input for units in the corresponding pathway was 0.0, whereas the base input to units in the other pathway was in the range of -4.0 to -4.9, depending on the experiment.) -->
出典: Cohen, Dunbar, and McClelland (1990) __On the Control of Automatic Processes: A Parallel Distributed Pro
cessing Account of the Stroop Effect__, Psychological Review, Vol. 97, No. 3, 332-361.

右: 転移学習，微調整を用いた Stroop 課題の枠組み
<!-- </div> -->
<!-- </div> -->

## 実習

* [1990 年代の Stroop 効果のシミュレーション<img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_1110Stroop_1990Cohen_model.ipynb){:target="_blank"}
* [転移学習による Stroop 効果のデモ<img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_1123Stroop_model.ipynb)

<div class="figcenter">
<img src="/2023assets/2003Roelofs_stroop_fig7.svg" width="33%">　　　　　　　　　
<img src="/2023assets/2003Roelofs_stroop_fig9.jpg" width="44%">
<div class="figcaption">

図 7. WEAVER++ における処理レベル。
単語の読解はレンマ選択を伴う場合もあれば (経路 a)，伴わない場合もある (経路 b)。
<!-- Figure 7. Levels of processing in WEAVER++.
Word reading may involve lemma selection (Route a) or may not (Route b). -->
<!-- Adapted from Cognition, 42, A. Roelofs, “A Spreading-Activation Theory of Lemma Retrieval in Speaking,” p. 114, Figure 1, Copyright 1992, with permission from Elsevier Science. -->

図 9. Stroop 課題における，単語計画と実行制御。
ヒトの左半球の側面図 (上) と 中央 (下)。
単語計画系は，色知覚 (cp)，概念同定 (ci)，レンマ検索 (lr)，単語携帯符号化 (wfe)，構音処理 (art) を介して色名呼称へと至る。
単語形態知覚 (wfp) は，語彙と形態と並列的に至る。
単語音読は，最小限 wfp, wfe, art を含む。
実行系は前帯状回にあり，目標と入力制御に関与する。
<!-- Figure 9. Word planning and executive control in the Stroop task.
Lateral view (top panel) and medial view (bottom panel) of the left hemisphere of the human brain.
The word-planning system achieves color naming through color perception (cp), conceptual identification (ci),
lemma retrieval (lr), word-form encoding (wfe), and articulatory processing (art);
word-form perception (wfp) activates lemmas and word forms in parallel.
Word reading minimally involves wfp, wfe, and art.
The executive system centered on the anterior cingulate achieves goal and input control. -->
出典: Roelofs (2003) __Goal-Referenced Selection of Verbal Action: Modeling Attentional Control in the StroopTask__, Psychological Review, 2003, Vol. 110, No. 1, 88–125.
</div></div>


<div class="figcenter">
<img src="/2023assets/1984Glaser_picture-word_fig1.svg">
<div class="figcaption">

刺激成分の特徴例: (a) 非絵画，(b) 空単語付き絵画刺激, (c) 非単語，(d) 不調和刺激
</div></div>


<div class="figcenter">
<img src="/2023assets/1984Glaser_picture-word_fig2.svg">
<div class="figcaption">
図 課題 $\times$ SOA $\times$ 一致性における平均促進・抑制得点
<!-- Figure 2. Mean facilitation and inhibition scores in the Task X SOA X Congruency cells of Experiment I. (SOA = stimulus onset asynchrony.) -->
</div></div>

<div class="figcenter">
<img src="/2023assets/2006Howard_fig1.svg" width="44%">
<img src="/2023assets/2006Howard_fig3.svg" width="44%">
<div class="figcaption">

左 カテゴリー内の順序位置が命名反応時間 (補正なし RT) に及ぼす影響。<br/>
右  (A) 健常群の反応時間 (上) と (B) モデル出力
</div></div>

<div class="figcenter">
<img src="/2023assets/2006Howard_tab1.svg" width="77%">
<div class="figcaption">

表 平均正答反応時間 (順番，ラグ別) (95% 被験者内信頼区間) A. 未補正の反応時間, B. 実験期間中の線形変化を補正した反応時間
</div></div>
<!-- <img src="figures/2006Howard_tab2.svg"> -->

<div class="figcenter">
<img src="/2023assets/2006Howard_fig2.svg" width="49%">
<img src="/2023assets/2006Howard_fig4.svg" width="33%">
<!-- <img src="figures/2006Howard_fig5.svg">
<img src="figures/2006Howard_fig6.svg"> -->
</div>

# 機械学習一般

$$
\begin{aligned}
\text{損失関数} &= \text{誤差関数} + \text{ペナルティ項}\\
\mathcal{L}\left(y,x;\theta\right) &=\left\|y-f(x;\theta)\right\|^2+\lambda\left\|P\theta\right\|^2
\end{aligned}
$$

損失関数は目標関数とも呼ばれる。誤差関数は最小自乗誤差 least squared error が用いられる(回帰との類推では)。
ニューラルネットワークによる画像分類[@2012AlexNet]，主成分分析[@1901Pearson_PCA]，標準正則化理論(画像復元)[@Poggio1985]，画像分類課題では次式交差エントロピー誤差[@1989Hinton]が用いられる。

$$
\text{CEE}=-\sum_{j,c}y_{j,c}\log_2\left(f(x_{j,c})\right)+\left(1-y_{j,c}\right)\log_2\left(1-f(x_{j,c})\right),
$$

[@1995GirosiPoggio]

- See https://ermongroup.github.io/cs228-notes/inference/variational/


$$
H[f]=\sum_{i=1}^{N}
\left(y_i-f\left(\mathbf{x}_i\right)\right)^2+\lambda\left\|Pf\right\|^2
$$

ここに $P$ は制約演算子，$\left\|\cdot\right\|$ はノルムを表す
$\lambda$ は正の有理数であり正則化パラメータと呼ばれる。
汎関数 $H$ の最小化は オイラー=ラグランジェ方程式として定式化される。
$P$ は事前知識を表す。 [GirosiPoggio1990]

$$
\hat{P}Pf\left(\mathbf{x}\right)=\frac{1}{\lambda}\sum_{i=1}^N\left(y_i-f\left(\mathbf{x}\right)\right)\,\delta\left(\mathbf{x}-\mathbf{x}_i\right),
$$
ここで $\hat{P}$ は微分演算子 $P$ の随伴演算子であり，微分方程式，右辺の

上記は偏微分方程式であり，その解は微分作用素 $G$ のグリーン関数で与えられるカーネルを持つ右辺の積分変換，すなわち以下の分布微分方程式を満たす関数 $G$ として書けることがよく知られている：
<!-- The above is a partial differential equation, and it is well known that its solution can be written as the integral transformation of its right side with a kernel given by the Green's function of the differential operator $\hat{P}P$, that is the function $G$ satisfying the following distributional differential equation: -->
$$\tag{4}
\hat{P}P\,G\left(\mathbf{x};y\right)=\delta\left(\mathbf{x}-y\right).
$$
(4) 式にデルタ関数が現れるので，積分変換は離散和になり，$f$ は次のように書ける:
<!-- Because of the delta functions appearing in (4) the integral transformation becomes a discrete sum and $f$ can then be written as -->
$$
f(\mathbf{x})=\frac{1}{\lambda}\sum_{i=1}^N(y_i-f(\mathbf{x}_i))
G(\mathbf{x};\mathbf{x}_i).
$$
式 (5) は，正則化問題の解が滑らかな関数の空間の $N$ 次元部分空間にあることを示している。
この部分空間の基底は $N$ 個の関数 $G(\mathbf{x};mathbf{x}_j)$ によって与えられる。
以下では，$G(\mathbf{x};mathbf{x}_j)$ を点 $\mathbf{x}_i$ を「中心とする」グリーン関数，点$\mathbf{x}_i$ を展開の「中心」と呼ぶ。
この理由は，通常グリーン関数は遷移的に不変であり，$G=G(\mathbf{x}-\mathbf{x}_i)$ であり，この場合 $G(\mathbf{x})$ と $G(\mathbf{x}-\mathbf{x}_i)$ とは，原点に $\mathbf{x}_i$ を写す座標変換によって等価になることにある。
<!-- Equation (5) says that the sol ution of the regularization problem lies in an N-dimensional subspace of the space of smooth functions.
A basis for this subspace is given by the $N$ functions $G(\mathbf{x};\mathbf{x}_j)$.
In the following we will refer to $G(\mathbf{x}; \mathbf{x}_j)$ as to the Green's function "centered" at the point $\mathbf{x}_i$, and to the points $\mathbf{x}_i$ as to the "centers" of the expansion.
The reason for this lies in the fact that usually the Green's function is transitionally invariant, that is $G=G(\mathbf{x}-\mathbf{x}_i)$, and in this case $G(\mathbf{x})$ and $G(\mathbf{x}-\mathbf{x}_i)$ are equivalent modulo a coordinates translation that maps $\mathbf{x}_i$ in the origin. -->

R. Courant and D. Hilbert, Methods of Mathematica/Physics, Vol. 2. Interscience, London, England, 1962.
where $c$, which is related to $P_d(d)$, depens only on $d$.

物理学の場合 $\lambda$ が定まる，あるいは意味を持つ場合があるが，機械学習，ニューラルネットワークの場合定まるとはかぎらない。ハイパーパラメータとして扱われる場合が多い。

<center>
<img src="/2023assets/2018Tschannen_Fig1.svg" style="width:74%"><br/>
<img src="/2023assets/2018Tschannen_Fig2.svg" style="width:74%"><br/>
</center>

## 関連技術
1. 主成分分析[@1901Pearson_PCA]
$$
H[y,X,w]=\left(y-Xw\right)^2+\lambda(w^{\top}w-1)
$$
2. エントロピー最大化
3. word2vec における負例サンプリング[@2013Mikolov_skip-gram_NIPS]
2. 画風変換 [@2015Gatys_DeepArt]
3. 領域 CNN [@2015Girshick_FastRCNN],[@2015Ren_FasterRCNN],[@2017He_MaskRCNN]
- 解絡学習，解絡表現 disentangled representation, disentaglement
4. $\beta-\text{VAE}$ (Kruse=Kuhn=Tucker 条件[@2017Higgins_betaVAE])
5. InfoGAN[@2016Chen_infoGAN]



## 実習

* [実習 オーバーフィッティング，アンダーフィッテング <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2020Sight_Visit_polynomilal_fittings_demo.ipynb){:target="_blank"}

## 機械学習と推測統計学

# 機械学習の技法

3. Breiman の 2 つの文化
2. データセット, 訓練データ，検証データ，テストデータ
1. フィードフォワード, フィードバック
8. 活性化関数
9. 損失関数 (誤差関数，目的関数)
10. 誤差逆伝播法, 勾配降下法, 確率的勾配降下法, ミニバッチ
13. データ拡張
15. 正則化
14. ドロップアウト

## 正則化

データ $y$ から $z$ を見つけ出す不良設定問題の正則化 $Az = y$ では，正則化項 $\left\|\cdot\right\|$ の選択と汎関数の安定化項 $\left\|Pz\right\|$ が必要となる。
標準正則化理論においては，$A$ は線形演算子，ノルムは 2 次，$P$ は線形である。
2 種類の方法が適用可能である。
すなわち

1. $\left\|Az-y\right\|\leqslant\epsilon$ を満たし，$\displaystyle\left\|Pz\right\|^2$ を最小化する $z$ を探す
2. $\displaystyle \left\|Az-y\right\|+\lambda\left\|Pz\right\|^2,$ を最小化する $z$ を探す
ここで $\lambda$ は正則化パラメータ。

最初の方法は，十分にデータを近似し，かつ，「基準」$\left\|Pz\right\|$ を最小化するという意味で「正則」な $z$ を探す方法である。
二番目の方法は，$\lambda$ が正則化の程度と解のデータへの近似とをコントロールする。
標準正則化理論は，最良の $\lambda$ を決定する手法を提供する。
標準正則化の手法は，上式に制約を導入することで変分原理の問題としている。
最小化するコストは物理的制約条件を満たす良い解を反映している。
すなわち，データへの近似もよく，かつ，正則化項 $\left\|Pz\right\|^2$ も小さいことを意味する。
$P$ は問題の物理的制約を表しており，2 次の変分原理であり，解空間内での唯一解が存在する。
標準正則化手法は，不良設定問題に対して注意深い分析が必要であることを注記しておく。
ノルム $\left\|\cdot\right\|$，正則化関数 $\left\|Pz\right\|$, および，汎関数空間の選択は数学的性質と，物理的説得性を有する必要がある。
これらにより，正しい正則化の詳細条件が定まる。

変分原理は物理学，経済学，工学，で幅広く用いられている。例えば物理学における基本法則は変分原理を用いて，
エネルギーやラグランジェ関数を用いて簡潔に表現されている。


# Transformer

* Transformer: マルチヘッド注意機構，位置符号化器，埋め込み表現，ソフトマックス関数
* 事前訓練とファインチューニング: マスク言語モデル，次文予測  <!--Masked Language model, next sentence prediction--->
* GTP-4: 符号化器・復号化器モデルを用いた画像と言語との融合
* プロンプトエンジニアリングと RLHF (人間のフィードバックによる強化学習): 報酬モデルと代理方針最適化 (Proximal Policy Optimization)

<div class="figcenter">
<img src="/assets/2017Vaswani_Fig2_1.svg" width="09%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="/assets/2017Vaswani_Fig2_2.svg" width="19%">&nbsp;&nbsp;&nbsp;
<img src="/assets/2017Vaswani_Fig1.svg" width="29%">
<div class="figcaption">

Transformer ([2017Vaswani++](https://arxiv.org/abs/1706.03762)) Fig.2 を改変
</div></div>

上図で，`matmul` は行列の積，`scale` は，平均 0 分散 1 への標準化，`mask` は 0 と 1 とで，データを制限すること，`softmax` はソフトマックス関数である。

トランスフォーマーの注意とは，このソフトマックス関数である。

<!-- <div class="figure figcenter">
<img src="figures/2017Vaswani_Fig2_1.svg" width="19%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="figures/2017Vaswani_Fig2_2.svg" width="29%">&nbsp;&nbsp;&nbsp;
<img src="figures/2017Vaswani_Fig1.svg" width="39%"> -->

<!-- # Transformer(2): Attention is all you need -->

$$
\text{MultiHead}\left(Q,K,V\right)=\text{Concat}\left(\text{head}_1,\ldots,\text{head}_{h}\right)W^O
$$
where, $\text{head}_i =\text{Attention}\left(QW_i^Q,KW_i^K,VW_i^V\right)$

The projections are parameter matrices $W_i^Q\in\mathbb{R}^{d_{\text{model}}\times d_k}$, $W_i^K \in\mathbb{R}^{d_{\text{model}}\times d_k}$,
$W_i^V\in\mathbb{R}^{d_{\mathop{model}}\times d_v}$, and $W^O\in\mathbb{R} ^{hd_v\times d_{\mathop{model}}}$.
$h=8$, $d_k=d_v=\frac{d_{\mathop{model}}}{h}=64$

$$
\text{FFN}(x)=\max\left(0,xW_1+b_1\right)W_2+b_2
$$

$$
\text{PE}_{(\text{pos},2i)} = \sin\left(\frac{\text{pos}}{10000^{\frac{2i}{d_{\mathop{model}}}}}\right)
$$

$$
\mathop{PE}_{(\mathop{pos},2i+1)} = \cos\left(\frac{\mathop{pos}}{10000^{\frac{2i}{d_{\mathop{model}}}}}\right)
$$

<!-- # Transformer(3): Attention is all you need -->

<div class="figcenter">
<img src="/assets/2017Vaswani_Fig1.svg">
<div class="figcaption" style="width:33%">
[Vaswani+2017](https://arxiv.org/abs/1706.03762) Fig. 1 より
</div></div>

<!-- # Sejnowski2022

<div class="figcenter">
<img src="figures/2022Sejnowski_fig5.jpg" width="66%">
<div class="figcaption">

トランスフォーマーのループと皮質-基底核のループの比較。
(左) トランスフォーマーは，出力を入力とループさせて単語系列を生成するフィードフォワード自己回帰型アーキテクチャを持つ (Vaswani+2017)。
示された単一のエンコーダ/デコーダモジュールは N 層 深く (Nx) 積み重ねることができる。
(右) 位相的に写像された運動皮質は大脳基底核に投射し，大脳皮質にループバックして，話し言葉の単語列のような一連の動作を生成する。
大脳皮質のすべての部分が大脳基底核に投影され，前頭前野と大脳基底核の間の同様のループによって，思考の系列が生み出される。

thalamus: 視床，
putamen: 被殻
SMA: supplementary motor area 補足運動野
PM: premotor cortex 運動前野
STN: subthalamic nucleus 視床下核
GPi: internal segment of globus pallidus 淡蒼球内節
GP: globus pallidus     淡蒼球
M1: 一次運動野
</div></div>
-->

## 1 位置符号器 Position encoders

 Transformer の入力には，上述の単語表現に加えて，位置符号器からの信号も重ね合わされる。
位置 $i$ の信号は次式で周波数領域へと変換される:

$$
\text{PE}_{(\text{pos},2i)} = \sin\left(\frac{\text{pos}}{10000^{\frac{2i}{d_{\text{model}}}}}\right)\\
\text{PE}_{(\text{pos},2i+1)} = \cos\left(\frac{\text{pos}}{10000^{\frac{2i}{d_{\text{model}}}}}\right)
$$

位置符号器による位置表現は，$i$ 番目の位置情報をワンホット表現するのではなく，
周波数領域に変換することで周期情報を表現する試みと見なし得るだろう。

<div class="figcenter">
<img src="/assets/PE_example.svg" width="66%">
<div class="figcaption">
位置符号化に用いられる符号化
</div></div>

# BERT

## BERT の入力表現

<div class="figure figcenter">
<img src="/assets/2018Devlin_BERT_Fig2.svg" width="49%">
<div class="figcaption">
埋め込みトークンの総和，位置符号器，分離埋め込みの 3 者
</div></div>

<!-- <div class="figure figcenter">
<img src="figures/2018Devlin_BERT_Fig2.svg">
</div> -->

## BERT の事前訓練: マスク化言語モデル

全入力系列のうち 15% をランダムに [MASK] トークンで置き換える

* 入力はオリジナル系列を [MASK] トークンで置き換えた系列
* ラベル: オリジナル系列の [MASK] 部分にの正しいラベルを予測

%Rather than always replacing the chosen words with [MASK], the date generator will do the following:

* 80%: オリジナル入力系列を [MASK] で置換
y $\rightarrow$ my dog is  [MASK].
* 10%: [MASK] の位置の単語をランダムな無関連語で置き換える
my dog is hairy $\rightarrow$ my dog is apple
* 10%: オリジナル系列

## BERT の事前訓練: 次文予測課題

言語モデルの欠点を補完する目的，次の文を予測

[SEP] トークンで区切られた 2 文入力
* 入力: the man went to the store [SEP] he bought a gallon of milk.
* ラベル: IsNext
* 入力: the man went to the store [SEP] penguins are flightless  birds.
* ラベル: NotNext

### BERT のファインチューニング

<div class="figcenter">
<img src="/2023assets/2019Liu_mt-dnn.png" width="66%">
<div class="figcaption">

[Liu+2019](https://arxiv.org/abs/1901.11504) Fig. 1
</div></div>

<!-- <div class="figcenter">
<img src="figures/2017Vaswani_Fig2_1ja.svg" width="22%">
<img src="figures/2017Vaswani_Fig2_2ja.svg" width="22%">
<div class="figcaption">
From Vaswani+2017 transformer Fig. 2
</div></div> -->

<!-- # BERT: ファインチューニング (1) -->

<div class="figcenter">
<img src="/assets/2018Devlin_BERT_Fig3.svg">
<div class="figcaption">

(a), (b) は文レベル課題，(c),(d)はトークンレベル課題, E: 入力埋め込み表現,
$T_i$: トークン $i$ の文脈表象。[CLS]: 分類出力記号, [SEP]:文分離記号
</div></div>

# GPT-4
加えて，chatGPT の後続モデルである GPT-4 では，マルチモーダル，すなわち，視覚と言語の統合が進んだ。

<div class="figcenter">
<img src="/2023assets/2023kosmos_coverpage.png" width="49%">
<div class="figcaption">

[Kosmos-1 の概念図](https://arXiv.org/abs/2302.14045)
</div></div>

<!-- まず第一に，大規模ではない，言語モデルについて考えます。
言語モデルは，機械翻訳などでも使われる技術です。
ですから，DeepL や Google 翻訳で，使っている方もいることでしょう。

chatGPT を使える方は，上記太字のキーワードについて，chatGPT に質問してみることをお勧めします。
とりわけ 注意 については，認知，視覚，心理学との関連も深く，注意の障害は，臨床，教育，発達などの分野と関係するでしょう。 -->


# BERT: 埋め込みモデルによる構文解析

BERT の構文解析能力を下図示した。
各単語の共通空間に射影し，単語間の距離を計算することにより構文解析木と同等の表現を得ることができることが報告されている [@2019HewittManning_structural]。

<div class="figure figcenter">
<img src="/assets/2019hewitt-header.jpg" width="44%">
<img src="/assets/2019HewittManning_blogFig1.jpg" width="22%">
<img src="/asets/2019HewittManning_blogFig2.jpg" width="22%">
<div class="figcaption">
BERT による構文解析木を再現する射影空間
From `https://github.com/john-hewitt/structural-probes``
</div></div>

word2vec において単語間の距離は内積で定義されていた。
このことから，文章を構成する単語で張られる線形内積空間内の距離が構文解析木を与えると見なすことは不自然ではない。

そこで構文解析木を再現するような射影変換を見つけることができれば BERT を用いて構文解析が可能となる。
例えば上図における chef と store と was の距離を解析木を反映するような空間を見つけ出すことに相当する。
2 つの単語 $w_i$, $w_j$ とし単語間の距離を $d\left(w_i,w_j\right)$ とする。 適当な変換を施した後の座標を $h_i$, $h_j$ とすれば，求める変換 $B$ は次式のような変換を行なうことに相当する:

$$
\min_{B}\sum_l\frac{1}{\left|s_\ell\right|^2}\sum_{i,j}\left(d\left(w_i,w_j\right)-\left\|B\left(h_i-h_j\right)\right\|^2\right)
$$

ここで $\ell$ は文 s の訓練文のインデックスであり，各文の長さで規格化することを意味している。


# Seq2seq model

<div class="figure figcenter">
<img src="/assets/2014Sutskever_S22_Fig1.svg" width="77%">
<div class="figcaption">

Sutskever+2014 Fig. 1, 翻訳モデル `seq2seq` の概念図
</div>
</div>

`eos` は文末を表す。
中央の `eos` の前がソース言語であり，中央の `eos` の後はターゲット言語の言語モデルである SRN の中間層への入力として用いる。

注意すべきは，ソース言語の文終了時の中間層状態のみをターゲット言語の最初の中間層の入力に用いることであり，それ以外の時刻ではソース言語とターゲット言語は関係がない。
逆に言えば最終時刻の中間層状態がソース文の情報全てを含んでいるとみなしうる。
この点を改善することを目指すことが 2014 年以降盛んに行われてきた。
顕著な例が後述する **双方向 RNN**，**LSTM** 採用したり，**注意** 機構を導入することであった。

<div class="figure figcenter">
<img src="/assets/2014Sutskever_Fig2left.svg" width="44%">
<img src="/assets/2014Sutskever_Fig2right.svg" width="44%">
<div class="figcaption">

From Sutskever+2014, Fig. 2
</div></div>

# 自然言語系の注意

<div class="figure figcenter">
<img src="/assets/2015Bahdanau_attention.jpg" width="30%">
<img src="/assets/2015Luong_Fig2.svg" width="30%">
<img src="/assets/2015Luong_Fig3.svg" width="30%">
<div class="figcaption">

左: Bahdanau+2014,
中: Luong+2015, Fig. 2,
右: Luong+2015, Fig. 3
</div></div>

# StableDiffusion と LangChain

<div class="figure figcenter">
<img src="/2023assets/2022patrickvonplaten_scientific_images_stable_diffusion.png" width="34%">
<img src="/2023assets/2023Polzer_LLM_app_ja_fig1.webp" width="44%">
<div class="figcaption">
左: `https://github.com/patrickvonplaten/scientific_images/tree/master`，
右: [Polzer2023](https://towardsdatascience.com/all-you-need-to-know-to-build-your-first-llm-app-eb982c78ffac) より
</div></div>

<!-- * [StableDiffusion <img src="figures/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_0714stable_diffusion.ipynb) -->

# 埋め込みモデル，ベクトル空間

* ピラミッド・パームツリー・テスト: 認知症検査
* ターゲットと最も関連のあると考えられる選択肢を一つ選べ。

1. ターゲット: オートバイ，選択肢: 麦わら帽子，帽子，ヘルメット，兜
2. ターゲット: かもめ，選択肢: 水田，池，滝，海
3. ターゲット: 柿，選択肢: 五重塔，教会，病院，駅

<div class="figure figcenter">
<img src="/2023assets/2023_0712projection_concept.svg" width="24%">
<img src="/2023assets/2021_0831jcss_PPT1.svg" width="29%">
<img src="/2023assets/2021_0831jcss_PPT2.svg" width="29%">
</div>

<!-- ベクトル空間の例として，word2vec による PPT  `~/study/2021ccap/notebooks/2021_0831jcss_PPT_projection.[ip
ynb,pdf]` まで

* いまだに，このような記事が出ることの方が問題だろうと思う。
[<img src="https://www.mag2.com/p/news/wp-content/uploads/2017/09/logo_mag2news_290x50-1.png" style="width:9%"
> 大ウソつきChatGPT。訴訟文書「過去の判例」が“ほぼ出鱈目”だった理由](https://www.mag2.com/p/news/577615)

生成 AI と呼ばれる，生成 generative とは，サンプリングを行うことを意味している。
このため，サンプリングに伴う変動は常に存在する。

$$
p(x_i,\beta) = \frac{e^{x_i/\beta}}{\sum_{j\in X} e^{x_j/\beta}}
$$ -->


# 14. 視覚における注意と CAM

<div class="figcenter">
<img src="/2023assets/2016Grad-CAM_boxer_tigercat.png" width="19%">
<img src="/2023assets/2023_0723Grad-CAM_boxer_tigercat_results.png" width="74%">
</div>

<!--
## ファインチューニング (fine-tuning)，転移学習 (transfer-learning)

<div class="figcenter">
<img src="figures/2017Ruder_fig1.jpg" width="22%">
<div class="figcaption">

微調整 (fine tuning) による課題ごとの訓練。
多層ニューラルネットワークモデルの最終層を，課題ごとに入れ替えることで，複数の課題に適応できるようにする。
今回は，BIT の 4 課題 (線分二等分，線分検出，文字検出，星印検出) を考える。
ただし，文字検出課題と星印検出課題は，文字と記号検出を微調整した。
そのため，課題ごとの微調整は，この両課題については同一である。
従って，3 種類の微調整を行った。

図は Ruder (2017) [An Overview of Multi-Task Learning in Deep Neural Network](https://arXiv.org/abs/1706.05098), Fig. 1. より
</div></div>

## 様々なタイプの生成モデル

<div class="figure figcenter">
<img src="figures/generative-overview.png" width="66%">
<div class="figcaption">
[Weng2021](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) より
</div></div>

-->


# 実習

* [PyTorch による Transfomer 実装 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_0602Transformer_from_scratch.ipynb)
* [chatGPT <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_0608rinna_chatGPT_demo.ipynb)
* [Stable-baselines3 を用いた PPO デモ Atari Lunalander 月面着陸 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_0619stable_baselines3_demo_LunaLander_V2.ipynb)
* [画像認識における注意 CAM <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2021_0618CAM_demo.ipynb)
* [Stable diffusion デモ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_0707stable_diffusion.ipynb)
* [sentenceBERT <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_0602minimam_sentenceBERT.ipynb)
* [BERT の微調整 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_0623BERT_SNOW_training.ipynb)
* [BERT のマルチヘッド注意の視覚化 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_1007BERT_head_view.ipynb)
* [日本語 BERT 2 つの文の距離を求めるデモ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2020_0624BERTja_test.ipynb)
* [リカレントニューラルネットワークによる文処理デモ 青空文庫より，夏目漱石 こころ](https://komazawa-deep-learning.github.io/character_demo.html)
* [CartoonGAN 実習<img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_0628CartoonGAN_demo.ipynb)
* [加算型注意 (Bahdanu) と 内積型注意 (Loung) の実習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_1022Two_attentions_additive_and_multiplicative_Seq2seq.ipynb)

# Huggingface RTL

* [TRL - Transformer Reinforcement Learning](https://github.com/huggingface/trl/tree/main)
