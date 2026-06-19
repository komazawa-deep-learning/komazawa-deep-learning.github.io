---
title: 第 09 回 2026 年度開講 心理学特講 IIIA 駒澤大学 
author: 浅川 伸一
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="center">
<font size="+1" color="navy"><strong>計算モデルによる課題の理解：認知課題から神経心理学検査への適用</strong></font><br/><br/>
</div>

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 19/Jun/2026<br/>
Appache 2.0 license<br/>
</div>

<!-- 
課題：以下の用語を最低一回は用いて，自分の考えを述べよ。（A4 用紙 1 枚程度）
1. ロゴジェンモデル
2. IAM （Interactive Activation Model）
3. DRC（Dual Route Cascaded）モデル
4. WAB（Western Aphasia Battery）
5. 失読症（surface dyslexia, phonological dyslexia）
6. DRC モデル
7. Triangle モデル -->

# 07440 心理学特講ⅢA - 第 09 回

* [課題提出フォルダ](https://drive.google.com/drive/u/6/folders/1wYaBn4dovEwtlOfOhcAFP2bJdyDqM9ZL){:target="_blank"}
<!-- * [実習コード <img src="/assets/colab_icon.svg">](){:target="_blank"} -->

<!-- https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2026notebooks/2026psy3a_lect07_iam_dell_model.ipynb){:target="_blank"}
 -->

<!-- 以下に、第7回の授業資料（Google Colaboratory用ノートブックおよび講義スライドの統合案）を提示する。学生の暗記主義を完全に破壊し、数理モデルを通じた神経心理学的症状の逆算を強制する設計としている。 -->

---

<!-- # 07440 心理学特講ⅢA - 第7回: 語彙アクセスのモデル化（局所表現とWABへの接続）

## 1. 授業の戦略的要件

本日の目的は、単語を読むという行為が「単一のブラックボックス」ではなく、複数の経路（カスケード）と階層間の相互作用によって成立している事実を、数理的に証明することである。
現象（例：単語優位効果や失読症）の名前を暗記することは一切評価しない。「ネットワークのどの行列（重み）が機能したか」、あるいは「どこが物理的に断線したか」というアーキテクチャの観点からのみ事象を語れ。 -->


### 三角モデル<!-- ## The Triangle Model-->

Seidenberg と McClelland（1989）が提唱した計算枠組みは三角モデルと呼ばれている（図 1）。このモデルは綴りから音への二つの経路を想定している。一つは書記表現から音韻表現への直接的な対応関係であり、もう一つは印字から音への対応関係で、これは単語の意味表現を介して行われる。
<!-- The computational framework described by Seidenberg and McClelland (1989) has been referred to as the triangle model (see Figure 1). The model assumes the existence of two pathways from spelling to sound: One pathway is a direct mapping from ortho-graphic to phonological representations, whereas the second path-way maps from print to sound by means of the representation of word meanings.  -->

<div class="figcenter">
<img src="/2026assets/2007Perry_CDP_fig1.png" width="33%;">
<div class="figcaption">

Figure 1. The triangle model. The part of the model implemented by Seidenberg and McClelland (1989) and also by Plaut et al. (1996) is shown in bold. From “A Distributed, Developmental Model of Word Recognition and Naming,” by M. S. Seidenberg and J. L. McClelland, 1989, Psychological Review, 96, p. 526. Copyright 1989 by the American Psychological Association. Adapted with permission.
</div>
</div>

Seidenberg と McClelland (1989) の先駆的研究では、直接的な書記から音韻への経路のみが実装された。このモデルでは、任意の単語または非単語の音韻は、単一過程によってその書記表象から計算される。この過程は、3 層ニューラルネットワークを通じた活性化伝播であり、入力素子と出力素子上の活性化パターンはそれぞれ、単語の書かれた形と音韻的形を表す。綴りと音の対応に関する知識はネットワーク内に分散され、処理素子を連結する接続部に存在する。
<!-- Only the direct orthography-to-phonology pathway was implemented in Seidenberg and McClelland’s (1989) seminal work. In the model, the phonology of any given word or nonword is computed from its orthographic representation by a single process. This process is the spread of activation through a three-layer neural network, where the activation patterns over input and output units represent the written and phonological form of the word, respectively. The knowledge about spelling–sound mappings is distributed in the network and resides in the connections that link the processing units. -->

