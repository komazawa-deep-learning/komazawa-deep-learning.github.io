---
title: 第13回 2025 年度開講 駒澤大学 心理学特講 IIIA
author: 浅川 伸一
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

$$
\newcommand{\mb}[1]{\mathbf{#1}}
\newcommand{\Brc}[1]{\left(#1\right)}
\newcommand{\Rank}{\text{rank}\;}
\newcommand{\Hat}[1]{\widehat{#1}}
\newcommand{\Prj}[1]{\mb{#1}\Brc{\mb{#1}^{\top}\mb{#1}}^{-1}\mb{#1}^{\top}}
\newcommand{\RegP}[2]{\Brc{\mb{#1}^{\top}\mb{#1}}^{-1}\mb{#1}^{\top}\mb{#2}}
\newcommand{\NSQ}[1]{\left|\mb{#1}\right|^2}
\newcommand{\Norm}[1]{\left|#1\right|}
\newcommand{\IP}[2]{\left({#1}\cdot{#2}\right)}
\newcommand{\Bar}[1]{\overline{\;#1\;}}
\newcommand{\of}[1]{\left(#1\right)}
$$

<div align="center">
<font size="+2" color="navy"><strong>ディープラーニングの心理学的解釈</strong></font><br/><br/>
</div>

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br/>
Date: 18/Jul./2025<br/>
Appache 2.0 license<br/>
</div>


# 第 13 回 強化学習

* [課題提出用フォルダ](https://drive.google.com/drive/u/3/folders/1JqlWt8l67rBYZA3zjcV4x0UjSwO1-Ys4){:target="_blank"}

## 実習教材

* [Cart Pole のデモ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/2015corona/blob/master/2023notebooks/2023_0618_1_getting_started.ipynb){:target="_blank"}

- [ランダム探索  <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/2019komazawa/blob/master/notebooks/2019komazawa_rl_ogawa_2_2_maze_random.ipynb){:target="_blank"}
- [方針勾配法 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/2019komazawa/blob/master/notebooks/2019komazawa_rl_ogawa_2_3_policygradient.ipynb){:target="_blank"}
- [SARSA <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/2019komazawa/blob/master/notebooks/2019komazawa_rl_ogawa_2_5_Sarsa.ipynb){:target="_blank"}
- [Q 学習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/2019komazawa/blob/master/notebooks/2019komazawa_rl_ogawa_2_6_Qlearning.ipynb){:target="_blank"}
* [DQN](https://komazawa-deep-learning.github.io/2020pytorch_tutorail_reinforcement_q_learning/){:target="_blank"}
* [REINFORCE.js](https://komazawa-deep-learning.github.io/reinforcejs/){:target="_blank"}

* アルファ碁, アルファ碁ゼロ, DQN, [Atari ゲーム (OpenAI Gym)](https://gym.openai.com/){:target="_blank"}
* [エージェント 57](https://deepmind.com/blog/article/Agent57-Outperforming-the-human-Atari-benchmark){:target="_blank"}

## 苦い教訓

- [Sutton のブログ，苦い教訓](/2019sutton_bitter_Lesson.pdf){:target="_blank"}

コンピュータビジョンにおいても，同様のパターンがある。
初期の手法では，視覚をエッジや一般化された円柱の探索，あるいは SIFT 特徴の観点から考えていた。
しかし今日では，このような考え方はすべて捨て去られている。
現代のディープラーニングニューラルネットワークは，畳み込みとある種の不変性という概念のみを使用し，はるかに優れた性能を発揮する。
<!--In computer vision, there has been a similar pattern.
Early methods conceived of vision as searching for edges, or generalized cylinders, or in terms of SIFT features.
But today all this is discarded. Modern deep-learning neural networks use only the notions of convolution and certain kinds of invariances, and perform much better.-->

これは大きな教訓である。
我々は同じような過ちを犯し続けている。
このことを理解し，それに効果的に抵抗するためには，我々はこうした間違いの魅力を理解しなければならない。
我々は，我々の考え方を構築しても長期的にはうまくいかないという苦い教訓を学ばなければならない。
この苦い教訓は，次のような歴史的観察に基づいている。
1) AI 研究者は，しばしばエージェントに知識を組み込もうとしてきた，
2) これは短期的には常に役に立ち，研究者を個人的に満足させた，
3) 長期的には，それは停滞し，さらなる進歩を阻害した，
4) 探索と学習による計算のスケーリングに基づく反対のアプローチによって，画期的な進歩がもたらされる，

最終的な成功は苦渋を帯びたものであり，しばしば不完全に消化される，
なぜなら，それは人間中心のアプローチに対する成功だからである。

<!--This is a big lesson.
As a field, we still have not thoroughly learned it, as we are continuing to make the s ame kind of mistakes.
To see this, and to effectively resist it, we have to understand the appeal of these mistakes.
We have to learn the bitter lesson that building in how we think we think does not work in the long run.
The bitter lesson is based on the historical observations that
1) AI researchers have often tried to build knowledge into their agents,
2) this always helps in the short term, and is personally satisfying to the researcher, but
3) in the long run it plateaus and even inhibits further progress, and
4) breakthrough progress eventually arrives by an opposing approach based on scaling computation by search and  learning.
The eventual success is tinged with bitterness, and often incompletely digested, because it is success over a
favored, human-centric approach.-->

## Sutton のブログより

<center>
<div style="text-align: left;width: 88%;background-color: powderblue;">
人工知能の長年の目標は，困難な領域でも超人的な能力をタブラ・ラサ方式で学習するアルゴリズムである。
最近では AlphaGo が囲碁の世界チャンピオンを破った初めてのプログラムとなった。
AlphaGo の木探索は，深層ニューラルネットワークを用いて局面の評価と手の選択を行う。
このニューラルネットワークは，人間の熟練した手からの教師付き学習と， 自分自身の競技からの強化学習によって訓練されている。
ここでは，人間のデータやガイダンス，ゲームルール以外の領域の知識を必要としない，強化学習のみに基づいたアルゴリズムを導入する。
AlphaGo は自分自身の教師となり AlphaGo 自身の手の選択や AlphaGo のゲームの勝敗を予測するようにニューラルネットワークが学習される。
このニューラルネットワークは，木探索の強度を向上させ，その結果，より質の高い手の選択が可能となり，次の反復ではより強力な自己対戦が可能となる。
タブララサからスタートした私たちの新しいプログラム AlphaGo Zero は，既発表のチャンピオンに敗れた AlphaGo に対して 100-0 で勝利するという超人的な成績を達成した。
</div>
</center>



# 強化学習，条件付け 心理学の教科書的説明

<img src="https://www.nobelprize.org/images/pavlov-12840-content-portrait-mobile-tiny.jpg" width="24%">
<a href="https://www.nobelprize.org/prizes/medicine/1904/pavlov/biographical/">Ian Pavlov</a>&nbsp;&nbsp;
<img src="https://www.bfskinner.org/wp-content/gallery/1970s-1990/BFS-IN-THE-OFFICE.jpg" width="24%">
<a href="https://www.bfskinner.org/archives/photos/">Burrhus Frederic Skinner</a>&nbsp;&nbsp;<br/>


<!-- <img src="http://incompleteideas.net/sutton-head5.jpg" width="24%"> --><!-- <img src="https://cloudfront.ualberta.ca/-/media/science/people/rsutton/sutton.jpg" width="24%"> -->
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Richard_Sutton_2021_%28cropped%29.jpg/500px-Richard_Sutton_2021_%28cropped%29.jpg" width="24%;">
<a href="http://incompleteideas.net/">Richard S. Sutton,</a>&nbsp;&nbsp;
<img src="https://people.cs.umass.edu/~barto/barto2006-lowres.jpg" width="24%">
<a href="https://people.cs.umass.edu/~barto/">Andrew G. Barto</a>


- [パブロフ](https://en.wikipedia.org/wiki/Ivan_Pavlov) (Ivan Petrovich Pavlov; 1849/Sep/14-1936/Feb/27)古典的条件づけ 1904 年ノーベル医学生理学賞
- [スキナー](https://en.wikipedia.org/wiki/B._F._Skinner) (Burrhus Frederic Skinner; 1904/Mar/20-1990/Aug/18) 道具的条件付け， オペラント条件づけ，[スキナー箱, Skinner(1938) Fig.1, page 39 より](./assets/1938Skinner_Fig1_skinnerBOX.jpg)
- [Sutton](http://incompleteideas.net/) and [Barto](http://www-anw.cs.umass.edu/~barto/) の強化学習 [初版 1998年](http://incompleteideas.net/book/first/the-book.html), [第2版 2018年](http://incompleteideas.net/book/the-book-2nd.html), [初版は翻訳あり](https://www.amazon.co.jp/dp/4627826613/)，第2版は pdf ファイルで[ダウンロード可能](http://incompleteideas.net/book/bookdraft2017nov5.pdf)


# 強化学習とは何か？

<center>
<img src="/assets/2018Sutton_Fig3j.svg" style="width:74%"><br/>
<p align="center" style="width:74%">
Sutton & Barto (2018) Fig. 3.2 を改変
</p>
</center>

強化学習という言葉は古い言葉ですが機械学習の文脈では，環境とその環境におかれた動作主（エージェントと言ったり，ロボットシステムだったりします）が，環境と相互作用しながらより良い行動を形成するためのモデルです。
動作主は，環境から受け取った現在の状態を分析して，次にとるべき行動を選択します。このとき将来に渡って報酬が最大となるような行動を学習する手法の一つです。

2015 年には，Google 傘下のデープマインドというスタートアップチームが開発した囲碁プログラム AlphaGo がプロ棋士のイ・セドル氏に勝利し話題になりました。
AlphaGo は強化学習を基本技術の一つとして用いています。

1. [強化学習(1): 基礎](https://komazawa-deep-learning.github.io/rl01_elements.pdf)
2. [強化学習(2): エージェントと環境](https://komazawa-deep-learning.github.io/rl02_agentAndEnv.pdf)
3. [強化学習(3): 目標と報酬](https://komazawa-deep-learning.github.io/rl03_goalAndReward.pdf)
4. [強化学習(4): マルコフ決定過程](https://komazawa-deep-learning.github.io/rl04_mdp.pdf)
5. [強化学習(5): 価値反復，方策反復](https://komazawa-deep-learning.github.io/rl05_vi.pdf)
6. [強化学習(6): ](https://komazawa-deep-learning.github.io/rl06_advanced.pdf)
6. [強化学習(7): ](https://komazawa-deep-learning.github.io/rl07_robotics.pdf)

<!-- - エージェントと環境，マルコフ決定過程 MDP，POMDP，効用関数，ベルマン方程式，探索と利用のジレンマ，SARSA:
- 価値，方策，Q 学習，モデルベース対モデルフリー，アクター=クリティック:
- 深層 Q 学習:
- ゲーム AI へ (AlphaGo，AlphaGoZero，OpenAI five):
- セルフプレイ:
- 最近の発展 A3C，Rainbow，RDT，World model: -->

<!--
### 方策，報酬，価値観数，(環境)モデル

- $s,s'$: 状態 state
- $a$: 行動，行為 action
- $r$: 報酬 reward
- $t$: 時間 (離散時間 $t=1,2,\ldots,T$)
- $p(s',r\vert s, a)$: 状態 $s$ で行為 $a$ を行ったとき，報酬 $r$ を受け取って 状態 $s'$ に遷移する確率
- $p(s'\vert s, a)$: 状態 $s$ で行為 $a$ を行った場合，状態 $s'$ へ遷移する確率
- $r(s,a)$: 状態 $s$ で行為 $a$ を行った場合の即時報酬 immediate reward の期待値
- $r(s,a,s')$: 行為 $a$ を行った場合状態が $s$ から $s'$ へ変化したときの即時報酬の期待値
- $v_\pi(s)$: 方策 $\pi$ での状態 $s$ の価値 (期待報酬)
- $v_*(s)$: 最適方策化での状態 $s$ の価値
- $q_\pi(s,a)$: 方策 $\pi$ のもとで状態 $s$ で行為 $a$ をおこなた場合の価値
- $q_*(a)$: 行動 $a$ を行った場合の期待報酬(真の報酬) <!-- true value (expected reward) of action $a$-->

<!--
- $Q_t(a)$: 時刻 $t$ での $q_*(a)$ の期待値 qestimate at time $t$ of $q_*(a)$
- $N_t(a)$: 時刻 $t$ で行為 $a$ を行った回数 number of times action $a$ has been selected up prior to time $t$
- $H_t(a$) 時刻 $t$ で行為 $a$ を行う傾向(選好 preference) learned preference for selecting action a at time $t$
- $\pi_t(a)$: 時刻 $t$ で行為 $a$ を選択する確率 probability of selecting action a at time $t$
- $R_t$: $\pi_t$ が与えられた場合，時刻 $t$ における の期待報酬 estimate at time $t$ of the expected reward given $\pi_t$
--->


## 複雑な状況をどう理解して解決するのか？

- 強化学習というニューラルネットワークモデルがあるわけではない
- 動的で複雑な環境に対処 $\rightarrow$ **強化学習** + DL $\rightarrow$ 一般人工知能への礎

- DQN ATARIのビデオゲーム, [https://www.nature.com/articles/nature14236](https://www.nature.com/articles/nature14236)
- AlphaGo 囲碁, [https://www.nature.com/articles/nature16961](https://www.nature.com/articles/nature16961)
- AlphaGoZero 囲碁, [https://www.nature.com/articles/nature24270](https://www.nature.com/articles/nature24270)

# Deep Q Network

<center>

<img src="/assets/2015DQNFig1.svg" width="66%"><br/>
DQNの模式図, 原著論文より
</center>

<!--
- [ギャラガ1](/assets/MOV_0013s.mp4)
- [ギャラガ2](/assets/MOV_0071s.mp4)
-->

- **Q 学習** Q learning に DNN を採用
- CNN が LeNet, [@1998LeCun] そうであったように，強化学習 RL も昔からの技術 [@Sutton_and_Barto1998]
- ではなぜ，今になって囲碁や自動運転に応用できるようになったのか？
  - $\Rightarrow$ コンピュータの能力, データ規模，アルゴリズムの改良, エコシステム(ArXiv, Linux, Git, ROS, AMT, TensorFlow)

<!--
# 強化学習

- 強化学習 $\Rightarrow$ 意思決定
  - **エージェント** agent が **行動**(行為) action をする
  - 行動によって **状態** が変化する
  - **環境** から与えられる **報酬** によって**目標**が決定
- 深層学習: $\Rightarrow$ 表現，表象
  - 教師信号として目標が与えられる
  - 目標を達成するために外部状況の **表現** を獲得

<center>
<font size="+2" color="Green">強化学習 + 深層学習 = 人工知能</font>
</center>

  - 強化学習 $\Rightarrow$ 目標の設定
  - 深層学習 $\Rightarrow$ 内部表象の獲得機構を提供

# 用語の整理

- 教師信号なし **報酬信号** reward signal
- 遅延フィードバック

- **価値** Value
- **行為** Action
- **状態** State
- TD 学習
  - **Sarsa**
  - **Q 学習**
  - **アクタークリティック**
- 報酬 $R_t$: **スカラ値**
  - 時刻 $t$ でエージェントのとった行動を評価する指標
  - エージェントは**累積報酬** cumulative reward の最大化する
  - 報酬仮説: **目標は累積期待報酬の最大化として記述可能**
-->

## DQN 結果

<center>

<img src="/assets/2015Mnih_DQNFig.png" style="width:39%"><br/>
</center>


## YouTube 上でのデモ動画

* ブロック崩し: [https://www.youtube.com/watch?v=V1eYniJ0Rnk](https://www.youtube.com/watch?v=V1eYniJ0Rnk)
* スペースインベーダー: [https://www.youtube.com/watch?v=W2CAghUiofY](https://www.youtube.com/watch?v=W2CAghUiofY)

<!--- packman: [https://www.youtube.com/watch?v=r3pb-ZDEKVg](https://www.youtube.com/watch?v=r3pb-ZDEKVg)
- OpenMind selfplay: [https://www.youtube.com/watch?v=OBcjhp4KSgQ](https://www.youtube.com/watch?v=OBcjhp4KSgQ)

-->
<!--
* DQN の動画 スペースインベーダー

<center>

<video style="width:33%" controls src="/assets/2015Mnih_DQN-Nature_Video1.mp4" type="video/mp4" >
</center>

* DQN の動画 ブロック崩し

<center>

<div>
<video style="width:33%" controls src="/assets/2015Mnih_DQN-Nature_Video2.mp4" type="video/mp4" >
</div>
</center>
-->

<!-- ## なぜ DQN には難しいのか？

<center>
<div>
<video style="width:74%" controls src="/assets/Montezuma.mp4" type="video/mp4" /></br>
**Montezuma**
</div>
</center>

<center>
<video style="width:74%" controls src="/assets/PrivateEye.mp4" type="video/mp4" /></br>
**Private Eye**
</center>

<center>
<video width="39%" autoplay loop markdown="0" controls muted>
  <source src="./assets/Montezuma.mp4">
</video>
<video width="39%" autoplay loop markdown="0" controls muted>
  <source src="./assets/privateEye.mp4">
</video>
 -->

## 人間にはできて強化学習には難しいこと

- Montenzuma's Revenge の動画 [https://www.youtube.com/watch?v=Klxxg9JM5tY](https://www.youtube.com/watch?v=Klxxg9JM5tY)
- Private Eys の動画 [https://www.youtube.com/watch?v=OfyS-Wj1M78](https://www.youtube.com/watch?v=OfyS-Wj1M78)

<!---
## エージェントと環境

- At each step $t$ the agent:
  - Executes action $A_t$
  - Receives observation $O_t$
  - Receives scalar reward $R_t$
- The environment:
  - Receives action $A_t$
  - Emits observation $O_{t+1}$
  - Emits scalar reward $R_{t+1}$
- $t$ increments at env. step
-->

<!--
- **エージェント**: 学習と意思決定を行う主体
  1. **行動** action **$A_t$** を行い
  1. 環境の **観察** observation **$O_t$** を行う
  1. 環境からスカラ値の **報酬** reward **$R_t$** を受け取る
- **環境**: エージェント外部の全て
  1. エージェントから **行為** $A_t$ を受け取り
  1. エージェントに **観察** $O_{t+1}$ を与え
  1. エージェントへ **報酬** $R_{t+1}$ を与える

## エージェントの要素

- **方策** Policy
- **価値関数** Value function
- **モデル** エージェントが持つ環境の表象

## 方策 policy

- **方策** : エージェントの行為
- 決定論的方策: $a=\pi(S)$
- 確率論的方策: $\pi(a|s)=p(A_{t=a}|S_{t=s})$

## 価値関数
- 将来の報酬予測
- 状態評価(良/悪)
- 行為の選択
$$
v_\pi(S)=\mathbb{E}_\pi\left\{R_{t+1}+\gamma R_{t+2} + \gamma^2R_{t+3}+\ldots|S_{t=s}\right\}
$$

## 強化学習のモデル
- 価値ベース
  - 方策:なし
  - 価値関数:あり
- 方策ベース
  - 方策:あり
  - 価値関数:なし
- アクター=クリティック Actor Critic
  - 方策: あり
  - 価値関数: あり

- モデルフリー
  - 方策，価値関数: あり
  - モデル: なし
- モデルベース
  - 方策，価値関数: あり
  - モデル: あり

## 探索と利用のジレンマ Exploration and exploitaion dilemma
- 過去の経験から，一番良いと思う行動ばかりをしていると，さらに良い選択肢を見つけ出すことができない **探索不足**
- 更に良い選択肢ばかり探していると過去の経験が活かせない **過去の経験の利用不足**

## 目標，収益，報酬

- エージェントの目標は累積報酬を最大化すること (報酬仮説)
  - **報酬仮説** Reward Hypothesis
  - 目標: 期待報酬の最大化

- 時刻 $t$ における報酬 $R_t$ : **スカラ値**
- 時刻 $t$ におけるエージェント行為の評価

## 逐次的意思決定 Sequential Decision Making
- 目標 Goal: 総収益を最大化する行動を選択すること
- 行為，行動 Actions は長期的結果
- 収益は遅延することも有る
- 直近の報酬を選ぶよりも，長期的な報酬を考えた方が良い場合がある


## 収益 Return
- **収益** return $G_t$: 割引付き収益
$$
G_t=R_{t+1}+\gamma R_{t+2}+\ldots=\sum_{k=0}^{\infty}\gamma^k R_{t+k+1}
$$

- 割引率 The discount $\gamma\in\left\{0,1\right\}$ : 現時点から見た将来の報酬を計算するため

- **遅延報酬** delayed reward の評価
- $0$ に近ければ __近視眼的__ 評価
- $1$ に近ければ __将来を見通した__ 評価

## 価値関数 Value Function

- **状態価値関数 $v$ ** と **行動価値関数 $q$ **

- **価値関数** $v(s)$: gives the long-term value of state $s$
- **状態価値関数** $v(s)$ of an MRP is the expected return starting from state $s$
$$
v(s)=\mathbb{E}\left\{G_t|S_{t=2}\right\}
$$

- **状態価値関数** state-value function:
$$
v_\pi(s)=\mathbb{E}_\pi\left\{G_t|S_{t=s}\right\}
$$

# ベルマン期待期待 Bellman Expectation Equation
- **状態価値関数** : 即時報酬と後続状態の割引付き報酬の和に分解できる

$$
v_\pi(s)=\mathbb{E}_\pi\left\{R_{t+1}+\gamma v_\pi(S_{t+1}|S_t=s)\right\}
$$

- **行動価値関数** action-value function:
$$
q_\pi(s,a)=\mathbb{E}_\pi\left\{G_t|S_{t}=s,A_{t}=a\right\}
$$

- **行動価値関数** 同じく分解可能 The action-value function can similarly be decomposed,
$$
q_\pi(s,a)=\mathbb{E}_\pi\left\{R_{t+1}+\gamma q_\pi(S_{t+1},A_{t+1})|S_{t}=s,A_{t}=a\right\}
$$


## 最適価値関数 Optimal Value Function
- 最適状態価値関数
$$
v_{*}(s) = \max_{\pi} v_{\pi}(s)
$$
- 最適行動価値関数
$$
q_{*}(s,a)=\max q_{\pi}(s,a)
$$

- ベルマン方程式 一般に非線形になるので難しい
-->

<!--
- No closed form solution (in general)
- Many iterative solution methods
- 幾つかの解法:
  - 価値反復
  - 方策反復
  - Q 学習
  - sarsa
-->

<!--
  - Value Iteration
  - Policy Iteration
  - Q-learning
  - Sarsa
-->

<!--
# Markov Reward Process
A Markov reward process is a Markov chain with values.

- A Markov Reward Process is a tuple $<S,P,R,\gamma>$
  - $S$ is a finite set of states
  - $P$ is a state transition probability matrix,
  - $P_{ss'}=P\of{S_{t+1}=s'\given{S_t=s}}$
  - $R$ is a reward function, $R_s=\mathbb{E}\BRc{R_{t+1}\given{S_t=s}}$
  - $\gamma$ is a discount factor

# Bellman Equation for MRPs
The value function can be decomposed into two parts:
  - immediate reward $R_{t+1}$
  - discounted value of successor state $\gamma v\of{S_{t+1}}$

$$
\begin{array}{lll}
v\of{s}&=&\mathbb{E}\BRc{G_t\given{S_t=s}}\\
&=&\mathbb{E}\BRc{R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\ldots\given{S_{t}=s}}\\
&=&\mathbb{E}\BRc{R_{t+1}+\gamma\Brc{R_{t+2}+\gamma R_{t+3}+\ldots}\given{S_{t}=s}}\\
&=&\mathbb{E}\BRc{R_{t+1}+\gamma G_{t+1}\given{S_{t}=s}}\\
&=&\mathbb{E}\BRc{R_{t+1}+\gamma v\of{S_{t+1}\given{S_{t}=s}}}
\end{array}
$$

# Bellman Equation for MRPs

$$
v\of{s}=\mathbb{E}\BRc{R_{t+1}+\gamma v\of{S_{t+1}}\given{S_t=s}}
$$


$$
v\of{s}=R_s +\gamma\sum_{s'\in S} P_{ss'}v\of{s'}
$$

# Solving the Bellman Equation
- The Bellman equation is a linear equation
- It can be solved directly:
$$
\begin{array}{lll}
v &=& R +\gamma Pv\\
\Brc{I - \gamma P}v &=& R\\
v &=& \Brc{I-\gamma P}^{-1}R
\end{array}
$$

- Computational complexity is $O(n^3)$ for $n$ states
- Direct solution only possible for small MRPs
- There are many iterative methods for large MRPs, e.g.
  - Dynamic programming
  - Monte-Carlo evaluation
  - Temporal-Difference learning
-->


<!-- # 価値関数 Value Function -->
<!-- - 将来の報酬予測の関数 -->
<!--   - ある状態である行動を起こすとどれほどの報酬が得られるか -->
<!-- - **Q-値関数** Q-value function : 総期待報酬を得る関数<\!--gives expected total reward-\-> -->
<!--   - 方策 $\pi$ のもとで -->
<!--   - 状態 $s$ で行動 $a$ を行ったとき -->
<!-- $$ -->
<!--   Q^\pi\of{s,a}=\mathbb{E}\BRc{r_{t+1}+\gamma r_{t+2}+\gamma^2 r_{t+3}+\ldots\given{s,a}} -->
<!-- $$   -->

<!--
# 最適価値関数 Optimal Value Functions
- 最大の価値を与える関数
$$
Q^*(s,a)=\max_{\pi}Q^\pi(s,a)=Q^{\pi^*}(s,a)
$$
- 最適価値関数 $Q^*$ が得られれば最適方策 $\pi^*$ を求めることができる
$$
\pi^*(s)=\operatorname{argmax}_aQ^*(s,a)
$$

- 全ての意思決定における最適価値:
$$
\begin{array}{lll}
Q^*(s,a)&=&r_{t+1}+\gamma\max_{a_{t+1}}r_{t+2}+\gamma^2\max_{a_{t+2}}r_{t+3}+\ldots\\
           &=&r_{t+1}+\gamma\max_{a_{t+1}}Q^*(s_{t+1},a_{t+1})
\end{array}
$$
-->

<!-- from sliver (2016) icml lecture -->
<!--
- **ベルマン方程式** Bellman equation:
$$
Q^*(s,a)=\mathbb{E}_{s'}\left\{r+\gamma\max_{a'}Q^*(s',a')|s,a\right\}.
$$
-->

<!--
# 報酬(収益) Rewards
- 時刻 $t$ における報酬 $R_t$ : **スカラ値**
- 時刻 $t$ におけるエージェント行為の評価Indicates how well agent is doing at step $t$

# Sequential Decision Making
- 目標 Goal: select actions to maximise total future reward
- 行為 Actions はmay have long term consequences
- 収益は遅延することも有る
- 直近の報酬を選ぶよりも，長期的な報酬を考えた方が良い場合がある It may be better to sacrifice immediate reward to gain more long-term reward-
- Examples:
  - A financial investment (may take months to mature)
  - Refuelling a helicopter (might prevent a crash in several hours)
  - Blocking opponent moves (might help winning chances many moves from now)
-->


## 強化学習の歴史

* [David Silver homepage](https://www.davidsilver.uk/){:target="_blank"}


## DeepMind による強化学習

* [DQN: Human-level control through deep reinforcement learning](https://www.nature.com/articles/nature14236){:target="_blank"}
* [AlphaGo: Mastering the game of Go with deep neural networks and tree search](https://www.nature.com/articles/nature16961){:target="_blank"}
* [AlphaGo Zero: Mastering the game of Go without human knowledge](https://www.nature.com/articles/nature24270){:target="_blank"}


<div class="figcenter">
<img src="/assets/2016AlphaGo_Fig1a.svg" style="width:44%;">
<img src="/assets/2016AlphaGo_Fig1b.svg" style="width:49%;"><br/>
AlphaGo の模式図，原著論文より
</div>

<!-- <div class="figcaption"> -->

**図 1. ニューラルネットワークの学習パイプラインとアーキテクチャ**<br/>
**a**  高速ロールアウト方針 $p_\pi$ と教師あり学習 (SL: supervised learning) 方針ネットワーク $p_\sigma$ は，棋盤上の位置データセットにおける人間の専門家の動きを予測するために学習される。
強化学習 (RL: Reinforcement Learning) 方針ネットワーク $p_\rho$ は教師あり学習方針ネットワークに初期化され，方針勾配学習によって方針ネットワークの以前のバージョンに対する結果 (すなわち，より多くのゲームに勝つこと) を最大化するように改善される。
新しいデータ集合は，強化学習方針ネットワークと自己対戦ゲームを行うことによって生成される。
最後に，価値ネットワーク $v_\theta$ が回帰によって訓練され，自己対戦データセットから位置における期待結果（つまり，現在のプレイヤーが勝つかどうか）を予測する。<br/>
**b**  AlphaGo で使用されているニューラルネットワークアーキテクチャの模式図。
方針ネットワークは，碁盤上の位置の表現 $s$ を入力とし，それをパラメータ $\sigma$ （教師あり学習方針ネットワーク）または $\rho$ （強化学習方針ネットワーク）を持つ多層畳み込み層に通し，碁盤上の確率地図によって表される，合理的な手 $a$ に関する確率分布 $p_{\sigma}(a|s)$ または $p_{\rho}(a|s)$ を出力する。
価値ネットワークも同様に，パラメータ $\theta$ を持つ多数の畳み込み層を使用するが，位置 $s'$ における期待結果を予測するスカラ値 $v_{\theta}(s')$ を出力する。
<!-- Figure 1. Neural network training pipeline and architecture.
a, A fast rollout policy pπ and supervised learning (SL) policy network pσ are trained to predict human expert moves in a data set of positions.
A reinforcement learning (RL) policy network pρ is initialized to the SL policy network, and is then improved by policy gradient learning to maximize the outcome (that is, winning more games) against previous versions of the policy network.
A new data set is generated by playing games of self-play with the RL policy network.
Finally, a value network vθ is trained by regression to predict the expected outcome (that is, whether the current player wins) in positions from the self-play data set.
b, Schematic representation of the neural network architecture used in AlphaGo. The policy network takes a representation of the board position s as its input, passes it through many convolutional layers with parameters σ (SL policy network) or ρ (RL policy network), and outputs a probability distribution σpa(|s) or ρpa(|s) over legal moves a, represented by a probability map over the board.
The value network similarly uses many convolutional layers with parameters θ, but outputs a scalar value vθ(s′) that predicts the expected outcome in position s′. -->
<!-- </div> -->

### アルファ碁ゼロにおける強化学習<!-- ### Reinforcement learning in AlphaGo Zero-->

我々の新手法は，パラメータ $\theta$ を持つ深層ニューラルネットワーク $f_{\theta}$ を使用する。
このニューラルネットワークは，位置とその履歴の生の碁盤表現 s を入力とし，手の確率と価値， $(p,v)=f_{\theta}(s)$ の両方を出力する。
手の確率のベクトル $p$ は，各手 $a$ (パスを含む) を選択する確率を表し，$p_a=Pr(a|s)$ である。
価値 $v$ はスカラ評価であり，現在のプレイヤーが位置 $s$ から勝つ確率を推定する。
このニューラルネットワークは，方針ネットワークと価値ネットワーク(12) の両方の役割を 1 つのアーキテクチャにまとめたものである。
ニューラルネットワークは，バッチ正規化(18) と整流非線形 (19) を持つ畳み込み層 (16,17) の多数の残差ブロック(4)  から構成される (「手続き」節参照)。
<!--Our new method uses a deep neural network fθ with parameters θ.
This neural network takes as an input the raw board representation s of the position and its history, and outputs both move probabilities and a value, (p,v)=fθ(s).
The vector of move probabilities p represents the probability of selecting each move a (including pass), pa=Pr(a|s).
The value v is a scalar evaluation, estimating the probability of the current player winning from position s.
This neural network combines the roles of both policy network and value network12 into a single architecture.
The neural network consists of many residual blocks4 of convolutional layers(16,17) with batch normalization18 and rectifier nonlinearities(19) (see Methods) -->

AlphaGoZero のニューラルネットワークは，新しい強化学習アルゴリズムによって，自己対局のゲームから学習される。
各位置 s において，ニューラルネットワーク $f_{\theta}$ によって導かれる MCTS 探索が実行される。
MCTS 探索は，各手を打つ確率 $\pi$ を出力する。
これらの探索確率は通常，ニューラルネットワーク $f_{\theta}(s)$ の生の手確率 $p$ よりもはるかに強い手を選択する。
したがって，MCTS は強力な方針改善演算子と見なすことができる (20,21)。
探索を伴う自己対局の各手を選択するために改善された MCTS に基づく方針を使用し，その後，価値のサンプルとしてゲームの勝者 z を使用するのは，強力な方針評価演算子と見なすことができる。
ニューラルネットワークのパラメータは，手の確率と値 $(p,v)=f_{\theta}(s)$ が，改善された探索確率と自己対局の勝者 $(\pi,z)$ とより密接に一致するように更新される。
これらの新しいパラメータは自己対局の次の反復で使用され，探索をより強力にする。
図 1 は自己対局の訓練パイプラインを示している。
<!-- The neural network in AlphaGo Zero is trained from games of selfplay by a novel reinforcement learning algorithm.
In each position s, an MCTS search is executed, guided by the neural network fθ.
The MCTS search outputs probabilities π of playing each move.
These search probabilities usually select much stronger moves than the raw move probabilities p of the neural network fθ(s); MCTS may therefore be viewed as a powerful policy improvement operator(20,21).
Self-play with search—using the improved MCTS-based policy to select each move, then using the game winner z as a sample of the value—may be viewed as a powerful policy evaluation operator.
The main idea of our reinforcement learning algorithm is to use these search operators repeatedly in a policy iteration procedure22,23: the neural network’s parameters are updated to make the move probabilities and value (p,v)=f_θ(s) more closely match the improved search probabilities and self-play winner (π,z); these new parameters are used in the next iteration of self-play to make the search even stronger.
Figure 1 illustrates the self-play training pipeline. -->

<div class="figcenter">
<img src="/2024assets/2017Silver_AlphaGoZero_fig1_.svg" style="width:44%;">
</div>

**図 1 AlphaGoZero における自己対戦強化学習**<br/>
**a**: プログラムは自分自身と対局 $s_1,\ldots,s_T$ を行う。
各位置 $s_t$ において，最新のニューラルネットワーク $f_\theta$ を用いて MCTS（モンテカルロ木探索）$\alpha_\theta$ が実行される（図 2 参照）。
移動は MCTS によって計算された探索確率に従って，$a_t\sim\pi_t$ で選択される。
終端位置 $s_T$ はゲームの勝者 $z$ を計算するためにゲームのルールに従って得点される。<br/>
**b**, AlphaGoZero におけるニューラルネットワークの学習。
ニューラルネットワークは生の盤面位置 $s_t$ を入力とし，それをパラメータ $\theta$ を持つ多層畳み込み層に通し，手に関する確率分布を表すベクトル $p_t$ と，現在のプレイヤーが位置 $s_t$ で勝利する確率を表すスカラー値 $v_t$ の両方を出力する。
ニューラルネットワークのパラメータ $\theta$ は，探索確率 $\pi_t$ に対する方針ベクトル $p_t$ の類似性を最大化し，予測勝者 $v_t$ とゲーム勝者 $z$ との誤差を最小化するように更新される（式(1)参照）。
新しいパラメータは，$a$ のように，次の自己プレイの繰り返しで使用される。
<!-- Figure 1 Self-play reinforcement learning in AlphaGo Zero.
a, The program plays a game s1, ..., sT against itself.
In each position st, an MCTS (Monte Carlo Tree Search) αθ is executed (see Fig. 2) using the latest neural network fθ.
Moves are selected according to the search probabilities computed by the MCTS, at ∼ πt.
The terminal position sT is scored according to the rules of the game to compute the game winner z.
b, Neural network training in AlphaGo Zero. The neural network takes the raw board position st as its input, passes it through many convolutional layers with parameters θ, and outputs both a vector pt, representing a probability distribution over moves, and a scalar value vt, representing the probability of the current player winning in position st.
The neural network parameters θ are updated to maximize the similarity of the policy vector pt to the search probabilities πt, and to minimize the error between the predicted winner vt and the game winner z (see equation (1)).
The new parameters are used in the next iteration of self-play as in a. -->

MCTS はニューラルネットワーク $f_\theta$ を用いてシミュレーションを行う (図 2)。
探索木の各辺 (s,a) には事前確率 $P(s,a)$，訪問回数 $N(s,a)$，行動価値 $Q(s,a)$ が格納されている。
各シミュレーションはルート状態から開始し，葉ノード s’ に遭遇するまで，$U(s,a)\sim P(s,a)/(1 + N(s,a)$) (文献12, 24) である上限信頼限界 $Q(s,a)+U(s,a)$ を最大にする手を反復的に選択する。
この葉の位置は，事前確率と評価 $(P(s',\cdot),V(s'))=f_\theta(s’)$ の両方を生成するために，ネットワークによって一度だけ展開され評価される。
シミュレーションで通過した各辺 (s,a) は，その訪問回数 N(s,a) をインクリメントするように更新され，その行為価値をこれらのシミュレーションの平均評価に更新する，$Q(s,a)=1/N(s,a)\sum_{s'|s,a\mapsto s'}V(s’)$ ここで s,a→s’ はシミュレーションが最終的に位置 $s$ から移動 $a$ をとって $s’$ に到達したことを示す。
<!-- The MCTS uses the neural network fθ to guide its simulations (see Fig. 2).
Each edge (s,a) in the search tree stores a prior probability P(s,a), a visit count N(s,a), and an action value Q(s,a).
Each simulation starts from the root state and iteratively selects moves that maximize an upper confidence bound Q(s,a)+U(s,a), where U(s,a)∝P(s,a)/(1 + N(s,a)) (refs 12, 24), until a leaf node s' is encountered.
This leaf position is expanded and evaluated only once by the network to generate both prior probabilities and evaluation, (P(s',·),V(s'))=f_\theta(s').
Each edge (s, a) traversed in the simulation is updated to increment its visit count N(s,a), and to update its action value to the mean evaluation over these simulations, Q(s,a)=1/N(s,a)\sum_{}V(s') where s,a→s' indicates that a simulation eventually reached s' after taking move a from position s. -->

<div class="figcenter">
<img src="/2024assets/2017Silver_AlphaGoZero_fig2_.svg" style="width:54%;">
</div>

**図 2. AlphaGo Zero における MCTS**<!-- Figure 2. MCTS in AlphaGo Zero.--><br/>
**a**, 各シミュレーションは，最大行動価値 Q と，保存された事前確率 P とそのエッジの訪問回数 N に依存する上限信頼区間 U を持つエッジを選択することによって木を探索する（これは一度探索されると増分される）。<br/>
**b**, 枝ノードが展開され，関連する位置 s がニューラルネットワーク $P(s,-),V(s))=f_{\theta}(s)$ によって評価される。<br/>
**c**, 行動価値 Q は，その行動の下の部分木内のすべての評価 V の平均を追跡するように更新される。<br/>
**d**, 探索が完了すると，$N^{1/\tau}$ に比例した探索確率 $\pi$ が返される。
ここで，N はルート状態からの各移動の訪問回数，$\tau$ は温度を制御するパラメータ。
<!-- a, Each simulation traverses the tree by selecting the edge with maximum action value Q, plus an upper confidence bound U that depends on a stored prior probability P and visit count N for that edge (which is incremented once traversed).
b, The leaf node is expanded and the associated position s is evaluated by the neural network (P(s,·),V(s))=f_θ(s); the vector of P values are stored in the outgoing edges from s.
c, Action value Q is updated to track the mean of all evaluations V in the subtree below that action.
d, Once the search is complete, search probabilities π are returned, proportional to N^{1/τ}, where N is the visit count of each move from the root state and τ is a parameter controlling temperature.-->

MCTS はニューラルネットワークパラメータ $\theta$ とルート位置 s が与えられると，打つべき手を推奨する探索確率のベクトル $\pi=a_\theta(s)$ を計算し，各手に対する指数化された訪問回数$\pi_{a}\propto N(s,a)^{1/\tau}$ に比例する自己プレイアルゴリズムと見なすことができる。
ここで $\tau$ は温度パラメータである。
<!-- MCTS may be viewed as a self-play algorithm that, given neural network parameters θ and a root position s, computes a vector of search probabilities recommending moves to play, π=α_θ(s), proportional to
the exponentiated visit count for each move, π_a∝N(s,a)^{1/τ}, where τ is a temperature parameter. -->

ニューラルネットワークは，MCTSを用いて各手を打つ自己再生強化学習アルゴリズムによって学習される。
まず，ニューラルネットワークはランダムな重み $\theta_0$ に初期化される。
続く各反復 $i\ge 1$ において，自己対局ゲームが生成される (図 1a)。
各タイム・ステップ $t$ で，ニューラルネットワーク $f_{\theta_{i-1}}$ の前の反復を用いて MCTS 探索 $\pi_t =a_{\theta_{t- i}}(s_t)$ が実行され，探索確率 $\pi_{t}$ をサンプリングすることによって手が打たれる。
ゲームは，両プレイヤーがパスしたとき，探索値が諦めの閾値を下回ったとき，またはゲームが最大長を超えたときにステップ $T$ で終了する。
その後，ゲームは $r_T\in\left[-1,+1\right]$ の最終報酬を与えるように採点される (詳細は方法参照)。
各タイムステップ $t$ のデータは $(s_t,\pi_t, z_t)$ として保存され $z_t=\pm r_T$ はステップ $t$ における現在のプレイヤーから見たゲームの勝者である。
並行して (図1b)，新しいネットワーク・パラメータ $\theta_i$ が，自己対局の最後の反復の全タイム・ステップ間で一様にサンプリングされたデータ $(s,\pi,z)$ から学習される。
ニューラルネットワーク $(p,v)=f_{\theta_{i}}(s)$ は，予測値 v と自己対局の勝者 z との間の誤差を最小化し，ニューラルネットワークの移動確率 $p$ と探索確率 $\pi$ との類似性を最大化するように調整される。
具体的には，パラメータ $\theta$ は，平均二乗誤差と交差エントロピー損失をそれぞれ合計する損失関数lの勾配降下によって調整される：
<!-- The neural network is trained by a self-play reinforcement learning algorithm that uses MCTS to play each move.
First, the neural network is initialized to random weights θ0. At each subsequent iteration i≥1, games of self-play are generated (Fig. 1a).
At each time-step t, an MCTS search π =αθ−t i 1(st) is executed using the previous iteration of neural network θ − f i 1 and a move is played by sampling the search probabilities πt.
A game terminates at step T when both players pass, when the search value drops below a resignation threshold or when the game exceeds a maximum length; the game is then scored to give a final reward of rT ∈ {− 1,+ 1} (see Methods for details).
The data for each time-step t is stored as (st, πt, zt), where zt = ± rT is the game winner from the perspective of the current player at step t.
In parallel (Fig. 1b), new network parameters θi are trained from data (s, π, z) sampled uniformly among all time-steps of the last iteration(s) of self-play.
The neural network = (p, v) fθ (s) i is adjusted to minimize the error between the predicted value v and the self-play winner z, and to maximize the similarity of the neural network move probabilities p to the search probabilities π.
Specifically, the parameters θ are adjusted by gradient descent on a loss function l that sums over the mean-squared error and cross-entropy losses, respectively: -->
$$\tag{1}
(\mathbf{p},v)=f_{\theta}(s) \text{ and } l=(z-v)^{2} - \pi^{\top}n \log\mathbf{p} + c\left\|\theta\right\|^{2}
$$
ここで c は L2 重みの正則化レベルを制御するパラメータである（過学習を防ぐため）。
<!-- where c is a parameter controlling the level of L2 weight regularization (to prevent overfitting). -->

<center>
<div style="text-align: left;width: 88%;background-color: powderblue;">
ムーブ３７:
ムーブ３７とはアルファ碁とイセドル氏との対局において，アルファ碁の打った決定的な３７手目（第四局）のことを指す。
アルファ碁の置いた３７手目の石はとくに評判になったため記憶に新しい。
ムーブ３７の意味は以下のように解釈できる。人類が積み上げてきた経験則である定石が，盤石とは限らないことを示した点にある。
囲碁の世界王者であっても経験に基づいた知識である。すべての可能な石の配置で構成される囲碁空間は膨大が量の人類が築き上げてきた経験の結集であっても，可能な囲碁配置空間の一部に過ぎず結果として偏っていた可能性がある。
このことを示してくれたのがムーブ３７といえる。
確かに千年以上の歳月をかけて人類が探索してきた碁石の可能な配置空間は広大である。
だが可能な囲碁の配置空間は，現在まで我われが探索してきた空間よりも広大であったのであり，アルファ碁なくしては人類が到達し得ない地平が存在したのである。
それまでは，知の地平の存在に気がついていた碩学が存在したとしても，具体例を示すことができず，従って説得力 を持った議論が展開できなかったのである。
</div>
</center>

* Mastering the game of Go without human knowledge

<center>
<div style="text-align: left;width: 88%;background-color: powderblue;">
人工知能の長年の目標は， 困難な領域でも超人的な能力をタブラ・ラサ方式で学習するアルゴリズムである。
最近では AlphaGo が囲碁の世界チャンピオンを破った初めてのプログラムとなった。
AlphaGo の木探索は， 深層ニューラルネットワークを用いて局面の評価と手の選択を行う。
このニューラルネットワークは，人間の熟練した手からの教師付き学習と， 自分自身の競技からの強化学習によって訓練されている。
ここでは， 人間のデータやガイダンス， ゲームルール以外の領域の知識を必要としない， 強化学習のみに基づいたアルゴリズムを導入する。
AlphaGo は自分自身の教師となり AlphaGo 自身の手の選択や AlphaGo のゲームの勝敗を予測するようにニューラルネットワークが学習される。
このニューラルネットワークは， 木探索の強度を向上させ， その結果， より質の高い手の選択が可能となり， 次の反復ではより強力な自己対戦が可能となる。
タブララサからスタートした私たちの新しいプログラム AlphaGo Zero は，既発表のチャンピオンに敗れた AlphaGo に対して 100-0 で勝利するという超人的な成績を達成した。
</div>
</center>

* [David Silver homepage](https://www.davidsilver.uk/)



<!-- <center>
<img src="http://www.newscientist.com/wp-content/uploads/2003/03/dn3488-1_602.jpg" width="49%"><br/>
</center> -->

# Agent57

<!-- # Conclusions and the future-->
Agent57 では，Atari ゲーム 57 ベンチマークの全ゲームで人間以上の性能を持つ，より一般的な知的エージェントの構築に成功した。
Agent57 は，以前のエージェント Never Give Up の上に構築され，エージェントがいつ探索し、いつ利用するか，また，どの時間地平で学習するのが有用かを知るのに役立つ適応的メタコントローラを実体化したものである。
幅広いゲーム課題では，当然これらのトレードオフの選択を変える必要があるため，メタコントローラはこのような選択を動的に適応させる方法を提供している。

Agent57 は，学習時間が長いほど得点が高くなり，計算量の増加に対応することができた。
これにより，Agent57 は強力な一般的成績を達成することができたが，多くの計算と時間がかかりるので，データ効率は確実に向上させることができる。
さらに，Agetn 57 は，Atari 57ゲームのセットでより良い 5 パーセンタイルの成績を示した。
これは，データ効率だけでなく，一般性能の点でも，決して Atari の研究の終わりを意味するものではない。
このことについて，2 つの見解を示す。

1. パーセンタイル間の成績を分析することで，Agent57 アルゴリズムがいかに一般的であるかについて新しい洞察を得ることができる。
Agent57 は 全 57 ゲームの最初のパーセンタイルで強力な結果を達成し，MuZero で示されるように NGU や R2D2 よりも良い平均値と中央値を保持しているが，それでもより高い平均性能を得ることができる。
2. 現在のすべてのアルゴリズムは，いくつかのゲームにおいて最適な性能を達成するには程遠いということである。
そのため，Agent57 が探索，計画，信用割当てに使用する表現を強化することが，使用する上で重要な改善点となるかもしれない。

<!-- With Agent57, we have succeeded in building a more generally intelligent agent that has above-human performance on all tasks in the Atari57 benchmark.
It builds on our previous agent Never Give Up, and instantiates an adaptive meta-controller that helps the agent to know when to explore and when to exploit, as well as what time-horizon it would be useful to learn with.
A wide range of tasks will naturally require different choices of both of these trade-offs, therefore the meta-controller provides a way to dynamically adapt such choices.

Agent57 was able to scale with increasing amounts of computation: the longer it trained, the higher its score got.
While this enabled Agent57 to achieve strong general performance, it takes a lot of computation and time; the data efficiency can certainly be improved.
Additionally, this agent shows better 5th percentile performance on the set of Atari57 games.
This by no means marks the end of Atari research, not only in terms of data efficiency, but also in terms of general performance.
We offer two views on this: firstly, analyzing the performance among percentiles gives us new insights on how general algorithms are.
While Agent57 achieves strong results on the first percentiles of the 57 games and holds better mean and median performance than NGU or R2D2, as illustrated by MuZero, it could still obtain a higher average performance.
Secondly, all current algorithms are far from achieving optimal performance in some games.
To that end, key improvements to use might be enhancements in the representations that Agent57 uses for exploration, planning, and credit assignment. -->


### DQN からの改善
* 二重 DQN
* 優先度付き経験再生
* 決闘 (dueling)
* 分散化

#### 短期記憶
* LSTM, GRU $\rightarrow$ R2D2

#### エピソード記憶
* メモリーネットワーク
* ニューラルエピソディック制御
* トランスフォーマー

#### 探索
* 好奇心
* 内発的動機づけ

#### メタ制御


### エージェント 57 の先祖

2012 年 DeepMind は Atari57 ゲーム群に取り組むために Deep Q network エージェント（DQN）を開発した。
以来，研究コミュニティは DQN の多くの拡張機能や代替機能を開発してきた。
しかし，これらの進歩にもかかわらず，すべての深層強化学習エージェントは 4 つのゲーム で一貫してスコアを出すことができなかった。
4 つのゲーム: モンテズマの復讐，ピットフォール，ソラリス，スキー

モンテズマの復讐 と ピットフォール は，良好な成績を得るために広範な探索が必要となる。
学習における中心的なジレンマは，探索と利用の問題である。
例えば，地元のレストランでいつも同じお気に入りの料理を注文すべきか，それとも，昔からのお気に入りを上回るかもしれない何か新しいものを試すべきなのか，である。
探索活動には，最終的により強力な行動を発見するために必要な情報を収集するために行われる。
このとき，多くの最適でない行動を取ることが含まれる。

ソラリス と スキー では長期的な信用割り当ての問題がある。 ソラリスとスキーでは，エージェントの行動の結果とそれが受け取る報酬を一致させることが困難である。
エージェントは学習に必要なフィードバックを得るために，長い時間スケールで情報を収集しなければならない。

<center>

[エイリアン](https://youtu.be/luZm3jmwGwI?list=PLqYmG7hTraZCHS3JLle_kxwNvImpYVq4z) :<br/>

<iframe width="600" height="320" src="https://www.youtube.com/embed/luZm3jmwGwI?list=PLqYmG7hTraZCHS3JLle_kxwNvImpYVq4z" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

<!--
<center>
* ソラリス:<br/> <video width="38%" repeat controls><source src="https://youtu.be/QDb3rmEBTZI"></video>
* スキー:<br/> <video width="38%" repeat controls><source src="https://youtu.be/Lppco8heTxI"></video>
* モンテズマの復讐: <video width="38%" repeat controls><source src="https://youtu.be/M9Yn1kYZb6E"></video>
* ピットフォール: <video width="38%" repeat controls><source src="https://youtu.be/LRRq3BXh0xk"></video>
</center>
-->

<center>

<img src="/assets/2020-1029agent57_1.svg" style="width:49%">
<!--- <img
src="https://kstatic.googleusercontent.com/files/f6b5f285173d4449285a8e812b8385f45c03f7104e1c41370a73e0c8558ff82d6a69e60962dd91c4972c444fd73bc4f98a06b5487eff5a037a37bc42f97cef3b" -->
</center>


### DQN の改善
<!-- # DQN improvements-->

DQN の初期の改良では，二重 DQN，経験の優先再生，決闘アーキテクチャなど，学習効率と安定性が向上した。
これらの変更により，エージェントは経験をより効率的かつ効果的に利用できるようになった。

<!--Early improvements to DQN enhanced its learning efficiency and stability, including double DQN, prioritised experience replay and dueling architecture. These changes allowed agents to make more efficient and effective use of their experience.-->

### 分散エージェント
<!-- ## Distributed agents-->

* 複数のコンピュータ上で同時に実行できる分散型の DQN, Gorila, Ape-X を導入
* エージェントはより迅速に経験を獲得し，経験から学ぶことが可能となった。
* アイデアを迅速に反復することができるようになった。
* Agent57 もまたデータ収集と学習処理と切り離した分散型強化学習エージェント
* 多くのアクターが環境の独立したコピーと相互作用し，優先順位付けされた経験再生バッファの形で中央の「メモリバンク」にデータを供給する。
<!--図 4 に示すように，-->
学習者はこの経験再生バッファから訓練データをサンプリングし，
<!--学習者は，-->これらの経験再生を使って損失関数を構築し，行動やイベントのコストを推定する。
* 損失を最小化することでニューラルネットワークのパラメータを更新する。
* <!--最後に，--> 各アクターは学習者と同じネットワーク・アーキテクチャを共有する。
<!--だが，重み係数の独自のコピーを持ちます。-->
* 学習者の重み係数はアクターに頻繁に送られ，後述するように，アクターは個々の優先順位によって決定された方法で自分の重みを更新する

<!-- Next, researchers introduced distributed variants of DQN, Gorila DQN and ApeX,  that could be run on many computers simultaneously. This allowed agents to acquire and learn from experience more quickly, enabling researchers to rapidly iterate on ideas. Agent57 is also a distributed RL agent that decouples the data collection and the learning processes. Many actors interact with independent copies of the environment, feeding data to a central ‘memory bank’ in the form of a prioritized replay buffer. A learner then samples training data from this replay buffer, as shown in Figure 4, similar to how a person might recall memories to better learn from them.  The learner uses these replayed experiences to construct loss functions, by which it estimates the cost of actions or events. Then, it updates the parameters of its neural network by minimizing losses. Finally, each actor shares the same network architecture as the learner, but with its own copy of the weights. The learner weights are sent to the actors frequently, allowing them to update their own weights in a manner determined by their individual priorities, as we’ll discuss later.  -->

<center>

* [ソラリス](https://youtu.be/QDb3rmEBTZI)<br/>
<iframe width="560" height="320" src="https://www.youtube.com/embed/QDb3rmEBTZI?list=PLqYmG7hTraZBuNkJn6YFhi7TYrAg_NDAr" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

<center>
<img src="/assets/2020-1029agent57_2.svg" style="width:66%"><br/>
図4: Agent57 の分散設定
</center>


#### 短期記憶<!-- ## Short-term memory-->

エージェントは，過去の観察を考慮に入れて意思決定を行うために，記憶を持つ必要がある。
これにより，エージェントは，現在の観察 (通常は部分的な観察，つまり，エージェントは自分の世界の一部しか見ていない)だけでなく，環境全体についてのより多くの情報を明らかにすることができる過去の観察に基づいて意思決定を行うことができるようになる。
例えば，ある建物内の椅子の数を数えるために，エージェントが部屋から部屋へと移動するタスクを考えてみよ。
記憶を持っていなければ，エージェントはある部屋の観察にしか頼ることができない。
記憶を持っていれば，エージェントは前の部屋の椅子の数を記憶し，現在の部屋で観察している椅子の数を足すだけでタスクを解くことができる。
したがって，記憶の役割は，過去の観察から得られた情報を集約して意思決定プロセスを改善することである。
深層強化学習では，短期記憶として LSTM（Long-Short Term Memory）などのリカレントニューラルネットワークが用いられる。
<!-- Agents need to have memory in order to take into account previous observations into their decision making. This allows the agent to not only base its decisions on the present observation (which is usually partial, that is, an agent only sees some of its world), but also on past observations, which can reveal more information about the environment as a whole. Imagine, for example, a task where an agent goes from room to room in order to count the number of chairs in a building. Without memory, the agent can only rely on the observation of one room. With memory, the agent can remember the number of chairs in previous rooms and simply add the number of chairs it observes in the present room to solve the task. Therefore the role of memory is to aggregate information from past observations to improve the decision making process. In deep RL and deep learning, recurrent neural networks such as Long-Short Term Memory (LSTM) are used as short term memories. -->

記憶と行動とのインターフェースは，自己学習するシステムを構築する上で極めて重要である。
強化学習では，エージェントは，その直接的な行動の価値のみを学習することができるオンポリシー学習者になることができる。
あるいは，それらの行動を実行していなくても最適な行動について学習することができるオフポリシー学習者になることができる。
--- 例えば，ランダムな行動を取っているかもしれないが，可能な限り最高の行動が何であるかを学習することができる。
したがって，オフポリシー学習はエージェントにとって望ましい特性であり，エージェントが自分の環境を徹底的に探索しながら，取るべき最善の行動のコースを学ぶのを助けることができる。
オフポリシー学習と記憶を組み合わせるのは難しいが，異なる行動を実行するときに何を覚えているかを知る必要があるからである。
例えば，リンゴを探しているときに覚えていること（例えば，リンゴがどこにあるか）は，オレンジを探しているときに覚えていることとは異なる。
しかし，オレンジを探していたとしても，将来的にリンゴを探す必要が出てきた場合に備えて，偶然リンゴに出くわしたとしても，リンゴを探す方法を覚えることができる。
メモリとオフポリシー学習を組み合わせた最初の 深層強化学習エージェント は，ディープリカレント Q-Network(DRQN) であった。
さらに最近になって，短期記憶のニューラルネットワークモデルとオフポリシー学習と分散学習を組み合わせた Recurrent Replay Distributed DQN (R2D2)
で Agent57 の系譜に大きな飛躍が発生し，Atari57 では非常に強い平均性能を達成した。
R2D2 は，過去の経験からの学習のための経験再生の仕組みを短期記憶に働きかけるように修正している。
以上のことから，R2D2 は収益性の高い行動を効率的に学習し，報酬のためにそれを利用することができた。
<!--Interfacing memory with behaviour is crucial for building systems that self-learn. In reinforcement learning, an agent can be an on-policy learner, which can only learn the value of its direct actions, or an off-policy learner, which can learn about optimal actions even when not performing those actions – e.g., it might be taking random actions, but can still learn what the best possible action would be.  Off-policy learning is therefore a desirable property for agents, helping them learn the best course of action to take while thoroughly exploring their environment. Combining off-policy learning with memory is challenging because you need to know what you might remember when executing a different behaviour. For example, what you might choose to remember when looking for an apple (e.g., where the apple is located), is different to what you might choose to remember if looking for an orange. But if you were looking for an orange, you could still learn how to find the apple if you came across the apple by chance, in case you need to find it in the future. The first deep RL agent combining memory and off-policy learning was Deep Recurrent Q-Network (DRQN). More recently, a significant speciation in the lineage of Agent57 occurred with Recurrent Replay Distributed DQN (R2D2), combining a neural network model of short-term memory with off-policy learning and distributed training, and achieving a very strong average performance on Atari57.  R2D2 modifies the replay mechanism for learning from past experiences to work with short term memory. All together, this helped R2D2 efficiently learn profitable behaviours, and exploit them for reward. -->


#### エピソード記憶<!-- ## Episodic memory-->

ネバーギブアップ (NGU) は，R2D2 にエピソード記憶という別の形の記憶を補強するように設計された。
NGU  はゲームの新しい部分に遭遇したときにそれを検知し，エージェントが報酬を得るためにその新しい部分を探索することができるようになった。
このため，エージェントの行動 (探索) は，エージェントが学習しようとしている方針 (ゲームで高得点を得ること) から大きく逸脱することになり，ここでも方針逸脱学習が重要な役割を果たす。
NGU は，Atari 57 ベンチマークの導入以来，どのエージェントも得点できなかった Pitfall や，その他の難しい Atari ゲームにおいて，領域知識なしで正の報酬を得た最初のエージェントであった。
残念ながら，NGU は歴史的に「簡単な」ゲームでは性能を犠牲にしたため，平均して R2D2 より性能が劣っている。
<!-- We designed Never Give Up (NGU) to augment R2D2 with another form of memory: episodic memory.
This enables NGU to detect when new parts of a game are encountered, so the agent can explore these newer parts of the game in case they yield rewards.
This makes the agent’s behaviour (exploration) deviate significantly from the policy the agent is trying to learn (obtaining a high score in the game); thus, off-policy learning again plays a critical role here.
NGU was the first agent to obtain positive rewards, without domain knowledge, on Pitfall, a game on which no agent had scored any points since the introduction of the Atari57 benchmark, and other challenging Atari games.
Unfortunately, NGU sacrifices performance on what have historically been the “easier” games and so, on average, underperforms relative to R2D2.
我々は R2D2 を別の記憶形態であるエピソード記憶で補強するために Never Give Up (NGU) を設計した。
これにより NGU はゲームの新しい部分に遭遇したときにそれを検出することができ，それが報酬をもたらす場合には，エージェントはゲームのこれらの新しい部分を探索することができるようになる。
これにより，エージェントの行動（探索）は，エージェントが学習しようとしている方針（ゲームで高得点を得ること）から大きく逸脱してしまいます。
NGU は Atari57 ベンチマークが導入されて以来，誰もポイントを獲得していないゲームである Pitfall や，他の難解な Atari ゲーム で， ドメイン知識なしで，ポジティブな報酬を獲得した最初のエージェントであった。
残念なことに NGU は歴史的に「より簡単な」ゲームでの成績を犠牲にしている。
このため，平均的には R2D2 と比較して低い成績となった。-->


## 直接的な探索を促すための内発的動機づけの方法<!-- # Intrinsic motivation methods to encourage directed exploration-->

最も成功した戦略を発見するためには，エージェントは環境を探索しなければならないが，探索戦略の中には他の戦略よりも効率的なものもある。
DQN では，$\epsilon$ 貪欲(グリーディ) として知られる無方向探索戦略を用いて探索問題を解決しようとした。
イプシロングリーディとは一定の確率（イプシロン）でランダムな行動をとり，そうでなければ現在の最良の行動を選ぶことである。
報酬がない場合，大きな状態行動空間を探索するのに膨大な時間を必要とする。
この限界を克服するために，多くの有向探索戦略が提案されてきた。
これらの中で，ある分野では，新規性を求める行動に対してより密な「内部」報酬を提供することで，エージェントが可能な限り多くの状態を探索し，訪問することを促す内発的動機報酬の開発に焦点を当ててきた。
その中で，我々は 2 つのタイプの報酬を区別した。
第一のタイプの報酬は，長期的な新規性報酬は，訓練期間中，多くのエピソードに渡って多くの状態を訪問することを促す。
第二のタイプの報酬は，短期的な新規性報酬は，短期間（例えば，ゲームの 1エピソード内）に多くの状態を訪問することを促すものである。
<!--In order to discover the most successful strategies, agents must explore their environment–but some exploration strategies are more efficient than others.
With DQN, researchers attempted to address the exploration problem by using an undirected exploration strategy known as epsilon-greedy: with a fixed probability (epsilon), take a random action, otherwise pick the current best action.
However, this family of techniques do not scale well to hard exploration problems: in the absence of rewards, they require a prohibitive amount of time to explore large state-action spaces, as they rely on undirected random action choices to discover unseen states.
In order to overcome this limitation, many directed exploration strategies have been proposed.
Among these, one strand has focused on developing intrinsic motivation rewards that encourage an agent to explore and visit as many states as possible by providing more dense “internal” rewards for novelty-seeking behaviours.
Within that strand, we distinguish two types of rewards: firstly, long-term novelty rewards encourage visiting many states throughout training, across many episodes. Secondly, short-term novelty rewards encourage visiting many states over a short span of time (e.g., within a single episode of a game). -->


### 長時間軸での新規性<!-- ## Seeking novelty over long time scales-->

長期的な新規性報酬は，以前に見たことのない状態がエージェントの生涯で遭遇したときのキッカケであり，訓練中にこれまでに見た状態密度の関数となる。
ある状況に接する頻度が高い場合 (その状態がよく知られていることを示す)，長期的な新規性報酬は低い。その逆もまた然り。
すべての状態が見慣れた状態であれば，エージェントは無方向の探索戦略に頼ることになる。
しかし，高次元空間の密度モデルの学習は，**次元の呪い** のために問題が多い。
実際には，エージェントが深層学習モデルを用いて密度モデルを学習する場合，壊滅的忘却（新しい経験に遭遇すると以前に見た情報を忘れる）や，すべての入力に対して正確な出力を生成することができないことに悩まされる。
例えば，モンテズマの復讐では，指向性のない探索戦略とは異なり，長期的な新規性報酬により，エージェントは人間のベースラインを超えることができる。
しかし，モンテズマの復讐で最高のパフォーマンスを発揮する方法であっても，密度モデルを適切な速度で注意深く訓練する必要がある。
密度モデルが最初の部屋の状態が馴染みのあるものであることを示すとき，エージェントは一貫して馴染みのない領域に到達することができるはずである。
<!-- Long-term novelty rewards signal when a previously unseen state is encountered in the agent’s lifetime, and is a function of the density of states seen so far in training: that is, it’s adjusted by how often the agent has seen a state similar to the current one relative to states seen overall.
When the density is high (indicating that the state is familiar), the long term novelty reward is low, and vice versa.
When all the states are familiar, the agent resorts to an undirected exploration strategy. However, learning density models of high dimensional spaces is fraught with problems due to the curse of dimensionality.
In practice, when agents use deep learning models to learn a density model, they suffer from catastrophic forgetting (forgetting information seen previously as they encounter new experiences), as well as an inability to produce precise outputs for all inputs.
For example, in Montezuma’s Revenge, unlike undirected exploration strategies, long-term novelty rewards allow the agent to surpass the human baseline.
However, even the best performing methods on Montezuma’s Revenge need to carefully train a density model at the right speed: when the density model indicates that the states in the first room are familiar, the agent should be able to consistently get to unfamiliar territory. -->

<center>

[モンテズマの復讐](https://www.youtube.com/watch?v=M9Yn1kYZb6E&list=PLqYmG7hTraZB5YFgejiwDoKBkg50SlY6z):<br/>
<iframe width="600" height="352" src="https://www.youtube.com/embed/M9Yn1kYZb6E?list=PLqYmG7hTraZB5YFgejiwDoKBkg50SlY6z" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>


### 短期間での新規性<!-- ## Seeking novelty over short time scales-->

短期的な新規性報酬は，エージェントが最近の過去に遭遇しなかった状態を探索することを促すために使用することができる。
近年，エピソード記憶のいくつかの特性を模倣したニューラルネットワークが強化学習エージェントの学習を高速化するために使用されている。
エピソード記憶もまた，新しい経験を認識するために重要であると考えられている。
このため，我々はこれらのモデルを適応させ，Never Give Up に短期的な新規性の概念を与えるようにした。
エピソード記憶モデルは（モデルのパラメータを学習したり，適応させたりする必要がなく）その場で適応させることができるノンパラメトリックな密度モデルを素早く学習することができる。
このため，短期的な新規性報酬を計算するための効率的で信頼性の高い候補である。
この場合，報酬の大きさは，エピソード記憶に記録された現在の状態と以前の状態との間の距離を測定することによって決定される。
<!-- Short-term novelty rewards can be used to encourage an agent to explore states that have not been encountered in its recent past.
Recently, neural networks that mimic some properties of episodic memory have been used to speed up learning in reinforcement learning agents.
Because episodic memories are also thought to be important for recognising novel experiences, we adapted these models to give Never Give Up a notion of short-term novelty.
Episodic memory models are efficient and reliable candidates for computing short-term novelty rewards, as they can quickly learn a non-parametric density model that can be adapted on the fly (without needing to learn or adapt parameters of the model).
In this case, the magnitude of the reward is determined by measuring the distance between the present state and previous states recorded in episodic memory.-->

すべての距離の概念が意味のある探索を促進するわけではない。
例えば，多くの歩行者や車両がいる混雑した街をナビゲートする課題を考えると，
あるエージェントが，視覚的なあらゆる微小な変化を考慮に入れた距離の概念を使用するようにプログラムされているとすれば，そのエージェントは，受動的に環境を観察するだけで，静止していることさえも含めて多くの異なる状態を訪れることになる。
このようなシナリオを避けるためには，エージェントが探索にとって重要だと考えられる特徴（たとえば，制御性）を学習し，その特徴についてだけ考慮した距離を計算する必要がある。
このようなモデルはこれまでも探索に用いられてきた。
だが，このエピソード記憶との組み合わせは ネバーギブアップ探索手法の主な進歩の一つであり，これにより Pitfall の性能が人間を凌駕した。
<!-- However, not all notions of distance encourage meaningful forms of exploration.
For example, consider the task of navigating a busy city with many pedestrians and vehicles.
If an agent is programmed to use a notion of distance wherein every tiny visual variation is taken into account, that agent would visit a large number of different states simply by passively observing the environment, even standing still – a fruitless form of exploration.
To avoid this scenario, the agent should instead learn features that are seen as important for exploration, such as controllability, and compute a distance with respect to those features only. Such models have previously been used for exploration, and combining them with episodic memory is one of the main advancements of the Never Give Up exploration method, which resulted in above-human performance in Pitfall!. -->

<center>

[NGU による Pitfall!](https://youtu.be/imAeLt1BPu4?list=PLqYmG7hTraZBgXcetCL9zzd6Cck8S4l4k)<br/>
<iframe width="548" height="323" src="https://www.youtube.com/embed/imAeLt1BPu4?list=PLqYmG7hTraZBgXcetCL9zzd6Cck8S4l4k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

Never Give Up (NGU) は 制御可能な状態に基づく短期的新規性報酬と ランダムネットワーク蒸留を用いた長期的新規性報酬と混合して使用した。
この混合は 長期的新規性が制限されている場合，両方の報酬を掛け合わせることで実現された。
このようにして，短期的な目新しさの報酬の効果は維持される。
だが エージェントが生涯にわたってゲームに慣れてくると，その効果は減衰される可能性がある。
NGU のもう一つの革新的アイデアとしては，NGU は方策族を学習することである。
方策族には，純粋に 利用的 (exploitative) なものから, 高度に探索的 (exploratary) なものまで含まれる。
R2D2 の上に構築することで，アクターは総新規性報酬の重要度の重み付けに基づいて，異なるポリシーでの経験を生成する。
この経験は，方策族内の各重み付けに関して一様に生成される。
<!-- Never Give Up (NGU) used this short-term novelty reward based on controllable states, mixed with a long term novelty reward, using Random Network Distillation.
The mix was achieved by multiplying both rewards, where the long term novelty is bounded.
This way the short-term novelty reward’s effect is preserved, but can be down-modulated as the agent becomes more familiar with the game over its lifetime.
The other core idea of NGU is that it learns a family of policies that range from purely exploitative to highly exploratory. This is achieved by leveraging a distributed setup: by building on top of R2D2, actors produce experience with different policies based on different importance weighting on the total novelty reward. This experience is produced uniformly with respect to each weighting in the family. -->


<center>
<img src="/assets/2017Pathak_fig2.svg" width="77%"><br/>
<div style="text-align: justify;width:88%;background-color:cornsilk">
図 2. 状態 $s_{t}$ のエージェントは，現在の方針 $\pi$ からサンプリングされた行動 $a_{t}$ を実行することで環境と相互作用し，最終的に状態 $s_{t+1}$ になる。
方針 $\pi$ は，環境 $E$ が提供する外発的報酬 ($r^{e}_{t}$) と，我々が提案する内発的好奇心モジュール (ICM) が生成する好奇心に基づく内発的報酬信号 ($r^{i}_{t}$) の和を最適化するように学習されます。
ICM は，状態 $s_{t}$, $s_{t+1}$ を，$a_{t}$ を予測するために学習された特徴量 $\phi(s_{t})$, $\phi(s_{t+1})$ に符号化します (すなわち，逆動力学モデル)。
順方向モデルは，$\phi(s_{t})$ と $a_{t}$ を入力とし $s_{t+1}$ の特徴表現 $\widehat{\phi}(s_{t+1})$ を予測します。
特徴空間での予測誤差は，好奇心に基づく内在的報酬信号として用いられる。
エージェントの行動に影響を与えない，あるいは影響を受けない環境特徴を符号化するインセンティブが $\phi(s_{t})$ にはないため，我々のエージェントの学習された探索戦略は，環境の制御不可能な側面に対してロバストである。

<!-- Figure 2.
The agent in state st interacts with the environment by executing an action $a_{t}$ sampled from its current policy $\pi$ and ends up in the state $s_{t+1}$.
The policy $\pi$ is trained to optimize the sum of the extrinsic reward ($r^{e}_{t}$) provided by the environment $E$ and the curiosity based intrinsic reward signal ($r^{i}_{t}$) generated by our proposed Intrinsic Curiosity Module (ICM).
ICM encodes the states $s_{t}$, $s_{t+1}$ into the features $\phi(s_{t})$, $\phi(s_{t+1})$ that are trained to predict $a_{t}$ (i.e. inverse dynamics model).
The forward model takes as inputs $\phi(s_{t})$ and $a_{t}$ and predicts the feature representation $\widehat{\phi}(s_{t+1})$ of $s_{t+1}$.
The prediction error in the feature space is used as the curiosity based intrinsic reward signal.
As there is no incentive for $\phi(s_{t})$ to encode any environmental features that can not influence or are not influenced by the agent’s actions, the learned exploration strategy of our agent is robust to uncontrollable aspects of the environment.-->
</div>
</center>


<center>
<img src="/assets/2019Jaegle_fig1.jpg" width="77%"><br/>
<div style="text-align: justify;width:88%;background-color:cornsilk">
好奇心は，稀にしか	報酬の得られない環境下での探索を動機づける。
<!-- Novelty can drive exploration in environments with sparse external rewards. -->
上イラストは探索の模式図である。サルは，果物 (報酬) を大きく生茂った枝振りの良い木から探そうとしている。
<!-- An illustration of the benefits of exploration:  -->
報酬にありつくまでに，数多くの枝，すなわち，多くの「状態」を探索せねばならない。
<!-- a monkey is trying to find a piece of fruit (a reward) in a large, densely foliated tree with many branches.  -->
一つ報酬を見つけ出した場合には，他の報酬はすべて捨て去ることをも含意している。
<!-- Typically, the monkey must make many choices and explore many ‘states’ before it receives a single reward.
If the monkey finds novel states rewarding, then it will be encouraged to explore the tree, and it can discover rewarding states that it would otherwise miss. -->
視点の普遍性:
<!-- View invariance: -->
同一状態の異なる見え(リンゴ)は，異なる画像に対応する。
<!-- different views of the same state (e.g. the apple) can correspond to different images.  -->
強化学習が成就するためには，入力画像を対応する状態への関連付けなければならない。
<!-- To effectively drive RL, a system must map images onto their corresponding states. -->
状態普遍性:
<!-- State invariance:  -->
状態が異なれば，新奇性も異なる。果物は通常，高い報酬となり，木々の葉は通常小さく，重なり合って細かな影をなす。
<!-- different states can share features that are indicative of their novelty, for example, reflecting the fact that fruits are usually large and are rarely green while leaves are often small and can take on many shades of green.
A system that can exploit the features shared by different states can drive the monkey to explore states with novel features (e.g. objects with a new size or shade).
-->
source: Jaegle2019+ Fig. 1
</div>
</center>

### メタコントローラ：探索と利用のバランス

Agent57 は 次のような観察に基づいて構築されている。
もしエージェントが，いつ利用 (exploit) するのが良いのか，いつ 探索 (explore) するのが良いのかを学習できるとしたらどうであろうか？
我々は，探索と利用のトレードオフを適応させるメタコントローラの概念と，より長い時間的な信用割当てを必要とするゲームのために調整可能な時間地平線を導入した。
この変更により Agent57 は簡単なゲームでも難しいゲームでも人間レベル以上の成績を得ることができるようになった。
<!-- # Meta-controller: learning to balance exploration with exploitation
Agent57 is built on the following observation: what if an agent can learn when it’s better to exploit, and when it’s better to explore? We introduced the notion of a meta-controller that adapts the exploration-exploitation trade-off, as well as a time horizon that can be adjusted for games requiring longer temporal credit assignment. With this change, Agent57 is able to get the best of both worlds: above human-level performance on both easy games and hard games.-->

具体的には，内在的動機付け方法には 2 つの欠点がある。<!-- Specifically, intrinsic motivation methods have two shortcomings:-->
<!-- * Exploration: Many games are amenable to policies that are purely exploitative, particularly after a game has been fully explored. This implies that much of the experience produced by exploratory policies in Never Give Up will eventually become wasteful after the agent explores all relevant states.
* Time horizon: Some tasks will require long time horizons (e.g. Skiing, Solaris), where valuing rewards that will be earned in the far future might be important for eventually learning a good exploitative policy, or even to learn a good policy at all. At the same time, other tasks may be slow and unstable to learn if future rewards are overly weighted. This trade-off is commonly controlled by the discount factor in reinforcement learning, where a higher discount factor enables learning from longer time horizons. -->

* **探索** 多くのゲームは，特にゲームが完全に探索 explore された後に 純粋に 利用可能 exploit な方針に従順である。
これは NGU での 探索的 (explore) 方策によって生成された経験の多くは，エージェントが関連するすべての状態を探索した後に，最終的に無駄になることを意味している。
* **時間の地平線** Skiing や Solaris のように 遠い将来に得られる報酬を評価することは，最終的に良い 利用可能 (搾取的 exploitive) な政策を学ぶために，あるいは良い政策を全く学ぶために重要かもしれない。
同時に，将来の報酬が過度に重み付けされている場合，他の課題は学習に時間がかかり，不安定になる可能性がある。
このトレードオフは，一般的に強化学習では割引率によって制御され，割引率が高いほど長い時間軸からの学習が可能になる。

このことから，可変長の時間水平線と新規性の重要性を考慮して，異なる方策で生成される経験の量を制御するオンライン適応メカニズムを使用した。
研究者たちは，異なるハイパーパラメータを持つエージェントの集団を訓練する，勾配降下法によってハイパーパラメータの値を直接学習する，ハイパーパラメータの値を学習するために中央集権型バンディットを使用するなど，複数の方法でこれに取り組むことを試みてきた。

我々はバンディットアルゴリズムを使用して，経験を生成するためにエージェントが使用すべき方策を選択した。
具体的には，各アクターに対してスライドウィンドウ型 UCB バンディットを訓練し，そのポリシーが持つべき探索への選好度と時間軸を選択した。

<!-- This motivated the use of an online adaptation mechanism that controls the amount of experience produced with different policies, with a variable-length time horizon and importance attributed to novelty. Researchers have tried tackling this with multiple methods, including training a population of agents with different hyperparameter values, directly learning the values of the hyperparameters by gradient descent, or using a centralized bandit to learn the value of hyperparameters.

We used a bandit algorithm to select which policy our agent should use to generate experience. Specifically, we trained a sliding-window UCB bandit for each actor to select the degree of preference for exploration and time horizon its policy should have. -->

<center>

[NGU によるスキー](https://youtu.be/0_67wNXyOcI?list=PLqYmG7hTraZDp9fZRWVMeGwUupEl7uN8S)<br/>
<iframe width="560" height="323" src="https://www.youtube.com/embed/0_67wNXyOcI?list=PLqYmG7hTraZDp9fZRWVMeGwUupEl7uN8S" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>


### Agent57: すべてをまとめる

Agetn57 を達成するために，我々は以前に開発した探索エージェント Never Give Up をメタコントローラと組み合わせた。
このエージェントは 方策族を探索して学習するために，長期的，および短期的な，内在的動機を混合したものを計算する。
メタコントローラは，エージェントの各アクターが，新しい状態を探索するか，すでに知られていることを利用するかの違いと同様に，短期と長期とのパフォーマンスの間で異なるトレードオフを選択することを可能にする (図4)。
強化学習はフィードバックループを形成する。
選択された行為が訓練データを決定し，メタコントローラはまたエージェントがどのようなデータから学習するかを決定する。

<!-- # Agent57: putting it all together
To achieve Agent57, we combined our previous exploration agent, Never Give Up, with a meta-controller. This agent computes a mixture of long and short term intrinsic motivation to explore and learn a family of policies, where the choice of policy is selected by the meta-controller. The meta-controller allows each actor of the agent to choose a different trade-off between near vs. long term performance, as well as exploring new states vs. exploiting what’s already known (Figure 4). Reinforcement learning is a feedback loop: the actions chosen determine the training data. Therefore, the meta-controller also determines what data the agent learns from. -->

<center>
<img src="/assets/2020deepmind_agent57_fig4.svg" style="width:66%"><br/>
<!-- <img src="https://kstatic.googleusercontent.com/files/a9754efe518fdef7e39f50baeffd0f8348f21d0fd3c919f6ca749799321a9b514134f3a2a6f19d33b9fcf254ccf05847f91da511567e44ffc375a6ccb75b069c"> -->
</center>

<!--
## 結論と今後の展開
Agent57 では Atari57 ベンチマークのすべての課題において人間以上の性能を持つ，より一般的な知的エージェントを構築することに成功した。
このエージェントは，以前のエージェント Never Give Up を ベースに構築されており， 適応的なメタコントローラを実体化している。
広範囲の課題は当然，これらのトレードオフの両方の異なる選択を必要とする。そのためメタコントローラはそのような選択を動的に適応させる方法を提供している。

Agent57 は計算量の増加に伴ってスケーリングすることができた。
これにより Agent57 は強力な一般性能を達成することが可能となった。
多くの計算量と時間を必要とするが，データ効率は確実に改善することができる。
さらに，この Agent57は Atari の 57 ゲームセット全てで 5 パーセンタイル のより良い性能を示した。
これは，データ効率の面だけでなく，一般的な性能の面でも，決して Atari の研究の終わりを意味するものではない。

* 第一に，パーセンタイル間の性能を分析することで，一般的なアルゴリズムがどのようなものであるかについて新たな洞察を得ることができる。
* 第一に，パーセンタイル間の性能を分析することで，一般的な アルゴリズムがどのようなものであるかを知ることができる。
* 第二に，現在のアルゴリズムはすべて，いくつかのゲームで最適なパフォーマンスを達成するには程遠いということです。

そのためには Agent57 が探索，計画，および信用割り当てのために使用する表現を強化することが，使用するための重要な改善点になるかもしれない。 -->





### NIC (Neural Caption Generation)

<center>
<img src="/assets//17VISIOn-slide-WBE2-jumbo.jpg" width="49%"><br/>
- 人間: A group of men playing Frisbee in the park.
- 機械: A group of young people playing a game of Frisbee.
</center>

<img src="/assets/2014Vinyals_Fig5_left.jpg" width="44%">
<img src="/assets/2014Vinyals_Fig5_right.jpg" width="44%"><br/>
Vinyals et. al (2014) より

# Transformer, [Attention is all you need](https://arxiv.org/abs/1706.03762)

単語の多義性解消のために，あるいは単語のベクトル表現を超えて，より大きな意味単位である，句，節，文のベクトル表現を得る努力がなされてきた。
適切な普遍文表現ベクトルを得ることができれば，翻訳を含む多くの下流課題にとって有効だと考えられる。

そこで，注意機構を積極的に取り込んだゲームチェンジャーが Transformer である。


* 注意を用いて，RNN を置き換える [Devlin+2017,Attention Is All You Need](https://arxiv.org/abs/1706.03762)
* Transformer の注意とは，このソフトマックス関数である。
* 専門用語としては，**多頭=自己注意** Multi-Head Self-Attention (以下 MHSA と表記)と呼ぶ。
* **自己** がつく注意である理由は，トップダウン信号がないためであろう。
* 上図，クエリ，キー，バリュー ，意味としては，問い合わせ，キー（鍵），値，であるが，とりわけ，Q と K との間に明確な相違はない。
* ある問い合わせ Q に対して，キー K を与えて，その答え A となる値を得ることに相当する。
* この操作を入力情報から作り出して答えを出力する仕組みに，ワンホット表現を使う。

<!-- 下図左は上図右と同じものです。この下図右を複数個束ねると下図中央になります。 -->

- 図中央の Scaled Dot-Product Attention と書かれた右脇に小さく h と書かれている。この h とは ヘッド の意味。
- 図中央を 1 つの単位として，次に来る情報と連結させる。図右。
- リカレントニューラルネットワークでは，中間層の状態が次の時刻の処理に継続して用いられていた。
- ところが 多頭=自己注意 MHSA では一つ前の入力情報を，現在の時刻の情報に対するクエリとキーのように扱って情報を処理する。
- 図右の下から入力される情報は，input と output と書かれている。
さらに output の下には (Shifted right) と書かれています。
すなわち，時系列情報を一時刻分だけ右にずらし（シフト）させて逐次情報を処理することを意味している。
- 図右の下から入力される情報は，embedding つまり埋め込み表現 と 位置符号化 position embedding が足し合わされたもの。
埋め込み表現とは先週 word2vec で触れたベクトルで表現された，単語（あるいはそれぞれの項目）の 意味表現 に対応。

<div class="pagebreak"></div>

#### Transformer の概略図

<div class="figcenter">
<img src="/2023assets/2017Vaswani_Fig2_1ja.svg" width="15%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="/2023assets/2017Vaswani_Fig2_2ja.svg" width="25%">&nbsp;&nbsp;&nbsp;
<img src="/assets/2017Vaswani_Fig1.svg" width="25%">
<div class="figcaption">

Transformer [2017Vaswani++](https://arxiv.org/abs/1706.03762) Fig.2 を改変。
`matmul` は行列の積，`scale` は，平均 0 分散 1 への標準化，`mask` は 0 と 1 とで，データを制限すること，`softmax` はソフトマックス関数
</div></div>
Transformer における注意 = ソフトマックス関数。<br/>

<div class="pagebreak"></div>

### Transformer における位置符号化器 (PE: position encoders)

$$
\text{PE}_{(\text{pos},2i)} = \sin\left(\frac{\text{pos}}{10000^{\frac{2i}{d_{\mathop{model}}}}}\right)
$$

$$
\mathop{PE}_{(\mathop{pos},2i+1)} = \cos\left(\frac{\mathop{pos}}{10000^{\frac{2i}{d_{\mathop{model}}}}}\right)
$$

<div class="figcenter">
<img src="/2024assets/2023_0723PE_Transformer_curves.png" width="77%">
<div class="figcaption" style="width:55%">

Transformer の位置符号化器の出力。
Transformer は位置情報を持たないので，位置情報を周波数変換して用いる。
</div></div>

<div class="pagebreak"></div>

### 事前訓練

#### マスク化言語モデル

<div class="figcenter">
<img src="/2024assets/2019Lample_Fig1.svg" width="55%">
</div>

#### 次文予測課題

言語モデルの欠点を補完する目的，次の文を予測

[SEP] トークンで区切られた 2 文入力

- 入力: the man went to the store [SEP] he bought a gallon of milk.
- ラベル:  IsNext
- 入力:  the man went to the store [SEP] penguins are flightless birds.
- ラベル:  NotNext

#### ファインチューニング GLUE 課題 (General Language Understanding Evaluation)

- **CoLA**: 入力文が英語として正しいか否かを判定
- **SST-2**: スタンフォード大による映画レビューの極性判断
- **MRPC**: マイクロソフトの言い換えコーパス。2 文 が等しいか否かを判定
- **STS-B**: ニュースの見出し文の類似度を5段階で評定
- **QQP**: 2 つの質問文の意味が等価かを判定
- **MNLI**: 2 入力文が意味的に含意，矛盾，中立を判定
- **QNLI**: 2 入力文が意味的に含意，矛盾，中立を判定
- **RTE**: MNLI に似た2つの入力文の含意を判定
- **WNI**: ウィノグラッド会話チャレンジ

### ファインチューニング手続きによる性能比較

マスク化言語モデルのマスク化割合は マスクトークン:ランダム置換:オリジナル=80:10:10 だけでなく，他の割合で訓練した場合の 2 種類下流課題，
MNLI と NER で変化するかを下図 に示した。
80:10:10 の性能が最も高いが大きな違いがあるわけではないようである。

<div class="figcenter">
<img src="/assets/2019Devlin_mask_method21.jpg" width="49%"><br/>
</div>
<div class="figcaption">
マスク化言語モデルのマスク化割合の違いによる性能比較
</div>

<div class="pagebreak"></div>

#### モデルサイズ比較

<div class="figcenter">
<img src="/assets/2019Devlin_model_size20.jpg" width="59%"><br/>
</div>
<div class="figcaption">
モデルのパラメータ数による性能比較
</div>

パラメータ数を増加させて大きなモデルにすれば精度向上が期待できる。
下図では，横軸にパラメータ数で MNLI は青と MRPC は赤 で描かれている。
パラメータ数増加に伴い精度向上が認められる。
図に描かれた範囲では精度が天井に達している訳ではない。
パラメータ数が増加すれば精度は向上していると認められる。

#### モデル単方向，双方向モデル比較

<div class="figcenter">
<img src="/assets/2019Devlin_directionality19.jpg" width="59%"><br/>
</div>
<div class="figcaption">
言語モデルの相違による性能比較
</div>

<!-- 言語モデルをマスク化言語モデルか次単語予測の従来型の言語モデルによるかの相違による性能比較を下図に示した。
横軸には訓練ステップである。訓練が進むことでマスク化言語モデルとの差は 2 パーセントではあるが認められるようである。 -->

## Transformer (SBERT) の文ベクトル

先に紹介した word2vec は，単語ベクトルを得る手法であるが，Transformer は文ベクトルを扱う。
そこで，文単位での類似性を検討した。
下の画像に対して，5 つの脚注がある。

<center>
<img src="/assets/coco175469.jpg" width="55%"><br/>
</center>

1. 夕暮れのハーバーに汽船と複数の鳥が浮かんでいる
2. 水面に浮かぶ4羽の水鳥と、その向こうに停泊している2隻の船
3. 船着き場に2艘の船がとまっている
4. 朝焼けの中待機場所にある旅客船とマガモ
5. 停められた船の近くで水鳥が泳いでいる<br/>
MS COCO データセットより: <http://farm5.staticflickr.com/4055/4704393899_a041476b4a_z.jpg>

上図は，MS COCO 画像データと画像に対応する脚注からなるデータセットからの一例である。
日本語文は，千葉工業大学 STAIRLABO が公開しているデータである。
人間が見れば，写真と文章とは結びいていることが分かる。
加えて，5 つの脚注も相互に似ていることが分かる。
MS COCO データセットでは，一枚の写真に 5 つの脚注が紐付けられている。

コンピュータにこれらの文章が似ていることを判断させようとすると，最近まで難しい仕事であった。
本章で紹介する，文の意味ベクトルを用いると，これらの文章が相互に似ていると判断させることが可能である。
下図は tSNE を用いて，日本語の文章の類似度を sentence BERT を用いて表現し，文章の類似度に従って地図を描いたものである。
図では，同じ写真に紐付いている文章は同じ色で表現している。

<center>
<img src="/2024assets/2022_0915sbert_staircoco500.svg" style="width:77%">
</center>

<div class="pagebreak"></div>

<!--# マルチタスク学習，転移学習

- 学習したことがらを応用することは賢さの尺度であろう。

たとえば，映画[カラテキッド](https://youtu.be/DsLk6hVBE6Y)(1984)では，ミヤギ先生はダニエルさんに車のワックスがけや床掃除を教えました :-) ワックスがけや床磨きは空手の技術習得にとって必要な技能であったというオチです。

## 実習ファイル

- [マルチタスク学習2 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2020_0703four_in_one_network2.ipynb){target="_blank"}
- [マルチタスク学習3 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2020_0703four_in_one_network3.ipynb){target="_blank"}

    1. 画像脚注付け<br>
    ![](https://twitter.com/paraschopra/status/1096710728092995584/photo/1){target="_blank"}
    2. 類義語<br>
    ![](https://cdn-images-1.medium.com/max/1280/1*tWrGWKXwWMbuocw2nXBysA.png){target="_blank"}
    3. 類義画像<br>
    ![](https://cdn-images-1.medium.com/max/1280/1*NZSJiMUMQi9u07oA6vI9cA.png){target="_blank"}
    4. 文章からの画像検索
        - __犬__を検索<br>
    ![犬](https://cdn-images-1.medium.com/max/1280/1*VmIgBrrr-3XwGGwoXwiQMg.png){target="_blank"}<br>
        - __笑顔の少年__ を検索<br>
    ![笑顔の少年](https://cdn-images-1.medium.com/max/1280/1*4Km1YpfFbwhRF8Obu54EaA.png){target="_blank"}<br>

---

- [マーガレット ミッチェルによるソーシャルメディアを用いたメンタルヘルスのマルチタスク学習](http://m-mitchell.com/publications/multitask-blurb.html){target="_blank"}
    - [arXiv 論文](https://arxiv.org/abs/1712.03538){target="_blank"}
- [One neural network, many uses](https://towardsdatascience.com/one-neural-network-many-uses-image-captioning-image-search-similar-image-and-words-in-one-model-1e22080ce73d){target="_blank"}
    - [ソースコード](https://github.com/paraschopra/one-network-many-uses){target="_blank"}
    - [An Overview of Multi-Task Learning in Deep Neural Networks](http://ruder.io/multi-task/){target="_blank"}
    - [上の arXiv](https://arxiv.org/abs/1706.05098){target="_blank"}

---

### Hard parameter sharing

<center>
<img src="http://ruder.io/content/images/2017/05/mtl_images-001-2.png" style="width:44%">
<img src="http://ruder.io/content/images/size/w2000/2019/03/transfer_learning_taxonomy-1.png" style="width:44%"><br>
左:マルチタスク学習, 右:転移学習, いずれも Sebastuan Ruder のブログより<br>
</center>

---

### Soft parameter sharing

In soft parameter sharing on the other hand, each task has its own model with its own parameters.
The distance between the parameters of the model is then regularized in order to encourage the parameters to be similar. [8]
for instance use the $l2$ norm for regularization, while [9] use the trace norm.

- [8]: Duong, L., Cohn, T., Bird, S., & Cook, P. (2015). Low Resource Dependency Parsing: Cross-lingual Parameter Sharing in a Neural Network Parser. Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Short Papers), 845–850.
- [9]: Yang, Y., & Hospedales, T. M. (2017). Trace Norm Regularised Deep Multi-Task Learning. In Workshop track - ICLR 2017. Retrieved from http://arxiv.org/abs/1606.04038

![](http://ruder.io/content/images/size/w2000/2017/05/mtl_images-002-2.png)

---

# Recent work on MTL for Deep Learning

### Deep Relationship Networks
![](http://ruder.io/content/images/2017/05/relationship_networks.png)
__A Deep Relationship Network with shared convolutional and task-specific fully connected layers with matrix priors (Long and Wang, 2015).__

- Long, M., & Wang, J. (2015). Learning Multiple Tasks with Deep Relationship Networks. arXiv Preprint arXiv:1506.02117. Retrieved from http://arxiv.org/abs/1506.02117 ↩︎

---

### Fully-Adaptive Feature Sharing
![](http://ruder.io/content/images/2017/05/fully_adaptive_feature_sharing.png)<br>
__The widening procedure for fully-adaptive feature sharing (Lu et al., 2016).__

Lu, Y., Kumar, A., Zhai, S., Cheng, Y., Javidi, T., & Feris, R. (2016). Fully-adaptive Feature Sharing in Multi-Task Networks with Applications in Person Attribute Classification. Retrieved from http://arxiv.org/abs/1611.05377

---

### Cross-stitch Networks
![](http://ruder.io/content/images/2017/05/cross-stitch_networks.png)<br>
__Cross-stitch networks for two tasks (Misra et al., 2016).__

Misra, I., Shrivastava, A., Gupta, A., & Hebert, M. (2016). Cross-stitch Networks for Multi-task Learning. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. https://doi.org/10.1109/CVPR.2016.433


<!--
### Low supervision

Søgaard, A., & Goldberg, Y. (2016). Deep multi-task learning with low level tasks supervised at lower layers. Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics, 231–235.

---

## A Joint Many-Task Model
![](http://ruder.io/content/images/2017/05/joint_many_task_model.png)<br>
__A Joint Many-Task Model (Hashimoto et al., 2016).__

---

### Weighting losses with uncertainty
![](http://ruder.io/content/images/2017/05/weighting_using_uncertainty.png)<br>
__Uncertainty-based loss function weighting for multi-task learning (Kendall et al., 2017).__

Kendall, A., Gal, Y., & Cipolla, R. (2017). Multi-Task Learning Using Uncertainty to Weigh Losses for Scene Geometry and Semantics. Retrieved from http://arxiv.org/abs/1705.07115

---

### Sluice Networks
![](http://ruder.io/content/images/2017/05/sluice_network-003.png)<br>
__A sluice network for two tasks (Ruder et al., 2017).__

Ruder, S., Bingel, J., Augenstein, I., & Søgaard, A. (2017). Sluice networks: Learning what to share between loosely related tasks. Retrieved from http://arxiv.org/abs/1705.08142
-->

