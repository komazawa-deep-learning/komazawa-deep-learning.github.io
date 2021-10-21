---
title: 第06回
layout: home
---

# 7. ネオコグニトロン (Fukushima, 1980)

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

# 8. LeNet5 (LeCun, 1998)

- **LeNet**. Yann LeCun (現 Facebook AI 研究所所長)による CNN 実装
[LeNet](http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf){:target="_blank"} 手書き数字認識
 
<center>
<img src="/assets/1998LeNet5.png" width="88%">
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

# 9. 畳み込みニューラルネットワーク CNN

畳み込みニューラルネットワークは，ネオコグニトロンを先祖にした現在のニューラルネットワークによる画像認識の基礎モデルです。

## 9.1 CNN の特徴

<!--[@2017Asakawa_deep_jps][^2017Aakawa\_deep\_jps\]-->。

1.  畳込み演算 (convolutional operation)
1.  非線形活性化関数 (nonlinear activation functions)
3.  プーリング処理 (pooling)
4.  データ拡張 (data augmentation)
5.  バッチ正規化 (batch normalization)
6.  ショートカット(shortcut) あるいは スキップ結合
7. ドロップアウト (dropout)
8.  GPU の使用


* カーネル, ストライド，ダイアレーション，勾配消失問題，整流線形化関数 (ReLU),
* 完全結合層，交差エントロピー損失
* データ拡張 data augumentation
* 転移学習 transfer learning 

<center>
    <iframe src="/2021/conv-demo/index.html" width="140%" height="640px;" style="border:none;"></iframe>

</center>


## 9.2 ディープラーニングの短所

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


# 10. 最大値プーリングの生理学的根拠

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


# 11. 生理学，視覚心理学との対応

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

# 11. 転移学習

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
The softmax function takes a vector of scores and squashes it to a vector of values between 0 and 1 that add u
p to 1.

After you apply a softmax function, you can apply the loss function.
Cross entropy often goes hand in hand with softmax. 
We want to minimize the loss function so we can maximize the performance of our
network.
At the beginning of backpropagation, your output values would be tiny.
That’s why you might choose cross entropy loss. 
The gradient would be very low and it would be hard for the neural network to start adjusting in the right dir
ection. 
Using cross entropy helps the network assess even a tiny error and get to the optimal state faster.

 -->
