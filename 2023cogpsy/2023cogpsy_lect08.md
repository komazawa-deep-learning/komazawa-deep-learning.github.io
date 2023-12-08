---
title: "第08回 2023年度開講 駒澤大学 認知心理学研究"
author: "浅川 伸一"
layout: home
codemirror_mode: python
codemirror_mime_type: text/x-cython
---

<div align="right">
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 17/Nov/2023<br/>
Appache 2.0 license<br/>
</div>

<!-- <link href="/css/asamarkdown.css" rel="stylesheet"> -->

## 機械学習と推測統計学

### 機械学習の技法

3. Breiman の 2 つの文化
2. データセット, 訓練データ，検証データ，テストデータ
1. フィードフォワード, フィードバック
8. 活性化関数
9. 損失関数 (誤差関数，目的関数)
10. 誤差逆伝播法, 勾配降下法, 確率的勾配降下法, ミニバッチ
13. データ拡張
15. 正則化
14. ドロップアウト

### 正則化

データ $y$ から $z$ を見つけ出す不良設定問題の正則化 $Az = y$ では，正則化項 $\left\|\cdot\right\|$ の選択と汎関数の安定化項 $\left\|Pz\right\|$ が必要となる。
標準正則化理論においては，$A$ は線形演算子，ノルムは 2 次，$P$ は線形である。
2 種類の方法が適用可能である。
すなわち

1. $\left\|Az-y\right\|\leqslant\epsilon$ を満たし，$\displaystyle\left\|Pz\right\|^2$ を最小化する $z$ を探す
2. $\displaystyle \left\|Az-y\right\|+\lambda\left\|Pz\right\|^2,$ を最小化する $z$ を探す
ここで $\lambda$ は正則化パラメータ。

最初の方法は，十分にデータを近似し，かつ，「基準」$\left\|Pz\right\|$ を最小化するという意味で「正則」な $z$ を探す方法である。
二番目の方法は，$\lambda$ が正則化の程度と解のデータへの近似とをコントロールする。
標準正則化理論は，最良の $\lambda$ を決定する手法を提供する。
標準正則化の手法は，上式に制約を導入することで変分原理の問題としている。
最小化するコストは物理的制約条件を満たす良い解を反映している。
すなわち，データへの近似もよく，かつ，正則化項 $\left\|Pz\right\|^2$ も小さいことを意味する。
$P$ は問題の物理的制約を表しており，2 次の変分原理であり，解空間内での唯一解が存在する。
標準正則化手法は，不良設定問題に対して注意深い分析が必要であることを注記しておく。
ノルム $\left\|\cdot\right\|$，正則化関数 $\left\|Pz\right\|$, および，汎関数空間の選択は数学的性質と，物理的説得性を有する必要がある。
これらにより，正しい正則化の詳細条件が定まる。

変分原理は物理学，経済学，工学，で幅広く用いられている。例えば物理学における基本法則は変分原理を用いて，
エネルギーやラグランジェ関数を用いて簡潔に表現されている。

### 機械学習と心理統計学の違い

仮説検定とパラメータチューニングの差異は，母集団の相違に期すのか，それとも選択しているモデルによるものなのか。
心理統計では，データを説明する努力よりも，母集団の相違，すなわち，帰無仮説が棄却できるか採択されるかに興味がある。
ところが，帰無仮説が正しいかどうかは，選択する統計モデルに依存する。
このとき統計モデルの精度が正しいのかどうかを問題にすることは少ない。
だが，用いるモデルに依存して推論結果が変化するかも知れない。
そうするとモデルの優劣が問題になるであろう。

一方，機械学習では，心理統計の母集団に相当する概念が，汎化性能である。
所与のデータにだけ当てはまるモデルではなく，未知のデータにたいして性能の高いモデルが選択される。
未知のデータ，未学習のデータに対する性能と母集団の差異を，一概に比較することは難しいが，予測精度を高くすることが，現実には用いられる実用性が高い。
応用が可能で，実学として世の中の役に立つ成果を生み出すことができる。

### ASA アメリカ統計学会の声明再録

<!-- 1. **P 値は，データが指定された統計モデルとどの程度相性が悪いかを示すことができる** P-values can indicate how incompatible the data are with a specified statistical model. -->
<!-- 2. **P 値は，研究された仮説が真である確率を測定するものではない。そうではなく，データがランダムな偶然だけから，生成された確率を測定するものである** P-values do not measure the probability that the studied hypothesis is true, or the probability that the data were produced by random chance alone. -->
<!-- 3. **科学的な結論やビジネスや政策の決定は，p 値が特定の閾値を超えたかどうかだけに基づくべきではない** Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold. -->
<!-- 4. **適切な推論を行うには，完全な報告と透明性が必要である** Proper inference requires full reporting and transparency. -->
<!-- 5. **P 値や統計的有意性は，効果の大きさや結果の重要性を測定するものではない** A p-value, or statistical significance, does not measure the size of an effect or the importance of a result. -->
<!-- 6. **それ自体では，p 値はモデルや仮説に関する証拠の良い尺度を提供しない。** By itself, a p-value does not provide a good measure of evidence regarding a model or hypothesis. -->

* [基礎と応用社会心理学 (BASP)  編集方針 (2014,2015)](../2023/2015Basic_and_Applied_Social_Psychology_ban_p_values_ja.md)
* [アメリカ統計学会の声明 2014, 2015](../2023/2015Basic_and_Applied_Social_Psychology_ban_p_values_ja.md)
* [統計学の誤り : 統計的妥当性の「ゴールドスタンダード」である P 値は多くの科学者が想定しているほど信頼できるものではない (Nuzzo+2014)](../2023/2014Nuzzo_Statistical_errors_ja.md)
* [統計的有意性を引退させろ (サイエンティフィックアメリカン, 2019)](2019Amrhein_Retire_statistical_significance_ja.md)

### Breiman によるデータサイエンスにおける 2 つの文化 <!-- あるいは，統計学と機械学習とニューラルネットワークの関係-->

