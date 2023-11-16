---
title: "第08回 2023年度開講 駒澤大学 認知心理学研究"
author: "浅川 伸一"
layout: home
---

# 認知心理学研究 IIB
<div style="align:right">
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 10/Nov/2023<br/>
Appache 2.0 license<br/>
</div>

<link href="/css/asamarkdown.css" rel="stylesheet">

<div class="figcenter">
<img src="/2023assets/1990Cohen_McClelland_stroop_fig3.svg">
<img src="/2023assets/2023_1110task_demand_conflict_ja.svg" width="49%">
<div class="figcaption">

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
</div></div>

## 実習

* [1990 年代の Stroop 効果のシミュレーション<img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_1110Stroop_1990Cohen_model.ipynb){:target="_blank"}


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


## 実習

* [実習 オーバーフィッティング，アンダーフィッテング <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2020Sight_Visit_polynomilal_fittings_demo.ipynb){:target="_blank"}

## 機械学習と推測統計学

# 機械学習の技法

3. Breiman の 2 つの文化
2. データセット
7. 交差検証法
6. 誤差逆伝播法
4. 勾配降下法，確率的勾配降下法
5. ミニバッチ
1. データ拡張
1. ドロップアウト
2. 正則化
3. フィードフォワード結合，フィードバック結合，リカレント結合

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


# PyTorch

* [Pytorch によるニューラルネットワークの構築 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_1115PyTorch_buildmodel_tutorial_ja.ipynb)
* [Dataset とカスタマイズと，モデルのチェックポイント，微調整 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2023notebooks/2023_0824pytorch_simple_fine_tune_tutorial.ipynb)
* [PyTorch Dataset, DataLoader, Sampler, Transforms の使い方 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2023notebooks/2023_0824pytorch_dataset_data_loader_sampler.ipynb)

# tSNE
* [kmnist による PCA と tSNE の比較 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/2019komazawa/blob/master/notebooks/2019komazaawa_kmnist_pca_tsne.ipynb)
* [効率よく t-SNE を使う方法](https://project-ccap.github.io/misread-tsne/)

# Google colabratory でのファイルの [アップ|ダウン]ロード

<div style="width:	77%;align:center;text-align:left;margin-left:10%;margin-right:10%">

```python
from google.colab import files
uploaded = files.upload()
```

```python
from google.colab import files
files.download('ファイル名')
```
</div>


# エントロピー Entropy
<!-- Srihari slides https://cedar.buffalo.edu/~srihari/CSE574/ -->

* 離散的確率変数 $x$ の特定の値を観測したとき，どの程度の情報を受け取ることができるかを示す量。
* `驚き surprise` の程度を表す情報の量<!--Amount of information is degree of surprise-->
    * 確実性 certainity は，情報がないことを言う。
    * ある事象が起こる可能性が低い場合には，その情報が起こった時に，より多くの情報が得られると考える。
* 確率分布 $p(x)$ とそのときの量 $h(x)$ に依存する。
* 無関係な 2 つの事象 $x$ と $y$ があるとき，$h(x,y) = h(x)+h(y)$ としたい。
* したがって $h(x)=-\log_{2}p(x)$ を選ぶ。
    * 負は情報量が正であることを保証するために付与されている
* 平均的な情報伝達量は $p(x)$ に対する期待値であり，これがエントロピーと呼ばれる量である。


- 情報量: 確率変数 $x$ のサプライズ量
  - まれにしか起こらない事象が起こった場合には情報量は大きい。<strong>ニュースになる</strong>
  - 必ず起こることが起こっても情報量は小さい。<strong>ニュースにならない</strong>

$$
H(x)=-\sum_x p(x)\log_2p(x)
$$
- マイナスをつけるのは正の値にするため
サプライズ量の平均: 平均エントロピー


一方情報論的エントロピー $H$ の定義は事象 $A$ の起こる確率を $P(A)$ とすれば

$$
H(A) = - \sum_{A\in\Omega} P(A) \log P(A)
$$

確率の制約，及び，平均と分散に関する制約条件を以下のように記述:

- $\displaystyle\int p\left(x\right)\;dx =1$ : 確率
- $\displaystyle\int xp\left(x\right)\;dx =\mu$ : 平均
- $\displaystyle\int \left(x-\mu\right)^2p\left(x\right)\;dx=\sigma^2$ : 分散
- ラグランジェ乗数を使って制約条件下での最大化

$$
L(x,\lambda_1,\lambda_2,\lambda_3)=-\int p\left(x\right)\log p\left(x\right)\;dx + \lambda_1\left(\int p\left(x\right)\;dx-1\right) + \lambda_2\left(\int xp\left(x\right)\;dx-\mu\right)+\lambda_3\left(\int\left(x-\mu\right)^2p\left(x\right)\;dx-\sigma^2\right)
$$

各変数で微分して 0 と置き，整理:

$$
p\left(x\right)=\exp\left(-1+\lambda_1+\lambda_2x+\lambda_3\left(x-\mu\right)^2\right)
$$

- 以上より連続量の最大エントロピーを与える確率分布はガウス分布となる


* (自由エネルギーの最小化) = (予測誤差を最小化するように信念を書き換え予測を最適化)+(予測誤差)を最小化するような行動をとる)
* (自由エネルギー) = (内部エネルギー)-(エントロピー)

## 条件付きエントロピー Conditional Entropy
- 同時確率 $p(x,y)$ に対して
$$
H[x,y]=-\int\int p(x,y)\log p(x,y)\;dx\;dy
$$
<!--  - We draw pairs of values of $x$ and $y$-->
- $x$ が所与のとき<strong>条件付きエントロピー</strong>
$$
H[y\vert x]=-\int p(y\vert x)\log p(y\vert x)\;dy
$$

- さらに以下の関係がある
$$
H[x,y] = H[y\vert x] + H[x]
$$

<!--
  - If value of $x$ is already known, additional information to specify corresponding value of $y$ is $-\log p\of{y\given{x}}$
- Average additional information needed to specify $y$ is the conditional entropy
- By product rule $H\of{x,y} = H\of{y\given{x}} + H\of{x}$
-->
<!--
  - where $H\of{x,y}$ is differential entropy of $p\of{x,y}$
  - $H\of{x}$ is differential entropy of $p(x)$
  - Information needed to describe $x$ and $y$ is given by
  - information needed to describe $x$ plus additional information needed to specify $y$ given $x$
-->


<!--
- If we have joint distribution $p\of{x,y}$
  - We draw pairs of values of $x$ and $y$
  - If value of $x$ is already known, additional information to specify corresponding value of $y$ is $-\log p\of{y\given{x}}$
- Average additional information needed to specify $y$ is the conditional entropy
- By product rule $H\of{x,y} = H\of{y\given{x}} + H\of{x}$
  - where $H\of{x,y}$ is differential entropy of $p\of{x,y}$
  - $H\of{x}$ is differential entropy of $p\of{x}$
  - Information needed to describe $x$ and $y$ is given by
  - information needed to describe $x$ plus additional information needed to specify $y$ given $x$
-->

<!-- フリストンの言う自由エネルギーとは，ヘルムホルツの自由エネルギーを脳神経系に当てはめた仮説。

<p align="center">
力学的エネルギー = 運動エネルギー + 位置エネルギー(ポテンシャル)
</p>

$$
E = K + U\\
E = \frac{1}{2}mv^2 + mgh
$$ -->