誤差逆伝播学習アルゴリズムを用いて、約 3,000 語の単音節英語単語データセットでネットワークを訓練した（Rumelhart, Hinton, & Williams, 1986）。学習項目は、Kuc¸eraとFrancis（1967）の単語頻度基準を対数関数で反映した確率でネットワークに提示された。単語（および非単語）の書記・音韻的表現は、Wickelgren（1969）の三重構造スキームに従い、複数の原始的表現単位に分散した活性化パターンで構成された。このモデルは、正常な被験者の読解能力に関する様々な事実を説明できた。特に、単語頻度と綴音規則性との古典的な相互作用（例：Paap & Noel, 1991）を示した。



### DRC モデル<!-- ## The DRC Model-->

SeidenbergとMcClelland（1989）の単一経路モデルに対し、Coltheartらは（Coltheart et al., 1993, 2001; Coltheart & Rastle, 1994; Rastle & Coltheart, 1999; Ziegler, Perry, & Coltheart, 2000, 2003）は、二重経路理論の計算モデルを構築した。この DRC モデルでは、語彙経路と非語彙経路が、異なる表現的に独立した構成要素として実装されている（図 2）。さらに、二つの経路は異なる計算原理で動作する。非語彙経路では直列的・記号的処理が、語彙経路では並列的拡散活性化が行われる。
<!-- In response to the single-route model of Seidenberg and Mc-Clelland (1989), Coltheart and colleagues (Coltheart et al., 1993, 2001; Coltheart & Rastle, 1994; Rastle & Coltheart, 1999; Ziegler, Perry, & Coltheart, 2000, 2003) developed a computational im-plementation of the dual-route theory. In this model, known as DRC, lexical and nonlexical routes are implemented as different and representationally independent components (see Figure 2). Moreover, the two routes operate on different computational prin-ciples: serial, symbolic processing in the nonlexical route and parallel spreading activation in the lexical route. -->

<div class="figcenter">
<img src="/2026assets/2007Perry_CDP_fig2.png" width="33%;">

<div class="figcaption">

Figure 2. The dual-route cascaded model. The lexical–semantic route of the model is not implemented (dashed lines). From “Models of Reading Aloud: Dual-Route and Parallel-Distributed-Processing Approaches,” by M. Coltheart, B. Curtis, P. Atkins, and M. Haller, 1993, Psychological Review, 100, p. 214. Copyright 1993 by the American Psychological Association. Adapted with permission.
</div>
</div>

DRC の非語彙経路は、文字から音素への対応規則（GPC）を左から右への直列的順序で適用する。これは任意の文字列に適用可能であり、非単語の読解に必要である。語彙経路は、McClelland と Rumelhart（1981; Rumelhart & McClelland, 1982 参照）の単語認識モデルと、Dell（1986）の音声単語生成モデルに類似したものを組み合わせた相互活性化モデルとして実装され、並列カスケード処理によって動作する。処理は文字特徴レベルから始まり、活性化が文字、書記素的単語ノード（すなわち書記素的語彙）、音韻的単語ノード（すなわち音韻的語彙）、そして最終的に音韻的出力バッファ（すなわち音素体系）へと広がる。語彙経路は既知語の読解に使用され、例外語（不規則語とも呼ばれる）の正しい読解に必要である。不規則語／例外語は定義上、最も頻度の高い字母音対応（例：head と bead の ea の発音）に合致しない発音を持つ字母を少なくとも一つ含む。
<!-- The nonlexical route of DRC applies grapheme-to-phoneme correspondence (GPC) rules in a serial left-to-right manner; it can be used on any string of letters and is necessary for reading nonwords. The lexical route, which is implemented as an interac-tive activation model based on McClelland and Rumelhart’s (1981; see also Rumelhart & McClelland, 1982) word recognition model joined with something similar to Dell’s (1986) spoken word production model, operates by means of parallel cascaded process-ing. Processing starts at a letter feature level, and then activation spreads to letters, orthographic word nodes (i.e., an orthographic lexicon), phonological word nodes (i.e., a phonological lexicon), and finally a phonological output buffer (i.e., the phoneme system). The lexical route can be used to read known words and is neces-sary for the correct reading of exception words (also called irreg-ular words). Irregular/exception words contain, by definition, at least one grapheme pronounced in a way that does not conform to the most frequent grapheme–phoneme correspondences (e.g., the pronunciation of ea in head vs. bead). -->

