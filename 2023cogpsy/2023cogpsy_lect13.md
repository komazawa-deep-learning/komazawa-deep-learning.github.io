---
title: "第13回 2023年度開講 駒澤大学 認知心理学研究"
author: "浅川 伸一"
layout: home
---

<div align="right">
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 22/Dec/2023<br/>
Appache 2.0 license<br/>
</div>

$$
\newcommand{\of}[1]{\left(#1\right)}
\newcommand{\Of}[1]{\left[#1\right]}
\newcommand{\KL}[2]{\operatorname{KL}\left(\left.{#1}\right\|{#2}\right)}
\newcommand{\given}[1]{\left|{#1}\right.}
$$

<link href="/assets/css/asamarkdown.css" rel="stylesheet">

* [DaSiC ワークショップ 12月23日開催](https://sites.google.com/view/dasic7-2023/workshop){:target="_blank"}

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

* [系列探索と逆行流: 視覚野における双方向情報フローの計算モデル](2021Ullman_bu_td_ja.pdf)
* [ボトムアップ・トップダウンの反復処理による画像解釈](1995Ullman_bidirectional_cortex_ja.pdf)
