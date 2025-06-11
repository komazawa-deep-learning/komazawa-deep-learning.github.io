---
title: 第08回 2025 年度開講 駒澤大学 心理学特講 IIIA
author: 浅川 伸一
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="center">
<font size="+2" color="navy"><strong>ディープラーニングの心理学的解釈</strong></font><br/><br/>
</div>

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br/>
Date: 13/Jun/2025<br/>
Appache 2.0 license<br/>
</div>

# 第 8 回

## キーワード

* 誤差逆伝播法 back propagation
* 勾配降下法 gradient descent method
* 学習率
<!-- * モーメンタム -->
* [ソフトマックス関数 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_0512softmax.ipynb){:target="_blank"}
* 勾配消失問題 gradient vanishing problem，勾配爆発問題 gradient explosion problem,
* ワンホットベクトル
* 単語埋め込み
* 勝者占有回路
<!-- One hot vector,
word embeddings,
winners-take-all (winner takes it all) circuit.
ちはやふる -->

<!-- ## クイズ

* ML Machiine Learning, Mailing list, Maximum Likelihood
* SGD
* learning ratio
* pdf: probalility density function, portable document format

One hot vector,
word embeddings,
winners-take-all (winner takes it all) circuit.
ちはやふる -->

### 実習ファイル

* [最小コードの排他的論理和  <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/220komazawa_miniumXOR.ipynb)
* [3 層パーセプトロンと確率的勾配降下法のデモ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2021_0521mlp_Adam_SGD.ipynb)

* [三夕の歌  <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_0925RNN_3twilight_poetries.ipynb)
* [足し算モデル <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/2019cnps/blob/master/notebooks/2019cnps_addtion_rnn.ipynb)


## デモと実習

