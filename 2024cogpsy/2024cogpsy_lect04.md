---
title: "第04回 2024年度開講 駒澤大学 認知心理学研究"
author: "浅川 伸一"
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="right">
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 11/Oct/2024<br/>
Appache 2.0 license<br/>
</div>

$$
\newcommand{\of}[1]{\left(#1\right)}
\newcommand{\Of}[1]{\left[#1\right]}
\newcommand{\KL}[2]{\operatorname{KL}\left(\left.{#1}\right\|{#2}\right)}
\newcommand{\given}[1]{\left|{#1}\right.}
\newcommand{\mb}[1]{\mathbf{#1}}
$$

## 本日のメニュー

1. Hopfield and Hinton Novel Prize in Physics 受賞記念
2. 機械学習モデルと心理学，生理学モデル
3. Git のインストール
4. 機械学習モデルの説明，ロジスティック回帰，k-means, SVM, 判別分析
5. [Python の基礎](python_numpy_intro_ja)
6. [フレームワーク](/eco/)
7. CNN

## コード

* [Python の基礎 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_1011python_primers.ipynb){:target="_blank"}
* [Karapetian+(2023) データによるデモ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_1011Karapetian_demo.ipynb){:target="_blank"}
* [誤差逆伝播と注意を組み合わせたトップダウンネットワーク Abel &Ullman(2023) Top-Down Network Combines Back-Propagation with Attention <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_0105royabel_BU_TD_multi_mnist.ipynb){:target="_blank"}


<!--
<div class="memo">
クリストフ・コロンブスのアメリカ発見について，そもそも彼の偉大な点はどこにあるか，ということをきく人があるならば，それは西回りのルートでインドへ旅行するのに，地球が球形であることを利用するというアイディアではなかった，と答えなければならないだろう。
このアイディアはすでに他の人々によって考えられたものであったし，彼の探検の慎重な準備，船の専門的な装備などということでもなかった。
それらのことは，他の人でもやろうとすればやれたに違いない。
そうではなくて，この発見的航海で最も困難であったことは，既知の陸地を完全に離れ，残余の貯えでは引き返すことがもはや不可能であった地点から，さらに西へ西へと船を走らせるという決心であったに違いない。<br>
<div style="text-align:right">「部分と全体」ハイゼンベルク，山崎和夫訳，みすず書房，p.115，「VI 新世界への出発 1926-1927年」冒頭部</div>
</div> -->

# 1. [Hopfield and Hinton, Nobel Prize in Physics 2024 受賞記念](https://www.nobelprize.org/prizes/physics/2024/popular-information/){:target="_blank"}

今年の受賞者は，物理学のツールを活用して，今日の強力な機械学習の基礎を築くのに役立つ手法を構築した。
ホップフィールドは，情報を保存し再構築できる構造を考案した。
ヒントンは，データから独自に特性を発見できる手法を発明し，現在使用されている大規模な人工ニューラルネットワークにとって重要なものとなった。
<!-- This year’s laureates used tools from physics to construct methods that helped lay the foundation for today’s powerful machine learning.
John Hopfield created a structure that can store and reconstruct information.
Geoffrey Hinton invented a method that can independently discover properties in data and which has become important for the large artificial neural networks now in use. -->

### 彼らは物理学を用いて情報のパターンを見つけ出した<!-- They used physics to find patterns in information-->

多くの人が，コンピュータが言語を翻訳したり，画像を解釈したり，さらにはそれなりの会話を行うことができることを経験している。
しかし，おそらくあまり知られていないのは，この種のテクノロジーが膨大なデータの分類や分析など，研究において長い間重要な役割を果たしてきたということだ。
機械学習は過去15～20年で爆発的に発展し，人工ニューラルネットワークと呼ばれる構造を利用している。
今日，人工知能について語る場合，この技術を指すことが多い。
<!-- Many people have experienced how computers can translate between languages, interpret images and even conduct reasonable conversations.
What is perhaps less well known is that this type of technology has long been important for research, including the sorting and analysis of vast amounts of data.
The development of machine learning has exploded over the past fifteen to twenty years and utilises a structure called an artificial neural network.
Nowadays, when we talk about artificial intelligence, this is often the type of technology we mean. -->

コンピュータは思考することができないが，記憶や学習といった機能は模倣することができる。
今年のノーベル物理学賞受賞者たちは，これを可能にした。
物理学の基本的な概念と手法を用いて，ネットワークの構造を利用して情報を処理する技術を開発した。
<!-- Although computers cannot think, machines can now mimic functions such as memory and learning.
This year’s laureates in physics have helped make this possible. Using fundamental concepts and methods from physics, they have developed technologies that use structures in networks to process information. -->

機械学習は，レシピのような従来のソフトウェアとは異なる。
ソフトウェアはデータを受け取り，明確な説明に従って処理を行い，結果を生成する。これは，誰かが材料を集め，レシピに従ってそれらを処理し，ケーキを作るのとよく似ている。
これに対し，機械学習ではコンピュータが例から学習し，段階的な指示では管理できないほど曖昧で複雑な問題にも取り組むことができる。その一例が，画像を解釈してその中に含まれる物体を識別することである。
<!--Machine learning differs from traditional software, which works like a type of recipe.
The software receives data, which is processed according to a clear description and produces the results, much like when someone collects ingredients and processes them by following a recipe, producing a cake.
Instead of this, in machine learning the computer learns by example, enabling it to tackle problems that are too vague and complicated to be managed by step by step instructions. One example is interpreting a picture to identify the objects in it. -->

#### 脳を模倣する<!-- #### Mimics the brain-->

人工ニューラルネットワークは，ネットワーク構造全体を使用して情報を処理する。
当初の着想は，脳の仕組みを理解したいという欲求から生まれた。
1940 年代には，研究者たちは脳のニューロンとシナプスのネットワークの基礎となる数学について推論を始めていた。
また，神経科学者ドナルド・ヘッブが，ニューロン間の接続が連携して機能するときに強化されるという学習の発生に関する仮説を立てたことで，心理学からも新たな知見がもたらされた。
<!-- An artificial neural network processes information using the entire network structure.
The inspiration initially came from the desire to understand how the brain works.
In the 1940s, researchers had started to reason around the mathematics that underlies the brain’s network of neurons and synapses.
Another piece of the puzzle came from psychology, thanks to neuroscientist Donald Hebb’s hypothesis about how learning occurs because connections between neurons are reinforced when they work together. -->

その後，これらの考え方は，人工ニューラルネットワークをコンピュータシミュレーションとして構築することで，脳のネットワークの機能を再現しようとする試みに引き継がれた。
この場合，脳のニューロンは異なる値を持つノードで模倣され，シナプスはノード間の接続で表され，その接続は強くなったり弱くなったりする。
ドナルド・ヘッブの仮説は，訓練と呼ばれる処理を通じて人工ネットワークを更新する際の基本的な学習則の一つとして，現在でも使用されている。
<!--Later, these ideas were followed by attempts to recreate how the brain’s network functions by building artificial neural networks as computer simulations.
In these, the brain’s neurons are mimicked by nodes that are given different values, and the synapses are represented by connections between the nodes that can be made stronger or weaker.
Donald Hebb’s hypothesis is still used as one of the basic rules for updating artificial networks through a process called training. -->

<div class="figcenter">
<img src="https://www.nobelprize.org/uploads/2024/10/popular-physicsprize2024-figure2-2-1024x530.jpg" style="width:77%">
</div>

1960 年代の終わりには，いくつかの期待外れの理論的結果により，多くの研究者がこれらのニューラルネットワークが実用化されることはないだろうと疑うようになった。
しかし，人工ニューラルネットワークへの関心は1980年代に再び高まり，その年に受賞した研究者たちの研究を含むいくつかの重要なアイデアが注目を集めた。
<!-- At the end of the 1960s, some discouraging theoretical results caused many researchers to suspect that these neural networks would never be of any real use.
However, interest in artificial neural networks was reawakened in the 1980s, when several important ideas made an impact, including work by this year’s laureates. -->

#### 連想記憶<!-- #### Associative memory-->

映画館や講堂でよく見かける傾斜した床を表す言葉など，めったに使わないかなり変わった単語を思い出そうとしているとしよう。
記憶をたどってみる。
Ramp..., rad...idal? いや rake だ!
<!--ランプのようなもの…ラジアル…？いや，それじゃない。
レーキだ！
Imagine that you are trying to remember a fairly unusual word that you rarely use, such as one for that sloping floor often found in cinemas and lecture halls.
You search your memory.
It’s something like ramp… perhaps rad…ial? No, not that.
Rake, that’s it! -->

適切な単語を見つけるために類似した単語を探索するこのプロセスは，物理学者ジョン・ホップフィールドが1982年に発見した連想記憶を彷彿とさせる。
ホップフィールド・ネットワークはパターンを保存でき，それを再現する方法も備えている。
ネットワークに不完全なパターンやわずかに歪んだパターンが与えられると，その方法によって最も類似した保存パターンを見つけることができる。
<!-- This process of searching through similar words to find the right one is reminiscent of the associative memory that the physicist John Hopfield discovered in 1982.
The Hopfield network can store patterns and has a method for recreating them.
When the network is given an incomplete or slightly distorted pattern, the method can find the stored pattern that is most similar. -->

ホップフィールドは以前，物理学のバックグラウンドを活かして分子生物学の理論的な問題を研究していた。
神経科学に関する会議に招かれた際，彼は脳の構造に関する研究に出会った。
彼はそこで学んだことに魅了され，単純な神経ネットワークの力学について考え始めた。
ニューロンが同時に作用すると，ネットワークの個々の構成要素だけを見ている人には見えない，新しい強力な特性が生み出される可能性がある。
<!-- Hopfield had previously used his background in physics to explore theoretical problems in molecular biology.
When he was invited to a meeting about neuroscience he encountered research into the structure of the brain.
He was fascinated by what he learned and started to think about the dynamics of simple neural networks.
When neurons act together, they can give rise to new and powerful characteristics that are not apparent to someone who only looks at the network’s separate components. -->

1980年，ホップフィールドはプリンストン大学を辞し，大陸を横断した。
南カリフォルニアのパサデナにあるカリフォルニア工科大学（Caltech）の化学・生物学の教授職のオファーを受けたのだ。
同大学では，ニューラルネットワークに関する自身のアイデアを開発するための無料実験に利用できるコンピューターリソースを利用することができた。
<!-- In 1980, Hopfield left his position at Princeton University, where his research interests had taken him outside the areas in which his colleagues in physics worked, and moved across the continent.
He had accepted the offer of a professorship in chemistry and biology at Caltech (California Institute of Technology) in Pasadena, southern California.
There, he had access to computer resources that he could use for free experimentation and to develop his ideas about neural networks.-->

しかし，彼は物理学の基礎を捨てたわけではなく，そこから，多数の小さな部品が連携して機能するシステムが，新しい興味深い現象を生み出す仕組みについての理解を得た。
特に，原子スピンによって特殊な特性を持つ磁性材料について学んだことは有益であった。
隣接する原子のスピンは互いに影響し合うため，同じ方向のスピンを持つドメインを形成することができる。
彼は，スピンが互いに影響し合うことで物質がどのように発展するかを説明する物理学を利用して，ノードと接続からなるモデルネットワークを作成することができた。
<!--However, he did not abandon his foundation in physics, where he found inspiration for his under­standing of how systems with many small components that work together can give rise to new and interesting phenomena.
He particularly benefitted from having learned about magnetic materials that have special characteristics thanks to their atomic spin – a property that makes each atom a tiny magnet.
The spins of neighbouring atoms affect each other; this can allow domains to form with spin in the same direction.
He was able to make a model network with nodes and connections by using the physics that describes how materials develop when spins influence each other. -->

#### ネットワークは画像の景観を保存する<!-- #### The network saves images in a landscape-->

ホップフィールドが構築したネットワークは，強度の異なる接続によって結合されたノードで構成されている。
各ノードは個別の値を保存することができ，ホップフィールドの最初の研究では，白黒写真のピクセルのように，0または1のいずれかを保存することができた。
<!--The network that Hopfield built has nodes that are all joined together via connections of different strengths.
Each node can store an individual value – in Hopfield’s first work this could either be 0 or 1, like the pixels in a black and white picture. -->

ホップフィールドは，物理学におけるスピン系のエネルギーに相当する特性を用いてネットワークの全体的な状態を説明した。エネルギーは，ノードのすべての値と，それらの間の接続のすべての強度を使用する数式を用いて計算される。
ホップフィールドネットワークは，ノードに供給される画像によってプログラムされ，ノードには黒（0）または白（1）の値が与えられる。
次に，保存された画像のエネルギーが低くなるように，エネルギー式を用いてネットワークの接続が調整される。
別のパターンがネットワークに送られると，ノードを一つずつ順に調べ，そのノードの値が変更された場合にネットワークのエネルギーが低くなるかどうかを確認するルールがある。
黒いピクセルが白に置き換えられるとエネルギーが低くなることが判明した場合，色が変更される。
この手順は，これ以上改善が見込めなくなるまで続けられる。この段階に達すると，ネットワークは学習に使用された元の画像を再現していることが多い。
<!-- Hopfield described the overall state of the network with a property that is equivalent to the energy in the spin system found in physics; the energy is calculated using a formula that uses all the values of the nodes and all the strengths of the connections between them.
The Hopfield network is programmed by an image being fed to the nodes, which are given the value of black (0) or white (1).
The network’s connections are then adjusted using the energy formula, so that the saved image gets low energy.
When another pattern is fed into the network, there is a rule for going through the nodes one by one and checking whether the network has lower energy if the value of that node is changed.
If it turns out that energy is reduced if a black pixel is white instead, it changes colour.
This procedure continues until it is impossible to find any further improvements. When this point is reached, the network has often reproduced the original image on which it was trained.-->

これは，1つのパターンだけを保存する場合はそれほど目立たないかもしれない。
おそらく，画像そのものを保存して，それをテスト中の別の画像と比較すればいいのに，と思うかもしれないが，ホップフィールドの方法は特殊で，同時に複数の画像を保存でき，ネットワークは通常，それらの画像を区別することができる。
<!-- This may not appear so remarkable if you only save one pattern.
Perhaps you are wondering why you don’t just save the image itself and compare it to another image being tested, but Hopfield’s method is special because several pictures can be saved at the same time and the network can usually differentiate between them. -->

ホップフィールドは，ネットワークに保存された状態を検索することを，摩擦により動きが遅くなる山と谷の風景の中をボールが転がっていくことに例えた。
ボールが特定の場所に落とされた場合，ボールは最も近い谷に転がり落ちてそこで止まる。
ネットワークに保存されたパターンのいずれかに近いパターンが与えられた場合，同様に，エネルギー地形の谷底に到達するまで前進し続けるため，最も近いパターンを記憶の中から見つけることができる。
<!-- Hopfield likened searching the network for a saved state to rolling a ball through a landscape of peaks and valleys, with friction that slows its movement.
If the ball is dropped in a particular location, it will roll into the nearest valley and stop there.
If the network is given a pattern that is close to one of the saved patterns it will, in the same way, keep moving forward until it ends up at the bottom of a valley in the energy landscape, thus finding the closest pattern in its memory. -->

ホップフィールド・ネットワークは，ノイズを含むデータや一部が消去されたデータの再作成にも使用できる。
<!--The Hopfield network can be used to recreate data that contains noise or which has been partially erased. -->

<div class="figcenter">
<img src="https://www.nobelprize.org/uploads/2024/09/popular-physicsprize2024-figure3-1024x657.jpg" style="width:55%">
</div>

ホップフィールドやその他の研究者たちは，ホップフィールド・ネットワークの機能の詳細を開発し続けている。
その中には，0 や 1 以外のあらゆる値を保存できるノードも含まれる。
ノードを画像の画素と考えると，黒や白だけでなく，さまざまな色を持つことができる。
改良された方法により，より多くの画像を保存し，それらが非常に似通っている場合でも区別することが可能になった。
多くのデータ点から構築されている限り，あらゆる情報を識別または再構築することが可能である。
<!-- Hopfield and others have continued to develop the details of how the Hopfield network functions, including nodes that can store any value, not just zero or one.
If you think about nodes as pixels in a picture, they can have different colours, not just black or white.
Improved methods have made it possible to save more pictures and to differentiate between them even when they are quite similar.
It is just as possible to identify or reconstruct any information at all, provided it is built from many data points. -->

#### 19 世紀の物理学を用いた分類<!-- #### Classification using nineteenth-century physics-->

画像を想起することはできるが，それが何を表しているかを解釈するには，もう少し必要だ。
<!-- Remembering an image is one thing, but interpreting what it depicts requires a little more. -->

幼い子供でも，さまざまな動物を指さして，それが犬なのか，猫なのか，リスなのかを自信を持って言うことができる。
時には間違えることもあるが，すぐにほとんどの場合正しく言えるようになる。子供は，図や種や哺乳類といった概念の説明を見なくても，これを学ぶことができる。
それぞれの種類の動物の例をいくつか見れば，子供たちはすぐに異なるカテゴリーを理解する。
人は，猫を認識したり，言葉を理解したり，部屋に入って何かが変わったことに気づいたりするが，それは周囲の環境を経験することによってである。
<!-- Even very young children can point at different animals and confidently say whether it is a dog, a cat, or a squirrel.
They might get it wrong occasionally, but fairly soon they are correct almost all the time. A child can learn this even without seeing any diagrams or explanations of concepts such as species or mammal.
After encountering a few examples of each type of animal, the different categories fall into place in the child’s head.
People learn to recognise a cat, or understand a word, or enter a room and notice that something has changed, by experiencing the environment around them. -->

ホップフィールドが連想記憶に関する論文を発表した当時，ジェフリー・ヒントンは米国ピッツバーグのカーネギーメロン大学で働いていた。 彼はそれ以前に，英国とスコットランドで実験心理学と人工知能を研究しており，機械が人間と同様にパターン処理を学習し，情報を分類し解釈するための独自のカテゴリーを見つけ出すことができるかどうかを考えていた。
ヒントンは同僚のテレンス・セジュノフスキーとともに，ホップフィールドのネットワークを出発点として，統計物理学のアイデアを活用しながら，新しいものを構築するためにそれを拡張した。
<!--When Hopfield published his article on associative memory, Geoffrey Hinton was working at Carnegie Mellon University in Pittsburgh, USA. He had previously studied experimental psychology and artificial intelligence in England and Scotland and was wondering whether machines could learn to process patterns in a similar way to humans, finding their own categories for sorting and interpreting information.
Along with his colleague, Terrence Sejnowski, Hinton started from the Hopfield network and expanded it to build something new, using ideas from statistical physics. -->

統計力学は，気体中の分子のように，多くの類似した要素で構成される系を説明する。
気体中の個々の分子をすべて追跡することは困難，あるいは不可能であるが，それらをまとめて考え，圧力や温度といった気体の全体的な性質を決定することは可能である。
気体分子は，それぞれの速度で気体の体積全体に広がる可能性があり，それでも同じ全体的な性質が得られる。
<!-- Statistical physics describes systems that are composed of many similar elements, such as molecules in a gas.
It is difficult, or impossible, to track all the separate molecules in the gas, but it is possible to consider them collectively to determine the gas’ overarching properties like pressure or temperature.
There are many potential ways for gas molecules to spread through its volume at individual speeds and still result in the same collective properties.-->

個々の構成要素が共同して存在できる状態は，統計物理学を用いて分析することができ，その発生確率を計算することができる。
状態によっては，他の状態よりも発生確率が高いものもある。これは利用可能なエネルギーの量に依存するが，この量は 19 世紀の物理学者ルートヴィヒ・ボルツマンの式で表される。
ヒントンのネットワークは，この式を利用しており，その方法は1985年に「ボルツマン・マシン」という印象的な名称で発表された。
<!--The states in which the individual components can jointly exist can be analysed using statistical physics, and the probability of them occurring calculated.
Some states are more probable than others; this depends on the amount of available energy, which is described in an equation by the nineteenth-century physicist Ludwig Boltzmann.
Hinton’s network utilised that equation, and the method was published in 1985 under the striking name of the Boltzmann machine. -->

### 同じタイプの新しい例を認識する<!--#### Recognising new examples of the same type-->

ボルツマン・マシンは通常，2 種類の異なるノードとともに使用される。
情報は，可視ノードと呼ばれる1つのグループに供給される。他のノードは隠れ層を形成する。
隠れノードの値と接続も，ネットワーク全体のエネルギーに寄与する。
<!-- The Boltzmann machine is commonly used with two different types of nodes.
Information is fed to one group, which are called visible nodes. The other nodes form a hidden layer.
The hidden nodes’ values and connections also contribute to the energy of the network as a whole. -->

このマシンは，ノードの値を1つずつ更新するルールを適用することで実行される。
最終的に，ノードのパターンが変化する状態になるが，ネットワーク全体の特性は変わらない。
各パターンには，ボルツマン方程式に従ってネットワークのエネルギーによって決定される特定の確率が存在する。
マシンが停止すると，新しいパターンが作成される。これがボルツマンマシンを生成モデルの初期の例としている。
<!--The machine is run by applying a rule for updating the values of the nodes one at a time.
Eventually the machine will enter a state in which the nodes’ pattern can change, but the properties of the network as a whole remain the same.
Each possible pattern will then have a specific probability that is determined by the network’s energy according to Boltzmann’s equation.
When the machine stops it has created a new pattern, which makes the Boltzmann machine an early example of a generative model.-->

<div class="figcenter">
<img src="https://www.nobelprize.org/uploads/2024/09/popular-physicsprize2024-figure4-1024x594.jpg" style="width:55%">
</div>

ボルツマンマシンは学習することができる。
ただし，指示からではなく，例を示されることで学習する。
ネットワークの接続部分の値を更新することで訓練を行い，訓練時に可視ノードに与えられた例となるパターンが，マシンが実行された際に発生する可能性が最も高くなるようにする。
この訓練中に同じパターンが複数回繰り返された場合，そのパターンの発生確率はさらに高くなる。
また，訓練は，マシンが訓練された例に類似した新しいパターンを出力する確率にも影響を与える。
<!-- The Boltzmann machine can learn – not from instructions, but from being given examples.
It is trained by updating the values in the network’s connections so that the example patterns, which were fed to the visible nodes when it was trained, have the highest possible probability of occurring when the machine is run. If the same pattern is repeated several times during this training, the probability for this pattern is even higher.
Training also affects the probability of outputting new patterns that resemble the examples on which the machine was trained.-->

訓練されたボルツマンマシンは，以前に見たことのない情報でも，見覚えのある特徴を認識することができる。
友人の兄弟に会ったと想像してみよう。
それらが親戚であることはすぐに分かる。
同様に，ボルツマンマシンは，訓練事例に含まれるカテゴリーに属するものであれば，まったく新しい例を認識し，類似しない資料と区別することができる。
<!-- A trained Boltzmann machine can recognise familiar traits in information it has not previously seen.
Imagine meeting a friend’s sibling, and you can immediately see that they must be related.
In a similar way, the Boltzmann machine can recognise an entirely new example if it belongs to a category found in the training material, and differentiate it from material that is dissimilar. -->

ボルツマンマシンは，その原型ではかなり非効率的で，解を見つけるのに長い時間がかかった。
しかし，ヒントンが研究を続けたように，さまざまな方法で開発が進められると，状況はより興味深いものになっていく。
後続のバージョンでは，いくつかの素子間の接続が削除され，間引きが行われた。
これにより，マシンがより効率的になる可能性があることが判明した。
<!-- In its original form, the Boltzmann machine is fairly inefficient and takes a long time to find solutions.
Things become more interesting when it is developed in various ways, which Hinton has continued to explore.
Later versions have been thinned out, as the connections between some of the units have been removed. It turns out that this may make the machine more efficient. -->

1990 年代には，多くの研究者が人工ニューラルネットワークへの関心を失ったが，Hinton は研究を続けた。
また，彼は2006年に同僚の Simon Osindero, Yee Whye Teh, Ruslan Salakhutdinov とともに，層状に重ねられた一連のボルツマンマシンでネットワークを事前学習する方法を開発し，新たな成果の爆発的な増加に貢献した。
この事前学習により，ネットワーク内の接続に最適な出発点が与えられ，画像内の要素を認識するための学習が最適化された。
<!-- During the 1990s, many researchers lost interest in artificial neural networks, but Hinton was one of those who continued to work in the field.
He also helped start the new explosion of exciting results; in 2006 he and his colleagues Simon Osindero, Yee Whye Teh and Ruslan Salakhutdinov developed a method for pretraining a network with a series of Boltzmann machines in layers, one on top of the other.
This pretraining gave the connections in the network a better starting point, which optimised its training to recognise elements in pictures. -->

ボルツマン・マシンは，より大きなネットワークの一部として使用されることが多い。例えば，視聴者の好みに応じた映画やテレビ番組の推奨に使用できる。
<!-- The Boltzmann machine is often used as part of a larger network. For example, it can be used to recommend films or television series based on the viewer’s preferences. -->

#### 機械学習 - 現在と未来<!-- #### Machine learning – today and tomorrow-->

ジョン・ホップフィールドとジェフリー・ヒントンは，1980 年代以降の研究により，2010 年頃に始まった機械学習革命の基礎を築いた。
<!-- Thanks to their work from the 1980s and onward, John Hopfield and Geoffrey Hinton have helped lay the foundation for the machine learning revolution that started around 2010. -->

現在我々が目撃している発展は，ネットワークの訓練に使用できる膨大な量のデータへのアクセスと，コンピューティング能力の飛躍的な向上により可能となった。
今日の人工ニューラルネットワークは，多くの場合，巨大で多くの層から構成されている。これを深層ニューラルネットワークと呼び，その学習方法を深層学習と呼ぶ。
<!-- The development we are now witnessing has been made possible through access to the vast amounts of data that can be used to train networks, and through the enormous increase in computing power.
Today’s artificial neural networks are often enormous and constructed from many layers. These are called deep neural networks and the way they are trained is called deep learning. -->

1982 年の Hopfield の連想記憶に関する論文をざっと見ると，この発展についてある程度の見通しが得られる。
その論文では，30 個のノードを持つネットワークが使用されていた。
すべてのノードが互いに接続されている場合，435 の接続がある。
ノードには値があり，接続には異なる強度があり，合計すると，追跡すべきパラメータは 500 未満である。
また，彼は 100 ノードのネットワークも試したが，当時使用していたコンピュータでは複雑すぎた。
これを今日の巨大な言語モデルと比較すると，これは 1 兆以上のパラメータ（1 億億の1 億倍）を含むネットワークとして構築されている。
<!-- A quick glance at Hopfield’s article on associative memory, from 1982, provides some perspective on this development.
In it, he used a network with 30 nodes.
If all the nodes are connected to each other, there are 435 connections.
The nodes have their values, the connections have different strengths and, in total, there are fewer than 500 parameters to keep track of.
He also tried a network with 100 nodes, but this was too complicated, given the computer he was using at the time.
We can compare this to the large language models of today, which are built as networks that can contain more than one trillion parameters (one million millions). -->

現在，多くの研究者が機械学習の応用分野の開発に取り組んでいる。
どの分野が最も有望かはまだわからないが，この技術の開発と利用をめぐる倫理的な問題についても幅広い議論が行われている。
<!--Many researchers are now developing machine learning’s areas of application.
Which will be the most viable remains to be seen, while there is also wide-ranging discussion on the ethical issues that surround the development and use of this technology. -->

物理学は機械学習の発展に貢献するツールを提供してきたため，研究分野としての物理学が人工ニューラルネットワークからどのような恩恵を受けているのかを見るのは興味深い。
機械学習は，これまでのノーベル物理学賞受賞者たちの研究分野と関連の深い分野で，以前から利用されてきた。
例えば，ヒッグス粒子の発見に必要な膨大なデータをふるいにかけて処理するために機械学習が利用された。
その他の応用例としては，ブラックホールの衝突による重力波の測定におけるノイズの低減や，太陽系外惑星の探索などがある。
<!-- Because physics has contributed tools for the development of machine learning, it is interesting to see how physics, as a research field, is also benefitting from artificial neural networks.
Machine learning has long been used in areas we may be familiar with from previous Nobel Prizes in Physics.
These include the use of machine learning to sift through and process the vast amounts of data necessary to discover the Higgs particle.
Other applications include reducing noise in measurements of the gravitational waves from colliding black holes, or the search for exoplanets.-->

近年では，分子や物質の特性を計算したり予測したりする際にも，この技術が利用され始めている。例えば，タンパク質分子の構造を計算してその機能を決定したり，より効率的な太陽電池に使用するのに最適な特性を持つ物質の新しいバージョンを特定したりするなどである。
<!--In recent years, this technology has also begun to be used when calculating and predicting the properties of molecules and materials – such as calculating protein molecules’ structure, which determines their function, or working out which new versions of a material may have the best properties for use in more efficient solar cells. -->

#### さらに詳しく<!-- #### Further reading-->

今年の受賞に関する追加情報（英語による科学的背景を含む）は，スウェーデン王立科学アカデミーのウェブサイト（www.kva.se）および www.nobelprize.org で入手できる。
www.nobelprize.org では，記者会見のビデオやノーベル賞受賞講演などを視聴できる。
ノーベル賞および経済学賞に関連する展示会や活動に関する情報は，www.nobelprizemuseum.se で入手できる。
<!--Additional information on this year’s prizes, including a scientific background in English, is available on the website of the Royal Swedish Academy of Sciences, www.kva.se, and at www.nobelprize.org, where you can watch video from the press conferences, the Nobel Lectures and more.
Information on exhibitions and activities related to the Nobel Prizes and the Prize in Economic Sciences is available at www.nobelprizemuseum.se. -->

* [Hopfield1982, Neural networks and physical systems with emergent collective computationalabilitie](/2024cogpsy/1982Hopfield_Neural_networks_and_physical_systems_with_emergent_collective_computational_abilities.pdf){:target="_blank"}
* [Hopfiled&Tank1985, "Neural" Computation of Decisions in Optimization Problems](/2024cogpsy/1985Hopfield_Tank_Neural_computation_of_decisions_in_optimization_problems.pdf){:target="_blank"}
* [Rumelhart, Hinton, McClelland 1986, A General Framework for Parallel Distributed Processing, PDP book, chapt. 2](/2024cogpsy/1986Rumelhart_PDPbook_chapter2.pdf){:target="_blank"}
* [Rumelhart, Hinton, & Williams, 1986, Learning Internal Representations by Error Propagation, PDP book, chapt. 8](/2024cogpsy/1986Rumelhart_Hinton_Williams_PDP_Chapt8.pdf){:target="_blank"}
* [ジェフェリー・ヒントンのマクセル賞受賞記念講演(2016)](/Hinton_Maxwell_award/){:target="_blank"}
* [浅川, 2013, アトラクタニューラルネットワークモデルの数理解析とその神経心理学への応用](/2024cogpsy/2013Asakawa_JPsychoReview_Published.pdf){:target="_blank"}
* [浅川 2000, ニューラルネットワークの基礎](/2024cogpsy/main-web2010.pdf){:target="_blank"}

# 2. 機械学習モデルと心理学，生理学

<div class="figcenter">
<img src="/assets/2019Glaser_fig2.jpg" width="39%">
<img src="/2024assets/2008Kriegeskorte_fig3.jpg" width="39%">
<div class="memo">

左: Glaser+(2019) Fig.2, 右: Kriegeskorte+(2008) Fig.3

機械学習の 4 つ役割
1. 工学問題の解として
2. 予測変数の特定と改善
3. 単純モデルの評価とベンチマーク
4. 脳のモデルとして<br/>

図 3. 異なる表現を関連付けるハブとしての表現非類似性行列<!-- FIGURE 3. The representational dissimilarity matrix as a hub that relates different representations. --><br/>

A: システム神経科学は，3つの主要な研究分野，行動実験，脳活動実験，計算モデリングを関連付けるのに苦労してきた。
これまでは，これらの分野は主に 2 つのレベルで相互に作用してきた。
(1) 言語理論のレベルでの相互作用。すなわち，個別の分析から導き出された結論を比較することによる相互作用。
このレベルは不可欠であるが，定量的ではない。
(2) 特性関数のレベルで相互作用，例えば，心理測定関数と神経測定関数との比較。
この種の分野間の接触は同様に不可欠であり，定量的なものである。
しかし，特性関数は通常，少数のデータ点しか含まないため，そのインタフェースは情報的に豊かではない。
ここで示されている RDM は 4 つの条件のみに基づいているため，($(4^2-4)/2=$) 6 つのパラメータしか得られないことに注意。
しかし，パラメータの数は条件の数の 2 乗に比例して増えるため，RDM は異なる表現を関連付けるための情報豊富なインターフェースを提供できる。
例えば，ここで取り上げている 96 画像の実験では，行列のパラメータ数は $(96^{2}−96)/2=4,560$ となる。
<!-- **A**: Systems neuroscience has struggled to relate its three major branches of research: behavioral experimentation, brain-activity experimentation, and computational modeling.
So far these branches have interacted largely on two levels:
(1) They have interacted on the level of verbal theory, i.e., by comparing conclusions drawn from separate analyses.
This level is essential, but it is not quantitative.
(2) They have interacted at the level characteristic functions, e.g., by comparing psychometric and neurometric functions.
This form of bringing the branches in touch is equally essential and can be quantitative.
However, characteristic functions typically contain only a small number of data points, so the interface is not informationally rich. Note that the RDM shown is based on only four conditions, yielding only (42−4)/2=6 parameters.
However, since the number of parameters grows as the square of the number of conditions, the RDM can provide an informationally rich interface for relating different representations.
Consider for example the 96-image experiment we discuss, where the matrix has (962−96)/2=4,560 parameters. --><br/>

B: RDM が提供する量的インタフェースを介して，どのような異なる表現が関連付けられるかをより詳細に説明している。
ここでは，確立可能なモダリティ内での関係を説明するために，fMRI の例を任意に選択した。
これらの関係は，いずれも確立が困難であることに注意 (灰色の双方向矢印)。
<!-- **B**: This panel illustrates in greater detail what different representations can be related via the quantitative interface provided by the RDM.
We arbitrarily chose the example of fMRI to illustrate the within-modality relationships that can be established.
Note that all these relationships are difficult to establish otherwise (gray double arrows). -->
</div></div>

# 3. Git のインストールと実行

* [図解解説】これ1本でGitをマスターできるチュートリアル！【完全版】](https://qiita.com/Sicut_study/items/0318cc136c189b179b7f)

### コマンドライン版 `git` のインストール

[Git の公式ページ](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git){:target="_blank"} によれば，Windows へのインストールには複数の方法がある。

* [Git for Windows プロジェクト版 https://git-scm.com/download/win]
* [Chocolatoey package 版](https://community.chocolatey.org/kackages/git)

Chocolatory は総合パッケージ管理と呼ばれる複数のソフトウェアを矛盾なく管理するためのツールである。
個々のソフトウェアを個別にインストールすると，バージョン管理が煩雑であるため，chocolatory 管理を任せるという選択肢は一考に値する。

Chocolaty がインストールしてあれば，以下のコマンドを実行すれば git がインストールされる。
Chocolaty のインストールには，次節を参照のこと

```bash
choco install git.install --params "'/GitAndUnixtoolsOnPath /WindowsTerminal /NoAutoCrlf'"
```

### Chocolaty のインストール

1. 管理者権限で `powershell.exe` を実行する
2. `powershell.exe` 上に下記コマンドをコピーする:
```bash
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
3. エンターキーを押下して上記コマンドを実行する。
もし `Get-ExcutionPolicy` を実行して，`Restricted` が帰ってきたら，`Set-ExecutionPolicy Allsigned` もしくは `Set-ExecutionPolicy Bypass -Scope Process` を実行する必要がある。
4. インストールが終了するまでしばらく待つ。
5. エラーメッセージが表示されなければ，`choco -?` を実行して確認作業を行う。


<!-- 4. First, ensure that you are using an administrative shell - you can also install as a non-admin, check out Non-Administrative Installation.
5. Install with powershell.exe
```bash
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
1. Paste the copied text into your shell and press Enter.
2. Wait a few seconds for the command to complete.
3. If you don't see any errors, you are ready to use Chocolatey! Type choco or choco -? now, or see Getting Started for usage instructions. -->

### Git コマンドの実際

Windows Powershell のコマンドラインで必要なコマンドは，`git clone`, `git status`, `git pull` くらいでろう。
他のコマンドは，必要に応じて習得すれば良い。

Github 上のリポジトリ `CSAILVision` を自身の Windows PC のカレントディレクトリへ保存する場合， `git clone` コマンドを用いて，以下のように操作する:
```bash
git clone https://github.com/CSAILVision/places365.git
```

上例の場合，カレントディレクトリに `places365` というディレクトリが作成される。
`git clone 第一引数 第二引数` のように指定すると，`places365` ではなく，第二引数で指定されたディレクトリ名で，リポジトリが作成される。
`2024palces365.git` というディレクトリ名にしたければ，以下のようにする:<br/>
`git clone https://github.com/CSAILVision/places365.git 2024places365.git`

上記のコマンドで，`2024places365.git` ディレクトリ内に全リポジトリが格納されている。
Git 上でコードやデータが変更されていれば，最新の状態へ変更する必要が生じる。
この状態をチェックするコマンドが `git status` であり，最新の状態へ混交するコマンドが `git pull` である。
`git status` と `git pull` コマンドは，カレントディレクトリを該当ディレクトリ内へ変更してから実行する必要がある。
なぜなら，各リポジトリが格納されているディレクトリ内に，更新情報が格納されているからである。
`git pull` コマンドは，カレントディレクトリ内にある (具体的には隠しディレクトリ `.git` 以下) 更新場をサーバ側の更新情報と比較して，最新のデータを取得するからである。

### ロジスティック回帰，k-means, SVM (サポートベクターマシン)，および線形判別分析の相互関係

先週の竹市先生の授業回で説明のあった 3 手法に線形判別分析を加えて 4 手法の相互関係について補足していく。

復習: 機械学習の教師あり学習は，分類問題と回帰問題とに大別される。
これらは，教師信号が離散量か連続量かの違いである。
唯一紛らわしい用語にロジスティック回帰 (Logistic regressions) がある。
ロジスティック回帰は回帰ではなく，分類問題に用いられる。
すなわち線形問題の典型である単回帰 simple regressions: $y=f(x)=ax+b$ に対して，出力を $[0,1]$ の範囲に限定すれば，出力確率とみなしうる。
このため，単回帰式に対して $\displaystyle[1-e^{-y}]^{-1}=[1-e^{-(ax+b)}]^{-1}=\frac{1}{1+e^{-(ax+b)}}$ なる変換を考える。
この変換のことをロジスティック変換と呼び，この手法の名前の由来となっている。

ロジスティック変換は，ロジスティックシグモイド変換，あるいは単に，シグモイド関数と呼ばれることもある。
ロジスティック回帰の起源は，一説によれば人口動態を記述した Mathus(1789) であるとされる([Cramer2002](https://papers.tinbergen.nl/02119.pdf))。

任意のデータ $x\in[1,D]$ に対して，真偽，賛否，あるいは，あるクラスに属するか否かを定めるためのデータ，もしくは特徴を $x$ とする。
$x$ の範囲は $x\in(-\infty,+\infty)$ であるので，$P(x) + P(\neg x) = 1$ を満たすためには，$f(x)>0$ かつ $x>y\rightarrow f(x)>(y)$ という条件を満たす変換を考えれば良い。

この条件に合致する変換として $f(x)=e^{x}$ を考えれば，ロジスティック回帰式，あるいはシグモイド関数を得る。

今，A か B か，賛成か反対か，を A と B で表すことにする。
A と B とは互いに背反であり，A でなければ B が成り立つものとする。
このとき $e^{A}, e^{B}$ を用いて，A である確率 $P(A)$ は次式で与えられる:
$$
P(A) = \frac{e^{A}}{e^{A}+e^{B}}
$$
上式右辺分母は，二項とも正である。
したがって B である確率は $\displaystyle P(B)=1-P(A)=\frac{e^{B}}{e^{A}+e^{B}}=1-\frac{e^{A}}{e^{A}+e^{B}}$ である。
ここで，分子分母を $e^{A}$ で割ると $\displaystyle P(A)=\frac{1}{1+e^{-(A+B)}}$ となる。
このため，$P(A)=P(B)=0.5$ となる点は $e^{-(A+B)}=1$ であるから，指数の肩が 0 であれば $e^{0}=1$ である。
このため $-(A+B)=0$ より $A=B$ であれば，$P(A)=P(B)=0.5$ が成り立つ。

ここで，ニューラルネットワークとの関連を考える。
入力ベクトル $\mb{x}$ に対して，$A$ または $\neg A$ を学習する場合，出力層素子が 1 つである 2 層のニューラルネットワークを設計することができる。
$y = \mb{w}^{\top}\mb{x} +b$ なる線形結合により得られた $y$ に対してロジスティック回帰は $\displaystyle y=\frac{1}{1+e^{-\left(wx+b\right)}}$ である。
このとき，$\mb{w}^{\top}\mb{x}+b>0$ であれば，$P(A)>0.5$ であり，$\mb{w}^{\top}\mb{x}+b<0$ であれば $P(A)<0.5$ となる。
このことは，入力ベクトル $\mb{x}$ と重みベクトル $\mb{w}$ との内積 (バイアス項の和を除けば) の正負によって判断確率が定まることとなる。

すなわち，ベクトルの内積が正であることわ，入力ベクトルと重みベクトルとの内積が正であるとは，二本のベクトル間の角度を $\theta$ とすれば
${\mb{w}^{\top}\mb{x}}=|\mb{w}| |\mb{x}| \cos\theta$ であるから，$\cos$ によって右辺の正負が定まる。
したがって，$\mb{w}$ と $\mb{x}$ との成す角が $-1/2\ge\theta\ge1/2$ であれば $\cos\theta>0$ である。
すなわち，$A$ または $\neg A$ を判別するためには，ベクトル $\mb{x}$ に直交する


したがって，入力データベクトル $\mb{x}$ に対して，同じ次元を持つ重みベクトル $\mb{w}$ との内積 $\mb{w}^{\top}\mb{x}$ が正であれば，その正規確率である出力値は 0.5 を上回る ($P\left(\mb{x}\right)>0$)。
反対に内積が負であれば ($\mb{w}^{\top}\mb{x}<0$) その確率は 0.5 を下回る。


<!-- k-means は -->

### マルチモーダル統合，マルチタスク，トップダウン流とボトムアップ

* [Ullman (2021) 系列探索と逆行流: 視覚野における双方向情報フローの計算モデル](/2023cogpsy/2021Ullman_bu_td_ja.pdf){:target="_blank"}
* [Ullman (1995) ボトムアップ・トップダウンの反復処理による画像解釈](/2023cogpsy/1995Ullman_bidirectional_cortex_ja.pdf){:target="_blank"}

<!--
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
<img src="/2023assets/world_models_1990.jpeg" style="display: block; margin: auto; width: 44%;"/>
<img src="/2023assets/world_models_1990_feedback.jpeg" style="display: block; margin: auto; width: 44%;"/>
</div>
<div style="text-align: center;">
世界 RNN モデルを内蔵したコントローラ。

環境と相互作用する RNN ベースのコントローラの図 (Schmithuber1990)
A controller with internal RNN model of the world.
Ancient drawing (1990) of a RNN-based controller interacting with an environment. [20]
</div>
-->
