---
title: "The Roles of Supervised Machine Learning in Systems Neuroscience"
author: "Joshua I. Glaser and Ari S. Benjamin and Roozbeh Farhoodi and Konrad P. Kording"
layout: page
<!--layout: page-->
---

# The Roles of Supervised Machine Learning in Systems Neuroscience

## Abstract:

<!-- Over the last several years, the use of machine learning (ML) in neuroscience has been rapidly increasing. 
Here, we review ML’s contributions, both realized and potential, across several areas of systems neuroscience. 
We describe four primary roles of ML within neuroscience: 
1) creating solutions to engineering problems, 
2) identifying predictive variables, 
3) setting benchmarks for simple models of the brain, and 
4) serving itself as a model for the brain. 
The breadth and ease of its applicability suggests that machine learning should be in the toolbox of most systems neuroscientists. -->
ここ数年、神経科学分野における機械学習 (ML) の利用が急速に増えています。
ここでは、システム神経科学のいくつかの分野において、実現されたものと潜在的なものの両方で、ML の貢献をレビューします。
神経科学分野におけるMLの主な役割は4つあります。
1. 工学的な問題に対するソリューションの構築 
2. 予測変数の特定 
3. 脳の単純なモデルのベンチマークを設定する。
4. 脳のモデルとしての役割 

その適用範囲の広さと容易さは、機械学習がほとんどのシステム神経科学者のツールボックスに入るべきであることを示唆しています。


## はじめに:
<!-- There is a lot of enthusiasm about machine learning (ML). 
After all, it has allowed computers to surpass human-level performance at image classification (He et al. 2015)  to beat humans in complex games such as “Go” (Silver et al. 2016), and to provide high-quality speech to text (Hannun et al. 2014) in popular mobile phones. 
Progress in ML is also getting attention in the scientific community. 
Writing in the July 2017 issue of Science focusing on “AI Transforms Science”, editor Tim Appenzeller writes, “For scientists, prospects are mostly bright: AI promises to supercharge the process of discovery” (Appenzeller 2017) .
The field of systems neuroscience is no exception. 
In the last few years there have been many opinion pieces about the importance of ML in neuroscience (Vu et al. 2018; Barak 2017; Paninski and Cunningham 2017; Vogt 2018; Hinton 2011). 
Moreover, when we analyze the number of journal articles about ML in neuroscience, we find that its use has been continuously growing over the last 20 years (Fig. 1). 
Machine learning has been used in many different ways within this literature. 
In this review, we will catalog the conceptual applications of ML in systems neuroscience. -->
機械学習 (ML) には、多くの熱意が込められています。
何しろ、コンピュータが画像分類で人間レベルの性能を超えたり (He et al. 2015)、 「囲碁」などの複雑なゲームで人間を打ち負かしたり（Silver et al. 2016）, 人気のある携帯電話で高品質の音声合成を提供したり (Hannun et al. 2014) することが可能になったのですから。
ML の進歩は、科学界でも注目されています。
2017年 7 月号 の「Science」では 「AIが科学を変える」というテーマで 編集者のティム・アッペンツェラーが 「科学者にとって、見通しはほとんど明るい」 と書いています。
AI は発見のプロセスを超高速化することを約束する」と書いています (Appenzeller 2017)。

システム神経科学の分野も例外ではありません。
ここ数年、神経科学における ML の重要性を訴える意見書が多く出ています (Vu et al. 2018; Barak 2017; Paninski and Cunningham 2017; Vogt 2018; Hinton 2011)。
さらに、神経科学における ML に関するジャーナル記事の数を分析すると、過去 20 年間でその利用が継続的に増加していることがわかります (図1)。
この文献の中で、機械学習は様々な方法で使用されています。
このレビューでは、システム神経科学における ML の概念的な応用をカタログ化します。

<center>
	<img src="/assets/2019Glaser_fig1.jpg" width="66%"><br/>
<p align="left" style="width:77%">
<!-- Figure 1: Growth of Machine Learning in Neuroscience.
Here we plot the proportion of neuroscience papers that have used ML over the last two decades. 
That is, we calculate the number of papers involving both neuroscience and machine learning, normalized by the total number of neuroscience papers. 
Neuroscience papers were identified using a search for “neuroscience” on Semantic Scholar. 
Papers involving neuroscience and machine learning were identified with a search for “machine learning” and “neuroscience” on Semantic Scholar.	-->
図1：神経科学における機械学習の成長。
ここでは、過去20年間にMLを使用した神経科学の論文の割合をプロットしています。
つまり、神経科学と機械学習の両方を含む論文の数を、神経科学論文の総数で正規化して計算しています。
神経科学分野の論文は Semantic Scholar で "neuroscience" を検索して特定しました。
神経科学と機械学習を含む論文は、Semantic Scholarで "machine learning" と "neuroscience" を検索して特定しました。
</p>
</center>

<!-- On the highest level, ML is typically divided into the subtypes of supervised, unsupervised, and reinforcement learning. 
Supervised learning builds a model that predicts outputs from input data. 
Unsupervised learning is concerned with finding structure in data, e.g. clustering, dimensionality reduction, and compression. 
Reinforcement learning allows a system to learn the best actions based on the reward that occurs at an end of a sequence of actions. 
This review focuses on supervised learning. -->
ML は一般的に、教師あり学習、教師なし学習、強化学習というサブタイプに分けられます。
教師付き学習は、入力データから出力を予測するモデルを構築します。
教師なし学習は、クラスタリング、次元削減、圧縮など、データの構造を見つけることを目的としています。
強化学習は，一連の行動の最後に発生する報酬に基づいて，システムが最適な行動を学習するものである。
このレビューでは，教師付き学習に焦点を当てています．

