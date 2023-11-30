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

# 最適化の工夫


# 復習 確率的学習 SGD

誤差関数 $\mathbf{J}\left(w\right)$ を**ランダムサンプリング** random sampling して置き換える.

$$
w_{t+1}=w_t-\alpha_t\nabla_wJ\left(w\right)
$$

$$
w_{t+1}=w_t-\alpha_t\mathbb{E}\left[\nabla_wJ\left(w\right)\right]
$$

* ここで $\alpha$ は学習係数
* $\mathbb{E}$ は**期待値**をとる演算

$$
\mathbb{E}\left[\nabla_wJ\left(w\right)\right]=\frac{1}{N}\sum_{i=1}^{N}\nabla_wJ\left(w\right)
$$

- $N=\mbox{データサイズ}$ のとき**バッチ学習**
- $N=1$ のとき**オンライン学習**
- $1< N<\mbox{データサイズ}$ のとき**ミニバッチ学習**

## 勾配降下法

$$
w_{t+1} = w_{t} - \alpha_t\nabla_w J(w)
$$


## モーメント

$$
\begin{align}
v_t &= v_{t-1}+ \nabla_w J(w)\\
\Delta w_{t+1} &= m w_{t} - \eta v_t
\end{align}
$$

$$
\Delta w_{t+1} = m\Delta w_{t} - \alpha\nabla J\left(w_t\right)
$$

# ニュートン法

ちなみに wikipeida のニュートン法では [https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization](https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization)

$$
\mathbf{x}_{n+1}=\mathbf{x}_n-\gamma\left[\mathbf{H}f\left(\mathbf{x}_n\right)\right]^{-1}\nabla f\left(\mathbf{x}_n\right).
$$

表記をニューラルネットワーク風に書き換えると

$$
\mathbf{w}_{t+1}=\mathbf{w}_t-\frac{\alpha}{\left[\mathbf{H}\left(\mathbf{w}_t\right)\right]}\nabla J\left(\mathbf{w}_t\right).
$$

$$ \Delta\mathbf{w}_{t+1}=-\frac{\alpha}{\mathbf{H}\left(\mathbf{w}_t\right)}\nabla J\left(\mathbf{w}_t\right). $$

- 学習係数を固定したパラメータであると捉えるのではなく，その都度，ヘシアン行列を用いて調整する

# Adagrad

出典: 2011Duchi_ADAGRAD

$$
\Delta w_{t+1,i} = - \frac{\alpha}{\sqrt{G_{t,ii}+\epsilon}}\nabla J\left(w_{t,}\right).
$$

- ここで $G_{t,ii}$ は $\Delta w_{t,i}$ を対角成分とする**対角行列** (の自乗), すなわち $H$ の対角近似， かつ Adagrad は**各要素 $i$ について個別に考慮**
- $\epsilon=1e-8$ は分母が $0$ にならないための保険
- ヘシアン行列を対角要素だけで近似する

# Adadelta

出典: 2012Zeiler_ADADELTA

$$\mathbb{E}\left[g^2\right]_t = \gamma\mathbb{E}\left[g^2\right]_{t-1}+\left[1-\gamma\right]\nabla J\left(w_{t,i}\right)$$

- Adagrad が行っていたヘシアン行列の近似を，その都度計算するのではなく，履歴を保持しておいて平均値で近似することで精度向上を意図した手法

$$\Delta w_t = - \frac{\alpha}{\sqrt{\mathbb{E}\left[g^2\right]_t+\epsilon}}\nabla J\left(w_{t,i}\right)$$

ここで $\sqrt{\mathbb{E}\left[g^2\right]_t}$ は平均自乗和の開平 root mean squared :RMS と見なせるので


$$\Delta w_{t,i} = - \frac{\alpha}{\operatorname{RMS}\left[g\right]_t}\nabla J\left(w_{t,i}\right)$$

- 実際，繰り返し回数を $t$ とすると $\frac{1}{t}=\gamma$ とすれば $1-\gamma=\frac{t-1}{t}$ となるので，平均を計算していることになる。

<!--
$$
\Delta w_{t,i}=-\frac{\operatorname{RMS}\BRc{\Delta\theta_t}_{t-1}}{\operatorname{RMS}\BRc{g}_t}\nabla l\of{w_{t,i}}
$$
-->

# RMSprop
出典: 2012RMSprop

