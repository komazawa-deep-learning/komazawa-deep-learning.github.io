---
title: 2022年度 駒澤大学心理学特講IIIa
layout: home
---

<!--
この用語集は，~/study/2021corona/glossary.md が元になっている
-->

DETR, 

# 用語集

* **フレッシェ距離，フレッシェ得点** Frechet distance, Frechet score (FID): 生成敵対ネットワークにおいて，データ画像と生成画像との間の距離の定義の一つ。または 2 つの確率密度関数間の距離として定義される。$x, y$ をガウス分布に従う確率変数とすると FID は (平均間の差の 2 乗 と 各変数の共分散行列の和から共分散行列の積の 2 倍を減じた行列のトレースの 1/2 乗 との和) 次のように定義される $FID(x,y)=|\mu_{x}-\mu_{y}|^2 + \text{tr}\left(\Sigma_{x}+\Sigma_{y}-2\left(\Sigma_{x}\Sigma_{y}\right)^{1/2}\right)$
* **インセプション得点** Inception score (IS): 生成敵対ネットワークなどで生成された画像と元画像との品質を評価するための尺度。データ $x$ に基づいて生成された画像 $y$ の条件付き確率と $y$ との KL ダイバージェンスの指数乗 として定義される。$IS=\exp\left(\mathbb{E}_{x\sim g}KL(p(y|x)||p(y))\right)$
* **チューリングテスト** Turing test: チューリングが考案した思考実験。この思考実験では，端末をとおして，評価者と人またはコンピュータが通信する。このとき評価者が通信相手を人かコンピュータかを判断できなかったとしたら，そのとき，その通信相手のコンピュータは知性を持っているとみなす。
* 中国語の部屋:
* ダートマス会議: ダートマス大学において 1955 年夏に開催された会議。この会議で人工知能という言葉を用いることになった。それ以前は，サイバネティクス (自動制御) などの用語が用いられていた。この会議の参加者には，ミンスキー，マッカーシー，など初期の人工知能研究者が含まれる。
* **AI の冬** AI winter: 人工知能研究は，活発になる時期と下火になる時期を繰り返している。この下火になった時期のことを AI の冬と呼ぶ。AI の夏，すなわち AI ブーム は過去に 3 度あった。その間の時期を AI の冬と呼ぶ。このため，現在のところ AI の冬は 2 回存在する。
* **機械学習** machine learning データを用いて現象の記述，予測，分類を行う統計学の分野。人工知能の分野と考える場合もある。
* 教師あり学習 supervised learning データが与えられた時に，学習機の出力として望ましい値も与えらていている課題を言う。望ましい値のことを教師信号と呼ぶ。データ $x$ を教師信号 $y$ へと変換する意味では $y=f(x)$ であるから，教師あり学種とうは $f$ の精度を向上させることが機械学習の目標となる
* **教師なし学習** unsupervised learning: データに対して教師信号が与えられない場合を指す。学習機は所与のデータの統計的性質を学習することが求められる。
* **半教師あり学習** semi-supervised learning: 
* **回帰** regression 原因となる量 (説明変数) から結果となる量 (被説明変数) を予測すること。小学生以来の直線のグラフ，およびその拡張を線形回帰と呼ぶ。一方，直線以外の予測を非線形回帰と言う。予測する量が量的である場合を回帰と呼び，質的であれば分類と読んで区別することがある。
* **分類** classification: データ分析において，予測すべき量 (被説明変数) が離散的な場合を指す。回帰の場合はこの量が連続量であるのに対し，分類の場合は離散量となる。ロジスティック回帰では，任意のクラスに属する確率を予測する。
* **ナイーブベイズ** Naive Bayes ベイズの定理を用いた分類器。
* AdaBoost: 
* Nearest Neighbors: 最近隣法，
* **clustering**: クラスタリング
* **PCA**: 主成分分析と訳される。行列の固有値分解に基づいてデータ縮約，次元圧縮に用いられる手法。
* **パーセプトロン** Perceptrons: ローゼンブラット (Rosenblatt) によって考案された第一次ニューロブームにおける知覚モデル。多層化されたモデルも提案されたが，学習については最上位層とその直下層との間の結合係数の調整に限られる。また，オリジナルのパーセプトロンの出力関数は 2 値のみ，すなわち真か偽かのいずれか一方の値を出力する。
* **最小二乗法** least squared methods: 出力値と目標値，または教師信号との間の差の 2 乗を誤差関数とみなし，この誤差関数を最小にすることでパラメータを調整する手法。回帰分析において広く用いられている解法の一つである。ルジャンドルによって 1805 年に発表された。だが，数多くの業績を公刊せずに用いていたガウスが 1795 年に発見していたとされ。このため最小自乗法発見の功績は，ルジャンドルとガウスの共同名義とされる場合がある。
* **最尤法** Maximum likelihood method: 
* **情報量** Information criteria: 有る出来事が起こる確率にその確率を対数変換した値を掛けた量。または，この情報量の総和を言う。情報理論では対数の底を 2 とする場合が多い。幾何学的解釈が用いられる場合には，自然対数の底が用いられる。
* EM アルゴリズム: デンプスター (Dempster) ら によって提唱された，未観測変数を含む最尤推定を行うアルゴリズム。未観測変数を推定する E ステップと，目的関数を推定する M ステップとの 2 段階からなる。
* パンデモニアムモデル: セルフリッジ (Selfridge) によって提唱された知覚モデル。パンデモニアムとは，悪魔 (デーモン) が棲む城を意味する伏魔殿である。伏魔殿には複数のデーモンが棲んでいて，各デーモンは定まった役割を分担する。現代的な言葉では特徴抽出器のことを自律的に活動するデーモンに喩えたモデル。
* バックプロパゲーション: 誤差逆伝播法と訳される。ニューラルネットワークを含む非線形システムの訓練に用いられる計算方法。
* 損失関数: ニューラルネットワークを含む関数最適化の際に定義される関数。この関数の値を最大，または最小にするようにシステムは訓練される。
* 交差エントロピー: ニューラルネットワークを含む非線形システムの損失関数の定義の一つ。正と負との二値化した教師信号に対して，エントロピーを目標関数とする。正事例と負事例の関数が交差することから，交差エントロピーと呼ばれる。
* 確率的勾配降下法 SGD: ボット- (Bottou) らによって提案されたミニバッチを用いた訓練手法。
* 最適化手法
* 自然勾配法 甘利によって提案された勾配降下法による最適化手法の一つ，フィッシャーの情報行列に従って勾配を定める。
* フィッシャー情報量 パラメータの
* 相互活性化モデル
* 自己組織化，
* インフォマックス基準，情報量を最大化する基準
* Kohonen の SOM (自己組織化)
* HOG
* SIFT
* ガウシアンピラミッド
* ラプラシアンピラミッド
* ドロップアウト
* スキップ結合
* ソフトマックス関数
* LeNet
* Inception
* ResNet
* EfficientNet
* 標準正則化理論
* 物体認識 
* 相貌失認
* ゲーム理論
* ナッシュ均衡
* **GAN 生成敵対ネットワーク** Generative Adversarail Networks: 
* **単純再帰型ニューラルネットワーク** Simple Recurrent Networks: 中間層に帰還信号を持つネットワーク。
* エルマンネット Elman and Jordan
* BPTT
* 系列学習
* 報酬
* 価値
* TD 誤差
* 方策
* イプシロン貪欲探索
* マルコフ決定過程
* SARSA: State Action Reward State Action 日本語では，状態，行動，報酬，状態，行動，となる。強化学習の価値更新式で，この用語の順に式が並んでいることから命名された。
* Q 学習: 状態価値関数
* DQN Deep Q Network
* 価値反復 value iteration
* 方策反復 policy iteration
* 優先付き再生 prioritized replay 
* 経験再生 experience reply
* **A3C** Asynchronous Advantage Actor Critic の頭文字をとったモデル。強化学習に用いられるアルゴリズムの一つ。
* エージェント57
* **補助学習目的関数** 主学習目的関数と一緒に学習することで，モデルの汎用性を高め，性能を向上させるための追加学習目的または課題のこと。 Auxiliary Learning Objective <!-- この [論文](https://arxiv.org/abs/1704.07156) では，この概念について詳しく説明している。 -->
* **マスク化** 文中の単語を削除したり，他のダミートークンで置き換えたりして，学習時にモデルがそれらの単語にアクセスできないようにすること。Masking 
* **バイトペアエンコーディング** : データ圧縮技術の 1つ。 頻繁に出現する連続したバイト対を，データには存在しないバイトに置き換えることでデータを圧縮する技術。Byte Pair Encodings <!-- 元データを復元するには，置き換えられたバイトの写像を含むテーブルを使用する。[このブログ](https://towardsdatascience.com/byte-pair-encoding-the-dark-horse-of-modern-nlp-eb36c7df4f10) では BPE について詳しく説明している。 -->
* **ゼロショット学習**:  ある課題を実行する際に，過去にその課題を実行したことがないモデルの能力である。ゼロ撃学習では勾配の更新は行われず，モデルは例題を見ることなく課題を理解することになっている。ゼロショット課題転送またはメタ学習は，モデルにほとんど例を示さず，課題を理解させる設定を指す。ゼロ撃という言葉は，勾配更新が行われないことに由来する。モデルは例題と指示に基づいて課題を理解することになっている。Zero shot learning
* **錯綜度 (パープレクスティ)** 言語モデルの標準的な評価指標の一つ。パープレックスとは，テストセットの逆確率をテストセットの単語数で正規化したもの。パープレックス値が低い言語モデルは，高い言語モデルよりも優れているとされる。perplexity <!--パープレックスについての詳しい説明は [こちらのブログ](https://towardsdatascience.com/perplexity-in-language-models-87a196019a94) を参照。-->
* **逆強化学習** : 通常の強化学習（RL) が，エージェントが行った行動から報酬を予測することであるのに対して，観察された報酬から価値関数，あるいは Q 関数を予測する。Inverse Reinforcement Learning (IRL)  <!-- [@2000NgRussell_InverseRL]-->
* **MAML** Model Agnostic Meta Learning: (MAML マムルと発音する) モデルに依存しないメタ学習 Chelsea Finn の論文 (2020) を参照
* **VAE 変分自己符号化器** : 自己符号化器モデルの中間表象に (直交正規分布に基づく) 潜在変数 を導入するモデル。2014 年に Kingma and Welling と Rezende らによって提案された。Variational Auto-Encoders
* **BERT** 多頭自己注意機構に基づく，言語モデル。入力情報を 3 重化し，それぞれ Q, K, V, として用いる。Q と K との積の結果と V とから出力を得る。学習時には，マスク化言語モデルと次文予測課題とで事前訓練を行い，各下流課題に対して微調整を行うことで精度向上が示された。従来モデルであるリカレントニューラルネットワークモデルに基づく言語処理モデルを置き換える動きが主流となっている。BERT は **B**idirectional **E**ncoder **R**epresentations from **T**ransformers の略だとされる。それまで，リカレントニューラルネットワークが主流であった自然言語処理課題のほとんどにおいて，BERT に基づくモデルが性能を凌駕している。
* **CAM** 画像認識課題において，入力画像中のどの領域が，当該カテゴリーと判断するために貢献したかを示すための手法，またはアルゴリズムを指す。Class Association Mapping
* **EM アルゴリズム** 観測データ，未観測データ (もしくは潜在変数) の 2 種類があるときのモデルの最尤推定量を算出するアルゴリズム。E ステップでは，未観測データの推定を行い，M ステップでは，未観測データを推定した値であるとみなして最尤推定を行う。これらの E ステップと M ステップとを交互に繰り返すことにより，モデルの推定と未観測データ (もしくは潜在変数) の推定を行う手法である。
* **GAN generative adversarial networks**: 敵対的生成ネットワーク。 画像，言語を生成するニューラルネットワークモデルの一つ。 GAN 内部には，生成器と識別器と 2 つのネットワークが存在し， 互いに競合関係の中で学習が行われる。
* **GPU Graphical Processing Units**: グラフィック処理ユニット。コンピュータの中央演算装置 CPU に対してグラフック処理に特化した演算装置のこと。 PC 上でゲームをするために開発されたが，ディープラーニングや暗号通貨の計算でもゲームのグラフィック処理と同様の並列計算が行われる。 このため GPU を使ってディープラーニングモデルの学習を高速化することが一般的となっている。
* **LSTM 長-短期記憶 long short-term memory**: リカレントニューラルネットワークモデルの一つで，ゲートを内部に持つ。 注意機構を実装したトランスフォーマー以前は LSTM が支配的な地位を占めていた。
* **Q 学習** 動作主が，ある状況において，ある動作を行った際に期待される報酬を定義する関数を Q 関数と呼ぶ。すなわち Q 関数には 2 つの引数 状態 s と，この s という状態で行った行動 a によって定まる関数である。このため $Q(s,a)$ のように表記される。Q 関数を最大化するような学習を Q 学習と呼ぶ。より正確には，Q の値は，状態 s のときに行動 a を採択した場合の将来に渡る報酬，すなわち期待報酬で定義される。$Q(s,a)=\mathcal{E}\left[R+\gamma R+\gamma^{2} R+\cdots\vert s,a\right]$
* **R-CNN** (what/where or ventral/dorsal pathway: 領域切り出しと， 切り出された領域に対して認識を行うモデル。 このモデルの提案により， ほぼ実時間で領域切り出しと物体認識が可能になった。
* **SOTA**: State of the arts 現時点での最高性能の意。
* **Seq2seq** 入力系列を出力系列へと変換するための機構。系列から系列へ (sequence-to-sequnce) の略称である。系列処理を司るリカレントニューラルネットワークを 2 つ連結させた形をとるニューラルネットワークモデルである。入力側の中間層状態を出力側の中間層の初期状態とするのが，原型である。このとき中間層の状態に対して注意機構を用いることが行われる
* **TLPA** 日本で失語症の臨床診断に用いられている 失語症語彙検査 (**T**est of **L**exical **P**rocessing in **A**phasia) の一つである。語彙判断検査, 名詞表出検査, 名詞理解検査，絵画命名検査などの下位検査から構成されている。日本に失語症検査としては WAB (西洋失語症検査項目 Western Aphasia Battery) 日本語版 や SALA (上智大学失語症言語分析 **S**ophia **A**nalysis of **L**anguage in **A**phasia) などがある。
* **U-net**: 画像中の領域切り出しにおいて，高精度を得ることができるモデル。X 線画像から，関心領域 (腫瘍や変性) を切り出すことができる。
* **one convolution**: 畳み込みニューラルネットワークにおいて，カーネル幅が 1 である畳み込みを指す。特徴方向には畳み込みが行われることに注意。
* **word2vec** 単語埋め込みモデルの一つ。単語の意味を，前後の単語によって表現する スキップグラムと CBOW という 2 つのモデルがある。
* **おばあちゃん細胞仮説 grandmother hypothesis**: 脳の情報表現について，分散か局在かの論争の中で提唱された仮説。 自身のおばあちゃんを見たときにだけ応答を示す神経細胞が存在するという考え方を指す。 ニューラルネットワークとの関連では，疎性表現，あるいはワンホット表現と関連する。
* **アクター・クリティック法** 動作主の内部に，行動を選択する機構，すなわちアクターと，アクターが行動を行った場合の環境から与えられた報酬を用いて，アクターの行動を評価する機構，すなわちクリティク (批評家) の両者を併せ持つ強化学習の手法。具体的には，アクターは方針，クリティックは Q 関数 (または価値関数) である。
* **アドバンテージ関数** 強化学習において，$Q(s,a)$ 値と $V(s)$ との差分をアドバンテージ advantage と呼ぶ。
* **アレックスネット AlexNet**: 2012 年の ImageNet コンテンストにおいて，ディープラーニングアルゴリズムが初めて大規模画像認識で 1 位を獲得したときのディープラーニングモデルのこと。 第 1 著者のファーストネームから アレックスネットと呼ばれる。畳み込みニューラルネットワークとデータ拡張を特徴とする。 GPU が本格的に使用されるきっかけともなった。
* **エンドツーエンド**: 複雑で職人芸的な前処理，や後処理を必要としないで， （ほぼ）生データから一気に結論までを実行する処理や手順のこと。 エンドツーエンドを可能としたことがディープラーニングの特徴の一つである。 このエンドツーエンドにより， より高次で複雑な仕事や処理への発展，ビジネス展開が可能となる。
* **オペランド条件づけ** 環境に働きかけることで，報酬を獲得し，行動が変容することを指す概念。バーハス・F・スキナーによって提唱された。
* **カーネル kernel**: 畳み込み演算において，核 (kernel) となる関数のこと。畳み込みニューラルネットワークに置いては推定すべき結合係数である。
* **シグモイド関数 sigmoid functions**: 直訳すれば S 字状の曲線の意味である。ニューラルネットワークの活性化関数としても用いられてきた。 近年では勾配消失問題の回避のため別の活性化関数が採用されることが多い。 ただし，注意機構や LSTM のゲートの開閉にはシグモイド関数が用いられている。
* **スキップ結合 skip connections**: 階層型ニューラルネットワークにおいて，層をまたぐ結合のこと。
* **ストライド stride**: 畳み込みニューラルネットワークにおいて，カーネルの移動幅のこと
* **ストループ効果** 色のついた文字を読み上げる課題で，文字音読条件と文字の色名呼称条件とを比較した場合，両条件の音読潜時に差異が認められる現象。
* **ソフトマックス関数 softmax function**: 多値分類を行う最終層において，候補選択の際に用いられる出力関数の一つ。対比学習や注意においても重要な役割を果たす。
* **ソフトマックス関数** 複数の候補から，もっとも値の大きい項目一つ選び出す機構として頻用される関数。このため，注意を表現するためにも用いられる。たとえば $a=1,b=2,c=3$ のとき，ソフトマックス関数を用いて確率に変換する場合と，単純に総和 $a+b+c$ で除して確率化する場合とを比較するとソフトマックス関数によれば $p(a)\simeq0.09,p(b)\simeq0.24,p(c)\simeq0.67$ であるのに対して，総和による確率化では $p(a)\simeq0.16,p(b)\simeq0.33,p(c)=0.5$ となる。このように，ソフトマックス関数による確率化では，最大値 (本例の場合 c の値) がより強調される結果となる。 ソフトマックスの反対語としてハードマックスが挙げられる。ハードマックスでは，最大値をとる項目を 1 とし，他の全ての項目を 0 とする。ハードマックスの場合は，微分が不可能となる。このためハードマックスは，ニューラルネットワークの学習には不向きと言える。
* **ダイレーション dilation**: 畳み込み演算において，データのサンプル点の間隔を表す。 dilation=1 であれば通常の畳み込みである。dilation=2 であれば， 一画素飛ばしで畳み込みを行うことになる。
* **ディープニューラルネットワーク deep neural networks**: または ディープラーニング，深層学習，とも呼ばれる。 1980 年代の第二次ニューロブームまでは 3 層のニューラルネットワークが主流であった。 今世紀に入って，多層のニューラルネットワークを構築するための要因が整い多層化した。 その結果ニューラルネットワークの大規模化，性能の向上が可能となり，第 3 次ブームとなった。
* **データセット（訓練，検証，テスト） dataset**: ニューラルネットワークに限らず，機械学習におけるモデルの学習，パラメータのチューニングにもちいるデータのこと。 パラメータの設定に用いるデータを訓練データ。 妥当性の検証に用いるデータを検証データと呼ぶ。 モデルの性能評価に用いるデータをテストデータと呼ぶ。 公開されているデータセットにおいては， 訓練データとテストデータに分けられていることが多い。 検証データは，訓練データを分割して用いることがある。
* **データ拡張 data augmentation**: 限られたデータを部分的に変更して， データを増やす手法のこと。 画像や音声データでは， 拡大， 縮小， 回転， 反転， 色調変換， 周波数変調などを行う場合がこれに該当する。
* **トランスフォーマー** 多頭自己注意 muliti-head self attention を用いた言語モデル。
* **ドロップアウト dropout**: ニューラルネットワークにおける般化性能向上手法の一つ。 ニューロン間の結合をランダムに 0 にすることで実現される。 ドロップアウトにより，入出力関係が確率的に変動するので， 決定論的な推論をするよりも，確率的な変動を学習することになる。
* **ニューラルネットワーク neural networks**: 神経細胞の機能を模したモデル一般を指す。 実際の神経系のニューラルネットワークを 生物学的ニューラルネットワーク (BNN: biological neural networks) と呼ぶ。一方，BNN を簡略化，単純化，抽象化したモデルを人工ニューラルネットワーク （ANN: artifitial neural networks) と呼ぶ。実際のニューロンの抽象化の程度により，複数に分割される。最も単純な人工的ニューラルネットワークは，下位層ニューロンの信号を重み付けして足し合わせる $\sum_{i} w_{i} x_{i}$ ような場合も含まれる。
* **バイアス bias**: ニューラルネットワークにおける定数項のこと。バイアス項がない場合もある。
* **パディング padding**: 畳み込みニューラルネットワークにおいて， カーネルがデータ領域の外に出る場合に埋め草として用いる量あるいはその手法のこと。ゼロパディングであれば，埋め草として 0 を用いる，`same` パディングであれば連接データと同じ値を埋め草の値として用いることを表す。
* **パレイドリア** 視覚的妄想の一つ。幻視と呼ばれることもある。偏頭痛に伴う視覚障害では，単純な線分や白黒チェッカーパタンのような単純な幾何学模様が視認されるのに対して，パレイドリアでは高次視覚特徴により視覚経験が報告される。このため，初期視覚情報処理ではなく，高次視覚情報処理の障害であると考えられる。授業では，ディープラーニングモデルの上位層からのフィードバックによるトップダウン信号と，下位層 (初期視覚情報処理) との間の差異を強調するアルゴリズムを持ちいたモデルを実習した。
* **パーセプトロン perceptron**: 第 1 次ニューラルネットワークブームの際にフランク・ローゼンブラットによって提案されたニューラルネットワークモデル。出力層と直下層との間の結合係数を調整するための学習機能を有する初期のモデルの一つ。
* **ファインチューニング fine tuning**: 詳細微調整とも訳される。 訓練済のモデルに対して， 解くべき課題に特化した追加学習を行う際の学習を指す。 しばしば全結合係数を再学習することを指す。 乱数を用いた初期値から学習するよりも学習時間が短縮される。再学習時に，全層のパラメータを再調整する。 最終層と最終直下層との間野結合係数のみを調整する転移学習の反対語。
* **プーリング pooling**: 畳み込み層の上位にあって，下位層の演算結果を併せて出力とする技法。手法により，最大値プーリングや平均値プーリングなどの違いがある。
* **ベルマン方程式** ベルマンによって提案された，将来に渡って得られる報酬を定義する式。現在の報酬と次の時刻に得られる報酬に割引率を掛けた値を将来に渡って合算した形である。
* **マガーク効果** 聴覚情報と視覚情報との不一致によって生じる感覚統合における視覚優位を示す現象を指す。被験者に対して，ある音韻を発話している映像と別の音韻の音声を組み合わせて視聴させた場合，第三の音韻が知覚されることが報告される場合がある。ガ（ga）と発話している動画と共に，バ（ba）の音声を同時に提示した場合，「ガ」でも「バ」でもなく「ダ（da）」と聞こえ場合がある。 被検査は，この矛盾を自覚することが難しいとされている。マガーク効果は言語処理が行われる前に，視覚情報処理と聴覚情報処理がなされるためであると説明されている。
* **マルコフ性** 現在の状態が次の時刻の状態に影響を与えることを指す。換言すれば，将来の状態は現在の状態によって定まることを指す。逆言すれば，将来の状態は過去によって定まるのではなく，現在の状態にのみ依存する。未来予測する場合に，過去に起こった全ての出来事は現在の状況に反映されているので，現在の状況だけを考慮すれば良いことを指す。
* **メタ学習 meta learning**: 複数の課題や領域について学習を汎化させる試み 
* **モデルフリー** 強化学習において，規則に基づく意思決定がなされる場合を指す。行動選択の根拠となる規則が正しければ，学習あるいは経験が不要である。
* **モデルベース** 強化学習において，経験則に基づく意思決定がなされる場合を指す。経験に基づく必要があるため最適な行動選択のためには，データ量が要求される。
* **ラバーハンド錯視** 視覚，触覚，および固有受容感覚の 3 者で不一致が生じると触覚において錯覚が生じる現象。被験者の手を隠し，代わりにゴム製の手を被験者から見えるようにし，ゴム製の手と実際の手をブラシで同じ強度，リズム，で刺激することを繰り返す。テスト試行で，ゴム製の手だけをブラシで刺激すると，実際の手にブラシが触れたと報告されることがある。
* **リカレントニューラルネットワーク recurrent neural networks**: 時系列予測，自然言語，音声，制御で用いられるニューラルネットワークの一つ。 入力信号として， 外部入力に加えて， 前時刻の自己状態を入力とする。
* **ワン・アルゴリズム仮説 one algorithm hypothesis**: 脳内では，同一のアルゴリズムが用いられているという仮説。 [@1988Sur] は， 西洋イタチ(フェレット)の新生児に対して外側膝状体 (LGN) の視覚経路を視覚野につなぎ替える実験などを通して，考えられるようになった。
* **一撃学習, ゼロ撃学習, 少数学習 one/zero/few shot(s) learning**: 少数事例で学習を成立させる仕組み，または試みのこと。  
* **二重 Q 学習** Q 関数は得られる報酬を最大化するために用いられる。このとき Q を更新するために，Q 自身の評価が入っている。このことは Q の評価を行う際に，自分自身の値が入ってしまっていることを避ける目的で，Q 関数を 2 つ用意することが行われる。このことを **二重 Q 学習** double Q learning と呼ぶ。
* **二重フラッシュ錯視** 視覚情報処理が聴覚情報によって影響を受ける現象の一つ。通常の視覚優位効果とは逆と言える。視覚対象 (実験では，黒いディスプレイを背景とした白丸) が 1 回点滅する間に，音声情報 (ビープ音) を複数回同時提示すると，被験者はビープ音の回数だけ点滅しているとの知覚が報告される。
* **交差エントロピー cross entropy**: 
* **交差検証 (k-hold, leave-one-out) cross validation**:
* **価値関数** 強化学習において，動作主 (エージェント) が評価する値を与える関数。付与される価値が大きいほど，その行動が選択されやすくなる。
* **割引率** 強化学習において，将来の報酬に対して適用される減衰係数である。しばしば $\gamma$ (ガンマ) と表記され，$t=0$ のときは $\gamma^{0}=1$ である。1 時刻先では $\gamma^{1}$ となり n 時刻先では $\gamma^{n}$ などと表記される。$0\le\gamma\le1$ の範囲である。このため，$\gamma=0$ であれば，即時報酬のみが考慮され，将来に報酬が得られることが予想されたとしても考慮されない。一方 $\gamma\neq1$ であれば，即時報酬と将来得られる報酬との重みが同等となる。このため，即時に報酬が得られなくとも将来的に得られる報酬が相対的に重要視されることとなる。
* **勾配消失問題 gradient descent problem**: 多層ニューラルネットワークにおいて，上位層から誤差を逆伝播して学習させる際に，活性化関数の微分によってはその値が 0 に近づくことを指す。 勾配消失問題を解消することが， 多層化への障害となっていた。 現在では整流線形化関数を用いるなどして，この問題を回避する。畳み込みを用いる
* **半教師あり学習 semi-supervised learning**: 部分的に教師信号が与えられない場合の学習を言う。 正解データが与えられている場合でも，意図的に正解データを隠蔽して用いる場合もある。 こうすることによって，中間表現，潜在変数の表現を豊富にできる場合がある。 変分自己符号化器 VAE など半教師あり学習に該当する。
* **古典的条件づけ** 無条件刺激 (無関連な刺激) と条件刺激 (生体にとって好ましい刺激)  とが随伴して生起することで行動変容が起こることを指す概念。イアン・パブロフによって提唱された。
* **報酬** 強化学習において，動作主が受け取る利得。動物では餌，人間では金銭や名誉などである。強化学習では，将来に渡る報酬を最大化することが目的関数となる。
* **完全結合層 fully connected layers**: ニューラルネットワークに認識，識別を行う場合の最終層において，下位層からの情報全てが結合している層を指す。一方，畳み込み層は部分結合である。
* **対比予測符号化 contrastive predictive coding**: 自己回帰モデルを用いて潜在空間の予測を行う自己教師付きの表現を学習するモデル。 このモデルは将来のサンプルを予測するのに最大限役立つ情報を潜在空間に誘導する確率的な対比損失を用いる。
* **強化学習** アルファ碁やアタリのボードゲームなどを解くことで注目された枠組み，または理論。経済学，ゲーム理論，学習心理学などを背景として成立した。動作主 (エージェント) と呼ばれる主体が，環境を探索し，相互作用することで行動を変容させ，報酬を最大化するように振る舞うようプログラムされる。神経科学における脳内対応物についての研究などから，行動異常との関連が指摘され，精神医学的症状の計算モデルとして提案される場合がある。
* **強化学習**: 教師信号として報酬をとり，報酬を最大化するモデルの総称。囲碁やテレビゲーム，ロボット制御，ドローン，自動運転などに応用されている。reinforcement learning
* **微調整** 深層学習においては，事前訓練済のモデルに対して，標的とする課題に対して学習させる際に，全パラメータにわたる更新を行うことを指す。fine tuning
* **探索と実用のジレンマ** 過去の経験から報酬を最大にする行動を選ぶ実用 (「活用」と訳す場合もある) と，その実用によって選択されるべき行動を捨てて，新たな行動を探索する方が将来的に獲得される報酬が大きい場合もある。この行動を探索と呼ぶ。これら探索と実用という 2 つ行動の選択において葛藤が生じるため，ジレンマと称される。Exploration and exploitation dilemma 
* **損失関数 (誤差関数, 目的関数) loss function, error function, objective function**: 学習目標として設定される量，あるいはその関数。損失， 誤差， 目標 と言い方に變動があるが， 同じ意味で用いられる場合もある。 特に区別するという注意が無い限り， 同じ概念を表すと考えて良い場合が多い。 ニューラルネットワークや機械学習においてモデルのパラメータを調整するときに用いられる，最適化 (最小,最大) するための関数。 loss function,  目的関数 objective function，誤差関数 error function と区別せずに用いられることも多い。 畳み込みとは，カーネルと呼ばれるパラメータの組を入力データについて掛け合わせて総和を計算したもの。
* **教師あり学習 supervised learning**: 入力データと教師データとが対になったデータを用いて，与えられた入力データを正しい教師データを出力するように学習する枠組のこと。
* **教師なし学習 unsupervised learning**: 入力データに対して， 正解データ， すなわち教師信号が与えれていない場合の学習を指す。 教師なし学習では， 入力データの統計的性質を学習することになる。
* **方針 (ポリシー)** 強化学習において，ある状況に対して，特定の行動を起こす傾向のこと。方針によって Q が異なる。強化学習の文脈では，方針はギリシャアルファベット $\pi$ で表記される場合が多い (このため，本授業でも一貫して $\pi$ と表記した)。方針 $\pi$ に基づく Q 関数を $Q_{\pi}(s,a)$ のように表記することがある。
* **最終直下層 penultimate layers**: 転移学習においては， 最終直下層には豊富な情報が含まれていることから，転移学習では重視される。
* **最適化手法 optimization methods**: ニューラルネットワークや機械学習においてモデルのパラメータを最適化 (最小, 最大) するための関数。 loss function,  目的関数 objective function，誤差関数 error function と区別せずに用いられることも多い。
* **正則化 (L1, L2, エラスティック) regularization**:
* **残差ネット ResNet**: 2015 年の ImageNet コンテストで人間の性能を超えたことで話題となったモデル。スキップ結合， バッチ正則化， などを特徴とする
* **決闘 (ドュエリング) ネットワーク** アドバンテージを計算するために，Q 関数と 価値関数とを別々に分岐させたネットワークで算出し，各出力の差からアドバンテージを求めるように設計されたネットワーク。
* **注意 attention**: 画像の注目部位，言語翻訳モデルに使われる機構。言語処理では，マルチヘッド注意という， 同時に複数の注意を持つトランスフォーマーが採用されている。
* **活性化関数 activation functions**: ニューラルネットワークにおいて，入力値を出力値へ変換するために用いられる。整流線形化関数 ReLU， ハイパータンジェント， シグモイドロジスティック関数などがある。 
* **環境** 強化学習において，動作主と相互作用する世界を指す。動作主は環境に働きかけて，報酬を得る。環境は動作主の行動を受けて，環境自身の状態を偏移させ，かつ，動作主に報酬を与える。
* **畳み込みニューラルネットワーク**: 主に画像処理で用いられるディープラーニングの標準的なネットワーク。層ごとに， 畳み込み演算を行う。畳み込みとは，カーネルと呼ばれるパラメータの組を入力データについて掛け合わせて総和を計算したもの。
* **相互活性化モデル** 入力情報と中間段階，出力情報との間に相互作用を仮定するモデル。
* **神経心理学** 脳の障害によって生じる種々の認知機能の変化から，脳の機構，機能，役割を考察する心理学の一分野。言語，思考，記憶，意欲，行為などの障害が生じる機構を解明することを目指す。表出する障害によって，失語症，注意障害，物体失認，無視，失行，などの症状に分類される。
* **結合係数 weights, connections, or weight connections とも**。 ニューラルネットワークにおいて，ニューロン間を結びつける重みのこと。 通常，実数として扱われる。 複素数の場合もある。
* **絵画命名課題** 認知心理学，神経心理学などで用いられる検査または課題の名称。被検査者に対して，刺激図版 (近年では電子化された図版をディスプレイに提示する場合もある) を提示し，その刺激の視覚情報に基づく判断を求める。失語症患者の中には，視覚的な誤りの他，意味的な誤り，あるいは単語の音や綴りに類似した誤りを表出する場合があるため，言語処理の神経機構を推定することが期待される。
* **蒸留 distillation**: より小さなモデルに知識を転移する転移学習に用いる手法のこと。 エッジ実装の際より小さく軽量のモデルが求められることが必要な技術である。
* **誤差逆伝播法 error back-propagation**: ニューラルネットワークに限らず，目的とする関数の最小値 (または最大値) を求めるために用いられる手法。 合成関数の微分を用いてパラメータを調整する。
* **責任割当問題 credit assignment problems**:
* **転移学習 transfer learning**: 学習済のモデルを別の課題に対して適用する再学習の試み。最終層と最終直下層との間の結合係数のみを学習させる場合を指す場合もある。 このときには ファインチューニングの反対語となる。 解くべき課題が類似していれば学習時間が短縮される。
* **転移学習** 深層学習においては，事前訓練済のモデルに対して，標的とする課題に対して学習させる際に，最上位層である全結合層，あるいは，最終直下層付近のパラメータのみを更新し，それより下層のパラメータは凍結させることを指す。transfer learning 
* **領域分割 semantic, object, instance segmentations**: 画像の領域分割の手法。セマンティック，オブジェクト，インスタンス分離，などが挙げられる。