<!-- Why is creating progressively more accurate regression or classification methods (see Box 1) worthy of a title like ‘The AI Revolution’ (Appenzeller 2017)? 
It is because countless questions can be framed in this manner. 
When classifying images, an input picture can be used to predict the object in the picture. 
When playing a game, the setup of the board (input) can be used to predict an optimal move (output). 
When texting on our smartphones, our current text is used to create suggestions of the next word. 
Similarly, science has many instances where we desire to make predictions from measured data. -->
なぜ、徐々に精度の高い回帰法や分類法 (ボックス1参照) を作ることが、 「AI革命」 (Appenzeller, 2017) のようなタイトルに値するのでしょうか。
それは、無数の質問がこの方法でフレーム化できるからです。
画像を分類するときには、入力された写真を使って、その写真に写っている物体を予測することができます。
ゲームをするとき、盤面の設定 (入力) から、最適な手 (出力) を予測することができます。
スマートフォンでメールを打つときには、現在の文章から次の単語の候補を導き出します。
同じように、科学の世界でも、計測したデータから予測したいと思うことがたくさんあります。


<!-- In this review, we categorize the ways in which supervised ML promises to assist, or has already been applied to, problems in systems neuroscience. 
We believe that applications of supervised ML in this field can be divided in roughly four categories (Fig. 2). 
* 1) Solving engineering problems. Machine learning can improve the predictive performance of methods used by neuroscientists, such as medical diagnostics, brain-computer interfaces, and research tools. 
* 2) Identifying predictive variables . Machine learning can more accurately determine whether variables (e.g., those related to the brain and outside world) predict each other. 
* 3) Benchmarking simple models . We can compare the performance of simple interpretable models to highly accurate ML models in order to help determine the quality of the simple models. 
* 4) Serving as a model for the brain. We can argue whether the brain solves problems in a similar way to ML systems, e.g. deep neural networks. 
The logic behind each of these applications is rather distinct.
 -->
このレビューでは，システム神経科学の問題に対して，教師付きMLがどのように役立つか，あるいはすでに適用されているかを分類しています．
この分野でのスーパーバイズドMLの応用は、大きく 4 つのカテゴリーに分けられると考えています（図2）。
1. **工学的問題の解決**。機械学習は、医療診断、ブレインコンピュータインターフェース、研究ツールなど、神経科学者が使用する手法の予測性能を向上させることができます。
2. **予測変数の特定** 機械学習により、脳や外界に関連する変数が互いに予測しあっているかどうかをより正確に判断することができる。
3. **単純なモデルのベンチマーク**  解釈可能なシンプルなモデルと精度の高いMLモデルの性能を比較することで、シンプルなモデルの品質を判断するのに役立つ。
4. **脳のモデルとしての役割** 脳が ML システム、例えばディープニューラルネットワークと同様の方法で問題を解決するかどうかを論じることができます。
これらのアプリケーションの背後にあるロジックは、どちらかというと異なるものです。

<center>
	<img src="/assets/2019Glaser_fig2.jpg" width="66%"><br/>
<p align="left" style="width:77%">
<!-- Figure 2: Examples of the four roles of supervised machine learning in neuroscience. 
1 - ML can solve engineering problems . For example, it can help researchers control a prosthetic limb using brain activity. 
2 - ML can identify predictive variables . For example, by using MRI data, we can identify which brain regions are most predictive for diagnosing Alzheimer’s disease (Lebedev et al. 2014) . 
3 - ML can benchmark simple models . For example, we can compare the predictive performance of the simple “population vector” model of how neural activity relates to movement (Georgopoulos, Schwartz, and Kettner 1986) to a ML benchmark (e.g. an RNN). 
4 - ML can serve as a model of the brain . 
For example, researchers have studied how neurons in the visual pathway correspond to units in an artificial network that is trained to classify images (Yamins and DiCarlo 2016). -->
図2: 神経科学における教師付き機械学習の4つの役割の例. 
1. ML は工学的な問題を解決することができます。例えば，脳活動を利用して義肢を制御することができる．
2. 予測可能な変数の特定 例えば、MRIデータを用いて、アルツハイマー病の診断に最も予測的な脳領域を特定することができます (Lebedev et al. 2014)。
3. ML は単純なモデルをベンチマークすることができる。例えば、神経活動と運動の関係を示す単純な「人口ベクトル」モデル（Georgopoulos, Schwartz, and Kettner 1986）の予測性能を、MLベンチマーク  (RNNなど) と比較することができます。
4 - MLは，脳のモデルとしても使える． 
例えば、研究者は、視覚経路のニューロンが、画像を分類するように訓練された人工ネットワークのユニットにどのように対応するかを研究しています (Yamins and DiCarlo 2016)。
</p>
</center>

----
<!-- # Role 1: Solving engineering problems
A surprisingly wide array of engineering problems can be cast as prediction problems. 
Their common thread is that one would like to estimate some quantity of interest (Y) and can take measurements (X) that relate to that quantity. 
The relationship between X and Y, however, is unknown and might be complicated. 
We call these ‘engineering problems’ when the final quantity, Y, is all that is desired. 
In these problems, one does not need detailed understanding of the relationship - the aim is simply to estimate Y as accurately as possible. 
For example, email providers wish to filter spam from incoming messages, and only care about how accurately the emails are sorted. -->
## 役割1: 工学的な問題を解決する
工学的な問題の中には、驚くほど幅広いものが予測問題として挙げられます。
共通しているのは、興味のある量（Y）を推定したいということと、その量に関連する測定値（X）を取ることができるということです。
しかし、XとYの関係は未知であり、複雑かもしれません。
このように、最終的な量であるYが得られればよい場合を「工学的問題」と呼んでいます。
このような問題では、関係を詳しく理解する必要はなく、単にYをできるだけ正確に推定することが目的となります。
例えば、電子メールプロバイダは、受信メッセージからスパムをフィルタリングしたいと考えていますが、気になるのは電子メールがどれだけ正確にソートされるかということだけです。