$$ \mathbb{E}\left[g^2\right]_t = 0.9\mathbb{E}\left[g^2\right]_{t-1} + 0.1 g^2_t $$

$$ \Delta w_{t,i}=-\frac{\alpha}{\sqrt{\mathbb{E}\left[g^2\right]+\epsilon}}\nabla J\left(w_{t,i}\right) $$

$\gamma=0.9$, $\alpha=0.001$ が使われる。

# Adam

出典: 2015KingmaADAM

$$
\begin{align}
m_t &=\beta_1m_{t-1}+\left[1-\beta_1\right] J\left(w_t\right)\\
v_t &=\beta_2v_{t-1}+\left[1-\beta_2\right]g^2
\end{align}
$$

$$
\Delta w_{t+1}=-\frac{\alpha}{\sqrt{v_t}+\epsilon}m_t.
$$

ここで $\beta_1=0.9999$, $\beta_2=1e-8$

- Adam の名前は適応モーメント推定（adaptive moment estimation）に由来
- Adam は 適応的手法とモーメンタム法の両方の利点を持っています。

# Gif アニメ

<!-- <center>

<img src="assets/BealeFunction.gif" style="39%">
<img src="assets/longValley.gif" style="39%"><br/>
左:ベッセル関数，右:ロングバレー<br/>!
<img src="assets/SaddlePoint.gif" style="39%"><br/>

出典 アレックス ラッドフォード[YouTube <https://www.youtube.com/watch?v=VINCQghQRuM>](https://www.youtube.com/watch?v=VINCQghQRuM)<br/>
<https://imgur.com/a/Hqolp](https://imgur.com/a/Hqolp><br/>
</center>
-->

<center>
<!--<img src="assets/beales_20171117_00-02-20_2d.gif" style="width:47%"><br/>-->
<!--出典: [https://github.com/wassname/viz_torch_optim](https://github.com/wassname/viz_torch_optim)<br/>-->
<img src="/2023assets/opt1.gif" style="width:30%">
<img src="/2023assets/opt2.gif" style="width:30%">
<img src="/2023assets/opt3.gif" style="width:24%"><br/>

出典 [アレックス ラッドフォード
[YouTube](https://www.youtube.com/watch?v=VINCQghQRuM)](https://www.youtube.com/watch?v=VINCQghQRuM), [<https://imgur.com/a/Hqolp>](https://imgur.com/a/Hqolp)<br/>
</center>

<!-- from ml4a の /jp/how_neural_networks_are_trained/ -->
AdaDelta や RMSprop と同様 Adam は過去の勾配のスライディングウィンドウに基づいて学習率をパラメータごとに調整します。
さらに時間に沿って道筋を滑らかにするためのモーメンタムの成分もあります。

他にも多くの手法が存在します。派生形や実用的なヒントを含めたより包括的な議論は Sebastian Ruder の [ブログ記事](http://ruder.io/optimizing-gradient-descent/index.html) を参照してください。

<!--
以下の視覚化は Alec Radford によるものです。
モーメンタム法とネステロフ加速勾配降下法（NAG）は「下り坂を転がる」速度が付きすぎて最適な経路をオーバーシュートする傾向があることに対し、
標準的な SGD は適切な経路を取るものの遅すぎることに注意してください。
適応的手法である AdaGrad, AdaDelta, RMSProp（Adamも含まれる） はパラメータごとの柔軟性があることで、これらの問題を回避する傾向があります。

<center>
<img src="assets/opt2a.gif" style="width:30%">
</center>
-->

# 自然勾配法  Natural gradient method

1998Amari_NG

- ヘシアン行列をフィッシャーの情報行列 $I$ で置き換える

$$ \Delta\mathbf{w}_{t+1}=-\frac{\alpha}{\mathbf{I}\left(\mathbf{w}_t\right)}\nabla J\left(\mathbf{w}_t\right). $$


- フィッシャーの情報量行列は，目標関数の対数尤度の 2 回微分です $\displaystyle \mathbf{I}=\mathbb{E}\left[\log\left(\frac{\partial^2w}{\partial w_i\partial w_j}\right)\right]$


# まとめ

- 最適化手法として，Adagrad, AdaDelta, RMSprop, Adam, 自然勾配法 を紹介しました。
- いずれの手法も，ニュートン法におけるヘシアン行列の近似を考えています。どのようなアイデアで近似を行うのかで手法ごとに特徴があります

