---
title: 第13回
date: 2021_1217
layout: home
---

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 17/Dec/2021<br/>
Appache 2.0 license<br/>
</div>

# 転移学習とファインチューニング，顔認識実演

## お知らせ

来週 12月24日はオンラインで行います。 https://meet.google.com/oia-vgsd-cpb 


## 実習ファイル

* [オリベッティ顔データセットによる PCA 実習 <img src="https://komazawa-deep-learning.github.io/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_1215pca_decompostion.ipynb)
* [顔，非顔判別データセットを用いた紡錘状回のモデル化 --- 転移学習を用いた顔検出モデル ---  <img src="https://komazawa-deep-learning.github.io/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_0925face_dataset_transfer_learning.ipynb){:target="_blank"}
* [深層学習とPyTorchを使った顔のキーポイント検出](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_1010facial_keypoints_detection.ipynb#scrollTo=4d5561a8-dd37-4620-9eec-da286caf40e2){:target="_blank"}

<!-- * [ヴィオラ=ジョーンズ アルゴリズム(従来手法) による顔認識実験 <img src="https://komazawa-deep-learning.github.io/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_0930viola_jones_ipynb.ipynb){:target="_blank"}
-->

## 参照

* 学習院大学 田崎 清明先生の [数学：物理を学び楽しむために](https://www.gakushuin.ac.jp/~881791/mathbook/index.html){:target="_blank"}
* [線形代数 学部生向けに書いた資料](https://komazawa-deep-learning.github.io/2021cogpsy/lineralgebra.pdf){:target="_blank"}
* [回帰と実験計画 社会人向けセミナーの資料](https://komazawa-deep-learning.github.io/2021cogpsy/waseda2006.pdf){:target="_blank"}



# 1. 特異値分解 Singular Value Decomposition

<center>
<img src="/assets/Singular-Value-Decomposition.svg" width="39%"><br/>
<div style="text-align: left;width:66%;background-color: cornsilk;">

実在する $2\times2$ 行列 $\mathbf{M}$ の特異値分解 $\mathbf{U\Sigma V^{⁎ }}$ の説明図。<br/>
<!-- Illustration of the singular value decomposition UΣV⁎ of a real 2×2 matrix M. -->

* 上: $\mathbf{M}$ の作用，すなわち単位円盤 D と 2 つの正規単位ベクトル $\mathbf{e}_ {1}$, $\mathbf{e}_ {2}$ への影響によって示される。<br/>
* 左: $\mathbf{D}, \mathbf{e}_{1}, \mathbf{e}_{2}$ に対する $\mathbf{V^{ ⁎}}$ の作用(回転) <br/>
* 下: $\mathbf{\Sigma}$ の作用，つまり特異値 $\sigma_{1}$ による水平方向のスケーリングと $\sigma_{2}$ による垂直方向のスケーリング<br/>
* 右: $\mathbf{U}$ の作用，すなわち回転である。<br/>

<!-- **Top**: The action of M, indicated by its effect on the unit disc D and the two canonical unit vectors e1 and e2. 
**Left**: The action of V⁎, a rotation, on D, e1, and e2. 
**Bottom**: The action of Σ, a scaling by the singular values σ1 horizontally and σ2 vertically. 
**Right**: The action of U, another rotation.	
-->
from wikipedia<br/>

2次元実数シアリングの特異値分解（SVD）を視覚的に表現したもの。

図左上は，単位円盤を青で示し，2 つの正準単位ベクトルを表わしている。
右上は，単位円盤に対する $\mathbf{M}$ の作用を表す。
$\mathbf{M}$ は円を楕円に変形する。
SVD は $\mathbf{M}$ を 3 つの単純な変換に分解する。
すなわち，回転 $\mathbf{V^{* }}$, 座標軸に沿ったスケーリング $\mathbf{\Sigma}$, 2 回目の回転 $\mathbf{U}$ である。
SVD は，楕円の半長軸と半短軸の長さ $\sigma_{1}$ と $\sigma_{2}$ を明らかにする。
これらはちょうどスケーリング $\mathbf{\Sigma}$ の対角要素として現れる特異値。
楕円の座標軸に対する回転は $\mathbf{U}$ で与えられる。
ここで $\phi\doteqdot1.618$ は黄金比を示す。
$\sigma_{1}=\phi,\sigma_{2}=1/\phi,\mathbf{V}^{* }=\tan(\alpha)=\phi$ による $\alpha$ の時計回りの回転，すなわち，$\mathbf{V}$ は $-\alpha$ による回転。
$\mathbf{V}$ は $-\alpha\doteqdot58.28$° による回転。
$\mathbf{U}=\beta$ による反時計回りの回転，$\beta$ は $\tan(\beta)=\phi-1$, すなわち $\beta\approx31.72$° を満たす。
$\mathbf{\Sigma}$ は一意だが，$\mathbf{V}$ と $\mathbf{U}$ は一意ではないことに注意。
$\mathbf{V}$ と $\mathbf{U}$ の両方に 180° の回転を加えたり，反射を加えたりすることができる。
<!-- Visual representation of a singular value decomposition (SVD) of the 2-dimensional real shearing The upper left shows the unit disc in blue together with the two canonical unit vectors. 
The upper right shows the action of M on the unit disc: it distorts the circle to an ellipse. 
The SVD decomposes M into three simple transformations: a rotation $V*$, a scaling Σ along the coordinate axes and a second rotation U. 
The SVD reveals the lengths σ1 resp. σ2 of the semi-major axis resp. semi-minor axis of the ellispe; 
they are just the singular values which occur as diagonal elements of the scaling Σ. 
The rotation of the ellipse with respect to the coordinate axes is given by U. 
In this particular case the decomposition is as follows: σ1 = Φ where Φ ≈ 1.618 denotes the golden ratio σ2 = 1/Φ V* = a clockwise rotation by α with tan(α) = Φ, i.e. 
V is a rotation by −α ≈ −58.28°. 
U = a counter clockwise rotation by β where β satisfies tan(β) = Φ−1, i.e. β ≈ 31.72°. 
Notice that Σ is unique, but V and U are not. 
We could add a rotation by 180° to both V and U or add some reflections.-->
</div>	
</center>

* 線形代数学において，特異値分解 (SVD) は実数または複素数の行列の因数分解である。
正方正則行列の固有値分解を一般化したもので，任意の $m\times n$ 行列に適用される。極座標分解と関連する。
<!-- In linear algebra, the singular value decomposition (SVD) is a factorization of a real or complex matrix. 
It generalizes the eigen decomposition of a square normal matrix with an orthonormal eigenbasis to any $\displaystyle m\times n$ matrix. 
It is related to the polar decomposition.
-->
* 具体的には $m\times n$ 複素行列 $\mathbf{M}$ の特異値分解は $\times m$ 複素ユニタリー行列を $\mathbf{U}$，$n\times n$ 対角線上に非負の実数を持つ直交対角行列を $\mathbf{V}$，$n\times n$ 複素ユニタリー行列を $\mathbf{V}$ とすると，$\mathbf{U\Sigma V^{* }}$ の形で因数分解される。
$\mathbf{M}$ が実数の場合，$\mathbf{U}$ と $\mathbf{V}$ も実数の直交行列であることが保証される。
このような文脈では，SVD はしばしば $\mathbf{U\Sigma V^{\top}}$ と表記される。
<!-- Specifically, the singular value decomposition of an $\displaystyle m\times n$ complex matrix M is a factorization of the form $\displaystyle \mathbf{U\Sigma V^{* }$, where U is an $\displaystyle m\times m}m\times m$ complex unitary matrix, $\displaystyle\mathbf{\Sigma}$ is an $\displaystyle m\times n$ rectangular diagonal matrix with non-negative real numbers on the diagonal, and V is an $\displaystyle n\times n$ complex unitary matrix. 
If M is real, U and V can also be guaranteed to be real orthogonal matrices. 
In such contexts, the SVD is often denoted $\displaystyle \mathbf {U\Sigma V^{T}} $.-->
* 対角線上の要素 $\sigma_{i}=\Sigma_{ii}$ を $\mathbf{M}$ の特異値と呼ぶ。
非ゼロの特異値の数は，$\mathbf{M}$ のランクと等しい。
$\mathbf{U}$ の列と $\mathbf{V}$ の列とは，それぞれ $\mathbf{M}$ の左特異ベクトルと右特異ベクトルと呼ばれる。
<!-- The diagonal entries $\displaystyle\sigma_{i}=\Sigma_{ii}$ of $\displaystyle \mathbf{\Sigma}$ are known as the singular values of M. 
The number of non-zero singular values is equal to the rank of M. 
The columns of U and the columns of V are called the left-singular vectors and right-singular vectors of M, respectively.-->
* SVD は一意ではない。
特異値 $\Sigma_{ii}$ が降順になるように分解を選択することは常に可能である。
この場合 $\mathbf{\Sigma}$ (ただし $\mathbf{U}$ と $\mathbf{V}$ は必ずではない) は $\mathbf{M}$ で一意に決まる。
<!-- The SVD is not unique. 
It is always possible to choose the decomposition so that the singular values $\displaystyle \Sigma_{ii}$ are in descending order. 
In this case, $\mathbf{\Sigma}$ (but not always U and V) is uniquely determined by M.-->
* ここで $\mathbf{\Sigma}$ は $r\times r$ の正方対角線であり，$r\times r$ は $\mathbf{M}$ のランクであり，0 でない特異値のみを持つ。 
この変形では，$\mathbf{U}$ は $m\times r$ の半単射行列，$n\times r$ の半単射行列で，$\mathbf{U^{* }U}=\mathbf{V^{* }V} =\mathbf{I}_ {r}$ となる。
<!-- The term sometimes refers to the compact SVD, a similar decomposition $mathbf{M}=\mathbf{U\Sigma V^{* }}$ in which $\mathbf{\Sigma}$ is square diagonal of size $\displaystyle r\times r$, where $\displaystyle r\leq \min\{m,n\}$ is the rank of M, and has only the non-zero singular values. 
In this variant, U is an $displaystyle m\times r$ semi-unitary matrix and $\displaystyle \mathbf {V}$ is an $\displaystyle n\times r$ semi-unitary matrix, such that $\displaystyle\mathbf {U^{* }U} =\mathbf {V^{* }V} =\mathbf {I}_ {r}$.-->
* SVD の数学的な応用としては，擬似逆行列の計算，行列の近似，行列のランク，範囲，ヌル空間の決定などがある。
また，SVD は，信号処理，データの最小二乗法によるフィッティング，プロセス制御など，科学，工学，統計学のあらゆる分野で非常に有用である。
<!-- Mathematical applications of the SVD include computing the pseudoinverse, matrix approximation, and determining the rank, range, and null space of a matrix. 
The SVD is also extremely useful in all areas of science, engineering, and statistics, such as signal processing, least squares fitting of data, and process control. -->

# 2. ニューラルネットワークを学習するとはどういうことか
<!-- author: Stepan Ulyanin
- date: Feb 1, 2019
- source: https://medium.com/@stepanulyanin/notes-on-deep-learning-theory-part-1-data-generating-process-31fdda2c8941
-->

心理学も，ニューラルネットワークも，現象の予測にはデータを必要とする。
我々は，利用可能なデータを用いて，モデルを訓練する。
**機械学習アルゴリズムの目的は，「見たことのないサンプルに対してモデルがうまく一般化すること」という制約のもとで学習を行う** ことである。
<!-- This is a very crucial question for the whole field of machine learning. 
I want to start with defining a few things. 
First of all, neural networks consume data to predict (classify or regress). 
The data that is available to us as practitioners is training data; we are going to use it to train our model. However, the goal of any machine learning algorithm is to get trained subjected to the constraint: the model should generalize well on unseen samples. 
Here I will only consider the case of classification as it is the most common task for a machine learning algorithm. -->

一方，データを生成する **データ生成過程** がある。
データを生成する仮想的な分布があり，その分布に従うデータを得ることができると考える。
このデータの一部は収集することができ，**経験分布** (データ分布)に従って分布します。
このデータをモデルに通す(学習させる)と，**モデル分布** (仮説) が得られる。
以上が，ニューラルネットワークの学習に必要な 3 つの主な分布であり，汎化の概念はこれら分布から導かれる。
<!-- There is a data-generating process that generates data. 
There is a hypothetical data-generating distribution according to which this data is distributed. 
Some of this data can be collected, and it is, then, distributed according to an empirical distribution. 
If we pass this data through our model, we obtain the model distribution. 
These are the three main distributions we need to know about to train a neural network, and the concept of generalization is directly derived from these distributions. -->
我々の最終目標は，データを生成する分布を学習することである。

教科書的な記述になるが，記述統計と推測統計との差異は，背後に母集団を想定しているか否かである。
この「背後に母集団を想定している」ことは，我々の主たる興味は，生成モデルであることを含意している。
また，生成モデルの仮定は，一般的，かつ普遍的言質を得たいという，研究目的にも合致するだろう。

機械学習において，一般化しなければならないサンプルは，経験的に観察されたサンプルと同じデータ生成過程から来ており，同じデータ生成分布に従っていると仮定される。
ここで重要なのは，経験分布がデータ生成分布を表していない (サンプルが十分でない) 場合，オーバーフィッティングが生じることである。 経験分布がデータ生成過程を完全には代表していないため，例が不足している結果，ニューラルネットワークは経験分布をモデル分布を過度に忠実化し記述する。
結果として，一般化能力が低下する。
これを過学習 (overfitting) と呼ぶ。

科学の目標は，モデル(仮説) の性能を向上させることである。
<!-- 究極の方法の一つは，より多くのデータを収集するか，経験分布をより代表的なものにすることです。 より多くのデータを集めることは，パターンがあり，ノイズフロアが低いことを考慮すると，常にモデルの一般化能力を高めることになります。 しかし，データを収集することは必ずしも容易ではなく，非常にコストがかかる場合もあります。 そのため，研究者は過学習に対抗する別の方法を考え出しました。 
-->
ところが，我々は，データを生成する分布に直接アクセスすることはできない。
そのため，経験分布で近似することに注力することとなる。
モデル分布を経験分布にできる限り近づけ，モデル分布を使って推論を行う。
この作業を行うための統計的道具が以下である。

# 3. カルバック・ライブラー・ダイバージェンスと交差エントロピー
<!-- # 3. Kullback-Leibler Divergence And Cross-Entropy-->

カルバック・ライブラーのダイバージェンス (Kullback-Leibler divergence) は 2 つの分布の距離 (非類似性) の尺度である。
交差エントロピー (cross entropy) は同様のことを行うが，若干異なるアプローチを取る。
次の計算を参照: 
<!-- Kullback-Leibler divergence measures the dissimilarity of two distributions. Cross-Entropy does the same but in a different way. So here is a little math. -->

$$
D_{KL}=\left(\widehat{P}_{\text{data}}\vert\vert P_{\text{model}}\right)
= \sum_{x}\widehat{P}_{\text{data}}(y\vert x)\log\frac{\widehat{P}_{\text{data}}(y\vert x)}{P_{\text{model}}(y\vert x;\theta)}\tag{KL ダイバージェンスの定義}
$$

ここで
$\hat{P}_ {\text{data}}(y\vert x)$ は経験分布，$P_ {\text{model}}(y\vert x;\theta)$ は $\theta$ をパラメータとするモデル分布である。

モデル分布のみが重みによってパラメータ化されていることに注意。
つまり，モデル分布のみが変更(調整，あるいは学習) 可能である。
KL ダイバージェンスの RHS (右辺) を次のように展開する:

$$
\sum_{x}\widehat{P}_{\text{data}}(y\vert x)\log\frac{\widehat{p}_{\text{data}}(y\vert x)}{P_{\text{model}}(y\vert x;\theta)} = 
\sum_{x}\widehat{P}_{\text{data}}(y\vert x)\log\widehat{P}_{\text{data}}(y\vert x)-\sum_{x}\widehat{P}_{\text{data}}(y\vert x)\log P_{\text{model}}(y\vert x;\theta)
$$

RHS (右辺) 第 2 項 (the 2nd term) は重みでパラメータ化されており，これが変更できる唯一の項である。
つまり，モデルの **負の対数尤度** を最小化することで，経験分布とモデル分布の間の KL ダイバージェンスを最小化することができる。
<!-- Notice that the second term in the right hand side is now parametrized by weights and now this is the only term we can alter. 
So we can minimize the Kullback-Leibler divergence (measure of dissimilarity) between the empirical and model distributions by minimizing the Negative Log-Likelihood of the model:-->

$$
-\log P_{\text{model}}(y\vert x;\theta)
$$

2 つの分布間の交差エントロピーは，KLダイバージェンスという用語を定義に持つことで，この過程と関連する。
<!-- Cross-Entropy between two distributions is tied into this process by having the Kullback-Leibler divergence as a term in its definition: -->

$$
\text{CE}\left(\widehat{P}_{\text{data}},P_{\text{model}}\right)
=H\left(\widehat{P}_{\text{data}}\right) + D_{KL}\left( \widehat{P}_{\text{data}} \vert\vert P_{\text{model}} \right)
$$

ここで $H(\cdot)$ は経験分布である引数のエントロピーであり，以下のように定義される:
<!-- Here, $H()$ is the Entropy of its argument, which is the empirical distribution and is defined as: -->

$$
H(\widehat{P}_ {\text{data}})=-\sum \widehat{P}_ {\text{data}}(y\vert x)\log\widehat{P}_ {\text{data}}(y\vert x)
$$

ここで，経験分布のエントロピーを交差エントロピーの定義に代入するとどうなるかを考えてみよう
<!-- Now, notice what happens if we substitute the entropy of the empirical distribution into the definition of the Cross-Entropy: -->

$$
\begin{aligned}
H(\widehat{P}_{\text{data}})+D_{KL}(\widehat{P}_{\text{data}}\vert\vert P_{\text{model}}) &= -\sum_{x}\widehat{P}_{\text{data}}(y\vert x)\log \widehat{P}_{\text{data}}(y\vert x) + \sum_{x}\widehat{P}_{\text{data}}(y\vert x)\log\widehat{P}_{\text{data}}(y\vert x)-\sum_{x}\widehat{P}_{\text{data}}(y\vert x)\log P_{\text{model}}(y\vert x;\theta) \\
&= - \sum_{x}\widehat{P}_ {\text{data}}(y\vert x)\log P_{\text{model}}(y\vert x;\theta)
\end{aligned}
$$

<!-- これはかなりキレイですね。-->
交差エントロピーを期待値の形で書くと次式を得る:
<!-- This is pretty neat. Now, we can write the Cross-Entropy in the form of expectation: -->

$$
CE(\widehat{P}_{\text{data}},P_{\text{model}})
= \mathbb{E}_{x\sim\hat{p}_{\text{data}}}\left[
-\log P_{\text{model}}(y\vert x;\theta)\right]
$$

この記述と前の記述から，交差エントロピーを最小化したい場合は，モデルの負の対数尤度を最小化する必要があることがわかる。
実際には，負の対数尤度損失，あるいは，対数ソフトマックスを計算することとなる。
<!-- From this and the previous statements we can see that if we want to minimize the Cross-Entropy (cross-entropy loss in many deep learning libraries) we need to minimize the Negative Log-Likelihood of the model (cross-entropy loss in many libraries typically calculate Negative Log-Likelihood Loss and Log-Softmax under the hood, like in PyTorch). -->

<!-- しかし，大きな疑問がまだ残っています。 -->
では，ニューラルネットワークは，KLダイバージェンスや交差エントロピーをどのようにして最小化して学習するのだろうか？
ニューラルネットワークの結合係数 (重み係数) の最尤推定値 (MLE) は以下のように定義される:
<!-- It turns out that there is a link between the Maximum Likelihood Estimate of the weights and the the two aforementioned losses. The MLE for the weights is defined as: -->

$$
\theta_{ML}=\arg\max_{\theta}\mathbb{E}_{x\sim \hat{P}_{\text{data}}} \left[\log P_{\text{model}}(y\vert x;\theta)\right]
$$

したがって，経験分布とモデル分布の間の KL ダイバージェンスと交差エントロピーを最小化することは，ニューラルネットワークのパラメータ，すなわち重み係数の最尤推定値を求めることと等価であることがわかる。
<!-- Therefore, we can see that the minimization of the Kullback-Leibler divergence and Cross-Entropy between the empirical and the model distributions is equivalent to finding the Maximum-Likelihood estimate for the parameters of the neural network, i.e. weights. -->

モデルは，経験分布とモデル分布の間の KL ダイバージェンスや交差エントロピーの最小化，
あるいは負の対数尤度損失の最小化などの過程を通じて，証拠 (経験分布)， すなわちデータに最も適合するパラメータセットを見つけることができる。
<!-- Our model can find the set of parameters that results in the best fit to the evidence (empirical distribution), i.e. training data through the process of minimization of Kullback-Leibler divergence or Cross-Entropy between the empirical distribution and the model distribution, or equivalently minimization of the Negative Log-Likelihood Loss.-->

経験分布がデータ生成分布の代表性が高ければ，訓練データに適合したモデルは，未知の事例が同じデータ生成分布から来ているという仮定に制約されて，未知の例に対して非常によく一般化することができる。
<!-- If the empirical distribution is highly representative of the data-generating distribution, the model that fits the training data will be able to generalize very well on the unseen examples constrained to the assumptions that the unseen examples come from the same data-generating distribution. -->
