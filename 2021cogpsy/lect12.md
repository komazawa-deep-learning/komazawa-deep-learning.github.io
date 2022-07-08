---
title: 第12回
layout: home
date: 2021_1210
---

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 10/Dec/2021<br/>
Appache 2.0 license<br/>
</div>

# 転移学習とファインチューニング，顔認識実演


## 実習ファイル

* [ヴィオラ=ジョーンズ アルゴリズム(従来手法) による顔認識実験 <img src="https://komazawa-deep-learning.github.io/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_0930viola_jones_ipynb.ipynb){:target="_blank"}
* [顔，非顔判別データセットを用いた紡錘状回のモデル化 --- 転移学習を用いた顔検出モデル ---  <img src="https://komazawa-deep-learning.github.io/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_0925face_dataset_transfer_learning.ipynb){:target="_blank"}



## カルバック・ライブラー・ダイバージェンスと交差エントロピー
<!-- # 3. Kullback-Leibler Divergence And Cross-Entropy-->
<!--
- author: Stepan Ulyanin
- date: Feb 1, 2019
- source: https://medium.com/@stepanulyanin/notes-on-deep-learning-theory-part-1-data-generating-process-31fdda2c8941
-->

前々回にも解説したとおり，カルバック・ライブラー・ダイバージェンス Kullback-Leibler divergence (以下 KL ダイバージェンス) は 2 つの分布の非類似性を測定します。
一方，交差エントロピー cross entropy は同じことをしますが，やり方が違います。
まず，KL ダイバージェンスの定義を示す:

$$
D_{KL}=\left(\widehat{P}_{\text{data}}\vert\vert P_{\text{model}}\right)
= \sum_{x}\widehat{P}_{\text{data}}(y\vert x)\log\frac{\widehat{P}_{\text{data}}(y\vert x)}{P_{\text{model}}(y\vert x;\theta)}\tag{KL ダイバージェンスの定義}
$$

ここで
$\hat{P}_ {\text{data}}(y\vert x)$ は経験分布，$P_ {\text{model}}(y\vert x;\theta)$ は $\theta$ をパラメータとするモデル分布です。
モデル分布のみが重みによってパラメータ化されていることに注意してください。
つまり，モデル分布のみが変更可能です。

ここで KL ダイバージェンスの RHS を展開してみましょう。
<!-- Notice that only the model distribution is parametrized by the weights, so it is the only one we would be able to alter in any way. 
Now, let’s expand the right hand side of the KL divergence: -->

$$
\sum_{x}\widehat{P}_{\text{data}}(y\vert x)\log\frac{\widehat{p}_{\text{data}}(y\vert x)}{P_{\text{model}}(y\vert x;\theta)} = 
\sum_{x}\widehat{P}_{\text{data}}(y\vert x)\log\widehat{P}_{\text{data}}(y\vert x)-\sum_{x}\widehat{P}_{\text{data}}(y\vert x)\log P_{\text{model}}(y\vert x;\theta)
$$

RHS 第 2 項は重みでパラメータ化されており，これが変更できる唯一の項であることに注意してください。
つまり，モデルの負の対数尤度を最小化することで，経験分布とモデル分布の間のカルバック・ライブラー・ダイバージェンス (非類似性の尺度) を最小化することができます。
<!-- Notice that the second term in the right hand side is now parametrized by weights and now this is the only term we can alter. 
So we can minimize the Kullback-Leibler divergence (measure of dissimilarity) between the empirical and model distributions by minimizing the Negative Log-Likelihood of the model:
-->

$$
-\log P_{\text{model}}(y\vert x;\theta)
$$

2 つの分布間の交差エントロピーは，カルバック・ライブラー・ダイバージェンスと関連付けることが可能です。次式を参照してください:

$$
\text{CE}\left(\widehat{P}_{\text{data}},P_{\text{model}}\right)
=H\left(\widehat{P}_{\text{data}}\right) + D_{KL}\left( \widehat{P}_{\text{data}} \vert\vert P_{\text{model}} \right)
$$

ここで $H()$ は経験分布である引数のエントロピーであり，以下のように定義されます:
<!-- Here, $H()$ is the Entropy of its argument, which is the empirical distribution and is defined as: -->

$$
H(\widehat{P}_ {\text{data}})=-\sum \widehat{P}_ {\text{data}}(y\vert x)\log\widehat{P}_ {\text{data}}(y\vert x)
$$

ここで，経験分布のエントロピーを交差エントロピーの定義に代入してみます:
<!-- Now, notice what happens if we substitute the entropy of the empirical distribution into the definition of the Cross-Entropy: -->

$$
\begin{aligned}
H(\widehat{P}_{\text{data}})+D_{KL}(\widehat{P}_{\text{data}}\vert\vert P_{\text{model}}) &= -\sum_{x}\widehat{P}_{\text{data}}(y\vert x)\log \widehat{P}_{\text{data}}(y\vert x) + \sum_{x}\widehat{P}_{\text{data}}(y\vert x)\log\widehat{P}_{\text{data}}(y\vert x)-\sum_{x}\widehat{P}_{\text{data}}(y\vert x)\log P_{\text{model}}(y\vert x;\theta) \\
&= - \sum_{x}\widehat{P}_ {\text{data}}(y\vert x)\log P_{\text{model}}(y\vert x;\theta)
\end{aligned}
$$


<!--これはかなりキレイですね。-->
符号に注意して考えれば，経験分布のエントロピーは，経験分布とモデル分布との KL ダイバージェンスと直上式で表せることになります。
上式を，ELBO または変分下限 variational lower bound と呼ぶことがあります。

次に，交差エントロピーを期待値の形で書いてみましょう。
<!-- This is pretty neat. Now, we can write the Cross-Entropy in the form of expectation: -->

$$
CE(\widehat{P}_{\text{data}},P_{\text{model}})
= \mathbb{E}_{x\sim\hat{p}_{\text{data}}}\left[
-\log P_{\text{model}}(y\vert x;\theta)\right]
$$

この記述と前の記述から，交差エントロピー（多くの深層学習ライブラリにおける交差エントロピー損失）を最小化したい場合は，モデルの負の対数尤度を最小化する必要があることがわかります（多くのライブラリにおける交差

<!-- エントロピー損失は PyTorch のように，フードの下で負の対数尤度損失と 対数ソフトマックスを計算するのが一般的です）。
 --><!-- From this and the previous statements we can see that if we want to minimize the Cross-Entropy (cross-entropy loss in many deep learning libraries) we need to minimize the Negative Log-Likelihood of the model (cross-entropy loss in many libraries typically calculate Negative Log-Likelihood Loss and Log-Softmax under the hood, like in PyTorch). -->

<!-- しかし，大きな疑問がまだ残っています。
ニューラルネットワークは，カルバック・ライブラー・ダイバージェンスや交差エントロピーをどのようにして最小化して学習するのでしょうか？ -->
<!-- But the big question still remains unanswered: how does the neural network learn by minimizing the Kullback-Leibler divergence or Cross-Entropy? -->


次に，これらの推定方法についてです。
<!-- 重みの最尤推定値と前述の 2 つの損失の間には関連性があることがわかりました。 -->
ニューラルネットワークのパラメータ，尤度関数は次のように定義されます。
<!-- It turns out that there is a link between the Maximum Likelihood Estimate of the weights and the the two aforementioned losses. The MLE for the weights is defined as: -->

$$
\theta_{ML}=\arg\max_{\theta}\mathbb{E}_{x\sim \hat{P}_{\text{data}}} \left[\log P_{\text{model}}(y\vert x;\theta)\right]
$$

したがって，経験分布とモデル分布の間のカルバック・ライブラーダイバージェンス Kullback-Leibler divergence と交差エントロピーを最小化することは，ニューラルネットワークのパラメータ，すなわち重みの最尤推定値を求めることと等価であることがわかります。
<!-- Therefore, we can see that the minimization of the Kullback-Leibler divergence and Cross-Entropy between the empirical and the model distributions is equivalent to finding the Maximum-Likelihood estimate for the parameters of the neural network, i.e. weights. -->


我々のモデルは、経験分布とモデル分布の間の Kullback-Leibler divergence や交差エントロピーの最小化，
あるいは負の対数尤度損失の最小化などの過程を通じて，証拠 (経験分布)， すなわち訓練データに最もフィットするパラメータセットを見つけることができます。
<!-- Our model can find the set of parameters that results in the best fit to the evidence (empirical distribution), i.e. training data through the process of minimization of Kullback-Leibler divergence or Cross-Entropy between the empirical distribution and the model distribution, or equivalently minimization of the Negative Log-Likelihood Loss.-->

経験分布がデータ生成分布の代表性が高ければ，訓練データに適合したモデルは，未知の事例が同じデータ生成分布から来ているという仮定に制約されて，未知の例に対して非常によく一般化することができます。
<!-- If the empirical distribution is highly representative of the data-generating distribution, the model that fits the training data will be able to generalize very well on the unseen examples constrained to the assumptions that the unseen examples come from the same data-generating distribution. -->


