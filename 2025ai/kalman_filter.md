---
title: カルマンフィルタ詳説
author: 浅川伸一
layout: home
---

## カルマンフィルタのアルゴリズム

**初期化**

1.  フィルタの状態を初期化する。
2.  状態に関する信念を初期化する。

**予測**

1.  プロセスモデルを使って次のタイムステップにおける状態を予測する。
2.  予測の不確実性に応じて信念を調整する。

**更新**

1.  観測値とその正確さに関する信念を取得する。
2.  予測値と観測値の残差を計算する。
3.  予測値の正確さと観測値の正確さからスケーリング係数を計算する。
4.  計算されたスケーリング係数を使って予測値と観測値の間の値に状態を設定する。
5.  予測値の正確さと観測値の正確さに基づいて状態に関する信念を更新する。


<div class="figcenter">
<img src="/2025assets/residual_chart_with_h_jp.png" width="77%;">
</div>

**予測**


1. 状態の期待値の更新 $\bar \mu = \mu + \mu_{f_{x}}$, $\bar{\mathbf x} = \mathbf{Fx} + \mathbf{Bu}$ |
1. 状態の分散の更新 $\bar\sigma^2 = \sigma_x^2 + \sigma_{f_{x}}^2$, $\bar{\mathbf P} = \mathbf{FPF}^\mathsf T + \mathbf Q$|

- $\mathbf x,\\, \mathbf P$ は状態を表す多変量ガウス分布の平均と共分散行列であり、それぞれ $x$ と $\sigma^2$ に対応する。
- $\mathbf F$ は **状態遷移関数** (state transition function) である。$\mathbf x$ に $\mathbf{F}$ を乗じると事前分布が計算される。
- $\mathbf Q$ はプロセスモデルに加わるノイズの共分散行列 (**プロセスノイズ行列** process noise matrix) を表す。$\sigma^2_{f_x}$ に対応する。
- $\mathbf B$ と $\mathbf u$ は系に対する制御入力をモデル化する。

**更新**

1. $y = z - \bar x$, $\mathbf y = \mathbf z - \mathbf{H\bar x}$ 
1. $\displaystyle K = \frac{\bar P}{\bar P+R}$, $\mathbf K = \mathbf{\bar{P}H}^\mathsf T (\mathbf{H\bar{P}H}^\mathsf T + \mathbf R)^{-1}$
1. $\displaystyle \mu=\frac{\bar\sigma^2 \mu_z + \sigma_z^2 \bar\mu} {\bar\sigma^2 + \sigma_z^2}$, $\mathbf x = \bar{\mathbf x} + \mathbf{Ky}$ 
1. $\displaystyle \sigma^2 = \frac{\sigma_1^2\sigma_2^2}{\sigma_1^2+\sigma_2^2}$, $\mathbf P = (\mathbf I - \mathbf{KH})\mathbf{\bar{P}}$ 

記号の説明を示す:

- $\mathbf H$ は **観測関数** (measurement function) である。本書で初めて登場する概念であり、状態変数を観測変数に変換するために用いられる。
- $\mathbf z$ は観測された状態、$\mathbf R$ は観測された状態に含まれる誤差の共分散行列 (**観測ノイズ行列** measurement noise matrix) である。
- $\mathbf y$ と $\mathbf K$ はそれぞれ残差とカルマンゲインである。

## カルマンフィルタの式

### 予測ステップ

カルマンフィルタは **事前分布**  次の時刻における予測された系の状態を計算するために次式を使う。この式は事前分布の平均 $\mathbf{\bar x}$ と共分散行列 $\mathbf{\bar P}$ を計算する:

$$ \begin{aligned} \mathbf{\bar x} &= \mathbf{Fx} +
\mathbf{Bu}\\ \mathbf{\bar P} &= \mathbf{FPF}^\mathsf T +
\mathbf Q \end{aligned} $$

#### 平均: $\mathbf{\bar x} = \mathbf{Fx} + \mathbf{Bu}$