<div class="figcenter">
<img src="/2023assets/2001Breiman_Two_Cultures_fig2.svg" width="39%"><br/>
<img src="/2023assets/2001Breiman_Two_Cultures_fig3_.svg" width="39%"><br/>
<!-- <img src="/2023assets/2001Breiman_cultures.svg" width="23%"><br/> -->
<div class="figcaption">
<!-- ![Breiman(2001)](/2023assets/2001Breiman_cultures.svg){#fig:2001breiman style="width:34%"} -->


From Leo Breiman, Statistical Modeling: The Two Cultures, _Statistical Science_, 2001, Vol. 16, No. 3, 199–231, doi:10.1214/ss/1009213725.
[pdf](https://projecteuclid.org/journals/statistical-science/volume-16/issue-3/Statistical-Modeling--The-Two-Cultures-with-comments-and-a/10.1214/ss/1009213726.full)
</div></div>

Breiman は，アンサンブル学習 (バギング，ブートストラップ法) など，影響力のあるいくつかの機械学習手法を提案した機械学習界隈のレジェンド。
<!-- Breiman によれば，2 つの文化 -->

* データモデル文化: 心理統計で用いられるような統計学モデルを使用する文化
* アルゴリズムモデル文化: 機械学習における統計学的技法を重視する文化

* データモデル: データからパラメータの値を推定し，そのモデルを情報収集や予測に利用する。
  * 伝統的な統計学 p 値崇拝主義
  * データモデルの限界
    * データモデルにこだわるあまり，統計学における多変量解析のツールは，分類では判別分析とロジスティック回帰，回帰では重回帰に固まってしまっている。
    * 多変量データが多変量正規分布であると本気で信じている人はいないが，多変量統計解析に関するすべての大学院の教科書では，このデータモデルが多くのページを占めている。
    * 未知の物理的，化学的，生物学的機序を含む複雑な系の制御されていない観察から収集されたデータでは，統計学者が選択したパラメトリックモデルによって自然がデータを生成するという先験的な仮定は，適合度検定や残差分析に訴えても立証できない疑わしい結論になることがある。通常，複雑な系によって生成されたデータ，例えば医療データや金融データに単純なパラメトリックモデルを適用すると，アルゴリズムモデルと比較して精度と情報が損なわれる。

* アルゴリズムモデル
暗箱の中は複雑で未知であると考える。 アプローチは，関数，$f(x)$ すなわち $x$ を操作して応答 $y$  を予測するアルゴリズムを見出すこと。
  * モデルの検証方法： 予測精度によって測定する機械学習的手法

## Feynmann の技法

> 奇跡の人はいない。 あることに興味を持ち，たまたま，そのすべてを学んだ人がいるだけだ。- リチャード・ファインマン

> There’s no miracle people. It just happens they got interested in this thing and they learned all this stuff. There’s just people. – Richard Feynman

1. 学ぶべきテーマを一つ選ぶ
2. 自分に説明する，あるいは，誰かに説明する
3. 行き詰まったら元の資料に戻る
4. 説明を単純化し，例え話を作る

## 文献

* [1985 Poggio 計算論的視覚と正則化理論](1985Poggio_ja.pdf)
* [1988 Sur+ ワン・アルゴリズム仮説](2023_1030one_algorithm.pdf)
* [2000 Rasmussen&Ghahramani オッカムのカミソリ](2001Rasmussen_Ghahramani_occams_razor_ja.pdf)
* [1990 Riesenhuber&Poggio 皮質における物体認識の階層モデル](1999Riesenhuber_Poggio_HMAX.pdf)
* [1998 Hamming あなたとあなたの研究](1998Hamming_あなたとあなたの研究.pdf)
* [Hamming による最良の研究をする 10 のルール](2007ErrenCullenErrenBourne_Ten_Simple_Rules_for_Doing_Your_Best_Research,_According_to_Hamming.pdf)



## 告知

### 告知 1. [DaSiC2023 ワークショップ](https://sites.google.com/view/dasic7-2023){:target="_blank"}

* 日時: 2023年12月23日(土)
* 会場: [筑波大学天王台キャンパス 第一エリア1D201講義室 Google map](https://www.google.co.jp/maps/place/1D201%E6%95%99%E5%AE%A4/@36.108528,140.1019327,16.79z/data=!4m6!3m5!1s0x60220c0745ebad25:0x83c473710859d960!8m2!3d36.1084607!4d140.1018482!16s%2Fg%2F11g6yv8vk7?hl=ja&entry=ttu){:target="_blank"}
* 参加無料
* 概要：

健常者は日常の発話でついうっかり、また失語症患者は主に脳の疾患により言い誤り(錯語)を表出することが知られています。今回のイベントでは、こうした言語データを機械学習モデルと神経科学といういわば２枚の「鏡」の前に置いた時、そこに映し出されるのはどのような景色、振る舞いかを実演を交えて示します。はたしてそれは機械学習モデルの貢献か研究者の願望か。言語学者、機械学習の専門家、言語聴覚士という登壇者それぞれの３つの視座から、実際の健常者の言い誤りや失語症患者の錯語の実際のデータを供覧しつつ、それらのデータが機械学習モデルではどのように説明されるのか、から議論していきます。

[ワークショップホームページ](https://sites.google.com/view/dasic7-2023/workshop?authuser=0)

### 告知 2. 全脳アーキテクチャ勉強会

全脳アーキテクチャ・アプローチでは、脳全体のアーキテクチャを学び、ヒトのような汎用人工知能を構築することを目指しています。
このアプローチにおいては、脳が適応的かつ創造的に知識を形成する高度な情報処理の理解と構築が非常に重要な要素となっています。

今回、神経活動、認知機能、記憶、視覚認識、ニューロテックといった多角的な観点から計算論的神経科学を研究している倉重宏樹氏をお招きし、「記憶の自己構築性から脳と社会とAIの『知』を考える」というテーマで、論文などでは表現しきれない部分も含め、研究に関する多くの興味深いトピックを記憶・学習の視点から位置付けてご紹介いただくとともに、その内容について議論する場とさせていただきます。

* 日時：2023年11月28日（火）（18:00～21:00）
* 会場：オンライン（Zoom Meeting）
* 参加枠：一般 150 名／学生 50 名（一般：1000円、学生：無料）
* 主催： NPO法人 全脳アーキテクチャ・イニシアティブ（WBAI）

詳細・申し込みはこちらから：[https://wba-meetup.connpass.com/event/299180/](https://wba-meetup.connpass.com/event/299180/)

* 講演概要：
記憶は構造を持ち、そこにおいて情報は複雑に組織化している。これが我々の認識や思考や行動を定め、さらには学習や自励的な変化を通じ、次の記憶の構造を定める。
すなわち記憶とは、法則に従って再帰的に自己構築をし続けるある種の生命的なシステムであり、知の適応性/創造性や機能性はその構造とダイナミクスから理解される必要がある。
神経科学や心理学において、今自分が持っている記憶に依存して次の記憶を作る法則やメカニズムはスキーマ同化やスキーマ調節の術語のもとで研究されてきた。
そこでまず、自らのものを含めたそれらの研究が、記憶の再帰的自己構築性について何を示せており、何を示せていないかを説明する。
先取りすれば、現状ではとくに記憶の大域構造の理解が欠けている。
大域構造の自己構築の原理やそうして構築された構造そのもの、またそれらが脳情報処理にもたらす影響はほぼ分かっていない。
そこで、それらに迫るためのあり得る手段を、神経生理学・大規模言語モデル AI・数理工学の知見に基づいて議論する。
またそうして構築された記憶の構造は、先に述べたように認識や思考や行動といった人の知的情報処理を規定する。
では、どのように規定するのだろうか？これは脳のなかで記憶の大域構造がどのようにデコードされるかという問題に関係が深い。
これを脳の可塑性とAIにおける“埋め込み表現”の知見から考えていく。
ところで、記憶の自己構築性に法則があるということは、記憶は自由ではないということである。
つまりその法則に従って到達可能な状態の空間というものがある。そこでこのことの意味を、脳のみならず、AIや社会における知の生成にも敷衍して議論する。
これは「『AI にできないことはなにか？』とはどのような意味の問いか？」
という問題にも関わる。
また、その上でこの到達可能な空間を拡げることはできるかについても議論し、それにかかわる自身の研究プロジェクトの現状をプレリミナリーな結果とともに紹介する。


## 関連技術
1. 主成分分析[@1901Pearson_PCA]
$$
H[y,X,w]=\left(y-Xw\right)^2+\lambda(w^{\top}w-1)
$$
2. エントロピー最大化
3. word2vec における負例サンプリング[@2013Mikolov_skip-gram_NIPS]
2. 画風変換 [@2015Gatys_DeepArt]
3. 領域 CNN [@2015Girshick_FastRCNN],[@2015Ren_FasterRCNN],[@2017He_MaskRCNN]
- 解絡学習，解絡表現 disentangled representation, disentaglement
4. $\beta-\text{VAE}$ (Kruse=Kuhn=Tucker 条件[@2017Higgins_betaVAE])
5. InfoGAN[@2016Chen_infoGAN]



# エントロピー Entropy
<!-- Srihari slides https://cedar.buffalo.edu/~srihari/CSE574/ -->

* 離散的確率変数 $x$ の特定の値を観測したとき，どの程度の情報を受け取ることができるかを示す量。
* `驚き surprise` の程度を表す情報の量<!--Amount of information is degree of surprise-->
    * 確実性 certainity は，情報がないことを言う。
    * ある事象が起こる可能性が低い場合には，その情報が起こった時に，より多くの情報が得られると考える。
* 確率分布 $p(x)$ とそのときの量 $h(x)$ に依存する。
* 無関係な 2 つの事象 $x$ と $y$ があるとき，$h(x,y) = h(x)+h(y)$ としたい。
* したがって $h(x)=-\log_{2}p(x)$ を選ぶ。
    * 負は情報量が正であることを保証するために付与されている
* 平均的な情報伝達量は $p(x)$ に対する期待値であり，これがエントロピーと呼ばれる量である。


- 情報量: 確率変数 $x$ のサプライズ量
  - まれにしか起こらない事象が起こった場合には情報量は大きい。<strong>ニュースになる</strong>
  - 必ず起こることが起こっても情報量は小さい。<strong>ニュースにならない</strong>

$$
H(x)=-\sum_x p(x)\log_2p(x)
$$
- マイナスをつけるのは正の値にするため
サプライズ量の平均: 平均エントロピー


一方情報論的エントロピー $H$ の定義は事象 $A$ の起こる確率を $P(A)$ とすれば

$$
H(A) = - \sum_{A\in\Omega} P(A) \log P(A)
$$

確率の制約，及び，平均と分散に関する制約条件を以下のように記述:

- $\displaystyle\int p\left(x\right)\;dx =1$ : 確率
- $\displaystyle\int xp\left(x\right)\;dx =\mu$ : 平均
- $\displaystyle\int \left(x-\mu\right)^2p\left(x\right)\;dx=\sigma^2$ : 分散
- ラグランジェ乗数を使って制約条件下での最大化

$$
L(x,\lambda_1,\lambda_2,\lambda_3)=-\int p\left(x\right)\log p\left(x\right)\;dx + \lambda_1\left(\int p\left(x\right)\;dx-1\right) + \lambda_2\left(\int xp\left(x\right)\;dx-\mu\right)+\lambda_3\left(\int\left(x-\mu\right)^2p\left(x\right)\;dx-\sigma^2\right)
$$

各変数で微分して 0 と置き，整理:

$$
p\left(x\right)=\exp\left(-1+\lambda_1+\lambda_2x+\lambda_3\left(x-\mu\right)^2\right)
$$

- 以上より連続量の最大エントロピーを与える確率分布はガウス分布となる


* (自由エネルギーの最小化) = (予測誤差を最小化するように信念を書き換え予測を最適化)+(予測誤差)を最小化するような行動をとる)
* (自由エネルギー) = (内部エネルギー)-(エントロピー)

## 条件付きエントロピー Conditional Entropy
- 同時確率 $p(x,y)$ に対して
$$
H[x,y]=-\int\int p(x,y)\log p(x,y)\;dx\;dy
$$
<!--  - We draw pairs of values of $x$ and $y$-->
- $x$ が所与のとき<strong>条件付きエントロピー</strong>
$$
H[y\vert x]=-\int p(y\vert x)\log p(y\vert x)\;dy
$$

- さらに以下の関係がある
$$
H[x,y] = H[y\vert x] + H[x]
$$

<!--
  - If value of $x$ is already known, additional information to specify corresponding value of $y$ is $-\log p\of{y\given{x}}$
- Average additional information needed to specify $y$ is the conditional entropy
- By product rule $H\of{x,y} = H\of{y\given{x}} + H\of{x}$
-->
<!--
  - where $H\of{x,y}$ is differential entropy of $p\of{x,y}$
  - $H\of{x}$ is differential entropy of $p(x)$
  - Information needed to describe $x$ and $y$ is given by
  - information needed to describe $x$ plus additional information needed to specify $y$ given $x$
-->


<!--
- If we have joint distribution $p\of{x,y}$
  - We draw pairs of values of $x$ and $y$
  - If value of $x$ is already known, additional information to specify corresponding value of $y$ is $-\log p\of{y\given{x}}$
- Average additional information needed to specify $y$ is the conditional entropy
- By product rule $H\of{x,y} = H\of{y\given{x}} + H\of{x}$
  - where $H\of{x,y}$ is differential entropy of $p\of{x,y}$
  - $H\of{x}$ is differential entropy of $p\of{x}$
  - Information needed to describe $x$ and $y$ is given by
  - information needed to describe $x$ plus additional information needed to specify $y$ given $x$
-->

<!-- フリストンの言う自由エネルギーとは，ヘルムホルツの自由エネルギーを脳神経系に当てはめた仮説。

<p align="center">
力学的エネルギー = 運動エネルギー + 位置エネルギー(ポテンシャル)
</p>

$$
E = K + U\\
E = \frac{1}{2}mv^2 + mgh
$$ -->


- 統計物理学: 巨視的な物体，すなわち莫大な数の個別的な粒子，原子や分子，からなる物体のふるまいやっ性質を支配している特別な型の法則性を研究する学問分野
- [熱力学第一法則 エネルギー保存則](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%8D%E3%83%AB%E3%82%AE%E3%83%BC%E4%BF%9D%E5%AD%98%E3%81%AE%E6%B3%95%E5%89%87)
- [熱力学第二法則 エントロピーは増大する](https://ja.wikipedia.org/wiki/%E7%86%B1%E5%8A%9B%E5%AD%A6%E7%AC%AC%E4%BA%8C%E6%B3%95%E5%89%87)

## 熱力学的，および情報論的エントロピー (あるいは，情報量 Information Measure)
熱力学的エントロピーと情報論的エントロピーが存在するが式は同じである。

## (熱)力学的エントロピー

ある位置 $i$ にある粒子があるとする。各位置にそれぞれ $n_i$ の粒子が存在するとする。
はおのおの区別できないものとすれば，全ての状態は何通りあるかを表す式は次式となる:

$$
W=\frac{N!}{\prod_i n_i!}
$$

エントロピーとはこの状態の数 $W$ の負の対数である.
$$
H=\frac{1}{N}\log W=\frac{1}{N}\log N!-\frac{1}{N}\sum_i\log n_i!
$$

以下のスターリングの近似公式 ($\log N!\approx N\log N - N$) を用いると以下の式を得る

$$
H=-\lim_{N\rightarrow\infty}\sum_i\left(\frac{n_i!}{N}\right)
\log\left(\frac{n_i!}{N}\right)=-\sum_i p_i\log p_i
$$

$$
S = k \ln W
$$

ここで，$k$ は[ボルツマン定数](https://ja.wikipedia.org/wiki/%E3%83%9C%E3%83%AB%E3%83%84%E3%83%9E%E3%83%B3%E5%AE%9A%E6%95%B0)であり，$W$ は系の微視的な状態を表す。
一方で統計力学におけるエントロピーの定義は以下の通り:

$$
S=k\left<\ln\frac{1}{p(\omega)}\right>=-k\sum_{\omega}p(\omega)\ln p(\omega)
$$

上式中 $\left<\;\right>$ は[アンサンブル平均](https://ja.wikipedia.org/wiki/%E7%B5%B1%E8%A8%88%E9%9B%86%E5%9B%A3)と呼ばれ，巨視的に同条件下にある力学系が系を構成する分子間に相関がなければ，系は微視的にはすべての状態をとりうることから，巨視的状態において統計的に系はすべての状態をとりうることが仮定される。
系の時間的平均と空間間的平均が同じであると仮定できるときその系は**エルゴード性**を有するという。
エルゴード性により時間平均と空間平均とを区別しないで(しばしば意図的に混乱させて)用いることが行われる。

<!--## 情報量 Information Measure
Srihari slides https://cedar.buffalo.edu/~srihari/CSE574/

- 離散変数 $x How much information is received when we observe a specific value for a discrete random ariable $x$?
- Amount of information is degree of surprise
    - Certain means no information
    - More information when event is unlikely
- Depends on probability distribution $p\of{x}$, a quantity $h\of{x}$
- If there are two unrelated events $x$ and $y$ we want $h\of{x,y}=h\of{x}+h\of{y}$
- Thus we choose $h\of{x}=-\log_2p\of{x}$
    - Negative assures that information measure is positive
- Average amount of information transmitted is the expectation w.r.t $p\of{x}$ refered to as entropy

- 情報量: 確率変数 $x$ のサプライズ量
  - まれにしか起こらない事象が起こった場合には情報量は大きい。<strong>ニュースになる</strong>
  - 必ず起こることが起こっても情報量は小さい。<strong>ニュースにならない</strong>

$$
H\of{x}=-\sum_x p\of{x}\log_2p\of{x}
$$
- マイナスをつけるのは正の値にするため
サプライズ量の平均: 平均エントロピ


一方情報論的エントロピー $H$ の定義は事象 $A$ の起こる確率を $P(A)$ とすれば

$$
H(A) = - \sum_{A\in\Omega} P(A) \log P(A)
$$


確率の制約，及び，平均と分散に関する制約条件を以下のように記述:

- $\displaystyle\int p\left(x\right)\;dx =1$ : 確率
- $\displaystyle\int xp\left(x\right)\;dx =\mu$ : 平均
- $\displaystyle\int \left(x-\mu\right)^2p\left(x\right)\;dx=\sigma^2$ : 分散
- ラグランジェ乗数を使って制約条件下での最大化

$$
L(x,\lambda_1,\lambda_2,\lambda_3)=-\int p\left(x\right)\log p\left(x\right)\;dx + \lambda_1\left(\int p\left(x\right)\;dx-1\right) + \lambda_2\left(\int
 xp\left(x\right)\;dx-\mu\right)+\lambda_3\left(\int\left(x-\mu\right)^2p\left(x\right)\;dx-\sigma^2\right)
$$

各変数で微分して0と置き，整理:

$$
p\left(x\right)=\exp\left(-1+\lambda_1+\lambda_2x+\lambda_3\left(x-\mu\right)^2\right)
$$
- 以上より連続量の最大エントロピーを与える確率分布はガウス分布となる-->

<!-- - [自由エネルギー原理](./friston_FEP)<br> -->

ヘルムホルツの自由エネルギー: $F = U - TS $

$F$ はヘルムホルツの自由エネルギー，$T$ は温度，$S$ はエントロピー。<!-- <https://kotobank.jp/word/%E8%87%AA%E7%94%B1%E3%82%A8%E3%83%8D%E3%83%AB%E3%82%AE%E3%83%BC-76745>-->

- 熱力学の第一法則 エネルギー保存則
- 熱力学の第二法則

ギブスの自由エネルギー: $ G = F + pV$

* [変分自己符号化モデル 説明文](/vae_from2020gtext.pdf)
* [https://cbmm.mit.edu/video/brain-object-recognition-high-performing-shallow-recurrent-anns](https://cbmm.mit.edu/video/brain-object-recognition-high-performing-shallow-recurrent-anns)


---


<!-- from `~/study/2020blog.evjang.com/2016/08/2016EricJang_vb_basic_ja.md`-->
変分ベイズ法 (VB: Variational Bayeisan Methods) は，統計的機械学習で非常によく使われる手法の一群である。
VB 法は，統計的推論問題 (別の確率変数の値から確率変数の値を推定する問題) を最適化問題(ある目的関数を最小化するパラメータ値を求める問題) として書き直すことができる。
<!-- Variational Bayeisan (VB) Methods are a family of techniques that are very popular in statistical Machine Learning.
VB methods allow us to re-write *statistical inference* problems (i.e. infer the value of a random variable given the value of another random variable) as *optimization *problems (i.e. find the parameter values that minimize some objective function). -->

この推論と最適化の二重性は，最新の最適化アルゴリズムを使って統計的機械学習の問題を解く (逆に，統計的手法を使って関数を最小化する) ことを可能にするため強力である。
<!-- This inference-optimization duality is powerful because it allows us to use the latest-and-greatest optimization algorithms to solve statistical Machine Learning problems (and vice versa, minimize functions using statistical techniques). -->

ここでは，変分法について，最適化の目的を導出する。
目的は **変分下限 Variational Lower Bound** としても知られ [Variational Autoencoders](https://arxiv.org/abs/1312.6114) で使われているものと全く同じものである。

系を確率変数の集まりとしてモデル化すると，ある観察変数 ($X$) と，観察不可能な潜在変数 ($Z$) を仮定する。

[ベイズの定理](https://en.wikipedia.org/wiki/Bayes%27_theorem) は，任意の確率変数の組の間の一般的な関係を与える。
<!-- [Bayes' Theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem) gives us a general relationship between any pair of random variables: -->

$$
p(Z|X) = \frac{p(X|Z)p(Z)}{p(X)}
$$

これの様々な断片に通称が関連付けられている。
<!-- The various pieces of this are associated with common names:-->

$p(Z|X)$ は **事後確率** である。
`ある画像が与えられたとき，それが猫の画像である確率は？`
もし $z\sim P(Z|X)$ から標本抽出できるなら，これを使って，与えられた画像が猫かどうか教えてくれる猫分類器を作ることができる。
<!-- $p(Z|X)$ is the **posterior probability**: "given the image, what is the probability that this is of a cat?"
If we can sample from $z\sim P(Z|X)$, we can use this to make a cat classifier that tells us whether a given image is a cat or not. -->

$p(X\vert Z)$ は **尤度** である。
$Z$ の値が与えられたとき，この画像 $X$ がそのカテゴリに属する「確率」がどのくらいかを計算する。
もし $x\sim P(X\vert Z)$ から標本抽出できるなら，乱数を生成するのと同じくらい簡単に猫の画像と猫以外の画像を生成することができる。
$p(Z)$ は**事前確率** と呼ばれる。

隠れ変数は [ベイズ統計学](https://en.wikipedia.org/wiki/Bayesian_statistics) の枠組みで，観測変数に付随する **事前確信** と解釈することができる。
例えば，$X$ が多変量ガウス分布であると信じる場合，隠れ変数 $Z$ はガウス分布の平均と分散を表すかもしれない。
このとき，パラメータに対する分布 $P(Z)$ は，$P(X)$ に対する **事前分布** となる。
<!-- Hidden variables can be interpreted from a [Bayesian Statistics](https://en.wikipedia.org/wiki/Bayesian_statistics) framework as *prior beliefs* attached to the observed variables.
For example, if we believe $X$ is a multivariate Gaussian, the hidden variable $Z$ might represent the mean and variance of the Gaussian distribution.
The distribution over parameters $P(Z)$ is then a *prior* distribution to $P(X)$. -->

また，$X$ と $Z$ とがどの値を表すかは，自由に選択することができる。
例えば，$Z$ の代わりに「平均，分散の立方根，あるいは  $X+Y$，ここで $Y \sim \mathcal{N}(0,1)$」などとすることも可能である。
これはやや不自然で変であるが，$P(X|Z)$ を適宜修正すれば，構造はそのまま有効である。
<!-- You are also free to choose which values $X$ and $Z$ represent.
For example, $Z$ could instead be "mean, cube root of variance, and $X+Y$ where $Y \sim \mathcal{N}(0,1)$".
This is somewhat unnatural and weird, but the structure is still valid, as long as $P(X|Z)$ is modified accordingly.-->

変数を「追加」することもできる。
$P(Z|\theta)$ は，それ自身の事前分布 $P(\theta)$ を持ち，それらもやはり事前分布を持つなど，事前分布自体が他の確率変数に依存するかもしれない。
どんなハイパーパラメータも事前分布と考えることができる。



## 物理学におけるエントロピー <!--Physics view of Entropy-->
- $N$ 個の物質が $i$ 個の状態，各状態には $n_i$ 個の物質
<!--- $N$ objects into bins so that $n_i$ are in $i^{th}$ bin where $\sum_in_i=N$-->
<!--- Number of different ways of allocating objects to bins-->
- $N$ 個の物質を全て並べる: $N\cdot(N-1)\cdots2\cdot1=N!$<!-- であればways to choose first, $N-1$ ways for second leads to $N\cdot(N-1)\cdots2\cdot1=N!$-->
- 各状態の中では物質の順序は問わないことにする<!--We don’t distinguish between rearrangements within each bin-->
<!--    - In $i^{th}$ bin there are $n_i!$ ways of reordering objects-->
- 総数 $N$ 個の物質を $n_i$ に分ける場合の組み合わせ: $W=\frac{N!}{\prod_{i}n_{i}!}$
<!--  - Total number of ways of allocating $N$ objects to bins is $W=\frac{N!}{\prod_{i}n_{i}!}$-->
<!--    - Called Multiplicity (also weight of macrostate)-->
<!-- Entropy: scaled log of multiplicity -->
- <strong>エントロピーの定義</strong>

$$
H=\frac{1}{N}\ln W=\frac{1}{N}\ln N!-\frac{1}{N}\sum_i\ln n_i!
$$

- スターリングの公式 $N! \approx N\log N-N$ を用いて
$$
H=-\lim_{N\rightarrow\infty}\sum_i\left(\frac{n_i}{N}\right)\ln\left(\frac{n_!}{N}\right)=-\sum_ip_i\ln p_i
$$
- 全体の分布 $\displaystyle\frac{n_i}{N}$ をマクロステート
- 各状態をミクロステート $n_i$ を

### 連続系のエントロピー <!--Entropy with Continuous Variable-->
<!-- - Divide $x$ into bins of width $\Delta$-->
<!-- - For each bin there must exist a value $x_i$ such that -->
<!-- - Gives a discrete distribution with probabilities $p(x_i)\Delta$ -->
- 離散量 $p(x_i)\Delta$ を考えて $\Delta\rightarrow0$ を考える:
  - $\displaystyle\int_{i\Delta}^{\left(i+1\right)\Delta}p(x)d(x)=p(x_i)\Delta$
- <strong>連続系のエントロピー</strong><!--Entropy -->
$$
H_{\Delta}=-\sum_ip(x_i)\Delta\log\left(p(x_i)\Delta\right)=-\sum_ip(x_i)\Delta\log(x_i)-\Delta\log\Delta
$$

<!-- - Omit the second term and consider the limit $\Delta\rightarrow0$-->
- $\Delta\rightarrow0$ の極限を考えれば:<!--第2項を無視すれば:-->
$$
H_\Delta=-\int p(x) \log p(x)\,dx
$$
<!-- - Known as Differential Entropy-->
- 連続系と離散系のエントロピーは $\Delta\log\Delta$ だけ異なる
<!-- - Discrete and Continuous forms of entropy differ by quantity $\log\Delta$ which diverges-->
<!-- - Reflects to specify continuous variable very precisely requires a large no of bits-->

### 連続系のエントロピーを最大化する分布
<!--
# Entropy with Multiple Continuous Variables
- Differential Entropy for multiple continuous variables
$$
H[x]=-\int p(x)\log p(x)\;dx
$$
- For what distribution is differential entropy maximized?
  - For discrete distribution, it is uniform
  - For continuous, it is Gaussian
-->
- どのような分布が連続系のエントロピーを最大化するか？
  - 離散系では一様分布
  - 連続系では?
$$
H[x]=-\int p(x)\log p(x)\;dx
$$


### 汎関数としてのエントロピー <!--Entropy as a Functional-->
- 通常の関数: 微分 := スカラを入力として，スカラを返す関数(演算子)
- 汎関数: 関数を入力としてスカラを返す関数(演算子)
- 機械学習における汎関数の例: スカラ値を返すエントロピー $H[p(x)]$ を最大化
  - <strong>変分原理</strong>あるいは<strong>変分推論</strong>

<!-- - Ordinary calculus deals with functions
- A functional is an operator that takes a function as input and returns a scalar
- A widely used functional in machine learning is entropy $H\BRc{p(x)}$ which is a scalar quantity
- We are interested in the maxima and minima of functionals analogous to those for functions
  - Called calculus of variations-->

## 汎関数の最大化 <!--Maximizing a Functional-->

- 汎関数: 関数からスカラへの写像
  - 最大値を与える関数を探す
  - 制約付の最大化(最小化)
  - <strong>ラグランジアン</strong>の利用

<!-- - 汎関数: mapping from set of functions to real value
- For what function is it maximized?
- Finding shortest curve length between two points on a sphere (geodesic)
  - With no constraints it is a straight line
  - When constrained to lie on a surface solution is less obvious– may be several
- Constraints incorporated using Lagrangian-->

### エントロピーの最大化<!--Maximizing Differential Entropy-->

- 確率の制約，及び，平均と分散に関する制約条件を以下のように記述:<!--Assuming constraints on first and second moments of $p(x)$ as well as normalization-->
  - $\displaystyle\int p(x)\;dx =1$ : 確率
  - $\displaystyle\int xp(x)\;dx =\mu$ : 平均
  - $\displaystyle\int (x-\mu)^2 p(x)\;dx=\sigma^2$ : 分散
- ラグランジェ乗数を使って制約条件下での最大化<<!--Constrained maximization is performed using Lagrangian multipliers. Maximize following functional w.r.t $p(x)$:-->
<!--- Constrained maximization is performed using Lagrangian multipliers. Maximize following functional w.r.t $p(x)$:-->

$$
-\int p(x)\log p(x)\,dx + \lambda_1\left(\int p(x)\;dx-1\right) + \lambda_2\left(\int xp(x)\;dx-\mu\right) +\lambda_3\left(\int(x-\mu)^2p(x)\;dx-\sigma^2\right)
$$
<!--- Using the calculus of variations derivative of functional is set to zero giving-->
各変数で微分して0と置き，整理:
$$
p(x)=\exp\left(-1+\lambda_1+\lambda_2x+\lambda_3(x-\mu)^2\right)
$$
  - 以上より連続量の最大エントロピーを与える確率分布はガウス分布となる
<!--  - Backsubstituting into three constraint equations leads to the result that distribution that maxi
mizes differential entropy is Gaussian-->

### 正規分布のエントロピーの微分 <!--Differential Entropy of Gaussian-->
<!--- Distribution that maximizes Differential Entropy is Gaussian-->
$$
p(x)=\frac{1}{\left(2\pi\sigma^2\right)^{1/2}} e^{-\left(\frac{x-\mu}{\sigma}\right)^2}
$$
- このとき最大エントロピーは以下:
<!-- - Value of maximum entropy is-->
$$
H[x]=\frac{1}{2}\left(1+\log\left(2\pi\sigma^2\right)\right)
$$

- 分散が大きくなればエントロピーは増大する
- 離散系のエントロピーとは異なり，連続系のエントロピーは $\sigma^2<\frac{1}{2}\pi e$ のとき，<strong>負</strong>となる

<!--
- Entropy increases as variance increases
- Differential entropy, unlike discrete entropy, can be negative for $\sigma^2<\frac{1}{2}\pi e$
-->

## カルバック・ライブラー・ダイバージェンス，(KL ダイバージェンス)

カルバック・ライブラーダイバージェンスは 2 つの確率密度 $p$, $q$ の乖離を表す指標である。
教科書によっては，カルバック・ライブラーの偽距離と記載されている場合もある。
また，表記として $KL\left(p\|\| q\right)$ あるいは $D_{KL}\left(p\|\| q\right)$ と表記する文献も存在する。

カルバック・ライブラーダイバージェンスは，非対称であることに注意が必要である。
すなわち $KL[p\|q] \ne KL[q\|p]$ である。
カルバック・ライブラーのダイバージェンスの非対称性は，定義を見れば納得できる。

$$ KL\left(p\|q\right)= - \int p \log\left(\frac{p}{q}\right)\;dp = -\left[\int p\log p\;dp + \int p\log q\;dp\right] $$

上式最右辺，第一項は，エントロピーの定義式であり，分布 $p$ の負の対数の平均である。
一方，上式最右辺第二項は，分布 $q$ を，$q$ の確率密度を使って平均を求めている。
このため，$\log q$ に大きな値を取る領域や部分があっても，$p$ が 0 に近ければ，両分布の乖離度合いとして計算されないことを意味している。
KL ダイバージェンスの非対称性を説明する下図に示す。

青い曲線は真の事後分布とする。
仮に双峰性の分布であると考える。
緑の分布は最適化を介して青い密度に適合させる変分近似による分布を表すものとする。
これは フォワード KL と呼ばれている。
図左のように，双峰性の真の分布を単峰性の分布で近似することを考える。
このとき，一方の峰に当てはまるように調整すると，もう一方の峰の値についての当てはまりが悪くなり結果として右下図のような裾野の広い分布を得ることになる。

反対に，緑の単峰性の分布を青の双峰性の分布で近似しようとする リバースKL を考える。
このとき基準となる真の分布である単峰性の分布の確率密度がほとんど 0 の領域では，推定する分布がどのような値を取ろうとも KL ダイバージェンス の値に影響を与えないため，いずれか一方の峰が真の分布と重なるような値を得ることになる。

<center>
<img src="/assets/forward-KL.png" width="44%">
<img src="/assets/reverse-KL.png" width="44%">
<div class="figcaption">

KL ダイバージェンスの非対称性。
フォーワード KL （左）とリバース KL (右)。
<!-- \url{https://blog.evjang.com/2016/08/variational-bayes.html} [A Beginner's Guide to Variational Methods: Mean-Field Approximation]より -->
</div></center>

大抵の場合，現実は複雑(怪奇) で（図中の青色で描かれた分布），モデル (図中の緑で描かれた分布) は素朴で単純であると考えられる。
図左は，現実が双峰性分布でモデルが単峰性分布のときに，現実(青色)からみたモデル(緑色)の乖離であるから，
現実（青）の存在する領域に，モデルが存在しない状況 （左上図）では KL ダイバージェンスは大きく，したがって，両分布の乖離は大きくなる。
したがって，現実を最もよく推定することを試みた場合 (左下図) モデル（の推定）は，裾野の広い分布と推定することとなる。

一方，単峰性分布モデル(緑)から，双峰性分布である現実（青）を見た場合，モデルと現実があっていない状況(右上図)になる。
この状態で，モデルから，無理やり現実を推定しようとする リバース KL (右下図) では，現実を最もよく推定すると，
双峰性分布の，どちらかのピークと重なる形で，モデル（緑色）は，現実 （青色）を推定してしまうこととなる。


## ELBO あるいは 変分下界 <!-- # Variational Lower Bound for Mean-field Approximation-->

変分推論の考え方は，事後推論の方法がわかっている簡単なパラメトリック分布 $Q_{\phi}\left(Z \vert X\right)$ (ガウス分布など) に対して推論を行い，パラメータ $\phi$ を調整して$P$ になるべく近づけようというものである。

<!-- The idea behind variational inference is this: let's just perform inference on an easy, parametric distribution $Q_\phi(Z | X)$ (like a Gaussian) for which we know how to do posterior inference, but adjust the parameters $\phi$ so that $Q_\phi$ is as close to $P$ as possible. -->

<!-- 青い曲線が本当の事後分布で，緑の分布が最適化によって青い密度に合わせた変分近似 (ガウシアン) である。 -->
<!-- This is visually illustrated below: the blue curve is the true posterior distribution, and the green distribution is the variational approximation (Gaussian) that we fit to the blue density via optimization. -->

<div class="figcenter">
<img src="/2023assets/Untitled+presentation+(2).png" width="44%">
</div>

分布が「近い」とはどういうことか？
平均場変分ベイズ (最も一般的な型) では，2 つの分布の間の距離指標として 逆 KL ダイバージェンスを用いる。
<!-- What does it mean for distributions to be "close"? Mean-field variational Bayes (the most common type) uses the Reverse KL Divergence to as the distance metric between two distributions. -->

$$
KL(Q_\phi(Z\vert X)\|P(Z\vert X)) = \sum_{z \in Z}{q_\phi(z \vert x)\log\frac{q_\phi(z \vert x)}{p(z \vert x)}}
$$

逆 KL ダイバージェンスは，$P(Z)$ を $Q_\phi(Z)$ に「歪める」ために必要な情報量 (つまり $\displaystyle\frac{1}{\log(2)}$ ビット) を測定する。
この量を $\phi$ に関して最小化したい。
<!-- Reverse KL divergence measures the amount of information (in nats, or units of $\frac{1}{\log(2)}$ bits) required to "distort" $P(Z)$ into $Q_\phi(Z)$.
We wish to minimize this quantity with respect to $\phi$.-->

条件付き分布の定義から $\displaystyle p(z\vert x) = \frac{p(x,z)}{p(x)}$ となる。
この式を，もとの $KL$ 式に代入して，分配してみよう。
<!-- By definition of a conditional distribution, $p(z|x) = \frac{p(x,z)}{p(x)}$.
Let's substitute this expression into our original $KL$ expression, and then distribute: -->

$$\begin{aligned}
KL(Q||P) & = \sum_{z \in Z}{q_\phi(z|x)\log\frac{q_\phi(z|x)p(x)}{p(z,x)}} \\
& = \sum_{z \in Z}{q_\phi(z|x)\big(\log{\frac{q_\phi(z|x)}{p(z,x)}} + \log{p(x)}\big)} \\
& = \left(\sum_{z}{q_\phi(z|x)\log{\frac{q_\phi(z|x)}{p(z,x)}}}\right) + \left(\sum_{z}{\log{p(x)}q_\phi(z|x)}\right) \\
& = \left(\sum_{z}{q_\phi(z|x)\log{\frac{q_\phi(z|x)}{p(z,x)}}}\right) + \left(\log{p(x)}\sum_{z}{q_\phi(z|x)}\right) \\
& = \log{p(x)} + \left(\sum_{z}{q_\phi(z|x)\log{\frac{q_\phi(z|x)}{p(z,x)}}}\right)
\end{aligned}\tag{1}$$

$KL(Q \| P)$ を変分パラメータ $\phi$ に関して最小化するには，$\log{p(x)}$ は $\phi$ に関して固定なので，$\displaystyle\sum_{z}{q_\phi(z \vert x)} \log{\frac{q_\phi(z \vert x)}{p(z,x)}}$ を最小化すればよい。
この量を分布 $Q_\phi(Z\vert X)$ に対する期待値として書き直そう。
<!-- To minimize $KL(Q||P)$ with respect to variational parameters $\phi$, we just have to minimize $\sum_{z}{q_\phi(z|x)\log{\frac{q_\phi(z|x)}{p(z,x)}}}$, since $\log{p(x)}$ is fixed with respect to $\phi$.
Let's re-write this quantity as an expectation over the distribution $Q_\phi(Z|X)$. -->

$$\begin{aligned}
\sum_{z}{q_\phi(z|x)\log{\frac{q_\phi(z\vert x)}{p(z,x)}}} & = \mathbb{E}_{z \sim Q_\phi(Z\vert X)}\left[\log{\frac{q_\phi(z\vert x)}{p(z,x)}}\right] \\
&= \mathbb{E}_Q\left[ \log{q_\phi(z|x)} - \log{p(x,z)} \right] \\
&= \mathbb{E}_Q\left[ \log{q_\phi(z|x)} - (\log{p(x|z)} + \log(p(z))) \right] && \\
& = \mathbb{E}_Q\left[ \log{q_\phi(z|x)} - \log{p(x|z)} - \log(p(z))) \right] \\
\end{aligned}$$

これを最小化することは，この関数の負の値を **最大化** することと等価である。
<!-- Minimizing this is equivalent to *maximizing* the negation of this function: -->

$$\begin{aligned}
\max\mathcal{L} &= -\sum_{z}{q_\phi(z\vert x)\log{\frac{q_\phi(z\vert x)}{p(z,x)}}} \\
& = \mathbb{E}_Q\left[ -\log{q_\phi(z|x)} + \log{p(x\vert z)} + \log(p(z))) \right] \\
& =  \mathbb{E}_Q\left[ \log{p(x\vert z)} + \log{\frac{p(z)}{ q_\phi(z\vert x)}} \right] \\
\end{aligned}\tag{2}$$

文献では，$\mathcal{L}$ は **変分下限 variational lower bound** と呼ばれ，$p(x|z), p(z), q(z|x)$ を評価できれば，計算上，扱いやすいとされている。
さらに直感的な式が得られるように項を並べ替えることができる。
<!-- In literature, $\mathcal{L}$ is known as the *variational lower bound*, and is computationally tractable if we can evaluate $p(x|z), p(z), q(z|x)$. We can further re-arrange terms in a way that yields an intuitive formula: -->

$$\begin{aligned}
\mathcal{L} &= \mathbb{E}_Q\left[ \log{p(x|z)} + \log{\frac{p(z)}{ q_\phi(z|x)}} \right] \\
            &= \mathbb{E}_Q\left[ \log{p(x|z)} \right] + \sum_{Q}{q(z|x)\log{\frac{p(z)}{ q_\phi(z|x)}}} && \\
&= \mathbb{E}_Q\left[ \log{p(x|z)} \right] - KL(Q(Z|X)||P(Z)) && \\
\end{aligned}\tag{3}$$

標本抽出 $z \sim Q(Z\vert X)$ が観測値 $x$ を潜在符号 $z$ に変換する「符号化」過程だとすると，標本抽出 $x \sim Q(X\vert Z)$ は観測値を $z$ から復元する「復号化」過程であることがわかる。
<!-- If sampling $z \sim Q(Z|X)$ is an "encoding" process that converts an observation $x$ to latent code $z$, then sampling $x \sim Q(X|Z)$ is a "decoding" process that reconstructs the observation from $z$. -->

このことから $\mathcal{L}$ は，期待「復号化」尤度 (変分分布が $Z$の標本を $X$ の標本に復号化できる程度) と，変分近似と $Z$ に関する事前分布の間の KL ダイバージェンスの和であることがわかる。
$Q(Z|X)$ が条件付きガウス分布であるとすると，$Z$ の事前分布は平均 0，標準偏差 1 の対角ガウス分布が選ばれることが多い。
<!-- It follows that $\mathcal{L}$ is the sum of the expected "decoding" likelihood (how good our variational distribution can decode a sample of $Z$ back to a sample of $X$), plus the KL divergence between the variational approximation and the prior on $Z$.
If we assume $Q(Z|X)$ is conditionally Gaussian, then prior $Z$ is often chosen to be a diagonal Gaussian distribution with mean 0 and standard deviation 1. -->

$\mathcal{L}$ が変分下界と呼ばれるのはなぜか？
式(1) に $\mathcal{L}$ を代入し直すと，以下のようになる:
<!-- Why is $\mathcal{L}$ called the variational lower bound?
Substituting $\mathcal{L}$ back into Eq. (1), we have: -->

$$\begin{aligned}
KL(Q||P) & = \log p(x) - \mathcal{L} \\
\log p(x) & = \mathcal{L} + KL(Q||P) \\
\end{aligned}\tag{4}$$

式 (4) の意味を平たく言うと，あるデータ点 $x$ の真の分布の下での対数尤度 $p(x)$ は$\mathcal{L}$ に，その特定の値 $x$ における $Q(Z\vert X=x)$ と $P(Z\vert X=x)$ 間の距離を表す誤差項 $KL(Q \vert\vert P)$ が加わるということである。
<!-- The meaning of Eq. (4), in plain language, is that $p(x)$, the log-likelihood of a data point $x$ under the true distribution, is $\mathcal{L}$, plus an error term $KL(Q||P)$ that captures the distance between $Q(Z|X=x)$ and $P(Z|X=x)$ at that particular value of $X$.-->

$KL(Q||P) \geq 0$ なので，$\log p(x)$ は $\mathcal{L}$ より大きい必要がある。
よって，$\mathcal{L}$ は $\log p(x)$ の **下限 lower bound** である。
また，$\mathcal{L}$ は別形式で証拠下界 (ELBO) とも呼ばれる。
<!-- Since $KL(Q||P) \geq 0$, $\log p(x)$ must be greater than $\mathcal{L}$.
Therefore $\mathcal{L}$ is a *lower bound* for $\log p(x)$.
$\mathcal{L}$ is also referred to as evidence lower bound (ELBO), via the alternate formulation: -->

$$\mathcal{L} = \log p(x) - KL(Q(Z|X)||P(Z|X)) = \mathbb{E}_Q\left[ \log{p(x|z)} \right] - KL(Q(Z|X)||P(Z))$$

なお，$\mathcal{L}$ 自体には，近似事後確率と事前確率の間の KL ダイバージェンス項が含まれているので，$\log p(x)$ には合計 2 つの KL 項が含まれることになる。
<!-- Note that $\mathcal{L}$ itself contains a KL divergence term between the approximate posterior and the prior, so there are two KL terms in total in $\log p(x)$. -->

<!-- # 順方向 KL と逆方向 KL -->
<!-- # Forward KL vs. Reverse KL-->

<!-- KL ダイバージェンスは対称距離関数ではなく，$KL(P||Q) \neq KL(Q||P)$ ($Q \equiv P$ である場合を除く) である。
前者は「順向 KL」、後者は「逆向 KL」と呼ばれる。
では、なぜ 逆向 KLを使うのだろうか？
それは，結果として得られる導出が $p(Z|X)$ の計算方法を知っている必要があるからである。 -->
<!-- KL divergence is *not* a symmetric distance function, i.e. $KL(P||Q) \neq KL(Q||P)$ (except when $Q \equiv P$).
The first is known as the "forward KL", while the latter is "reverse KL".
So why do we use Reverse KL?
This is because the resulting derivation would require us to know how to compute $p(Z|X)$, which is what we'd like to do in the first place. -->

<!-- [PML 教科書](https://www.cs.ubc.ca/~murphyk/MLbook/) にある Kevin Murphy の説明がとても好みなので，ここで再掲してみることにする。 -->
<!-- I really like Kevin Murphy's explanation in the [PML textbook](https://www.cs.ubc.ca/~murphyk/MLbook/), which I shall attempt to re-phrase here: -->

<!-- まず，順方向 KL を考える。
上の導出で見たように KL は重み関数 $p(z)$ に対する「罰則」関数 $\displaystyle\log \frac{p(z)}{q(z)}$ の期待値として書くことができる。 -->
<!-- Let's consider the forward-KL first. As we saw from the above derivations, we can write KL as the expectation of a "penalty" function $\log \frac{p(z)}{q(z)}$ over a weighing function $p(z)$. -->

<!-- $$\begin{aligned}
KL(P||Q) & = \sum_z p(z) \log \frac{p(z)}{q(z)} \\
& = \mathbb{E}_{p(z)}{\left[\log \frac{p(z)}{q(z)}\right]}\\
\end{aligned}$$ -->

<!-- ペナルティ関数は $p(Z) > 0$ のとき，全 KL に損失を寄与する。
$p(Z) > 0$ の場合，$\lim_{q(Z) \to 0}\log\frac{p(z)}{q(z)} \to \infty$ となる。
これは，$Q(Z)$ が $P(Z)$ を「カバー」できないところでは，順向 KL が大きくなることを意味する。 -->
<!-- The penalty function contributes loss to the total KL wherever $p(Z) > 0$.
For $p(Z) > 0$, $\lim_{q(Z) \to 0} \log \frac{p(z)}{q(z)} \to \infty$.
This means that the forward-KL will be large wherever $Q(Z)$ fails to "cover up" $P(Z)$.-->

<!-- よって，$p(z)>0$ のところでは $q(z)>0$ を確保すれば，順向 KL は最小になることがわかる。
最適化された変分分布 $Q(Z)$ は「ゼロ回避 zero-avoiding」($p(Z)$ がゼロのとき，密度がゼロを回避する) として知られている。 -->
<!-- Therefore, the forward-KL is minimized when we ensure that $q(z) > 0$ wherever $p(z)> 0$.
The optimized variational distribution $Q(Z)$ is known as "zero-avoiding" (density avoids zero when $p(Z)$ is zero). -->

<!-- <div class="figure figcenter">
<img src="figures/forward-KL.png" width="44%"> -->
<!-- ![image](../assets/forward-KL.png) -->
<!-- {width="49%"} -->
<!-- </div> -->

<!-- 逆向 KL を最小化すると，全く逆の挙動になる: -->
<!-- Minimizing the Reverse-KL has exactly the opposite behavior: -->

<!-- $$\begin{aligned}
KL(Q||P) & = \sum_z q(z) \log \frac{q(z)}{p(z)} \\
& = \mathbb{E}_{p(z)}{\left[\log \frac{q(z)}{p(z)}\right]}\
\end{aligned}$$

$p(Z)=0$ ならば，分母 $p(Z)=0$ であればどこでも重み付け関数 $q(Z)=0$ を確保しなければ，KL は吹き飛んでしまう。
これは「ゼロ強制 zero-forcing」と呼ばれる。
<!-- If $p(Z)=0$, we must ensure that the weighting function $q(Z)=0$ wherever denominator $p(Z)=0$, otherwise the KL blows up.
This is known as "zero-forcing": -->

<div class="figure figcenter">
<img src="/assets/reverse-KL.png" width="44%">
</div>

<!-- つまり 順向 KL を最小化すると変分分布 $Q(Z)$ が $P(Z)$ 全体を **覆う** ように「伸び」，逆向 KL を最小化すると $P(Z)$ の **下に** $Q(z)$ が「しぼむ」。 -->
<!-- So in summary, minimizing forward-KL "stretches" your variational distribution $Q(Z)$ to cover **over** the entire $P(Z)$ like a tarp, while minimizing reverse-KL "squeezes" the $Q(Z)$ **under** $P(Z)$.-->

<!-- 機械学習の問題で平均場近似を使うとき，逆 KL を使うことの意味を覚えておくことが重要である。
単峰性の分布を多峰性の分布に当てはめると，偽陰性が多くなる ($Q(Z)$ は何もないと思っていたのに，$P(Z)$ は実際に確率的な量がある) ことになる。 -->
<!-- It's important to keep in mind the implications of using reverse-KL when using the mean-field approximation in machine learning problems.
If we are fitting a unimodal distribution to a multi-modal one, we'll end up with more false negatives (there is actually probability mass in $P(Z)$ where we think there is none in $Q(Z)$). -->

<!-- # Connections to Deep Learning-->

<!-- 変分法は Deep Learning にとって本当に重要である。 -->
<!-- 詳しくは後日記事にしますが，ここでは簡単にネタバレします。 -->
<!-- Variational methods are really important for Deep Learning.
I will elaborate more in a later post, but here's a quick spoiler: -->

<!-- 1. ディープラーニングは，たくさんのデータを使った非常に大きなパラメータ空間での最適化(具体的には勾配降下法) が得意だ。
2. 変分ベイズは，統計的推論問題を最適化問題として書き直すことができる枠組みを与えてくれる。 -->

<!-- 1. Deep learning is really good at optimization (specifically, gradient descent) over very large parameter spaces using lots of data.
2. Variational Bayes give us a framework with which we can re-write statistical inference problems as optimization problems. -->

<!-- 深層学習と変分ベイズの組み合わせにより，極めて複雑な事後分布の推論が可能になる。
結果的に，変分自己符号化器のような最新の技術は，この投稿で導かれたのと全く同じ平均場変分下界を最適化する -->
<!-- Combining Deep learning and VB Methods allow us to perform inference on *extremely* complex posterior distributions.
As it turns out, modern techniques like Variational Autoencoders optimize the exact same mean-field variational lower-bound derived in this post! -->


<!-- ## ある日のとある Slack team の会話より
from `2017rnn_book/bayes_learning.md`

「５回に１回の割合で帽子を忘れるくせのあるＫ君が，正月に Ａ，Ｂ，Ｃ ３軒を順に年始回りをして家に帰ったとき，帽子を忘れてきたことに気がついた。２軒目の家 Ｂ に忘れてきた確率を求めよ。」  早稲田大学（１９７６年文学部）で出題された入試問題  [http://www004.upp.so-net.ne.jp/s_honma/probability/bayes.htm](http://www004.upp.so-net.ne.jp/s_honma/probability/bayes.htm) より

新：同時確率を考えると（４/5）×（1/5）×（4/5）=16/125
  忘れた確定ならABCのどっかで忘れたんだから1/3 (自分はこの考えです)
  などいろいろある問題で
  ぶっちゃけ解がわからない

浅：同時確率を計算しただけでは，帽子を忘れたことに気が付いたという事実を考慮していないことになりますよね。帽子を忘れたという事象が生起する確率は 1/5 なのだから分母は全く忘れなかったを１から引いて 1-(4/5)^3 = 61/125. すなわち帽子を忘れたという事象が生起した確率。一方分子はA宅で忘れない(4/5)でかつB宅で忘れた(1/5)事象が起きたのでこれらの積で表される(4/5 * 1/5 = 4/5^2). 以上を計算すれば (4/25)/(61/125) = 20/61. ベイズ的には帽子を忘れたという事象が生起したという事実から考慮すべき確率空間，すなわち分母が変化するので新村さんの考えた同時確率 16/125 を帽子を忘れたという事実を知ったために調整しなければいけない，ということであります。

新：ぬぬ？abcのどこかに忘れたので1/3という解答はおかしいですかね？
  20/61だとしたら
  aに忘れてる確率も，bに忘れてる確率も同様になって
  あ，違うのか。
  順番に回ったから違うのですなぁ
  納得
  となると，よく忘れ物をする人は，最後に見たすぐ後に忘れてる可能性が最も高いのか
  確かにそんな気がします

---

## 解説
帽子を忘れた場所の確率は __負の二項分布__ Negative binomial distribution に従う。負の二項分布の確率密度は以下で与えられる：

$$
NB(X=x;r,p)=\left({x+r-1}\over{x}\right)\;p^{x}\left(1-p\right)^{r}
$$

負の二項分布を，上の例題に対応させて式中の文字の意味を記せば次のようになる。$p(=4/5)$ は帽子を忘れない確率，$1-p(=1/5)$ は反対に帽子を忘れる確率である。$p^x$ は $x$ 回帽子を忘れなかったことを意味し，$(1-p)^r$ は帽子を $r$ 回忘れなかったこととなる。今回は $r=1$ であり帽子を忘れた時点で次の家を訪問してもしなくても関係なくなる。負の二項分布とは $r$ 回失敗する前に成功回数が $x$ 回である確率を表している。[Wikiptediaを参照](https://en.wikipedia.org/wiki/Negative_binomial_distribution)。

1. 最初の訪問宅である A で帽子を忘れれば $p^{0}\;(1-p)^{1}$ で $p=\displaystyle\frac{4}{5}$ を代入すれば $Pr(A)=\displaystyle\frac{1}{5}=\frac{5}{25}=\frac{25}{125}$ となる。
2. B で帽子を忘れた場合は $Pr(B)=p^{1}\;(1-p)^{1}=\displaystyle\frac{4}{5}\;\left(1-\frac{4}{5}\right)=\frac{4}{25}\times\frac{1}{5}=\frac{20}{125}$ を得る。
3. C で帽子を忘れた場合は A, B で帽子を忘れず $x=2$ (成功２回)，C で忘れるのであるから  $p^{2}\;(1-p)^{1}=\displaystyle\left(\frac{4}{5}\right)^2\times\left(\frac{1}{5}\right)=\left(\frac{16}{25}\right)\times\left(\frac{1}{5}\right)=\frac{16}{125}$

比較が容易なように上では分母を $125$ に揃えた。上記のように A で帽子を忘れた確率が最も高くなる。負の二項分布で $r=1$ の場合は，初めて失敗する $r=1$ までに連続して成功した回数が $x$ となる。ベイズ確率を計算するには上の３つの起こった確率を足し合わせた値を分母にする。

$$
\frac{\frac{20}{125}}{\frac{25}{125}+\frac{20}{125}+\frac{16}{125}}=\frac{\frac{20}{125}}{\frac{61}{125}}=\frac{20}{61}
$$

このようにどこかの家で帽子を忘れたのだから等確率で $\displaystyle\frac{1}{3}$ という直観に反して B で忘れた確率は $\displaystyle\frac{1}{3}$ より少しだけ小さい $\displaystyle\frac{20}{61}$ となる。

---

### 繰り返し忘れるとどうなるか （ベイズ更新）

等確率の原理からどの家でも忘れる確率は等しく $\displaystyle\frac{1}{3}$ は事前知識あるいは事前分布を表している。そこで上式を事前知識を加味して書けば，

$$
\frac{\frac{20}{125}\times\frac{1}{3}}{\frac{25}{125}\times\frac{1}{3}+\frac{20}{125}\times\frac{1}{3}+\frac{16}{125}\times\frac{1}{3}}=\frac{\frac{20}{125}\times\frac{1}{3}}{\frac{61}{125}\times\frac{1}{3}}=\frac{20\times\frac{1}{3}}{61\times\frac{1}{3}}=\frac{20}{61}
$$

すなわち事前分布が等しく $\displaystyle\frac{1}{3}$ であったので省略してあったのである。ところが，一度帽子を忘れたという事実を観測した場合，上に従ってそれぞれの家で忘れる確率が $\displaystyle\frac{1}{3}$ ではなくなる。すなわち，

- $Pr(A)=\displaystyle\frac{25}{61}\doteq0.410$,
- $Pr(B)=\displaystyle\frac{20}{61}\doteq0.328$,
- $Pr(C)=\displaystyle\frac{16}{61}\doteq0.262$,

であるから，事前分布としてこの値を代入すれば，B に忘れた確率は $Pr(B)$ は

$$
\frac{\frac{20}{125}\times\frac{20}{61}}{\frac{25}{125}\times\frac{25}{61}+\frac{20}{125}\times\frac{20}{61}+\frac{16}{125}\times\frac{16}{61}}
=\frac{\frac{20^2}{125\times61}}{\frac{25^2+20^2+16^2}{125\times61}}
=\frac{20^2}{25^2+20^2+16^2}=\frac{400}{625+400+256}=\frac{400}{1281}\doteq0.312
$$

として求まる。同様の計算によって次式を得る：

$$
Pr(A)=\frac{25^2}{25^2+20^2+16^2}=\frac{625}{1281}\doteq0.487
$$

$$
Pr(C)=\frac{16^2}{25^2+20^2+16^2}=\frac{256}{1281}\doteq0.201
$$

A, B, C それぞれに帽子を忘れる確率は観測のたびに変化する。数式で表現すれば以下のようになる。
$$
P(\theta_{i}|D)=\frac{P(D|\theta_{i})P(\theta_{i})}{\sum_{j}P(D|\theta_{j})P(\theta_{j})}
$$
上式はベイズ更新と呼ばれる。ニューラルネットワークなどで $\theta$ を重み係数と考え $D$ を訓練データとみなせば上式は __ベイズ学習則の定義__ であり，重み係数の更新式である。ベイズ更新とは現在の重み係数と得られたデータから重み係数を更新する方法であると解釈可能である。 -->