- [リカレントニューラルネットワークによる文字ベース言語モデルデモ](https://komazawa-deep-learning.github.io/character_demo.html){:target="_blank"}
- [リカレントニューラルネットワークによる文字ベース言語モデルデモ みんなの日本語](https://komazawa-deep-learning.github.io/minnichi_char_rnn.html)
- [SRN のデモ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_0702rnn_demo.ipynb){:target="_blank"}
- [足し算のデモ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-l
earning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_0702RNN_binary_addtion_demo.ipynb){:target="_blank"}
- [百人一首データ取得](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_0917get_hyakunin_isshu.ipynb){:target="_blank"}
<!-- - [BERT の超簡単な使い方 <img src="/assets/colab_icon.svg">](https://colab.research.google.c
om/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_0903BERT_demo.ipynb){:target="_blank"} -->
- [最小限の MeCab](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2022_0916mecab_test.ipynb)


<!-- * [word2vec 実習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2020_0619word2vec.ipynb) -->

<!-- - [SRN のデモ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_0702rnn_demo.ipynb)
- [足し算のデモ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_0702RNN_binary_addtion_demo.ipynb) - [足し算のデモ keras 版 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/2019cnps/blob/master/notebooks/2019cnps_addtion_rnn.ipynb)-->

- [Bahdanau and Loung attentions <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_1022Two_attentions_additive_and_multiplicative_Seq2seq.ipynb)
* [Attention is all you need <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_1022The_Annotated_%22Attention_is_All_You_Need%22.ipynb)

<!--
* [注意つき翻訳モデル <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_1008seq2seq_attention_demo.ipynb)
* [バニラ風味 注意なし翻訳モデル <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_1003vanilla_seq2seq2.ipynb) -->

* [GPT-3 を使って，自発話のシミュレーション <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_0719japanese_gpt_1b.ipynb)
* [T5 による，文章穴埋め問題  <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_0918T5_demo_filling_blank_question.ipynb)
* [Seq2seq モデル による翻訳デモ 注意付きリカレントニューラルネットワーク <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_1008seq2seq_attention_demo.ipynb)
* [BERT の微調整実習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_0623BERT_SNOW_training.ipynb)


# 言語モデル

$$
P(x_{t+1}) = P(x|x_{i<t})
$$

1. RNN
2. LSTM, GRU
3. Transformer

<center>

<img src="/assets/SRN_J.svg" style="width:23%">
<img src="/assets/SRN_E.svg" style="width:23%">
<img src="/assets/2015Greff_LSTM_ja.svg" width="29%"><br/>
<img src="/assets/RNN_fold.svg" style="width:49%"><br>
Time unfoldings of recurrent neural networks

左：マイケル・ジョーダン発案ジョーダンネット [@1986Jordan]
中：ジェフ・エルマン発案エルマンネット
右: LSTM
</center>

の LSTM は一つのニューロンに該当します。このニューロンには 3 つのゲート(gate, 門) が付いています。
3 つのゲートは以下の名前で呼ばれます。

1. 入力ゲート input gate
2. 出力ゲート output gate
3. 忘却ゲート forget gate

各ゲートの位置を上図で確認してください。入力ゲートと出力ゲートが閉じていれば，セルの内容(これまでは中間層の状
態と呼んできました)が保持されることになります。
出力ゲートが開いている場合には，セル内容が出力されます。一方出力ゲートが閉じていればそのセル内容は出力されませ
ん。このように入力ゲートと出力ゲートはセル内容の入出力に関与します。
忘却ゲートはセル内容の保持に関与します。忘却ゲートが開いていれば一時刻前のセル内容が保持されることを意味します
。反対に忘却ゲートが閉じていれば一時刻前のセル内容は破棄されます。全セルの忘却ゲートが全閉ならば通常の多層ニュ
ーラルネットワークであることと同義です。すなわち記憶内容を保持しないことを意味します。SRN でフィードバック信号
が存在しない場合に相当します。セルへの入力は，

1. 下層からの信号，
2. 上層からの信号, すなわち Jordan ネットの帰還信号
3. 自分自身の内容，すなわち Elman ネットの帰還信号

が用いられます。これら入力信号が

1. 入力信号そのもの
2. 入力ゲートの開閉制御用信号
3. 出力ゲートの開閉制御用信号
4. 忘却ゲートの開閉制御用信号

という 4 種類に用いられます。従って LSTM のパラメータ数は SRN に比べて 4 倍になります。

LSTM に限らず一般のニューラルネットワークの出力には非線形関数が用いられます。代表的な非線形出力関数としては，
以下のような関数が挙げられます。

1. シグモイド関数: $f(x)=\left[1+e^{-x}\right]^{-1}$
2. ハイパーボリックタンジェント関数:  $f(x)=\left(e^{x}-e^{-x}\right)/\left(e^{x}+e^{-x}\right)$
3. 整流線形ユニット関数: $f(x)=\max\left(0,x\right)$

この中で，セルの出力関数として 2. のハイパーボリックタンジェント関数が，ゲートの出力関数にはシグモイド関数が使われます。
その理由はハイパーボリックタンジェント関数の方が収束が早いこと，シグモイド関数は値域が $[0,1]$ であるためゲートの開閉に直接対応しているからです。

- Le Cun, Y. Bottou, L., Orr, G. B, Muller K-R. (1988) Efficient BackProp, in Orr, G. and Muller, K. (Eds.) Neural Networks: tricks and trade, Springer.

<!--
The LSTM (left figure) can be described as the input signals $\mathbf{x}_t$ at
time $t$, the output signals $\mathbf{o}_t$, the forget gate $\mathbf{f}_t$, and
the output signal $\mathbf{y}_t$, the memory cell $\mathbf{c}_t$, then we can get
the following:
$i_{t}=\sigma\left(W_{xi}x_{t}+W_{hi}y_{t-1}+b_{i}\right)$, <br>
$f_{t}=\sigma\left(W_{xf}x_{t}+W_{hf}y_{t-1}+b_{f}\right)$, <br>
$o_{t}=\sigma\left(W_{xo}x_{t}+W_{ho}y_{t-1}+b_{o}\right)$, <br>
$g_{t}=\phi\left(W_{xc}x_{t}+W_{hc}y_{t-1}+b_{c}\right)$,<br>
$c_{t}=f_{t}\odot c_{t-1} + i_{t}\odot g_{t}$,<br>
$h_{t}=o_{t}\odot\phi\left(c_{t}\right)$<br>\label{eq:LSTM}
where
$\sigma\left(x\right)=\displaystyle\frac{1}{1+\mbox{exp}\left(-x\right)}$ (logistic function)
%% =1/2\left(\phi\Brc{x}+1\right)$,
$\phi\left(x\right)=\displaystyle\frac{\mbox{exp}\left(x\right)-\mbox{exp}\left(-x\right)}{\mbox{exp}\left(x\r
ight)+\mbox{exp}\left(-x\right)}$ (hyper tangent)
%% $=2\sigma\left(x\right)-1$
and $\odot$ menas Hadamard (element--wise) product.
-->

## LSTM におけるゲートの生理学的対応物 <!--Physiological correlates of gates in LSTM-->

以下の画像は <http://kybele.psych.cornell.edu/~edelman/Psych-2140/week-2-2.html> よりの引用。
ウミウシのエラ引っ込め反応時に，ニューロンへの入力信号ではなく，入力信号を修飾する結合が存在する。下図参照。

<center>
<img src="/assets/2016McComas_presynaptic_inhibition.jpg" style="width:24%">
<img src="/assets/C87-fig2_24.jpg" width="17%">
<img src="/assets/C87-fig2_25.jpg" width="33%"><br>
アメフラシ (Aplysia) のエラ引っ込め反応(a.k.a. 防御反応)の模式図[^seaslang]
<!-- <img src="/assets/shunting-inhibition.jpg" width="29%"> -->
</center>

* [注意機構の補足説明 大門他 (2023) <img src="https://www.adobe.com/content/dam/cc/en/legal/images/badges/PDF_32.png">](/2023/2023cnps注意機構の補足説明.pdf){:target="_blank"}

## 知能のコンピュータアナロジー

知能をコンピュータに擬 (なぞら) えることは，初期の AI は，コンピュータ黎明期でもあったこともあり，多くの人間を惹きつけた。
例えば，哲学者 Foder は「人間の心は脳のハードウェア上で動くプログラムである」と主張した。
プログラムであるならば，別のハードウェアにインストールすれば動作することを意味し，人工知能研究にとって重要な考え方であった。
また，同じハードウェアに異なるソフトウェアをインストールすれば，異なるプログラムが動作する。
<!-- Patricia Churchland  は 「猫についてはどうか？」 と質問した。
フォダーは自信たっぷりにこう答えた「猫の脳が猫のプログラムを動かしているのだ。」 -->
この脳を単なるハードウェアとして無視し，プログラムに集中する **「機能主義」** が正当化されてきた。

ところが脳は，状況が異なる。
上に書いたとおりコンピュータでは，同じハードウェアで異なるソフトウェアを動かすことができるが，脳では，ハードウェアとソフトウェアを分離することが難しく，また，まったく同じ脳は 2 つ存在しない。
人間が，新しいことを学習するときには，脳のハードウェアが修正されていると考えることができる。
そのため，神経細胞同士がどのようにつながっているかを再構築し，その通信内容を記録することで，自然が発見したアルゴリズムを解明することができる。

脳は多くの相互作用するアルゴリズムから作られていると考える研究者もいる ([Navlakha2018](https://www.wired.com/story/why-animal-extinction-is-crippling-computer-science/))。
脳は，互いに調整可能，適応可能な神経細胞 (ニューロン) ですべて作られているため，
各部分アルゴリズムを統合して一つにする問題は，神経細胞間の調整に委ねられている。<!-- これは，多様なネットワークアーキテクチャの構築と統合が急速に進んでいることに反映されている。 -->
これに対して，異なる規則や記号で設計された視覚モジュール，運動制御モジュール，計画モジュールなどのモジュールを統合して大規模な系を構築することは問題であった。
<!-- Navlakha, S. (2018). Why animal extinction is crippling computer science. Wired (September 19). https://www.wired.com/story/why-animal-extinction-is-crippling-computer-science/ -->
<!-- The computer metaphor for intelligence was an attractive garden path.
I once was at a talk given by Jerry Fodor, a philosopher of science, who claimed that the human mind was a program that ran on the brain’s hardware.
Patricia Churchland asked, “What about cats?” “Yes,” Fodor replied confidently.
“The cat brain is running the cat program.”
This argument was used to justify functionalism—the view that we can ignore the brain as mere hardware and focus on the program.
Unlike digital computers, where the same hardware can run different software programs, the hardware in brains is the software, and no two brains are identical.
As we learn new things, we are modifying our hardware.
This is why the algorithms that nature discovered can be uncovered by reconstructing how neurons are connected with each other and recording what they communicate.
Although brains are built from many interacting algorithms (Navlakha2018), the problem of integrating subsystems is alleviated because they are all built with neurons that can adapt to each other.
This is reflected in the rapid progress that has been made in building and integrating diverse network architectures.
In contrast, integrating modules such as a vision module, a motor control module, and a planning module designed with different rules and symbols to build large-scale systems was problematic. -->

## パーセプトロン perceptrons

現代の機械学習の種は AI の黎明期にはすでに蒔かれていた。
Frank Rosenblatt のパーセプトロン (1961) は，単層の **重み勾配降下法** を使って，例からの入力を分類することを学習した。

<center>
<img src='/assets/rosenblatt.jpg' style="width:33%">++++
<img src='/assets/perceptron.png' style="width:49%"><br/>
<!-- <img src='https://komazawa-deep-learning.github.io/assets//rosenblatt.jpg' style="width:49%"><br> -->
左: フランク・ローゼンブラット (Frank Rosenblatt)。
右: パーセプトロンの模式図 ミンスキーとパパート「パーセプトロン」より
<!-- <img src='https://komazawa-deep-learning.github.io/assets//perceptron.png' style="width:74%"></br> -->
</center>

**コネクショニスト connectionist** の研究コミュニティが，確率的な二値ニューロンの多層ネットワークの学習アルゴリズムを発明し(Ackley+1985)，決定論的な実数値ニューロンの **誤差逆伝播法 (バックプロパゲーション)** アルゴリズムを再発見してニューラルネットワークに適用するまで (Rumelhart+1986)，さらに 24 年かかった。
当時は，視覚や音声のような難しい問題の学習を進めるのに，どれだけのコンピュータパワーが必要なのかが分かっていなかった。
それから 30 年以上が経ち，今ではどれだけのコンピューティングパワーが必要なのかが分かっている。
この計算資源の進化により，**大規模言語モデル LLM (Large Language Model)** が構築され，近年の話題 chatGPT などにつながっている。
<!-- 驚いたのは，人間の知能の宝庫といわれる言語が，これほどまでに進歩したことである。 -->
<!--The seeds of modern machine learning were already being sown at the dawn of AI.
Frank Rosenblatt’s perceptron (1961) learned to categorize inputs from examples using gradient descent on a single layer of weights.
It would take another 24 years before the connectionist research community invented a learning algorithm for multilayer networks of stochastic binary neurons (Ackley+1985) and rediscovered the backpropagation algorithm for deterministic, real-valued neurons and applied them to neural networks (Rumelhart+1986).
What was not known back then was how much computer power it would take to make progress with learning on difficult problems like vision and speech.
A third of a century later, we now know how much computing power is needed.
The surprise was how much progress has been made with language, thought to be the crown jewel of human intelligence.-->

<!-- ### バイアス，(偏り，偏見，一般論，常識)
従来の AI で論理的推論を重視したのも見当違いだった。
数学者が習得している論理的なステップの系列をエミュレートする方法を学ぶには，多くの訓練が必要だ。
抽象的な推論課題に関する明示的な訓練がなければ，人間は身近な環境でより効果的に論理的な結論に達することができ，LLM でも同じバイアスが観察されている [Dasgupta+2022](https://arXiv.org/abs/2207.07051/)。
TD-ギャモンや AlphaGo が示した創造性は，深層学習皮質モデルだけで生じたものではなく，手続き学習の一種である強化学習と連動していた。
強化学習は，報酬予測誤差を表す神経調節物質であるドーパミンによって，我々の大脳基底核で実施される (図 5参照)。
我々はドーパミンの信号に意識的にアクセスすることはできないが，モチベーションに強力な影響を与え，すべての依存性薬物はドーパミンの活性を操作することで機能する(Sejnowski2019)。
<!-- The emphasis on logical reasoning in traditional AI was also misguided.
Learning how to emulate sequences of logical steps, which mathematicians have mastered, requires a lot of training.Without explicit training on abstract reasoning tasks, humans can more effectively reach logical conclusions in familiar settings, and the same bias has been observed in LLMs (Dasgupta+2022).
The creativity that TD-Gammon and AlphaGo exhibited did not arise from the deep learning cortical model alone, but in conjunction with reinforcement learning, a form of procedural learning.
Reinforcement learning is implemented in our basal ganglia by dopamine, a neuromodulator that represents reward prediction error (see Figure 5).
We do not have conscious access to dopamine signals, but they have a powerful impact on our motivation, and all addictive drugs work by manipulating dopamine activity (Sejnowski2019). -->


# ソフトマックス関数

## ゲートとして

<div class="figure figcenter">
<img src="/2023assets/2006Oreilly_wm_fig2.svg" width="49%">
<div class="figcaption">

#### 図 ゲートの概念図
ゲートが開いているときは，感覚入力は作業記憶を更新できるが，閉じているときはそれができない。
このため，妨害刺激など無関連情報が以前に記憶した情報の維持を妨げるのを防ぐことができる。
O'Reilly (2006) より
</div></div>


# ニューロンのモデル

ニューロンが振動数符号化法のみを利用している --- すなわちニューラルネットワークにおけるすべての情報はニューロンの発火頻度によって伝達される --- ことを仮定する。
すなわち，このニューロンに到達する信号を単位時間あたりで等しく貢献するものと考える。
このような記述の仕方は integrate--and--fire (積分発火) モデルと呼ばれる。

一つのニューロンの振る舞いは，n 個のニューロンから入力を受け取って出力を計算する多入力，1 出力の情報処理素子である (下図 1)。

$n$ 個の入力信号を $x_1, x_2, \cdots, x_n$ とし、$i$ 番目の軸索に信号が与えられたとき、この信号 1 単位によって変化する膜電位の量をシナプス荷重(または結合荷重, 結合強度とも呼ばれる) といい $w_i$ と表記する。
抑制性のシナプス結合については $w_i < 0$, 興奮性の結合については $w_i > 0$ である。
このニューロンのしきい値を $h$, 膜電位の変化を $u$, 出力信号を $z$ とする。

<center>
<img src='/assets/Neuron_Hand-tuned.png' style="width:69%"><br/>
<!-- <img src='https://komazawa-deep-learning.github.io/assets//Neuron_Hand-tuned.png' style="width:69%"></br>
 -->
ニューロンの模式図 wikipedia より
</center>

<!-- <center>
<img src='/assets/Formal_r.svg' style="width:84%"><br/>
<!-- <img src='https://komazawa-deep-learning.github.io/assets//Formal_r.svg' style="width:84%"><br>
形式ニューロン
</center> -->

<center>
<img src="/assets/formal_neuron.svg"><br/>

図 形式ニューロン
</center>

出力信号 $z$ は次式で表される:

$$ z=f(\mu)=f\left(\sum_{i=1}^{n}w_{i}x_{i}-h\right).\tag{1} $$

$f(\mu)$ は出力関数であり、$0\le f(\mu)\le1$ の連続量を許す場合や、0 または 1 の値しかとらない場合などがある。
連想記憶などを扱うときなどは $-1\le f(\mu)\le 1$ とする場合もある。

- 上図で，$f$ がなければ，$z=\sum wx - h$ となり，回帰と同じである。
- すなわちニューラルネットワークのもっとも簡単な形は，統計学の用語では，**回帰 regression** である。
- 統計学においては，回帰，この場合，線形回帰になる，にかかわる変数 $x_{i}$
- 回帰の中を複雑にしていくことで，データに適合させようとする努力が，データサイエンスであり，機械学習であり，ニューラルネットワークであると言える。


## マッカロック・ピッツの形式ニューロン

信号入力の荷重和
$$ \mu = \sum_{i=1}^{n}w_{i}x_{i},\tag{2} $$
に対して、出力 $z$ は $u$ がしきい値 $h$ を越えたときに $1$, そうでなければ 0 を出力するモデルのことをマッカロックとピッツの形式ニューロン (formal neuron) と呼ぶ。
マッカロック・ピッツの形式ニューロンは神経細胞の振る舞いを記述するもっとも古く、単純な神経細胞のモデルであるが、現在でも用いられることがある。

$$
z = \left\{ \begin{array}{ll}
 1, & \mbox{$u > 0$ のとき} \\
 0, & \mbox{それ以外}
 \end{array}\right.
$$

とすればマッカロック・ピッツのモデルは次式で表すことができる

$$ z=\mathbb{1}\left(\sum_{i=1}^nw_ix_i -h\right)\tag{3} $$

式中の $\mathbb{1}$ は数字ではなく 上式で表される関数の意味である。
このモデルは、単一ニューロンのモデルとしてではなく、ひとまとまりのニューロン群の動作を示すモデルとしても用いることがある。

<!--
### 出力が連続関数の場合

時間 $t$ における入力信号は $x_i(t)$ は $i$ 番目のシナプスの興奮伝達の時間 $t$ 付近での平均ととらえることができる。
すると、最高頻度の出力を 1, 最低(興奮無し)を 0 と規格化できると考えて $0\le f(\mu) \le1$ とする。
入出力関係は $f$ を用いて

$$ z = f(\mu) = f\left(\sum w_ix_i(t)-h\right)\tag{4} $$

のように表現される。
このモデルは、ニューロン集団の平均活動率ととらえることもできる。

良く用いられる出力関数 $f$ の形としては、$\mu = \sum w_ix_i -h$ として、

$$ f(\mu) = \frac{1}{1+e^{-\mu}},\tag{5} $$

や

$$ f(\mu) = \tanh(\mu)\tag{6}, $$

ただし $\mu = \sum w_{i}x_{i} -h$ などが使われることが多い。
(5) 式および (6) 式は、入力信号の重みつき荷重和 $\mu$ としてニューロンの活動が定まることを示している。
後述するバックプロパゲーション則で必要となるので、$\mu$ の微小な変化がニューロンの活動どのような影響を与えるか調べるために (5) 式 および (6) 式 を $\mu$ で微分することを考える。

$$ f(x) = \frac{1}{1+e^{-x}}, $$

を $x$ について微分すると

$$ \frac{df}{dx} = f(x)\left(1- f(x)\right) $$

$$ f(x) = \tanh{x} = \frac{e^{x}-e^{-x}}{e^{x}+e^{-x}} $$

を $x$ について微分すると

$$ \frac{df}{dx} =
1 - \tanh^2x = 1 - \left(f(x)\right)^2 $$

$\tanh$ は双曲線関数である。

以降では表記を簡単にするために線形数学の表記、すなわちベクトルと行列による表記方法を導入する。
$n$ 個の入力信号の組 $\left(x_1, x_2, \cdots, x_n\right)$ をまとめて $\mathbf{x}$ のようにボールド体で表す。本章では一貫してベクトル表記には小文字のボールド体を，行列には大文字のボールド体を用いることにする。
例えば $n$ 個の入力信号の組 $(x_1, x_2, \cdots, x_n)=\mathbf{x}$ に対して，同数の結合荷重 $\left(w_1, w_2, \cdots, w_n\right)=\mathbf{w}$ が存在するので，加算記号 $\sum$ を使って表現していた任意のニューロンへの全入力 $\mu=\sum w_{i}x_{i}$ はベクトルの内積を用いて $\mu=(\mathbf{w}\cdot\mathbf{x})$ と表現される。

なお，横一行のベクトルを行ベクトル，縦一列のベクトルを列ベクトルと呼ぶことがある。
ここでは行ベクトルと混乱しないように，必要に応じて列ベクトルを表現する際には $\{x_1, x_2, \cdots, x_n\}^{\top}=\mathbf{x}$ とベクトルの肩に $\top$ を使って表現することもある。

そして，これらをベクトル表現や行列表現で表せば，表記も簡単になり，行列の演算法則を活用することもできる。
そのため，ニューラルネットワークに関する文献でも行列表現が用いられることが多い。

図のような単純な 2 層の回路を例に説明する。

<center>
<img src="/assets/matrix-notation.svg"><br/>
ネットワークの行列表現
</center>

わかりやすいように図と対応させながら，対応する行列表現とシグマ記号による表記を併記するので，よく理解した上で先に読み進んでいただきたい。
なお，どうしても行列表現にはなじめないという読者は，行列表現の箇所だけをとばして読んでもある程度はわかるよう記述するつもりである。

それでは，まず図 4 のような単純な 2 層のネットワークを例に説明しよう。
図には、３つの入力素子 (ユニットと呼ばれることもある)
と ２ つの出力素子の活性値（ニューロンの膜電位に相当する）

$x_{1}, x_{2}, x_{3}$ と $y_{1}, y_{2}$，および入力素子と出力素子の結合強度を表す $w_{11}, w_{12}, \cdots, w_{32}$ が示されている。
これらの記号をベクトル $\mathbf{x}$, $\mathbf{y}$ と行列 $\mathbf{w}$ を使って表すと $\mathbf{y}=\mathbf{Wx}$ となる。

図\ref{fig:matrix-notation.eps}の場合、ベクトルと行列の各要素を書き下せば、
$$
\left(\begin{array}{l}y_{1}\\
y_2\\
\end{array}\right)
=\left(
\begin{array}{lll}
w_{11}&w_{12}&w_{13}\\
w_{21}&w_{22}&w_{23}
\end{array}
\right)
\left(
\begin{array}{l}
x_1\\
x_2\\
x_3\\
\end{array}
\right)
$$
のようになる。　　

行列の積は、左側の行列の $i$ 行目の各要素と右側の行列（ベクトルは１列の行列でもある）の $i$ 列目の各要素とを掛け合わせて合計することなので、以下のような、加算記号を用いた表記と同じである。

$$
\begin{array}{lllll}
y_1 &=& w_{11}x_1 + w_{12}x_2 + w_{13}x_3 &=&\sum_i w_{1i} x_i\\
y_2 &=& w_{21}x_1 + w_{22}x_2 + w_{23}x_3 &=&\sum_i w_{2i} x_i\\
\end{array}
$$

これを、$m$ 個の入力ユニットと $n$ 個の出力ユニットの場合に一般化すれば、
以下のようになる。

単純な 2 層のネットワークを考える。
$i$ 番目の出力層の各ニューロンの膜電位 $y_i,(i=1,2,\cdots,n)$ をまとめて $\mathbf{y}$ とベクトル表現し、同様に入力層も $\mathbf{x}$ とする。
ニューロン $x_{j}$ から ニューロン $y_{i}$ へのシナプス結合強度を $w_{ij}$ と表現すれば、入力層から出力層への関係は

$$
\left(\begin{array}{l}
y_1 \\ y_2 \\ \vdots \\ y_n \end{array}\right)  =
\left(\begin{array}{llll}
w_{11} & w_{12} & \cdots & w_{1m} \\
w_{21} & w_{22} & \cdots & w_{2m} \\
\vdots &        & \ddots & \vdots \\
w_{n1} & w_{n2} & \cdots & w_{nm}
\end{array}\right)
\left(\begin{array}{l}
x_1 \\ x_2 \\ \vdots \\ x_m \end{array}\right) \\
\mathbf{y} = \mathbf{Wx}
$$

と表現できる。
しきい値の扱いについては、常に 1 を出力する仮想的なニューロン$x_0=1$を
考えて $W$ に組み込むことも可能である。


実際の出力は $\mathbf{y}$ の各要素に対して

$$ f(y) = \frac{1}{1+e^{-y}}, $$

のような非線型変換を施すことがある。

階層型のネットワークにとっては上式，非線型変換が本質的な役割を果たす。
なぜならば、こうした非線形変換がなされない場合には、ネットワークの構造が何層になったとしても、この単純なシナプス結合強度を表す行列を
$\mathbf{W}_{i}$ ($i=1,\cdots, p$) としたとき、$\mathbf{W} = \prod_{i=1}^p \mathbf{W}_{i}$ と置くことによって本質的には 1 層のネットワークと等価になるからである。

$$ \mathbf{y} = \mathbf{W}_{p}\mathbf{W}_{p-1}\cdots\mathbf{W}_{1}\mathbf{y}=\left(\prod_{i=1}^p\mathbf{W}_{i}\right)\mathbf{y}. $$

<img src="/assets/xor.svg"><br/>

<img src="/assets/xor-graph.svg"><br/> -->

f
# 再帰型ニューラルネットワーク

<!-- ## 2.1. NETtalk
系列情報処理を扱った初期のニューラルネットワーク例として NETTalk が挙げられます。
NETTalk[^NETTalk] は文字を音読するネットワークです。下図のような構成になっています。
下図のようにアルファベット 7 文字を入力して，空白はアンダーラインで表現されています，中央の文字の発音を学習する 3 層のニューラルネットワークです。NETTalk は 7 文字幅の窓を移動させながら
逐次中央の文字の発音を学習しました。たとえば /I ate the apple/ という文章では
"the" を "ザ" ではなく "ジ" と発音することになります。

印刷単語の読字過程のニューラルネットワークモデルである SM89[^SM89], PMSP96[^PMSP96] で用いられた発音表現は <a target="_blank" href="https://en.wikipedia.org/wiki/ARPABET">ARPABET</a> の亜種です。Python では `nltk` ライブラリを使うと ARPABET の発音を得ることができます(<a target="_blank" href="https://github.com/ShinAsakawa/2019cnps/blob/master/notebooks/2019cnps_arpabet_test.ipynb">ARPABET のデモ<img src="/assets/colab_icon.svg"></a>)。

[^NETTalk]: Sejnowski, T.J. and Rosenberg, C. R. (1987) Parallel Networks that Learn to Pronounce English Text, Complex Systems 1, 145-168.
[^SM89]: Seidenberg, M. S. & McClelland, J. L. (1989). A distributed, developmetal model of word recognition and naming. Psychological Review, 96(4), 523–568.
[^PMSP96]: Plaut, D. C., McClelland, J. L., Seidenberg, M. S. & Patterson, K. (1996). Understanding normal and impaired word reading: Computational principles in quasi-regular domains. Psychological Review, 103, 56–115.

<center>
<img src="/assets/1986Sejnowski_NETtalkFig2.svg" style="width:47%"><br/>
Sejnowski (1986) Fig. 2
</center> -->

# 単純再帰型ニューラルネットワーク

<!-- NETTalk を先がけとして **単純再帰型ニューラルネットワーク** Simple Recurrent Neural networks (SRN) が提案された。 -->
発案者の名前で **Jordan ネット**，**Elman ネット** と呼ばれる。
<!-- [JordanNet]: Joradn, M.I. (1986) Serial Order: A Parallel Distributed Processing Approach, UCSD tech report.
[ElmanNet]: Elman, J. L. (1990)Finding structure in time, Cognitive Science, 14, 179-211. -->
Jordan ネットも Elman ネットも上位層からの **帰還信号** を持つ。
これを **フィードバック結合** と呼び，位置時刻前の状態が次の時刻に使われる。
Jordan ネットでは一時刻前の出力層の情報が用いられる (下図)。
一方，Elman ネットでは一時刻前の中間層の状態がフィードバック信号として用いられる。

<center>
<img src="/assets/SRN_J.svg" style="width:47%"><br/>
<div style="width:74%" align="center">
図：マイケル・ジョーダン発案ジョーダンネット [@1986Jordan]
</div>
</center>

<!-- - 駄菓子菓子 <a target="_blank" href="/assets/MJ_air.jpg">彼（マイケル・ジェフェリー(エアー)・ジョーダン）</a> ではない :)
- <a target="_blank" href="/assets/c3-s4-jordan.jpg">マイケル・アーウィン・ジョーダン。ミスター機械学習[^jordan_ai_revolution_not_yet]</a> -->
<!-- [^jordan_ai_revolution_not_yet]: 彼は(も？)神様です。多くの機械学習アルゴリズムを提案し続けている影響力のある人です。長らく機械学習の国際雑誌の編集長でした。2018年 <a target="_blank" href="https://medium.com/@mijordan3/artificial-intelligence-the-revolution-hasnt-happened-yet-5e1d5812e1e7">AI 革命は未だ起こっていない</a> と言い出して議論を呼びました。
-->

<center>
<img src="/assets/SRN_E.svg" style="width:47%"><br/>
<div style="align:center; width:47%">
図：ジェフ・エルマン発案のエルマンネット[@lman1990],[@Elman1993]
</div>
</center>

どちらも一時刻前の状態を短期記憶として保持して利用するのですが，実際の学習では一時刻前の状態をコピーして保存しておくだけで，実際の学習では通常の **誤差逆伝播法** すなわちバックプロパゲーション法が用いられる。
上 2 つの図に示したとおり U と W とは共に中間層への結合係数であり，V は中間層から出力層への結合係数である。
Z=I と書き点線で描かれている矢印はコピーするだけですので学習は起こりません。このように考えれば SRN は 3 層のニューラルネットワークであることが分かる。

SRN はこのような単純な構造にも関わらず **チューリング完全** であろうと言われてきた。
すなわちコンピュータで計算可能な問題はすべて計算できるくらい強力な計算機だという意味である。

- Jordan ネットは出力層の情報を用いるため **運動制御** に
- Elan ネットは内部状態を利用するため **言語処理** に

それぞれ用いられる。
従って **失行** aparxia (no matter what kind of apraxia such as 'ideomotor' or 'conceptual')，**行為障害** のモデルを考える場合 Jordan ネットは考慮すべき選択肢の候補の一つとなるだろう。

## リカレントニューラルネットワークの時間展開

一時刻前の状態を保持して利用する SRN は下図左のように描くことができる。
同時に時間発展を考慮すれば下図右のように描くことも可能である。

<center>
<img src="/assets/RNN_fold.svg" style="width:49%"><br/>
Time unfoldings of recurrent neural networks
</center>

上図右を頭部を 90 度右に傾けて眺めてみよ。
あるいは同義だ上図右を反時計回りに 90 度回転させたメンタルローテーションを想像してほしい。
このことから **"SRN とは時間方向に展開したディープラーニングである"** ことが分かる。

<!-- ## 2.4. エルマンネットによる言語モデル

下図に <a target="_blank" href="/assets/Elman_portrait.jpg">エルマン</a> が用いたネットワークモデルを示しました。
図中の数字はニューロンの数を表します。入力層と出力層のニューロン数 26 とは，もちいた語彙数が 26 であったことを表します。

<center>
<img src="/assets/1991Elman_starting_small_Fig1.svg" style="width:47%"><br/>
from [@Elman1991startingsmall]
</center>

エルマンは，系列予測課題によって次の単語を予想することを繰り返し学習させた結果，文法構造がネットワークの結合係数として学習されることを示しました。Elman ネットによって，埋め込み文の処理，時制の一致，性や数の一致，長距離依存などを正しく予測できることが示されました(Elman, 1990, 1991, 1993)。

- S     $\rightarrow$  NP VP “.”
- NP    $\rightarrow$  PropN | N | N RC
- VP    $\rightarrow$  V (NP)
- RC    $\rightarrow$  who NP VP | who VP (NP)
- N     $\rightarrow$  boy | girl | cat | dog | boys | girls | cats | dogs
- PropN $\rightarrow$  John | Mary |
- V     $\rightarrow$  chase | feed | see | hear | walk | live | chases | feeds | seeds | hears | walks | lives

これらの規則にはさらに 2 つの制約があります。

1. N と V の数が一致していなければならない
2. 目的語を取る動詞に制限がある。例えばhit, feed は直接目的語が必ず必要であり，see とhear は目的語をとってもとらなくても良い。walk とlive では目的語は不要である。

文章は 23 個の項目から構成され，8 個の名詞と 12 個の動詞，関係代名詞 who，及び文の終端を表すピリオドです。この文法規則から生成される文 S は，名詞句 NP と動詞句 VP と最後にピリオドから成り立っている。
名詞句 NP は固有名詞 PropN か名詞 N か名詞に関係節 RC が付加したものの何れかとなります。
動詞句 VP は動詞 V と名詞句 NP から構成されるが名詞句が付加されるか否かは動詞の種類によって定まる。
関係節 RC は関係代名詞 who で始まり，名詞句 NP と動詞句 VP か，もしくは動詞句だけのどちらかかが続く，というものです。

下図に訓練後の中間層の状態を主成分分析にかけた結果を示しました。"boy chases boy", "boy sees boy", および "boy walks" という文を逐次入力した場合の遷移を示しています。
同じ文型の文章は同じような状態遷移を辿ることが分かります。 -->

<!-- <center>
<img src="/assets/1991Elman_Fig3.jpg" style="width:49%"><br/>
<p align="left" style="width:47%">
<!-- Trajectories through state space for sentences boy chases boy, boy sees boy, boy walks.
Principal component 1 is plotted along the abscissa; principal component 3 is plotted along the ordinate.
These two PC’s together encode differences in verb-argument expectations.
</p>
</center> -->

<!-- <img src="/assets/1991Elman_Fig4a.jpg" style="width:84%"><br> -->

<!-- 下図は文 "boy chases boy who chases boy" を入力した場合の遷移図です。この文章には単語 "boy" が 3 度出てきます。それぞれが異なるけれど，他の単語とは異なる位置に附置されていることがわかります。
同様に 'chases" が 2 度出てきますが，やはり同じような位置で，かつ，別の単語とは異なる位置に附置されています。<br/>

<center>
<img src="/assets/1991Elman_Fig4b.jpg" style="width:49%"><br/>
</center>

同様にして "boy who chases boy chases boy" (男の子を追いかける男の子が男の子を追いかける) の状態遷移図を下図に示しました。<br/>
<center>

<img src="/assets/1991Elman_Fig4c.jpg" style="width:48%"><br/>
</center>

さらに複雑な文章例 "boy chases boy who chases boy who chases boy" の状態遷移図を下図に島します。</br>
<center>

<img src="/assets/1991Elman_Fig4d.jpg" style="width:48%"><br/>
</center>

Elman ネットが構文，文法処理ができるということは上図のような中間層での状態遷移で同じ単語が異なる文位置で異なる文法的役割を担っている場合に，微妙に異なる表象を，図に即してで言えば， 同じ単語では，同じような場所を占めるが，その文法的役割によって異なる位置を占めることが示唆されます。
このことから中間層の状態は異なる文章の表現を異なる位置として表現していることが考えられ，後述する **単語の意味** や **自動翻訳** などに使われることに繋がります(浅川の主観半分以上) -->

<!--
<p align="left" style="width:74%">
Movement through state space for sentences with relative clauses. Principal component 1 is displayed along the abscissa; principal component 11 is displayed along the ordinate. These two PC’s encode depth of embedding in relative clauses.
</p>
</center>
-->

<!-- ## 2.5. Seq2sep 翻訳モデル

上記の中間層の状態を素直に応用すると **機械翻訳** や **対話** のモデルになります。
下図は初期の翻訳モデルである "seq2seq" の概念図を示しました。
"`<eos>`" は文末 end of sentence を表します。中央の "`<eos>`" の前がソース言語であり，中央の "`<eos>`" の後はターゲット言語の言語モデルである SRN の中間層への入力として用います。

注意すべきは，ソース言語の文終了時の中間層状態のみをターゲット言語の最初の中間層の入力に用いることであり，それ以外の時刻ではソース言語とターゲット言語は関係がないことです。
逆に言えば最終時刻の中間層状態がソース文の情報全てを含んでいるとみなすことです。
この点を改善することを目指すことが 2014 年以降盛んに行われてきました。
顕著な例が後述する **双方向 RNN**， **LSTM** を採用したり，**注意** 機構を導入することでした。 -->

<!--
<center>
<img src="/assets/RNN_fold.svg" style="width:94%"></br>
Time unfoldings of recurrent neural networks
</center>
-->

<center>
<img src="/assets/2014Sutskever_S22_Fig1.svg" style="width:88%"><br/>
From [@2014Sutskever_Sequence_to_Sequence]
</center>
<!--
$$
\mbox{argmax}_{\theta}
\left(-\log p\left(w_{t+1}\right)\right)=f\left(w_{t}\vert \theta\right)
$$ -->

## 多様な RNN とその万能性
双方向 RNN や LSTM を紹介する前に，カルパシーのブログから下図に引用する。
下の 2 つ図ではピンク色が入力層，緑が中間層，青が出力層を示している。

<!-- [^karpathy]: 去年までスタンフォード大学の大学院生。
現在はステラ自動車，イーロン・マスクが社長，の AI 部長さんです。図は彼のブログから引用です。蛇足ですがブログのタイトルが unreasonable effectiveness of RNN です。
過去の偉大な論文 Wiegner (1960), Hamming (1967), Halevy (2009) からの <del>パクリ</del> **敬意を表したオマージュ**です。
"unreasonable effectiveness of [science|mathematics|data]" $\ldots$ www -->

<center>
<img src="/assets/diags.jpeg" style="width:77%"><br/>
RNN variations from <http://karpathy.github.io/2015/05/21/rnn-effectiveness/>
</center>

- 上図最左は通常の多層ニューラルネットワークで画像認識，分類，識別問題に用いられます。
- 上図左から 2 つ目は，画像からの文章生成
- 上図中央，左から 3 つ目は，極性分析，文章のレビュー，星の数推定
- 上図右から 2 つ目は翻訳や文章生成
- 上図最右はビデオ分析，ビデオ脚注付け

などに用いられます。これまで理解を促進する目的で中間層をただ一層として描いてきた。
だが中間層は多層化されていることの方が多いこと，中間層各層のニューロン数は 1024 程度まで用いられていることには注意。

数は各層のニューロン数が 4 つである場合の数値例を示しています。入力層では **ワンホット** 表現が用いられている。
<!-- [^onehot]: ベクトルの要素のうち一つだけが "1" であり他は全て "0” である疎なベクトルのこと。一つだけが "熱い" あるいは "辛い" ベクトルと呼びます。以前は one-of-$k$ 表現 (MacKay の PRML など) と呼ばれていたのですが ワンホット表現，あるいは ワンホットベクトル (おそらく命名者は Begnio 一派)と呼ばれることが多いです。ワンホットベクトルを学習させると時間がかかるという計算上の弱点が生じます。典型的な誤差逆伝播法による学習では，下位層の入力値に結合係数を掛けた値で結合係数を更新します。従って，下位層の値のほとんどが "0" であるワンホットベクトルは学習効率が落ちることになります。そこで Elman はワンホットベクトルを実数値を持つ多次元ベクトルに変換してから用いることを行いました。上のエルマンネットによる文法学習において,ニューロン数 10 の単語埋め込み層と書かれた層がこれに該当します。単語埋め込み層を用いることで学習効率が改善し，後に示す word2vec などの **分散ベクトルモデル** へと発展します。 -->

## おまけ，ブロードマン (Brodman) の脳地図

1910 年の論文に掲載された図。左図が，左脳を外側から眺めた図，右図は右脳を内側から眺めた図である。
<center>
<img src="/2023assets/2001榎_杉下_Brodmann2010upper.svg" width="44%">
<img src="/2023assets/2001榎_杉下_Brodmann2010lower.svg" width="44%">
</center>

1909 年の論文に掲載された図。大抵の教科書はこちらを使っていると指摘する文献が多数ある。
理由は不明。
<center>
<img src="/2023assets/1909BroadmannP131upper.svg" width="44%">
<img src="/2023assets/1909BroadmannP131lower.svg" width="44%">
</center>

12-16, 52 野は欠番である。


<!-- <center>
<img src="/assets/charseq.jpeg" style="width:66%"><br/>
RNN variations from <http://karpathy.github.io/2015/05/21/rnn-effectiveness/>
</center>

[@1991Siegelmann_RNN_universal] said Turing completeness of RNN.

- [用語集](/2023/2023lect03_glossary){:target="_blank"}

## 実習

- [実習 画像認識 Keras 版<img src="https://komazawa-deep-learning.github.io/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2021Kera_CNN_demo_with_wordnet_ja.ipynb) -->
<!-- - [実習 Keras CNN](https://colab.research.google.com/github/ShinAsakawa/2019komazawa/blob/master/notebooks/nothotdog.ipynb){:target="_blank"}
- [実習 Kermack McKendric model<img src="https://komazawa-deep-learning.github.io/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2021Kermack_McKendrick_model.ipynb){:target="_blank"} -->
<!-- - [実習 PyTorch CNN <img src="https://komazawa-deep-learning.github.io/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0416PyTorch_CNN_demo.ipynb){:target="_blank"}
<!--- [実習](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2021Kermack_McKendrick_model.ipynb#scrollTo=oD497lby40Fp)-->

<!-- - [実習 画像認識 Keras 版](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2021Kera_CNN_demo_with_wordnet_ja.ipynb) -->
<!-- - [実習 Keras CNN](https://colab.research.google.com/github/ShinAsakawa/2019komazawa/blob/master/notebooks/nothotdog.ipynb){:target="_blank"} -->
<!-- - [実習 PyTorch CNN](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0416PyTorch_CNN_demo.ipynb){:target="_blank"} -->
<!-- - [実習 Kermack McKendric model](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2021Kermack_McKendrick_model.ipynb){:target="_blank"}-->
<!--- [実習](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2021Kermack_McKendrick_model.ipynb#scrollTo=oD497lby40Fp)-->


<!-- - CNN: 畳み込みニューラルネットワーク
- RNN: リカレントニューラルネットワーク
- RL: 強化学習-->

<!-- <center> -->
<!--  <img src="https://komazawa-deep-learning.github.io/assets/2008Fuster_Prefrontal_Cortex_fig8_4.svg" width="39%"> -->
<!--  <img src="https://komazawa-deep-learning.github.io/assets/2015Ronneberger_U-Net_Fig1_ja.svg" width="48%"> -->
<!-- </center> -->

<!-- - [2018Kriegeskorte](2018Kriegeskorte){:target="_blank"}
- [1970Newell](1970Newell){:target="_blank"}
- [2019Glaser](2019Glaser){:target="_blank"}
- [2020Lindsay](2020Lindsay){:target="_blank"}
- [G 検定](https://www.seshop.com/product/detail/23864?utm_source=seid_it_spot_20210412&utm_medium=email&utm_campaign=coupon){:target="_blank"}

### 2021年02月23日分
- [2020-0215](2020-0215abstract){:target="_blank"}
- [どうぶつの森モデル，動物の名前連想モデル](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2021_0223word_associtaion.ipynb){:target="_blank"}
- [導入講義用 CCP ウィルス感染者予測モデルを題材に](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2021Kermack_McKendrick_model.ipynb){:target="_blank"}
- [CNN の簡単なデモ](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2021Keras_CNN_demo_with_wordnet_ja.ipynb){:target="_blank"}

# 統計学と機械学習の関係

母集団における差異の有無を問題にする心理統計学と機械学習との間には，決定的な差があります。

- [1970Newell](1970Newell){:target="_blank"}
- [2019Glaser](2019Glaser){:target="_blank"}
- [2020Lindsay](2020Lindsay){:target="_blank"}

1. [tSNE を用いた TLPA 200語の word2vec 視覚化](https://ShinAsakawa.github.io/2020cnps_tSNE_for_word2vec.ipynb)
2. [2020年2月24日資料1 tlpa 画像](https://ShinAsakawa.github.io/2020making_tlpa.html)


<a href="https://guides.github.com/features/pages/">Read this page to write this page.</a>-->