思い出しておくと、線形方程式 $\mathbf{Ax} = \mathbf b$ は方程式の集合を表す。$\mathbf A$ には方程式の係数が含まれ、$\mathbf x$ は変数のベクトルである。$\mathbf{Ax}$ の乗算を行うと、方程式の右辺にある $\mathbf b$ が計算される。 

$\mathbf F$ が考えているタイムステップにおける状態の遷移を表すから、状態 $\mathbf x$ との積 $\mathbf{Fx}$ は遷移後の状態を計算する。簡単だ！ 同様に $\mathbf B$ は制御関数で $\mathbf u$ が制御入力だから、$\mathbf{Bu}$ は遷移後の状態に対する制御の寄与を計算する。よって、事前分布 $\mathbf{\bar x}$ は $\mathbf{Fx}$ と $\mathbf{Bu}$ の和として計算される。

単変量カルマンフィルタでは次の式がこの式に対応する:

$$ \bar\mu = \mu + \mu_{move} $$

<!-- $\mathbf{Fx}$ の行列積を実際に計算すれば、$x$ に対する遷移を計算するこの式が得られる。

この式を具体的に計算してみよう。前に $\mathbf F$ は
$\mathbf F = \begin{bmatrix}1&\Delta t \\ 0&1\end{bmatrix}$ だと説明した。よって $\mathbf{\bar x} = \mathbf{Fx}$ は次の二つの線形方程式に対応する:

$$ \begin{cases} \begin{aligned} 
\bar x &= 1x + &\Delta t\, \dot
x \\ \bar{\dot x} &=0x + &1\, \dot x 
\end{aligned} \end{cases}$$ -->

#### 分散: $\mathbf{\bar P} = \mathbf{FPF}^\mathsf T + \mathbf Q$

この等式は手強いので、少し時間をかけて説明する。

単変量カルマンフィルタでは次の式を使った:

$$ \bar\sigma^2 = \sigma^2 + \sigma^2_{move} $$

移動の分散を推定値の分散に加えることで予測による知識の散逸を表している。ここでも同じことを行うのだが、多変量ガウス分布では少し難しくなる。

単純に $\mathbf{\bar P} = \mathbf P + \mathbf Q$ と書くことはできない。なぜなら、多変量カルマンフィルタでは状態変数に**相関**があるからだ。これは何を意味するだろうか？ 例えば私たちが持つ速度に関する知識は不完全だが、予測値は速度を位置に加えることで計算される:

$$ \bar x = \dot x\Delta t + x $$

速度 $\dot x$ の値について完璧な知識を持っていないので、和 $\bar x = \dot x \Delta t + x$ の計算だけでも不確実性は大きくなる。つまり位置と速度に相関があるために、共分散行列を足すだけでは正しい共分散行列は得られない。例えば $\mathbf P$ と $\mathbf Q$ が両方とも対角行列のとき和も対角行列となるが、位置と速度は相関するのだから、次のタイムステップにおける共分散行列は非ゼロの非対角要素を持たなければならない。 

正しい式を示す:

$$ \mathbf{\bar P} = \mathbf{FPF}^\mathsf T + \mathbf Q $$

$\mathbf{ABA}^\mathsf T$ という形をした式は線形代数でよく登場する。これは内側の項を外側の項で**射影**していると考えることができる。
<!-- この形の式は本書でもこれから何度も登場するものの、最初はこれが "魔法の" 式に思えても不思議でない。詳しく説明しよう。 -->
これがカルマンフィルタが **魔法** と呼ばれる所以である。

$\mathbf P$ は次の値で初期化した:

$$ \mathbf P = \begin{bmatrix}\sigma^2_x & 0 \\ 0 &
\sigma^2_v\end{bmatrix} $$

このとき $\mathbf{FPF}^\mathsf T$ を計算するとこうなる:

