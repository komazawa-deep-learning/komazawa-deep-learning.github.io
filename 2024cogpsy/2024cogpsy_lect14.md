---
title: "第14回 2024年度開講 駒澤大学 認知心理学研究"
author: "浅川 伸一"
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="right">
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 10/Jan/2025<br/>
Appache 2.0 license<br/>
</div>

$$
\newcommand{\of}[1]{\left(#1\right)}
\newcommand{\Of}[1]{\left[#1\right]}
\newcommand{\KL}[2]{\operatorname{KL}\left(\left.{#1}\right\|{#2}\right)}
\newcommand{\given}[1]{\left|{#1}\right.}
\newcommand{\mb}[1]{\mathbf{#1}}
$$


##### Colab 実習ファイル

* [2024_1213royabel_BU_TD_multi_mnist.ipynb <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_1213royabel_BU_TD_multi_mnist.ipynb)
* [2024_1220Karapetian_demo.ipynb <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_1220Karapetian_demo.ipynb)

# トップダウン，ボトムアップネットワーク (Ullman lab)

* [原著論文 Able+(2023) Top-Down Network Combines Back-Propagation with Attention](https://arxiv.org/abs/2306.02415){:target="_blank"}
* [ソースコード GitHub](https://github.com/royabel/Top-Down-Networks){:target="_blank"}

* 生物学に着想を得たインストラクションモデルの学習法を提案
* ボトムアップ (BU)-トップダウン (TD) モデルを用い，1 つの TD ネットワークを学習と注意誘導の両方に使用
* 本論文の主な貢献は以下の通り

<!-- The paper propose a biologically-inspired learning method for instruction-models.
It uses a bottom-up (BU) - top-down (TD) model, in which a single TD network is used for both learning and guiding attention.
The key contributions of the paper are: -->

* 誤差信号からの学習とトップダウンの注意を組み合わせた新しいトップダウン機構を提案
* 従来研究を拡張し，より生物学的に妥当な学習モデルへの新たなステップを提供
* 生物学的学習のためのカウンター Hebb 学習機構の提案
* 従来のネットワークの中に，課題依存した独自の部分ネットワークを動的作成。生物学に着想を得た新しい Multi Task Learning (MTL) アルゴリズムの提示

<!-- * Propose a novel top-down mechanism that combines learning from error signals with top-down attention.
* Extending earlier work, offering a new step toward a more biologically plausible learning model.
* Suggest a Counter-Hebbian mechanism for biological learning.
* Present a novel biologically-inspired MTL algorithm that dynamically creates unique task-dependent sub-networks within conventional networks. -->


<div class="figcenter">
<img src="/2023assets/top_down_processing.png" width="33%">
</div>
<div class="figcaption" style="width:66%">

Bottom-up Top-down アプローチ<br/>
BU-TD アプローチは，双方向接続を持つ BU (青色) と TD (オレンジ色) ネットワークから構成される。
これらのネットワークは再帰的に動作できる。
1 つの TD ネットワークは，ダウン誤差信号の伝搬と TD 注意の両方に使用され，BU ネットワークは入力信号の処理を行う。
右図では，この概念をマルチタスク学習の設定で説明している。
I は入力信号 (例：視覚の場合の画像)，E はエラー信号 (例 損失勾配)，A は注意信号(例: 選択された物体，場所，課題) を示す。
</div>

### カウンター Hebb 学習<!--Counter-Hebbian Learning-->

<div class="figcenter">
<img src="/2023assets/update_rule.png" width="44%">
</div>
<div class="figcaption">
カウンター Hebb 学習

* 生物学的に動機づけられた学習機構。
* 古典的な Hebb 学習と同様に，カウンター Hebb 学習則はシナプスに接続されたニューロンの活動に基づいてシナプスを更新。
* 右図に示す Counter-Hebb 学習則は，古典的 Hebb 則 (左図) のように上流ニューロンからの逆発射ではなく，側方結合を介して接続された下流 (オレンジ色で示された) カウンターニューロンに依存する。
<!-- A biologically motivated learning mechanism.
Similar to the classical Hebbian learning, the Counter-Hebb learning rule update the synapse based on the activity of the neurons connected to the synapse.
However, the Counter-Hebb update rule, presented on the right, relies on the counterpart downstream (marked in  orange) counter neurons which is connected via lateral connections instead of a back firing from the upstream neuron as in the classical Hebb rule (on the left). -->
</div>

## 活性関数とバイアス<!--\label{section - activation functions}-->

活性化関数 $\sigma$, $\bar{\sigma}$ は，要素ごとの関数であれば何でもよい。
本研究では 2 つの関数に注目する。
1 つ目はニューラルネットワークでよく用いられる ReLU である。

$$
\text{ReLU}(x):=(x)_{+}=\begin{cases}
x & x > 0 \\
0 & x\leq 0
\end{cases}$$

もう 1 つは Gated-Linear-Unit(GaLU) で，BU-TD の構造を利用し，カウンターニューロンに応じてゲーティングを行う。
<!-- The activation functions $\sigma$, $\bar{\sigma}$, may be any element-wise functions.
In this work, we focus on two functions.
The first is ReLU which is commonly used for neural networks $ReLU(x):=(x)_+=\begin{cases} x & x > 0 \\ 0 & x
\leq 0\end{cases}$.
The second is Gated-Linear-Unit (GaLU), which exploits our BU-TD structure by gating according to the counter
neurons. -->

$$
\tag{Couter Gating Def}
\text{GaLU}(x):=\text{GaLU}(x, \bar{x}) := x \cdot I_{\bar{x} > 0} =
\begin{cases}
x & \bar{x} > 0 \\
0 & \bar{x} \leq 0
\end{cases}$$

ここで，$\bar{x}$ は $x$ のカウンターニューロン，$I$ は指標関数である。
<!-- Where $\bar{x}$ is the counter neuron of $x$, and $I$ is an indicator function. -->

GaLU には興味深い特性がある。
GaLU は，BU ネットワークと TD ネットワークの間に横方向の接続性を導入し，対になるニューロンの値に基づいて一時的にニューロンをオフにする。
その結果，各ネットワークは，特定の部分的なサブネットワークで動作するように，その対応するネットワークを効果的に誘導することができる。
ただし，この関数のゲート $\bar{x}$ に対する勾配は常にゼロである。
加えて，GaLU は $x$ と インジケータ $l_{\bar{x}>0}$ これは，ReLU 関数の勾配 $\frac{\partial}{\partial\bar{x}}\text{ReLU}\left(\bar{x}\right)=I_{\bar{x}>0}$ と正確に同じであるである。
この性質は，BP と等価なバックワードパスを構築するために，学習アルゴリズム で使われる。
<!-- GaLU has some interesting properties.
It introduces lateral connectivity between the BU and TD networks by temporarily turning off neurons based on the values of their counter neurons.
As a result, each network can effectively guide its counterpart to operate on a specific partial sub-network.
However, it is worth noting that the gradients of this function with respect to the gate $\bar{x}$ are always zero.
Additionally, GaLU applies a product of $x$ with the indicator $I_{\bar{x} > 0}$ which is exactly the gradient of the ReLU function: $\frac{\partial}{\partial \bar{x}} ReLU(\bar{x}) = I_{\bar{x} > 0}$.
This property will be used in section ~\ref{section: learning algorithm} to construct a backward pass that is equivalent to BP. -->


#### マルチタスク学習 $Multi-task Learning (MTL)

MTL アルゴリズムは，課題ごとに課題依存のサブネットワークを動的に学習する。
MTL アルゴリズムは 2 つのフェーズから構成される：予測のための TD パスと，それに続くBU パス，そして学習のためのもう 1 つの TD パスである。
選択された課題は TD ネットワークに入力を提供し，活性化は ReLU 非線形性を持つ下方への注意誘導信号を伝播する。
ReLU を適用することで，課題はニューロンの部分集合 (すなわち非ゼロ値) を選択的に活性化し，前ネットワーク内の部分ネットワークを構成する。
そして BU ネットワークは，ReLU と GaLU の合成を用いて入力画像を処理する。
GaLU 関数 (破線の矢印で示す) は，対応する TD 隠れ層によって BU 隠れ層をゲートする。
その結果，BU 計算は選択されたサブネットワーク上でのみ実行される。
最後に，予測ヘッドはトップレベルの BU 隠れ層に基づいて予測を生成する。
学習のために，同じ TD ネットワークが，予測ヘッドを起点として予測誤差信号を伝播するために再利用される。
この計算は GaLU のみで行われ (ReLU なし)，これにより負の値が許容される。
最後に，'Counter-Hebb’ 学習則は，隠れ層の活性化値に基づいて両方のネットワークの重みを調整する。
したがって，標準的モデルとは対照的に，すべての計算はネットワーク内のニューロンによって実行され，学習に外部計算 (例えば誤差逆伝播法) は使用されない。
あるいは，BU と TD の重みを共有するという制約のもとで，学習段階を標準的な BP で再現することもできる。
これにより同等の学習フェーズが得られる。
<!-- The MTL algorithm offers dynamically learning task-dependent sub-networks for each task.
The MTL algorithm comprises of two phases: a TD pass followed by a BU pass for prediction, and another TD pass for learning.
The selected task provides input to the TD network, and the activation propagates downward attention-guiding signals with ReLU non-linearity.
By applying ReLU, the task selectively activates a subset of neurons (i.e. non-zero values), composing a sub-network within the full network.
The BU network then processes an input image using a composition of ReLU and GaLU.
The GaLU function (denoted with dashed arrows) gates the BU hidden layers by their corresponding counter TD hidden layers.
As a result, the BU computation is performed only on the selected sub-network. Lastly, the prediction head generates a prediction based on the top-level BU hidden layer.
For learning, the same TD network is then reused to propagate prediction error signals, starting from the prediction head.
This computation is performed with GaLU exclusively (no ReLU), thereby permitting negative values.
Finally, the 'Counter-Hebb' learning rule adjusts both networks' weights based on the activation values of their hidden layers.
Therefore, in contrast with standard models, the entire computation is carried out by neurons in the network, and no external computation is used for learning (e.g. Back-Propagation).-->

<div class="figcenter">
<img src="/2023assets/MTL_schematic.png" width="49%">
</div>

**カウンター Hebbian 学習**<br/>

1. BU ネットワークを実行し，入力 $x$ を非線形活性化関数を用いて出力 $y$ へと写像
2. 誤差信号を計算
3. 誤差信号を用いて TD ネットワークを GaLu (非線形性なし) のバイアスブロックモードで実行
4. Counter-Hebb 学習則に従い，BU と TD パラメータの両方を更新

<!-- 1. Run BU network to map the input x to an output y with non-linear activation function.
2. Compute error signals.
3. Run the TD network using the error signals, in a bias-blocking mode with GaLu (no non-lineality).
4. Update both the BU and TD parameters according to the Counter-Hebb learning rule. -->

**マルチタスク学習**<!--Multi-task learning--><br/>

1. 課題ヘッドを使って，課題 $t$ を入力とする TD ネットワークを ReLU で実行する。
2. BU ネットワークを実行し，入力 $x$ を出力 $y$ に ReLU と GaLU の合成で対応付ける。
3. 誤差信号，すなわち BU 出力に対する損失 $L$ の勾配を計算： $\displaystyle -\frac{\partial L}{\partial y}$
4. 誤差信号を入力として，GaLU (非線形性なし) のバイアスブロックモードで TD ネットワークを実行
5. すべての重みを Counter-Hebb 学習則に従って更新する (課題ヘッドは除く，6 節参照)。

<!-- 1. Run the TD network with task t as input with ReLU, using the task head.
2. Run the BU network to map the input x to an output y with a composition of ReLU and GaLU.
3. Compute error signals, i.e. the gradients of a loss L with respect to the BU output: $\displaystyle -\frac{\partial L}{\partial y}$
4. Run the TD network using the error signals as inputs, in a bias-blocking mode with GaLU (no non-lineality).
5. Update all the weights according to th Counter-Hebb learning rule. (Excluding the task head, see section 6) -->

### Rao(1990) の世界モデル

<div class="figcenter">
<img src="/2024assets/1999Rao_Fig1.jpg" style="width:39%;">
<img src="/2024assets/1999Rao_fig2.jpg" style="width:44%;">
<div class="figcaption">

左 図 1. 内部世界モデルと隠れ状態の最適推定問題。
* (a): 環境の内部モデルに依存する生物が直面する一般的な問題の本質を伝えている(O'Reilly, 1996)。
その根底にある目標は，感覚的な測定値 $\mathbf{I}$ だけが与えられた環境の隠れた内部状態を，各時間瞬間に最適に推定することである。
* (b): 推定問題に対するカルマンフィルタに基づく解の例示。
内部モデルは状態遷移行列 $\bar{\mathbf{V}}$ と生成行列 $\bar{\mathbf{U}}$ によって共同で符号化され，フィルタはこの内部モデルを用いて環境の現在の内部状態$\mathbf{r}$ の最適推定値 $\hat{\mathbf{r}}$ を計算する。

<!-- Fig. 1. Internal world models and the problem of optimal estimation of hidden state.
(a) conveys the essence of the general problem faced by an organism relying on an internal model of its environment (from O’Reilly, 1996).
The underlying goal is to optimally estimate, at each time instant, the hidden internal state of the environment given only the sensory measurements mathbf{I}.
(b) depicts a Kalman filter-based solution to the estimation problem.
The internal model is encoded jointly by the state transition matrix bar{mathbf{V}} and the generative matrix bar{mathbf{U}}, and the filter uses this internal model to compute optimal estimates hat{mathbf{r}} of the current internal state mathbf{r} of the environment. -->

右 図 2. カルマンフィルタの概念図<!--Fig. 2. Schematic diagram of the Kalman filter.-->
</div>
</div>

<!-- ### 自由エネルギーモデル (Friston+2014 他)

<div class="figcenter">
<img src="/assets/2014Friston_Fig1.svg" style="width:44%">
<img src="/assets/2009Friston_box3.svg" style="width:44%">
</div> -->

<!-- <img src="/2023assets/2018Higgins_SCAN_fig1.svg" style="width:66%;">
<img src="/2023assets/2017Higgins_SCAN_fig1ja_.svg" style="widht:66%;">

<img src="/2024assets/1993Kawato_Fig1.svg" style="width:44%">
<img src="/2024assets/1993Kawato_fig2.svg" style="width:44%">
<img src="/2024assets/1993Kawato_fig3_.svg" style="width:44%"><br/>
<img src="/2024assets/1993Kawato_fig3all.jpg" style="width:66%"><br/> -->


## ERP モデル (Laszlo&Armstrong2014)
<!-- ## 1.1. The ERP model-->

下図は，先行モデルと同様，書記素入力の分散パターンを取り込み，隠れ層で複数の非線形変換を行った後，分散意味出力を生成するモデルの構造を示している。
<!-- In prior work, we began bridging the gap between computation and cognitive electrophysiology through development of the ERP model (Laszlo&Plaut, 2012).
The ERP model is heavily based on PDP models that preceded it (e.g., Harm&Seidenberg2004, Plaut+1996, Seidenberg&McClelland1989); Fig. 1 displays the architecture of the model, which, like its predecessors, takes a distributed pattern of orthographic input, and after multiple nonlinear transformations in hidden layers, producesa distributed semantic output. -->

<div class="figcenter">
<img src="/2024assets/2014Laszlo_Armstrong_PSP_fig1.svg" style="width:55%">
<div class="figcaption" style="width:66%">

**図 1.(A)** ERP モデルのアーキテクチャ。INH は 抑制性を表す。**(B)** シグモイド関数 (挿入図) と閾値上下のアルファ関数の形状。
$\alpha$ 素子では，$t\rightarrow\infty$ において $V\rightarrow\Theta$ となる。
<!-- Fig. 1.
(A) Architecture of the ERP model. INH stands for ‘‘inhibitory’’.
(B) The shape of the sigmoid function (inset), and of the alpha function above and below threshold. Note that
for alpha units, as $t\rightarrow\infty$, $V\rightarrow\Theta$. -->
</div>
</div>

ERP モデルと先行モデルとの重要な違いは，行動だけでなく ERP の構成要素の効果もシミュレーションする必要があることである。
具体的には，N400 (語彙的意味的アクセスを試みる構成要素と考えられている。Kutas&Federmeier2011 参照) に関連する効果である。
これを可能にするために，ERP モデルには PDP 読みモデルには典型的なものではない神経学的現実的な特性が与えられた。
まず，ERP モデルが先行するモデルと異なるのは，興奮と抑制の分離である。
この分離により，興奮性素子よりも抑制性素子の方が多いこと (EPSP が優勢であると考えられている ERP のシミュレーションには重要)，興奮と抑制の時間経過が別々であること，抑制には高速と低速の集団があることなど，神経学的には現実
的な特性がいくつか付与される。
しかし，ERP モデルには，真の皮質系にみられる数多くの特性が欠けている。
我々は，モデルにさらに神経の現実性を取り入れることで，より多くの N400 効果をシミュレートできるようになると考えた。
さらに，この現実性を提供することで，シミュレートされた効果の神経機構に関する洞察が得られる可能性がある。
これは，N400 の研究では基本的に未開拓の分野である。

#### アルファモデル
<!-- ## 1.2. The alpha model-->

ERP モデルでは，平均的な意味活性化は平均的な N400 振幅と関連している (脚注 2)。
したがって，繰り返しによって減少した N400 をシミュレートするモデルでは，反復が発生した際に平均的な意味活性化が減少することが示されなければならない。
つまり，素子には疲労する能力が備わっていなければならない。
この疲労は，意味層全体ではなく，単一素子に作用する形で選択的に発生することが重要である。
なぜなら，最近活性化していない素子は，反復ではなく新しい項目が提示された場合のように，最大限に活性化できなければならないからである。
したがって，個々の意味単位の活性化の望ましい動態は，活性化のピーク (最初の提示に対する反応) が徐々に減衰していくというものである。
これは，N400 反復効果の認知理論が提唱しているものであり，また反復による N400 振幅の減少にも必要である。
	重要なのは，この動態は $\alpha$ 関数によって正式に表現できるということである。
これは、神経計算において PSP をシミュレートするために使用される。
<!--In the ERP model, mean semantic activation is linked to mean N400 amplitude.(footnote 2)
Thus, for the model to simulate reduced N400s with repetition, it must display reduced mean semantic activation when repetitions occur.
That is, units must have the capacity to become fatigued. It is important that this fatigue occur selectively, acting on single units as opposed to the entire semantic layer, because units that have not recently been active must be able to activate to maximum, as when a novel item is presented instead of a repetition.
The desired dynamic of activation for individual semantic units is thus one where a peak of activation (response to a ﬁrst presentation) is followed by gradual decay, as posited by the cognitive theory of N400 repetition effects and also as necessary to reduce N400 amplitude with repetition.
Crucially, this dynamic can be formally expressed by the alpha function; used in neural computation to simulate PSPs: -->

$$\tag{1:アルファ関数}
V=\alpha t e^{-t/T}
$$
従来から用いられてきた $\alpha$ 関数 (例: Bugmann1997) では，V は膜電位 (電圧) の測定値，$\alpha$ はスケーリング定数，$t$ は単位が活性化してからの時間ステップ数，$T$ は $V$ がピークに達するタイミングを決定する自由パラメータである (例: David+2006)。
$\alpha$ 関数の形状は，式(1) で定義され，シミュレーションで使用される。
<!-- Eq. (1): The alpha function.
In the alpha function as used classically (e.g., Bugmann1997), V is a measure of membrane potential (voltage), a a scaling constant, t the number of time steps since a unit became active, and T a free parameter that determines when V peaks (e.g., David+2006).
The shape of the alpha function, as deﬁned in Eq. (1) and as used in our simulations, is displayed in Fig. 1. -->

$\alpha$ 関数が事象関連電位のシミュレーションで使用されていることから，我々のモデルでの使用に特に適している。
それは，所望の動作が生成されるからだけでなく，皮質事象関連電位が ERP 信号のソースであるためである (Fabiani+2007)。
$\alpha$ 関数の結果である $V$ は，意味素子の活性化がリンクされている N400 と同様に，電圧を表している。
実際，この関数の妥当性は，誘発反応の動的因果モデリングにおける類似の関数の使用によって裏付けられている (Dauizeau+2011 参照)。
この種の関数は，実際のニューロンにおける活性化の動力学に近似することが示されている (David+2006)。
したがって，N400 反復効果を実装するために必要な機能の動態に関する独立した観察結果，その効果の神経源，および $\alpha$ 関数の計算特性が，シミュレーションの機序を示唆する方向に収束している。
したがって，ERP モデルを N400 反復効果のシミュレーションに拡張しようとする試みにおいて，我々は興奮性素子の活性化を $\alpha$ 関数の包絡線 (式(1) で指定) に制限した。
<!-- That the alpha function is used in simulation of PSPs makes it especially appropriate for use in our model, not only because it produces the desired dynamic, but also because cortical PSPs are the source of the ERP signal (Fabiani+2007).
The result, V,of the alpha function represents a voltage, as does the N400, to which semantic unit activations are linked. Indeed, the appropriateness of this function is supported by use of an analogous function in dynamic causal modeling of evoked responses (see Dauizeau+2011), where this type of function has been shown to approximate activation dynamics in actual neurons (David+2006).
Thus, independent observations about the dynamics of the function needed to implement N400 repetition effects, the neural source of those effects, and the computational properties of the alpha function converge to suggest a mechanism for simulation. Therefore, in our attempt to extend the ERP model to simulation of N400 repetition effects, we constrained excitatory unit activations to the envelope of the alpha function (as speciﬁed in Eq. (1)). -->

<!-- 以下では，Laszlo&Plaut(2012) のモデルを ERP モデルと呼び続けるが，$\alpha$ 関数で制約されたモデルを $\alpha$ モデルと呼ぶ。 -->
$\alpha$ モデルにおける興奮性素子の活性化に $\alpha$ 関数 (上式) を適用することが，2 つのモデル間の唯一の違いである。(脚注 3)
以下に紹介するシミュレーションの目的は，$\alpha$ 関数で実装された選択的疲労要因が，N400 反復効果に対する正式に十分な機構的説明となるかどうかを判断することである。
<!-- In what follows, we will continue to refer to the Laszlo&Plaut(2012) model as the ERP model, but we will refer to the model constrained with the alpha function as the alpha model.
Application of the alpha function (Eq. (1)) to excitatory unit activation in the alpha model is the only distinction between the two models.(footnote 3)
The goal of the simulations presented below was to determine whether a selective fatigue factor, as implemented with the alpha function, constitutes a formally sufﬁcient mechanistic explanation for N400 repetition effects. -->

<div class="footnote">

2. 多数の皮質内抑制性電位 (IPSP) と興奮性電位 (EPSP) の遠心性和によって決定される電圧。
3. モデルの構造は他のすべての点で同一であるため，$\alpha$ モデルは，ERP モデルがシミュレーション可能なあらゆる現象をシミュレーションする能力を形式的に保持していることに留意されたい。

<!-- 2. A voltage determined by distal summation of numerous cortical IPSPs and EPSPs.
3. Note that, because the architecture of the models is in all other ways identical, the alpha model formally retains the ability to simulate any phenomenon the ERP model can simulate. -->
</div>


```python
import numpy as np
import matplotlib.pyplot as plt


def alpha_f(
    alpha: float = 1.0,
    # steps=np.array([t for t in range(0,100,1)], dtype=np.float32),
    steps=np.linspace(0, 100, 1000),
    T=20.0,
):

    V = alpha * steps * np.exp(-steps / T)
    return V

alpha = 0.4
V10 = alpha_f(T=10, alpha=1.0)
V20 = alpha_f(T=20, alpha=alpha)
plt.plot(range(len(V10)), V10, label=f"T=10, alpha={alpha}")
plt.plot(range(len(V20)), V20, label=f"T=20, alpha={alpha}")
plt.legend()
plt.show()
```

### 結果 (ERP)

各項目型について，第 1 回および第 2 回提示時の中央頭頂電極における ERP の平均値 (図 2) を計算した。
このデータセットにおける N400 効果に対応する時間ウィンドウに合わせてデータをトリミングした: 250ー450ミリ秒 (Laszlo&Federmeier2011)。
ERP とシミュレーション分析の一貫性を最大限に高めるため，これらのデータは，統計的に定義された関心領域，すなわち N400 窓の半値全幅 (FWHM) に再びトリミングされた。
<!--Grand-averaged ERPs (Fig. 2) were computed over the middle parietal electrode for each item type on ﬁrst and second presentation.
Data were trimmed to the time-window corresponding to N400 effects in this data set: 250–450 ms (Laszlo&Federmeier2011).
To maximize the consistency of ERP and simulation analyses, these data were again trimmed to a statistically-deﬁned window of interest, the full width at half-maximum (FWHM) of the N400 window. -->

<div class="figcenter">
<img src="/2024assets/2014Laszlo_Armstrong_PSP_fig2.svg" style="width:77%">
<div class="figcaption" style="width:77%">

**図 2. ERP とモデル (sERP) の時間および周波数領域のデータ**<br/>
時間領域の ERP データは，頭頂葉中央の電極部位における単語，頭文字語，擬似語，および非単語文字列の提示 1 回目と 2 回目に対する全体平均反応からなる。
同じデータが周波数領域で提示される。
時間領域の sERP データは，同じ種類の項目の提示 (1 回目と 2 回目) に対するすべての意味単位の平均反応からなる。
同じデータが周波数領域で提示される。
反復効果のシミュレーションに $\alpha$ 関数の適用が必要かどうかを評価するために実施された制御シミュレーションも，オリジナルの ERP モデルを使用して実施された。
このシミュレーションでは，すべての方法は上記で説明したものと同じであったが，$\alpha$ 関数は適用されなかった。
<!-- Fig.2. ERP and model (sERP) data in the time and frequency domains.
Time-domain ERP data consists of grand-averaged responses to ﬁrst and second presentations of words, acronyms, pseudowords, and illegal strings, over the middle parietal electrode site; the same data is presented in the frequency domain.
Time-domain sERP data consists of responses, averaged over all semantic units, to ﬁrst and second presentations of the same item types.
The same data is presented in the frequency domain.
A control simulation, performed in order to assess whether application of the alpha function is necessary for simulation of repetition effects, was also conducted using the original ERP model—in this simulation, all methods were identical to those described above, but the alpha function was not applied. -->
</div></div>


### N400 成分 (Federmeier&Laszlo(2009))

ERP 信号の特定の部分 (ERP `成分`と呼ばれることもある) は，意味情報の処理と特に関連している。
N400 は，刺激開始後 400ms 付近にピークを持つ負の電圧変動であることから呼ばれ，文の文脈において意味的に異常な単語 (例えば，「彼は靴下で温かいパンを広げた」Kutas&Hillyard1980b）に反応して最初に観察された。
Kutas&Hillyard は，このような変則的な単語が，さまざまな型の予期せぬ出来事の処理に広く関連している (例えば Duncan-Johnson&Donchin1977, Ruchkin+1975) 正の going ERP 成分である P300 を誘発すると予想した。
その代わりに，意味的に予期しない文末に対しては，予期した文末と比較して，より大きな陰性が観察された。
図 1 にその例を示す。
しかし，他の理由で予期せぬ単語，たとえば予期せぬ大きさで現れた単語は，予期した P300 反応を引き起こした(Kutas&Hillyard1980a)。
このように，意味に影響を与える操作とそうでない操作とでは，脳の扱いが異なることを示す最初のヒントとなった。
<!--A particular part of the ERP signal, sometimes called a `component` of the ERP, has been specifically associated with the processing of semantic information.
The N400—so-called because it is a negative-going voltage fluctuation that tends to peak around 400 ms after stimulus-onset—was first observed in response to words that were semantically anomalous in their sentence contexts (e.g., `He spread the warm bread with socks`; Kutas&Hillyard1980b).
Kutas and Hillyard anticipated that these anomalous words would elicit a P300, a positive-going ERP component that had been broadly linked to the processing of unexpected events of a wide variety of types (e.g., Duncan-Johnson&Donchin1977, Ruchkin+1975).
Instead, they observed a larger negativity to the semantically unexpected, as compared with the expected, sentence endings.
Figure 1 shows an example. However, words that were unexpected for other reasons—for example, because they appeared in an unexpected size— did elicit the anticipated P300 response (Kutas&Hillyard1980a).
This was thus the first hint that the brain treats manipulations that impact meaning differently from those that do not. -->


<div class="figcenter">
<img src="/2024assets/2009Federmeier_Laszlo_fig1.svg" style="width:55%;">
<div class="figcaption">

**図 1 N400文意一致効果**<br/>
N400 反応は，文の文脈で予期される単語では，予期されない単語に比べて振幅が小さくなる。
したがって，例えば dog という単語は `I take my coffee with cream and ...` という文の文脈の完了としての `suger` という単語よりも，刺激開始後 250ms から 500ms の間の平均振幅反応が小さくなる。
この図とそれ以降の図では，応答は中央から後方のチャンネルで示され，負の電圧が上にプロットされている。
<!-- Figure 1 N400 sentential congruency effect.
N400 responses are reduced in amplitude for words that are expected in a sentence context relative to those that are not.
Thus, for example, the word `dog` elicits smaller mean amplitude responses between 250 and 500 ms poststimulus onset than does the word `sugar` as a completion for the sentence context "I take my coffee with cream and ...."
In this and all subsequent figures, responses are shown at a middle, centro-posterior channel, with negative voltage plotted up. -->
</div></div>

その後の研究で，N400 は実際には意味的な意外性のマーカーではないことが明らかになった。
むしろ，N400 は潜在的に意味のある刺激に対する正常な反応の一部であるようだ。
ある面では，N400 は，一般にそれに先行する「感覚的」ERP 成分に似ている。
これらの成分は，特定のモダリティで刺激を認知することによって必ず誘発され (感覚成分の異なるパターンは，各モダリティの刺激に対する反応を特徴づける; 総説は Munte+2000 参照)，その特性 (振幅，潜時，分布) は，誘発事象の物理的特性によって大きく制御される。
N400 の誘発も同様に義務的であるように思われるが，モダリティを超えて意味のある刺激に対して N400 が観察されることから，感覚処理との関連性は低い。
他の点では，N400 はより「認知的」な構成要素とも類似しており，一般にこれらの構成要素は時間的に遅れて発生し，モダリティにかなり依存しない。
認知的な成分は，課題環境による情報処理要求の影響を強く受ける。
したがって，異なる課題環境では，同じ刺激でも，これらの構成要素に対する反応パターンが大きく異なることがあり，実際，このような構成要素は，外的誘因となる事象がなくても，その不在が有益であれば，誘発されることさえある (例えば Ruchkin+1975)。
N400 は，誘発刺激の文脈設定に強く影響されるという点で，この種の成分と少なくとも1つの特徴を共有している (例えば，同じ単語がリストとして提示されるか，文の完成として提示されるかで，N400 の誘発は大きく異なる)。
<!-- Subsequent research has established that the N400 is not actually a marker for semantic unexpectedness as such. Instead, the N400 seems to be part of the normal response to potentially meaningful stimuli.
In some respects, the N400 resembles the `sensory` ERP components that generally precede it in time.
These components are obligatorily elicited by the apprehension of a stimulus in a particular modality (a different pattern of sensory components characterizes the response to stimuli in each modality; for a review, see Munte+2000), and their characteristics (amplitude, latency, and distribution) are largely controlled by the physical properties of that eliciting event.
The elicitation of the N400 seems similarly obligatory, but less yoked to sensory processing, as N400s are observed to meaningful stimuli across modalities. In other respects, the N400 is also similar to more `cognitive` components, which generally occur later in time and are fairly modality-independent.
Cognitive components are highly affected by the information processing demands placed upon the person by the task environment.
Thus, in different task environments, the same stimulus may elicit a very different response pattern on these components, and, indeed, such components can even be elicited in the absence of an external triggering event, if that absence is informative (e.g., Ruchkin+1975).
The N400 shares at least one characteristic with this type of component, in that it is strongly affected by the contextual setting of an eliciting stimulus (e.g., the same word presented in a list or as a sentence completion can elicit very different N400s). -->

このように，N400 は ERP の構成要素「型」の興味深い融合である。
詳細は後述するが，N400 はあらゆるモダリティにおいて，さまざまなタイプの刺激によって誘発され，変調される。
しかし，すべての刺激が明確な N400 活動を誘発するわけではなく，誘発される刺激には，言葉や絵などの意味に関連するものが多い傾向がある (例えば Ganis+1996, Kutas+1987)。
このような刺激は，睡眠中のある段階 (Brualla+1998)，マスキング (Deacon+2000, Kiefer2002, Misra&Holcomb2003)，注意の瞬き (Rolke+2001, Vogel+1998) のように，偶発的かつ/またはほとんど意識せずに処理される場合でも N400 を誘発する。
これらの刺激に対する N400 の振幅 (潜時ではなく) は，感覚成分に影響しがちな知覚パラメータではなく，これらの刺激に対する意味処理のしやすさに特に関連する因子によって調節される (総説は Kutas&Federmeier2000 参照)。
意味に影響しない物理的・言語的変数の操作 (文法的誤りなど; Kutas&Hillyard1983) は N400 を変調させないし，N400 の効果は，音楽など他の構造化領域における予期せぬ出来事に対しても見られない (例えば Besson+1998)。
このように，N400 は意味の処理に機能的に特異的であり，次に述べるように，多くの研究が N400 を分散型意味記憶系における処理の電気生理学的マーカとして指摘している。
<!-- N400s are thus an interesting blend of ERP component `types.`
As will be discussed in more detail, N400s are elicited and modulated by stimuli of a wide variety of types in all modalities.
However, not all stimuli elicit clear N400 activity; those that do tend to be associated with meaning, such as words and pictures (e.g., Ganis+1996, Kutas+1987).
Such stimuli elicit N400s even when they are processed incidentally and/or with little conscious awareness, as during some stages of sleep (Brualla+1998), with masking (Deacon+2000, Kiefer2002, Misra&Holcomb2003), or during the attentional blink (Rolke+2001, Vogel+1998).
The amplitude (but not the latency) of the N400 to these stimuli is modulated, not by the kind of perceptual parameters that tend to affect sensory components, but by factors specifically related to the ease of semantic processing for these stimuli (for a review, see Kutas&Federmeier2000).
Manipulations of physical and linguistic variables that do not affect meaning (such as grammatical errors; Kutas & Hillyard, 1983) do not modulate the N400, and N400 effects are also not seen to unexpected events in other structured domains, such as music (e.g., Besson+1998).
Thus, the N400 seems to be functionally specific to the processing of meaning, and, as described next, a large body of research points to the N400 as an electro-physiological marker of processing in the distributed semantic memory system. -->

### N400 の神経回路

N400 が意味記憶の処理を反映しているのであれば，その神経的起源は，機能画像や神経心理学的研究で強調された脳領域と一致すると予想される。
N400 は広い頭皮分布を持ち，ほとんどの頭皮部位で見られるが，頭の中心部で最も大きくなる傾向がある。
このようなパターンは，分散した発生源を示唆する傾向があり，実際，電気生理学的データをモデル化する試みは，皮質の発生源が広範囲に集まっていることを指摘している (Haan+2000)。
しかし，この逆問題，つまり特定の頭皮パターンに関与する神経源を特定しようとする試みは，数学的に定義が難しく，N400 のように多面的で拡散した神経源については，特に近似すら困難である。
そのため研究者たちは，大脳皮質の表面やその中に埋め込まれた電極から電気生理学的信号を測定する頭蓋内記録や，脳磁図 (MEG) や事象関連光信号 (EROS) の測定など，他の手法に目を向けてきた。
<!--If the N400 reflects processing in semantic memory, then its neural origins would be expected to line up with the brain areas highlighted by functional imaging and neuropsychological studies.
The N400 has a wide scalp distribution; it can be seen at most scalp sites, although it tends to be largest over the center of the head. This pattern would tend to implicate a distributed source, and, in fact, attempts to model the electrophysiological data have pointed to a wide-spread collection of cortical sources (Haan+2000).
However, the inverse problem—that is, attempting to determine the neural sources responsible for a particular scalp pattern—is mathematically ill-defined and is particularly difficult to even approximate for multifaceted, diffuse sources, as the N400 seems to be.
Therefore, researchers have turned to other techniques, such as the use of intracranial recordings, which measure electrophysiological signals from electrodes placed on the surface of the cortex or implanted within it, or the measurement of the magnetoencephalogram (MEG) or the event-related optical signal (EROS), which each also track correlates of brain electrical activity with high temporal resolution but provide better spatial sampling. -->

多くの MEG 研究 (例えば Halgren+2002, Helenius&Salmelin2002, Helenius+1998, 1999, Kwon+2005, Pylkkanen&McElree2007, Simos+1997, Uusvuori+2008) と 1 つの EROS 研究 (Tse+2007) が，N400 の原因となる活動の局在化を試みてきた。
これらの研究では，かなり一貫して上・中側頭回，側頭頭頂接合部，内側側頭葉に原因があると指摘されている。
いくつかの研究では，背外側前頭皮質領域も関与している (Helenius+1998)。
これらの研究のいくつかは，左半球の活動のみを記録しているが，両半球の活動を記録した研究では，両半球の活動を認める傾向がある(意味処理における右半球の重要な役割を指摘するデータの増加と一致する)。
このように，画像研究によってアモーダルな意味処理に関与することが示唆されている脳領域と同じネットワークが，頭皮に記録されたN400活動の重要な一部であるようだ。
<!-- A number of MEG studies (e.g., Halgren+2002, Helenius&Salmelin2002, Helenius+1998, 1999, Kwon+2005, Pylkkanen&McElree2007, Simos+1997, Uusvuori+2008) and one EROS study (Tse+2007) have attempted to localize the activity responsible for the N400.
These studies have fairly consistently pointed to sources in the superior/middle temporal gyrus, the temporoparietal junction, and the medial temporal lobe. Dorsolateral frontal cortical regions have also been implicated in some studies (Helenius+1998).
Although several of these studies have recorded only over the left hemisphere, studies that have recorded activity from both hemispheres have tended to find bilateral activity (consistent with growing data pointing to an important role for the right hemisphere in meaning processing; see, e.g., the review by Federmeier+2008), although the right hemisphere source is often found to be weaker.
Thus the same network of brain areas that have been implicated in amodal semantic processing by imaging studies seem to be an important part of the source of scalp-recorded N400 activity. -->

MEG と EROS 研究は，意味処理に関連する脳電気活動の発生源だけでなく，その時間経過に関する情報も提供できる。
例えば Halgren+(2002) のデータによると，頭皮記録 N400 は，左上側頭回の後半分で発症後 250ms 頃に始まる活動の波を反映しており，365ms までに前方と腹側に広がって左側頭葉の大部分を包含し，N400 反応のピーク (370～500ms の間) までに右半球の前側頭葉と両側の前頭葉に広がる。
唯一の EROS N400 研究 (Tse+2007) では，上側頭葉から前頭葉へ，そして再び前頭葉へと，同様の活動の進行が見られた。
これらの所見は，てんかん手術の術前評価を受ける患者の頭蓋内記録を用いた研究によって補完される。
EROS や MEG では (信号強度に対する様々な物理的制限のために) 皮質深部の発生源を確認することは困難であるが，N400 誘発パラダイムの頭蓋内データは，通常，内側側頭葉と下側頭葉 (てんかん発生源が最も多い) から収集されている。
頭蓋内研究では，意味プライミング，意味異常，反復，言語記憶に対する感受性において，頭皮記録N400と密接なパターンを示す前内側側頭葉の信号源が同定されている(Elger+1997，Fernandez+2001，Guillem+1996，Halgren+1994，Halgren+1994，McCarthy+1995，Nobre+1994, Nobre&McCarthy1994, Smith+1986）。
N400 様活動は，MEG/EROS で摘出された中側頭や上側頭，下側頭や前頭前野など，他の多くの脳領域からの頭蓋内記録でも観察されている。
頭蓋内記録から得られる空間的情報は，個人でサンプリングできる記録部位が比較的少ないという事実によって制限されている(また，それらの部位の配置は，研究上の関心よりもむしろ臨床上の関心によって決定されるため）。
しかし，このような研究のデータから，N400 は，高次知覚野，マルチモーダル処理野，さらには扁桃体のような情動・動機づけ関連野など，分散した脳領域の活動を反映していることが示唆される。
これらの領域はすべて，刺激開始後約250ミリ秒から500ミリ秒の間に，同じような時間スパンで活動を示す。
<!-- MEG and EROS studies can provide information not only about the source of brain electrical activity associated with semantic processing but also its timecourse.
Halgren+(2002) data, for example, suggest that the scalp-recorded N400 reflects a wave of activity beginning around 250 ms after-onset in the posterior half of the left superior temporal gyrus, spreading forward and ventrally to encompass most of the left temporal lobe by 365 ms, and then spreading to the anterior temporal lobe in the right hemisphere and to the frontal lobe bilaterally by the peak of the N400 response (between 370 and 500 ms).
The only EROS N400 study (Tse+2007) found a similar progression of activity from the superior temporal lobe to frontal areas and then back again.
These findings are complemented by work using intracranial recordings, typically from patients undergoing preoperative evaluation for epilepsy surgery.
Whereas deep cortical sources may be difficult to see with EROS and MEG (because of various physical limitations on the signal strength), intracranial data in N400-eliciting paradigms have typically been collected from the medial and inferior temporal lobe (where epileptic sources are most frequent).
Intracranial studies have identified a source in the anterior medial temporal lobe that patterns closely with the scalp-recorded N400 in its sensitivity to semantic priming, semantic anomaly, repetition, and verbal memory (Elger+1997, Fernandez+2001, Guillem+1996, Halgren+1994, Halgren+1994, McCarthy+1995, Nobre+1994, Nobre&McCarthy1994, Smith+1986).
N400-like activity has also been observed in intracranial recordings from a number of other brain areas, including the middle and superior temporal areas picked out by MEG/EROS, and inferior temporal and prefrontal cortical areas.
The spatial information available from intracranial recordings is limited by the fact that relatively few recording sites can be sampled in any individual (and because the placement of those sites is determined by clinical rather than research concerns).
However, data across such studies suggest that the N400 reflects activity in a distributed set of brain regions, including higher order perceptual areas, multimodal processing areas, and even emotion-and motivation-related areas, such as the amygdala.
These areas all show activity over a similar time span, between about 250 and 500 ms after stimulus onset. -->

もし N400 がアモーダル (またはマルチモーダル) な意味系の活動を反映しているのであれば，そのような活動は意味に関連するあらゆる刺激に反応するはずである。
実際，N400 は，話し言葉，書き言葉，手話による言葉，発音可能な偽単語 (例 pank) や親しみのある略語 (例 VCR) などの言葉に似たものなど，あらゆる種類の言語刺激に対して記録されている (Holcomb&Neville1990, Kutas+1987, Laszlo&Federmeier2008)。
N400 は環境音 (動物の鳴き声，電話の呼び出し音など)，線画や情景 (Ganis&Kutas2003, Ganis+1996, Nigam+1992)，顔 (Barrett&Rugg1989, Bobes+1994)，映画 (Sitnikova+2003)，ジェスチャー (Kelly+2004, Wu&Coulson2005) など，意味はあるが非言語的な刺激に対しても観察される。
N400 反応のモダリティ非依存性のもう 1 つの重要な側面は，N400 振幅が刺激のモダリティや種類に関係なく，刺激間の意味的関係によって調節されることである。
すなわち，例えば絵に対する N400 反応は，別の絵との意味的関係 (Barrett&Rugg1990b, McPherson&Holcomb1999) だけでなく，視覚的に提示された単語や文 (Federmeier&Kutas2002, Wich+2003)，聴覚的に提示された単語 (Pratarelli1994)，あるいは匂い(Grigor+1999, Sarfarazi+1999) でも影響を受ける。
このようなクロスモダリティ効果は，対応するイン・モダリティ効果よりも弱いことがあるが (Anderson&Holcomb1995)，刺激をマスクして戦略的な注意主導型処理の寄与を減らしても持続する (Eddy+2006, Kiyonaga+2007)。
このように，N400 は感覚モダリティや刺激の種類にかかわらず，共通の処理段階で生じるようである。
<!-- If the N400 reflects activity in an amodal (or multimodal) semantic system, then such activity should be seen in response to the full range of stimuli that are associated with meaning.
And, in fact, N400s have been recorded to all types of linguistic stimuli, including spoken, written, and signed words, and word-like items such as pronounceable pseudowords (e.g., pank) and familiar acronyms (e.g., VCR) (Holcomb&Neville1990, Kutas+1987, Laszlo&Federmeier2008).
N400s are also observed to meaningful but nonlinguistic stimuli such as environmental sounds (e.g., animal sounds, telephone ringing; Chao+1995, Van Petten&Rheinfelder1995), line drawings and scenes (Ganis&Kutas2003, Ganis+1996, Nigam+1992), faces (Barrett&Rugg1989, Bobes,+1994), movies (Sitnikova+2003), and gestures (Kelly+2004, Wu&Coulson2005).
Another important aspect of the modality-independence of the N400 response is that N400 amplitudes are modulated by semantic relationships between stimuli, irrespective of stimulus modality or type.
That is, the N400 response to a picture, for example, can be affected not only by its semantic relationship with another picture (Barrett&Rugg1990b, McPherson&Holcomb1999), but also with a visually presented word or sentence (Federmeier&Kutas2002, Wich+2003), an auditory word (Pratarelli1994)or even a smell (Grigor+1999, Sarfarazi+1999).
Such cross-modal effects are sometimes weaker than corresponding within-modality ones (Anderson&Holcomb1995) but persist even when stimuli are masked to reduce the contribution of strategic, attentionally driven processing (Eddy+2006, Kiyonaga+2007).
Thus, the N400 seems to occur at a processing stage that is common across sensory modality and stimulus type. -->

一方，もし意味系がモダリティ依存的な処理領域とモダリティ非依存的な処理領域を含んでいるならば，N400 の発生源は入力の種類や単語の種類によって変化することが予想される。
実際，異なる種類の刺激によって誘発される N400 の頭皮分布には信頼できる違いがある。
視覚的に提示された単語に対する N400 は，内側，中心-後方に焦点があり，左半球よりも右半球で大きくなることが多い (電気双極子の正確な方向によっては，左半球の刺激源が右半球の電極部位に極大を持つ電気活動を誘発することがあるので，右半球の関与が大きいことを示唆するものと考えるべきではない, Kutas&Hillyard1982)。
代わりに，聴覚的な単語に対する N400 は，より中心的な頭皮分布を示す (Holcomb&Anderson1993, McCallum+1984)。
環境音に対する N400 は，聴覚的な単語に対するN400と同様の頭皮分布を示すが，大脳半球の非対称性は異なる。
これは，言語刺激の処理には左半球の偏りがあるが，非言語刺激の処理には右半球の偏りがあるとする見解と一致している (Van Petten&Rheinfelder1995)。
絵や情景に対する N400 反応は，視覚的に提示された単語に対する反応よりも明らかに前方である (Ganis+1996，Holcomb&McPherson1994)。
興味深いことに，抽象的な単語と比較して具体的な単語に対する N400 反応でも同様の前方シフトが見られる (Holcomb+1999, Kounios&Holcomb1994, Lee&Federmeier2008)。
このような分布の違いの正確な性質は完全には理解されていないが，その存在は，意味処理が異なる種類の刺激に対して部分的に非重複な神経領域セットからサンプリングされることを示唆している (したがって，機能的にも非同一である可能性がある)。
<!-- On the other hand, if the semantic system contains modality-dependent as well as modality-independent processing areas, then the source of the N400 might be expected to shift for different kinds of inputs or different kinds of words.
In fact, there are reliable differences in the scalp distribution of the N400 elicited by different types of stimuli.
N400s to visually presented words have a medial, centro-posterior focus and are often larger over the right than the left hemisphere (which should not be taken to suggest greater involvement from the right hemisphere, as, depending on the precise orientation of the electrical dipole, a left hemisphere source can elicit electrical activity with a maxima over right hemisphere electrode sites) (Kutas&Hillyard1982).
N400s to auditory words, instead, manifest a more central scalp distribution (Holcomb&Anderson1993, McCallum+1984).
Environmental sounds elicit a scalp distribution similar to that seen for auditory words, but with a different pattern of hemispheric asymmetry.
This is consistent with views that posit a left hemisphere bias for the processing of verbal stimuli but a right hemisphere bias for the processing of nonverbal stimuli (Van Petten&Rheinfelder1995).
N400 responses to pictures and scenes are notably more anterior than those to visually presented words (Ganis+1996, Holcomb&McPherson1994), perhaps reflecting enhanced contributions from brain areas involved in visual-or imagery-related processing.
Interestingly, a similar anterior shift is seen for the N400 responses to concrete, as compared with abstract, words (Holcomb+1999, Kounios&Holcomb1994, Lee&Federmeier2008).
Although the precise nature of these distributional differences is not entirely understood, their existence suggests that semantic processing samples from partially nonoverlapping sets of neural areas for different types of stimuli (and may therefore be functionally nonidentical as well; see, e.g., Federmeier&Kutas2001), consistent with the Hebbian cell-assembly type of accounts of semantics that have already been discussed. -->

### N400 と概念構造と柔軟性

N400 が意味記憶の処理のマーカーであるならば，行動研究で明らかにされた概念レベルの構造を反映するはずである。
N400 は，文の検証に関する ERP 研究で見られるように，知識の分類学的構成に敏感である (All dogs are animals/furniture; Fischler+1983)。
N400 はまた，典型性によって段階的にカテゴリーメンバーシップに敏感であり (図 2)，カテゴリーラベルの手がかりの後では，典型的でないカテゴリーメンバーよりも典型的なカテゴリーメンバーにより大きな促進 (振幅の減少) が見られる (例えば `DOG` の手がかりの後では，`Bichon Frise` よりも `Collie` に反応する N400 が小さい; Harbin+1984, Heinze+1998, Polich1985, Stuss+1988)。
より一般的には，N400 振幅は，物理的，機能的，感情的，認知的特徴の共有を含む，刺激間の多くのタイプの意味的類似性によって調節される (例えば Barrett&Rugg1990a,b, Bentin+1985, Holcomb&Neville1990, Kellenbach+2000, Zhang+2006)。
このような感度は，類似性やカテゴリー関係に気づくよう指示されたときだけでなく，より暗黙的な条件下でも生じる。
例えば，文処理 (あからさまな行動課題なしに，参加者が単に理解のために読む場合) において，予想される語尾に対するカテゴリー的類似性は，文脈的に変則的な文の完成 (例えば「彼はパスをキャッチし，タッチダウンを決めた)。
このように，特定の課題状況にとって意味関係が無関係な場合でも，N400 の処理は概念知識の構造に影響されるようである。
最後に，N400 の効果は新しく学習したカテゴリーでも観察され，訓練セットと共通する特徴が多い新しい模範例に対する N400 は小さい (Gratton+2009)。
<!--If the N400 is a marker of processing in semantic memory, then it should reflect the kind of conceptual-level structure uncovered in behavioral studies.
The N400 is sensitive to the taxonomic organization of knowledge, as can be seen in ERP studies of sentence verification (with smaller N400s to `animals` than `furniture` in "All dogs are animals/furniture"; Fischler+1983).
The N400 is also sensitive to category membership in a manner graded by typicality (Figure 2), with greater facilitation (amplitude reduction) for more than less typical category members following a category label cue (e.g., smaller N400s in response to `Collie` than `Bichon Frise` after the cue `DOG`; Harbin+1984, Heinze+1998, Polich1985, Stuss+1988).
More generally, N400 amplitudes are modulated by semantic similarity of many types between stimuli, including shared physical, functional, affective, and cognitive features (e.g., Barrett&Rugg1990a,b, Bentin+1985, Holcomb&Neville1990, Kellenbach+2000, Zhang+2006).
This sensitivity arises not only when participants are directed to notice or judge similarity or categorical relations, but also under more implicit conditions.
For example, during sentence processing (when participants simply read for comprehension without any overt behavioral task), categorical similarity to an expected ending produces N400 facilitation for even contextually anomalous sentence completions (e.g., "He caught the pass and scored another touchdown.
There was nothing he enjoyed more than a good game of baseball"; Federmeier&Kutas1999, 2001).
Thus, even when semantic relationships are irrelevant for a particular task situation, N400 processing seems to be influenced by the structure of conceptual knowledge.
Finally, N400 effects can be observed even for newly learned categories, with smaller N400s to novel exemplars that share more features in common with the training set (Gratton+2009). -->

<div class="figcenter">
<img src="/2024assets/2009Federmeier_Laszlo_fig2.svg" style="width:49%">
<div class="figcaption">

**図 2 N400カテゴリー典型性効果**<br/>
「果物の一種」のようなカテゴリーラベルの手がかりに対して，N400 反応は，非メンバー (例えば 10 セント硬貨) に対してカテゴリーメンバー (例えば「リンゴ」や「さくらんぼ」）に対して振幅が減少し，低い典型性 (例えば「チェリー」) よりも高い典型性 (例えば「リンゴ」) に対してより減少する。
<!-- Figure 2 N400 category typicality effects.
In response to a category label cue, such as "A type of fruit," N400 responses are reduced in amplitude to category members (e.g., `apple` or `cherry`) relative to nonmembers (e.g., `penny`) and are more reduced to high typicality (e.g., `apple`) than to low typicality (e.g., `cherry`) category exemplars. -->
</div></div>


N400 は意味記憶における能動的な処理を反映すると仮定されているため，情報使用の動的特性，すなわち，概念情報にアクセスする頻度や直近の頻度，意味のある項目が出現する文脈や過去に出現した文脈などの要因にも敏感であるはずである。
図 3 からわかるように，N400 振幅は確かに単語頻度に影響され，頻度の高い単語に対する N400 反応は低い単語に対する反応よりも小さい (促進される) (Muente+2001, Rugg1990, Van Petten&Kutas1990)。
図 3 が示すように，N400 は反復にも敏感であり (Rugg1985, Van Petten+1991)，認識記憶によって調節される (Chao+1995, Friedman1990, Smith+1986)。
さらに，記憶による N400 へのこのような影響は，意味記憶ではなくエピソード記憶に障害のある健忘患者で保たれる (Olichney+2000)。
最後に，N400 は文脈に非常に敏感である。
実際，N400 の測定法として最も重要な用途の 1 つは，言語における文脈効果の研究である。
N400 の振幅は，文脈が 1 つの単語や絵であろうと，文，談話，映画であろうと，その文脈に対する意味項目の適合性によって調節される (言語的文脈については Kutas&Federmeier2000 の総説を，非言語的文脈については West&Holcomb2002, Sitnikova+2003 などを参照)。
N400 に対する文脈の効果は段階的であり，N400 の振幅は，文脈適合性の尺度である「クロース確率」(与えられた文の断片を特定の単語で完結させることを選択する人の割合; Taylor1953) などと強い負の相関を示す。
このように，N400 は，概念処理の行動研究が強調してきた構造と柔軟性の両方を指標化している。
<!-- Because the N400 is assumed to reflect active processing in semantic memory, it should also be sensitive to dynamic properties of information use—that is, to factors such as the frequency and recency with which conceptual information has been accessed and to the context in which a meaningful item occurs or has occurred in the past.
As can be seen in Figure 3, N400 amplitudes are indeed affected by word frequency, with smaller (facilitated) N400 responses to high than to low frequency words (Muente et al., 2001; Rugg, 1990; Van Petten & Kutas, 1990).
As Figure 3 shows, the N400 is also sensitive to repetition (Rugg1985, Van Petten+1991) and is modulated by recognition memory (Chao+1995, Friedman1990, Smith+1986).
Furthermore, such effects of memory on the N400 are preserved in amnesic patients (Olichney+2000), who are impaired in episodic—but not semantic—memory.
Finally, the N400 is highly sensitive to context; indeed, one of the most important uses of the N400 as a measure has been in studies of context effects in language. N400 amplitudes are modulated by the fit of a meaningful item to its context, whether that context is a single word or picture, or a sentence, discourse, or movie (for verbal contexts, see review by Kutas&Federmeier2000, for nonverbal contexts, see, e.g., West&Holcomb2002, Sitnikova+2003).
Context effects on the N400 are graded, with the amplitude of the N400 showing a strong negative correlation with measures of contextual fit, such as `cloze probability` (the percentage of people who would choose to complete a given sentence fragment with a particular word; Taylor1953).
Thus, the N400 indexes both the structure and the flexibility that behavioral studies of conceptual processing have highlighted. -->

<!-- A 5 mV  Repetition 400 ms Word: 1st presentation Word: 2nd presentation  B 5 mV  Frequency Low frequency word High frequency word  C Neighborhood size 5 mV High N string Low N string -->

<div class="figcenter">
<img src="/2024assets/2009Federmeier_Laszlo_fig3.svg" style="width:77%;">
<div class="figcaption">

**図 3 N400 に対する反復，頻度，書記近傍のサイズの効果**<br/>
**(A)** リスト形式の単語を 2 回目に提示したときに生じる N400 は，1 回目に提示したときに生じる N400 よりも小さい。<br/>
**(B)** 高頻度語は低頻度語よりも N400 が小さい。<br/>
**(C)** 無意味文字列は，書記近傍サイズが大きい場合，書記近傍サイズが小さい場合よりも N400 が大きくなる。
これらの因子は，意味的一致性とともに，N400 振幅の最も重要な決定因子である。
<!-- Figure 3 Effects of repetition, frequency, and orthographic neighborhood size on the N400.
In (A), the N400 elicited by the second presentation of a word in a list format is smaller than that to the first presentation.
In (B), higher frequency words elicit smaller N400s than lower frequency words.
In (C), meaningless strings with high orthographic neighborhood size elicit larger N400s than those with low orthographic neighborhood size.
These factors, along with semantic congruency, comprise the most important determinants of N400 amplitude. -->
</div></div>



##### Bayes の定理

$$
P(X,Y) = P(X|Y)P(Y) = P(Y|X) P(X)
$$

$$\begin{aligned}
P(Y|X) &= \frac{P(X|Y)P(Y)}{P(X)} &= \frac{\text{尤度 $\times$ 事前確率}} {\text{証拠}}\\
&= \frac{P(X|Y)P(Y)}{P(X|Y)P(\neg Y)+ P(X|Y)P(Y)}
\end{aligned}$$

* [Puppy book, ベイズ統計モデリング: R,JAGS, Stan によるチュートリアル](https://www.amazon.co.jp/dp/4320113160/){:target="_blank"} を超えて

* [原著 Doing Bayesian Data Analysis: A Tutorial Introduction with R, JAGS, and STAN](https://www.amazon.com/dp/0124058884/){:target="_blank"}
* [原著 A Tutorial Introduction with R](https://www.amazon.com/dp/B004QOB460/){:target="_blank"}


#### KL ダイバージェンス

KL ダイバージェンスは，2 つの分布間の距離に相当する量を与える。
だが KL ダイバージェンスは通常の距離と異なり非対称で，どちらの分布を基準に考えるかによって値が異なる。
すなわち $\KL{P}{Q}\ne\KL{Q}{P}$ です。
下図 (fig:forward_reverse_KL) にその関係を示した。
青い曲線は真の事後分布とします，例えば双峰性の分布であるとする。
緑の分布は最適化を介して青い密度に適合させる変分近似による分布を表すものとする。
これを **フォワード KL** と呼ぶ。
図 (fig:forward_reverse_KL) 右のように，双峰性の真の分布を単峰性の分布で近似することを考える。
このとき，一方の峰に当てはまるように調整すると，もう一方の峰の値についての当てはまりが悪くなり結果として右下図のような裾野の広い分布を得ることになる。
反対に，緑の単峰性の分布を青の双峰性の分布で近似しようとする **リバース KL** を考える。
このとき基準となる真の分布である単峰性の分布の確率密度がほとんど 0 の領域では，推定する分布がどのような値を取ろうとも KL ダイバージェンスの値に影響を与えないため，いずれか一方の峰が真の分布と重なるような値を得ることになる。

<div class="figcenter">
<img src="/assets/forward-KL.png" width="33%">
<img src="/assets/reverse-KL.png" width="33%">
<div class="figcaption">

左: フォワード KL, 右: リバース KL

KL ダイバージェンスの非対称性
[A Beginner's Guide to Variational Methods: Mean-Field Approximation](https://blog.evjang.com/2016/08/variational-bayes.html) より
</div></div>

分布が 近い とはどういう意味かというと
平均場変分ベイズ（最も一般的なタイプ）は，2 つの分布間の距離として 逆 KL ダイバージェンスを使用する。
<!-- % Reverse KL divergence measures the amount of information (in nats, or units of $\frac{1}{\log(2)}$ bits) required to "distort" $P(Z)$ into $Q_\phi(Z)$.
% We wish to minimize this quantity with respect to $\phi$.-->
条件付き分布の定義により，$p\of{z\given{x}}=p\of{x,z}p\of{x}$
この式を，オリジナルの KL ダイバージェンスの定義式に代入すれば，
<!-- % By definition of a conditional distribution, $p\of{z\given{x}}=p\of{x,z}p\of{x}$.
% Let's substitute this expression into our original KL expression, and then distribute: -->

このようなフォワード，リバース KL ダイバージェンスの値から VAE の表現性能などを考えることが可能です。

<!--
## Colab 実習ファイル

* [2024_1205Karapetian_RNN.ipynb <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_1205Karapetian_RNN.ipynb){:target="blank"} -->


## 参考資料

* [7–1 リカレントニューラルネットワーク](/2022/6657.pdf){:target="_blank"}
* [7–1 リカレントネットワークによる文法学習](/2022/6685.pdf){:target="_blank"}

* [Bahdanau and Loung attentions <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_1022Two_attentions_additive_and_multiplicative_Seq2seq.ipynb)

* [系列探索と逆行流: 視覚野における双方向情報フローの計算モデル](/2023cogpsy/2021Ullman_bu_td_ja.pdf){:target="_blank"}
* [ボトムアップ・トップダウンの反復処理による画像解釈](/2023cogpsy/1995Ullman_bidirectional_cortex_ja.pdf){:target="_blank"}


### A. 最大事後確率法：貧乏人の Bayes 推論
<!-- ### MAXIMUM A POSTERIORI: POOR MAN’S BAYESIAN INFERENCE-->

統計的信号処理の文献で最もよく使われる手法の 1 つが最大事後確率法 (MAP: Maximum A Posteriori 法) である。
MAP は，パラメータベクトル $\theta$ を確率変数と仮定し，$\theta$ に事前分布 $p(\theta)$ を課すことから，しばしばベイズ的と呼ばれる。
ここでは，MAP 推定とベイズ推定との類似点と相違点を明らかにする。
$x$ を観測値，$\theta$ を未知量とすると，MAP 推定は次のように定義される。
<!-- One of the most commonly used methodologies in the statistical signal processing literature is the maximum a posteriori (MAP) method.
MAP is often referred to as Bayesian, since the parameter vector θ is assumed to be a random variable and a prior distribution pθ is imposed on θ.
In this appendix, we would like to illuminate the similarities and differences between MAP estimation and Bayesian inference.
For x the observation and θ an unknown quantity the MAP estimate is defined as -->

$$ \hat{\theta}_ {\text{MAP}} = \arg\max_ {\theta} p(\theta\vert x)\tag{A.1} $$

Bayes 則を用いて， MAP 推定は次式より得られる:
<!-- Using Bayes’ theorem, the MAP estimate can be obtained from  -->

$$
\hat{\theta}_{\text{MAP}} = \arg\max_{\theta} p(x|\theta)\,d\theta
\tag{A.2}$$

ここで $p(x|\theta)$ は観測値の尤度である。
MAP 推定値は (A.1) よりも (A.2) から求めた方が簡単である。
ベイズの定理に基づく (A.1) の事後確率は次式で与えられる:
<!-- where p(x|θ) is the likelihood of the observations.
The MAP estimate is easier to obtain from (A.2) than (A.1).
The posterior in (A.1) based on Bayes’ theorem is given by -->

$$ p(\theta\vert x) = \frac{p(x\vert\theta)p(\theta)}{\int p(x\vert\theta)p(\theta) d\theta}\tag{A.3} $$

であり 式 (A.3) の分母にベイズ積分を計算し，$\theta$ を周辺化する必要がある。
<!-- and requires the computation of the Bayesian integral in the denominator of (A.3) to marginalize θ.-->

以上より，MAP 推定量も Bayes 推定量も $\theta$ を確率変数と仮定し，Bayes の定理を用いることは明らかであるが，その類似性はそこに止まっている。
ベイズ推定では事後分布を用いるため，$\theta$ を周辺化する必要がある。
これに対して，MAP では事後値の最頻値を用いる。
ベイズ推定は，MAP と異なり，$\theta$ に関する利用可能なすべての情報を平均化すると言える。
したがって MAP は「貧乏人の Bayes 推論」と言える。
<!-- From the above, it is clear that both MAP and Bayesian estimators assume that θ is a random variable and use Bayes’ theorem, however, their similarity stops there.
For Bayesian inference, the posterior is used and thus θ has to be marginalized.
In contrast, for MAP the mode of the posterior is used.
One can say that Bayesian inference, unlike MAP, averages over all the available information about θ.
Thus, it can be stated that MAP is more like “poor man’s” Bayesian inference. -->

EM は $\theta$ の MAP 推定値も得るために用いることができる。
Bayes の定理を用いて，次のように書くことができる:
<!-- The EM can be used to also obtain MAP estimates of θ.
Using  Bayes’ theorem we can write -->

$$ \begin{aligned}
\ln p(\theta\vert x) & = \ln p(x,\theta) − \ln p(x)\\
&= \ln p(x\vert\theta) + \ln p(\theta) − \ln p(x).
\end{aligned}\tag{A.4} $$

上式は，下記のように書くことができる:
<!-- 「EM アルゴリズムの別見解」節 の ML-EM の場合と同様の枠組みで，次のように書くことができる: -->
<!-- Using a similar framework as for the ML-EM case in the section “An Alternative View of the EM Algorithm,” we can write-->

$$\begin{aligned}
\ln p(\theta\vert x) &= F(q,\theta) + D_ {\text{KL}}(q\vert\vert p) + \ln p(\theta) − \ln p(x)\\
&\ge F(q,\theta) + \ln p(\theta) − \ln p(x),
\end{aligned}\tag{A.5}$$

ここで，$\ln p(x)$ は定数である。
(A.5) 式右辺は，EM アルゴリズムと同様に交互に最大化することができる。
$q(z)$  に関して最適化すると，先に説明した ML の場合と同じ E-step が得られる。
$\theta$ に関して最適化すると，目的関数が $\ln p(\theta)$  の項を含むので，異なるM-step が得られる．
<!-- 一般に MAP-EM アルゴリズムの M-ステップは，ML の場合よりも複雑であり，例えば  [30]  や [31] を参照されたい。
厳密に言えば，このようなモデルでは，MAP  推定は $\theta$ 確率変数のみに使用され，ベイズ推定は隠れ変数 $z$ に使用される。 -->
<!-- where in this context ln p(x) is a constant.
The right-hand side of (A.5) can be maximized in an alternating fashion as in the EM algorithm.
Optimization with respect to q(z) gives an identical E-step as for the ML case previously explained.
Optimization with respect to θ gives a different M-step since the objective function now contains also the term ln p(θ).
In general, the M-step for the MAP-EM algorithm is more complex than in its ML counterpart, see for example [30] and [31].
Strictly speaking, in such a model MAP estimation is used only for the θ random variables, while Bayesian inference is used for hidden variables z.-->
