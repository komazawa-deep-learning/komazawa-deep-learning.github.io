---
title: 第12回 2025 年度開講 駒澤大学 心理学特講 IIIA
author: 浅川 伸一
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="center">
<font size="+2" color="navy"><strong>ディープラーニングの心理学的解釈</strong></font><br/><br/>
</div>

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br/>
Date: 11/Jul./2025<br/>
Appache 2.0 license<br/>
</div>

* [課題提出用フォルダ](https://drive.google.com/drive/u/3/folders/1w70ys8I6HejtPlmHgkwB_O4aKvk_eTH1){:target="_blank"}

# 第 12 回

* [文字音読モデル <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2025notebooks/2025_0626psylex71_CDP%2Bja1.ipynb){:target="_blank"}
* [百人一首の上の句とエンコーダによって符号化し，下の句をデコーダで生成する自作 Transformer モデル <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2023notebooks/2023_1113chihaya_Transformer.ipynb){:target="_blank"}
* [文ベクトルの類似度計算 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_1025sentence_similarity_by_SBERT.ipynb){:target="_blank"}



<!-- <center>
<img src="http://www.newscientist.com/wp-content/uploads/2003/03/dn3488-1_602.jpg" width="49%"><br/>
</center> -->

## 先週の補足 意味ベクトルの応用例

<center>
<img src="/assets/2008Mitchell_fig1ja.svg" style="width:77%"><br/>
Mitchell et al (2008) Fig. 1 を改変
</center>


<center>
<img src="/assets/2019Jat_Mitchell_fig1.svg" style="width:74%;"><br/>
<img src="/assets/2019Jat_Mitchell_fig4.svg" style="width:84%"><br/>
</center>

<div class="figcaption">
上：MEG データの符号化モデル。1  単語あたり 306 チャンネルで  500ms 間の MEG 信号は、100ms 区間のデータを平均して 306x5 に圧縮された。この MEG 脳記録データは、リッジ回帰を用いてテキスト表現ベクトルから脳活動に符号化された。評価は  5 交差検証を用いて行われた。<br/>
下: いくつかの選択された深層ニューラルネットワークモデル層からのさまざまな脳領域対ごとの精度。言語理解の中心と考えられている脳の左側が、特に左側頭葉で高い精度で予測されている。（L = 左、R = 右）
</div>

### NIC (Neural Caption Generation)

<center>
<img src="/assets//17VISIOn-slide-WBE2-jumbo.jpg" width="49%"><br/>
- 人間: A group of men playing Frisbee in the park.
- 機械: A group of young people playing a game of Frisbee.
</center>

<img src="/assets/2014Vinyals_Fig5_left.jpg" width="44%">
<img src="/assets/2014Vinyals_Fig5_right.jpg" width="44%"><br/>
Vinyals et. al (2014) より

# Transformer, [Attention is all you need](https://arxiv.org/abs/1706.03762)

単語の多義性解消のために，あるいは単語のベクトル表現を超えて，より大きな意味単位である，句，節，文のベクトル表現を得る努力がなされてきた。
適切な普遍文表現ベクトルを得ることができれば，翻訳を含む多くの下流課題にとって有効だと考えられる。

そこで，注意機構を積極的に取り込んだゲームチェンジャーが Transformer である。


* 注意を用いて，RNN を置き換える [Devlin+2017,Attention Is All You Need](https://arxiv.org/abs/1706.03762)
* Transformer の注意とは，このソフトマックス関数である。
* 専門用語としては，**多頭=自己注意** Multi-Head Self-Attention (以下 MHSA と表記)と呼ぶ。
* **自己** がつく注意である理由は，トップダウン信号がないためであろう。
* 上図，クエリ，キー，バリュー ，意味としては，問い合わせ，キー（鍵），値，であるが，とりわけ，Q と K との間に明確な相違はない。
* ある問い合わせ Q に対して，キー K を与えて，その答え A となる値を得ることに相当する。
* この操作を入力情報から作り出して答えを出力する仕組みに，ワンホット表現を使う。

<!-- 下図左は上図右と同じものです。この下図右を複数個束ねると下図中央になります。 -->

- 図中央の Scaled Dot-Product Attention と書かれた右脇に小さく h と書かれている。この h とは ヘッド の意味。
- 図中央を 1 つの単位として，次に来る情報と連結させる。図右。
- リカレントニューラルネットワークでは，中間層の状態が次の時刻の処理に継続して用いられていた。
- ところが 多頭=自己注意 MHSA では一つ前の入力情報を，現在の時刻の情報に対するクエリとキーのように扱って情報を処理する。
- 図右の下から入力される情報は，input と output と書かれている。
さらに output の下には (Shifted right) と書かれています。
すなわち，時系列情報を一時刻分だけ右にずらし（シフト）させて逐次情報を処理することを意味している。
- 図右の下から入力される情報は，embedding つまり埋め込み表現 と 位置符号化 position embedding が足し合わされたもの。
埋め込み表現とは先週 word2vec で触れたベクトルで表現された，単語（あるいはそれぞれの項目）の 意味表現 に対応。

<div class="pagebreak"></div>

#### Transformer の概略図

<div class="figcenter">
<img src="/2023assets/2017Vaswani_Fig2_1ja.svg" width="15%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="/2023assets/2017Vaswani_Fig2_2ja.svg" width="25%">&nbsp;&nbsp;&nbsp;
<img src="/assets/2017Vaswani_Fig1.svg" width="25%">
<div class="figcaption">

Transformer [2017Vaswani++](https://arxiv.org/abs/1706.03762) Fig.2 を改変。
`matmul` は行列の積，`scale` は，平均 0 分散 1 への標準化，`mask` は 0 と 1 とで，データを制限すること，`softmax` はソフトマックス関数
</div></div>
Transformer における注意 = ソフトマックス関数。<br/>

<div class="pagebreak"></div>

### Transformer における位置符号化器 (PE: position encoders)

$$
\text{PE}_{(\text{pos},2i)} = \sin\left(\frac{\text{pos}}{10000^{\frac{2i}{d_{\mathop{model}}}}}\right)
$$

$$
\mathop{PE}_{(\mathop{pos},2i+1)} = \cos\left(\frac{\mathop{pos}}{10000^{\frac{2i}{d_{\mathop{model}}}}}\right)
$$

<div class="figcenter">
<img src="/2024assets/2023_0723PE_Transformer_curves.png" width="77%">
<div class="figcaption" style="width:55%">

Transformer の位置符号化器の出力。
Transformer は位置情報を持たないので，位置情報を周波数変換して用いる。
</div></div>

<div class="pagebreak"></div>

### 事前訓練

#### マスク化言語モデル

<div class="figcenter">
<img src="/2024assets/2019Lample_Fig1.svg" width="55%">
</div>

#### 次文予測課題

言語モデルの欠点を補完する目的，次の文を予測

[SEP] トークンで区切られた 2 文入力

- 入力: the man went to the store [SEP] he bought a gallon of milk.
- ラベル:  IsNext
- 入力:  the man went to the store [SEP] penguins are flightless birds.
- ラベル:  NotNext

#### ファインチューニング GLUE 課題 (General Language Understanding Evaluation)

- **CoLA**: 入力文が英語として正しいか否かを判定
- **SST-2**: スタンフォード大による映画レビューの極性判断
- **MRPC**: マイクロソフトの言い換えコーパス。2 文 が等しいか否かを判定
- **STS-B**: ニュースの見出し文の類似度を5段階で評定
- **QQP**: 2 つの質問文の意味が等価かを判定
- **MNLI**: 2 入力文が意味的に含意，矛盾，中立を判定
- **QNLI**: 2 入力文が意味的に含意，矛盾，中立を判定
- **RTE**: MNLI に似た2つの入力文の含意を判定
- **WNI**: ウィノグラッド会話チャレンジ

### ファインチューニング手続きによる性能比較

マスク化言語モデルのマスク化割合は マスクトークン:ランダム置換:オリジナル=80:10:10 だけでなく，他の割合で訓練した場合の 2 種類下流課題，
MNLI と NER で変化するかを下図 に示した。
80:10:10 の性能が最も高いが大きな違いがあるわけではないようである。

<div class="figcenter">
<img src="/assets/2019Devlin_mask_method21.jpg" width="49%"><br/>
</div>
<div class="figcaption">
マスク化言語モデルのマスク化割合の違いによる性能比較
</div>

<div class="pagebreak"></div>

#### モデルサイズ比較

<div class="figcenter">
<img src="/assets/2019Devlin_model_size20.jpg" width="59%"><br/>
</div>
<div class="figcaption">
モデルのパラメータ数による性能比較
</div>

パラメータ数を増加させて大きなモデルにすれば精度向上が期待できる。
下図では，横軸にパラメータ数で MNLI は青と MRPC は赤 で描かれている。
パラメータ数増加に伴い精度向上が認められる。
図に描かれた範囲では精度が天井に達している訳ではない。
パラメータ数が増加すれば精度は向上していると認められる。

#### モデル単方向，双方向モデル比較

<div class="figcenter">
<img src="/assets/2019Devlin_directionality19.jpg" width="59%"><br/>
</div>
<div class="figcaption">
言語モデルの相違による性能比較
</div>

<!-- 言語モデルをマスク化言語モデルか次単語予測の従来型の言語モデルによるかの相違による性能比較を下図に示した。
横軸には訓練ステップである。訓練が進むことでマスク化言語モデルとの差は 2 パーセントではあるが認められるようである。 -->

## Transformer (SBERT) の文ベクトル

先に紹介した word2vec は，単語ベクトルを得る手法であるが，Transformer は文ベクトルを扱う。
そこで，文単位での類似性を検討した。
下の画像に対して，5 つの脚注がある。

<center>
<img src="/assets/coco175469.jpg" width="55%"><br/>
</center>

1. 夕暮れのハーバーに汽船と複数の鳥が浮かんでいる
2. 水面に浮かぶ4羽の水鳥と、その向こうに停泊している2隻の船
3. 船着き場に2艘の船がとまっている
4. 朝焼けの中待機場所にある旅客船とマガモ
5. 停められた船の近くで水鳥が泳いでいる<br/>
MS COCO データセットより: <http://farm5.staticflickr.com/4055/4704393899_a041476b4a_z.jpg>

上図は，MS COCO 画像データと画像に対応する脚注からなるデータセットからの一例である。
日本語文は，千葉工業大学 STAIRLABO が公開しているデータである。
人間が見れば，写真と文章とは結びいていることが分かる。
加えて，5 つの脚注も相互に似ていることが分かる。
MS COCO データセットでは，一枚の写真に 5 つの脚注が紐付けられている。

コンピュータにこれらの文章が似ていることを判断させようとすると，最近まで難しい仕事であった。
本章で紹介する，文の意味ベクトルを用いると，これらの文章が相互に似ていると判断させることが可能である。
下図は tSNE を用いて，日本語の文章の類似度を sentence BERT を用いて表現し，文章の類似度に従って地図を描いたものである。
図では，同じ写真に紐付いている文章は同じ色で表現している。

<center>
<img src="/2024assets/2022_0915sbert_staircoco500.svg" style="width:77%">
</center>

<div class="pagebreak"></div>

<!--# マルチタスク学習，転移学習

- 学習したことがらを応用することは賢さの尺度であろう。

たとえば，映画[カラテキッド](https://youtu.be/DsLk6hVBE6Y)(1984)では，ミヤギ先生はダニエルさんに車のワックスがけや床掃除を教えました :-) ワックスがけや床磨きは空手の技術習得にとって必要な技能であったというオチです。

## 実習ファイル

- [マルチタスク学習2 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2020_0703four_in_one_network2.ipynb){target="_blank"}
- [マルチタスク学習3 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2020_0703four_in_one_network3.ipynb){target="_blank"}

    1. 画像脚注付け<br>
    ![](https://twitter.com/paraschopra/status/1096710728092995584/photo/1){target="_blank"}
    2. 類義語<br>
    ![](https://cdn-images-1.medium.com/max/1280/1*tWrGWKXwWMbuocw2nXBysA.png){target="_blank"}
    3. 類義画像<br>
    ![](https://cdn-images-1.medium.com/max/1280/1*NZSJiMUMQi9u07oA6vI9cA.png){target="_blank"}
    4. 文章からの画像検索
        - __犬__を検索<br>
    ![犬](https://cdn-images-1.medium.com/max/1280/1*VmIgBrrr-3XwGGwoXwiQMg.png){target="_blank"}<br>
        - __笑顔の少年__ を検索<br>
    ![笑顔の少年](https://cdn-images-1.medium.com/max/1280/1*4Km1YpfFbwhRF8Obu54EaA.png){target="_blank"}<br>

---

- [マーガレット ミッチェルによるソーシャルメディアを用いたメンタルヘルスのマルチタスク学習](http://m-mitchell.com/publications/multitask-blurb.html){target="_blank"}
    - [arXiv 論文](https://arxiv.org/abs/1712.03538){target="_blank"}
- [One neural network, many uses](https://towardsdatascience.com/one-neural-network-many-uses-image-captioning-image-search-similar-image-and-words-in-one-model-1e22080ce73d){target="_blank"}
    - [ソースコード](https://github.com/paraschopra/one-network-many-uses){target="_blank"}
    - [An Overview of Multi-Task Learning in Deep Neural Networks](http://ruder.io/multi-task/){target="_blank"}
    - [上の arXiv](https://arxiv.org/abs/1706.05098){target="_blank"}

---

### Hard parameter sharing

<center>
<img src="http://ruder.io/content/images/2017/05/mtl_images-001-2.png" style="width:44%">
<img src="http://ruder.io/content/images/size/w2000/2019/03/transfer_learning_taxonomy-1.png" style="width:44%"><br>
左:マルチタスク学習, 右:転移学習, いずれも Sebastuan Ruder のブログより<br>
</center>

---

### Soft parameter sharing

In soft parameter sharing on the other hand, each task has its own model with its own parameters.
The distance between the parameters of the model is then regularized in order to encourage the parameters to be similar. [8]
for instance use the $l2$ norm for regularization, while [9] use the trace norm.

- [8]: Duong, L., Cohn, T., Bird, S., & Cook, P. (2015). Low Resource Dependency Parsing: Cross-lingual Parameter Sharing in a Neural Network Parser. Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Short Papers), 845–850.
- [9]: Yang, Y., & Hospedales, T. M. (2017). Trace Norm Regularised Deep Multi-Task Learning. In Workshop track - ICLR 2017. Retrieved from http://arxiv.org/abs/1606.04038

![](http://ruder.io/content/images/size/w2000/2017/05/mtl_images-002-2.png)

---

# Recent work on MTL for Deep Learning

### Deep Relationship Networks
![](http://ruder.io/content/images/2017/05/relationship_networks.png)
__A Deep Relationship Network with shared convolutional and task-specific fully connected layers with matrix priors (Long and Wang, 2015).__

- Long, M., & Wang, J. (2015). Learning Multiple Tasks with Deep Relationship Networks. arXiv Preprint arXiv:1506.02117. Retrieved from http://arxiv.org/abs/1506.02117 ↩︎

---

### Fully-Adaptive Feature Sharing
![](http://ruder.io/content/images/2017/05/fully_adaptive_feature_sharing.png)<br>
__The widening procedure for fully-adaptive feature sharing (Lu et al., 2016).__

Lu, Y., Kumar, A., Zhai, S., Cheng, Y., Javidi, T., & Feris, R. (2016). Fully-adaptive Feature Sharing in Multi-Task Networks with Applications in Person Attribute Classification. Retrieved from http://arxiv.org/abs/1611.05377

---

### Cross-stitch Networks
![](http://ruder.io/content/images/2017/05/cross-stitch_networks.png)<br>
__Cross-stitch networks for two tasks (Misra et al., 2016).__

Misra, I., Shrivastava, A., Gupta, A., & Hebert, M. (2016). Cross-stitch Networks for Multi-task Learning. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. https://doi.org/10.1109/CVPR.2016.433


<!--
### Low supervision

Søgaard, A., & Goldberg, Y. (2016). Deep multi-task learning with low level tasks supervised at lower layers. Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics, 231–235.

---

## A Joint Many-Task Model
![](http://ruder.io/content/images/2017/05/joint_many_task_model.png)<br>
__A Joint Many-Task Model (Hashimoto et al., 2016).__

---

### Weighting losses with uncertainty
![](http://ruder.io/content/images/2017/05/weighting_using_uncertainty.png)<br>
__Uncertainty-based loss function weighting for multi-task learning (Kendall et al., 2017).__

Kendall, A., Gal, Y., & Cipolla, R. (2017). Multi-Task Learning Using Uncertainty to Weigh Losses for Scene Geometry and Semantics. Retrieved from http://arxiv.org/abs/1705.07115

---

### Sluice Networks
![](http://ruder.io/content/images/2017/05/sluice_network-003.png)<br>
__A sluice network for two tasks (Ruder et al., 2017).__

Ruder, S., Bingel, J., Augenstein, I., & Søgaard, A. (2017). Sluice networks: Learning what to share between loosely related tasks. Retrieved from http://arxiv.org/abs/1705.08142
-->