このモデルが生み出す典型的な誤りの一つが「規則化誤り」である。この誤りは、例外語を処理する際に語彙経路が作動していない状態で非語彙経路が使用された場合に発生する。なぜなら非語彙経路は、最も典型的な文字音素関係のみを規定する規則を通じて音韻を生成するからだ。例えば pint という単語が提示された場合、非語彙経路は mint と韻を踏む発音を導き出す。通常、語彙経路と非語彙経路は処理中（単語処理でも非単語処理でも）常に相互作用する。しかし語彙経路は非語彙経路より高速に動作するため、非語彙経路が規則化された発音を導出しても、不規則語は通常（常にではないが）DRC によって正しく発音される。
<!--One common type of error produced by the model is known as a regularization error. This type of error occurs if the nonlexical route is used to read an exception word without the lexical route being on, because the nonlexical route generates phonology through rules that specify only the most typical grapheme–phoneme relationships. For example, the nonlexical route would generate a pronunciation that rhymes with mint when presented with the word pint. Normally, the lexical and nonlexical routes always interact during processing (whether during the processing of words or the processing of nonwords). However, the lexical route runs faster than the nonlexical route, which is why irregular words are usually (but not always) pronounced correctly by DRC, even though the nonlexical route generates a regularized pronunciation. -->

### CDP モデル<!-- ## The CDP Model-->

Zorzi ら（1998b）は、音読のコネクショニストモデルを開発した。このモデルでは、読解習得の過程において、課題要求と初期ネットワーク構造の相互作用から二重経路処理系が出現する。このモデルでは、音韻的組み立てと語彙知識の区別は、書記入力と音韻出力パターンの間の接続性（直接的または媒介的）の形で実現される（書き言葉における音-綴り対応の学習問題に関する類似の扱いは Houghton & Zorzi, 1998, 2003 参照）。したがって、このモデルは PDP モデル（すなわちコネクショニスト構造）の統一的な計算様式を維持しつつ、読解における語彙的過程と語彙下位過程を明確に区別している。
<!-- Zorzi et al. (1998b) developed a connectionist model of reading aloud where a dual-route processing system emerges from the interaction of task demands and initial network architecture in the course of reading acquisition. In this model, the distinction be-tween phonological assembly and lexical knowledge is realized in the form of connectivity (either direct or mediated) between orthographic input and phonological output patterns (see Houghton & Zorzi, 1998, 2003, for a similar treatment of the problem of learning the sound–spelling mapping in writing). The model thus maintains the uniform computational style of the PDP models (i.e., connectionist architecture) but makes a clear distinction between lexical and sublexical processes in reading. -->

<div class="figcenter"> 
<img src="/2026assets/2007Perry_CDP_fig3.svg" width="39%;">
<div class="figcaption">

Figure 3. The connectionist dual process model. From “Two Routes or One in Reading Aloud? A Connectionist Dual-Process Model,” by M. Zorzi, G. Houghton, and B. Butterworth, 1998, Journal of Experimental Psychology: Human Perception and Performance, 24, p. 1150. Copyright 1998 by the American Psychological Association. Adapted with permission.
</div></div>


