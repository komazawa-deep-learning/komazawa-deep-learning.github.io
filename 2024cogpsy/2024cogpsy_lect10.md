---
title: "第10回 2024年度開講 駒澤大学 認知心理学研究"
author: "浅川 伸一"
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="right">
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 29/Nov/2024<br/>
Appache 2.0 license<br/>
</div>

$$
\newcommand{\of}[1]{\left(#1\right)}
\newcommand{\Of}[1]{\left[#1\right]}
\newcommand{\KL}[2]{\operatorname{KL}\left(\left.{#1}\right\|{#2}\right)}
\newcommand{\given}[1]{\left|{#1}\right.}
\newcommand{\mb}[1]{\mathbf{#1}}
$$

# 先週の復習

* 畳み込みニューラルネットワーク，ResNet によるスキップ結合，
* 畳み込みニューラルネットワークについては，カーネルサイズ，ストライド，パディング，ダイアレーション(未言及)，
* HMax 最大値プーリング，最大値プーリングが行われなくなった理由としては，画像切り分けの際に不利になるからという理由が考えられる。
* ドロップアウト (未言及)
* バッチ正規化 (未言及)
* データ拡張 (未言及)

# 本日のメニュー

* 転移学習，微調整
* ViT 視覚 Transformer ([Dosovitskiy+2020](https://arXiv.org/abs/2010.11929/))

## [ViT 2020Dosovitskiy AN IMAGE IS WORTH 16X16 WORDS: TRANSFORMERS FOR IMAGE RECOGNITION AT SCALE](https://arxiv.org/abs/2010.11929/)

### 3. 方法<!--3 METHOD-->

モデル設計において，我々はオリジナルのTransformer（Vaswani+2017）に可能な限り忠実に従う。
この意図的にシンプルなセットアップの利点は，スケーラブルなNLP Transformerアーキテクチャとその効率的な実装が，ほぼそのまま使えることである。
<!-- In model design we follow the original Transformer (Vaswani+2017) as closely as possible.
An advantage of this intentionally simple setup is that scalable NLP Transformer architectures – and their efficient implementations – can be used almost out of the box. -->

#### 3.1 VISION TRANSFORMER (VIT)

モデルの概要を図 1 に示す。
標準的な Transformer はトークン埋込みの 1 次元系列を入力として受け取る。
2 次元画像を扱うために，画像 $x\in\mathcal{R}^{H\times W\times C}$ を平坦化された 2 次元パッチの系列 $x_{p}$ に再形成する。
(H,W) は原画像の解像度，C はチャンネル数，(P,P) は各画像パッチの解像度，$N=HW/P^{2}$ は結果のパッチ数であり，これは Transformer の有効入力系列長でもある。
Transformer は全ての層で一定の潜在ベクトルサイズ D を用いるので，パッチを平坦化し，訓練可能な線形射影（式 1）を用いて D 次元に写像する。
この射影の出力をパッチ埋め込みと呼ぶ。
<!-- An overview of the model is depicted in Figure 1.
The standard Transformer receives as input a 1D sequence of token embeddings.
To handle 2D images, we reshape the image $x\in\mathcal{R}^{H\times W\times C}$ into a sequence of flattened 2D patches $x_{p}\in\mathcal{R}^{N\times(P^{2}\cdot C)}$, where (H,W) is the resolution of the original
image, C is the number of channels, (P,P) is the resolution of each image patch, and $N=HW/P^{2}$ is the resulting number of patches, which also serves as the effective input sequence length for the Transformer.
The Transformer uses constant latent vector size D through all of its layers, so we flatten the patches and map to D dimensions with a trainable linear projection (Eq. 1).
We refer to the output of this projection as the patch embeddings. -->

<div class="figcenter">
<img src="/2024assets/2020Dosovitskiy_ViT_fig1.svg" style="width:66%;">
</div>
<div class="figcaption" style="width:77%;">

**図 1：モデルの概要**<br/>
画像を固定サイズのパッチに分割し，それぞれを線形に埋め込み，位置埋め込みを追加し，得られたベクトル列を標準的な Transformer 符号化器に与える。
分類を行うために，学習可能な 「分類トークン 」を系列に追加するという標準的なアプローチを用いる。
Transformer 符号化器の図は，Vaswani+(2017) に触発された。
<!-- Figure 1: Model overview.
We split an image into fixed-size patches, linearly embed each of them, add position embeddings, and feed the resulting sequence of vectors to a standard Transformer encoder.
In order to perform classification, we use the standard approach of adding an extra learnable “classification token” to the sequence.
The illustration of the Transformer encoder was inspired by Vaswani+(2017). -->
</div>

BERT の `[class]` トークンと同様に，学習可能な埋め込みを埋め込みパッチのシーケンス($z_0^0=x_{text{class}}$) の前に付加し，Transformer エンコーダの出力 ($z_{L}^{0}$) の状態が画像表現yとなる（式 4）。
事前学習時と微調整時の両方で，分類ヘッドが $z^{0}_{L}$ に取り付けられる。
分類ヘッドは，事前学習時には 1 つの隠れ層を持つ MLP によって実装され，微調整時には 1 つの線形層によって実装される。
<!-- Similar to BERT’s `[class]` token, we prepend a learnable embedding to the sequence of embedded patches ($z_0^0=x_{\text{class}}$), whose state at the output of the Transformer encoder ($z_{L}^{0}$) serves as the
image representation y (Eq. 4).
Both during pre-training and fine-tuning, a classification head is attached to $z^{0}_{L}$.
The classification head is implemented by a MLP with one hidden layer at pre-training time and by a single linear layer at fine-tuning time. -->

位置埋め込みは位置情報を保持するためにパッチ埋め込みに追加される。
我々は標準的な学習可能な 1 次元の位置埋め込みを使用する (付録 D.3)。
結果として得られる埋め込みベクトルの系列スは符号化器の入力となる。
Transformer 符号化器 (Vaswani+2017) は，多頭自己注意 (MSA 付録 A) と MLP ブロックの交互の層で構成される (式 2, 3)。
各ブロックの前には層正規化 (LN) が適用され，各ブロックの後には残差接続が適用される (Wang+2019, Baevski&Auli2019)。
MLP には GELU 非線形性を持つ 2 つの層が含まれる。
<!-- Position embeddings are added to the patch embeddings to retain positional information.
We use standard learnable 1D position embeddings, since we have not observed significant performance gains from using more advanced 2D-aware position embeddings (Appendix D.3).
The resulting sequence of embedding vectors serves as input to the encoder.
The Transformer encoder (Vaswani+2017) consists of alternating layers of multiheaded selfattention (MSA, see Appendix A) and MLP blocks (Eq. 2, 3).
Layer-norm (LN) is applied before every block, and residual connections after every block (Wang+2019, Baevski&Auli2019).
The MLP contains two layers with a GELU non-linearity. -->

$$\tag{1}
z_0 = \left[x_{\text{class}}; x_{p}^{1}\mathbf{E};x_{p}^{2}\mathbf{E};\ldots;x_{p}^{N}\mathbf{E}\right]+\mathbf{E}_{pos},
$$
where, $\mathbf{E}\in\mathcal{R}^{(p^{2}\cdot C)}$, and $\mathbf{E}_{pos}\in\mathcal{R}^{(N+1)\times D}$

$$\tag{2}
\mathcal{z}^{\top}_{\ell}= \text{MSA}\left(LN\left(\mathbf{z}_{\ell-1}\right)\right)+\mathbf{z}_{\ell-1},
$$
where $\ell=1\ldots,L$

$$\tag{3}
\mathbf{z}_{\ell}=\text{MLP}\left(LN\left(\mathbf{z}^{\top}_{\ell}\right)\right)+\mathbf{z}^{\top}_{\ell},
$$
where $\ell=1,\ldots,L$

$$\tag{4}
\mathbf{y}=LN\left( \mathbf{z}_{L}^{0}\right),
$$

**ハイブリッド・アーキテクチャ**<!-- **Hybrid Architecture**.-->
生の画像パッチの代わりに，入力系列を CNN の特徴地図から形成することができる (LeCun+1989)。
このハイブリッド・モデルでは，パッチ埋め込み射影 E (式 1) が CNN 特徴地図から抽出されたパッチに適用される。
特殊なケースとして，パッチは空間サイズ 1x1 を持つことができ，これは入力系列が単に特徴地図の空間次元を平坦化し，Transformer 次元に射影することによって得られることを意味する。
分類入力埋め込みと位置埋め込みは上述のように追加される。
<!--As an alternative to raw image patches, the input sequence can be formed from feature maps of a CNN (LeCun+1989).
In this hybrid model, the patch embedding projection E (Eq. 1) is applied to patches extracted from a CNN feature map.
As a special case, the patches can have spatial size 1x1, which means that the input sequence is obtained by simply flattening the spatial dimensions of the feature map and projecting to the Transformer dimension.
The classification input embedding and position embeddings are added as described above. -->

#### 3.2 微調整と高解像度化<!-- #### 3.2 FINE-TUNING AND HIGHER RESOLUTION-->

通常，ViT を大規模なデータセットで事前学習し，(より小規模な) 下流課題に対して微調整を行う。
このために，事前訓練された予測ヘッドを取り除き，ゼロ初期化された DxK フィードフォワード層を追加する。
事前学習よりも高い解像度で微調整を行うことが有益な場合が多い (Touvron+2019, Kolesnikov+2020)。
より高い解像度の画像を与える場合，パッチサイズを同じにすることで，有効系列長が大きくなる。
Vision Transformer は任意の系列長（メモリ制約まで）を扱うことができるが，事前に学習された位置埋め込みはもはや意味をなさないかもしれない。
そこで我々は，事前に学習された位置埋め込みを，元画像の位置に応じて 2 次元補間する。
この解像度調整とパッチ抽出は，画像の 2 次元構造に関する帰納的バイアスが Vision Transformer に手動で注入される唯一の点であることに注意してください。
<!--Typically, we pre-train ViT on large datasets, and fine-tune to (smaller) downstream tasks.
For this, we remove the pre-trained prediction head and attach a zero-initialized DxK feedforward layer, where K is the number of downstream classes.
It is often beneficial to fine-tune at higher resolution than pre-training (Touvron+2019, Kolesnikov+2020).
When feeding images of higher resolution, we keep the patch size the same, which results in a larger effective sequence length.
The Vision Transformer can handle arbitrary sequence lengths (up to memory constraints), however, the pre-trained position embeddings may no longer be meaningful.
We therefore perform 2D interpolation of the pre-trained position embeddings, according to their location in the original image.
Note that this resolution adjustment and patch extraction are the only points at which an inductive bias about the 2D structure of the images is manually injected into the Vision Transformer. -->

### 4. 実験<!-- ### 4 EXPERIMENTS-->

ResNet, Vision Transformer (ViT)，ハイブリッドの表現学習能力を評価する。
各モデルのデータ要件を理解するために，様々なサイズのデータセットで事前学習を行い，多くのベンチマーク課題を評価する。
モデルを事前学習する計算コストを考慮すると，ViT は非常に有利な性能を示し，より低い事前学習コストで，ほとんどの認識ベンチマークで最先端技術を達成した。
最後に，自己教師あり学習を用いた小規模な実験を行い，自己教師付き学習 ViT が将来有望であることを示す。
<!--We evaluate the representation learning capabilities of ResNet, Vision Transformer (ViT), and the hybrid.
To understand the data requirements of each model, we pre-train on datasets of varying size and evaluate many benchmark tasks.
When considering the computational cost of pre-training the model, ViT performs very favourably, attaining state of the art on most recognition benchmarks at a lower pre-training cost.
Lastly, we perform a small experiment using self-supervision, and show that self-supervised ViT holds promise for the future. -->

#### 4.1 セットアップ<!-- #### 4.1 SETUP-->

**データセット:**<!--**Datasets.**-->
モデルのスケーラビリティを調べるために，1k クラスと 1.3M 画像を持つ ILSVRC-2012 ImageNet データセット (以下 ImageNet と呼ぶ)，21k クラスと 14M 画像を持つそのスーパーセット ImageNet-21k (Deng+2009)，18k クラスと 303M 高解像度画像を持つ JFT (Sun+2017) を用いる。
Kolesnikov+(2020) に従い，下流課題のテストセットに対して事前学習データセットの重複を排除する。
これらのデータセットで学習したモデルをいくつかのベンチマークタスクに移植する： オリジナルの検証ラベルとクリーンアップされた ReaL ラベルの ImageNet (Beyer+2020)，CIFAR-10/100 (Krizhevsky2009)，Oxford-IIIT Pets (Parkhi+2012)，Oxford Flowers-102  (Nilsback&Zisserman2008)。
これらのデータセットの前処理は Kolesnikov+(2020) に従う。
<!--To explore model scalability, we use the ILSVRC-2012 ImageNet dataset with 1k classes and 1.3M images (we refer to it as ImageNet in what follows), its superset ImageNet-21k with 21k classes and 14M images (Deng+2009), and JFT (Sun+2017) with 18k classes and 303M high-resolution images.
We de-duplicate the pre-training datasets w.r.t. the test sets of the downstream tasks following Kolesnikov+(2020).
We transfer the models trained on these dataset to several benchmark tasks: ImageNet on the original validation labels and the cleaned-up ReaL labels (Beyer+2020), CIFAR-10/100 (Krizhevsky2009), Oxford-IIIT Pets (Parkhi+2012), and Oxford Flowers-102 (Nilsback&Zisserman2008).
For these datasets, pre-processing follows Kolesnikov+(2020). -->

また，19 課題の VTAB 分類スイート (Zhai+2019b) でも評価する。
VTAB は，1 課題あたり 1,000 の学習例を用いて，多様な課題への低データ転移を評価する。
課題は 3 群に分けられる：
* 自然 - 上記のような課題，PET，CIFARなど。
* 専門 - 医療や衛星画像。
* 構造化課題 - 局在化のような幾何学的理解を必要とする課題。
<!-- We also evaluate on the 19-task VTAB classification suite (Zhai+2019b).
VTAB evaluates low-data transfer to diverse tasks, using 1,000 training examples per task.
The tasks are divided into three groups:
* Natural – tasks like the above, Pets, CIFAR, etc.
* Specialized – medical and satellite imagery, and
* Structured – tasks that require geometric understanding like localization. -->

**モデルの変種:**<!-- **Model Variants.**-->
表 1 にまとめたように，BERT（Devlin+2019）で使用されたものを ViT 構成のベースとしている。
Base モデルと Large モデルは BERT からそのまま採用し，より大きなHuge モデルを追加した。
以下では，モデルサイズと入力パッチサイズを示すために簡潔な表記を使用します：例えば，ViT-L/16 は 16x16 入力パッチサイズの Large バリアントを意味する。
Transformer の系列長はパッチサイズの 2 乗に反比例するので，パッチサイズの小さいモデルは計算コストが高くなることに注意。
<!--We base ViT configurations on those used for BERT (Devlin+2019), as summarized in Table 1.
The "Base" and "Large" models are directly adopted from BERT and we add the larger "Huge" model.
In what follows we use brief notation to indicate the model size and the input patch size: for instance, ViT-L/16 means the "Large" variant with 16x16 input patch size.
Note that the Transformer’s sequence length is inversely proportional to the square of the patch size, thus models with smaller patch size are computationally more expensive. -->

<div class="figcenter">
<img src="/2024assets/2020Dosovitskiy_ViT_tab1and2.svg" style="width:66%;">
</div><div class="figcaption" style="width:77%;">

**表 2：一般的な画像分類ベンチマークにおける最新技術との比較**<br/>
精度の平均と標準偏差を3回の微調整の平均値で示す。
JFT-300M データセットで事前訓練された Vision Transformer モデルは，すべてのデータセットで ResNet ベースのベースラインを上回った。
より小さなパブリック ImageNet-21k データセットで事前に訓練された ViT も良好な結果を示した。
Touvron+(2020) で報告された 88.5% の結果をわずかに改善。
<!-- Table 2: Comparison with state of the art on popular image classification benchmarks.
We report mean and standard deviation of the accuracies, averaged over three fine-tuning runs.
Vision Transformer models pre-trained on the JFT-300M dataset outperform ResNet-based baselines on all datasets, while taking substantially less computational resources to pre-train.
ViT pre-trained on the smaller public ImageNet-21k dataset performs well too.
Slightly improved 88:5% result reported in Touvron+(2020). -->
</div>

ベースライン CNN には ResNet (He+2016) を用いるが，バッチ正規化層 (Ioffe&Szegedy2015) を群正規化 (Wu&He2018) に置き換え，標準化畳み込み (Salimans&Kingma2016) を用いる。
これらの修正により伝達が改善され (Kolesnikov+2020)，この修正モデルを ResNet (BiT) と呼ぶ。
ハイブリッドの場合，中間特徴地図を 1 画素のパッチサイズで ViT に送り込む。
異なる系列長を実験するために，(i) 通常の ResNet50 のステージ 4 の出力を取るか，(ii) ステージ 4 を取り除き，同じ数の層をステージ 3 に配置し (層の総数を維持する），この拡張ステージ 3 の出力を取る。
オプション (ii) の場合，系列の長さが 4 倍長くなり，ViT モデルのコストが高くなる。
<!-- For the baseline CNNs, we use ResNet (He+2016), but replace the Batch Normalization layers (Ioffe&Szegedy2015) with Group Normalization (Wu&He2018), and used standardized convolutions (Salimans&Kingma2016).
These modifications improve transfer (Kolesnikov+2020), and we denote the modified model “ResNet (BiT)”.
For the hybrids, we feed the intermediate feature maps into ViT with patch size of one "pixel".
To experiment with different sequence lengths, we either (i) take the output of stage 4 of a regular ResNet50 or (ii) remove stage 4, place the same number of layers in stage 3 (keeping the total number of layers), and take the output of this extended stage 3.
Option (ii) results in a 4x longer sequence length, and a more expensive ViT model. -->

**学習と微調整:**<!-- **Training & Fine-tuning.**-->
ResNets を含む全てのモデルを，$\beta_1=0.9$, $\beta_2=0.999$，バッチサイズ 4096，重み減衰 0.1 の Adam で学習した。
我々は，線形学習率のウォームアップと減衰を使用する。
詳細については付録 B.1.1 を参照。
微調整のために，すべてのモデルでモメンタム付き SGD，バッチサイズ 512 を使用した。
表 2 の ImageNet の結果については，より高い解像度で微調整を行った：
ViT-L/16 では 512，ViT-H/14 では 518，また Polyak&Juditsky(1992) の係数 0.9999 を用いた平均化も行った (Ramachandran+2019, Wang+2020b)。
<!--We train all models, including ResNets, using Adam with  $\beta_1=0.9$, $\beta_2=0.999$, a batch size of 4096 and apply a high weight decay of 0.1, which we found to be useful for transfer of all models (Appendix D.1 shows that, in contrast to common practices, Adam works slightly better than SGD for ResNets in our setting).
We use a linear learning rate warmup and decay, see Appendix B.1 for details.
For fine-tuning we use SGD with momentum, batch size 512, for all models, see Appendix B.1.1.
For ImageNet results in Table 2, we fine-tuned at higher resolution:
512 for ViT-L/16 and 518 for ViT-H/14, and also used Polyak&Juditsky(1992) averaging with a factor of 0.9999 (Ramachandran+2019, Wang+2020b). -->

**計量:**<!-- **Metrics.**-->
下流課題データセットの結果は，少数撃精度または微調整精度によって報告される。
微調整精度は，それぞれのデータセットで微調整した後の各モデルの性能を捉える。
少数撃精度は，訓練画像の部分集合の（凍結）表現を ${-1,1}$ の標的ベクトルに写像する正則化線形回帰問題を解くことによって得られる。
我々は主に性能の微調整に重点を置いているが，微調整にコストがかかりすぎる場合，その場で高速に評価するために線形少数撃精度を使用することもある。
<!--We report results on downstream datasets either through few-shot or fine-tuning accuracy.
Fine-tuning accuracies capture the performance of each model after fine-tuning it on the respective dataset.
Few-shot accuracies are obtained by solving a regularized linear regression problem that maps the (frozen) representation of a subset of training images to $\{-1,1\}$ target vectors.
Though we mainly focus on fine-tuning performance, we sometimes use linear few-shot accuracies for fast on-the-fly evaluation where fine-tuning would be too costly. -->

<div class="figcenter">
<img src="/2024assets/2020Dosovitskiy_ViT_fig2-3-4.svg" style="width:77%;">
</div><div class="figcaption" style="width:77%;">

**図 3：ImageNet への転移学習**<br/>
小さなデータセットで事前訓練した場合，大きな ViT モデルは BiT ResNets (斜線部分) よりも性能が劣るが，大きなデータセットで事前訓練した場合は輝く。
同様に，データセットが大きくなるにつれて，大きな ViT モデルは小さな ViT モデルを追い越す。

**図 4：ImageNet における事前訓練サイズに対する線形少数撃学習の評価**<br/>
ResNets は事前学習データセットが小さいほど良い性能を示すが，事前学習が大きいほど良い性能を示す ViT よりも早くプラトーする。
ViT-b はすべての隠れ次元を半分にした ViT-B である。
<!-- Figure 3: Transfer to ImageNet.
While large ViT models perform worse than BiT ResNets (shaded area) when pre-trained on small datasets, they shine when pre-trained on larger datasets.
Similarly, larger ViT variants overtake smaller ones as the dataset grows.

Figure 4: Linear few-shot evaluation on ImageNet versus pre-training size.
ResNets perform better with smaller pre-training datasets but plateau sooner than ViT, which performs better with larger pre-training.
ViT-b is ViT-B with all hidden dimensions halved. -->
</div>

# 視覚モデルの歴史

人間の視覚処理のモデリングは，Hubel&Wiesel にさかのぼることができる。
Hubel&Wiesel では，視覚野 V1 の単純な細胞の応答特性はエッジの特徴検出として形式化され，複雑な細胞の特性は視野上で空間的に繰り返される一連の操作として概念化された（Hubel&Wiesel1962，translationaly invariant 並進不変）。
この計算原理は，コンピュータビジョンに霊長類の視覚系の特性を取り入れる試みとして Neocognitron（Fukushima1980）に取り入れられた。
さらに HMAX モデルファミリー（Riesenhuber&Poggio1999, Serre+2007）にも影響を与えた。
これらは，今日の特徴検出器とプーリング演算子を交互に用いた物体認識の深層学習モデルとして用いられれている。
(ただし，画像切り分けでは，プーリングを除外する傾向にある。)
AlexNet (Russakovsky+2015) 以前は，ネットワークをどのように組み込むか，あるいは他の方法で訓練するか，明確ではなかった（Olshausen&Field1996, Lowe1999, Torralba&Oliva2003）。
深層ニューラルネットワークを訓練する少なくとも 1 つの方法が示された。
同時に，このような不変

ImageNet 画像認識コンテストで優勝したモデルでは，視覚野 V4 と IT のニューロンの応答を圧倒的によくモデル化した内部「神経」表現を生成することが実証された（Yamins+2013, Cadieu+2014, Yamins+2014）。
ヒトの fMRI や MEG といった，より高度な実験レベルでの説明力の向上が確認された（Khaligh-Razavi&Kriegeskorte2014, Güçlü&van Gerven2015, Cichy+2016）。
<!-- Modeling human visual processing traces back at least to Hubel and Wiesel where response properties of simple cells in visual area V1 were formalized as feature detection of edges and properties of complex cells were conceptualized as a set of operations that were spatially repeated over the visual field (Hubel&Wiesel1962, i.e., translationally invariant).
These computational principles inspired the first models of object recognition, most notably, the Neocognitron (Fukushima1980) and the HMAX model family (Riesenhuber&Poggio1999; Serre+2007), where feature detectors and pooling operators were used in turns to build deep hierarchical models of object recognition.
However, such models lacked robust feature representations as it was not clear at the time how to either build in or otherwise train these networks to learn their spatially-repeated operations from input statistics – particularly for areas beyond visual area V1 (Olshausen&Field1996, Lowe1999, Torralba&Oliva2003).
These issues were first addressed by the AlexNet ANN (Krizhevsky+2012) in that it demonstrated at least one way to train a deep neural network for a large-scale invariant object recognition task (Russakovsky+2015).
Concurrently, deep networks optimized for such invariant object recognition tasks were demonstrated to produce internal "neural" representations that were by far the best models of the responses of neurons in non-human primate visual areas V4 and IT (Yamins+2013, Cadieu+2014, Yamins+2014).
Later work in humans confirmed these gains in explanatory power at the courser experimental level of fMRI and MEG (Khaligh-Razavi&Kriegeskorte2014; Güçlü&van_Gerven2015, Cichy+2016), with detailed measures of behavioral response patterns in both humans and non-human primates (e.g., Rajalingham+2015, Kubilius+2016, Rajalingham+2018), and with non-human primate neural spiking measures from the cortical area V1 (Cadena+2017). -->

#  畳み込みニューラルネットワークの基礎


<div class="figcenter">
<img src="/2024assets/2020Spoerer_fig1.svg" style="width:66%;">
<div class="figcaption">

<font style="font-weight:bold">図 1. パラメータを一致させたネットワークの模式図</font><br/>
白箱は畳み込み層を表し，幅は畳み込み層の空間次元，高さは特徴地図数を表す。
モデル:<br/>
<font style="font-weight:bold">(1)</font> 畳み込みカーネル (B-K) のサイズを大きくすることで，パラメータ数を一致させたモデル <br/>
<font style="font-weight:bold">(2)</font> 特徴地図の数を一致させたモデル (B-F)，<br/>
<font style="font-weight:bold">(3)</font> ネットワークの深さを一致させたモデル (B-D)<br/>
例となる素子 (黒点) は，入力カーネル (B-K では幅が異なる) を表す色つきの領域にリンクされている。
範囲は例示的なもので，縮尺通りに描かれていない。

[Spoerer+2020 Fig.1](https://doi.org/10.1371/journal.pcbi.1008215)
<!-- Fig 1. Schematic representation of the parameter-matched networks.
White boxes represent convolutional layers, with the width representing the spatial dimensions of the convolut
ional layers and the height representing the number of feature maps.
Models were matched in the number of parameters by increasing (1) the size of the convolutional kernels (B-K),
 (2) the number of feature maps (B-F), and (3) the depth of the network (B-D).
Example units (black dots) are linked to coloured regions representing their input kernels (which differ in wi
dth in B-K).
The extents are illustrative and not drawn to scale. -->
</div></div>

## 本日のメニュー

1. 畳み込みニューラルネットワークの歴史と技法
2. 畳み込みニューラルネットワークの技法
3. 画像切り分け技術
4. トップダウン，ボトムアップ，再帰結合

## 実習ファイル


* [ソフトマックス関数解題 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_1107softmax.ipynb){:target="_blank"}
また，ソフトマックス関数は，エネルギー関数とみなすことも可能である。

* [ニューラルネットワークモデルの定義 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_1028komazawa_neural_networks_primer.ipynb){:target="_blank"}
* [3 層パーセプトロンと確率的勾配降下法のデモ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/2015corona/blob/master/2021notebooks/2021_0521mlp_Adam_SGD.ipynb){:target="_blank"}
<!-- * [ccap 資料初心者のためのニューラルネットワーク <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/project-ccap/project-ccap.github.io/blob/master/2022notebooks/2022_0418ccap_neural_networks_for_primer.ipynb){:target="_blank"}
* [画像認識 PyTorch の基礎編 AlexNet <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2020_0515komazawa_step_by_step_CNN_Pytorch.ipynb){:target="_blank"} -->


<!-- * [[Karapetian+(2023)](https://direct.mit.edu/jocn/article/35/11/1879/117201/Empirically-Identifying-and-Computationally) <img src="/assets/colab_icon.svg"> ](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_115Karapetian_demo.ipynb) -->
* [ResNet 実習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_0603ResNet_with_Olivetti_faces_.ipynb){:target="_blank"}

<!-- * [ResNet 実習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_0603ResNet_with_Olivetti_faces_.ipynb) -->
<!-- * [セグメンテーション実習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_0603Image_segmentation_demo.ipynb){:target="_blank"}
* [DETR  <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2022notebooks/2022_0625DETR_demo.ipynb)
* [実装 Bottom-up Top-down model <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2024notebooks/2024_0105royabel_BU_TD_multi_mnist.ipynb){:target="_blank"}-->

* [はじめての colab による画像認識 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021komazawa_cogsy000_CNN_demo.ipynb){:target="_blank"}
* [画像認識 PyTorch の基礎編  <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2020_0515komazawa_step_by_step_CNN_Pytorch.ipynb){:target="_blank"}
* [畳み込み演算の実習と DOG 関数 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_1024convolution_exercise.ipynb){:target="_blank"}
* [CNN 畳み込み層の可視化 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_1024CNN_layer_visualization.ipynb){:target="_blank"}
* [3 層パーセプトロンと確率的勾配降下法のデモ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/2015corona/blob/master/2021notebooks/2021_0521mlp_Adam_SGD.ipynb){:target="_blank"}
* [実習 MLP Adam SGD <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0521mlp_Adam_SGD.ipynb){:target="_blank"}
* [実習 LeNet PyTorch 版 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0528LeNet_pytorch.ipynb){:target="_blank"}
* [実習 3 つの MNIST <img src='/assets/colab_icon.svg'>](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0514komazawa_3mnists.ipynb){:target="_blank"}
* [実習 いくつかの画像フィルタ 特徴点検出アルゴリズム <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2020Sight_visit_feature_extractions_demo.ipynb){:target="_blank"}
* [実習 DOG などのフィルタと Harr 特徴による顔検出 a.k.a ビオラ＝ジョーンズ アルゴリズム <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0528edge_and_face_detection_algorithm_not_cnn.ipynb){:target="_blank"} -->


## 畳込みニューラルネット(CNN)

<div class="figcenter">
<img src='/assets/imagenet_result2017.png' style='width:74%'><br/>
イメージネットコンテストの結果
<!-- 画像認識の進歩 -->
</div>

深層学習 (ディープラーニング) の中で **畳み込みニューラルネットワーク** CNN と呼ばれるニューラルネットワークについて解説する。

最初に画像処理の概略を述べる CNN が，それまで主流であった従来の手法の性能を凌駕したことはすでに述べました。
CNN の特徴の一つに **エンドツーエンド** と呼ばれる考え方があります。
エンドツーエンドとは，従来手法によるパターン認識システムでは，専門家による手の込んだ詳細な作り込みを必要としていたことと異なり，面倒な作り込みをせずとも性能が向上したことを指します。

エンドツーエンドなニューラルネットワークにより，次のことが実現しました。

- ニューラルネットワークの層ごとに，特徴抽出が行われ，抽出された特徴がより高次の層へと伝達される
- ニューラルネットワークの各層では，比較的単純な特徴から次第に複雑な特徴へと段階的に変化する
- 高次層にみられる特徴は低次層の特徴より大域的，普遍的である
- 高次層のニューロンは，低次層で抽出された特徴を共有している

このことを簡単に説明してみます。

我々人間は，外界を認識するために必要な計算を，生物種としての発生の過程と，個人の発達を通しての経験に基づく認識システムを保持していると見ることができます。
従って我々の視覚認識には化石時代に始まる光の受容器としての眼の進化の歴史と発達を通じた個人の視覚経験が反映された結果でもあります。
人工知能の目標は，この複雑な特徴検出過程をどうやったらコンピュータが獲得できるかということでもあります。
外界を認識するために今日まで考案されてきたモデル（例えば，ニューラルネットワークサポートベクターマシンなどは）は複雑です。
ですがモデルを訓練するための学習方法はそれほど難しくありません。
この意味で画像認識課題が正しく動作するためのポイントは，認識システムが問題を解く事が可能なほど複雑であるかどうかではなく，十分に複雑が視覚環境，すなわち画像認識の場合，外部の艦橋を反映するために十分な量の像データを容易すことができるか否かにあります。
今日の CNN による画像認識性能の向上は，簡単な計算方法を用いて複雑な外部環境に適応できる認識システムを構築する方法が確立したからであると言うことが可能です。

下図<!--[fig:2012Ng_01](#fig:2012Ng_01){reference-type="ref"reference="fig:2012Ng_01"} -->に画像処理の例を挙げました。

<center>
<img src="/assets/2012Ng_ML_and_AI_01.png" style="width:66%">
</center>
<!-- 図[[fig:2012Ng_01]](#fig:2012Ng_01){reference-type="ref"reference="fig:2012Ng_01"} -->

<center>
<img src='/assets/2013LeCun-tutorial-icml_15.svg' style="width:66%"><br/>

**LeCun (2013) より**
</center>

## 福島のネオコグニトロン (Fukushima, 1980)

* S 細胞と C 細胞との繰り返し。最初の多層（深層）化された物体認識モデルととらえることが可能
    - S 細胞：生理学の単純細胞 simple cells に対応。受容野 receptive fields の概念を実現。特徴抽出，特徴検出。<br/>
    - C 細胞：複雑細胞 complex cells に対応。広い受容野。位置，回転，拡大縮小の差異を吸収<br>

<div class="figure figcenter">
<img src="/assets/Neocognitron.jpeg" width="55%">
<img src="/assets/Fukushima.jpeg" style="width:24%"><br>
<div class="figcaption">

ネオコグニトロンの模式図
</div></div>

## LeNet5 (LeCun1998)

* **LeNet**. Yann LeCun (現 Facebook AI 研究所所長)による CNN 実装
 [LeNet](http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf){:target="_blank"} 手書き数字認識

<center>
<img src="/assets/1998LeNet5.png" width="84%"><br/>
<div style="text-align:left; width:77%;background-color:cornsilk">

LeNet5 の論文より改変
</div>
</center>

- 畳込層とプーリング層（発表当初はサブサンプリング）との繰り返し
  - 畳込とプーリングは<font color="green">局所結合</font>
- MNIST を用いた１０種類の手書き文字認識
- 最終２層は全結合層をつなげて最終層１０ニューロン，最終層の各ニューロンの出力がそれぞれの数字（０から９までの１０種）に対応する

<center>
<img src="/assets/dmoulin_gif/full_padding_no_strides.gif" style="width:33%">
<img src="/assets/dmoulin_gif/same_padding_no_strides_transposed.gif" style="width:33%"><br/>
<div style="text-align=:left; width:66%; background-color:cornsilk">

左:入力層 5x5青，出力層緑，カーネルサイズ3x3, フルパディング，ストライド=1.<br/>
右:入力層 5x5青，出力層緑，カーネルサイズ3x3, フルパディング，ストライド=1. トランスポーズド畳み込み
</div>
<img src="/assets/dmoulin_gif/numerical_max_pooling.gif" style="width:33%">
<img src="/assets/dmoulin_gif/numerical_average_pooling.gif" style="width:33%"><br/>
<div style="text-align=:left; width:66%; background-color:cornsilk">

左: 最大値プーリング。
右: 平均値プーリング
</div>
<div style="text-align=:left; width:44%; background-color:cornsilk">
Dmoulin and Visin (2020) より
</div>

<img src="/assets/dmoulin_gif/padding_strides.gif" style="width:33%">
<img src="/assets/dmoulin_gif/padding_strides_odd.gif" style="width:33%">
<img src="/assets/dmoulin_gif/padding_strides_odd_transposed.gif" style="width:33%"><br/>
<div style="text-align=:left; width:44%; background-color:cornsilk">

左: padding_strides, 中:padding_strides_odd, 右:padding_stride_transposed
</div>
<img src="/assets/dmoulin_gif/same_padding_no_strides.gif" style="width:33%">
<img src="/assets/dmoulin_gif/same_padding_no_strides_transposed.gif" style="width:33%">
<div style="text-align=:left; width:44%; background-color:cornsilk">

右:same_padding_no_strides, 左: same_padding_no_strides_transposed
</div>
<img src="/assets/dmoulin_gif/arbitrary_padding_no_strides.gif" style="width:33%">
<img src="/assets/dmoulin_gif/arbitrary_padding_no_strides_transposed.gif" style="width:33%">
<div style="text-align=:left; width:44%; background-color:cornsilk">
右:arbitrary padding no strides, 左: artibtrary padding no stride transposed
</div>
</center>

## Riesenhuber&Poggio(1999) HMAX 最大値プーリング

<div class="figcenter">
<img src="/assets/1999Riesenhuber_Poggio_fig2.svg" style="width:49%">
<div class="figcaption" style="width:66%;">

<font style="font-weight:bold">モデルのスケッチ</font><br/>
単純細胞から作られた複雑細胞の古典的なモデルを拡張したもので，線形演算 (福島の表記法では `S` ユニット，テンプレート・マッチング 図中の実線) と非線形演算 (`C`プーリングユニット，最大値 MAX 演算を行う 図中破線) を持つ層の階層で構成。
細胞入力の最大値を選択，その値を用いてセルを駆動する非線形の MAX 演算は複雑細胞に対して，線形入力の合計とは異なりモデルの特性の鍵となる概念である。
この 2 種類の操作は 異なる位置にチューニングされた求心性結合をプールすることでパターン特異性と並進不変性を，また異なるスケールにチューニングされた求心性結合をプールすることで、スケール不変性をもたらした (図示せず)。<br/>
Riesenhuber&Poggio(1999) Fig. 2 より
</div></div>


<div class="figcenter">
<img src="/assets/1999Riesenhuber_Poggio_fig3a.svg" style="width:44%">
<img src="/assets/1999Riesenhuber_Poggio_fig3b.svg" style="width:44%"><br/>
<div class="figcaption" style="width:99%">

MAX 機構 高度に非線形な形状調整の特性。<br/>
「最適」特徴を決定するために考案された「単純化手順」を用いて得られた下側頭葉細胞の応答（選好刺激に対する反応が等しくなるように正規化された反応)。
実験では，もともと細胞は「水のボトル」の画像 (一番左の物体) に非常に強い反応を示した。
その後，刺激を単色の輪郭に単純化したところ，細胞の発火が増加し，さらに，楕円を支える棒からなるパドルのような物体に変化した。
この物体が強い反応を引き起こすのに対し，棒や楕円だけではほとんど反応しなかった。
Riesenhuber&Poggio(1999) Fig 3A.
</div></div>

実験とモデルの比較。
白棒はの実験用ニューロンの反応を示す。
黒と灰色の棒は 選好刺激の 幹-楕円 の基部の遷移に合わせてチューニングしたモデル細胞の反応を示している。
モデル細胞は 直上図に示したモデルを簡略化したもの。
受容野の各位置に 2 種類の S1 特徴があり，それぞれが遷移領域の左側または右側にチューンしていて，その出力が C1 ユニットに入力され MAX 関数 (黒棒) または SUM 関数 (灰色棒) を用いてプールされている。
モデル細胞は 実験ニューロンの 選好刺激が受容野内にあるときに反応が最大になるよう，C1 ユニットに接続されていた。

図 3. MAX 機構の高度に非線形な形状チューニング特性。
(a) `最適` 特徴を決定するために考案された `単純化手続`(26) を用いて得られた，実験的に観察された IT 細胞の応答 (好ましい刺激に対する応答が 1 に等しくなるように正規化された応答)。
実験では，細胞はもともと「水瓶」 (一番左の物体) の画像にかなり強く反応した。
その後，刺激は単色の輪郭に「単純化」され，細胞の発火が増加し，さらに楕円を支える棒からなるパドルのような物体に変化した。
この物体は強い反応を引き起こしたが，棒や楕円だけではほとんど全く反応を起こさなかった (図は許可を得て使用)。
(b) 実験とモデルの比較。
白棒は (a) の実験ニューロンの反応。
黒棒と灰色棒は，優先刺激の幹-楕円底遷移に同調させたモデルニューロンの反応を示す。
このモデルニューロンは，図 2 に示したモデルの単純化された版の最上部にあり，受容野の各位置に 2 種類の S1 特徴のみが存在し，それぞれが遷移領域の左側または右側に同調し，MAX 関数 (黒棒グラフ) または SUM 関数 (灰色棒グラフ) のいずれかを用いてそれらをプールする C1 ユニットに供給される。
モデルニューロンは，実験ニューロンの好ましい刺激がその受容野にあるときに，その反応が最大になるように，これらの C1 ユニットに接続された。
<!-- Fig. 3. Highly nonlinear shape-tuning properties of the MAX mechanism.
(a) Experimentally observed responses of IT cells obtained using a `simplification procedure`(26) designed to determine `optimal` features (responses normalized so that the response to the preferred stimulus is equal to 1).
In that experiment, the cell originally responded quite strongly to the image of a `water bottle` (leftmost object).
The stimulus was then `simplified` to its monochromatic outline, which increased the cell’s firing, and further, to a paddle-like object consisting of a bar supporting an ellipse.
Whereas this object evoked a strong response, the bar or the ellipse alone produced almost no response at all (figure used by permission).
(b) Comparison of experiment and model.
White bars show the responses of the experimental neuron from (a).
Black and gray bars show the response of a model neuron tuned to the stem-ellipsoidal base transition of the preferred stimulus.
The model neuron is at the top of a simplified version of the model shown in Fig. 2, where there were only two types of S1 features at each position in the receptive field, each tuned to the left or right side of the transition region, which fed into C1 units that pooled them using either a MAX function (black bars) or a SUM function (gray bars).
The model neuron was connected to these C1 units so that its response was maximal when the experimental neuron’s preferred stimulus was in its receptive field. -->


<!-- MAX 機構に対する追加的な間接的支持は，IT 細胞の好ましい特徴，つまり細胞を駆動するための刺激成分を決定するために，「単純化手順」(26 )または「複雑性減少」(27) を用いた研究から得られている。 -->
MAX 機構に対する追加的な間接的支持は，IT 細胞の好ましい特徴，つまり細胞を駆動するための刺激成分を決定するために，「単純化手順」または「複雑性減少」を用いた研究から得られている。
これらの研究では一般的に，IT 細胞の高度に非線形な同調を発見している (図 3a)。
このような同調は MAX 応答関数 (図 3b 黒棒) と一致する。
線形モデル (図 3b 灰色棒) では，入力画像のわずかな変化に対す るこの強い応答の変化を再現できないことに注意。
<!--Additional indirect support for a MAX mechanism comes from studies using a `simplification procedure`(26) or `complexity reduction`(27) to determine the preferred features of IT cells, that is, the stimulus components that are responsible for driving the cell.
These studies commonly find a highly nonlinear tuning of IT cells (Fig. 3a).
Such tuning is compatible with the MAX response function (Fig. 3b, black bars).
Note that a linear model (Fig. 3b, gray bars) could not reproduce this strong change in response for small changes in the input image.
-->

<div class="figcenter">

<iframe src="/conv-demo/index.html" width="140%" height="640px;" style="border:none;"></iframe>

</div>

# CORnet [Kubilius+2018](https://doi.org/10.1101/408385){:target="_blank"}

<div class="figcenter">
<img src="/2024assets/2018Kubillus_CORnet_fig1.svg" width="77%">
</div>
<div class="figcaption" style="width:77%;">

**図 1. CORnet 族のアーキテクチャ**<br/>
この族のすべてのモデルには，皮質領域 V1, V2, V4, IT にあらかじめ写像された 4 領域がある。
網膜と LGN の処理は現在のところモデル化されていない (灰色で塗りつぶされた領域)。
すべての領域はフィードフォワードかリカレント (領域内) のどちらかであるが，現在のところ，領域間のスキップ接続やフィードバック接続を持つモデルは考慮していない (灰色で塗りつぶした破線の矢印)。
本論文では，3  種類の CORnet を検討し，それぞれ異なる機能を提供する： CORnet-Z は軽量な AlexNet 代替モデル，CORnet-R は生物学的に説得力のある時間的アンロールを持つ単純なリカレントモデル，そしてCORnet-S は Brain-Score で現時点で最も高い性能を発揮するモデルである。
下段の図は各モデルの領域内の回路を表している。
<!-- Fig. 1. CORnet family of architectures.
All models in this family have four areas that are pre-mapped to cortical areas V1, V2, V4, and IT.
Retinal and LGN processing is currently not modeled (greyed-out areas).
All areas can be either feedforward or recurrent (within area) but currently we do not consider models with skip or feedback connections between areas (grayed-out dashed arrows).
In this paper, we consider three flavors of CORnet, each serving distinct functions: CORnet-Z is a lightweight AlexNet alternative, CORnet-R is a simple recurrent model with biologically-plausible unrolling in time, and CORnet-S is our highest-performing model on Brain-Score at the moment.
Diagrams in the bottom panel depict circuitry within an area of each model. -->
</div>

<div class="figcenter">
<img src="/2024assets/2018Kubillus_CORnet_tab1.svg">
</div>

モデルの復号化部は，単純な線形分類器 (各物体カテゴリに対して 1 つの総和を持つ重み付き線形和の集合) を実装する。
ImageNet で学習する場合，最後のモデル領域 (再帰の場合は最後の時間ステップ) の応答は，さらにソフトマックス非線形に渡され，1000 通りの分類が実行される。
この分類器に投影される神経応答の量を減らすために，まず特徴地図ごとの受容野全体の応答を平均化する。
現在の CORnet 族の定義では，領域横断バイパス接続や領域横断フィードバック接続は存在しない。
網膜と LGN の処理は省略されている (考察参照)。
また，計算要求が高いため，CORnet-S の第 1 領域は簡略化され，2 つの畳み込みのみが含まれる (下記参照)。
<!-- The decoder part of a model implements a simple linear classifier – a set of weighted linear sums with one sum for each object category.
When training on ImageNet, responses of last model area (and last time step in the case of recurrence) are further passed through a softmax nonlinearity to perform a 1000-way classification.
To reduce the amount of neural responses projecting to this classifier, we first average responses over the entire receptive field per feature map.
There are no across-area bypass or across-area feedback connections in the current definition of CORnet family.
Retinal and LGN processing are omitted (see Discussion).
Also, due to high computational demands, the first area in CORnet-S is simplified to only include two convolutions (see below). -->

**CORnet-Z** (通称 Zero) は我々の最も単純なモデルであり，(i) AlexNet は既に深いモデル(Schrimpf+2018) とほぼ同程度に神経応答を予測しており，(ii) VGG (Simonyan&Zisserman2014) 以降に提案されたほとんどのアーキテクチャが 1 つの 1000-way 線形分類層のみを含むため，ImageNetの良好な性能を達成するために複数の完全連結層は必要ないようであることを観察することによって導き出された。
従って，CORnet-Z の面積回路は単一の畳み込み，それに続く ReLU 非線形と最大プーリングのみで構成される。
<!-- CORnet-Z (a.k.a. "Zero") is our simplest model, derived by observing that (i) AlexNet is already nearly as good in predicting neural responses as deeper models (Schrimpf+2018) and (ii) multiple fully-connected layers do not appear necessary to achieve good ImageNet performance, as most architectures proposed after VGG (Simonyan&Zisserman2014) contain only a singe 1000-way linear classification layer.
Thus, CORnet-Z’s area circuits consist of only a single convolution, followed by a ReLU nonlinearity and max pooling. -->

**CORnet-R** (通称 Recurrent) は，生物学的に妥当な方法でネットワークを伝播するリカレントダイナミクスを導入する (生物学的ネットワーク・アンローリングと非生物学的ネットワーク・アンローリングの比較については図 2 参照)。
CORnet-R では，リカレンスは領野内でのみ導入される (エリア間のフィードバック接続はない) ため，アンロールの特殊な方法は (より多くのメモリを消費することを除けば) ほとんど影響を及ぼさないが，それでもこのモデルを神経ダイナミクスの調査に役立てるため，生物学的に妥当なアンロールを使用することにした。
<!-- CORnet-R (a.k.a. "Recurrent") introduces recurrent dynamics that would propagate through the network in a biologically-valid manner (see Fig. 2 for a comparison between biological and non-biologicall network unrolling).
In CORnet-R, recurrence is introduced only within an area (no feedback connections between areas), so the particular way of unrolling has little effect (apart from consuming much more memory), but we chose to use biologically-valid unrolling nonetheless to make this model useful for investigating neural dynamics. -->

入力はまず，畳み込みを通すことでチャンネル数を 2 倍に増やしながら 2 倍にダウンスケールされ，続いて正規化と非線形化が行われる。
状態 (最初はゼロ) が結果に追加され，別の畳み込み，正規化，非線形性を経て，結果が領域の新しい状態として保存される。
我々は，群正規化 (Wu&He2018) と ReLU 非線形性を使用した。
<!-- The input is first downscaled twofold while increasing the number of channels twofold by passing it through a convolution, followed by normalization and a nonlinearity.
The state (initially zero) is added to the result and passed through another convolution, normalization, and nonlinearity, and the result is saved as a new state of the area.
We used group normalization (Wu and He, 2018) and ReLU nonlinearity -->

**CORnet-S** (通称 Skip) は，非常に深いフィードフォワードアーキテクチャを浅いリカレントモデルに変換することで，Brain-Score の最高モデルに匹敵することを目指している。
具体的には，CORnet-S は我々の行動ベンチマークで最も優れたモデルのいくつかである ResNets からインスピレーションを得ている (Rajalingham+2018, Schrimpf+2018)。
Liao&Poggio(2016) は ResNet 構造をアンロール型リカレントネットワークと考えることができると提案し，さらに最近の研究では CIFAR や ImageNet の性能に大きな損失を与えることなく重み共有が実際に可能であることを実証した (Jastrzebski+2017, Leroux+2018)。
<!-- CORnet-S (a.k.a. "Skip") aims to rival the best models on Brain-Score by transforming very deep feedforward architectures into a shallow recurrent model.
Specifically, CORnet-S draws inspiration from ResNets that are some of the best models on our behavioral benchmark (Rajalingham+2018, Schrimpf+2018).
Liao&Poggio(2016) proposed that ResNet structure could be thought of as an unrolled recurrent network and recent studies further demonstrated that weight sharing was indeed possible without a significant loss in CIFAR and ImageNet performance (Jastrzebski+2017, Leroux+2018). -->

CORnet-S は CORnet-R の回路の上にさらに 2 つの畳み込み（それぞれ正規化と非線形化が続く）を積み重ねる。
さらに，ResNet のボトルネックブロック構造に従い，2 回目の畳み込みでチャンネル数を4倍に拡大し，最後の畳み込みでチャンネル数を減少させる。
また，入力に状態を追加した結果が非線形を適用する直前に最後の畳み込みの出力と結合されるように，スキップ接続も含めた。
CORnet-S が領域内リカレント接続のみを有することを考慮し，メモリフットプリントを最小化するために，時間的にネットワークのアンロールを利用することなくこのモデルを訓練した (すなわち 図 2 に描かれているようなアンロールはないが，繰り返される計算にわたって重みは依然として共有される)。
特に，最初に情報が処理されるとき，3 回目の畳み込みとスキップ畳み込みは，入力をダウンスケールするために 2 のストライドを使用する。
そして，その出力は，さらなるリカレント処理（図 1 では gate と呼ばれる）のために，元の入力の代わりに使われる。
このモデルではバッチ正規化 (Ioffe&Szegedy2015) と ReLU 非線形性を使用し，バッチ正規化は (Jastrzebski+2017) が示唆するように経時的に共有されなかった。
<!-- CORnet-S stacks two more convolutions (each followed by a normalization and nonlinearity) on top of CORnet-R’s circuit.
Moreover, following ResNet’s bottleneck block structure, the second convolution expands the number of channels fourfold while the last one decreases them back.
We also included a skip connection, such that the result of adding the state to the input is combined with the output of the last convolution just prior to applying a nonlinearity.
Given that CORnet-S only has within-area recurrent connections, in order to minimize memory footprint we trained this model without making use of any network unrolling in time (i.e. no unrolling as depicted in Fig. 2, but weights are still shared over repeated computations).
In particular, the first time information is processed, the third convolution and the skip convolution use a stride of two to downscale inputs.
The output is then used instead of the original input for further recurrent processing (referred to as "gate" in Fig. 1).
We used batch normalization (Ioffe and Szegedy, 2015) and ReLU nonlinearity in this model, and batch normalization was not shared over time as suggested by (Jastrzebski+2017). -->


# 10. 経路集約ネットワーク Path Aggregation Network (PANet)

経路集約ネットワーク (PANet) [Liu+(2018)](https://arxiv.org/pdf/1803.01534.pdf) は最近, 経路集約ネットワーク Path Aggregation Network (PANet) を発表した。
このネットワークは Masked RCNN と FPN の枠組みを ベースにしながら，情報伝播を強化している。
このネットワークの特徴抽出器は FPN アーキテクチャを使用しており，低次層の特徴の伝搬を向上させる新たな拡張ボトムアップ経路を備えている。
この第 3 経路の各ステージは，前のステージの特徴地図を入力として 3x3 の畳み込み層で処理する。
その出力は，横方向に接続されたトップダウン経路の同じステージの特徴地図に追加され，これらの特徴地図は次のステージに供給される。
<!-- S. Liu et al. (2018) have recently released the Path Aggregation Network (PANet).
This network is based on the Mask R-CNN and the FPN frameworks while enhancing information propagation.
The feature extractor of the network uses a FPN architecture with a new augmented bottom-up pathway improving the propagation of low-layer features.
Each stage of this third pathway takes as input the feature maps of the previous stage and processes them with a 3x3 convolutional layer.
The output is added to the same stage feature maps of the top-down pathway using lateral connection and these feature maps feed the next stage. -->

<div class="figcenter">
<img src="/2024assets/2018Ouaknine_fig21.jpg" width="33%">
<div class="figcaption" style="width:44%;">

**トップダウン経路と拡張されたボトムアップ経路の横の連結**<!-- Lateral connection between the top-down pathway and the augmented bottom-up pathway.  -->
出典: [Liu+(2018)](https://arxiv.org/pdf/1803.01534.pdf)
</div></div>

補強されたボトムアップ経路の特徴地図は，RoI Align 層にプールされ，すべてのレベルの特徴から提案を抽出する。
適応的な特徴プーリング層は，各段階の特徴地図を完全連結層で処理し，すべての出力を連結する。
<!-- The feature maps of the augmented bottom-up pathway are pooled with a RoIAlign layer to extract proposals from all level features.
An adaptative feature pooling layer processes the features maps of each stage with a fully connected layer and concatenate all the outputs.  -->

<div class="figcenter">
<img src="/2024assets/2018Ouaknine_fig22.jpg" width="49%">
<div class="figcaption" style="width:44%;">

**適応的特徴プーリング層**<!-- Adatative feature pooling layer. --> Source: [Liu+(2018)](https://arxiv.org/pdf/1803.01534.pdf)
</div></div>

適応型特徴プーリング層の出力は，Mask R-CNN と同様に 3 つのブランチに供給される。
最初の 2 つのブランチでは，完全連結層を使用して，バウンディングボックスの座標と関連する物体クラスの予測を生成する。
3 つ目のブランチでは FCN を用いて RoI を処理し，検出された物体の画素単位の 2 値マスクを予測する。
さらに FCN の畳み込み層の出力を完全連結層で処理することで，予測される画素の位置関係を改善している。
最後に，並列パスの出力を再形成し，2 値化マスクを生成する FCN の出力に連結する。
<!-- The output of the adaptative feature pooling layer feeds three branches similarly to the Mask R-CNN.
The two first branches uses a fully connected layer to generate the predictions of the bounding box coordinates and the associated object class.
The third branch process the RoI with a FCN to predict a binary pixel-wise mask for the detected object.
The authors have added a path processing the output of a convolutional layer of the FCN with a fully connected layer to improve the localisation of the predicted pixels.
Finally the output of the parallel path is reshaped and concatenated to the output of the FCN generating the binary mask.  -->

<div class="figcenter">
<img src="/2024assets/2018Ouaknine_fig23.jpg" width="49%">
<div class="figcaption" style="width:44%;">

**FCN と完全連結層を持つ新しいパスを用いてバイナリマスクを予測する PANet のブランチ**
<!-- Branch of the PANet predicting the binary mask using a FCN and a new path with a fully connected layer.  -->
Source: https://arxiv.org/pdf/1803.01534.pdf
</div></div>

PANet は 2016COCO 画像切り分けチャレンジにおいて，特徴抽出器に ResNeXt を用いて 42.0 % の AP 得点を達成している。
また 2017COCO 画像切り分けチャレンジでは，7 つの特徴抽出器のアンサンブルを用いて 46.7 %の AP 得点を達成している。
ResNet ([He+(2015)](https://arxiv.org/pdf/1512.03385.pdf)), ResNeXt([Xie+(2016)](https://arxiv.org/pdf/1611.05431.pdf)), SENet ([Hu+(2017)](https://arxiv.org/pdf/1709.01507.pdf)) である。
<!-- The PANet has achieved 42.0% AP score on the 2016 COCO segmentation challenge using a ResNeXt as feature extractor.
They also performed the 2017 COCO segmentation challenge with an 46.7% AP score using a ensemble of seven feature extractors: ResNet (K. He et al. (2015), ResNeXt (S. Xie et al. (2016)) and SENet (J. Hu et al.(2017)).  -->

<div class="figcenter">
<img src="/2024assets/2018Ouaknine_fig24.jpg" widht="77%">
<div class="figcaption" style="width:66%;">

**PANet Achitecture**<br/>
**(a)**: FPN アーキテクチャを用いた特徴抽出器。<br/>
**(b)**: FPN アーキテクチャに新たに追加された増強されたボトムアップ経路。<br/>
**(c)**: 適応的な特徴プーリング層．<br/>
**(d)**: バウンディングボックスとオブジェクトクラスを表現する 2 つのブランチ．<br/>
**(e)**: オブジェクトのバイナリマスクを予測するブランチ．破線は，低レベルのパターンと高レベルのパターンの間のリンクに対応しており，赤は FPN で 100 以上の層で構成されており，緑は PANet で 10 以下の層で構成されているショートカットであ
る。
出典: [Liu+(2018)](https://arxiv.org/pdf/1803.01534.pdf)
<!-- PANet Achitecture. (a): Feature extractor using the FPN achitecture. (b): The new augmented bottom-up pathway added to the FPN architecture. ©: The adaptative feature pooling layer. (d): The two branches predicting the bounding box coordinated and the object class. (e): The branch predicting the binary mask of the object. The dashed lines correspond to links between low-level and high level patterns, the red one is in the FPN and consists in more than 100 layers, the green one is a shortcut in the PANet consisting of less than 10 layers. Source: S. Liu et al. (2018)  -->
</div></div>

# 11. Context Encoding Network (EncNet)

H. Zhang+(2018) は，シーンセグメンテーションを改善するために，画像の大域的情報を取り込む Context Encoding Network (EncNet) を作成しました。
このモデルは， 基本的な特徴抽出器 (ResNet) を使用することから始まり，特徴地図を H. Zhang ら (2016) の 符号化層からインスパイアされた Context Encoding Module に供給します。
基本的には，クラスに依存する特徴地図を強調しつつ，文脈情報を考慮した埋め込みを作成するために，視覚的中心と平滑化係数を学習します。
モジュールの上には，特徴地図注目層  (完全連結層) で文脈情報のスケーリング係数を学習します。
これと並行して， 2 値の交差エントロピー損失に対応するセマンティック符号化損失 (SE-Loss)
が，(画素単位の損失とは異なり) 物体クラスの存在を検出することで，モジュールの学習を正則化します。
文脈符号化モジュールの出力は 2 つの SE-損失 と最終的な画素単位の損失を最小化しながら，希釈された畳み込み戦略によって再形成され，処理されます。
最高の EncNet は，PASCAL-Context チャレンジにおいて 52.6% の mIoU と 81.2% の pixAcc スコアを達成しました。
また 2012 年の PASCAL VOC セグメンテーションチャレンジでは 85.9% の mIoU スコアを達成しています。
<!-- H. Zhang et al. (2018) have created a Context Encoding Network (EncNet) capturing global information in an image to improve scene segmentation.
The model starts by using a basic feature extractor (ResNet) and feeds the feature maps into a Context Encoding Module inspired from the Encoding Layer of H. Zhang et al. (2016).
Basically, it learns visual centers and smoothing factors to create an embedding taking into account the contextual information while highlighting class-dependant feature maps. On top of the module, scaling factors for the contextual information are learnt with a feature maps attention layer (fully connected layer).
In parallel, a Semantic Encoding Loss (SE-Loss) corresponding to a binary cross-entropy loss regularizes the training of the module by detecting presence of object classes (unlike the pixel-wise loss).
The outputs of the Context Encoding Module are reshaped and processed by a dilated convolution strategy while minimizing two SE-losses and a final pixel-wise loss.
The best EncNet has reached 52.6% mIoU and 81.2% pixAcc scores on the PASCAL-Context challenge. It has also achieved a 85.9% mIoU score on the 2012 PASCAL VOC segmentation challenge. -->

<div class="figcenter">
<img src="/2024assets/2018Ouaknine_fig25.jpg" width="49%">
<div class="figcaption" style="width:66%;">

**拡張された畳み込み戦略**<br/>
青色は畳み込みフィルタ，D は拡張率。
SE-損失 (Semantic Encoding Loss) は，第 3 段階と第 4 段階の後に適用され，オブジェクトクラスを検出。
最後の Seg-損失 (pixel-wise loss) は，セグメンテーションを改善するために適用される。
<!-- Dilated convolution strategy.
In blue the convolutional filter with D the dilatation rate.
The SE-losses (Semantic Encoding Loss) are applied after the third and the fourth stages to detect object classes.
A final Seg-loss (pixel-wise loss) is applied to improve the segmentation.-->
Source: H. Zhang+(2018)
</div></div>


<div class="figcenter">
<img src="/2024assets/2018Ouaknine_fig26.jpg" width="49%">
<div class="figcaption" style="width:55%;">

**EncNet のアーキテクチャ**<br/>
特徴抽出器は，文脈符号化器モジュールの入力となる特徴地図を生成する。
このモジュールは，意味符号化損失を用いた正則化によって学習される。
このモジュールの出力は，希釈された畳み込み戦略によって処理され，最終的なセグメンテーションが生成される。
<!-- Architecture of the EncNet.
A feature extractor generates feature maps took as input of a Context Encoding Module.
The module is trained with regularisation using the Semantic Encoding Loss.
The outputs of the module are processed by a dilated convolution strategy to produce the final segmention.-->
Source: [Zhang+(2018)](https://arxiv.org/pdf/1803.08904.pdf)
</div></div>



# `bl_net.py`

```python
'''
Keras implementation of BL network
'''

import tensorflow as tf


class BLConvLayer(object):
    '''BL recurrent convolutional layer

    Note that this is NOT A KERAS LAYER but is an object containing Keras layers

    Args:
        filters: Int, number of output filters in convolutions
        kernel_size: Int or tuple/list of 2 integers, specifying the height and
            width of the 2D convolution window. Can be a single integer to
            specify the same value for all spatial dimensions.
        layer_name: String, prefix for layers in the RCL
        '''
    def __init__(self, filters, kernel_size, layer_name):
        # initialise convolutional layers
        self.b_conv = tf.keras.layers.Conv2D(
            filters, kernel_size, padding='same', use_bias=False,
            kernel_initializer='glorot_uniform',
            kernel_regularizer=tf.keras.regularizers.l2(1e-6),
            name='{}_BConv'.format(layer_name))

        self.l_conv = tf.keras.layers.Conv2D(
            filters, kernel_size, padding='same', use_bias=False,
            kernel_initializer='glorot_uniform',
            kernel_regularizer=tf.keras.regularizers.l2(1e-6),
            name='{}_LConv'.format(layer_name))

        # layer for summing convolutions
        self.sum_convs = tf.keras.layers.Lambda(
            tf.add_n, name='{}_ConvSum'.format(layer_name))

        # holds the most recent bottom-up conv
        # useful when the bottom-up input does not change, e.g. input image
        self.previous_b_conv = None

    def __call__(self, b_input=None, l_input=None):
        conv_list = []

        if not b_input is None:
            # run bottom-up conv and save result
            conv_list.append(self.b_conv(b_input))
            self.previous_b_conv = conv_list[-1]
        elif not self.previous_b_conv is None:
            # use the most recent bottom-up conv
            conv_list.append(self.previous_b_conv)
        else:
            raise ValueError('b_input must be given on first pass')

        # run lateral conv
        if l_input is not None:
            conv_list.append(self.l_conv(l_input))

        # return element-wise sum of convolutions
        return self.sum_convs(conv_list)


def bl_net(input_tensor, classes, n_timesteps=8, cumulative_readout=False):
        '''Build the computational graph for the model

        Note that evaluations based on model outputs will reflect instantaneous
        rather than cumulative readouts

        Args:
            input_tensor: Keras tensor (i.e. output of `layers.Input()`)
                to use as image input for the model.
            classes: int, number of classes to classify images into
            n_timesteps: int, number of model time steps to build
            cumulative_readout: Bool, if True then the outputs correspond to a
                cumulative readout on each time step if True then they
                correspond to a instant readout

        Returns:
            model
        '''

        data_format = tf.keras.backend.image_data_format()
        norm_axis = -1 if data_format == 'channels_last' else -3

        # initialise trainable layers (RCLs and linear readout)
        layers = [
            BLConvLayer(96, 7, 'RCL_0'),
            BLConvLayer(128, 5, 'RCL_1'),
            BLConvLayer(192, 3, 'RCL_2'),
            BLConvLayer(256, 3, 'RCL_3'),
            BLConvLayer(512, 3, 'RCL_4'),
            BLConvLayer(1024, 3, 'RCL_5'),
            BLConvLayer(2048, 1, 'RCL_6'),
        ]
        readout_dense = tf.keras.layers.Dense(
                classes, kernel_initializer='glorot_uniform',
                kernel_regularizer=tf.keras.regularizers.l2(1e-6),
                name='ReadoutDense')

        # initialise list for activations and outputs
        n_layers = len(layers)
        activations = [[None for _ in range(n_layers)]
                       for _ in range(n_timesteps)]
        presoftmax = [None for _ in range(n_timesteps)]
        outputs = [None for _ in range(n_timesteps)]

        # build the model
        for t in range(n_timesteps):
            for n, layer in enumerate(layers):

                # get the bottom-up input
                if n == 0:
                    # B conv on the image does not need to be recomputed
                    b_input = input_tensor if t == 0 else None
                else:
                    # pool b_input for all layers apart from input
                    b_input = tf.keras.layers.MaxPool2D(
                        pool_size=(2, 2),
                        name='MaxPool_Layer_{}_Time_{}'.format(n, t)
                        )(activations[t][n-1])

                # get the lateral input
                if t == 0:
                    l_input = None
                else:
                    l_input = activations[t-1][n]

                # convolutions
                x_tn = layer(b_input, l_input)
                # batch-normalisation
                x_tn = tf.keras.layers.BatchNormalization(
                    norm_axis,
                    name='BatchNorm_Layer_{}_Time_{}'.format(n, t))(x_tn)
                # ReLU
                activations[t][n] = tf.keras.layers.Activation(
                    'relu', name='ReLU_Layer_{}_Time_{}'.format(n, t))(x_tn)

            # add the readout layers
            x = tf.keras.layers.GlobalAvgPool2D(
                name='GlobalAvgPool_Time_{}'.format(t)
                )(activations[t][-1])
            presoftmax[t] = readout_dense(x)

            # select cumulative or instant readout
            if cumulative_readout and t > 0:
                x = tf.keras.layers.Add(
                    name='CumulativeReadout_Time_{}'.format(t)
                    )(presoftmax[:t+1])
            else:
                x = presoftmax[t]
            outputs[t] = tf.keras.layers.Activation(
                'softmax', name='Sotfmax_Time_{}'.format(t))(x)

        # create Keras model and return
        model = tf.keras.Model(
            inputs=input_tensor,
            outputs=outputs,
            name='bl_net')

        return model
```

## 畳み込みニューラルネットワーク

<img src="/2023assets/alex_net_block_diagram.png"><br/>

<img src="/assets/ResNet_Fig2.svg" width="33%"><br/>
<img src="/assets/2015ResNet30.svg" width="94%"><br/>
<img src="/2023assets/2015Ren_Faster_R-CNN_fig2.svg">

<!-- <img src="/assets/2017He_MaskRCNN_41.svg">
<img src="/assets/2015Fast_R-CNN_Fig1.svg">
<img src="/assets/2015Faster_RCNN_RPN.svg">
<img src="/assets/1998LeCun_Fig2_CNN.svg">
<img src="/assets/2017He_MaskRCNN_02SemSeg.svg">
<img src="/assets/2017He_MaskRCNN_08.svg">
<img src="/assets/2017He_MaskRCNN_02Oject.svg">
<img src="/assets/2013Girshick_RCNN_Fig1.svg"> -->

## 経路仮説と残差ネット

* 腹側経路 ventral pathways ("what" 経路)
* 背側経路 dorsan pathways ("where" 経路)

<center>
<img src="/assets/1982Ungerleider_Mishkin.jpg" width="49%">
<div style="text-align:left;width:88%;color:teal">

* 下左: 物体弁別課題と下側頭回損傷。
* 下右: 目印課題と頭頂葉損傷。
Ungerleider&Mishkin1982 より。
</div></center>

<center>
<img src="/2023assets/2004Hickok_dorsal_ventral_language_fig1a.jpg" width="49%">
<img src="/2023assets/2004Hickok_dorsal_ventral_language_fig1b.jpg" width="49%">
<div style="text-align:left;width:94%;color:teal">
左: 言語の機能解剖学的枠組み。Hickok&Poeppel2000 より

右: 脳の側面図に示したモデル構成要素の一般的な場所。
モデル内のある機能に関連する皮質領域は，その機能に特化しているという仮説ではない。
調音に基づく音声符号を支援すると考えられる前頭葉領域の定義は，物品の命名と調音リハーサル処理の機能画像研究にお
ける活性化領域の一般的な分布から得られる (例えば Awh+1996, Hickok+2003, Indefrey&Levelt)。
帯状の領域 (上側頭溝) は，音素レベルの表現を支援すると思われる領域。
</div>
</center>



# [Top-Down Network Combines Back-Propagation with Attention](https://arxiv.org/abs/2306.02415)

* [GitHub](https://github.com/royabel/Top-Down-Networks)

* 生物学に着想を得たインストラクションモデルの学習法を提案
* ボトムアップ (BU)-トップダウン (TD) モデルを用い，1 つの TD ネットワークを学習と注意誘導の両方に使用
* 本論文の主な貢献は以下の通り
<!-- The paper propose a biologically-inspired learning method for instruction-models.
It uses a bottom-up (BU) - top-down (TD) model, in which a single TD network is used for both learning and guiding attention.
The key contributions of the paper are: -->

  * 誤差信号からの学習とトップダウンの注意を組み合わせた新しいトップダウン機構を提案
  * 従来研究を拡張し，より生物学的に妥当な学習モデルへの新たなステップを提供
  * 生物学的学習のためのカウンター Hebb 学習機構の提案
  * 従来のネットワークの中に，課題依存した独自の部分ネットワークを動的作成。生物学に着想を得た新しい Multi Task Learning (MTL) アルゴリズムの提示

<!-- * Propose a novel top-down mechanism that combines learning from error signals with top-down attention.
* Extending earlier work, offering a new step toward a more biologically plausible learning model.
* Suggest a Counter-Hebbian mechanism for biological learning.
* Present a novel biologically-inspired MTL algorithm that dynamically creates unique task-dependent sub-networks within conventional networks. -->


<div class="figcenter">
<img src="/2023assets/top_down_processing.png" width="33%">
</div>
<div class="figcaption" style="width:66%">

Bottom-up Top-down アプローチ<br/>
BU-TD アプローチは，双方向接続を持つ BU (青色) と TD (オレンジ色) ネットワークから構成される。
これらのネットワークは再帰的に動作できる。
1 つの TD ネットワークは，ダウン誤差信号の伝搬と TD 注意の両方に使用され，BU ネットワークは入力信号の処理を行う。
右図では，この概念をマルチタスク学習の設定で説明している。
I は入力信号 (例：視覚の場合の画像)，E はエラー信号 (例 損失勾配)，A は注意信号(例: 選択された物体，場所，課題) を示す。
</div>

### カウンター Hebb 学習<!--Counter-Hebbian Learning-->


<div class="figcenter">
<img src="/2023assets/update_rule.png" width="44%">
</div>
<div class="figcaption">
カウンター Hebb 学習

* 生物学的に動機づけられた学習機構。
* 古典的な Hebb 学習と同様に，カウンター Hebb 学習則はシナプスに接続されたニューロンの活動に基づいてシナプスを更新。
* 右図に示す Counter-Hebb 学習則は，古典的 Hebb 則 (左図) のように上流ニューロンからの逆発射ではなく，側方結合を介して接続された下流 (オレンジ色で示された) カウンターニューロンに依存する。
<!-- A biologically motivated learning mechanism.
Similar to the classical Hebbian learning, the Counter-Hebb learning rule update the synapse based on the activity of the neurons connected to the synapse.
However, the Counter-Hebb update rule, presented on the right, relies on the counterpart downstream (marked in  orange) counter neurons which is connected via lateral connections instead of a back firing from the upstream neuron as in the classical Hebb rule (on the left). -->
</div>

## 活性関数とバイアス<!--\label{section - activation functions}-->

活性化関数 $\sigma$, $\bar{\sigma}$ は，要素ごとの関数であれば何でもよい。
本研究では 2 つの関数に注目する。
1 つ目はニューラルネットワークでよく用いられる ReLU である。

$$
\text{ReLU}(x):=(x)_{+}=\begin{cases}
x & x > 0 \\
0 & x\leq 0
\end{cases}$$

もう 1 つは Gated-Linear-Unit(GaLU) で，BU-TD の構造を利用し，カウンターニューロンに応じてゲーティングを行う。
<!-- The activation functions $\sigma$, $\bar{\sigma}$, may be any element-wise functions.
In this work, we focus on two functions.
The first is ReLU which is commonly used for neural networks $ReLU(x):=(x)_+=\begin{cases} x & x > 0 \\ 0 & x
\leq 0\end{cases}$.
The second is Gated-Linear-Unit (GaLU), which exploits our BU-TD structure by gating according to the counter
neurons. -->

$$
\tag{Couter Gating Def}
\text{GaLU}(x):=\text{GaLU}(x, \bar{x}) := x \cdot I_{\bar{x} > 0} =
\begin{cases}
x & \bar{x} > 0 \\
0 & \bar{x} \leq 0
\end{cases}$$

ここで，$\bar{x}$ は $x$ のカウンターニューロン，$I$ は指標関数である。
<!-- Where $\bar{x}$ is the counter neuron of $x$, and $I$ is an indicator function. -->

GaLU には興味深い特性がある。
GaLU は，BU ネットワークと TD ネットワークの間に横方向の接続性を導入し，対になるニューロンの値に基づいて一時的にニューロンをオフにする。
その結果，各ネットワークは，特定の部分的なサブネットワークで動作するように，その対応するネットワークを効果的に誘導することができる。
ただし，この関数のゲート $\bar{x}$ に対する勾配は常にゼロである。
加えて，GaLU は $x$ と インジケータ $l_{\bar{x}>0}$ これは，ReLU 関数の勾配 $\frac{\partial}{\partial\bar{x}}\text{ReLU}\left(\bar{x}\right)=I_{\bar{x}>0}$ と正確に同じであるである。
この性質は，BP と等価なバックワードパスを構築するために，学習アルゴリズム で使われる。
<!-- GaLU has some interesting properties.
It introduces lateral connectivity between the BU and TD networks by temporarily turning off neurons based on the values of their counter neurons.
As a result, each network can effectively guide its counterpart to operate on a specific partial sub-network.
However, it is worth noting that the gradients of this function with respect to the gate $\bar{x}$ are always zero.
Additionally, GaLU applies a product of $x$ with the indicator $I_{\bar{x} > 0}$ which is exactly the gradient of the ReLU function: $\frac{\partial}{\partial \bar{x}} ReLU(\bar{x}) = I_{\bar{x} > 0}$.
This property will be used in section ~\ref{section: learning algorithm} to construct a backward pass that is equivalent to BP. -->


#### Multi-task Learning (MTL)

MTL アルゴリズムは，課題ごとに課題依存のサブネットワークを動的に学習する。
MTL アルゴリズムは 2 つのフェーズから構成される：予測のための TD パスと，それに続くBU パス，そして学習のためのもう 1 つの TD パスである。
選択された課題は TD ネットワークに入力を提供し，活性化は ReLU 非線形性を持つ下方への注意誘導信号を伝播する。
ReLU を適用することで，課題はニューロンの部分集合 (すなわち非ゼロ値) を選択的に活性化し，前ネットワーク内の部分ネットワークを構成する。
そして BU ネットワークは，ReLU と GaLU の合成を用いて入力画像を処理する。
GaLU 関数 (破線の矢印で示す) は，対応する TD 隠れ層によって BU 隠れ層をゲートする。
その結果，BU 計算は選択されたサブネットワーク上でのみ実行される。
最後に，予測ヘッドはトップレベルの BU 隠れ層に基づいて予測を生成する。
学習のために，同じ TD ネットワークが，予測ヘッドを起点として予測誤差信号を伝播するために再利用される。
この計算は GaLU のみで行われ (ReLU なし)，これにより負の値が許容される。
最後に，'Counter-Hebb’ 学習則は，隠れ層の活性化値に基づいて両方のネットワークの重みを調整する。
したがって，標準的モデルとは対照的に，すべての計算はネットワーク内のニューロンによって実行され，学習に外部計算 (例えば誤差逆伝播法) は使用されない。
あるいは，BU と TD の重みを共有するという制約のもとで，学習段階を標準的な BP で再現することもできる。
これにより同等の学習フェーズが得られる。
<!-- The MTL algorithm offers dynamically learning task-dependent sub-networks for each task.
The MTL algorithm comprises of two phases: a TD pass followed by a BU pass for prediction, and another TD pass for learning.
The selected task provides input to the TD network, and the activation propagates downward attention-guiding signals with ReLU non-linearity.
By applying ReLU, the task selectively activates a subset of neurons (i.e. non-zero values), composing a sub-network within the full network.
The BU network then processes an input image using a composition of ReLU and GaLU.
The GaLU function (denoted with dashed arrows) gates the BU hidden layers by their corresponding counter TD hidden layers.
As a result, the BU computation is performed only on the selected sub-network. Lastly, the prediction head generates a prediction based on the top-level BU hidden layer.
For learning, the same TD network is then reused to propagate prediction error signals, starting from the prediction head.
This computation is performed with GaLU exclusively (no ReLU), thereby permitting negative values.
Finally, the 'Counter-Hebb' learning rule adjusts both networks' weights based on the activation values of their hidden layers.
Therefore, in contrast with standard models, the entire computation is carried out by neurons in the network, and no external computation is used for learning (e.g. Back-Propagation).-->

<div class="figcenter">
<img src="/2023assets/MTL_schematic.png" width="49%">
</div>

**カウンター Hebbian 学習**<br/>

1. BU ネットワークを実行し，入力 $x$ を非線形活性化関数を用いて出力 $y$ へと写像
2. 誤差信号を計算
3. 誤差信号を用いて TD ネットワークを GaLu (非線形性なし) のバイアスブロックモードで実行
4. Counter-Hebb 学習則に従い，BU と TD パラメータの両方を更新

<!-- 1. Run BU network to map the input x to an output y with non-linear activation function.
2. Compute error signals.
3. Run the TD network using the error signals, in a bias-blocking mode with GaLu (no non-lineality).
4. Update both the BU and TD parameters according to the Counter-Hebb learning rule. -->

**マルチタスク学習**<!--Multi-task learning--><br/>

1. 課題ヘッドを使って，課題 $t$ を入力とする TD ネットワークを ReLU で実行する。
2. BU ネットワークを実行し，入力 $x$ を出力 $y$ に ReLU と GaLU の合成で対応付ける。
3. 誤差信号，すなわち BU 出力に対する損失 $L$ の勾配を計算： $\displaystyle -\frac{\partial L}{\partial y}$
4. 誤差信号を入力として，GaLU (非線形性なし) のバイアスブロックモードで TD ネットワークを実行
5. すべての重みを Counter-Hebb 学習則に従って更新する (課題ヘッドは除く，6 節参照)。

<!-- 1. Run the TD network with task t as input with ReLU, using the task head.
2. Run the BU network to map the input x to an output y with a composition of ReLU and GaLU.
3. Compute error signals, i.e. the gradients of a loss L with respect to the BU output: $\displaystyle -\frac{\partial L}{\partial y}$
4. Run the TD network using the error signals as inputs, in a bias-blocking mode with GaLU (no non-lineality).
5. Update all the weights according to th Counter-Hebb learning rule. (Excluding the task head, see section 6) -->

### 文献

* [系列探索と逆行流: 視覚野における双方向情報フローの計算モデル](/2023cogpsy/2021Ullman_bu_td_ja.pdf)
* [ボトムアップ・トップダウンの反復処理による画像解釈](/2023cogpsy/1995Ullman_bidirectional_cortex_ja.pdf)