<!-- Traditionally, one would attempt to carefully understand the relationship between X and Y, and synthesize this into a model. 
Modern machine learning (ML) is changing this paradigm. 
Instead of detailed expert knowledge of a process, a practitioner simply needs a large database of measurements along with the associated quantity of interest for each measurement. 
Machine learning algorithms can then automatically model their relationship. Once trained, an ML algorithm can make predictions for new measurements. -->
従来は、XとYの関係を注意深く理解し、それをモデルに合成しようとしていました。
しかし、最新の機械学習（ML）はこのパラダイムを変えつつあります。
プロセスに関する詳細な専門知識がなくても、実務者が必要とするのは、測定値の大規模なデータベースと、各測定値に関連する関心事の量だけです。
機械学習アルゴリズムは、それらの関係を自動的にモデル化します。一度学習させれば、MLアルゴリズムは新しい測定値を予測することができます。

<!-- This ‘engineering’ framework is the traditional application of ML and is common in industry. 
In neuroscience, there are many problems that resemble this general problem format. -->
この「エンジニアリング」の枠組みは、ML の伝統的なアプリケーションであり、産業界では一般的なものです。
脳科学の分野では、この一般的な問題形式に似た問題がたくさんあります。

<!-- ## Neural Activity / Function
Many medical applications depend on successfully extracting information about intention, sensation, or disease from measurements of neural activity. 
This is a difficult problem, since the meaning of neural activity, the ‘neural code’, is most often not known. 
Machine learning is now a ubiquitous tool for this task in situations in which it is possible to obtain large datasets of neural activity along with the behaviors or diseases of interest. 
One such application is brain-computer interfaces (BCIs), which seek to use neural signals to control prosthetic limbs, computer cursors, or other external objects. 
Several groups have used modern ML techniques, such as recurrent neural networks, to improve BCIs using recordings of spikes (Sussillo et al. 2016, 2012), ECoG (Elango et al. 2017), or EEG (Bashivan et al. 2015). 
Machine learning can also be used to predict future neural activity from past neural activity. 
This application is relevant for epilepsy, since imminent seizures can be predicted using deep learning (Talathi 2017; Nigam and Graupe 2004) and ensemble methods (Brinkmann et al. 2016). 
In another line of applications, researchers have used ML to diagnose neurological conditions from activity. 
Several reviews on this specific application have recently been published (see (Arbabshirani et al. 2017) for classification using neuroimaging data, (Rathore et al. 2017) for classification of Alzheimer’s disease, and (Vieira, Pinaya, and Mechelli 2017) for a focus on deep learning approaches). 
Due to the large datasets available for neural recordings, ML has improved the standards of accuracy on these medical applications despite the complexity of the input signals. -->
### 神経活動/機能
多くの医療アプリケーションは、神経活動の測定値から意図、感覚、または病気に関する情報をうまく抽出することに依存しています。
しかし、神経活動の意味、すなわち「神経コード」はほとんどの場合知られていないので、これは難しい問題です。
機械学習は、神経活動の大規模なデータセットが得られる状況では、この課題のためのユビキタスなツールとなっている。
このようなアプリケーションの 1 つに、ブレイン・コンピュータ・インターフェース (BCI) がある。
BCIは、神経信号を使って義肢やコンピュータのカーソルなどの外部機器を制御しようとするものである。
いくつかのグループは、スパイク (Sussilloら 2016,2012), ECoG (Elangoら, 2017), または EEG (Bashivanら, 2015) の記録を用いて、リカレントニューラルネットワークなどの最新のML技術を使用して BCI を改善している。
機械学習は、過去の神経活動から将来の神経活動を予測するためにも使用できます。
深層学習 (Talathi, 2017; Nigam and Graupe 2004) やアンサンブル法 (Brinkmann et al., 2016) を用いて切迫した発作を予測することができるため、この応用はてんかんに関連している。
別の応用分野では、研究者はMLを使って活動から神経学的な状態を診断しています。
この特定のアプリケーションに関するいくつかのレビューが最近発表されています (神経画像データを用いた分類については Arbabshirani et al., 2017), アルツハイマー病の分類については (Rathore et al., 2017), 深層学習アプローチに焦点を当てたものについては (Vieira, Pinaya, and Mechelli, 2017 を参照)。
神経記録に利用できる大規模なデータセットがあるため、MLは、入力信号の複雑さにもかかわらず、これらの医療アプリケーションの精度の基準を向上させました。

<!-- An ML approach also promises to assist with the inverse of the above problem: predicting neural activity from variables in the outside world. 
Solving this problem is important if we want to use neural stimulation to induce accurate sensation. 
A prosthetic eye, for example, could be built by stimulating retinal ganglion cells in the correct manner according to the output of a camera (Nirenberg and Pandarinath 2012). 
The most accurate model of ganglion cell activity is currently a deep learning model trained to predict activity from naturalistic scenes (McIntosh et al. 2016). 
Similarly, prosthetic limbs could provide tactile and proprioceptive sensations if somatosensory neurons were correctly stimulated (Armenta Salas et al. 2018). 
Machine learning models may help to enable these neural prosthetics to induce sensations. -->
ML のアプローチは、上記の問題の逆の問題、つまり外界の変数から神経活動を予測することにも役立つと期待されています。
この問題を解決することは、神経刺激を用いて正確な感覚を誘発するためには重要です。
例えば、カメラの出力に応じて網膜の神経節細胞を正しい方法で刺激することで、義眼を作ることができる (Nirenberg and Pandarinath, 2012)。
現在、神経節細胞の活動の最も正確なモデルは、自然なシーンから活動を予測するように訓練された深層学習モデルである (McIntosh et al., 2016)。
同様に、義肢は、体性感覚ニューロンが正しく刺激されれば、触覚と固有感覚を提供することができます (Armenta Salas et al., 2018)。
機械学習モデルは、これらの神経義肢が感覚を誘発することを可能にするのに役立つかもしれない。

