---
title: "第12回 2024年度開講 駒澤大学 認知心理学研究"
author: "浅川 伸一"
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="right">
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 13/Dec/2024<br/>
Appache 2.0 license<br/>
</div>

$$
\newcommand{\of}[1]{\left(#1\right)}
\newcommand{\Of}[1]{\left[#1\right]}
\newcommand{\KL}[2]{\operatorname{KL}\left(\left.{#1}\right\|{#2}\right)}
\newcommand{\given}[1]{\left|{#1}\right.}
\newcommand{\mb}[1]{\mathbf{#1}}
$$


<img src="/2024assets/1995WolpertGhahramaniJordan_fig2m.svg">
<img src="/2024assets/1995WolpertGhahramaniJordan_fig2a.svg">

<img src="/2023assets/2018Higgins_SCAN_fig1.svg" style="width:66%;">
<img src="/2023assets/2017Higgins_SCAN_fig1ja_.svg" style="widht:66%;">

<img src="/assets/2014Friston_Fig1.svg" style="width:44%">
<img src="/assets/2009Friston_box3.svg" style="width:44%">

<img src="/2024assets/1993Kawato_Fig1.svg" style="width:44%">
<img src="/2024assets/1993Kawato_fig2.svg" style="width:44%">
<!-- <img src="/2024assets/1993Kawato_fig3_.svg" style="width:44%"><br/> -->
<img src="/2024assets/1993Kawato_fig3all.jpg" style="width:66%"><br/>

測定信号 $x(t)$ から推定しなければならない未知信号を $s(t+a)$ とする。
a は調整可能なパラメータである。
* a>0 は予測，
* a=0 はフィルタ，
* a<0 はスムージングと呼ばれる

## KL ダイバージェンス

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


## Colab 実習ファイル

* [2024_1205Karapetian_RNN.ipynb <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_1205Karapetian_RNN.ipynb){:target="blank"}

## 参考資料

* [7–1 リカレントニューラルネットワーク](/2022/6657.pdf){:target="_blank"}
* [7–1 リカレントネットワークによる文法学習](/2022/6685.pdf){:target="_blank"}

* [Bahdanau and Loung attentions <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_1022Two_attentions_additive_and_multiplicative_Seq2seq.ipynb)

* [系列探索と逆行流: 視覚野における双方向情報フローの計算モデル](/2023cogpsy/2021Ullman_bu_td_ja.pdf){:target="_blank"}
* [ボトムアップ・トップダウンの反復処理による画像解釈](/2023cogpsy/1995Ullman_bidirectional_cortex_ja.pdf){:target="_blank"}

# 言語モデル，あるいは時系列予測モデル

## LSTM におけるゲートの生理学的対応物 <!--Physiological correlates of gates in LSTM-->

以下の画像は <http://kybele.psych.cornell.edu/~edelman/Psych-2140/week-2-2.html> よりの引用。
ウミウシのエラ引っ込め反応時に，ニューロンへの入力信号ではなく，入力信号を修飾する結合が存在する。下図参照。

<center>
<img src="/assets/2016McComas_presynaptic_inhibition.jpg" style="width:24%">
<img src="/assets/C87-fig2_24.jpg" width="17%">
<img src="/assets/C87-fig2_25.jpg" width="33%"><br>
アメフラシ (Aplysia) のエラ引っ込め反応(a.k.a. 防御反応)の模式図[^seaslang]
<!-- <img src="/assets/shunting-inhibition.jpg" width="29%"> -->
</center>

* [注意機構の補足説明 大門他 (2023) <img src="https://www.adobe.com/content/dam/cc/en/legal/images/badges/PDF_32.png">](/2023/2023cnps注意機構の補足説明.pdf){:target="_blank"}


## [Top-Down Network Combines Back-Propagation with Attention](https://arxiv.org/abs/2306.02415)

* [GitHub](https://github.com/royabel/Top-Down-Networks)

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


#### Multi-task Learning (MTL)

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
