---
title: 第 10 回 2026 年度開講 心理学特講 IIIA 駒澤大学 
author: 浅川 伸一
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="center">
<font size="+1" color="navy"><strong>計算モデルによる課題の理解：認知課題から神経心理学検査への適用</strong></font><br/><br/>
</div>

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 26/Jun/2026<br/>
Appache 2.0 license<br/>
</div>

# 07440 心理学特講ⅢA - 第 10 回

* [課題提出フォルダ](https://drive.google.com/drive/u/6/folders/1wYaBn4dovEwtlOfOhcAFP2bJdyDqM9ZL){:target="_b
lank"}


* [フィラデルフィア絵画命名検査課題 PNT を転移学習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_0618pnt_transfer_learning.ipynb){:target="_blank"}
* [転移学習による Stroop 効果のデモ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_1123Stroop_model.ipynb)


# WEAVER++

<div class="figcenter">
<img src="/2023assets/2003Roelofs_stroop_fig7.svg" width="33%">　　　　　　　　　
<img src="/2023assets/2003Roelofs_stroop_fig9.jpg" width="44%">
</div>
<div class="figcaption" style="width:88%">

図 7. WEAVER++ における処理レベル。
単語の読解はレンマ選択を伴う場合もあれば (経路 a)，伴わない場合もある (経路 b)。
<!-- Figure 7. Levels of processing in WEAVER++.
Word reading may involve lemma selection (Route a) or may not (Route b). -->
<!-- Adapted from Cognition, 42, A. Roelofs, “A Spreading-Activation Theory of Lemma Retrieval in Speaking,” p. 114, Figure 1, Copyright 1992, with permission from Elsevier Science. -->

図 9. Stroop 課題における，単語計画と実行制御。
ヒトの左半球の側面図 (上) と 中央 (下)。
単語計画系は，色知覚 (cp)，概念同定 (ci)，レンマ検索 (lr)，単語携帯符号化 (wfe)，構音処理 (art) を介して色名呼称へと至る。
単語形態知覚 (wfp) は，語彙と形態と並列的に至る。
単語音読は，最小限 wfp, wfe, art を含む。
実行系は前帯状回にあり，目標と入力制御に関与する。
<!-- Figure 9. Word planning and executive control in the Stroop task.
Lateral view (top panel) and medial view (bottom panel) of the left hemisphere of the human brain.
The word-planning system achieves color naming through color perception (cp), conceptual identification (ci),
lemma retrieval (lr), word-form encoding (wfe), and articulatory processing (art);
word-form perception (wfp) activates lemmas and word forms in parallel.
Word reading minimally involves wfp, wfe, and art.
The executive system centered on the anterior cingulate achieves goal and input control. -->
出典: Roelofs (2003) __Goal-Referenced Selection of Verbal Action: Modeling Attentional Control in the StroopTask__, Psychological Review, 2003, Vol. 110, No. 1, 88–125.
</div>


## 関連する話題

### 絵画‐単語干渉課題

<center>
<img src="/2023assets/1984Glaser_picture-word_fig1.svg" width="39%">
<div class="figcaption">

刺激の例: (a) 非絵画，(b) 単語なし絵画, (c) 非単語，(d) 不一致刺激

<!-- Figure 1. Characteristic examples of the stimulus components:
Panel a, nonpicture;
Panel b, picture with blank word field;
Panel c, nonword; and Panel d, complete incongruent stimulus.

Note. The pictures are from Bildgeschichten [Picture stories] (pp. I , 22) by F. Meixner, n.d., Frankfurt, Federal Republic of Germany: Diesterweg. Copyright 1 975 by Diesterweg. Reprinted by permission. -->
</div></center>

<center>
<img src="/2023assets/1984Glaser_picture-word_fig2.svg">
<div class="figcaption">
図 課題 $\times$ SOA $\times$ 一致性における平均促進・抑制得点
<!-- Figure 2. Mean facilitation and inhibition scores in the Task X SOA X Congruency cells of Experiment I. (SOA = stimulus onset asynchrony.) -->
</div></center>

### 単語反復課題

<div class="figcenter">
<img src="/2023assets/2006Howard_fig1.svg" width="44%">
<img src="/2023assets/2006Howard_fig3.svg" width="44%">
<div class="figcaption">

左 カテゴリー内の順序位置が命名反応時間 (補正なし RT) に及ぼす影響。<br/>
右  (A) 健常群の反応時間 (上) と (B) モデル出力
</div></div>

<div class="figcenter">
<img src="/2023assets/2006Howard_tab1.svg" width="77%">
<div class="figcaption">

表 平均正答反応時間 (順番，ラグ別) (95% 被験者内信頼区間) A. 未補正の反応時間, B. 実験期間中の線形変化を補正した反応時間
</div></div>
<!-- <img src="figures/2006Howard_tab2.svg"> -->

<div class="figcenter">
<img src="/2023assets/2006Howard_fig2.svg" width="49%">
<img src="/2023assets/2006Howard_fig4.svg" width="33%">
<!-- <img src="figures/2006Howard_fig5.svg">
<img src="figures/2006Howard_fig6.svg"> -->
</div>


# 文献

* ストループ効果 J. Ridley Stroop (1935) __Studies of Interference in Serial Verbal Reactions__, Journal of Experimental Psychology, 18, 643-662.
* サイモン効果 J. Richard Simon (1969) __Reactions Toward the Source of Stimulation__, Journal of Experimental Psychology, 81(1), 174-176.
* 絵画‐単語干渉効果 W. Glaser & F-J. Dungelhoff, (1984) __The Time Course of Picture-Word Interference__, Journal of Experimental Psychology: Human Perception and Performance, 10(5), 640-654.
* 絵画‐単語課題の意味促進 M-T. Bajo (1988) __Semantic Facilitation With Pictures and Words__, Journal of Experimental Psychology: Learning, Memory, and Cognition, 14(4), 579-589.
* 絵画命名課題における累積意味抑制 D. Howard+ (2006) __Cumulative semantic inhibition in picture naming: experimental and computational studies__, Cognition 100, 464–482.
* 絵画命名課題における言語間の干渉と促進 A. Roelofs+ (2016) __Electrophysiology of cross-language interference and facilitation in picture naming__. http://dx.doi.org/10.1016/j.cortex.2015.12.003
* 累積意味，意味ブロック，意味妨害効果 A. Roelofs+ (2018) __A unified computational account of cumulative semantic, semantic blocking, and semantic distractor effects in picture naming__. https://doi.org/10.1016/j.cognition.2017.12.007



## ブロードマン (Brodman) の脳地図

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

