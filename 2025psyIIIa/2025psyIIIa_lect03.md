---
title: 第03回 2025 年度開講 駒澤大学 心理学特講 IIIA
author: 浅川 伸一
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">
<div align="center">
<font size="+1" color="navy"><strong>ディープラーニングの心理学的解釈</strong></font><br/><br/>
</div>

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 25/Apr/2025<br/>
Appache 2.0 license<br/>
</div>


* [相貌失認 prosoagnosia](https://en.wikipedia.org/wiki/Prosopagnosia){:target="_blank"}，
* [パレイドリア](https://en.wikipedia.org/wiki/Pareidolia){:target="_blank"} ，
* シミュルクラ現象,

* Eigenface, Fisherface,
* Viola-Jones 

# 実習

* [DNN の特徴検出器視覚化<img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2021_1029Visualization_the_visual_features_on_CNN.ipynb){:target="_blank"}

* [ヴィオラ=ジョーンズ アルゴリズム(従来手法) による顔認識実験 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_0930viola_jones_ipynb.ipynb){:target="_blank"}
* [DOG などのフィルタと Harr 特徴による顔検出 a.k.a ビオラ＝ジョーンズ アルゴリズム<img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0528edge_and_face_detection_algorithm_not_cnn.ipynb){:target="_blank"}
* [いくつかの画像フィルタ 特徴点検出アルゴリズム<img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2020Sight_visit_feature_extractions_demo.ipynb){:target="_blank"}

* [顔，非顔判別データセットを用いた紡錘状回のモデル化 --- 転移学習を用いた顔検出モデル ---  <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_0925face_dataset_transfer_learning.ipynb){:target="_blank"}
    - Robust Real-Time Face Detection, Viola, P. and Jones, M. (2004)


# 本日のメニュー

1. 数式の読み方
2. 特徴検出器 feature detectors
3. One algorithm hypothesis


## 考え方，背景，キーワード

* 構成論的アプローチ vs 分析的アプローチ （人工知能と心理学との関係）
* 神は細部に宿る God is in the detail. あるいは 悪魔は細部に宿る (The devil is in the detail)
* [炭素排他主義 (Carbon chauvinism)](https://en.wikipedia.org/wiki/Carbon_chauvinism)
    * 炭素排他主義（Carbon Chauvinism）とは，知られている限り、炭素の化学的および熱力学的特性は、生物に使用される分子を形成する上で、他のすべての元素よりもはるかに優れていることから，地球外を含む全ての生命体の化学過程は，炭素（有機化合物）から構築されなければならないという仮定を軽蔑するための造語。
    * 人工知能は理論上，基礎となる物質が生物学的でないことから，感覚や知性を持ち得ないという考えを批判するためにも 炭素排他主義という言葉が使われる。

  <!-- - Carbon chauvinism is a neologism meant to disparage the assumption that the chemical processes of hypothetical extraterrestrial life must be constructed primarily from carbon (organic compounds) because as far as is known, carbon's chemical and thermodynamic properties render it far superior to all other elements at forming molecules used in living organisms.[1]
  The expression "carbon chauvinism" is also used to criticize the idea that artificial intelligence can't in theory be sentient or truly intelligent because the underlying matter isn't biological.[2] -->


- [Sutton のブログ，苦い教訓](/2019sutton_bitter_Lesson.pdf){:target="_blank"}

コンピュータビジョンにおいても，同様のパターンがある。
初期の手法では，視覚をエッジや一般化された円柱の探索，あるいは SIFT 特徴の観点から考えていた。
しかし今日では，このような考え方はすべて捨て去られている。
現代のディープラーニングニューラルネットワークは，畳み込みとある種の不変性という概念のみを使用し，はるかに優れた性能を発揮する。
<!--In computer vision, there has been a similar pattern.
Early methods conceived of vision as searching for edges, or generalized cylinders, or in terms of SIFT features.
But today all this is discarded. Modern deep-learning neural networks use only the notions of convolution and certain kinds of invariances, and perform much better.-->

これは大きな教訓である。
我々は同じような過ちを犯し続けている。
このことを理解し，それに効果的に抵抗するためには，我々はこうした間違いの魅力を理解しなければならない。
我々は，我々の考え方を構築しても長期的にはうまくいかないという苦い教訓を学ばなければならない。
この苦い教訓は，次のような歴史的観察に基づいている。
1) AI 研究者は，しばしばエージェントに知識を組み込もうとしてきた，
2) これは短期的には常に役に立ち，研究者を個人的に満足させた，
3) 長期的には，それは停滞し，さらなる進歩を阻害した，
4) 探索と学習による計算のスケーリングに基づく反対のアプローチによって，画期的な進歩がもたらされる，

