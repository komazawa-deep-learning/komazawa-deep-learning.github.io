---
title: 2021年度 駒澤大学 認知心理学研究 II (b)
layout: home
---


<img src="figures/qrcode.png">

- 授業名: 認知心理学研究 II (b)
- 担当者名: 永田 陽子, 竹市 博臣, 浅川 伸一 (アサカワ シンイチ) なおこのページは，浅川個人が管理しているページです。
- 電子メールアドレス: <educ20233@komazawa-u.ac.jp>, <asakawa@cis.twcu.a.jp>
- 開講年度・期:　2021年 後期
- 開講曜日・時限: 金曜日 2 限 10:40-12:10
- 教室: 第一研究館 1307 永田研究室
- 単位数　2
- オフィスアワー: なし，メールや SNS を活用してください。駒澤大学の専任ではありません。
非常勤講師ですので，金曜日の 1 時限だけしか駒澤大学には居ません。

---

- [はじめての colab による画像認識 <img src="https://komazawa-deep-learning.github.io/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021komazawa_cogsy000_CNN_demo.ipynb){:target="_blank"}


* [**第 4 回**](lect04){:target="_blank"} 授業の計画・内容 【浅川：畳み込みニューラルネットワークによる特徴抽出】第２講パターン認知の知識に基づき，畳み込みニューラルネットワークによる特徴抽出の実装とその意味について考える。生体が行う視覚情報処理に触発されて福島が提案したネオコグニトロンから，現在の畳み込みニューラルネットワークによる物体認識に至る道筋を確認します。畳み込み，スキップ結合，ドロップアウト，などの概念と生理学的対応物について議論します。 
    * 準備学習（予習・復習等）  YouTube上で以下のキーワードで検索し，結果の幾つか最初の数分ほどを視聴し，その内容を 1, 2行で要約してださい。キーワード : deeplearning, beginners, tutorial 60分 
* [**第 5 回**](lect05){:target="_blank"} 授業の計画・内容 【浅川：意味的領域切り出し，および，汎光学的領域切り出しとクラス関連記憶】第３講不良設定問題と自然制約条件を踏まえて，環境からの不変項を抽出するための技法について議論します。また，生理学で言及される背側経路と腹側経路との情報処理経路の役割分担の実装について実習します。画像切り出しに用いられる技法の心理学的意味を考察したのち，クラス関連記憶からの示唆について考察を加えます。 
    * 準備学習（予習・復習等） 自身の使っている PCで，画像の一部を切り取り，あるいはトリミングする方法を調べ，実際に切り取った画像を保存してください。60分画像のうち一枚は正面から撮影された顔画像である必要があります。（操作に習熟しているか否かで作業に要する時間は異なりますが60分程度でしょう） 
* [**第 8 回**](lect08){:target="_blank"} 授業の計画・内容 【浅川：転移学習とファインチューニング，顔認識実演】顔認識実演：訓練済の顔認識プログラムのコードを用いる。履修者は，顔のキーポイントを抽出して，各パーツを切り出す。切り出したパーツを元にシャッフル顔を作成しする。作成した画像を認識プログラムに入力し，出力結果を得る。結果を検討，考察の上レポートを作成し提出する。 
準備学習（予習・復習等） 転移学習に関する PyTorch のチュートリアルに目を通しておいてください。
* [**第 12 回**](lect12){:targret="blank"} 授業の計画・内容 【浅川：視覚と言語の双方で用いられる共通の注意メカニズム】第９講で学習した注意の発展を考える。注意機構を実装することでニューラルネットワークは精度向上が認められた。このため注意は複数の分野で採用される基本構成単位となっている。直接的な出発点は，自然言語処理分野での注意機構，すなわちトランスフォーマー論文(2018年 )である。トランスフォーマーで提唱されたマルチヘッド自己注意は，画像処理にも波及している。このことから，注意機構は認知処理を考える上で鍵となる概念であろう。眼球運動実演について： DeepGaze IIIや CAMなど事前訓練された眼球運動のシミュレーションプログラムプログラムを用いる。履修者は，自身の研究テーマに関連する画像を用意して，（なければロールシャッハ図版などでも可）実施する。パラメータを調整することで，特徴ある眼球運動が誘発できるかどうかをレポートする。余力があれば，サッケード抑制，アンチサッケードなどの刺激図版を使って，結果を観察しレポートを作成し提出する
    * 準備学習（予習・復習等）成し提出する。
注意に関する心理実験や神経心理学的症状を簡潔にま60分とめておいてください。
* [**第 13 回**](lect13){:target="_blank"} 【浅川：行動制御】第10講で議論された内容は環境との相互作用を通して，認知機構を構築していく過程が示唆される。強化学習の脳内対応物を考える際には，皮質だけでなく，大脳基底核，海馬など皮質下領域も考慮する必要がある。大脳基底核を制御機構と捉えることにより，視覚探索課題と眼球運動制御などの説明モデルを考察します。
世界モデルについて調べてください。ユクスキュル／クリサート著，生物から見た世界，日高・羽田訳，岩波文庫青943-1に出てくる「環世界」と関連します。
* [**第 14 回**](lect14){:target="_blank"}【浅川：感覚統合】感覚統合実演：変分自己符号化モデル (VAE )を用いてマルチモーダル統合の実演を行う。履修者は，マガーク効果や知覚運動協応の題材を用いて結果を観察しレポートを作成し提出する。
自身の体験から，複数のモダリティを統合することの意味と背景となる機構について考えをまとめておいて
60分ください。



## 文献資料

1. [ディープラーニング概説, 2015, LeCun, Bengio, Hinton, Nature](https://komazawa-deep-learning.github.io/2021/2015LeCun_Bengio_Hinton_NatureDeepReview.pdf){:target="_blank"}
1. [苦い教訓 (2019) Sutton](https://komazawa-deep-learning.github.io/2021cogpsy/2019Sutton_Bitter_Lesson.pdf){:target="_blank"}
1. [ゴール駆動型深層学習モデルを用いた感覚皮質の理解 Yamins(2016) Nature](https://project-ccap.github.io/2016YaminsDiCarlo_Using_goal-driven_deep_learning_models_to_understand_sensory_cortex.pdf){:target="_blank"}
1. [ディープラーニングレビュー Storrs ら, 2019, Neural Network Models and Deep Learning, 2019](https://komazawa-deep-learning.github.io/2021/2019Storrs_Golan_Kriegeskorte_Neural_network_models_and_deep_learning.pdf){:target="_blank"}
<!-- * [Storrs ら, Neural Network Models and Deep Learning, 2019](2019Storrs_Golan_Kriegeskorte_Neural_network_models_and_deep_learning.pdf){:target="_blank"} -->
1. [深層学習と脳の情報処理レビュー Kriegestorte, 2015, Deep Neural Networks: A New Framework for Modeling Biological Vision and Brain Information Processing](2015Kriegeskorte_Deep_Neural_Networks-A_New_Framework_for_Modeling_Biological_Vision_and_Brain_Information_Processing.pdf){:target="_blank"}
1. [生物の視覚と脳の情報処理をモデル化する新しい枠組み Kriegeskorte, Deep Neural Networks: A New Framework for Modeling Biological Vision and Brain Information Processing, 2015](https://project-ccap.github.io/2015Kriegeskorte_Deep_Neural_Networks-A_New_Framework_for_Modeling_Biological_Vision_and_Brain_Information_Processing.pdf){:target="_blank"}
1. [計算論的認知神経科学 Kriegeskorte and Douglas, 2018, Cognitive computational neuroscience](https://project-ccap.github.io/2018Kriegeskorte_Douglas_Cognitive_Computational_Neuroscience.pdf){:target="_blank"}
<!-- * [Kriegeskorte, N. and Douglas, P. K., Cognitive computational neuroscience, 2018](2018Kriegeskorte_Douglas_Cognitive_Computational_Neuroscience.pdf){:target="_blank"} -->
1. [視覚系の畳み込みニューラルネットワークモデル，過去現在未来 Lindsay, 2020, Convolutional Neural Networks as a Model of the Visual System: Past, Present, and Future](https://project-ccap.github.io/2020Lindsay_Convolutional_Neural_Networks_as_a_Model_of_the_Visual_System_Past_Present_and_Future.pdf){:target="_blank"}
<!-- * [Lindsay, G. W., Convolutional Neural Networks as a Model of the Visual System: Past, Present, and Future, 2020](2020Lindsay_Convolutional_Neural_Networks_as_a_Model_of_the_Visual_System_Past_Present_and_Future.pdf){:target="_blank"} -->
1. [計算論的視覚と正則化理論 Poggio, Torre, Koch, 1985](https://komazawa-deep-learning.github.io/2021cogpsy/1985Poggio_Computational_Vision_and_Regularization_Theory.pdf){:target="_blank"}
1. [皮質における物体認識の階層モデル Riesenhuber and Poggio (1999) Nature](https://komazawa-deep-learning.github.io/2021cogpsy/1999Riesenhuber_Poggio_Hierarchical_models_of_object_recognition_in_cortex.pdf){:target="_blank"}
1. [名詞の意味に関連した人間の脳活動の予測, Mitchell, 2018, Predicting Human Brain Activity Associated with the Meanings of Nouns](https://shinasakawa.github.io/2008Mitchell_Predicting_Human_Brain_Activity_Associated_with_the_Meanings_of_Nounsscience.pdf){:target="_blank"}
1. [ディープラーニング回顧録 Senjowski, 2020, Unreasonable effectiveness of deep learning in artificial intelligence](https://komazawa-deep-learning.github.io/2021/2020Sejnowski_Unreasonable_effectiveness_of_deep_learning_in_artificial_intelligence.pdf){:target="_blank"}
<!-- * [Senjowski, Unreasonable effectiveness of deep learning in artificial intelligence, 2020](2020Sejnowski_Unreasonable_effectiveness_of_deep_learning_in_artificial_intelligence.pdf){:target="_blank"} -->
1. [注意レビュー論文 Lindsay, 2020, Attention in Psychology, Neuroscience, and Machine Learning](https://project-ccap.github.io/2020Lindsay_Attention_in_Psychology_Neuroscience_and_Machine_Learning.pdf){:target="_blank"}
1. [運動制御のカルマンフィルター仮説 Wolpert, Ghahramani, and Jordan, 1995, An Internal Model for Sensorimotor Integration](https://project-ccap.github.io/1995WolpertGhahramaniJordan_Internal_Model_for_Sensorimotor_Integration.pdf){:target="_blank"}
1. [ハブ＆スポーク仮説 Lambon Ralph, M., Jefferies, E., Patterson, K, and Rogers, T.T., 2017 The neural and computational bases of semantic cognition](https://project-ccap.github.io/2017LambonRalphJefferiesPattersonRogers_The_neural_and_computational_bases_of_semantic_cognition.pdf){:target="_blank"}

---

# 授業概要

<!-- * 本授業では，毎回オンライン配信を行う予定です。
* 授業の Google meet URL は以下のとおりです: [https://meet.google.com/oia-vgsd-cpb](https://meet.google.com/oia-vgsd-cpb) 
-->
* コンピュータ実習を予定しています。そのため，仮にオンラインで受講する際には，十分な回線速度を確保してください。
* スマートフォンによる参加では不十分です。
* 必ず PC や Macintosh などでの履修をお願いします。
* 十分な授業参加環境が用意できない場合には，対面での参加を検討してください。

<!-- この授業は，2021年度後期開講予定の 07445/心理学特講IIIB と連係し，連続した内容となります。
履修者は両授業を履修することで完結した理解に至るようになります。
前期のこの授業では，主として画像認識，視覚情報処理に関する話題を取り上げます。
深層学習で採用されている技法を知ることで，如何にして人間を上回る認識性能を示すようになったのか，そこから人間の認識機構への示唆はどのようなものが感がられるのかについて考えます。

本授業では人工知能に用いられる技術の詳細を検討しながら，その心理学的意味を考えます。
自動運転が可能となり，
囲碁の世界チャンピオンを破り，自動翻訳の精度が向上し，スマートスピーカーが普及するなど AI 技術は毎日のように報道されています。
これらの技術はニューラルネットワークモデルに基づいています。
とりわけディープラーニング (深層学習) 技術は現在の人工知能の根幹をなしています。
現在は第 3 次ニューラルネットワークブームと呼ばれますが 3 度のブーム とも心理学者が火付け役でした。
2014年 から始まった現在のブームも心理系出身の研究者が先導しました。
加えてディープマインドの共同創設者デミス・ハサビスは認知科学出です。
このように人工知能と心理学とは同じことを別の側面から理解しようとしているとさえ言えます。
このような背景から，心理学と最近の人工知能技術の相互関係を考察する授業になります。
昨今の人工知能技術と心理学との関係から理解することで，最新の技術についての背景となる考え方を解説します。
 -->
<!-- - CNN: 畳み込みニューラルネットワーク
- RNN: リカレントニューラルネットワーク
- RL: 強化学習
-->

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

 -->

<!--
<br/>
1. [tSNE を用いた TLPA 200語の word2vec 視覚化](https://ShinAsakawa.github.io/2020cnps_tSNE_for_word2vec.ipynb)
2. [2020年2月24日資料1 tlpa 画像](https://ShinAsakawa.github.io/2020making_tlpa.html)
3. [2020年4月15日かじゅまるつがる松本先生のモデルの説明](https://shinasakawa.github.io/2020gajumarutugaru/2020-0415Friston_in_detail.html)
4. [2020年4月18日かじゅまるつがる投稿](https://shinasakawa.github.io/2020gajumarutugaru/2020-0418gajumarutugaru.html)
   
<br/>

1. [2020ccap 資料置き場](2020ccap)
2. [2020中央大学，緑川先生，重宗先生，研究会資料](2020chuo)
3. [2020 第2回 中央大学，緑川先生，重宗先生，研究会資料](2020chuo2)
4. [2020サイトビジット資料](2020sightvisit)

 <a href="https://guides.github.com/features/pages/">Read this page to write this page.</a>
-->
