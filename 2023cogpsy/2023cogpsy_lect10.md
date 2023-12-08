---
title: "第10回 2023年度開講 駒澤大学 認知心理学研究"
author: "浅川 伸一"
layout: home
codemirror_mode: python
codemirror_mime_type: text/x-cython
---

<div align="right">
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 01/Dec/2023<br/>
Appache 2.0 license<br/>
</div>

<link href="/css/asamarkdown.css" rel="stylesheet">

## 実習

* [転移学習による Stroop 効果のデモ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_1123Stroop_model.ipynb)

<!-- * [1990 年代の Stroop 効果のシミュレーション<img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_1110Stroop_1990Cohen_model.ipynb){:target="_blank"}
* [Stroop 効果シミュレーションの準備 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_1123Stroop_model.ipynb){:target="_blank"} -->

* [実習 オーバーフィッティング，アンダーフィッテング <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2020Sight_Visit_polynomilal_fittings_demo.ipynb){:target="_blank"}
* [ニューラルネットワークで遊んでみよう](https://komazawa-deep-learning.github.io/tensorflow-playground/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.98055&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false){:target="_blank"}


## 参考

* [ベイズ学習](../2023_1124bayes)
* [最適化](../2023_1124optimizations)

## ニューラルネットワークと機械学習とのコスト関数 (損失関数，誤差関数) の類似

<div class="figcenter">
<img src="/2023assets/2016Marblestone_fig1.jpg" width="77%"><br/>
</div>
<div class="figcaption">

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
</div>


## Stroop 効果

<div class="figcenter">
<img src="/2023assets/1990Cohen_McClelland_stroop_fig3.svg">
<img src="/2023assets/2023_1110task_demand_conflict_ja.svg" width="49%">
</div>
<div class="figcaption" style="width:94%">

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
</div>


---

<div class="figcenter">
<img src="/2023assets/2003Roelofs_stroop_fig7.svg" width="33%">　　　　　　　　　
<img src="/2023assets/2003Roelofs_stroop_fig9.jpg" width="44%">
</div>
<div class="figcaption" style="width:88%">

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
</div>

## 関連する話題

### 絵画‐単語干渉課題

<center>
<img src="/2023assets/1984Glaser_picture-word_fig1.svg" width="39%">
<div class="figcaption">

刺激の例: (a) 非絵画，(b) 単語なし絵画, (c) 非単語，(d) 不一致刺激

<!-- Figure 1. Characteristic examples of the stimulus components:
Panel a, nonpicture;
Panel b, picture with blank word field;
Panel c, nonword; and Panel d, complete incongruent stimulus.

Note. The pictures are from Bildgeschichten [Picture stories] (pp. I , 22) by F. Meixner, n.d., Frankfurt, Federal Republic of Germany: Diesterweg. Copyright 1 975 by Diesterweg. Reprinted by permission. -->
</div></center>

<center>
<img src="/2023assets/1984Glaser_picture-word_fig2.svg">
<div class="figcaption">
図 課題 $\times$ SOA $\times$ 一致性における平均促進・抑制得点
<!-- Figure 2. Mean facilitation and inhibition scores in the Task X SOA X Congruency cells of Experiment I. (SOA = stimulus onset asynchrony.) -->
</div></center>

### 単語反復課題

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


# 文献

* ストループ効果 J. Ridley Stroop (1935) __Studies of Interference in Serial Verbal Reactions__, Journal of Experimental Psychology, 18, 643-662.
* サイモン効果 J. Richard Simon (1969) __Reactions Toward the Source of Stimulation__, Journal of Experimental Psychology, 81(1), 174-176.
* 絵画‐単語干渉効果 W. Glaser & F-J. Dungelhoff, (1984) __The Time Course of Picture-Word Interference__, Journal of Experimental Psychology: Human Perception and Performance, 10(5), 640-654.
* 絵画‐単語課題の意味促進 M-T. Bajo (1988) __Semantic Facilitation With Pictures and Words__, Journal of Experimental Psychology: Learning, Memory, and Cognition, 14(4), 579-589.
* 絵画命名課題における累積意味抑制 D. Howard+ (2006) __Cumulative semantic inhibition in picture naming: experimental and computational studies__, Cognition 100, 464–482.
* 絵画命名課題における言語間の干渉と促進 A. Roelofs+ (2016) __Electrophysiology of cross-language interference and facilitation in picture naming__. http://dx.doi.org/10.1016/j.cortex.2015.12.003
* 累積意味，意味ブロック，意味妨害効果 A. Roelofs+ (2018) __A unified computational account of cumulative semantic, semantic blocking, and semantic distractor effects in picture naming__. https://doi.org/10.1016/j.cognition.2017.12.007


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
