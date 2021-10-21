---
title: 第05回
layout: home
---

# 授業計画案 (仮)

* 10/22 05【浅川：標準正則化理論における，滑らかさの制約条件と単純さの制約条件を オリベッティ顔データセットを用いて，L1 と L2 の実習】
* 10/29 06【浅川：畳み込みニューラルネットワークによる特徴抽出】<!-- 　←　[10/01, 04] -->
<!-- ＞固有顔？　現在の心理学研究ではどうなっているのか？　＞永田先生 -->
* 11/05 07【竹市対面：初期視覚特徴の神経生理学と　解析力学入門】
* 11/12 08【浅川：初期視覚特徴の検証，畳み込み演算による第 1 次視覚野の対応物の検証】<!-- 　++ -->
* 11/19 09【浅川：意味的領域切り出し，および，汎光学的領域切り出しとクラス関連記憶】<!-- 　←　[10/22 05] -->
* 11/26 10【竹市対面：顔認知の神経生理学のもろもろ，カテゴリ知覚，個体識別と表情認知，紡錘状回と相貌失認，視点依存性など】
* 12/03 11【浅川：ビオラ・ジョーンズアルゴリズムの実習】<!-- 　++   <---- ここに，顔の特徴点抽出実習 -->
* 12/10 12【浅川：転移学習とファインチューニング，顔認識実演】<!-- 　←　[11/12 08] -->
* 12/17 13【浅川：ディープラーニングを用いた転移学習で，顔と非顔の識別をする実習】<!-- 　++ -->
* 12/24 14（課題授業）【浅川： GAN と変分自己符号化器モデルによる実習も行う】
* 01/07 15【永田：授業のまとめ】

# 0. 本日のメニュー


