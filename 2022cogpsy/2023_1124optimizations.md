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