<!-- A very similar approach can be used to quantify behavior (D. J. Anderson and Perona 2014), such as movement, sleeping, and socializing. 
For example, we may want to quantify movement of the whole body using cheap video recordings. 
Recent progress in the field has made video quantification far more precise. 
Researchers have used deep learning to estimate human poses from video (Insafutdinov et al. 2016). 
Related approaches have recently gotten easier to use and less data intensive, and have been extended to animal tracking (Mathis et al. 2018; T. Pereira et al. 2018). 
Along with estimating poses, we can also directly estimate types of behavior (e.g., walking vs. stopping vs. jumping) from video (Kabra et al. 2013). 
Behavior can also be estimated based on other modalities such as audio recordings (Arthur et al. 2013). 
This progress in ML-based behavior tracking is timely, given recent calls to understand neural control of more naturalistic behavior in more natural environments (Krakauer et al. 2017). -->
非常に似たアプローチは、移動、睡眠、社会性などの行動を定量化するためにも使用できます (D. J. Anderson and Perona 2014)。
例えば、安価なビデオ録画を使って全身の動きを定量化したい場合があります。
近年のこの分野の進歩により、動画の定量化ははるかに正確になりました。
研究者たちは、深層学習を用いて、動画から人間のポーズを推定している (Insafutdinov et al.2016)。
関連するアプローチは、最近では使いやすくなり、データ量も少なくなり、動物追跡にも拡張されています (Mathis et al. 2018; T. Pereira et al., 2018)。
ポーズの推定とともに、映像から行動の種類 (例えば、歩く vs 止まる vs 跳ぶ) を直接推定することもできる (Kabra et al. 2013)。
また、音声記録などの他のモダリティに基づいて行動を推定することもできる (Arthur et al.  2013)。
より自然な環境におけるより自然な行動の神経制御を理解することが最近求められていることを考えると、ML ベースの行動追跡におけるこのような進歩はタイムリーである (Krakuer et al.2017)。

<!-- The engineering approach of applying ML is also helping solve the problem of obtaining accurate estimates of neural activity from raw measurements. 
Many imaging methods, such as EEG, MEG, and fMRI, require the solving of an ‘inverse problem’ – obtaining the source from the measurements. 
For example, researchers estimate the origin of EEG signals within the brain based on electrode recordings from the scalp. 
Recently, it has been observed that deep learning can improve the estimates for imaging (McCann, Jin, and Unser 2017). 
Neural networks have improved image denoising (Burger, Schuler, and Harmeling 2012; Xie, Xu, and Chen 2012) and deconvolution (L. Xu et al. 2014), can provide super-resolution images (Dong
et al. 2016), and can even replace the entire image processing pipeline (Golkov et al. 2016; Vito et al. 2005). 
Outside of imaging, the deconvolution of time series data is another common application. 
For example, once a researcher has obtained traces of cellular calcium concentration, there is still the difficult ‘inverse problem’ of inferring the timing of the underlying spiking. 
Competition-style ML on labeled datasets (Theis et al. 2016) provides good solutions (Berens et al. 2017). 
In each of these applications, a difficult engineering problem was replaced by building a large labeled dataset and using ML to learn the desired relationship. -->
ML を応用した工学的アプローチは、生の測定値から神経活動の正確な推定値を得るという問題の解決にも役立っています。
EEG, MEG, fMRI などのイメージング手法の多くは、測定値からソースを得るという「逆問題」の解決を必要とします。
例えば、研究者は、頭皮からの電極記録に基づいて、脳内のEEG信号の起源を推定します。
最近では、深層学習によってイメージングのための推定値を改善できることが観察されている (McCann, Jin, and Unser 2017)。
ニューラルネットワークは、画像のノイズ除去 (Burger, Schuler, and Harmeling 2012; Xie, Xu, and Chen 2012) やデコンボリューション（L. Xu et al. 2014) を改善し、超解像画像を提供できる (Dong
et al., 2016), さらには画像処理パイプライン全体を置き換えることも可能です (Golkov et al., 2016; Vito et al., 2005)。
画像処理以外では、時系列データのデコンボリューションも一般的なアプリケーションです。
例えば、研究者が細胞内のカルシウム濃度の痕跡を得たとしても、根底にあるスパイクのタイミングを推測するという難しい「逆問題」が残っています。
ラベル付きデータセットでの競争型 ML (Theis et al., 2016) は良い解決策を提供する (Berens et al., 2017)。
これらのアプリケーションのいずれにおいても、難しい工学的問題は、大規模なラベル付きデータセットを構築し、ML を使って望ましい関係を学習することで置き換えられました。