- 統計物理学: 巨視的な物体，すなわち莫大な数の個別的な粒子，原子や分子，からなる物体のふるまいやっ性質を支配している特別な型の法則性を研究する学問分野
- [熱力学第一法則 エネルギー保存則](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%8D%E3%83%AB%E3%82%AE%E3%83%BC%E4%BF%9D%E5%AD%98%E3%81%AE%E6%B3%95%E5%89%87)
- [熱力学第二法則 エントロピーは増大する](https://ja.wikipedia.org/wiki/%E7%86%B1%E5%8A%9B%E5%AD%A6%E7%AC%AC%E4%BA%8C%E6%B3%95%E5%89%87)

## 熱力学的，および情報論的エントロピー (あるいは，情報量 Information Measure)
熱力学的エントロピーと情報論的エントロピーが存在するが式は同じである。

## (熱)力学的エントロピー

ある位置 $i$ にある粒子があるとする。各位置にそれぞれ $n_i$ の粒子が存在するとする。
はおのおの区別できないものとすれば，全ての状態は何通りあるかを表す式は次式となる:

$$
W=\frac{N!}{\prod_i n_i!}
$$

エントロピーとはこの状態の数 $W$ の負の対数である.
$$
H=\frac{1}{N}\log W=\frac{1}{N}\log N!-\frac{1}{N}\sum_i\log n_i!
$$

以下のスターリングの近似公式 ($\log N!\approx N\log N - N$) を用いると以下の式を得る

$$
H=-\lim_{N\rightarrow\infty}\sum_i\left(\frac{n_i!}{N}\right)
\log\left(\frac{n_i!}{N}\right)=-\sum_i p_i\log p_i
$$

$$
S = k \ln W
$$

ここで，$k$ は[ボルツマン定数](https://ja.wikipedia.org/wiki/%E3%83%9C%E3%83%AB%E3%83%84%E3%83%9E%E3%83%B3%E5%AE%9A%E6%95%B0)であり，$W$ は系の微視的な状態を表す。
一方で統計力学におけるエントロピーの定義は以下の通り:

$$
S=k\left<\ln\frac{1}{p(\omega)}\right>=-k\sum_{\omega}p(\omega)\ln p(\omega)
$$

上式中 $\left<\;\right>$ は[アンサンブル平均](https://ja.wikipedia.org/wiki/%E7%B5%B1%E8%A8%88%E9%9B%86%E5%9B%A3)と呼ばれ，巨視的に同条件下にある力学系が系を構成する分子間に相関がなければ，系は微視的にはすべての状態をとりうることから，巨視的状態において統計的に系はすべての状態をとりうることが仮定される。
系の時間的平均と空間間的平均が同じであると仮定できるときその系は**エルゴード性**を有するという。
エルゴード性により時間平均と空間平均とを区別しないで(しばしば意図的に混乱させて)用いることが行われる。

<!--## 情報量 Information Measure
Srihari slides https://cedar.buffalo.edu/~srihari/CSE574/

- 離散変数 $x How much information is received when we observe a specific value for a discrete random ariable $x$?
- Amount of information is degree of surprise
    - Certain means no information
    - More information when event is unlikely
- Depends on probability distribution $p\of{x}$, a quantity $h\of{x}$
- If there are two unrelated events $x$ and $y$ we want $h\of{x,y}=h\of{x}+h\of{y}$
- Thus we choose $h\of{x}=-\log_2p\of{x}$
    - Negative assures that information measure is positive
- Average amount of information transmitted is the expectation w.r.t $p\of{x}$ refered to as entropy

- 情報量: 確率変数 $x$ のサプライズ量
  - まれにしか起こらない事象が起こった場合には情報量は大きい。<strong>ニュースになる</strong>
  - 必ず起こることが起こっても情報量は小さい。<strong>ニュースにならない</strong>

$$
H\of{x}=-\sum_x p\of{x}\log_2p\of{x}
$$
- マイナスをつけるのは正の値にするため
サプライズ量の平均: 平均エントロピ


一方情報論的エントロピー $H$ の定義は事象 $A$ の起こる確率を $P(A)$ とすれば

$$
H(A) = - \sum_{A\in\Omega} P(A) \log P(A)
$$


確率の制約，及び，平均と分散に関する制約条件を以下のように記述:

- $\displaystyle\int p\left(x\right)\;dx =1$ : 確率
- $\displaystyle\int xp\left(x\right)\;dx =\mu$ : 平均
- $\displaystyle\int \left(x-\mu\right)^2p\left(x\right)\;dx=\sigma^2$ : 分散
- ラグランジェ乗数を使って制約条件下での最大化

$$
L(x,\lambda_1,\lambda_2,\lambda_3)=-\int p\left(x\right)\log p\left(x\right)\;dx + \lambda_1\left(\int p\left(x\right)\;dx-1\right) + \lambda_2\left(\int
 xp\left(x\right)\;dx-\mu\right)+\lambda_3\left(\int\left(x-\mu\right)^2p\left(x\right)\;dx-\sigma^2\right)
$$

各変数で微分して0と置き，整理:

$$
p\left(x\right)=\exp\left(-1+\lambda_1+\lambda_2x+\lambda_3\left(x-\mu\right)^2\right)
$$
- 以上より連続量の最大エントロピーを与える確率分布はガウス分布となる-->

<!-- - [自由エネルギー原理](./friston_FEP)<br> -->

ヘルムホルツの自由エネルギー: $F = U - TS $

$F$ はヘルムホルツの自由エネルギー，$T$ は温度，$S$ はエントロピー。<!-- <https://kotobank.jp/word/%E8%87%AA%E7%94%B1%E3%82%A8%E3%83%8D%E3%83%AB%E3%82%AE%E3%83%BC-76745>-->

- 熱力学の第一法則 エネルギー保存則
- 熱力学の第二法則

ギブスの自由エネルギー: $ G = F + pV$

* [変分自己符号化モデル 説明文](/vae_from2020gtext.pdf)
* [https://cbmm.mit.edu/video/brain-object-recognition-high-performing-shallow-recurrent-anns](https://cbmm.mit.edu/video/brain-object-recognition-high-performing-shallow-recurrent-anns)


---


<!-- from `~/study/2020blog.evjang.com/2016/08/2016EricJang_vb_basic_ja.md`-->
変分ベイズ法 (VB: Variational Bayeisan Methods) は，統計的機械学習で非常によく使われる手法の一群である。
VB 法は，統計的推論問題 (別の確率変数の値から確率変数の値を推定する問題) を最適化問題(ある目的関数を最小化するパラメータ値を求める問題) として書き直すことができる。
<!-- Variational Bayeisan (VB) Methods are a family of techniques that are very popular in statistical Machine Learning.
VB methods allow us to re-write *statistical inference* problems (i.e. infer the value of a random variable given the value of another random variable) as *optimization *problems (i.e. find the parameter values that minimize some objective function). -->

この推論と最適化の二重性は，最新の最適化アルゴリズムを使って統計的機械学習の問題を解く (逆に，統計的手法を使って関数を最小化する) ことを可能にするため強力である。
<!-- This inference-optimization duality is powerful because it allows us to use the latest-and-greatest optimization algorithms to solve statistical Machine Learning problems (and vice versa, minimize functions using statistical techniques). -->

ここでは，変分法について，最適化の目的を導出する。
目的は **変分下限 Variational Lower Bound** としても知られ [Variational Autoencoders](https://arxiv.org/abs/1312.6114) で使われているものと全く同じものである。

系を確率変数の集まりとしてモデル化すると，ある観察変数 ($X$) と，観察不可能な潜在変数 ($Z$) を仮定する。

[ベイズの定理](https://en.wikipedia.org/wiki/Bayes%27_theorem) は，任意の確率変数の組の間の一般的な関係を与える。
<!-- [Bayes' Theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem) gives us a general relationship between any pair of random variables: -->

$$
p(Z|X) = \frac{p(X|Z)p(Z)}{p(X)}
$$

これの様々な断片に通称が関連付けられている。
<!-- The various pieces of this are associated with common names:-->

$p(Z|X)$ は **事後確率** である。
`ある画像が与えられたとき，それが猫の画像である確率は？`
もし $z\sim P(Z|X)$ から標本抽出できるなら，これを使って，与えられた画像が猫かどうか教えてくれる猫分類器を作ることができる。
<!-- $p(Z|X)$ is the **posterior probability**: "given the image, what is the probability that this is of a cat?"
If we can sample from $z\sim P(Z|X)$, we can use this to make a cat classifier that tells us whether a given image is a cat or not. -->

$p(X\vert Z)$ は **尤度** である。
$Z$ の値が与えられたとき，この画像 $X$ がそのカテゴリに属する「確率」がどのくらいかを計算する。
もし $x\sim P(X\vert Z)$ から標本抽出できるなら，乱数を生成するのと同じくらい簡単に猫の画像と猫以外の画像を生成することができる。
$p(Z)$ は**事前確率** と呼ばれる。

隠れ変数は [ベイズ統計学](https://en.wikipedia.org/wiki/Bayesian_statistics) の枠組みで，観測変数に付随する **事前確信** と解釈することができる。
例えば，$X$ が多変量ガウス分布であると信じる場合，隠れ変数 $Z$ はガウス分布の平均と分散を表すかもしれない。
このとき，パラメータに対する分布 $P(Z)$ は，$P(X)$ に対する **事前分布** となる。
<!-- Hidden variables can be interpreted from a [Bayesian Statistics](https://en.wikipedia.org/wiki/Bayesian_statistics) framework as *prior beliefs* attached to the observed variables.
For example, if we believe $X$ is a multivariate Gaussian, the hidden variable $Z$ might represent the mean and variance of the Gaussian distribution.
The distribution over parameters $P(Z)$ is then a *prior* distribution to $P(X)$. -->

また，$X$ と $Z$ とがどの値を表すかは，自由に選択することができる。
例えば，$Z$ の代わりに「平均，分散の立方根，あるいは  $X+Y$，ここで $Y \sim \mathcal{N}(0,1)$」などとすることも可能である。
これはやや不自然で変であるが，$P(X|Z)$ を適宜修正すれば，構造はそのまま有効である。
<!-- You are also free to choose which values $X$ and $Z$ represent.
For example, $Z$ could instead be "mean, cube root of variance, and $X+Y$ where $Y \sim \mathcal{N}(0,1)$".
This is somewhat unnatural and weird, but the structure is still valid, as long as $P(X|Z)$ is modified accordingly.-->

変数を「追加」することもできる。
$P(Z|\theta)$ は，それ自身の事前分布 $P(\theta)$ を持ち，それらもやはり事前分布を持つなど，事前分布自体が他の確率変数に依存するかもしれない。
どんなハイパーパラメータも事前分布と考えることができる。



## 物理学におけるエントロピー <!--Physics view of Entropy-->
- $N$ 個の物質が $i$ 個の状態，各状態には $n_i$ 個の物質
<!--- $N$ objects into bins so that $n_i$ are in $i^{th}$ bin where $\sum_in_i=N$-->
<!--- Number of different ways of allocating objects to bins-->
- $N$ 個の物質を全て並べる: $N\cdot(N-1)\cdots2\cdot1=N!$<!-- であればways to choose first, $N-1$ ways for second leads to $N\cdot(N-1)\cdots2\cdot1=N!$-->
- 各状態の中では物質の順序は問わないことにする<!--We don’t distinguish between rearrangements within each bin-->
<!--    - In $i^{th}$ bin there are $n_i!$ ways of reordering objects-->
- 総数 $N$ 個の物質を $n_i$ に分ける場合の組み合わせ: $W=\frac{N!}{\prod_{i}n_{i}!}$
<!--  - Total number of ways of allocating $N$ objects to bins is $W=\frac{N!}{\prod_{i}n_{i}!}$-->
<!--    - Called Multiplicity (also weight of macrostate)-->
<!-- Entropy: scaled log of multiplicity -->
- <strong>エントロピーの定義</strong>

$$
H=\frac{1}{N}\ln W=\frac{1}{N}\ln N!-\frac{1}{N}\sum_i\ln n_i!
$$

- スターリングの公式 $N! \approx N\log N-N$ を用いて
$$
H=-\lim_{N\rightarrow\infty}\sum_i\left(\frac{n_i}{N}\right)\ln\left(\frac{n_!}{N}\right)=-\sum_ip_i\ln p_i
$$
- 全体の分布 $\displaystyle\frac{n_i}{N}$ をマクロステート
- 各状態をミクロステート $n_i$ を

### 連続系のエントロピー <!--Entropy with Continuous Variable-->
<!-- - Divide $x$ into bins of width $\Delta$-->
<!-- - For each bin there must exist a value $x_i$ such that -->
<!-- - Gives a discrete distribution with probabilities $p(x_i)\Delta$ -->
- 離散量 $p(x_i)\Delta$ を考えて $\Delta\rightarrow0$ を考える:
  - $\displaystyle\int_{i\Delta}^{\left(i+1\right)\Delta}p(x)d(x)=p(x_i)\Delta$
- <strong>連続系のエントロピー</strong><!--Entropy -->
$$
H_{\Delta}=-\sum_ip(x_i)\Delta\log\left(p(x_i)\Delta\right)=-\sum_ip(x_i)\Delta\log(x_i)-\Delta\log\Delta
$$

<!-- - Omit the second term and consider the limit $\Delta\rightarrow0$-->
- $\Delta\rightarrow0$ の極限を考えれば:<!--第2項を無視すれば:-->
$$
H_\Delta=-\int p(x) \log p(x)\,dx
$$
<!-- - Known as Differential Entropy-->
- 連続系と離散系のエントロピーは $\Delta\log\Delta$ だけ異なる
<!-- - Discrete and Continuous forms of entropy differ by quantity $\log\Delta$ which diverges-->
<!-- - Reflects to specify continuous variable very precisely requires a large no of bits-->

### 連続系のエントロピーを最大化する分布
<!--
# Entropy with Multiple Continuous Variables
- Differential Entropy for multiple continuous variables
$$
H[x]=-\int p(x)\log p(x)\;dx
$$
- For what distribution is differential entropy maximized?
  - For discrete distribution, it is uniform
  - For continuous, it is Gaussian
-->
- どのような分布が連続系のエントロピーを最大化するか？
  - 離散系では一様分布
  - 連続系では?
$$
H[x]=-\int p(x)\log p(x)\;dx
$$


### 汎関数としてのエントロピー <!--Entropy as a Functional-->
- 通常の関数: 微分 := スカラを入力として，スカラを返す関数(演算子)
- 汎関数: 関数を入力としてスカラを返す関数(演算子)
- 機械学習における汎関数の例: スカラ値を返すエントロピー $H[p(x)]$ を最大化
  - <strong>変分原理</strong>あるいは<strong>変分推論</strong>

<!-- - Ordinary calculus deals with functions
- A functional is an operator that takes a function as input and returns a scalar
- A widely used functional in machine learning is entropy $H\BRc{p(x)}$ which is a scalar quantity
- We are interested in the maxima and minima of functionals analogous to those for functions
  - Called calculus of variations-->

## 汎関数の最大化 <!--Maximizing a Functional-->

- 汎関数: 関数からスカラへの写像
  - 最大値を与える関数を探す
  - 制約付の最大化(最小化)
  - <strong>ラグランジアン</strong>の利用

<!-- - 汎関数: mapping from set of functions to real value
- For what function is it maximized?
- Finding shortest curve length between two points on a sphere (geodesic)
  - With no constraints it is a straight line
  - When constrained to lie on a surface solution is less obvious– may be several
- Constraints incorporated using Lagrangian-->

### エントロピーの最大化<!--Maximizing Differential Entropy-->

- 確率の制約，及び，平均と分散に関する制約条件を以下のように記述:<!--Assuming constraints on first and second moments of $p(x)$ as well as normalization-->
  - $\displaystyle\int p(x)\;dx =1$ : 確率
  - $\displaystyle\int xp(x)\;dx =\mu$ : 平均
  - $\displaystyle\int (x-\mu)^2 p(x)\;dx=\sigma^2$ : 分散
- ラグランジェ乗数を使って制約条件下での最大化<<!--Constrained maximization is performed using Lagrangian multipliers. Maximize following functional w.r.t $p(x)$:-->
<!--- Constrained maximization is performed using Lagrangian multipliers. Maximize following functional w.r.t $p(x)$:-->

$$
-\int p(x)\log p(x)\,dx + \lambda_1\left(\int p(x)\;dx-1\right) + \lambda_2\left(\int xp(x)\;dx-\mu\right) +\lambda_3\left(\int(x-\mu)^2p(x)\;dx-\sigma^2\right)
$$
<!--- Using the calculus of variations derivative of functional is set to zero giving-->
各変数で微分して0と置き，整理:
$$
p(x)=\exp\left(-1+\lambda_1+\lambda_2x+\lambda_3(x-\mu)^2\right)
$$
  - 以上より連続量の最大エントロピーを与える確率分布はガウス分布となる
<!--  - Backsubstituting into three constraint equations leads to the result that distribution that maxi
mizes differential entropy is Gaussian-->

### 正規分布のエントロピーの微分 <!--Differential Entropy of Gaussian-->
<!--- Distribution that maximizes Differential Entropy is Gaussian-->
$$
p(x)=\frac{1}{\left(2\pi\sigma^2\right)^{1/2}} e^{-\left(\frac{x-\mu}{\sigma}\right)^2}
$$
- このとき最大エントロピーは以下:
<!-- - Value of maximum entropy is-->
$$
H[x]=\frac{1}{2}\left(1+\log\left(2\pi\sigma^2\right)\right)
$$

- 分散が大きくなればエントロピーは増大する
- 離散系のエントロピーとは異なり，連続系のエントロピーは $\sigma^2<\frac{1}{2}\pi e$ のとき，<strong>負</strong>となる

<!--
- Entropy increases as variance increases
- Differential entropy, unlike discrete entropy, can be negative for $\sigma^2<\frac{1}{2}\pi e$
-->

## カルバック・ライブラー・ダイバージェンス，(KL ダイバージェンス)

カルバック・ライブラーダイバージェンスは 2 つの確率密度 $p$, $q$ の乖離を表す指標である。
教科書によっては，カルバック・ライブラーの偽距離と記載されている場合もある。
また，表記として $KL\left(p\|\| q\right)$ あるいは $D_{KL}\left(p\|\| q\right)$ と表記する文献も存在する。

カルバック・ライブラーダイバージェンスは，非対称であることに注意が必要である。
すなわち $KL[p\|q] \ne KL[q\|p]$ である。
カルバック・ライブラーのダイバージェンスの非対称性は，定義を見れば納得できる。

$$ KL\left(p\|q\right)= - \int p \log\left(\frac{p}{q}\right)\;dp = -\left[\int p\log p\;dp + \int p\log q\;dp\right] $$

上式最右辺，第一項は，エントロピーの定義式であり，分布 $p$ の負の対数の平均である。
一方，上式最右辺第二項は，分布 $q$ を，$q$ の確率密度を使って平均を求めている。
このため，$\log q$ に大きな値を取る領域や部分があっても，$p$ が 0 に近ければ，両分布の乖離度合いとして計算されないことを意味している。
KL ダイバージェンスの非対称性を説明する下図に示す。

青い曲線は真の事後分布とする。
仮に双峰性の分布であると考える。
緑の分布は最適化を介して青い密度に適合させる変分近似による分布を表すものとする。
これは フォワード KL と呼ばれている。
図左のように，双峰性の真の分布を単峰性の分布で近似することを考える。
このとき，一方の峰に当てはまるように調整すると，もう一方の峰の値についての当てはまりが悪くなり結果として右下図のような裾野の広い分布を得ることになる。

反対に，緑の単峰性の分布を青の双峰性の分布で近似しようとする リバースKL を考える。
このとき基準となる真の分布である単峰性の分布の確率密度がほとんど 0 の領域では，推定する分布がどのような値を取ろうとも KL ダイバージェンス の値に影響を与えないため，いずれか一方の峰が真の分布と重なるような値を得ることになる。

<center>
<img src="/assets/forward-KL.png" width="44%">
<img src="/assets/reverse-KL.png" width="44%">
<div class="figcaption">

KL ダイバージェンスの非対称性。
フォーワード KL （左）とリバース KL (右)。
<!-- \url{https://blog.evjang.com/2016/08/variational-bayes.html} [A Beginner's Guide to Variational Methods: Mean-Field Approximation]より -->
</div></center>

大抵の場合，現実は複雑(怪奇) で（図中の青色で描かれた分布），モデル (図中の緑で描かれた分布) は素朴で単純であると考えられる。
図左は，現実が双峰性分布でモデルが単峰性分布のときに，現実(青色)からみたモデル(緑色)の乖離であるから，
現実（青）の存在する領域に，モデルが存在しない状況 （左上図）では KL ダイバージェンスは大きく，したがって，両分布の乖離は大きくなる。
したがって，現実を最もよく推定することを試みた場合 (左下図) モデル（の推定）は，裾野の広い分布と推定することとなる。

一方，単峰性分布モデル(緑)から，双峰性分布である現実（青）を見た場合，モデルと現実があっていない状況(右上図)になる。
この状態で，モデルから，無理やり現実を推定しようとする リバース KL (右下図) では，現実を最もよく推定すると，
双峰性分布の，どちらかのピークと重なる形で，モデル（緑色）は，現実 （青色）を推定してしまうこととなる。


## ELBO あるいは 変分下界 <!-- # Variational Lower Bound for Mean-field Approximation-->

変分推論の考え方は，事後推論の方法がわかっている簡単なパラメトリック分布 $Q_{\phi}\left(Z \vert X\right)$ (ガウス分布など) に対して推論を行い，パラメータ $\phi$ を調整して$P$ になるべく近づけようというものである。

<!-- The idea behind variational inference is this: let's just perform inference on an easy, parametric distribution $Q_\phi(Z | X)$ (like a Gaussian) for which we know how to do posterior inference, but adjust the parameters $\phi$ so that $Q_\phi$ is as close to $P$ as possible. -->

<!-- 青い曲線が本当の事後分布で，緑の分布が最適化によって青い密度に合わせた変分近似 (ガウシアン) である。 -->
<!-- This is visually illustrated below: the blue curve is the true posterior distribution, and the green distribution is the variational approximation (Gaussian) that we fit to the blue density via optimization. -->

<div class="figcenter">
<img src="/2023assets/Untitled+presentation+(2).png" width="44%">
</div>

分布が「近い」とはどういうことか？
平均場変分ベイズ (最も一般的な型) では，2 つの分布の間の距離指標として 逆 KL ダイバージェンスを用いる。
<!-- What does it mean for distributions to be "close"? Mean-field variational Bayes (the most common type) uses the Reverse KL Divergence to as the distance metric between two distributions. -->

$$
KL(Q_\phi(Z\vert X)\|P(Z\vert X)) = \sum_{z \in Z}{q_\phi(z \vert x)\log\frac{q_\phi(z \vert x)}{p(z \vert x)}}
$$

逆 KL ダイバージェンスは，$P(Z)$ を $Q_\phi(Z)$ に「歪める」ために必要な情報量 (つまり $\displaystyle\frac{1}{\log(2)}$ ビット) を測定する。
この量を $\phi$ に関して最小化したい。
<!-- Reverse KL divergence measures the amount of information (in nats, or units of $\frac{1}{\log(2)}$ bits) required to "distort" $P(Z)$ into $Q_\phi(Z)$.
We wish to minimize this quantity with respect to $\phi$.-->

条件付き分布の定義から $\displaystyle p(z\vert x) = \frac{p(x,z)}{p(x)}$ となる。
この式を，もとの $KL$ 式に代入して，分配してみよう。
<!-- By definition of a conditional distribution, $p(z|x) = \frac{p(x,z)}{p(x)}$.
Let's substitute this expression into our original $KL$ expression, and then distribute: -->

$$\begin{aligned}
KL(Q||P) & = \sum_{z \in Z}{q_\phi(z|x)\log\frac{q_\phi(z|x)p(x)}{p(z,x)}} \\
& = \sum_{z \in Z}{q_\phi(z|x)\big(\log{\frac{q_\phi(z|x)}{p(z,x)}} + \log{p(x)}\big)} \\
& = \left(\sum_{z}{q_\phi(z|x)\log{\frac{q_\phi(z|x)}{p(z,x)}}}\right) + \left(\sum_{z}{\log{p(x)}q_\phi(z|x)}\right) \\
& = \left(\sum_{z}{q_\phi(z|x)\log{\frac{q_\phi(z|x)}{p(z,x)}}}\right) + \left(\log{p(x)}\sum_{z}{q_\phi(z|x)}\right) \\
& = \log{p(x)} + \left(\sum_{z}{q_\phi(z|x)\log{\frac{q_\phi(z|x)}{p(z,x)}}}\right)
\end{aligned}\tag{1}$$

$KL(Q \| P)$ を変分パラメータ $\phi$ に関して最小化するには，$\log{p(x)}$ は $\phi$ に関して固定なので，$\displaystyle\sum_{z}{q_\phi(z \vert x)} \log{\frac{q_\phi(z \vert x)}{p(z,x)}}$ を最小化すればよい。
この量を分布 $Q_\phi(Z\vert X)$ に対する期待値として書き直そう。
<!-- To minimize $KL(Q||P)$ with respect to variational parameters $\phi$, we just have to minimize $\sum_{z}{q_\phi(z|x)\log{\frac{q_\phi(z|x)}{p(z,x)}}}$, since $\log{p(x)}$ is fixed with respect to $\phi$.
Let's re-write this quantity as an expectation over the distribution $Q_\phi(Z|X)$. -->

$$\begin{aligned}
\sum_{z}{q_\phi(z|x)\log{\frac{q_\phi(z\vert x)}{p(z,x)}}} & = \mathbb{E}_{z \sim Q_\phi(Z\vert X)}\left[\log{\frac{q_\phi(z\vert x)}{p(z,x)}}\right] \\
&= \mathbb{E}_Q\left[ \log{q_\phi(z|x)} - \log{p(x,z)} \right] \\
&= \mathbb{E}_Q\left[ \log{q_\phi(z|x)} - (\log{p(x|z)} + \log(p(z))) \right] && \\
& = \mathbb{E}_Q\left[ \log{q_\phi(z|x)} - \log{p(x|z)} - \log(p(z))) \right] \\
\end{aligned}$$

これを最小化することは，この関数の負の値を **最大化** することと等価である。
<!-- Minimizing this is equivalent to *maximizing* the negation of this function: -->

$$\begin{aligned}
\max\mathcal{L} &= -\sum_{z}{q_\phi(z\vert x)\log{\frac{q_\phi(z\vert x)}{p(z,x)}}} \\
& = \mathbb{E}_Q\left[ -\log{q_\phi(z|x)} + \log{p(x\vert z)} + \log(p(z))) \right] \\
& =  \mathbb{E}_Q\left[ \log{p(x\vert z)} + \log{\frac{p(z)}{ q_\phi(z\vert x)}} \right] \\
\end{aligned}\tag{2}$$

文献では，$\mathcal{L}$ は **変分下限 variational lower bound** と呼ばれ，$p(x|z), p(z), q(z|x)$ を評価できれば，計算上，扱いやすいとされている。
さらに直感的な式が得られるように項を並べ替えることができる。
<!-- In literature, $\mathcal{L}$ is known as the *variational lower bound*, and is computationally tractable if we can evaluate $p(x|z), p(z), q(z|x)$. We can further re-arrange terms in a way that yields an intuitive formula: -->

$$\begin{aligned}
\mathcal{L} &= \mathbb{E}_Q\left[ \log{p(x|z)} + \log{\frac{p(z)}{ q_\phi(z|x)}} \right] \\
            &= \mathbb{E}_Q\left[ \log{p(x|z)} \right] + \sum_{Q}{q(z|x)\log{\frac{p(z)}{ q_\phi(z|x)}}} && \\
&= \mathbb{E}_Q\left[ \log{p(x|z)} \right] - KL(Q(Z|X)||P(Z)) && \\
\end{aligned}\tag{3}$$

標本抽出 $z \sim Q(Z\vert X)$ が観測値 $x$ を潜在符号 $z$ に変換する「符号化」過程だとすると，標本抽出 $x \sim Q(X\vert Z)$ は観測値を $z$ から復元する「復号化」過程であることがわかる。
<!-- If sampling $z \sim Q(Z|X)$ is an "encoding" process that converts an observation $x$ to latent code $z$, then sampling $x \sim Q(X|Z)$ is a "decoding" process that reconstructs the observation from $z$. -->

このことから $\mathcal{L}$ は，期待「復号化」尤度 (変分分布が $Z$の標本を $X$ の標本に復号化できる程度) と，変分近似と $Z$ に関する事前分布の間の KL ダイバージェンスの和であることがわかる。
$Q(Z|X)$ が条件付きガウス分布であるとすると，$Z$ の事前分布は平均 0，標準偏差 1 の対角ガウス分布が選ばれることが多い。
<!-- It follows that $\mathcal{L}$ is the sum of the expected "decoding" likelihood (how good our variational distribution can decode a sample of $Z$ back to a sample of $X$), plus the KL divergence between the variational approximation and the prior on $Z$.
If we assume $Q(Z|X)$ is conditionally Gaussian, then prior $Z$ is often chosen to be a diagonal Gaussian distribution with mean 0 and standard deviation 1. -->

$\mathcal{L}$ が変分下界と呼ばれるのはなぜか？
式(1) に $\mathcal{L}$ を代入し直すと，以下のようになる:
<!-- Why is $\mathcal{L}$ called the variational lower bound?
Substituting $\mathcal{L}$ back into Eq. (1), we have: -->

$$\begin{aligned}
KL(Q||P) & = \log p(x) - \mathcal{L} \\
\log p(x) & = \mathcal{L} + KL(Q||P) \\
\end{aligned}\tag{4}$$

式 (4) の意味を平たく言うと，あるデータ点 $x$ の真の分布の下での対数尤度 $p(x)$ は$\mathcal{L}$ に，その特定の値 $x$ における $Q(Z\vert X=x)$ と $P(Z\vert X=x)$ 間の距離を表す誤差項 $KL(Q \vert\vert P)$ が加わるということである。
<!-- The meaning of Eq. (4), in plain language, is that $p(x)$, the log-likelihood of a data point $x$ under the true distribution, is $\mathcal{L}$, plus an error term $KL(Q||P)$ that captures the distance between $Q(Z|X=x)$ and $P(Z|X=x)$ at that particular value of $X$.-->

$KL(Q||P) \geq 0$ なので，$\log p(x)$ は $\mathcal{L}$ より大きい必要がある。
よって，$\mathcal{L}$ は $\log p(x)$ の **下限 lower bound** である。
また，$\mathcal{L}$ は別形式で証拠下界 (ELBO) とも呼ばれる。
<!-- Since $KL(Q||P) \geq 0$, $\log p(x)$ must be greater than $\mathcal{L}$.
Therefore $\mathcal{L}$ is a *lower bound* for $\log p(x)$.
$\mathcal{L}$ is also referred to as evidence lower bound (ELBO), via the alternate formulation: -->

$$\mathcal{L} = \log p(x) - KL(Q(Z|X)||P(Z|X)) = \mathbb{E}_Q\left[ \log{p(x|z)} \right] - KL(Q(Z|X)||P(Z))$$

なお，$\mathcal{L}$ 自体には，近似事後確率と事前確率の間の KL ダイバージェンス項が含まれているので，$\log p(x)$ には合計 2 つの KL 項が含まれることになる。
<!-- Note that $\mathcal{L}$ itself contains a KL divergence term between the approximate posterior and the prior, so there are two KL terms in total in $\log p(x)$. -->

<!-- # 順方向 KL と逆方向 KL -->
<!-- # Forward KL vs. Reverse KL-->

<!-- KL ダイバージェンスは対称距離関数ではなく，$KL(P||Q) \neq KL(Q||P)$ ($Q \equiv P$ である場合を除く) である。
前者は「順向 KL」、後者は「逆向 KL」と呼ばれる。
では、なぜ 逆向 KLを使うのだろうか？
それは，結果として得られる導出が $p(Z|X)$ の計算方法を知っている必要があるからである。 -->
<!-- KL divergence is *not* a symmetric distance function, i.e. $KL(P||Q) \neq KL(Q||P)$ (except when $Q \equiv P$).
The first is known as the "forward KL", while the latter is "reverse KL".
So why do we use Reverse KL?
This is because the resulting derivation would require us to know how to compute $p(Z|X)$, which is what we'd like to do in the first place. -->

<!-- [PML 教科書](https://www.cs.ubc.ca/~murphyk/MLbook/) にある Kevin Murphy の説明がとても好みなので，ここで再掲してみることにする。 -->
<!-- I really like Kevin Murphy's explanation in the [PML textbook](https://www.cs.ubc.ca/~murphyk/MLbook/), which I shall attempt to re-phrase here: -->

<!-- まず，順方向 KL を考える。
上の導出で見たように KL は重み関数 $p(z)$ に対する「罰則」関数 $\displaystyle\log \frac{p(z)}{q(z)}$ の期待値として書くことができる。 -->
<!-- Let's consider the forward-KL first. As we saw from the above derivations, we can write KL as the expectation of a "penalty" function $\log \frac{p(z)}{q(z)}$ over a weighing function $p(z)$. -->

<!-- $$\begin{aligned}
KL(P||Q) & = \sum_z p(z) \log \frac{p(z)}{q(z)} \\
& = \mathbb{E}_{p(z)}{\left[\log \frac{p(z)}{q(z)}\right]}\\
\end{aligned}$$ -->

<!-- ペナルティ関数は $p(Z) > 0$ のとき，全 KL に損失を寄与する。
$p(Z) > 0$ の場合，$\lim_{q(Z) \to 0}\log\frac{p(z)}{q(z)} \to \infty$ となる。
これは，$Q(Z)$ が $P(Z)$ を「カバー」できないところでは，順向 KL が大きくなることを意味する。 -->
<!-- The penalty function contributes loss to the total KL wherever $p(Z) > 0$.
For $p(Z) > 0$, $\lim_{q(Z) \to 0} \log \frac{p(z)}{q(z)} \to \infty$.
This means that the forward-KL will be large wherever $Q(Z)$ fails to "cover up" $P(Z)$.-->

<!-- よって，$p(z)>0$ のところでは $q(z)>0$ を確保すれば，順向 KL は最小になることがわかる。
最適化された変分分布 $Q(Z)$ は「ゼロ回避 zero-avoiding」($p(Z)$ がゼロのとき，密度がゼロを回避する) として知られている。 -->
<!-- Therefore, the forward-KL is minimized when we ensure that $q(z) > 0$ wherever $p(z)> 0$.
The optimized variational distribution $Q(Z)$ is known as "zero-avoiding" (density avoids zero when $p(Z)$ is zero). -->

<!-- <div class="figure figcenter">
<img src="figures/forward-KL.png" width="44%"> -->
<!-- ![image](../assets/forward-KL.png) -->
<!-- {width="49%"} -->
<!-- </div> -->

<!-- 逆向 KL を最小化すると，全く逆の挙動になる: -->
<!-- Minimizing the Reverse-KL has exactly the opposite behavior: -->

<!-- $$\begin{aligned}
KL(Q||P) & = \sum_z q(z) \log \frac{q(z)}{p(z)} \\
& = \mathbb{E}_{p(z)}{\left[\log \frac{q(z)}{p(z)}\right]}\
\end{aligned}$$

$p(Z)=0$ ならば，分母 $p(Z)=0$ であればどこでも重み付け関数 $q(Z)=0$ を確保しなければ，KL は吹き飛んでしまう。
これは「ゼロ強制 zero-forcing」と呼ばれる。
<!-- If $p(Z)=0$, we must ensure that the weighting function $q(Z)=0$ wherever denominator $p(Z)=0$, otherwise the KL blows up.
This is known as "zero-forcing": -->

<div class="figure figcenter">
<img src="/assets/reverse-KL.png" width="44%">
</div>

<!-- つまり 順向 KL を最小化すると変分分布 $Q(Z)$ が $P(Z)$ 全体を **覆う** ように「伸び」，逆向 KL を最小化すると $P(Z)$ の **下に** $Q(z)$ が「しぼむ」。 -->
<!-- So in summary, minimizing forward-KL "stretches" your variational distribution $Q(Z)$ to cover **over** the entire $P(Z)$ like a tarp, while minimizing reverse-KL "squeezes" the $Q(Z)$ **under** $P(Z)$.-->

<!-- 機械学習の問題で平均場近似を使うとき，逆 KL を使うことの意味を覚えておくことが重要である。
単峰性の分布を多峰性の分布に当てはめると，偽陰性が多くなる ($Q(Z)$ は何もないと思っていたのに，$P(Z)$ は実際に確率的な量がある) ことになる。 -->
<!-- It's important to keep in mind the implications of using reverse-KL when using the mean-field approximation in machine learning problems.
If we are fitting a unimodal distribution to a multi-modal one, we'll end up with more false negatives (there is actually probability mass in $P(Z)$ where we think there is none in $Q(Z)$). -->

<!-- # Connections to Deep Learning-->

<!-- 変分法は Deep Learning にとって本当に重要である。 -->
<!-- 詳しくは後日記事にしますが，ここでは簡単にネタバレします。 -->
<!-- Variational methods are really important for Deep Learning.
I will elaborate more in a later post, but here's a quick spoiler: -->

<!-- 1. ディープラーニングは，たくさんのデータを使った非常に大きなパラメータ空間での最適化(具体的には勾配降下法) が得意だ。
2. 変分ベイズは，統計的推論問題を最適化問題として書き直すことができる枠組みを与えてくれる。 -->

<!-- 1. Deep learning is really good at optimization (specifically, gradient descent) over very large parameter spaces using lots of data.
2. Variational Bayes give us a framework with which we can re-write statistical inference problems as optimization problems. -->

<!-- 深層学習と変分ベイズの組み合わせにより，極めて複雑な事後分布の推論が可能になる。
結果的に，変分自己符号化器のような最新の技術は，この投稿で導かれたのと全く同じ平均場変分下界を最適化する -->
<!-- Combining Deep learning and VB Methods allow us to perform inference on *extremely* complex posterior distributions.
As it turns out, modern techniques like Variational Autoencoders optimize the exact same mean-field variational lower-bound derived in this post! -->


<!-- ## ある日のとある Slack team の会話より
from `2017rnn_book/bayes_learning.md`

「５回に１回の割合で帽子を忘れるくせのあるＫ君が，正月に Ａ，Ｂ，Ｃ ３軒を順に年始回りをして家に帰ったとき，帽子を忘れてきたことに気がついた。２軒目の家 Ｂ に忘れてきた確率を求めよ。」  早稲田大学（１９７６年文学部）で出題された入試問題  [http://www004.upp.so-net.ne.jp/s_honma/probability/bayes.htm](http://www004.upp.so-net.ne.jp/s_honma/probability/bayes.htm) より

新：同時確率を考えると（４/5）×（1/5）×（4/5）=16/125
  忘れた確定ならABCのどっかで忘れたんだから1/3 (自分はこの考えです)
  などいろいろある問題で
  ぶっちゃけ解がわからない

浅：同時確率を計算しただけでは，帽子を忘れたことに気が付いたという事実を考慮していないことになりますよね。帽子を忘れたという事象が生起する確率は 1/5 なのだから分母は全く忘れなかったを１から引いて 1-(4/5)^3 = 61/125. すなわち帽子を忘れたという事象が生起した確率。一方分子はA宅で忘れない(4/5)でかつB宅で忘れた(1/5)事象が起きたのでこれらの積で表される(4/5 * 1/5 = 4/5^2). 以上を計算すれば (4/25)/(61/125) = 20/61. ベイズ的には帽子を忘れたという事象が生起したという事実から考慮すべき確率空間，すなわち分母が変化するので新村さんの考えた同時確率 16/125 を帽子を忘れたという事実を知ったために調整しなければいけない，ということであります。

新：ぬぬ？abcのどこかに忘れたので1/3という解答はおかしいですかね？
  20/61だとしたら
  aに忘れてる確率も，bに忘れてる確率も同様になって
  あ，違うのか。
  順番に回ったから違うのですなぁ
  納得
  となると，よく忘れ物をする人は，最後に見たすぐ後に忘れてる可能性が最も高いのか
  確かにそんな気がします

---

## 解説
帽子を忘れた場所の確率は __負の二項分布__ Negative binomial distribution に従う。負の二項分布の確率密度は以下で与えられる：

$$
NB(X=x;r,p)=\left({x+r-1}\over{x}\right)\;p^{x}\left(1-p\right)^{r}
$$

負の二項分布を，上の例題に対応させて式中の文字の意味を記せば次のようになる。$p(=4/5)$ は帽子を忘れない確率，$1-p(=1/5)$ は反対に帽子を忘れる確率である。$p^x$ は $x$ 回帽子を忘れなかったことを意味し，$(1-p)^r$ は帽子を $r$ 回忘れなかったこととなる。今回は $r=1$ であり帽子を忘れた時点で次の家を訪問してもしなくても関係なくなる。負の二項分布とは $r$ 回失敗する前に成功回数が $x$ 回である確率を表している。[Wikiptediaを参照](https://en.wikipedia.org/wiki/Negative_binomial_distribution)。

1. 最初の訪問宅である A で帽子を忘れれば $p^{0}\;(1-p)^{1}$ で $p=\displaystyle\frac{4}{5}$ を代入すれば $Pr(A)=\displaystyle\frac{1}{5}=\frac{5}{25}=\frac{25}{125}$ となる。
2. B で帽子を忘れた場合は $Pr(B)=p^{1}\;(1-p)^{1}=\displaystyle\frac{4}{5}\;\left(1-\frac{4}{5}\right)=\frac{4}{25}\times\frac{1}{5}=\frac{20}{125}$ を得る。
3. C で帽子を忘れた場合は A, B で帽子を忘れず $x=2$ (成功２回)，C で忘れるのであるから  $p^{2}\;(1-p)^{1}=\displaystyle\left(\frac{4}{5}\right)^2\times\left(\frac{1}{5}\right)=\left(\frac{16}{25}\right)\times\left(\frac{1}{5}\right)=\frac{16}{125}$

比較が容易なように上では分母を $125$ に揃えた。上記のように A で帽子を忘れた確率が最も高くなる。負の二項分布で $r=1$ の場合は，初めて失敗する $r=1$ までに連続して成功した回数が $x$ となる。ベイズ確率を計算するには上の３つの起こった確率を足し合わせた値を分母にする。

$$
\frac{\frac{20}{125}}{\frac{25}{125}+\frac{20}{125}+\frac{16}{125}}=\frac{\frac{20}{125}}{\frac{61}{125}}=\frac{20}{61}
$$

このようにどこかの家で帽子を忘れたのだから等確率で $\displaystyle\frac{1}{3}$ という直観に反して B で忘れた確率は $\displaystyle\frac{1}{3}$ より少しだけ小さい $\displaystyle\frac{20}{61}$ となる。

---

### 繰り返し忘れるとどうなるか （ベイズ更新）

等確率の原理からどの家でも忘れる確率は等しく $\displaystyle\frac{1}{3}$ は事前知識あるいは事前分布を表している。そこで上式を事前知識を加味して書けば，

$$
\frac{\frac{20}{125}\times\frac{1}{3}}{\frac{25}{125}\times\frac{1}{3}+\frac{20}{125}\times\frac{1}{3}+\frac{16}{125}\times\frac{1}{3}}=\frac{\frac{20}{125}\times\frac{1}{3}}{\frac{61}{125}\times\frac{1}{3}}=\frac{20\times\frac{1}{3}}{61\times\frac{1}{3}}=\frac{20}{61}
$$

すなわち事前分布が等しく $\displaystyle\frac{1}{3}$ であったので省略してあったのである。ところが，一度帽子を忘れたという事実を観測した場合，上に従ってそれぞれの家で忘れる確率が $\displaystyle\frac{1}{3}$ ではなくなる。すなわち，

- $Pr(A)=\displaystyle\frac{25}{61}\doteq0.410$,
- $Pr(B)=\displaystyle\frac{20}{61}\doteq0.328$,
- $Pr(C)=\displaystyle\frac{16}{61}\doteq0.262$,

であるから，事前分布としてこの値を代入すれば，B に忘れた確率は $Pr(B)$ は

$$
\frac{\frac{20}{125}\times\frac{20}{61}}{\frac{25}{125}\times\frac{25}{61}+\frac{20}{125}\times\frac{20}{61}+\frac{16}{125}\times\frac{16}{61}}
=\frac{\frac{20^2}{125\times61}}{\frac{25^2+20^2+16^2}{125\times61}}
=\frac{20^2}{25^2+20^2+16^2}=\frac{400}{625+400+256}=\frac{400}{1281}\doteq0.312
$$

として求まる。同様の計算によって次式を得る：

$$
Pr(A)=\frac{25^2}{25^2+20^2+16^2}=\frac{625}{1281}\doteq0.487
$$

$$
Pr(C)=\frac{16^2}{25^2+20^2+16^2}=\frac{256}{1281}\doteq0.201
$$

A, B, C それぞれに帽子を忘れる確率は観測のたびに変化する。数式で表現すれば以下のようになる。
$$
P(\theta_{i}|D)=\frac{P(D|\theta_{i})P(\theta_{i})}{\sum_{j}P(D|\theta_{j})P(\theta_{j})}
$$
上式はベイズ更新と呼ばれる。ニューラルネットワークなどで $\theta$ を重み係数と考え $D$ を訓練データとみなせば上式は __ベイズ学習則の定義__ であり，重み係数の更新式である。ベイズ更新とは現在の重み係数と得られたデータから重み係数を更新する方法であると解釈可能である。 -->


# 文献

* ストループ効果 J. Ridley Stroop (1935) __Studies of Interference in Serial Verbal Reactions__, Journal of Experimental Psychology, 18, 643-662.
* サイモン効果 J. Richard Simon (1969) __Reactions Toward the Source of Stimulation__, Journal of Experimental Psychology, 81(1), 174-176.
* 絵画‐単語干渉効果 W. Glaser & F-J. Dungelhoff, (1984) __The Time Course of Picture-Word Interference__, Journal of Experimental Psychology: Human Perception and Performance, 10(5), 640-654.
* 絵画‐単語課題の意味促進 M-T. Bajo (1988) __Semantic Facilitation With Pictures and Words__, Journal of Experimental Psychology: Learning, Memory, and Cognition, 14(4), 579-589.
* 絵画命名課題における累積意味抑制 D. Howard+ (2006) __Cumulative semantic inhibition in picture naming: experimental and computational studies__, Cognition 100, 464–482.
* 絵画命名課題における言語間の干渉と促進 A. Roelofs+ (2016) __Electrophysiology of cross-language interference and facilitation in picture naming__. http://dx.doi.org/10.1016/j.cortex.2015.12.003
* 累積意味，意味ブロック，意味妨害効果 A. Roelofs+ (2018) __A unified computational account of cumulative semantic, semantic blocking, and semantic distractor effects in picture naming__. https://doi.org/10.1016/j.cognition.2017.12.007


# 用語集 glossary

* BERT (**B**idirectional **E**ncoder **R**epresentations from **T**ransformers): Google が開発した Transformer に基づく言語モデル。マスク化言語モデルと次文予測課題によって事前訓練を行い，各下流課題に対して微調整 (fine turing) を行うことで SOTA を達成した。
* GPT (Generative Pretrained Transformer): [OpenAI 社](https://openai.com/) の開発した Transformer に基づく生成 AI モデルの一つ。
* LLM (Large Language Model): 大規模言語モデル。大規模コーパスによって訓練された言語モデル。近年の BERT, GPT 等の言語モデルはすべて LLM である。
* LM (Language Model): 言語モデル。伝統的には，直前までの単語から次単語を予測するモデルを指す。
* LangChain: LLM の API を提供している。
* PPO (Proxical Policy Gradient): 近位方針勾配法。強化学習の最適化手法の一つ。価値勾配法 に対して，方針 (policy) 勾配を用いる。[Schullman+2017](https://arXiv.org/abs/1707.06347)
* RNN (Recurrent Neural Networks): 再帰的ニューラルネットワーク。系列情報を扱うためのニューラルネットワークモデル。Elman ネット，Jordan ネット，LSTM, GRU などが含まれる。
* SOTA (State of the Art): 現時点での最高性能のこと。
* Transformer: [Vaswani+2017](https://arXiv.org/abs/1706.03762) によって提案された RNN の代替モデル。マルチヘッド注意 (MHSA) に基づく処理機構。
* カルバック=ライブラー・ダイバージェンス (Kullback–Leibler divergence): 2 つの確率密度関数の差異を定義する値。機械学習においては，目的関数とモデル出力との間で，カルバック=ライブラー・ダイバージェンスを用いる場合がある。
* ソフトマックス: 実数値を要素とするベクトルを，離散記号に変換する場合，最大値の値を大きくし，他の要素は 0 に近づける操作を行う場合がある。このときに用いられる変換がソフトマックス変換，あるいはソフトマックス関数という。ソフトマックス関数は，識別や分類を行う機械学習モデルの最終層に用いられワンホットベクトルを得る場合用いられる。また，その性質から Transformer ベースの注意機構の実装にも用いられている。
* ワンホットベクトル (one-hot vector): 言語処理に用いられるニューラルネットワークモデルでは，入出力が，単語や文字など記号表現である場合が多い。任意の記号を表す場合に，その記号に該当する位置だけが 1 で，他の要素はすべて 0 であるベクトルを用いる。このようにして作成されたベクトルを 1 つだけが熱く，他の要素がすべて冷たい，ワンホットベクトル，あるいはワンホット表現と呼ぶ。
* 単語埋め込み (word embeddings): 単語のベクトル表現。古くは潜在意味解析 (Latent Semantic Analysis) なども含まれるが，[word2vec](https://arXiv.org/abs/1301.3781) や [GloVe](http://nlp.stanford.edu/projects/glove/) などが代表的モデルである。
* 微調整 (Fine-tuning): 事前学習を施したモデルに対して，課題に合わせて再学習を行うこと。
* 文脈注入 (Context Injection): プロンプトの一つ。
* 転移学習 (Transfer learnign): 従来は最終層のみを課題に合わせて入れ替えて，最終層と最終直下層 (penultimate layers) の結合係数のみを調整することを指した。微調整 (fine-tuning) との相違は，再学習させる層の相違である。
* ロジスティック回帰: 回帰と名がつくが，分類問題を解くための手法。出力を確率と仮定して シグモイド関数 (logistic sigmoid functions) を用いる。
* シグモイド関数: $f(x) = \left( 1 + e^{-x}\right)^{-1}$ 連続量を確率的判断に変換する。すなわち 2 値 true or false, head or tail, $p$ or $1-p$ など。ニューラルネットワークでは伝統的に用いられてきた経緯がある。理由は，微分が極端に簡単になることが挙げられる。現在では ハイパータンジェント tanh や，整流線形関数 ReLU (Recutified Linear Unit) が用いられる場合が多い。理由は，勾配消失問題対策のため。
* ソフトマックス関数 (softmax function): 多値分類に用いられる。物理学のボルツマン分布，エネルギー関数と式としては同一。$\displaystyle f(x_i)=\frac{e^{x_i}}{\sum e^{x_i}}$. 左辺 LHS の 分母 the denominator は，分配関数 partition function と呼ばれる。
- 交差エントロピー損失: エントロピー $- p\log p$ は，熱力学と情報論とで用いられる概念。熱力学の第二法則，時間の矢 に関連。情報理論では，情報量の定義。機械学習では，分類問題の損失関数として頻用される。$-\left(t \log p + (1-t) \log(1-p)\right)$
- [次元圧縮 t-SNE](https://komazawa-deep-learning.github.io/t-SNE/) 2008 年の提案以来，よく見かけるようになった次元圧縮手法。
- サポートベクターマシン: ウラジミール・ヴァプニク(Vapnik) による 教師あり学習 (Vapnik 1999, 1998). ディープラーニング以前に主流であった。2 群分類で特徴を最もよく (マージン最大化) 分離する境界面決定アルゴリズム。カーネルトリック，スラック変数の導入。線形回帰，線形判別に比べて性能が出ると考えられていた。今でも，最終層における判別に応用されることがある。カラス=クーン=タッカー条件(KKT Karush-Kuhn-Tucker condition)を ラグランジェ未定乗項 Lagrange's multpliers 付きで解く
<center>
<img src="/assets/2015scikit-learn-0.16_svm_p150.jpg" style="width:66%"><br/>
出典: scikit-learn マニュアル
</center>
* 確率的勾配降下法 SGD: stochastic gradient descent methods. Bottou ら (2007) によって導入された機械学習における学習法の工夫の一つ。ミニバッチの導入を特徴とする。オンライン学習とバッチ学習の中間で，学習データをランダムサンプリングして学習に用いる。精度改善の手法ではないが，計算時間の削減に貢献。ビッグデータの使用を前提とする現代的な実用手段

<center>
<img src="/assets/2007Bottou_NIPSpage30.svg" style="width:77%">
</center>

- 多層パーセプトロン MLP: multi-layer perceptron:
* neural networks,
* perceptron, multi-layer perceptron, feed-forward
* convolution, feature engineering
* RNN (SRN, Elman, Jordan, LSTM, GRU)
* activation functions {sigmoide,tanh,ReLU}
* back-propagation {gradient descent algorithm}
* gradient vanishing problems, gradient exploding problems
* objective/error/loss functions
* MSE (mean square errors), NLL (negitive log likelihood), CE (cross entropy), ML (maximam likelihood), KL-divergence, EM algorithm
* optimization methods (SGD, AdaGrad, AdaDelta, RMSprop, Adam)
* dataset {training/validation/test}
* L0, L1, L2 normalization
* dropout
* over/under fitting
* batch normalization, skip-connection, ResNet
* auto-encoders
* reinforcement learning {environment, state, action, reward, value, q-value, policy, TD, REINFORCE, MDP, POMDP, SARSA, experice replay, advantage, duealing, double-Q, A3C}