$$ \begin{aligned} \mathbf{FPF}^\mathsf T &=
\begin{bmatrix}1&\Delta t\\0&1\end{bmatrix}
\begin{bmatrix}\sigma^2_x & 0 \\ 0 & \sigma^2_{v}\end{bmatrix}
\begin{bmatrix}1&0\\\Delta t&1\end{bmatrix} \\ &=
\begin{bmatrix}\sigma^2_x&\sigma_v^2\Delta t\\ 0 &
\sigma^2_{v}\end{bmatrix} \begin{bmatrix}1&0\\\Delta
t&1\end{bmatrix} \\ &= \begin{bmatrix}\sigma^2_x +
\sigma_v^2\Delta t^2 & \sigma_v^2\Delta t \\
\sigma_v^2\Delta t & \sigma^2_{v}\end{bmatrix} \end{aligned}$$

$\mathbf P$ の初期値では位置と速度の共分散が $0$ だった。しかし新しい位置は $\dot x\Delta t + x$ と計算されるので、新しい位置と速度には相関がある。そして $\mathbf{FPF}^\mathsf{T}$ という乗算が $\sigma_v^2 \Delta t$ という位置と速度の共分散を計算する。この正確な値は重要でない: $\mathbf{FPF}^\mathsf T$ がプロセスモデルを使って自動的に位置と速度の共分散を計算することを理解するだけで十分だ！

乗算 $\mathbf{Fx}$ について考察しても説明ができる。この乗算によって $\mathbf{F}$ で射影された $\mathbf{x}$ は次の時刻の値となる。$\mathbf{FP}$ が同じ操作だと思うかもしれないが、$\mathbf x$ はベクトルなのに対して $\mathbf P$ は行列である。$\mathbf P$ を $\mathbf F$ の列と行の両方で乗じるには最後の $\mathbf F^\mathsf T$ が必要になる。実際 $\mathbf{FPF}^\mathsf T$ の計算の二行目に注目すると、$\mathbf{FP}$ が上三角行列であり $\mathbf{F}$ が完全には積に取り込まれてはいないことが分かる。

線形代数と統計学の経験があるなら、次の説明も理解に役立つだろう。予測された状態の共分散行列は予測ステップにおける誤差の期待値とモデル化できる。この値は次の等式で計算できる:

$$ \begin{aligned} 
\bar{\mathbf P} &= \mathbb E\left[(\mathbf{Fx} - \bar{\mu})(\mathbf{Fx} - \bar{\mu})^\mathsf T\right]\\ 
&= \mathbf F\, \mathbb E\left[(\mathbf{x}- {\mu})(\mathbf{x} - {\mu})^\mathsf T\right]\, \mathbf F^\mathsf T 
\end{aligned} $$

もちろん $\mathbb E\left[(\mathbf{x} - {\mu})(\mathbf{x}- {\mu})^\mathsf T\right]$ は $\mathbf{P}$ に等しいから、次を得る:

$$ \bar{\mathbf P} = \mathbf{FPF}^\mathsf T $$


### 更新ステップ

更新ステップの式は予測ステップの式よりずっと複雑に見えるものの、複雑に見える理由の大部分はカルマンフィルタが更新を観測空間で計算するためである。観測空間で計算しなければならないのは、観測値が**不可逆**なためだ。例えば対象との距離を報告するセンサがあったとしたら、観測された距離を位置に変換することはできない──特定の円上の任意の点が同じ距離を報告する。一方で、位置
(状態) があれば距離 (観測値) を必ず計算できる。

観測値と予測値の間にある何らかの値を推定値として選択する処理である。これを次の図に示す:

![推定値の選択](/2025assets/residual_chart_with_h_jp.png)

状態が多次元なので式は複雑になるが、何をしているかといえばこの図が全てである。複雑な式を見てこのアイデアの単純さを忘れてはいけない。

#### 系不確実性:$\textbf{S} = \mathbf{H\bar PH}^\mathsf T + \mathbf R$

