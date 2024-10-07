---
title: "第04回 2024年度開講 駒澤大学 認知心理学研究"
author: "浅川 伸一"
layout: home
---

<div align="right">
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 11/Oct/2024<br/>
Appache 2.0 license<br/>
</div>

$$
\newcommand{\of}[1]{\left(#1\right)}
\newcommand{\Of}[1]{\left[#1\right]}
\newcommand{\KL}[2]{\operatorname{KL}\left(\left.{#1}\right\|{#2}\right)}
\newcommand{\given}[1]{\left|{#1}\right.}
$$

<link href="/assets/css/asamarkdown.css" rel="stylesheet">

<div class="memo">
クリストフ・コロンブスのアメリカ発見について，そもそも彼の偉大な点はどこにあるか，ということをきく人があるならば，それは西回りのルートでインドへ旅行するのに，地球が球形であることを利用するというアイディアではなかった，と答えなければならないだろう。
このアイディアはすでに他の人々によって考えられたものであったし，彼の探検の慎重な準備，船の専門的な装備などということでもなかった。
それらのことは，他の人でもやろうとすればやれたに違いない。
そうではなくて，この発見的航海で最も困難であったことは，既知の陸地を完全に離れ，残余の貯えでは引き返すことがもはや不可能であった地点から，さらに西へ西へと船を走らせるという決心であったに違いない。<br>
<div style="text-align:right">「部分と全体」ハイゼンベルク，山崎和夫訳，みすず書房，p.115，「VI 新世界への出発 1926-1927年」冒頭部</div>
</div>


<div class="figcenter">
<img src="/assets/2019Glaser_fig2.jpg" width="39%">
<img src="/2024assets/2008Kriegeskorte_fig3.jpg" width="39%">
<div class="memo">

左: Glaser+(2019) Fig.2, 右: Kriegeskorte+(2008) Fig.3

機械学習の 4 つ役割
1. 工学問題の解として
2. 予測変数の特定と改善
3. 単純モデルの評価とベンチマーク
4. 脳のモデルとして<br/>


図 3. 異なる表現を関連付けるハブとしての表現非類似性行列<!-- FIGURE 3. The representational dissimilarity matrix as a hub that relates different representations. --><br/>

A: システム神経科学は，3つの主要な研究分野，行動実験，脳活動実験，計算モデリングを関連付けるのに苦労してきた。
これまでは，これらの分野は主に 2 つのレベルで相互に作用してきた。
(1) 言語理論のレベルでの相互作用。すなわち，個別の分析から導き出された結論を比較することによる相互作用。
このレベルは不可欠であるが，定量的ではない。
(2) 特性関数のレベルで相互作用，例えば，心理測定関数と神経測定関数との比較。
この種の分野間の接触は同様に不可欠であり，定量的なものである。
しかし，特性関数は通常，少数のデータ点しか含まないため，そのインタフェースは情報的に豊かではない。
ここで示されている RDM は 4 つの条件のみに基づいているため，($(4^2-4)/2=$) 6 つのパラメータしか得られないことに注意。
しかし，パラメータの数は条件の数の 2 乗に比例して増えるため，RDM は異なる表現を関連付けるための情報豊富なインターフェースを提供できる。
例えば，ここで取り上げている 96 画像の実験では，行列のパラメータ数は $(96^{2}−96)/2=4,560$ となる。
<!-- **A**: Systems neuroscience has struggled to relate its three major branches of research: behavioral experimentation, brain-activity experimentation, and computational modeling.
So far these branches have interacted largely on two levels:
(1) They have interacted on the level of verbal theory, i.e., by comparing conclusions drawn from separate analyses.
This level is essential, but it is not quantitative.
(2) They have interacted at the level characteristic functions, e.g., by comparing psychometric and neurometric functions.
This form of bringing the branches in touch is equally essential and can be quantitative.
However, characteristic functions typically contain only a small number of data points, so the interface is not informationally rich. Note that the RDM shown is based on only four conditions, yielding only (42−4)/2=6 parameters.
However, since the number of parameters grows as the square of the number of conditions, the RDM can provide an informationally rich interface for relating different representations.
Consider for example the 96-image experiment we discuss, where the matrix has (962−96)/2=4,560 parameters. --><br/>

B: RDM が提供する量的インタフェースを介して，どのような異なる表現が関連付けられるかをより詳細に説明している。
ここでは，確立可能なモダリティ内での関係を説明するために，fMRI の例を任意に選択した。
これらの関係は，いずれも確立が困難であることに注意 (灰色の双方向矢印)。
<!-- **B**: This panel illustrates in greater detail what different representations can be related via the quantitative interface provided by the RDM.
We arbitrarily chose the example of fMRI to illustrate the within-modality relationships that can be established.
Note that all these relationships are difficult to establish otherwise (gray double arrows). -->
</div></div>

## 本日のメニュー

1. Git のインストール
2. 機械学習モデルの説明，ロジスティック回帰，k-means, SVM, 判別分析
3. [Python の基礎](python_numpy_intro_ja)
4. [フレームワーク](/eco/)
5. CNN


## [世界モデル](https://worldmodels.github.io/){:target="_blank"}

先週取り上げた変分符号化器モデルの応用として，[世界モデル](https://arxiv.org/abs/1803.10122) を取り上げます。

<div style="text-align: center;">
<img src="/2023assets/2018Ha_Schmithuber_world_model_schematic.svg" style="width:49%">
<div class="figcaption">

エージェントモデルのフロー図。
未加工の観測データは，まず各時間ステップ t で視覚 V によって処理され，潜在変数 z_t が生成される。
コントローラ C への入力はこの潜在ベクトル z_t と各時間ステップでのメモリ M の隠れ状態 h_t が結合されたものである。
コントローラ C は次に，運動制御のための行動ベクトル a_t を出力する。
メモリ M は現在の潜在変数 z_t と行動 a_t を入力として，自身の隠れ状態を更新し，時間 t+1 で使用するh_{t+1} を生成する。
</div></div>


世界モデルの考え方は，比較的単純であり，1) 外界とのインターフェイス，2) 内部モデル，3) コントローラ，から成り立っている。

<div style="text-align: center;">
<img src="/2023assets/world_models_1990.jpeg" style="width:44%;"/>
<img src="/2023assets/world_models_1990_feedback.jpeg" style="width:44%;"/>
<!-- <img src="/2023assets/world_models_1990.jpeg" style="display: block; margin: auto; width: 44%;"/>
<img src="/2023assets/world_models_1990_feedback.jpeg" style="display: block; margin: auto; width: 44%;"/> -->
</div>
<div style="text-align: center;">
世界 RNN モデルを内蔵したコントローラ。

環境と相互作用する RNN ベースのコントローラの図 (Schmithuber1990)
<!-- A controller with internal RNN model of the world.
Ancient drawing (1990) of a RNN-based controller interacting with an environment. [20] -->
</div>

## マルチモーダルインテグレーション，マルチタスク，トップダウン流とボトムアップ流

* [系列探索と逆行流: 視覚野における双方向情報フローの計算モデル](/2023cogpsy/2021Ullman_bu_td_ja.pdf)
* [ボトムアップ・トップダウンの反復処理による画像解釈](/2023cogpsy/1995Ullman_bidirectional_cortex_ja.pdf)