* [多項式回帰によるアンダーフィッティング，オーバーフィッテイングのデモ <img src="https://komazawa-deep-learning.github.io/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2020Sight_Visit_polynomilal_fittings_demo.ipynb){:target="_blank"}
* [顔データベースによる機械学習のデモと PyTorch による回帰，正則化項の実習](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_1020face_dataset_regression.ipynb){:target="_blank"}



# 1. 一般化とオーバーフィッティング，アンダーフィッティング

- データへの当てはまりが良いことが良いモデルではない
- 未知のデータに対してどれほど当てはまるのかがモデルの性能を決める
<!--
* 訓練データ training data 実際に学習に用いたデータ
* テストデータ test data 未知のデータ，訓練時には使用していないデータ
-->
* オーバーフィッティング 訓練データへの過剰適合
* アンダーフィッティング 訓練データを十分に学習できない場合

<!--
* データ数(*小*) アンダーフィットする可能性**大**
-->

<center>
<img src="/assets/04_07underOverFittings.svg" width="39%"><br/>
<!-- ![](assets/04_07underOverFittings.svg){#fig:underOver style="width:59%"}
 --></center>

<!-- - [多項回帰による過剰適合，デモ <img src="assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2020Sight_Visit_polynomilal_fittings_demo.ipynb)
-->

<!--
It's not a good idea to test a machine learning model on a dataset which we used to train it, since it won't give any indication of how well our model performs on unseen data. The ability to perform well on unseen data is called generalization, and is the desirable characteristic we want in a model.
When a model performs well on training data (the data on which the algorithm was trained) but does not perform well on test data (new or unseen data), we say that it has overfit the training data or that the model is overfitting. This happens because the model learns the noise present in the training data as if it was a reliable pattern. 
Conversely, when a model does not perform well on training data (i.e. it fails to capture patterns present in the training data) as well as unseen data then it is said to be under-fitting. That is, the model is unable to capture patterns present in the training data. 
A smaller dataset can significantly increase the chance of overfitting. This is because it is much tougher to separate reliable patterns from noise when the dataset is small. [1]
Examples of overfitting and under-fitting
-->

$$
\begin{aligned}
y &= w_0 + w_1 x,\\
y &= w_0 + w_1 x_1 + w_2 x_2,\\
y &= w_0 + w_1 x_1 +\cdots + x_nx_n
\end{aligned}
$$

<!--
Suppose we have the following dataset (red points in the figure), where we have only one input variable x and one output variable y. 

If we fit y = w0 + w1x to the above dataset, we get the straight line fit as shown above. Note that this is not a good fit since it is quite far from many data points. This is an example of under-fitting. 

Now, if we add another feature x2 and fit y = w0 + w1x1 + w2x2 then we'll get a curve fit as shown above. (Side note: This is still a linear model. x2 is a feature, i.e. input. The weights are w's and they are interacting linearly with the features x and x2. The curve we are fitting is a quadratic curve). As you can see, this is slightly better since it passes much closer to the data points above. 

If we keep adding more features we'll get a curve that is more and more complex and that passes through more and more data points. Above figure shows an example. This is an example of overfitting. In this case, we are performing polynomial fitting y = w0 + w1x1 + w2x2 + ... + wdxd.
Even though the fitted curve passes through almost all points, it won't perform well on unseen data. 
-->

## 2. オーバーフィッティングの回避
<!-- Strategies to Avoid Overfitting

One way to avoid overfitting it to collect more data. However, that is not always feasible. Below are some other strategies to overcome the problem of overfitting - regularization and cross-validation. -->

## 2.1 正則化 Regularization

モデルの複雑さを調整する

<!--
In regularization, we combat overfitting by controlling the model's complexity, i.e. by introducing an additional term in our cost function in-order to penalize large weights. This biases our model to be simpler, where simpler is weights of smaller magnitude (or even zero). We want to make the weights smaller, because complex models and overfitting are characterized by large weights. Recall the mean-squared error cost function, 
J(w)=1nn∑i=1(y(xi)−yit)2
-->

### 2.1.1 L2 正則化 リッジ回帰
<!--Regularization or Ridge Regression-->

$$
\text{損失関数(目的関数)} = \text{誤差} + \lambda\left|w\right|^2
$$

<!--
In L2 regularization, a commonly used regularization technique, we add a penalty proportional to the squared magnitude of each weight. Our new cost function with L2 regularization is as follows:-
J(w)=1nn∑i=1(y(xi)−yit)2+λ||w2||
where, the first term is the same as in regular linear regression (without any regularization), and the second term is the regularization term. λ is a hyper-parameter that we choose and decides the regularization strength. Larger values of λ imply more regularization, i.e. smaller values for the model parameters. ||w2|| is w12 + w22 + ... wd2. 
-->
* L2 正則化はパラメータの絶対値が大きくなると罰則項 pernalty term として作用

<!--
L2 regularization penalizes the larger weights more (since the penalty is proportional to the weight squared). For example, reducing w = 10 to w = 9 has a larger effect on the penalty term (102-92) than reducing w = 3 to w = 2 (32-22).  
-->

### 2.1.2 L1 正則化 Lasso 回帰 <!--Regularization or Lasso Regression-->

$$
\text{目的関数} = \text{誤差} + \lambda\left|w\right|
$$

<!--
In L1 regularization, we the penalty term is λ ||w||. That is, our cost function is:
J(w)=1nn∑i=1(y(xi)−yit)2+λ||w||
-->
<!--
An interesting property of L1 regularization is that model's parameters become sparse during optimization, i.e. it promotes a larger number of parameters w to be zero. This is because smaller weights are equally penalized as larger weights, whereas in L2 regularizations, larger weights are being penalized much more. This sparse property is often quite useful. For example, it might help us identify which features are more important for making predictions, or it might help us reduce the size of a model (the zero values don't need to be stored). 
Ordinary least square (which we saw earlier in linear regression) with L2 regularization is known as Ridge Regression and with L1 regularization it is known as Lasso Regression.
Cross Validation and Validation Datasets
-->

# 3. 正則化項

- 簡潔さ原理 simplicity principle L1
- 滑らかさ原理 smoothness principle L2
- 疎性原理 sparseness principle L0

<center>
<img src="/assets/Regularization.svg" width="39%"><br/>
<!-- ![]( assets/Regularization.svg){#fig:regularization style="width:44%"} -->
</center>

## 3.1 正則化項の影響

<center>
<img src="/assets/2001Hastie_p84.png" width="33%">
<img src="/assets/2001Hastie_p89.png" width="33%"><br/>
<img src="/assets/2001Hastie_p91.png" width="33%">
<!-- ![](assets/2001Hastie_p84.png){#fig:hasiterP84 style="width:33%"}
![](assets/2001Hastie_p89.png){#fig:hasiterP84 style="width:33%"}<br/>
![](assets/2001Hastie_p91.png){#fig:hasiterP84 style="width:39%"}
-->
</center>
[@2001HTF] より

<!-- # まとめ

- アンダーフィッテイングとオーバーフィッティング
- データ数に比べて，推定すべきパラメータが多過ぎ = オーバーフィッティング
- データ数に比べて，推定すべきパラメータが少な過ぎ = アンダーフィッティング
- 正則化 L1, L2, L0, エラスティック
- 正則化項の大きさ $\lambda$ はハイパーパラメータと呼ぶ

# クイズ

次の ＊＊＊＊ に当てはまる言葉をかんがえてください

- データ数に比べて，推定すべきパラメータの過多 = ＊＊＊＊フィッティング
- データ数に比べて，推定すべきパラメータが過少 = ＊＊＊＊フィッティング

# クイズの答え

- データ数に比べて，推定すべきパラメータが過多 = オーバーフィッティング
- データ数に比べて，推定すべきパラメータが過少 = アンダーフィッティング
-->

- [多項式回帰の簡単なデモ  <img src="https://komazawa-deep-learning.github.io/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2020Sight_Visit_polynomilal_fittings_demo.ipynb){:target="_blank"}

# 4. ネオコグニトロン (Fukushima, 1980)

* S 細胞と C 細胞との繰り返し。最初の多層（深層）化された物体認識モデルととらえることが可能
    - S 細胞：生理学の単純細胞 simple cells に対応。受容野 receptive fileds の概念を実現。特徴抽出，特徴検出を
行う。<br/>
    - C 細胞：複雑細胞 complex cells に対応。広い受容野。位置，回転，拡大縮小の差異を吸収<br>

<center>
<img src="/assets/Neocognitron.jpeg" width="66%">
<div class="figcaption">
ネオコグニトロンの模式図
</div>
</center>

---

# 5. LeNet5 (LeCun, 1998)

- **LeNet**. Yann LeCun (現 Facebook AI 研究所所長)による CNN 実装
[LeNet](http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf){:target="_blank"} 手書き数字認識
 
<center>
<img src="figures/1998LeNet5.png" width="88%">
<div class="figcaption">
LeNet5 の論文より改変
</div>
</center>

- 畳込層とプーリング層（発表当初はサブサンプリング）との繰り返し
    - 畳込とプーリングは<font color="green">局所結合</font>
- MNIST を用いた１０種類の手書き文字認識
- 最終２層は全結合層をつなげて最終層１０ニューロン，最終層の各ニューロンの出力がそれぞれの数字（０から９までの１０種）に対応する


<center>
<img src="/assets/1999Riesenhuber_Poggio_fig2.svg" width="49%"><br/>
<!-- <img src="https://raw.githubusercontent.com/komazawa-deep-learning/komazawa-deep-learning.github.io/cde8974e50a598aa8c2ff88760acc450fab3fbf8/assets/1999Riesenhuber_Poggio_fig2.svg"  style="width:89%"><br/> -->
<div style="text-align:left; width:66%; background-color:cornsilk">
モデルのスケッチ。
このモデルは、単純な細胞から作られた複雑な細胞の古典的なモデル[4]を拡張したもので、線形演算（福島の表記法では「S」ユニット，テンプレート・マッチング 図中の実線）と非線形演算
（「C」プーリングユニット，最大値 MAX 演算を行う 図中破線）を持つ層の階層で構成。
細胞入力の最大値を選択、その値を用いてセルを駆動する非線形の MAX演算は複雑細胞に対して，線形入力の合計とは異なり モデルの特性の鍵となる概念。
この 2 種類の操作は 異なる位置にチューニングされた求心性結合をプールすることでパターン特異性と並進不変性を，また異なるスケールにチューニングされた求心性結合をプールすることで、スケール不変性をもたらした(図示せず)。
</div>
</center>

# 6. 畳み込みニューラルネットワーク CNN

畳み込みニューラルネットワークは，ネオコグニトロンを先祖にした現在のニューラルネットワークによる画像認識の基礎モデルです。

## 6.1 CNN の特徴

<!--[@2017Asakawa_deep_jps][^2017Aakawa\_deep\_jps\]-->。

1. 畳込み演算 (convolutional operation)
1. 非線形活性化関数 (nonlinear activation functions)
3. プーリング処理 (pooling)
4. データ拡張 (data augmentation)
5. バッチ正規化 (batch normalization)
6. ショートカット(shortcut) あるいは スキップ結合
7. ドロップアウト (dropout)
8. GPU の使用


* カーネル, ストライド，ダイアレーション，勾配消失問題，整流線形化関数 (ReLU),
* 完全結合層，交差エントロピー損失
* データ拡張 data augumentation
* 転移学習 transfer learning 

<center>
    <iframe src="/2021/conv-demo/index.html" width="140%" height="640px;" style="border:none;"></iframe>

</center>


## 6.2 ディープラーニングの短所

- データハングリー data hungry
- 計算資源ハングリー resource hungry
- 理論欠如 theory lagging
- 不透明 opacity
- ニューラルネットワークは素人の統計学である, Anderson et. al (1993)


<!--
## [TensorFlow HUB](https://www.tensorflow.org/hub){:target="_blank"}

- ドロップアウト，データ拡張，各種正規化: cnn.md
- 有名なモデル LeNet，Alex Net，Inception，VGG，ResNet
- R-CNN，ハイウェイネット，YOLO，SSD
- セマンティックセグメンテーション
- 転移学習，事前学習，ファインチューニング
- GAN

### インセプション Inception，残渣ネット ResNet，領域 R-CNN (Regional Convolutional Neural Networks)
- what and where routes 
- 心理学的対応物(？)
  - Cadieu (2014) Deep Neural Networks Rival the Representation of Primate IT Cortex for Core Visual Object Re cognition
  - Nasr, Viswanathan, Nieder (2019) Number detectors spontaneously emerge in a deep neural network designed for visual object recognition
  - Marcus (2018) Deep Learning A Critical Appraisal
 -->


# 7. 最大値プーリングの生理学的根拠

<center>
<img src="/assets/1999Riesenhuber_Poggio_fig3a.svg" width="49%"><br/>
<div style="text-align: left; width:66%; background-color:cornsilk">
MAX 機構 高度に非線形な形状調整の特性。
「最適」特徴を決定するために考案された「単純化手順」を用いて得られた下側頭葉細胞の応答（選好刺激に対する反応が
等しくなるように正規化された反応)。
この実験では、もともと細胞は「水のボトル」の画像（一番左の物体）に非常に強い反応を示した。
その後、刺激を単色の輪郭に単純化したところ、細胞の発火が増加し、さらに、楕円を支える棒からなるパドルのような物
体に変化した。
この物体が強い反応を引き起こすのに対し、棒や楕円だけではほとんど反応しなかった。
</div>
</center>

<center>
<img src="/assets/1999Riesenhuber_Poggio_fig3b.svg" width="49%"><br/>
<div style="text-align: left; width:88%; background-color:cornsilk">
実験とモデルの比較。
白棒はの実験用ニューロンの反応を示す。
黒と灰色の棒は 選好刺激の 幹-楕円 の基部の遷移に合わせてチューニングしたモデル細胞の反応を示している。
モデル細胞は 直上図に示したモデルを簡略化したもの。
受容野の各位置に 2 種類の S1 特徴があり、それぞれが遷移領域の左側または右側にチューンしていて、その出力が C1 ユニットに入力され MAX 関数 (黒棒) または SUM 関数 (灰色棒) を用いてプールされている。
モデル細胞は 実験ニューロンの 選好刺激が受容野内にあるときに反応が最大になるよう、C1 ユニットに接続されていた。
</div>
</center>


# 8. 生理学，視覚心理学との対応

- Julesz(1981) Textons, the elements of texture perception, and their interactions, Nature

<center>
<img src="/assets/1981Julesz-texton-Fig2.svg" width="84%"><br/>
Julesz (1981) Fig. 2 より
</center>


### 生理学との対応 (Hubel and Wiesel のネコとサル, Blackmore のネコ, ヴァンエッセン) 
- 層間の結合の仕方, アーキテクチャ
- forward/backward 役割，機能，実現方法
- 側抑制 lateral inhibition (これについては多層化して回避できる可能性あり)
- shape from X は正しかったのか？ ただし発達心理学におけるシェイプバアスは言語発達において重要な意味を持つはず
。だからと言って乳幼児はそのように強制(脅迫？)，矯正されて育つわけではないだろう。

    - Ritter (2017) Cognitive Psychology for Deep Neural Networks: A Shape Bias Case Study
    - Landau, Smith, Jones (1992) Syntactic Context and the Shape Bias in Childrens and Adults Lexical Learnin
    - Yamins (2016) Using goal-driven deep learning models to understand sensory cortex
    - Julez のアプローチは視覚研究者 Haar, SIFT, DoG などのアルゴリズム開発者と対応
    - Poggio (1985) Computational Vision and Regularization Theory

# 9. 転移学習

**転移学習** transfer learning は機械学習分野のみならず，ロボット工学や実応用の分野でも応用が考えられます。
シミュレーションと現実との間隙をどのように埋めるのかという大きな問題に関連します。
一方で，転移学習と **ファインチューニング** や **領域適応** domain adaptation の区別がなされています。

転移学習とは 課題 A を用いて訓練したモデルに対して，別の課題 B に適用することを言います。
DNN では転移学習は頻用されます。
イメージネットで画像分類を学習したネットワークに対して，例えば顔認識を学習させるような場合です。

PyTorch のチュートリアルなどでは，学習済のネットワークに対して，最終直下層を入れ替えて別の課題を訓練することを
転移学習と呼びます。
このとき，最終直下層と出力層との結合を学習させ，その他の下位層の結合は固定し，訓練しません。
一方で，下位層まで含めて全結合を訓練させる場合をファインチューニングと呼び，区別しています。

<div align="center" style="width:99%">
<img src="/assets/2019Ruder_hard_parameter_sharing_p48.jpg" style="width:44%">
<img src="/assets/2019Ruder_soft_parameter_sharing_p49.jpg" style="width:44%"><br/>
左: ハードパラメータ共有: 転移学習,  右: ソフトパラメータ共有: ファインチューニング
</div>


### Notebooks

- [colab/text_classification_with_tf_hub_on_kaggle.ipynb](https://github.com/tensorflow/hub/blob/master/examples/colab/text_classification_with_tf_hub_on_kaggle.ipynb)
Shows how to solve a problem on Kaggle with TF-Hub.
- [colab/semantic_similarity_with_tf_hub_universal_encoder.ipynb](https://github.com/tensorflow/hub/blob/master/examples/colab/semantic_similarity_with_tf_hub_universal_encoder.ipynb)
Explores text semantic similarity with the [Universal Encoder Module](https://tfhub.dev/google/universal-sentence-encoder/2).
- [colab/tf_hub_generative_image_module.ipynb](https://github.com/tensorflow/hub/blob/master/examples/colab/tf_hub_generative_image_module.ipynb)
Explores a generative image module.
- [colab/action_recognition_with_tf_hub.ipynb](https://github.com/tensorflow/hub/blob/master/examples/colab/action_recognition_with_tf_hub.ipynb)
Explores action recognition from video.
- [colab/tf_hub_delf_module.ipynb](https://github.com/tensorflow/hub/blob/master/examples/colab/tf_hub_delf_module.ipynb)
Exemplifies use of the [DELF Module](https://tfhub.dev/google/delf/1) for landmark recognition and matching.
- [colab/object_detection.ipynb](https://github.com/tensorflow/hub/blob/master/examples/colab/object_detection.ipynb) 
Explores object detection with the use of the  [Faster R-CNN module trained on Open Images v4](https://github.com/tensorflow/hub/blob/master/examples/colab/object_detection.ipynb)



#### プーリング Pooling

ネットワークが、ある特定の場所のある特定の色合いのある特定の特徴を探してしまうのは、一番避けたいことです。
これでは良いCNNを作ることはできません。
画像は反転したり、回転したり、つぶれたりしているものがいい。
ネットワークがすべての画像の中からある物体（たとえばヒョウ）を認識できるように、同じものの写真がたくさん必要で
す。大きさや場所は関係ありません。
照明や斑点の数、そのヒョウが早く眠っているのか、獲物を潰しているのかなどは関係ありません。
空間的な変化が欲しい。柔軟性が必要です。
それがプーリングです。
<!--
The last thing you want is for your network to look for one specific feature in an exact shade in an exact loc
ation. 
That’s useless for a good CNN! 
You want images that are flipped, rotated, squashed, and so on. 
You want lots of pictures of the same thing so that your network can recognize an object (say, a leopard) in a
ll the images. No matter what the size or location. 
No matter what the lighting or the number of spots,or whether that leopard is fast asleep or crushing prey. 
You want **spatial variance**! You want flexibility. 
That’s what pooling is all about.
-->

プーリングは、入力表現のサイズを徐々に小さくしていきます。
これにより、画像内のオブジェクトがどこにあっても検出できるようになります。
プーリングは、必要なパラメータの数を減らし、必要な計算量を減らすのに役立ちます。
また、**オーバーフィッティング** の抑制にも役立ちます。
<!-- Pooling progressively reduces the size of the input representation. 
It makes it possible to detect objects in an image no matter where they’re located. 
Pooling helps to reduce the number of required parameters and the amount of computation required. 
It also helps control **overfitting**.-->

オーバーフィッティングは、テスト前に情報を理解せずに超具体的な内容を暗記してしまうのと同じようなものです。
細かいことを暗記するときは、家でフラッシュカードを使ってやるといいでしょう。
しかし、実際のテストでは、新しい情報が提示されると失敗してしまいます。
<!-- Overfitting can be kind of like when you memorize super specific details before a test without understanding t
he information. 
When you memorize details, you can do a great job with your flashcards at home.
You’ll fail a real test, though, if you’re presented with new information.-->


別の例としては、訓練データに含まれるすべての犬に斑点と黒目がある場合、ネットワークは、犬に分類するために
は画像に斑点と黒目がなければならないと考えるでしょう。
その学習データを使ってテストをすると、驚くほど正確に犬を分類することができます。
犬を正しく分類することができます。しかし、「犬」と「猫」しか出力されていないネットワークに、ロットワイラーとハ
スキーが写っている画像を新たに入力した場合、ロットワイラーとハスキーの両方を猫に分類してしまうでしょう。このよ
うな問題があるのです！)
<!-- 
(Another example: if all of the dogs in your training data have spots and dark eyes, your network will believe
 that for an image to be classified as a dog, it must have spots and dark eyes. 
If you test your data with that same training data, it will do an amazing job of
classifying dogs correctly! But if your outputs are only “dog” and “cat,” and your network is presented wiew images containing, say, a Rottweiler and a Husky, it will probably wind up classifying both the Rottweiler 
and the Husky as cats. You can see the problem!)-->

分散がないと、ネットワークはトレーニングデータと完全に一致しない画像では役に立たなくなります。

**訓練データと検証データは必ず別々にする** 

- 訓練データで検証を行うと ネットワークはその情報を記憶してしまいます。
- 新しいデータを導入すると、ひどい結果になるでしょう。
<!-- Without variance, your network will be useless with images that don’t exactly match the training data. 
**Always, always, always keep your training and testing data separate**! 
If you test with the data you trained on, your network has the information memorized! 
It will do a terrible job when it’s introduced to any new data.  -->


### 過学習は良くない

つまり、このステップでは、**特徴地図** を取得し、**プーリング層** を適用して、**プール済特徴地図** を作成します。
<!-- So for this step, you take the **feature map**, apply a **pooling layer**, and the result is the **pooled feature map**.-->

プーリングの最も一般的な例は、**最大値プーリング** (またはマックスプーリング) です。
最大値プーリングでは、入力画像を重ならない領域のセットに分割します。
各エリアの出力は、各エリアの最大値となります。
これにより、少ないパラメータで小さなサイズになります。
<!-- The most common example of pooling is **max pooling**. 
In max pooling, the input image is partitioned into a set of areas that don’t overlap. 
The outputs of each area are the maximum value in each area. 
This makes a smaller size with fewer parameters. -->

**最大値プーリング** は， 画像の各スポットで最大値だけの残して他は捨て去ることを意味します。
これにより、特徴ではない 75％ の情報を取り除くことができます。
ピクセルの最大値を取ることで、歪みを考慮することができます。
特徴が左や右に少し回転しても、プールされた特徴は同じになります。サイズやパラメータを小さくしているのですね。
これは、モデルがその情報に対してオーバーフィットしないことを意味するので、素晴らしいことです。
<!-- Max pooling is all about grabbing the maximum value at each spot in the image. 
This gets rid of 75% of the information that is not the feature. 
By taking the maximum value of the pixels, you’re accounting for distortion. 
If the feature rotates a little to the left or right or whatever, the pooled feature will be the same. You’rereducing the size and parameters. 
This is great because it means that the model won’t overfit on that information.-->

**平均プーリング** または **合計プーリング** を使用することもできますが、一般的な選択肢ではありません。
実際には、最大プーリングの方が両者よりも性能が良い傾向にあります。
最大プーリングでは、最大のピクセル値を取ることになります。
平均プーリングでは、画像のその場所にあるすべてのピクセル値の平均を取ります。
実際には、より小さなフィルターを使ったり、プーリングレイヤーを完全に破棄したりする傾向があります。
これは、積極的な表現サイズの縮小に対応したものです)。
<!-- You could use **average pooling or sum pooling**, but they aren’t common choices. 
Max pooling tends to perform better than both in practice. 
In max pooling, you’re taking the largest pixel value. 
In average pooling, you take the average of all the pixel values at that spot in the image. 
(Actually, there’s a trend now towards using smaller filters or discarding pooling layers entirely. 
This is in response to an aggressive reduction in representation size.)-->


<!-- なぜ最大プーリングを選択するのか、もう少し詳しく見てみましょう。
を選択する理由と、ストライドを2ピクセルにする理由をもう少し見てみたいと思いませんか？
[Dominik Scherer et. al, Evaluation of Pooling Operations in Convolutional Architectures for Object Recognitio
n](http://ais.uni-bonn.de/papers/icann2010_maxpool.pdf){:target="_blank"} をご覧ください。
-->
<!-- __Want to look a little more at why you might want to choose max pooling
and why you might prefer a stride of two pixels? Check out Dominik
Scherer et. al, [Evaluation of Pooling Operations in Convolutional
Architectures for Object Recognition](http://ais.uni-bonn.de/papers/icann2010_maxpool.pdf).__-->


[ここ](http://scs.ryerson.ca/~aharley/vis/conv/flat.html){:target="_blank"} に行くと、畳み込み層の実に面白い 2D 視覚化をチェックすることができます。
画面の左端のボックスに数字を描き、出力を見てみましょう。
畳み込み層とプール層、そして推測を見ることができます。
1 つの画像の 上にカーソルを置いてみると、フィルターが適用された場所がわかります。
<!-- If you go [here](http://scs.ryerson.ca/~aharley/vis/conv/flat.html) you can check out a really interestin
g 2D visualization of a convolutional layer. 
Draw a number in the box on the left-hand side of the screen and then really go through the output. 
You can see the  convolved and pooled layers as well as the guesses. 
Try hovering over a single pixel so you can see where the filter was applied.-->

<!-- So now we have an input image, an applied convolutional layer, and an applied pooling layer.

Let’s visualize the output of the pooling layer!

We were here:
-->
<center>
<img src="https://komazawa-deep-learning.github.io/assets/output3.jpg" width="49%">
</center>
<!-- 
The pooling layer takes as input the feature maps pictured above and reduces the dimensionality of those maps.
 
It does this by constructing a new, smaller image of only the maximum (brightest) values in a given kernel are
a.

See how the image has changed size?

-->
<center>
<img src="https://komazawa-deep-learning.github.io/assets/output4.jpg" width="88%">
</center>

<!-- Cool, right?

#### Flattening

This is a pretty simple step. You flatten the pooled feature map into a sequential column of numbers (a long v
ector). 
This allows that information to become the input layer of an artificial neural network for further processing.


#### Fully connected layer
At this step, we add an **artificial neural network** to our convolutional neural network. 
(Not sure about artificial neural networks? [You can learn about them here](https://towardsdatascience.com/sim
ply-deep-learning-an-effortless-introduction-45591a1c4abb)!)


The main purpose of the artificial neural network is to combine our features into more attributes. 
These will predict the classes with greater accuracy. This combines features and attributes that can predict c
lasses better.

At this step, the error is calculated and then backpropagated. 
The weights and feature detectors are adjusted to help optimize the performance of the model. 
Then the process happens again and again and again. 
This is how our network trains on the data! 

How do the output neurons work when there’s more than one?

First, we have to understand what weights to apply to the synapses that connect to the output. 
We want to know which of the previous neurons are important for the output.


If, for example, you have two output classes, one for a cat and one for a dog, a neuron that reads “0” is ablutely uncertain that the feature belongs to a cat. A neuron that reads “1 is absolutely certain that the feaure belongs to a cat. 
In the final fully connected layer, the neurons will read values between 0 and 1. 
This signifies different levels of certainty. 
A value of 0.9 would signify a certainty of 90%. 
The cat neurons that are certain when a feature is identified know that the image is a cat. 
They say the mathematical equivalent of, “These are my neurons! I should be triggered!” If this happens manyimes, the network learns that when certain features fire up, the image is a cat.


Through lots of iterations, the cat neuron learns that when certain features fire up, the image is a cat. 
The dog (for example) neuron learns that when certain other features fire up, the image is a dog. 
The dog neuron learns that for example again, the “big wet nose” neuron and the “floppy ear” neuron contri with a great deal of certainty to the dog neuron.
It gives greater weight to the “big wet nose” neuron and the “floppy ear” neuron. 
The dog neuron learns to more or less ignore the “whiskers” neuron and the “cat-iris” neuron. 
The cat neuron learns to give greater weight to neurons like “whiskers” and “cat-iris.”
(Okay, there aren’t actually “big wet nose” or “whiskers” neurons. 
But the detected features do have distinctive features of the specific class.)


Once the network has been trained, you can pass in an image and the neural network will be able to determine t
he image class probability for that image with a great deal of certainty.

The fully connected layer is a traditional Multi-Layer Perceptron. 
It uses a classifier in the output layer. 
The classifier is usually a softmax activation function. 
Fully connected means every neuron in the previous layer connects to every neuron in the next layer. 
What’s the purpose of this layer? To use the features from the output of the previous layer to classify the iput image based on the training data.

Once your network is up and running you can see, for example, that you have a 95% probability that your image 
is a dog and a 5% probability that your image is a cat.


Why do these numbers add up to 1.0? (0.95 + 0.05)

There isn’t anything that says that these two outputs are connected to each other. 
What is it that makes them relate to each other? 
Essentially, they wouldn’t, but they do when we introduce the **softmax function**.
This brings the values between 0 and 1 and makes them add up to 1 (100%). 
(You can read all about this on Wikipedia.) 
The softmax function takes a vector of scores and squashes it to a vector of values between 0 and 1 that add up to 1.

After you apply a softmax function, you can apply the loss function.
Cross entropy often goes hand in hand with softmax. 
We want to minimize the loss function so we can maximize the performance of our network.
At the beginning of backpropagation, your output values would be tiny.
That’s why you might choose cross entropy loss. 
The gradient would be very low and it would be hard for the neural network to start adjusting in the right direction. 
Using cross entropy helps the network assess even a tiny error and get to the optimal state faster.
-->