<!-- ## Neuroanatomy / Structure
Just as neural activity can be indicative of disease, so can neuroanatomy. As such, it is often possible to take anatomical measurements and use machine learning to diagnose disease. 
For example, researchers can distinguish between Alzheimer's disease and healthy brains of older adults using MRI scans (Sarraf, Tofighi, and Others 2016). 
More generally, neuroanatomical measurements such as structural MRI and diffusion tensor imaging (DTI) can distinguish healthy from unhealthy patients across many conditions including schizophrenia, depression, autism and ADHD (Arbabshirani et al. 2017; Rathore et al. 2017; Vieira, Pinaya, and Mechelli 2017).
Sometimes, ML enables surprising opportunities. 
For example, using deep convolutional neural networks, we can surprisingly predict cardiovascular risk factors from retinal fundus photographs (Poplin et al. 2018). 
The future will undoubtedly see ongoing efforts to automatically detect disease from biological data. -->

### 神経解剖学/構造
神経活動が病気の兆候を示すことがあるように、神経解剖学的にもそうである。そのため、解剖学的な計測を行い、機械学習を用いて病気を診断することが可能な場合があります。
例えば、高齢者のアルツハイマー病と健康な脳を MRI スキャンで区別することができます (Sarraf, Tofighi, and Others 2016)。
より一般的には、構造的MRIや拡散テンソル画像 (DTI) などの神経解剖学的測定により、 統合失調症、う つ病、 自閉症、 ADHD を含む多くの疾患において、健康な患者と不健康な患者を区別することができます (Arbabshirani ほか2017, Rathore ほか, 2017, Vieira, Pinaya, and Mechelli 2017)。
ML が意外な機会を可能にすることもあります。
例えば、深層畳み込みニューラルネットワークを用いて、網膜眼底写真から心血管危険因子を驚くほど予測することができます (Poplin et al.2018)。
将来的には、生物学的データから病気を自動的に検出する取り組みが継続的に行われることは間違いありません。


<!-- Since the majority of research in neuroanatomy is based on imaging techniques, recent advances in computer vision using ML are becoming important tools for neuroanatomy. 
Thus, segmenting and labeling parts of an image, which usually requires manual annotation, is an especially important task. However, as imaging techniques improve and the volume of data increases, it will become infeasible to rely on manual annotation. To solve this problem, many ML techniques have been developed to automatically segment or label new images based on a dataset of previously labeled images. 
The vast majority of techniques in this developing literature are based, at least in part, on convolutional neural networks (Litjens et al. 2017; Ronneberger, Fischer, and Brox 2015). 
This approach has been employed to label medical images, such as in identifying white matter tracts from MRI scans (Ghafoorian et al., 2017). 
They have also been used to understand the connections and morphologies of neurons from electron microscopy (Helmstaedter et al., 2013; Funke et al., 2017; Turaga et al., 2010). 
As imaging data improve in resolution and volume, ML is becoming a crucial and even necessary tool for reconstructing and mapping neuroanatomy. -->
神経解剖学の研究の大部分は画像処理技術に基づいているため、近年のMLを用いたコンピュータビジョンの進歩は神経解剖学にとって重要なツールとなりつつあります。
そのため、通常は手作業での注釈付けが必要な画像の部分的な分割とラベル付けは、特に重要な作業となります。
しかし、画像処理技術の向上やデータ量の増加に伴い、人手によるアノテーションに頼ることは不可能になってきています。
この問題を解決するために、過去にラベル付けされた画像のデータセットに基づいて、新しい画像を自動的にセグメント化またはラベル付けする ML 技術が数多く開発されています。
この開発中の文献にある技術の大半は、少なくとも部分的には畳み込みニューラルネットワークに基づいている (Litjens et al.  2017)。
このアプローチは、MRI スキャンから白質路を識別する際など、医療画像のラベル付けに採用されてきた (Ghafoorian et al.2017)。
また、電子顕微鏡からニューロンの接続と形態を理解するためにも使用されている  (Helmstaedterら, 2013; Funkeら, 2017; Turaga ら, 2010)。
イメージングデータの解像度とボリュームが向上するにつれ、ML は神経解剖学を再構築してマッピングするための重要なツール、さらには必要なツールとなりつつある。

<!-- ## Caveats
While ML methods have been able to provide many engineering solutions, ML is not magic (Wolpert and Macready 1997). 
Several conditions must be met for an ML method to solve a problem successfully. -->
### 注意点
ML 手法は多くの工学的解決策を提供してきましたが，MLは魔法ではありません (Wolpert and Macready 1997)。
ML の手法で問題を解決するためには，いくつかの条件を満たす必要があります．

<!-- A first consideration is that the selected method must match the structure of the data. 
For example, convolutional neural networks make the assumption that images have common local features (like edges), which allows them to be more successful than standard feedforward neural networks. 
In practice, this means that a user of ML must take care to select their method, or alternatively to preprocess their data, such that the assumptions match how the inputs relate to outputs.
This requires good knowledge of the specifics of the data and also of ML methods. 
A workaround to this is to apply automated ML methods, which iterate intelligently through many possible model configurations and select the best-performing option (Guyon et al. 2015; Elsken,
Metzen, and Hutter 2018; Feurer et al. 2015; Kotthoff et al. 2017). 
This approach is slow but often works comparatively well. 
The general rule, however, is that good ML engineering requires a good awareness of the data. -->
まず考えられるのは、選択した手法がデータの構造にマッチしていることです。
例えば、畳み込みニューラルネットワークは、画像にはエッジのような共通の局所的な特徴があると仮定しているため、標準的なフィードフォワードニューラルネットワークよりも成功率が高くなっています。
実際には，ML の利用者は，入力と出力の関係が前提条件と一致するように，手法を選択するか，あるいはデータを前処理するか，注意しなければなりません，ということです。
このためには、データの詳細とMLの手法についての知識が必要です。
これを回避するには、自動化されたML手法を適用することです。自動化された ML 手法は、多くの可能なモデル構成をインテリジェントに反復し、最良の性能を持つオプションを選択します (Guyon et al, Metzen, and Hutter 2018; Feurer et al.2015; Kotthoff et al.2017)。
このアプローチは時間がかかりますが、比較的うまくいくことが多いです。
しかし、一般的には、優れたMLエンジニアリングには、データをよく認識することが必要です。

