---
title: 2021年度 駒澤大学心理学特講IIIa
layout: home
---

<!-- # 2021年度 駒澤大学心理学特講IIIa -->

<!--
- ARISA MIZUTANI <1nb8004a@komazawa-u.ac.jp>,
- 1nb9049s@komazawa-u.ac.jp,
- TADAYOSHI MIYAWAKI <1nb9076t@komazawa-u.ac.jp>
-->

<!--
- [計画](2021plan)
- [情報](2021info)
-->

# ディープラーニング deep learning  と心理学との関連を探る
- 授業名: 心理学特講IIIA
- 担当者名: 浅川 伸一 (アサカワ シンイチ)
- 電子メールアドレス: <educ20233@komazawa-u.ac.jp>, <asakawa@cis.twcu.a.jp>
- 開講年度・期:　2021年 前期
- 開講曜日・時限: 金曜日 1 限 09:00-10:30
- 教室: 1-507
- 単位数　2
- オフィスアワー: なし，メールや SNS を活用してください。駒澤大学の専任ではありません。
非常勤講師ですので，金曜日の 1 時限だけしか駒澤大学には居ません。

# 前期

- [第01回 04月16日](2021lect01)
- [第02回 04月23日](2021lect02)
- [第03回 04月30日](2021lect03)
- [第04回 05月07日](2021lect04)
- [第05回 05月14日](2021lect05)
- [第06回 05月21日](2021lect06)
- [第07回 05月28日](2021lect07)
- [第08回 06月04日](2021lect08)
- [第09回 06月11日](2021lect09)
- [第10回 06月18日](2021lect10)
- [第11回 06月25日](2021lect11)
- [第12回 07月02日](2021lect12)
- [第13回 07月09日](2021lect13)


# 後期

- [第14回 09月17日](2021lect14) 自然言語処理: 言語モデル，言語処理課題
- [第15回 09月24日](2021lect15) 単純再帰型ニューラルネットワーク:Elman and Jordan, BPTT, 系列学習
- [第16回 10月01日](2021lect16) 休講
- [第17回 10月08日](2021lect17) 翻訳モデル と seq2seq モデルでの注意 <!-- 意味モデル: word2vec, LDA, LSI, SVD，トピックモデル，意味記憶-->
- [第18回 10月22日](2021lect18) 注意: BERT, GLUE, マルチヘッド注意<!-- ，ポスナー，ブロードベント，トリーズマン -->
-  10月29日 <!-- 眼球運動: DeepGaze, 眼球運動，CAM，AIの民主化-->
- [第19回 11月05日](2021lect19) BERT 実習と強化学習の導入<!-- ニューラル脚注付け: NIC, VQA -->
- [第20回 11月12日](2021lect20) 強化学習 1: 報酬，価値，TD 誤差，方策，イプシロン貪欲探索，マルコフ決定過程，SARSA, Q 学習，DQN <!-- 失語症モデル-->
- [第21回 11月19日](2021lect21) 強化学習 2: 二重 Q 学習，アクタークリティック法，アドバンテージアクタークリティック，非同期アドバンテージアクタークリティック
- [第22回 11月26日](2021lect22) 強化学習 3: 価値反復，方策反復，優先付き再生，経験再生，A3C，エージェント57
- [第23回 12月03日](2021lect23) マルチモーダル統合 1 変分自己符号器モデル VAE, KL divergence
- [第24回 12月10日](2021lect24) 
- [第25回 12月17日](2021lect25) 
- [第26回 12月24日](2021lect26)  [Google Meet https://meet.google.com/oia-vgsd-cpb](https://meet.google.com/oia-vgsd-cpb)
- [第15回 01月07日](2021lect27)

---

# 授業概要
* 本授業では，毎回オンライン配信を行う予定です。
* 授業の Google meet URL は以下のとおりです: [https://meet.google.com/oia-vgsd-cpb](https://meet.google.com/oia-vgsd-cpb)
コンピュータ実習を予定しています。そのため，仮にオンラインで受講する際には，十分な回線速度を確保してください。
* スマートフォンによる参加では不十分です。
* 必ず PC や Macintosh などでの履修をお願いします。
* 十分な授業参加環境が用意できない場合には，対面での参加を検討してください。

この授業は，2021年度後期開講予定の 07445/心理学特講IIIB と連係し，連続した内容となります。
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