最終的な成功は苦渋を帯びたものであり，しばしば不完全に消化される，
なぜなら，それは人間中心のアプローチに対する成功だからである。

<!--This is a big lesson.
As a field, we still have not thoroughly learned it, as we are continuing to make the s ame kind of mistakes.
To see this, and to effectively resist it, we have to understand the appeal of these mistakes.
We have to learn the bitter lesson that building in how we think we think does not work in the long run.
The bitter lesson is based on the historical observations that
1) AI researchers have often tried to build knowledge into their agents,
2) this always helps in the short term, and is personally satisfying to the researcher, but
3) in the long run it plateaus and even inhibits further progress, and
4) breakthrough progress eventually arrives by an opposing approach based on scaling computation by search and  learning.
The eventual success is tinged with bitterness, and often incompletely digested, because it is success over a
favored, human-centric approach.-->

## Sutton のブログより

<center>
<div style="text-align: left;width: 88%;background-color: powderblue;">
人工知能の長年の目標は，困難な領域でも超人的な能力をタブラ・ラサ方式で学習するアルゴリズムである。
最近では AlphaGo が囲碁の世界チャンピオンを破った初めてのプログラムとなった。
AlphaGo の木探索は，深層ニューラルネットワークを用いて局面の評価と手の選択を行う。
このニューラルネットワークは，人間の熟練した手からの教師付き学習と， 自分自身の競技からの強化学習によって訓練されている。
ここでは，人間のデータやガイダンス，ゲームルール以外の領域の知識を必要としない，強化学習のみに基づいたアルゴリズムを導入する。
AlphaGo は自分自身の教師となり AlphaGo 自身の手の選択や AlphaGo のゲームの勝敗を予測するようにニューラルネットワークが学習される。
このニューラルネットワークは，木探索の強度を向上させ，その結果，より質の高い手の選択が可能となり，次の反復ではより強力な自己対戦が可能となる。
タブララサからスタートした私たちの新しいプログラム AlphaGo Zero は，既発表のチャンピオンに敗れた AlphaGo に対して 100-0 で勝利するという超人的な成績を達成した。
</div>
</center>

* [David Silver homepage](https://www.davidsilver.uk/){:target="_blank"}

1. [計算論的認知神経科学 Kriegeskorte and Douglas, 2018, Cognitive computational neuroscience](https://project-ccap.github.io/2018Kriegeskorte_Douglas_Cognitive_Computational_Neuroscience.pdf){:target="_blank"}
1. [視覚系の畳み込みニューラルネットワークモデル，過去現在未来 Lindsay, 2020, Convolutional Neural Networks as a Model of the Visual System: Past, Present, and Future](https://project-ccap.github.io/2020Lindsay_Convolutional_Neural_Networks_as_a_Model_of_the_Visual_System_Past_Present_and_Future.pdf){:target="_blank"}
1. [計算論的視覚と正則化理論 Poggio, Torre, Koch, 1985](https://komazawa-deep-learning.github.io/2021cogpsy/1985Poggio_Computational_Vision_and_Regularization_Theory.pdf){:target="_blank"}
1. [皮質における物体認識の階層モデル Riesenhuber and Poggio (1999) Nature](https://komazawa-deep-learning.github.io/2021cogpsy/1999Riesenhuber_Poggio_Hierarchical_models_of_object_recognition_in_cortex.pdf){:target="_blank"}