<!-- Another potential failure mode of ML is “overfitting” to the training data. 
Ideally, an ML method should accurately predict data it is not trained on. 
If a method learns to make accurate predictions on the training data but cannot generalize to new data, it is said to be overfit. 
To guard against the worry of overfitting, ML practitioners always report a model’s performance on a test set that the model has not been trained on. 
The capacity of a method to overfit to data can be lowered with regularization methods, which penalize the complexity of a model. 
Still, overfitting is especially worrisome for small datasets and complex models. 
While different methods have different sensitivities to the number of data points, all methods become less vulnerable to overfitting when datasets are large. 
Sometimes simpler methods may be better choices on small datasets, even if a more complex method could better express the underlying input/output relationship (if there was sufficient data). The risk of overfitting means that all ML practitioners must be aware of regularization techniques, their dataset size, and the importance of reporting accuracy on a test set not used for training. -->
ML のもう一つの潜在的な失敗モードは、学習データに対する「オーバーフィッティング」です。
ML の手法は、学習していないデータを正確に予測するのが理想的です。
学習データに対して正確な予測ができるようになっても、新しいデータに対して一般化できない場合、オーバーフィットと呼ばれます。
オーバーフィットの心配を避けるために，ML の専門家は，モデルが学習されていないテストセットでのモデルの性能を常に報告しています．
モデルの複雑さにペナルティを課す正則化手法を用いることで、データへのオーバーフィットの可能性を低くすることができます。
しかし、オーバーフィットは、データセットが小さく、モデルが複雑な場合に特に問題となります。
データポイントの数に対する感度は手法によって異なりますが、どの手法もデータセットが大きくなるとオーバーフィッティングの影響を受けにくくなります。
データセットが小さい場合には、（十分なデータがあれば）より複雑な手法の方が基本的な入出力関係をよりよく表現できるとしても、より単純な手法の方が良い選択となることもある。オーバーフィッティングのリスクがあるということは、すべてのML関係者が正則化技術、データセットのサイズ、そしてトレーニングに使われていないテストセットでの精度を報告することの重要性を認識しなければならないということです。

<!-- 
Yet another practical drawback of ML is that it can be slow. 
For large datasets and complex models, the time it takes to train the model can be prohibitive without proper hardware, like GPUs for deep learning. 
Once a model is trained, however, it is much faster to make predictions. Still, for applications that require real-time predictions, even the prediction step may be too slow for some ML methods. 
For example, predictions for brain machine interfaces often need to be made in the timescale of tens of milliseconds, which can be a challenge for models requiring many computations. 
This tradeoff between complexity and run-time is an important aspect in choosing a model for many engineers. -->

さらに、ML のもう一つの実用的な欠点は、時間がかかることです。
大規模なデータセットや複雑なモデルの場合、ディープラーニング用の GPU のような適切なハードウェアがないと、モデルの学習にかかる時間が膨大になってしまいます。
しかし、いったんモデルが学習されれば、予測の速度は格段に向上します。
しかし、リアルタイムな予測を必要とするアプリケーションでは、ML の手法によっては、予測のステップでさえも遅すぎる場合があります。
例えば、ブレイン・マシン・インターフェースの予測は、数十ミリ秒のタイムスケールで行う必要がある場合が多く、多くの計算を必要とするモデルにとっては困難な場合があります。
<この複雑さと実行時間のトレードオフは、多くの技術者にとってモデルを選択する際の重要なポイントです。


---
<!-- # Role 2: Identifying predictive variables
Neuroscientists often ask questions of the form, “which variables are related to something of interest?” 
For example, which brain regions can predict each other? Which brain regions contain information related to a subject’s decision? Which cell types are affected by a certain disease?
Machine learning (ML) can help to more accurately identify how informative one set of variables is about another. 
This is particularly instructive when there is a complex nonlinear relationship between the variables, which is often the case in neural systems. Answering these types of questions allows researchers to better understand the relationship between parts of the brain, stimuli, behavior, and more.
 -->
## 役割2: 予測変数の特定
脳科学者は、"どの変数が興味のあることに関連しているか？" という形式の質問をよくします。
例えば、どの脳領域がお互いを予測できるのか？どの脳領域が被験者の意思決定に関連する情報を含んでいるのか？ある病気の影響を受けるのはどの細胞タイプか？
機械学習 (ML) は、ある変数セットが別の変数セットに対してどれだけ情報を与えているかをより正確に特定するのに役立ちます。
これは、神経系でよく見られるように、変数間に複雑な非線形関係がある場合に、特に有効です。このような質問に答えることで、研究者は、脳の一部、刺激、行動などの関係をより深く理解することができます。