Zorzi et al. (1998b) は、書記と音韻の対応関係を学習するように訓練された完全並列の単純な二層連想ネットワーク（隠れ素子を持たないネットワーク）の性能を詳細に研究した。Zorzi et al. は、このネットワークが音韻的組み立て過程の特徴と見なされる性質を獲得することを発見した。特に、音韻構成の二層ネットワーク（TLA ネットワーク）は、個々の訓練項目（例外語など）の表現を形成することなく、英語における統計的に最も信頼性の高い綴り-音の関係を抽出できることを示した（この能力の発達的研究については Zorzi, Houghton, & Butterworth, 1998a 参照）。したがって、この二層連合ネットワークは（入力語が例外語である場合）規則化された発音を生成し、訓練語の基礎語頻度にあまり敏感ではない。しかしながら、複数の粒度（文字から語幹まで）における綴り-音関係の統計的一貫性には非常に敏感であり、これは同一音節位置（特に母音）における代替音素候補の活性化に反映される。モデルの最終発音は、命名潜時に影響する因果的要因である活性化競合に基づき、音韻決定系（すなわち音韻出力バッファ）によって生成される。このモデルは人間被験者の非単語読解能力と合理的に一致し、単一文字・複数文字の形態素(グラフェム)も読み上げ可能である。
<!-- Zorzi et al. (1998b) studied in great detail the performance of a fully parallel simple two-layer associative network (i.e., a network without hidden units) trained to learn the mapping between or-thography and phonology. Zorzi et al. found that this network acquired properties that are considered the hallmark of a phonological assembly process. In particular, Zorzi et al. showed that the two-layer network of phonological assembly (TLA network) was able to extract the statistically most reliable spelling–sound relationships in English (see also Zorzi, Houghton, & Butterworth, 1998a, for a developmental study of this capacity), without forming representations of the individual training items (such as the exception words). Therefore, the two-layer associative network produces regularized pronunciations (if the input word is an ex-ception word) and is not very sensitive to the base-word frequency of the trained words. Nonetheless, it is highly sensitive to the statistical consistency of spelling–sound relationships at multiple grain sizes (from letters to word bodies), which is reflected by the activation of alternative phoneme candidates in the same syllabic position (especially the vowel). The model’s final pronunciation is produced by a phonological decision system (i.e., a phonological output buffer) on the basis of activation competition, which is a causal factor in naming latencies. The model provides a reasonable match to the nonword reading performance of human participants and can also read single- and multiletter graphemes. -->

完全な CDP（図 3 参照）では、組み立てられた音韻コードが、音韻決定系内の頻度感受性語彙処理の出力をオンラインで統合する。この相互作用により例外語の正しい発音が可能となり、語彙的要因と部分語彙的要因の組み合わせに依存する遅延（および／または正確性）効果が生まれる。Zorzi ら（1998b）は語彙ネットワークの分散型実装と局所的実装の双方の可能性を論じたが、彼らのシミュレーションの大半は完全には実装されていない局所的版に基づいていた（すなわち、語の語彙音韻は、いかなる語彙書記処理を経ることなくモデル内で直接活性化された）。
<!--In the full CDP (see Figure 3), the assembled phonological code is pooled online with the output of a frequency-sensitive lexical process in the phonological decision system. Such an interaction allows the correct pronunciation of exception words and produces the latency (and/or accuracy) effects that depend on the combination of lexical and sublexical factors. Zorzi et al. (1998b) discussed the possibility of using either a distributed or a localist implemen-tation of the lexical network, but most of their simulations were based on a localist version that was not fully implemented (i.e., the lexical phonology of a word was directly activated in the model without going through any lexical orthographic processing). -->

### 臨床への接続：WAB（失語症検査）

#### WAB

自発話，話し言葉の理解，復唱，呼称，読み，書字，行為，構成，の 8 項目。
各項目は，下位検査が存在する。

* I. 自発話: 7. 絵の中で起こっていることを説明してください。
* II. 話し言葉の理解: A. 「はい」「いいえ」で答える問題，B. 単語の聴覚的認知，C. 経時的命令
* III. 復唱
* IV. 呼称: 物品呼称，語想起，文章完成，会話での応答
* V. 読み: 
    * A. 文章の理解，
    * B. 文字による命令文，
    * C. 漢字単語と物品との対応，C'. カナ単語と物品との対応，
    * D. 漢字単語と絵の対応，D'. カナ単語と絵の対応，
    * E. 絵と漢字単語との対応，E'. 絵とカナ単語との対応，
    * F. 話し言葉の単語とカナ単語との対応，F': 話し言葉の単語と漢字単語との対応，
    * G. 文字の弁別，
    * H. 漢字の構造を聞いて語を認知する，
    * I. 漢字の構造を言う

#### II. 話し言葉の理解 B: 単語の聴覚的認知

* 実物: 毛糸，切手，灰皿，時計，新聞，鉛筆，
* 絵カード: 切手，毛糸，新聞，鉛筆，灰皿，時計
* 図形: 四角形，三角形，丸，矢印，十字形，円柱
* 文字カード: め，て，た，き，や，き
* 数字カード: 5, 61, 500, 1867, 32, 5000
* 色カード: 紫，茶，赤，緑，黄，黒
* 家具: 家，椅子，机，電燈，ドア，天井
* 身体部: 耳，鼻，目，胸，首，あご

