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
* [DOG などのフィルタと Harr 特徴による顔検出 a.k.a ビオラ＝ジョーンズ アルゴリズム<img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/notebooks/2021_0528edge_and_face_detection_algorithm_not_cnn.ipynb){:target="_blank"}
* [いくつかの画像フィルタ 特徴点検出アルゴリズム<img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/notebooks/2020Sight_visit_feature_extractions_demo.ipynb){:target="_blank"}

* [顔，非顔判別データセットを用いた紡錘状回のモデル化 --- 転移学習を用いた顔検出モデル ---  <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_0925face_dataset_transfer_learning.ipynb){:target="_blank"}
    - Robust Real-Time Face Detection, Viola, P. and Jones, M. (2004)

* [ヴィオラ=ジョーンズ アルゴリズム(従来手法) による顔認識実験 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_0930viola_jones_ipynb.ipynb){:target="_blank"}


# 本日のメニュー

<!-- 1. 数式の読み方 -->
1. ブレイクモア＆クーパーの実験ビデオ閲覧
2. 特徴検出器 feature detectors, セルフリッジのパンデモニアムモデル
3. ワンアルゴリズム仮説 ワンアルゴリズム仮説 One algorithm hypothesis


## 考え方，背景，キーワード

* 構成論的アプローチ vs 分析的アプローチ （人工知能と心理学との関係）
* 神は細部に宿る God is in the detail. あるいは 悪魔は細部に宿る (The devil is in the detail)
* [炭素排他主義 (Carbon chauvinism)](https://en.wikipedia.org/wiki/Carbon_chauvinism)
    * 炭素排他主義（Carbon Chauvinism）とは，知られている限り、炭素の化学的および熱力学的特性は、生物に使用される分子を形成する上で、他のすべての元素よりもはるかに優れていることから，地球外を含む全ての生命体の化学過程は，炭素（有機化合物）から構築されなければならないという仮定を軽蔑するための造語。
    * 人工知能は理論上，基礎となる物質が生物学的でないことから，感覚や知性を持ち得ないという考えを批判するためにも 炭素排他主義という言葉が使われる。

<!-- - Carbon chauvinism is a neologism meant to disparage the assumption that the chemical processes of hypothetical extraterrestrial life must be constructed primarily from carbon (organic compounds) because as far as is known, carbon's chemical and thermodynamic properties render it far superior to all other elements at forming molecules used in living organisms.[1]
The expression "carbon chauvinism" is also used to criticize the idea that artificial intelligence can't in theory be sentient or truly intelligent because the underlying matter isn't biological.[2] -->

# 視覚モデルの歴史

人間の視覚処理のモデリングは，Hubel&Wiesel にさかのぼることができる。
Hubel&Wiesel では，視覚野 V1 の単純な細胞の応答特性はエッジの特徴検出として形式化され，複雑な細胞の特性は視野上で空間的に繰り返される一連の操作として概念化された（Hubel&Wiesel1962，translationaly invariant 並進不変）。
この計算原理は，コンピュータビジョンに霊長類の視覚系の特性を取り入れる試みとして Neocognitron（Fukushima1980）に取り入れられた。
さらに HMAX モデルファミリー（Riesenhuber&Poggio1999, Serre+2007）にも影響を与えた。
これらは，今日の特徴検出器とプーリング演算子を交互に用いた物体認識の深層学習モデルとして用いられれている。
(ただし，画像切り分けでは，プーリングを除外する傾向にある。)
AlexNet (Russakovsky+2015) 以前は，ネットワークをどのように組み込むか，あるいは他の方法で訓練するか，明確ではなかった（Olshausen&Field1996, Lowe1999, Torralba&Oliva2003）。
深層ニューラルネットワークを訓練する少なくとも 1 つの方法が示された 。同時に，このような不変
ImageNet 画像認識コンテストで優勝したモデルでは，視覚野 V4 と IT のニューロンの応答を圧倒的によくモデル化した内部「神経」表現を生成することが実証された（Yamins+2013, Cadieu+2014, Yamins+2014）。
ヒトの fMRI や MEG といった，より高度な実験レベルでの説明力の向上が確認された（Khaligh-Razavi&Kriegeskorte2014, Güçlü&van Gerven2015, Cichy+2016）。
<!-- Modeling human visual processing traces back at least to Hubel and Wiesel where response properties of simple cells in visual area V1 were formalized as feature detection of edges and properties of complex cells were conceptualized as a set of operations that were spatially repeated over the visual field (Hubel&Wiesel1962, i.e., translationally invariant).
These computational principles inspired the first models of object recognition, most notably, the Neocognitron (Fukushima1980) and the HMAX model family (Riesenhuber&Poggio1999; Serre+2007), where feature detectors and pooling operators were used in turns to build deep hierarchical models of object recognition.
However, such models lacked robust feature representations as it was not clear at the time how to either build in or otherwise train these networks to learn their spatially-repeated operations from input statistics – particularly for areas beyond visual area V1 (Olshausen&Field1996, Lowe1999, Torralba&Oliva2003).
These issues were first addressed by the AlexNet ANN (Krizhevsky+2012) in that it demonstrated at least one way to train a deep neural network for a large-scale invariant object recognition task (Russakovsky+2015).
Concurrently, deep networks optimized for such invariant object recognition tasks were demonstrated to produce internal "neural" representations that were by far the best models of the responses of neurons in non-human primate visual areas V4 and IT (Yamins+2013, Cadieu+2014, Yamins+2014).
Later work in humans confirmed these gains in explanatory power at the courser experimental level of fMRI and MEG (Khaligh-Razavi&Kriegeskorte2014; Güçlü&van_Gerven2015, Cichy+2016), with detailed measures of behavioral response patterns in both humans and non-human primates (e.g., Rajalingham+2015, Kubilius+2016, Rajalingham+2018), and with non-human primate neural spiking measures from the cortical area V1 (Cadena+2017). -->


## ブレイクモア と クーパー Blackmore and Cooper (1970)

<center>
<iframe width="1024" height="768" src="https://www.youtube.com/embed/QzkMo45pcUo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<!-- <iframe width="450" height="300" src="https://www.youtube.com/embed/QzkMo45pcUo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> -->
<!--<iframe width="845" height="676" src="https://www.youtube.com/embed/QzkMo45pcUo" frameborder="0"
 allow="ac
celerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>-->
<br/>
source:` https://youtu.be/QzkMo45pcUo`
</center>

<center>
<img src='/assets/1970BlackmoreCooper_Fig1.svg' style='width:39%'>
<img src='/assets/1970BlackmoreCooper_Fig2.svg' style='width:49%'>
</center>


<center>
<iframe width="1024" height="768" src="https://www.youtube.com/embed/RSNofraG8ZE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br/>
<!-- <iframe width="450" height="300" src="https://www.youtube.com/embed/RSNofraG8ZE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br/> -->
source: https://youtu.be/RSNofraG8ZE
</center>


## 心理学的対応

### セルフリッジ (Selfridge) のパンデモニウム (pandemonium) モデル

<div class="figcenter">
<img src="/assets/1958Selfridge_fig3.svg" style="width:55%"><br>
セルフリッジ (1958) ``Mechanisation of Thought Processes'' より

<!-- <img src="/assets/1958Selfridge_fig7.svg" style="width:84%"><br>
セルフリッジ (1958) ``Mechanisation of Thought Processes'' より -->
</div>


<!-- <center>
<img src='../assets/1958Selfridge_fig4.svg' style='width:49%'><br>
<img src='../assets/1958Selfridge_fig5.svg' style='width:74%'><br>
<img src='../assets/1958Selfridge_fig6.svg' style='width:49%'><br>
セルフリッジ (1958) ``Mechanisation of Thought Processes'' より
</center> -->


<img src="/2025assets/1977LindseyNorman_pand.jpg" style="width:44%;">
<img src="/2025assets/1977LindseyNorman_pand2.jpg" style="width:44%;">
<div class="figcaption">

Lindsey&Norma(1977) Human Information Processing より。Fig. 7-2, 7-7
</div>

## 大細胞系と小細胞系の区別と視覚経験の成立

<div class="figcenter">
<img src="/2025assets/1987LivingstoneHubel_tab2.svg" style="width:66%;">
<img src="/2025assets/1987LivingstoneHubel_tab7ja.svg" style="width:88%;">>
</div>

<div class="figcenter">
<img src="/2025assets/1988Livingstone_Hubel_fig2.jpeg" style="width:22%;">
<img src="/2025assets/1988Livingstone_Hubel_fig3.svg" style="width:44%;">
</div>

## 従来モデルと深層学習との対比

<div class="figcenter">
<img src='/assets/2013LeCun-tutorial-icml_15.svg' style="width:66%"><br/>

LeCun (2013)
</div>

我々人間は，外界を認識するために必要な計算を，生物種としての発生の過程と，個人の発達を通しての経験に基づく認識系を保持していると見ることができる。
従って我々の視覚認識には化石時代に始まる光の受容器としての眼の進化の歴史と発達を通じた個人の視覚経験が反映された結果でもある。
人工知能の目標は，この複雑な特徴検出過程をどうやったらコンピュータが獲得できるかということでもある。
外界を認識するために今日まで考案されてきたモデル（例えば，ニューラルネットワーク，サポートベクターマシンなどは）は複雑である。
ですがモデルを訓練するための学習方法はそれほど難しくない。
この意味で画像認識課題が正しく動作するためのポイントは，認識系が問題を解く事が可能なほど複雑であるかどうかではなく，十分に複雑が視覚環境，すなわち画像認識の場合，外部の艦橋を反映するために十分な量の像データを容易すことができるか否かにある。
今日の CNN による画像認識性能の向上は，簡単な計算方法を用いて複雑な外部環境に適応できる認識系を構築する方法が確立したからであると言うことが可能であろう。

下図 <!--[fig:2012Ng_01](#fig:2012Ng_01){reference-type="ref"reference="fig:2012Ng_01"} -->
に画像処理の例を挙げた。

<center>
<img src="/assets/2012Ng_ML_and_AI_01.png" style="width:66%">
</center>


### ワン・アルゴリズム仮説 One algorithm hypothesis

Sur ら (1988) は，フェレット（西洋イタチ）の 聴覚信号と視覚信号との中継核，膝状体 で信号を入れ替える実験を行った。
すなわち，聴覚信号が視覚野へ入力され，逆に視覚信号が聴覚野への入力となるように外科手術を行った。
結果，本来聴覚信号を処理すべき聴覚野ニューロンでは，視覚刺激に応答する反応が観察され，
本来視覚信号を処理すべき視覚野ニューロンでは，聴覚刺激に応答する反応が観察された。

<div class="figcenter">
<img src="/assets/1988Sur_Fig1upper.svg" style="width:34%">
<img src="/assets/1988Sur_Fig1lower.svg" style="width:34%"><br/>
<div class="figcaption">

図 1. フェレットの聴覚系への視覚投射を誘導するための実験デザイン。
(左) 正常な動物における投射。
網膜は LGN と上丘 (superior colliculus: SC) に投射する。
LGN は 皮質 17 野 (一次視覚野すなわち線条体皮質) と 18野, さらに 19 野と外側上絨毛皮質などの外延野に投射している。
聴覚系では 下丘 (Inferior colliculus: IC) が MGN に投射している。
MGNの腹側および背側部は一次聴覚野 (A1) に，また大脳皮質の前聴野 (anterior auditory field:AAF) および後聴野(posterior auditory field:PAF) を含む他の皮質領域にも大きく投射している (29)。
(下) フェレット新生児で皮質 17 野と 18 野を切除すると，逆行性変性により LGN は著しく萎縮する。
上丘も切除し，下丘を切除するか，下丘から上行する線維を切断して MGN を遠ざけると，網膜は MGN へ，ひいては聴覚野へ投射されるようになる。
(Sur,1988, Fig. 1)
<!-- Fig. 1. The experimental design for induction of visual projections to the auditory systetn in ferrets.
(Top) Projections in normal animals.
The retina projects to LGN and superior colliculus (SC).
The LGN projects to cortical areas 17 (primary visual cortex or striate cortex) and 18 as well as to other extrastriatc areas including area 19 and the lateral suprasylvian (LS) cortex.
In the auditory system, the inferior colliculus (IC) projects to the MGN.
The ventral and the dorsal division of the MGN project heavily to primary auditory cortex (Al), as well as to other cortical areas including the anterior auditory field (AAF) and the posterior auditory field (PAF) in cortex (29).
(Bottom) If cortical areas 17 and 18 are ablated in neonatal ferrets, the LGN atrophies severely by retrograde degeneration.
Ablating the superior colliculus as well, and deafferenting the MGN by ablating the inferior colliculus or sectioning fibers ascending from it, causes the retina to project to the M GN and hence to auditory cortex. -->
</div>
</div>

<div class="figcenter">
<img src="/assets/1988Sur_fig2.jpg" style="width:66%"><br/>
<div class="figcaption">

図 2. 実験的に誘導された視床聴覚部への網膜投射 (網掛け部分) と視床聴覚部と大脳皮質聴覚野の接続。
手術した半球の反対側の眼は，生き残った背側 LGN (LGd) と腹側 LGN (LGv)，および MGN の背側部と腹側部内のパッチ （それぞれ MGd とMGv) に投射を，視床の傍矢状断面図 (番号付き) で示す。
同じ動物で，一次聴覚皮質 (A1) (注入部位を左上に示す) に HRP を注入すると，MGv, MGd および後方複合体の外側分割 (PO1) の細胞 (点で示す) が逆行性に満たされた。
MGd と MGv の多くの細胞は網膜投射を覆っている。
Sur (1988) Fig. 2
<!-- Fig. 2. Experimentally induced retinal projections (hatched areas) to the auditory thalamus and the connections of auditory thalamus with auditory cortex.
The eye contralateral to the operated hemisphere projects to the surviving dorsal LGN (LGd) and ventral LGN (LGv) as well as to patches within the dorsal and ventral divisions of the MGN (MGd and MG" respectively).
Numbered parasagittal sections of the thalamus are shown.
In the same animal, an injection of HRP in primary auditory cortex (A1) (the injection site is shown at top left) fills cells (indicated by dots) retrogradely in MGv,  MGd, and the lateral division of the posterior complex (PO1).
Many cells in MGd and MGv overlie the retinal projection zone. -->
</div></div>


<div class="figcenter">
<img src="/assets/1988Sur_Fig4.svg" style="width:77%"><br/>
<div class="figcaption">

図 3. 手術動物と正常動物の視床の電気生理学的結果と，これらの無感覚症の視床に入力を与える網膜神経節細胞の解剖学的標識。
(A) 正常動物の LGN における X, Y, W 細胞の視交叉電気刺激後の発火潜時の分布。
ヒストグラムは 5 匹の動物からプールされた 107 個の細胞を含んでいる。
X 細胞と Y 細胞は A 層に存在し，C 層には Y 細胞と W 細胞が存在する(11)。
(B) 手術した動物の LGN には A 層と C 層に見られる細胞と，C 層に見られる W 細胞があるが，X 細胞は非常に少ない。
5 匹から 81 個の細胞をプーリングしたデータ。
(c) 手術した動物 (5 匹 94個) の MGN 内の細胞は，正常な動物の LGN 細胞に比べ，視交叉刺激に対する潜時が長い(A と同じデータ)。
(D) 正常動物と手術した動物の視床に HRP を注入し，逆行性に充填した網膜神経節細胞の細胞体サイズを示すヒストグラム。
正常動物への注入は LGN を中心とし，手術動物への注入は MGN を中心とした。
ヒストグラムの各バーは，逆行充填された細胞集団の総数に対する所定の大きさの怒張の神経節細胞の割合を示す。
正常なフェレットの視床への網膜入力 (18) は，α すなわち Y 様細胞 （これらは一般に細胞体サイズが 400 $\mu m^{2}$ 以上の大型 (L 細胞)，β すなわち X 様細胞 （一般に細胞体サイズが 300 から 400 $\mu m^2$ の中型 (M サイズ細胞)，および W 様細胞の異種集団 （このクラスには中型細胞も含みうるが一般に細胞体サイズが 300 $\mu m^2$ 未満の小型 (S 細胞) から生起する。
操作されたフェレットでは MGN に投射する細胞は主に小サイズの範囲にある。
<!-- Fig. 3. Electrophysiological results from the thal­amus of operated and normal animals and anatomical labeling of retinal ganglion cells that provide input to the thalamus in these aninuls.
(A) The distribution of the latencies of firing, after electrical stimulation of the optic chiasm, of X, Y, and W cells in the LGN of normal animals.
The histogram include 107 cells pooled from five animals.
X and Y cells are found in the A laminae, whereas the C laminae contain Y and W cells (11).
(B) The LGN of operated animals contains cells (found in the A and C laminae), along with W cells (found in the C laminae), but very few X cells.
lData are from 81 cells pooled from five animals.
(C) Cells in the MGN of operated animals (94 celss in five animals) have long latencies
to optic chiasm stimulation compared to cells in the LGN of normal aninmals [same data as in (A)].
(D) Histogram of soma sizes of retinal ganglion cells filled retrogradely from an HRP injection in the thalamus of a norrnal animal and an operated aninmal.
The injection in the normal animal was centered on the LGN, and the injection in the operated animal was centered on the MGN.
Each bar in the histogram represents the ganglion cells in a given size rage as a percentage of the total population of backfilled cells.
Retinal input to the thalamus in normal ferrets (18) arises from alpha or Y-like cells (These are, in general, large (L) cells with soma size of 400 mum^2 and larger), beta or X-like cells (generally medium (M)-sized cells with soma sizes between 300 and 400 mum^2), and a heterogeneous population of W-like cells (generallly small (S) cells with soma sized smaller than 300 mum^2, although this class can include medium-sized cells as well).
In operated ferrets, the cells that project to the MGN lie mainly in the small size range. -->

結果: Sur (1988) Fig. 4
</div></div>

<div class="figcenter">
<img src="/assets/1988Sur_fig4new.png" style="width:66%"><br/>
<div class="figcaption">

図4. 聴覚系に視覚投射を誘導した手術動物の一次聴覚野の視覚細胞の受容野と、正常動物の一次視覚野の受容野との比較。
細胞は Hubel と Wiesel の基準に従って無指向性，方位選択性，単純型，複雑型に分類された(21)。
単純細胞はオン(+) とオフ (-) のゾーンを持つ配向野を持つが，複雑細胞は通常オンとオフのゾーンを併せ持つ方位選択野を持つ。
(A) 正常動物の 17 野領域で記録された細胞。
フェレットの第 17 野の視覚空間地図 (30) と同様に，17 野の背側から腹側へ記録位置が移動するにつれて，受容野の位置は視野の高い位置に漸次移動する。
十字は領域中枢の位置を示す。
受容野内の小さな矢印は，最大反応をもたらす刺激移動の方向を示している。
各受容野の端から伸びている線は，端が止まっていないことを示す。
受容野の端で終端する線は終端停止野を示す。
(B）手術したフェレットの一次聴覚野では，視覚細胞は無方位性 (円形) または方位選択性 (長方形) のいずれかの受容野を有していた。
方位選択性野は複雑な形をしている。
視覚野では背側から腹側へ、聴覚野では後背側から前外側へ記録位置が移動するように，受容野が移動する。
(挿入）一次聴覚野の視覚細胞が，ヒストグラムの上に示した方向で受容野を横切るバーに対して反応したときの刺激周囲の時間ヒストグラム。
バー幅:1°, バー長:20°, 速度:5°/s, 50回 スイープ sps/s：spikes per second。
<!-- Fig. 4. Receptive fields of visual cells in primary auditory cortex of an operated animal with visual projections induced into the auditory system and co1nparison with receptive fields in primary visual cortex of a normal animal.
Cells were classified as nonoriented or oriented simple or complex according to the criteria of Hubel and Wiesel (21).
Simple cells have oriented fields with separate on (+) and off (-) zones, whereas complex cells have oriented fields usually with coextensive on and off zones.
(A) Cells recorded in area 17 of a normal animal.
Receptive field locations shifted progressively higher in the visual field as recording locations moved from dorsal to ventral in area 17, consistent with the map of visual spacee in area 17 in ferrets (3O).
The cross denotes the location of the area centrails.
Small arrows within the receptive field denote the direction of stimulus movement yielding maximal response.
Oriented line within each receptive field extending beyond receptive field edges denotes lack of end-stopping;
lines thar terminate at receptive field edges indicate end-stopped fields.
(B) In primary auditory cortex of an operated ferret, visual cells had either nonoricnted (circular) or oriented (rectangular) receprive fields.
The oriented fields were complex like.
Receptive fields moved from dorsal to ventral in the visual field as recording locations moved from posteromcdial to anterolateral in auditory cortex.
(Inset) Peristimulus time histogram of a visual cell in primary auditory cortex responding to a bar sweeping across the receptive field at the orientation and directions indicated above the histogram.
Bar width, 1°; bar length, 20°; velocity, 5°/s; 50 stimulus sweeps; sps/s, spikes per second. -->
</div></div>

#### 文献

- Metin and Frost (1989) Visual responses of neurons in somatosensory cortex of hamsters with experimentally induced retinal projections to somatosensory thalamus
- Roe et al. (1992) Visual Projections Routed to the Auditory Pathway in Ferrets: Receptive Fields of Visual Neurons in Primary Auditory Cortex


### ニューラル インプラント (neural implant), あるいは，義神経回路

* 人工内耳のように単に脳の活動を刺激するだけのものとは異なり、シリコンチップ製のインプラントは、損傷した脳の一部と同じプロセスを実行します。
* この人工器官は ラットの脳の組織でテストされました。次第に，人間に近い動物でのテストがなされています。
* 問題がなければ 脳卒中やてんかん，アルツハイマー病などで脳に損傷を受けた人の補助器具として実験が行われるでしょう。
* ですが，脳を模倣したデバイスは **倫理的な問題** を引き起こします。困っている人を助ける器具としては，義肢は有効な道具でしょう。しかし，その延長線上に義脳を考えることには，慎重な議論が必要だと考えます。

<div class="figcenter">
<img src="/2022assets/dn3488-1_602.jpg" width="44%">
<!-- <img src="http://www.newscientist.com/wp-content/uploads/2003/03/dn3488-1_602.jpg" width="44%"> -->
<img src="/assets/2001Berger_fig1.jpg" width="44%"><br/>
<div class="figcaption">

図 1.
左図: ラット脳 (左下)，左脳の海馬形成の相対的位置 (白)，脳から分離後の左海馬の図解(中央)，海馬の縦軸に横切る断面のスライス。

右図: 内嗅皮質 (ENTO) からの線維は穿通路 (pp) を通って歯状回 (DG)へ，歯状回の顆粒細胞は CA3 領域へ，さらに CA1 領域へ投射，CA1 細胞は小柱 (SUB)へ，そして無傷脳では内嗅皮質へ投射される。
スライス標本を作製すると CA1 と小室からの帰還結合が切断され，海馬ニューロンの実験的研究のための開ループ状態が作り出される。
<!-- Fig. 1. Left panel: Diagrammatic representation of the rat brain (lower left), showing the relative location of the hippocampal formation on the left side of the brain (white); diagrammatic representation of the left hippocampus after isolation from the brain (center), and slices of the hippocampus for sections transverse to the longitudinal axis.
Right panel: Diagrammatic representation of one transverse slice of hippocampus, illustrating its intrinsic organization: fibers from the entorhinal cortex (ENTO) project through perforant path (pp) to the dentate gyrus (DG); granule cells of the dentate gyrus project to the CA3 region, which in turn projects to the CA1 region; CA1 cells project to the subiculum (SUB), which in the intact brain then projects back to the entorhinal cortex. In a slice preparation, return connections from CA1 and the subiculum are transected, creating an open-loop condition for experimental study of hippocampal neurons. -->
</div></div>


<div class="figcenter">
<img src="/assets/2001Berger_fig3upper.jpg" width="88%"><br/>
<img src="/assets/2001Berger_fig3lower.jpg" width="44%">
<img src="/assets/2001Berger_fig13.jpg" width="33%"><br/>
<div class="figcaption">

図 3 (a) 従来の人工ニューラルネットワークの処理要素の性質と，生物学的にリアルな Dynamic Synapse ニューラルネットワークの処理要素の性質。
(b）Dynamic Synapse ニューラルネットワークによる話者非依存型単語認識識別の概念的表現。
ネットワークへの入力は，同じ単語に対する異なる話者のデジタル音声波形であり，話者の発声の違いにより，類似性が低い（相互相関が低い）。
2 つのネットワークは，2 つの異なる訓練またはテスト試行における同じネットワークを表すためのものであり，実際の場合では，1 つのネットワークが両方 (またはそれ以上) の音声波形で訓練されます。
このとき，各音声波形は 第 1 層にある 5 つの入力ユニットすべての入力を構成する。
このネットワークの第 1 層の各ユニットは，音声波形の異なるパルストレイン符号化を生成する (異なるパラメータ値を持つ「積分発火ニューロン」）。
各シナプス (矢印) の第 2 層への出力は 4 つの動的過程［( a) 参照］に支配され，そのうちの 2 つの過程は 2 次非線形性を表す。
したがって，第 2 層のニューロンへの出力は以前の入力事象からの時間に依存する。
「動的学習規則」は，異なる入力音声信号に応答して出力ニューロンが共通の時間パターンに収束するまで (すなわち出力パターン間の高い相互相関)，各動的処理過程の相対的寄与を変更する。
<!-- Fig. 3. (a) Properties of a processing element of a traditional artificial neural network versus properties of a processing element of a biologically realistic Dynamic Synapse neural network.
(b) Conceptual representation of speaker-independent word recognition identification by a Dynamic Synapse neural network.
Inputs to the network are digitized speech waveforms from different speakers for the same word, which have little similarity (low cross-correlation) because of differences in speaker vocalization.
The two networks shown are intended to represent the same network on two different training or testing trials; in a real case, one network is trained with both (or more) speech waveforms.
On any given trial, each speech waveform constitutes the input for all five of the input units shown in the first layer.
Each unit in the first layer of the network generates a different pulse-train encoding of the speech waveform (“integrate and fire neurons” with different parameter values).
The output of each synapse (arrows) to the second layer of the network is governed by four dynamic processes [see (a)], with two of those processes representing second-order nonlinearities; thus, the output to the second layer neurons depends on the time since prior input events.
A “dynamic learning rule” modifies the relative contribution of each dynamic process until the output neurons converge on a common temporal pattern in response to different input speech signals (i.e., high cross-correlation between the output patterns).
-->

図 13 失われた高次皮質脳領域の認知機能を代替するための埋め込み型神経補綴の概念図。
ここでは，海馬の一部を補綴する具体的なケースを想定して，その概念を示している。
この義補系の 2 つの重要な構成要素は，機能不全または失われた海馬の領域の計算機能を実行する「ニューロコンピューティング」マルチチップモジュールと，ニューロコンピューティングマイクロチップが無傷の脳からの入力を受け取り，無傷の脳に出力を送るためのニューロン-シリコンインターフェースとして機能する「ニューロモーフィック」マルチサイト電極アレイである。
<!-- Fig. 13 Conceptual representation of an implantable neural prosthetic for replacing lost cognitive function of higher cortical brain regions.
The concept is illustrated here in the context of the specific case of a prosthetic substituting for a portion of the hippocampus.
The two essential components of the prosthetic system are a “neurocomputational” multichip module that performs the computational functions of the dysfunctional or lost region of hippocampus, and a “neuromorphic” multisite electrode array that acts as a neuron-silicon interface to allow the neurocomputational microchips to both receive input from, and send output to, the intact brain. -->

出典: Berger (2001) 図 3, 図 13
</div></div>

## 教訓

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