<!-- The general strategy resembles that of the engineering applications (Role 1). 
However, instead of only searching for maximal predictive accuracy, one examines which input variables lead to that accuracy. 
There are many methods to establish so-called ‘feature importance’ (also known as ‘feature selection’). 
Two of the simplest are the leave-one-out strategy, in which each variable is removed and one observes the decrease in accuracy, and the ‘best first’ strategy, in
which the algorithm is run on each variable alone. 
Leave-one-out reflects the information in that variable but not the others, while best-first reflects the total (learnable) task information in each variable. 
Both are related but different definitions of what it means for a feature to be important. 
The development of feature importance measures is an active field in ML and statistics (Tang, Alelyani, and Liu 2014). 
These methods allow us to get insights into which variables are important for a given problem (with the specific meaning of ‘importance’ depending on the measure used). -->
一般的な戦略は、エンジニアリング・アプリケーションの場合と似ています (役割1)。
しかし，最大の予測精度だけを求めるのではなく，どの入力変数がその精度につながるかを検討する。
いわゆる「特徴の重要性」 (「特徴の選択」とも呼ばれる) を確立する方法は数多くある。
最も単純な方法は、各変数を削除して精度の低下を観察する「leave-one-out」戦略と、各変数に対してアルゴリズムを実行する「best first」戦略である。
各変数のみでアルゴリズムを実行します。
leave-one-out は、その変数の情報を反映しますが、他の変数は反映しません。
一方、best-first は、各変数に含まれる (学習可能な) タスク情報の合計を反映します。
両者は関連しているが、ある特徴が重要であることの意味については異なる定義である。
特徴の重要性測定法の開発は、MLや統計学において活発な分野です (Tang, Alelyani, and Liu 2014)。
これらの手法により、与えられた問題に対してどの変数が重要であるかという洞察を得ることができます (「重要性」の具体的な意味は、使用する尺度によって異なります)。

<!-- A more traditional approach for this type of question would be to fit simple models to data, like linear regression, and to examine the coefficients of the fit. 
This approach is ubiquitous in science. 
Its basic drawback, however, is that one needs to assume a model, which may be inaccurate. 
For example, if the model is assumed to be y = mx+b, but the true relationship is y = cos x, then the value of m (the “interaction between x and y”) will be 0 despite there being a
strong relationship between x and y. 
The ML approach, on the other hand, seeks to maximize predictive accuracy and in doing so does not need to assume a simple functional form. 
This has the advantage that we can evaluate a variable’s importance even when the relationship between inputs and outputs is unknown and possibly nonlinear. 
Plus, by bootstrapping, we can even find the confidence interval for their importance values. 
Machine learning combined with feature selection approaches can be universally applied to problems regardless of whether we know the underlying relationship. -->
この種の質問に対するより伝統的なアプローチは、線形回帰のような単純なモデルをデータにフィットさせ、フィットの係数を調べることです。
このアプローチは科学の世界では一般的なものです。
しかし、このアプローチの基本的な欠点は、モデルを仮定する必要があり、それが不正確である可能性があることです。
例えば、モデルを $y=mx+b$ と仮定しても、実際の関係が $y=\cos x$ であれば、 $x$ と $y$ の間に強い関係があるにもかかわらず、$m$ (「$x$ と $y$の間の相互作用」) の値は 0 になります。
一方，ML アプローチは，予測精度の最大化を目指しており，そのために単純な関数形を仮定する必要はありません。
これにより、入力と出力の関係が未知で、非線形の可能性がある場合でも、変数の重要性を評価できるという利点があります。
さらに、ブートストラップにより、重要性の値の信頼区間を求めることもできます。
機械学習と特徴選択アプローチの組み合わせは、根本的な関係が分かっているかどうかに関わらず、問題に普遍的に適用することができます。


<!-- Determining the important features can also help us to construct simpler models. 
Rather than using many inputs for a model, we can only use the important features as inputs. 
For example, determining which morphological features of neurons are most predictive of cell type can lead us to build more accurate generative models of morphologies (that are based on the most predictive features). 
Accurately determining the importance of features within ML algorithms is thus also beneficial for creating simpler models. -->
また、重要な機能を決定することで、よりシンプルなモデルを構築することができます。
モデルに多くの入力を用いるのではなく、重要な特徴のみを入力として用いることができるのです。
例えば、ニューロンの形態的特徴のうち、細胞の種類を予測するのに最も適したものを特定すれば、より正確な形態の生成モデル（最も予測性の高い特徴に基づいたモデル）を構築することができます。
このように、MLアルゴリズムにおいて特徴の重要性を正確に判断することは、よりシンプルなモデルを作成するのにも有効です。

<!-- This approach is designed to examine the same variables that serve as raw inputs into the ML model. 
Often the “features” we seek are different than the raw inputs. 
In vision, for example, the raw input variables may be as simple as single pixels, and the approach of Role 2 would then simply isolate the most relevant pixels. 
However, as we review below, many problems in neuroscience follow the format where the input variables are the variables of interest. -->
このアプローチは、ML モデルの生の入力として機能するのと同じ変数を調べるように設計されています。
しかし、私たちが求める「特徴」は、生の入力とは異なることがよくあります。
例えば、視覚の場合、生の入力変数は1つのピクセルのような単純なもので、「役割2」のアプローチでは、最も関連性の高いピクセルを分離するだけです。
しかし、以下で検討するように、神経科学の問題の多くは、入力変数が対象となる変数であるという形式をとっています。


やや飛ばして

----
<!-- ## Role 3: Benchmarking simple models
There are many uses of modeling in the biological sciences, and not all uses are satisfied by ML. 
In particular, many biophysical models embody specific hypotheses about a biological mechanism. 
The Hodgkin-Huxley model is a canonical model of this type, as the equation itself specifies how ion channel kinematics lead to spikes. 
Machine learning methods, on the other hand, aim primarily for prediction, and by and large do not automatically build mechanistic hypotheses of how the inputs relate to the outputs. 
Until methods for model interpretability progress, ML models cannot replace simpler models in this regard. -->
## 役割3: 単純なモデルのベンチマーク
生物科学におけるモデリングには様々な用途があり、すべての用途がMLで満たされるわけではありません。
特に、生物物理モデルの多くは、生物学的メカニズムに関する特定の仮説を具現化したものです。
Hodgkin-Huxley モデルはこのタイプの典型的なモデルで、イオンチャネルの運動性がスパイクにつながることを式自体が示しています。
一方、機械学習法は予測を主目的としており、入力と出力の関係についてのメカニズム仮説を自動的に構築することはほとんどありません。
モデルの解釈可能性を高める手法が進歩するまでは、機械学習モデルが単純なモデルに取って代わることはできません。