#### II. 話し言葉の理解 C: 経時的命令

#### III. 復唱

まど。パイプ。でんわ。なす。バナナ。33。ゆきだるま。25パーセント。92分の1。電話がなっています。魚屋は元気でした，兄はまだ戻りません。日本高校野球連盟。だけどやっぱりでもはだめ。新しい甘酒を５本のひょうたんに入れなさい。

#### IV. 呼称 A. 物品呼称

鉛筆，ボール，新聞，コップ，毛糸，切手，消しゴム，くし，ピストル，鍵，歯ブラシ，輪ゴム，金づち，ナイフ，スプーン，灰皿，フォーク，爪切り，虫メガネ，洗濯バサミ

#### IV. 呼称 B. 語想起

#### IV. 呼称 C. 文章完成

1. 砂糖は
2. 彼らは仲が悪く，まるで犬と
3. クリスマスのある月は
4. バラは赤で，ひまわりは
5. 草は

#### IV. 呼称 D. 会話で応答

1. 雪は何色ですか。
2. 一週間は何日ですか。
3. 看護婦さんは何処に勤めていますか。
4. どんなもので字を書きますか。
5. どこで切手を買いますか。

#### V. 読み

A. 文章の理解
B. 文字による命令文
C. 文字単語と物品の対応
D. 文字単語と絵の対応
E. 絵と文字単語との対応
F. 話し言葉の対応と文字単語との対応
G. 文字の弁別
H. 漢字の構造を聞いて語を認知する
I. 漢字の構造を言う

<!-- header-includes:
    - \usepackage{algorithm}
    - \usepackage[ruled,vlined,linesnumbered]{algorithm2e}
    - \usepackage[utf8]{inputenc} -->



**思考実験：**
WABの検査対象者が以下の症状を示したとする。モデルの「どこ」が断線しているか特定せよ。

1. **表層失読（Surface Dyslexia）**
* **症状**: 「仮名」や無意味な文字列はすらすら読める。しかし、「漢字」が読めない、あるいは漢字を無理やり仮名読みのルールで読もうとする。
* **モデル解釈**: 経路A（非語彙的経路）は完全に生きている。しかし、**経路B（語彙・意味的経路）が断線している**ため、意味アクセスを必要とする表意文字の処理がバイパスされ、機械的な音声変換プロセスだけが空回りしている状態である。


2. **音韻失読（Phonological Dyslexia）**
* **症状**: 日常的に使う単語や「漢字」は読める。しかし、初めて見る無意味な文字列（非語）を与えられると全く読めなくなる。
* **モデル解釈**: 経路B（語彙・意味的経路）は生きている。しかし、**経路A（非語彙的経路）が断線している**ため、既存の辞書（レキシコン）に登録されていない新しい入力を、ルールに従って音に変換する機能が喪失している。

<!-- ## 5. 小テスト（本質的理解の測定） -->

**Q1.**
WAB の物品呼称検査（絵を見て名前を答える）において、「リンゴ」の絵を見て「ミカン」と答えてしまう（意味性錯語）患者がいる。しかし、この患者は「リンゴ」という単語の音声を聞かせると、正しく「リンゴ」と復唱することは可能である。
DRCモデルおよび周辺のネットワーク配線を想定したとき、この患者の情報処理ネットワークにおいて、「正常に機能している経路」と「ノイズが混入している（または損傷している）層・経路」を明確に区別し、論理的に説明せよ。



# IAM: Interactive Activation Model 相互活性化モデル

<div class="figcenter">
<img src="/2026assets/1981McClellandRumelhart_fig1.png" width="22%">
<img src="/2026assets/1981McClellandRumelhart_fig2.png" width="11%">
<img src="/2026assets/1981McClellandRumelhart_fig3.jpg" width="32%">
<img src="/2026assets/1981McClellandRumelhart_fig4.png" width="27%">
<img src="/2026assets/1981IAM_fig5.png" width="14%">
<!-- <img src="/2026assets/1981IAM_fig6.png" width="4%"> -->
<img src="/2026assets/1981McClellandRumelhart_fig7.png" width="32%">
<img src="/2026assets/1981IAM_fig8.png" width="24%">
</div>

