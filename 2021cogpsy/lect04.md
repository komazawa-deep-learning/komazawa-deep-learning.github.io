---
title: 第04回
layout: home
---

- キーワード: レチノトピー retinotopy，ソマトピー somatopy, トノトピー tonotopy
- ワン・アルゴリズム仮説, 
- [苦い教訓 (2019) Sutton](https://komazawa-deep-learning.github.io/2021cogpsy/2019Sutton_Bitter_Lesson.pdf){:target="_blank"}

- Neural prosthesis, neural implants 
	- World's first brain prosthesis revealed 9:00 12 March 2003 by Duncan Graham Rowe
	http://www.technologyreview.com/featuredstory/514006/regaining-lost-brainfunction/
	Regaining Lost Brain Function By Susan Young Rojahn on April 23, 2013

	Our Amazingly Plastic Brains Mental and physical exercise can keep the brain fit and help it recover capacities lost to disease and trauma 
	http://www.wsj.com/articles/our-amazingly-plastic-brains-1423262095 2015年02月15日閲覧 By NORMAN DOIDGE 

	http://www.33rdsquare.com/2013/03/theodore-berger-on-neuro-engineering.html 2015年01月31日閲覧
	Theodore Berger On Neuro Engineering https://www.youtube.com/watch?v=kJsfQTcBhAM

	脳損傷によって失われた運動機能を肩代わりする脳の変化を解明 http://www.aist.go.jp/aist_j/press_release/pr2015/pr20150107/pr20150107.html 2015年02月02日閲覧 －脳から学んだリハビリの開発につながる発見－

	Future of Neuroscience
Later this year, Dr. Theodore Berger is slated to be a featured speaker at the GF2045 -
Global Futures 2045 International Congress in New York. Dr. Berger's work involves
recreating functions of the brain in silicon, with the aim of one day restoring and
enhancing neurological function in human beings.
Read more: http://www.33rdsquare.com/2013/03/theodore-berger-on-neuroengineering.html#ixzz3QMIpk4DK


<iframe width="640" height="360" src="https://www.youtube.com/embed/kJsfQTcBhAM"
frameborder="0" allowfullscreen></iframe>
Future of Neuroscience

Sur ら (1988) は，フェレット（西洋イタチ）の 聴覚信号と視覚信号との中継核，膝状体 で信号を入れ替える実験を行っ
た。
すなわち，聴覚信号が視覚野へ入力され，逆に視覚信号が聴覚野への入力となるように外科手術を行った。
結果，本来聴覚信号を処理すべき聴覚野ニューロンでは，視覚刺激に応答する反応が観察され，
本来視覚信号を処理すべき視覚野ニューロンでは，聴覚刺激に応答する反応が観察された。

<center>
   <img src="/assets/1988Sur_Fig1upper.svg" style="width:44%">
   <img src="/assets/1988Sur_Fig1lower.svg" style="width:44%"><br/>
<div style="text-align: left; width:94%; background-color: cornsilk;">
実験の概略 Sur (1988) Fig. 1 
</div>  
</center>

<center>
<img src="/assets/1988Sur_fig2.jpg" width="74%"><br/>
<div style="text-align: left; width:94%; text-color:cornsilk">
聴覚視床への実験的に誘導された網膜投影（ハッチングされた領域）および聴覚視床と聴覚皮質の接続。
手術した半球とは反対側の眼は、生き残っている背側LGN（LGd）と腹側LGN（LGv）、およびMGNの背側と腹側の区画内のパッチ（それぞれMGdとMG）に投影する。
視床の傍矢状切片を番号付きで示す。
視床の傍矢状切片の 同じ動物に、一次聴覚野（Al）にHRPを注入した場合（注入部位は左上に示す）、細胞が充填される。
ドットで示されている）MG "MGdでは逆行性に、MGvでは後遺症複合体の側方分裂（P01）が行われている。MGd と MGv の多くの細胞が網膜突起帯を覆っている。 
Sur (1988) Fig. 2
</div>
</center>

<center>
<img src="/assets/1988Sur_Fig4.svg" style="width:94%"><br/>
<div style="text-align: left; width:88%; background-color:cornsilk">
  結果: Sur (1988) Fig. 4 
</div>
</center>

- Hinton's words about AI
  * __speech for the IEEE/RSE Wolfson James Clerk Maxwell Award.__

> 50年前，人工知能の父たちは論理こそが知性の鍵である確信していた。コンピュータに論理推論をさせることこそが必要であると考えた。
論理ではなく，脳のネットワーク(訳注:現在のニューラルネットワーク)がどのように学習するのかを理解することはクレージーなアプローチであると考えた。
奇妙なことに、論理に基づいたAIへのアプローチを拒否した2人が、アラン・チューリングとフォン・ノイマンであった。
彼らが生きていたら、様子は違っていただろうと思う。
現在は，ニューラルネットワークはどこにでもあるありふれたものとなり，クレージーなアプローチが勝利しているのだ。

<!-- 
50 years ago, the fathers of artificial intelligence convinced everybody that logic was the key to intellige nce. 
Somehow we had to get computers to do logical reasoning.  
The alternative approach, which they thought was crazy, was to forget logic and try and understand how networks of brain cells learn things. 
Curiously, two people who rejected the logic based approach to AI were Turing and Von Neumann. 
If either of them had lived I think things would have turned out differently... now neural networks are everywhere and the crazy approach is winning.
-->

# 1. ヒューベルとウィーゼルによる視覚野の生理学研究

<center>
<img src="/assets/1968Hubel_Wiesel_1.svg" style="width:49%"><br/>
Hubel と Wiesel (1959, 1962, 1968) の実験の模式図
</center>

<center>
<img src="/assets/1968Hubel_Wiesel_2.svg" style="width:49%"><br/>
Hubel と Wiesel の実験結果 (Hubel & Wiesel, 1968 の Fig.2.7をトレーシングしたもの
</center>


* [実習 2 いくつかの画像フィルタ 特徴点検出アルゴリズム<img src="https://raw.githubusercontent.com/komazawa-deep-learning/komazawa-deep-learning.github.io/8ff17b2977309e5943f512b6d10b76ac0cddbbe3/assets/colab_icon.svg">]
(https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2020Sight_visit_feature_extractions_demo.ipynb){:target="_blank"}

* [実習 3 DOG などのフィルタと Harr 特徴による顔検出 a.k.a ビオラ＝ジョーンズ アルゴリズム<img src="https://raw.githubusercontent.com/komazawa-deep-learning/komazawa-deep-learning.github.io/8ff17b2977309e5943f512b6d10b76
ac0cddbbe3/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0528edge_and_face_detection_algorithm_not_cnn.ipynb){:target="_blank"}


```python
import matplotlib.pyplot as plt
%matplotlib inline
from torchvision import models
resnet = models.resnet18(pretrained=True)

# 30 行 30 列目の結合荷重を視覚化する
plt.imshow(resnet.layer4[0].conv1.weight.detach().numpy()[30,30], cmap='gray')
plt.title('resent layer 4')
plt.show()

print(resnet_model.layer1[0].conv1.weight.detach().numpy().shape) 
print(resnet_model.conv1.weight.detach().numpy().shape)

for name, param in resnet_model.named_parameters():
    print(name, type(param))

alexnet = models.alexnet(pretrained=True)
alex0 = alexnet.features[0].weight.detach().numpy()
plt.imshow(alex0[3,0], cmap='gray')
plt.title('alexnet features0')
plt.show()

for name, param in alexnet.named_parameters():
    print(name, type(param))
    
# 第 1 層は入力画像が 3 チャンネルの色情報 r,g,b を持っているはずである。
# 従って，色の情報を見ることが可能である。
# 以下サンプルコード
alexnet = models.alexnet(pretrained=True)

#  AlexNet の最初の中間層の重み係数を取り出して numpy 配列に格納
alex0 = alexnet.features[0].weight.detach().numpy()

# 第 n 番目の結合係数を表示させたいのかを決める
n = 7
plt.imshow(np.clip(alex0[n].transpose(1,2,0),0,1))
plt.show()
```

## MLPの問題点

1. **勾配消失問題** gradient vanishing problem
2. **責任割当問題** credit assignment problem

これら２点の問題を解決する諸手法を元に多層化ニューラルネットワークが構成される。
総称して **深層学習 deep learning** と呼ばれる。


# 2. ネオコグニトロン (Fukushima, 1980)

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

# 3. LeNet5 (LeCun, 1998)

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

<iframe src="../2021/conv-demo/index.html" width="140%" height="640px;" style="border:none;"></iframe>

<!--
## [TensorFlow HUB](https://www.tensorflow.org/hub){:target="_blank"}
-->

- ドロップアウト，データ拡張，各種正規化: cnn.md
- 有名なモデル LeNet，Alex Net，Inception，VGG，ResNet
- R-CNN，ハイウェイネット，YOLO，SSD
- セマンティックセグメンテーション
- 転移学習，事前学習，ファインチューニング
- GAN

### インセプション Inception，残渣ネット ResNet，領域 R-CNN (Regional Convolutional Neural Networks)
- what and where routes
- 心理学的対応物(？)
  - Cadieu (2014) Deep Neural Networks Rival the Representation of Primate IT Cortex for Core Visual Object Re
cognition
  - Nasr, Viswanathan, Nieder (2019) Number detectors spontaneously emerge in a deep neural network designed f
or visual object recognition
  - Marcus (2018) Deep Learning A Critical Appraisal
- 転移学習

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


<center>
<img src='https://cdn-images-1.medium.com/max/1280/1*sS_WZM4GLS88XlnDLKcZ-g.png' style='width:94%'><br>
from [A guide to Face Detection in Python](https://towardsdatascience.com/a-guide-to-face-detection-in-python-
3eab0f6b9fc1)
</center>

- [The Complete Beginner’s Guide to Deep Learning: Convolutional Neural Networks and Image Classification](https://towardsdatascience.com/wtf-is-image-classification-8e78a8235acb){:target="_blank"}, Anne Bonner Feb.  02

- 畳込みニューラルネットワーク (Convlutional Neural Networks:CNN) とは画像認識におけるゲームチェンジャー(以後画像認識，ビデオ分類，自動運転，ドローン，ゲームなどへの応用多数)
- [イメージネット画像コンテスト](http://image-net.org/challenges/LSVRC/){:target="_blank"} では，分類 (classification) 課題と位置 (locallization) 課題とからなる。
- コンテストは 2010 年から Li Fei-Fei さん中心となって [AMT](https://www.mturk.com/) で画像のアノテーションを行って 画像を2012 年の優勝チームが CNN を使った。通称[アレックスネット](https://papers.nips.cc/paper/4824-imag
enet-classification-with-deep-convolutional-neural-networks.pdf){:target="_blank"}
- [スタンフォード大学の授業 CS231n: Convolutional Neural Networks for Visual Recognition](http://cs231n.stanford.edu/index.html){:target="_blank"}. 
[スライド](http://cs231n.stanford.edu/slides/2019/cs231n_2019_lecture05.pdf){:target="_blank"}

# さらなる情報

- Math? [Introduction to Convolutional Neural Networks](https://web.stanford.edu/class/cs231a/lectures/intro_cnn.pdf) by Jianxin Wu
- C.-C. Jay Kuo [Understanding Convolutional Neural Networks With a Mathematical Model](https://arxiv.org/abs/1609.04112).
- [the absolute basics of activation functions, you can find that here](https://towardsdatascience.com/simply-deep-learning-an-effortless-introduction-45591a1c4abb)
- [Artificial neural networks? [You can learn about them here](https://towardsdatascience.com/simply-deep-learning-an-effortless-introduction-45591a1c4abb)


## 正規化，正則化，標準化，白色化，二重中心化

- 白色化については平井有三先生のパターン認識が参考文献で良いかな

- [Differences between normalization, standardization and regularization](https://maristie.com/blog/differences-between-normalization-standardization-and-regularization/)

---

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
**トレーニングデータとテストデータは必ず別々にしましょう。
トレーニングデータでテストを行うと、ネットワークはその情報を記憶してしまいます。
トレーニングしたデータでテストを行うと、ネットワークは情報を記憶してしまいます！新しいデータを導入すると、ひど
い結果になるでしょう。
<!-- Without variance, your network will be useless with images that don’t exactly match the training data. 
**Always, always, always keep your training and testing data separate**! 
If you test with the data you trained on, your network has the information memorized! 
It will do a terrible job when it’s introduced to any new data.  -->


### Overfitting is not cool.

つまり、このステップでは、**特徴地図** を取得し、**プーリング層** を適用して、**プール済特徴地図** を作成します。
<!-- So for this step, you take the **feature map**, apply a **pooling layer**, and the result is the **pooled feat
ure map**.-->


プーリングの最も一般的な例は、**最大値プーリング** (またはマックスプーリング) です。
最大値プーリングでは、入力画像を重ならない領域のセットに分割します。
各エリアの出力は、各エリアの最大値となります。
これにより、少ないパラメータで小さなサイズになります。
<!-- The most common example of pooling is **max pooling**. 
In max pooling, the input image is partitioned into a set of areas that don’t overlap. 
The outputs of each area are the maximum value in each area. 
This makes a smaller size with fewer parameters. -->

<!-- マックスプーリングとは、画像の各スポットで最大値を掴むことです。
これにより、特徴ではない 75％ の情報を取り除くことができます。
ピクセルの最大値を取ることで、歪みを考慮することができます。
特徴が左や右に少し回転しても、プールされた特徴は同じになります。サイズやパラメータを小さくしているのですね。
これは、モデルがその情報に対してオーバーフィットしないことを意味するので、素晴らしいことです。
Max pooling is all about grabbing the maximum value at each spot in the image. 
This gets rid of 75% of the information that is not the feature. 
By taking the maximum value of the pixels, you’re accounting for distortion. 
If the feature rotates a little to the left or right or whatever, the pooled feature will be the same. You’rereducing the size and parameters. 
This is great because it means that the model won’t overfit on that information.-->

<!-- **平均プーリング** または **合計プーリング** を使用することもできますが、一般的な選択肢ではありません。
実際には、最大プーリングの方が両者よりも性能が良い傾向にあります。
最大プーリングでは、最大のピクセル値を取ることになります。
平均プーリングでは、画像のその場所にあるすべてのピクセル値の平均を取ります。
実際には、より小さなフィルターを使ったり、プーリングレイヤーを完全に破棄したりする傾向があります。
これは、積極的な表現サイズの縮小に対応したものです)。
 -->
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


[ここ](http://scs.ryerson.ca/~aharley/vis/conv/flat.html){:target="_blank"} に行くと、畳み込み層の実に面白い 2
D 視覚化をチェックすることができます。
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