<!-- Simple, hypothesis-driven models are meaningful only to the extent that they are correct. 
One can easily check a model’s accuracy from its predictive performance (e.g. $R^2$), as is often done.
However, it is often hard to know how much error derives from sources of noise versus systematic insufficiencies of the model. 
This is where ML can help. 
It can serve as an approximate upper bound for how much structure in the data a simpler model should explain. 
If a human-generated model is much less accurate than ML methods trained on the same task, it is likely that important principles are missing. 
If, on the other hand, an intuitive model matches the performance of ML, it is more likely (but not guaranteed) that the posited concepts are, indeed, meaningful . Thus, we argue that if a hypothesis-driven model is to be trusted, then it must at least match ML methods trained on the same task. -->
単純な仮説に基づいたモデルは、それが正しいという範囲でのみ意味を持ちます。
モデルの精度は、その予測性能（例：$R^2$）から簡単に確認することができ、よく行われています。
しかし、どの程度の誤差がノイズの原因によるものなのか、モデルの系統的な不備によるものなのかを知ることは困難です。
ここで、MLが役に立ちます。
MLは、より単純なモデルでどれだけのデータの構造を説明できるか、そのおおよその上限を示すことができます。
人間が作成したモデルが、同じタスクで訓練されたMLメソッドよりもはるかに精度が低い場合、重要な原理が欠落している可能性があります。
一方、直感的なモデルがMLのパフォーマンスと一致した場合、仮定された概念が実際に意味のあるものである可能性が高くなります（保証されているわけではありません）。このように、仮説駆動型のモデルを信頼するには、少なくとも同じタスクで訓練されたMLの手法と一致しなければならないと主張しています。


<!-- This approach stands in contrast to the current paradigm of testing a model by comparing it with previous (simple) models. 
This comparison may be meaningless if both models are very far from the peak ML predictive performance. 
Even if a new model more accurately explains the data than previous models, it is possible that both models miss important phenomena. 
Without a change in paradigm, we run the risk of not recognizing predictable complexity when it exists.
Benchmarking with ML allows one to check against this trap. -->
このアプローチは、過去の（単純な）モデルと比較してモデルをテストするという現在のパラダイムとは対照的です。
この比較は、両方のモデルがMLの予測性能のピークから非常に離れている場合には意味がありません。
また、新しいモデルが以前のモデルよりも正確にデータを説明できたとしても、どちらのモデルも重要な現象を見逃している可能性があります。
パラダイムを変えないと、予測可能な複雑さがあってもそれを認識できない危険性があります。
MLを使ったベンチマークでは、この罠をチェックすることができます。


---
<!-- ## Role 4: Serving as a model for the brain
The role of computational models of the brain is not only to predict, but also to serve as human-understandable distillations of how we think the brain works. 
It has recently become a more popular idea that deep neural networks are good models of the brain, albeit at a high level of abstraction (Marblestone, Wayne, and Kording 2016; Hassabis et al. 2017; Kietzmann, McClure, and Kriegeskorte 2017). 
Even a decade ago, this idea seemed less appealing to the field given the hyper-simplified form of contemporary neural networks. However, numerous recent empirical studies have pointed to unexpected parallels between the brain and neural networks trained on behaviorally relevant tasks. 
Here we review these suggestive studies and discuss the variou s ways that artificial neural networks are becoming better models of biological ones. 
While exciting, much work is needed (and is ongoing) to evaluate the extent to which current neural networks are good models of the brain, and on what levels. 
We discuss neural activity and neuroanatomy without separation, as both aspects are often integrated together in ML models of the brain. 
In keeping with the theme of this review, we focus on reviewing work centered on supervised learning and omit other learning-based models of the brain like unsupervised learning or reinforcement learning.  -->
## 役割4: 脳のモデルとしての役割
脳の計算モデルの役割は、予測するだけではなく、脳がどのように機能しているかを人間が理解できるように蒸留して提供することです。
最近では、深層ニューラルネットワークは、抽象度が高いとはいえ、脳の良いモデルになるという考えが一般的になってきました (Marblestone, Wayne, and Kording 2016; Hassabis et al. 2017; Kietzmann, McClure, and Kriegeskorte 2017)。
10 年前でも、現代のニューラルネットワークが超単純化された形であることを考えると、このアイデアは現場ではあまり魅力的ではないように思えました。
しかし、最近の数多くの実証研究では、脳と、行動に関連するタスクで訓練されたニューラルネットワークとの間の予期せぬ類似性が指摘されている。
ここでは、これらの示唆的な研究をレビューし、人工的なニューラルネットワークが生物学的なもののよりよいモデルになりつつあるさまざまな方法について議論する。
しかし、現在のニューラルネットワークがどの程度まで脳の良いモデルになっているのか、また、どのようなレベルでモデルになっているのかを評価するには、多くの研究が必要であり、現在も進行中である。
ここでは、神経活動と神経解剖学を分けずに議論します。なぜなら、MLの脳モデルでは、この2つの側面がしばしば統合されているからです。
また、本レビューのテーマに沿って、教師あり学習を中心とした研究をレビューし、教師なし学習や強化学習などの他の学習ベースの脳のモデルは省略しています。