<!-- Models of Impaired Lexical Access in Speech Production
(Journal of Memory and Language, 43, 182–216) の研究背景 → モデル → シミュレーション → 理論的含意の流れを押さえた要約です。 -->

# Dell model, Dell+(1997) と Foygell & Dell(2000)

<div class="figcenter">
<img src="/2026assets/2000Foygell_Dell_fig1.png" width="33%">
</div>


Dell+(1997) の weight-decay（WD）モデル と Foygel & Dell (2000) の semantic-phonological（SP）モデルの違いは、同じ「interactive 2-step／拡散活性化」系譜の中で、損傷（lesion）をどのパラメータで表すか，そのパラメータが“理論的に何を意味するか，が異なる。

#### WD (1997)

患者を表す 2 パラメータ物 WD（1997）では，患者差は 2 つの大域的パラメータ：

* global connection weight（全結合の重みを一括で弱める）
* global decay rate（全体の減衰を一括で強める）

実際、1997 論文の要約部でも「モデルを 損傷する方法」として 結合重みと decay を大域的に変えると明記されている。

#### SP（2000）

患者差は 2 つの **経路特異的** パラメータで表現：

* semantic weight（意味→語彙側の重み）
* phonological weight（語彙→音韻側の重み）

この対比は Foygel & Dell (2000) の概要にもはっきり書かれていて、WD が「global connection weight と global decay rate」、SP が「semantic weight と phonological weight」で患者を特徴づける、とされている。

直感的に言うと：WDは「全体の元気さ」SPは「どこが弱いか」
<!-- WD：ネットワーク全体の“伝わりやすさ”と“持続しやすさ”を落とす
→ 結果として、エラーが増える・重症度が上がる、という方向に強い
SP：意味→語彙（意味駆動）と語彙→音韻（音韻化）の どちらのリンクが主に弱いかを分ける
→ 「意味錯語が多い」 vs 「音韻性錯語が多い」を、より直接に結びつけやすい
3) モデル比較としての含意：WDとSPは“同じデータに同程度フィット”しうる -->

Foygel & Dell (2000) の立て付け自体が「2モデル比較」で、

SP は WD と同程度に患者データにフィットできる
しかし パラメータの解釈・他理論との接続は SP の方が良い

という主張を置いています。

<!-- （あなたが言っていた「同じ命名データから原因が特定できない」問題は、まさにこの比較が炙り出す論点です。） -->

#### jolt との関係

両者ともベースは interactive 2-stepで、語彙選択→音韻アクセスの切り替えを jolt で表現する系譜です。1997 論文でも、音韻アクセス開始時に選択語へ大きな jolt を与える説明が出てくる。

<!-- ただし、WD と SP の違いの主眼は jolt の有無ではなく、上で述べた「損傷パラメータの意味づけ（global か pathway-specific か）」です。 -->

<!-- まとめ（最短） -->
* WD (1997)：患者＝ global weight と global decay（全体的な弱り）
* SP (2000)：患者＝ semantic weight と phonological weight（意味側と音韻側のどちらが弱いか）

そして Foygel & Dell (2000) は、この比較を通じて **「命名データだけだと内部要因の同定が難しい」**方向の議論を強くしやすい枠組みを作った

<!-- 必要なら次に、あなたの実装方針（「問題点を指摘しやすいコード」）に直結する形で、

WD の2次元（weight × decay）と
SP の2次元（s × p）を
同じ観測（命名のカテゴリ率・混同行列）でフィットさせて、近似解がどれだけ多重に出るかを並べる “同定不能性比較スクリプト”

をそのまま書けます。 -->

<!-- 1. 研究の目的と背景

本論文の目的は、失語症者（特に音韻性錯語を示す症例）における語彙アクセス障害を、計算モデルによって説明・分類することであった。
背景には以下の問題意識：

* 失語症の語産生エラー（意味錯語・音韻錯語・混合錯語）はどの処理段階の障害から生じるのか？
* 単に「意味段階が壊れている」「音韻段階が壊れている」という局所的説明だけで十分か？
* 単一モデルで多様な失語パターンを説明できるのか？

この文脈で、著者らは Dell の相互活性化モデル（interactive spreading activation model） を基盤として、障害をパラメータ操作として定式化する。