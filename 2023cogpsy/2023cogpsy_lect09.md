---
title: "第09回 2023年度開講 駒澤大学 認知心理学研究"
author: "浅川 伸一"
layout: home
codemirror_mode: python
codemirror_mime_type: text/x-cython
---

<div align="right">
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 24/Nov/2023<br/>
Appache 2.0 license<br/>
</div>

<link href="/css/asamarkdown.css" rel="stylesheet">

## 実習

* [1990 年代の Stroop 効果のシミュレーション<img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_1110Stroop_1990Cohen_model.ipynb){:target="_blank"}


## Stroop 効果

<div class="figcenter">
<img src="/2023assets/1990Cohen_McClelland_stroop_fig3.svg">
<img src="/2023assets/2023_1110task_demand_conflict_ja.svg" width="49%">
<div class="figcaption">

左: 図 3. 単語読解と色名学習後の接続強度を示すネットワーク図。 (強度は接続の横に示され，中間ユニットのバイアスはユニットの内側に示されている。
課題要求ユニットから中間ユニットへの注意強度は固定され，中間ユニットのバイアスも固定された。
課題要求ユニットがオンのとき，対応する経路のユニットの基本入力が 0.0 になり，もう一方の経路のユニットの基本入力が，実験によって -4.0 から -4.9 の範囲になるように選ばれた)。
<!-- Figure 3. Diagram of the network showing the connection strengths after training on the word-reading and color-naming tasks.
(Strengths are shown next to connections; biases on the intermediate units are shown inside the units.
Attention strengths-from task demand units to intermediate units-were fixed, as were biases for the intermediate units.
The values were chosen so that when the task demand unit was on, the base input for units in the corresponding pathway was 0.0, whereas the base input to units in the other pathway was in the range of -4.0 to -4.9, depending on the experiment.) -->

出典: Cohen, Dunbar, and McClelland (1990) __On the Control of Automatic Processes: A Parallel Distributed Pro
cessing Account of the Stroop Effect__, Psychological Review, Vol. 97, No. 3, 332-361.

右: 転移学習，微調整を用いた Stroop 課題の枠組み
</div></div>

<div class="figcenter">
<img src="/2023assets/2003Roelofs_stroop_fig7.svg" width="33%">　　　　　　　　　
<img src="/2023assets/2003Roelofs_stroop_fig9.jpg" width="44%">
<div class="figcaption">

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
</div></div>


# 文献

* ストループ効果 J. Ridley Stroop (1935) __Studies of Interference in Serial Verbal Reactions__, Journal of Experimental Psychology, 18, 643-662.
* サイモン効果 J. Richard Simon (1969) __Reactions Toward the Source of Stimulation__, Journal of Experimental Psychology, 81(1), 174-176.