観測空間で計算を行うために、カルマンフィルタは共分散行列を観測空間に射影する必要がある。このための式が $\mathbf{H\bar PH}^\mathsf T$ である。ここで $\mathbf{\bar P}$ は **事前分布の** 共分散行列、$\mathbf H$ は観測関数を表す。

この式が $\mathbf{ABA}^\mathsf T$ の形をしているのが分かるはずだ──予測ステップには状態遷移関数 $\mathbf{F}$ を使った $\mathbf{FPF}^\mathsf T$ があった。ここでは観測関数 $\mathbf{H}$ を使った同じ形の式で更新を行っている。線形代数によって座標系が変換される。

共分散行列を観測空間に移すのに加えて、センサノイズも考えに入れる必要がある。これは非常に簡単で、センサに加わるノイズの共分散行列 $\mathbf{R}$ を足すだけだ。こうして計算される $\mathbf{S}$ は **系不確実性** (system uncertainty) あるいは **発展共分散行列** (innovation covariance matrix) と呼ばれる。

$\mathbf{S}$ を計算する式の $\mathbf H$ を無視すると、単変量カルマンフィルタにおけるカルマンゲインの式の分母と同じような式になる:

$$ K = \frac {\bar\sigma^2} {\bar\sigma^2 + \sigma_z^2} $$

系不確実性の式と事前分布の共分散行列の式を比較してみよう:

$$ \begin{aligned} \mathbf{S} &= \mathbf{H\bar PH}^\mathsf T +
\mathbf R\\ \mathbf{\bar P} &= \mathbf{FPF}^\mathsf T + \mathbf
Q \end{aligned} $$

両方の式で状態の共分散行列 ($\mathbf{P}$ または $\bar{\mathbf{P}}$) が $\mathbf H$ または $\mathbf F$ によって異なる空間に移され、その空間に関連付いたノイズ行列が足されている。

#### カルマンゲイン: $\mathbf K = \mathbf{\bar PH}^\mathsf T \mathbf{S}^{-1}$

残差と推定値を示した図をもう一度見てほしい。予測値と観測値が求まったら、後はその二つの間の値を選択する必要がある。観測値の確実性が高いなら観測値に近い値を選択し、逆に予測値の確実性が高いなら予測値に近い値を選択するべきである。

単変量カルマンフィルタでは次の式を使ってスケーリングを行った:

$$ \mu =\frac{\bar\sigma^2 \mu_z + \sigma_\mathtt{z}^2
\bar{\mu}} {\bar\sigma^2 + \sigma_\mathtt{z}^2} $$

私たちはこの式を次の形に単純化した:
$$ \mu = (1-K)\bar{\mu} + K\mu_\mathtt{z} $$
ここで
$$ K = \frac {\bar\sigma^2} {\bar\sigma^2 + \sigma_z^2} $$
と定義され、$K$ は **カルマンゲイン** と呼ばれる $0$ から $1$ の実数である。カルマンゲインが予測値と観測値の間にある重み付き平均を選択しているという事実の理解を確認してほしい。カルマンゲインは **パーセンテージ** (**比**) である──もし $K$ が $0.9$ なら、観測値の 90% と予測値の 10% を取って $\mu$ が計算される。

多変量カルマンフィルタでは $\mathbf K$ はスカラーではなくベクトルとなる。式をもう一度示そう: $\mathbf K = \mathbf{\bar PH}^\mathsf T \mathbf{S}^{-1}$ である。これは**比**なのか？ 逆行列は線形代数における逆数と考えることができる──行列による除算は定義されないが、この考え方は式の意味を理解する上で都合がいい。こう考えると、$\textbf{K}$ の式は次のように読める: 

$$ \begin{aligned} 
\mathbf K &\approx \frac{\mathbf{\bar P}\mathbf H^\mathsf T}{\mathbf{S}} \\ 
\mathbf K &\approx \frac{\text{不確実性}_\text{予測値}}{\text{不確実性}_\text{予測値} + \text{不確実性}_\text{観測値}}\mathbf H^\mathsf T 
\end{aligned}$$

カルマンゲインの式は予測値と観測値をどれだけ信用するかに応じて比を計算する。同じことはこれまでの全ての章で行ってきた。行列を使って多次元の状態を考えているので式は複雑だが、考え方は難しくない。$\mathbf H^\mathsf T$ の部分は理解しにくいので、後でまた説明する。この部分を無視すれば、カルマンゲインの式は単変量の場合と同じである: 
事前分布の不確実性を事前分布の不確実性と観測値の不確実性の和で割っているだけだ。

#### 残差: $\mathbf y = \mathbf z - \mathbf{H\bar{x}}$

この式は観測関数 $\mathbf H$ を設計するときに触れたので、簡単に説明できる。観測関数は状態を観測値に変換することを思い出そう。そのため $\mathbf{Hx}$ は $\mathbf{x}$ を等価な観測値に変換する。こうして計算した値を観測値 $\mathbf{z}$ から引けば、残差──観測値と予測値の差──が得られる。

単変量の場合の式は
$$ y = z - \bar x $$
であり、明らかに同じ計算を (一次元で) 行っている。

#### 状態の更新: $\mathbf x = \mathbf{\bar x} + \mathbf{Ky}$

残差をカルマンゲインでスケールすることで、残差の直線上にある推定値 (新しい状態) が計算される。残差をスケールしているのは $\mathbf{Ky}$ であり、これは残差のスケールと状態空間への変換を同時に行う。$\mathbf{K}$ に含まれる $\mathbf{H}^\mathsf T$ は状態空間への変換のために存在する。後は残差を事前分布に足せば $\mathbf x =\mathbf{\bar x} + \mathbf{Ky}$ が得られる。$\mathbf{K}$ を展開して全体の計算を確認してみよう: 

$$ \begin{aligned} \mathbf x &= \mathbf{\bar x} + \mathbf{Ky}
\\ &= \mathbf{\bar x} + \mathbf{\bar PH}^\mathsf T
\mathbf{S}^{-1}\mathbf y \\ &\approx \mathbf{\bar x} +
\frac{\text{不確実性}_\text{予測値}}{\text{不確実性}_{\text{予測値}}
+ \text{不確実性}_\text{観測値}}\mathbf H^\mathsf T\mathbf y
\end{aligned} $$

この推定値の式を次のように書き直すと、カルマンゲインが比であるという事実が分かりやすくなるだろう:

$$ \begin{aligned} \mathbf x &= \mathbf{\bar x} + \mathbf{Ky}
\\ &= \mathbf{\bar x} +\mathbf K(\mathbf z - \mathbf{H\bar x})
\\ &= (\mathbf I - \mathbf{KH})\mathbf{\bar x} + \mathbf{Kz}
\end{aligned} $$

単変量の場合の式との類似性は明らかなはずだ:
$$ \mu = (1-K)\bar{\mu} + K\mu_\mathtt{z} $$

#### 共分散行列の更新: $\mathbf P = (\mathbf{I}-\mathbf{KH})\mathbf{\bar P}$

$\mathbf{I}$ は単位行列であり、多次元における $1$ を表す。$\mathbf{H}$ は観測関数を表す定数である。この式は $\mathbf P = (1-c\mathbf K)\mathbf P$ と考えることができる。$\mathbf{K}$ は予測値と観測値をどれくらいずつ使うかを表す比であり、もし $\mathbf{K}$ が大きいなら $1 - \mathbf{cK}$ は小さくなり、新しい $\mathbf{P}$ はこれまでより小さくなる。もし $\mathbf{K}$ が小さいなら $1-\mathbf{cK}$ は大きくなり、$\mathbf P$ は比較的大きくなる。これは不確実性の大きさをカルマンゲインの定数倍で調整していることを意味する。

この式は数値的に不安定である。
減算によって対称性が崩れる可能性がある上に、何度も繰り返すと浮動小数点数の誤差が溜まってしまう。
そのためコード上では異なる方法が用いられる。

