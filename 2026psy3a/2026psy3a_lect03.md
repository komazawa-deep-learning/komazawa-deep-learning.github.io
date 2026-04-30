---
title: 第 03 回 2026 年度開講 心理学特講 IIIA 駒澤大学 
author: 浅川 伸一
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="center">
<font size="+1" color="navy"><strong>計算モデルによる課題の理解：認知課題から神経心理学検査への適用</strong></font><br/><br/>
</div>

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 31/Apr/2026<br/>
Appache 2.0 license<br/>
</div>


<!-- * [実習ファイル  <img src="/assets/colab_icon.svg">](){:target="_blank"}
* [課題提出用フォルダ](){:target="_blank"} -->


<!-- # 心理学特講IIIA 第3回
## Simon課題：刺激-反応適合性

浅川 伸一  
駒澤大学 文学部 心理学科

2026年度 前期 -->

<!-- --- -->




## 本日の内容

1. 前回の復習（Stroop課題）
2. Simon効果とは
3. Stroopとの比較
4. 実験デザイン
5. 実習：Simon課題の実装と分析
6. 両課題の比較分析

---

### 実習ファイル

* [転移学習による Stroop 効果のデモ <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_1123Stroop_model.ipynb){:target="_blank"}
* [1990 年代の Stroop 効果のシミュレーション<img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_1110Stroop_1990Cohen_model.ipynb){:target="_blank"}
<!-- * [Stroop 効果シミュレーションの準備 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_1123Stroop_model.ipynb){:target="_blank"} -->


---

## 前回の復習：Stroop効果

**Stroop課題**
- 色名単語を異なる色で提示
- 文字の意味が色の命名に干渉

**主な発見**
- 不一致条件で反応時間が増加
- 文字読みは自動的に処理される
- 意味的な干渉効果


## Stroop 効果

<div class="figcenter">
<img src="/2023assets/1990Cohen_McClelland_stroop_fig3.svg">
<img src="/2023assets/2023_1110task_demand_conflict_ja.svg" width="49%">
</div>
<div class="figcaption" style="width:94%">

左: 図 3. 単語読解と色名学習後の接続強度を示すネットワーク図。 (強度は接続の横に示され，中間ユニット
のバイアスはユニットの内側に示されている。
課題要求ユニットから中間ユニットへの注意強度は固定され，中間ユニットのバイアスも固定された。
課題要求ユニットがオンのとき，対応する経路のユニットの基本入力が 0.0 になり，もう一方の経路のユニッ
トの基本入力が，実験によって -4.0 から -4.9 の範囲になるように選ばれた)。
<!-- Figure 3. Diagram of the network showing the connection strengths after training on the word-reading and color-naming tasks.
(Strengths are shown next to connections; biases on the intermediate units are shown inside the units.
Attention strengths-from task demand units to intermediate units-were fixed, as were biases for the intermediate units.
The values were chosen so that when the task demand unit was on, the base input for units in the corresponding pathway was 0.0, whereas the base input to units in the other pathway was in the range of
 -4.0 to -4.9, depending on the experiment.) -->

出典: Cohen, Dunbar, and McClelland (1990) __On the Control of Automatic Processes: A Parallel Distributed Processing Account of the Stroop Effect__, Psychological Review, Vol. 97, No. 3, 332-361.

右: 転移学習，微調整を用いた Stroop 課題の枠組み
</div>


---

## Simon効果とは

**J. Richard Simon (1969)**



<div class="figcenter">
<img src="/2026assets/1969Simon_tab1.svg" alt="Simon Effect" width="66%;">
</div>

装置：本装置は、被験者が 2 つのGrason-Stadler TDH-39マッチドイヤホンのいずれか一方を通じて聴いた、1,000 cps の単音音響の開始までの選択反応時間（RT）および動作時間（MT）を測定した。被験者の課題は、音響を聴いた耳に応じて、右手で制御ハンドルを中央位置から右または左へ動かすことだった。反応時間を測定するクロックカウンターは、音が提示された時点で開始され、被験者がハンドルを中央位置から動かした時点で停止した。
移動時間を測定する別のクロックカウンターは、ハンドルが中央位置から動かされた時点で開始され、10 インチの横方向の移動が完了した時点で停止した。
<!-- Apparatus. The apparatus measured choice RT and movement time (MT) to the onset of a 1,000-cps monaural tone, which S heard through one of two Grason-Stadler TDH-39 matched earphones. The S's task was, using his right hand, to move a control handle to either the right or the left from a center position depending on the ear in which he heard the tone. A Clock-counter which measured RT started when the tone was presented and stopped when S moved the handle from the center position. Another Clock-counter, which measured MT, started when the handle had been moved from the center position and stopped when the 10-in. lateral movement had been completed.-->

刺激音のランダムな系列をテープに録音し、その半分を右チャンネル、半分を左チャンネルに割り当て、ソニー製 TC-500 ステレオレコーダーを用いて提示した。各音の持続時間は 500 ミリ秒、音圧レベル（SPL）は約 85 デシベルであった。各音の 2 秒前に、2,000 Hz のバイノーラル・レディ信号を提示した。試行間の間隔は 7 秒であった。
<!--A random sequence of stimulus tones was recorded on tape, half in the right channel and half in the left, and presented by a Sony TC-500 stereo-recorder. Each tone was 500 msec. in duration and approximately 85-db. SPL. A 2,000-cps binaural ready signal was presented 2 sec. prior to each tone. There was a 7-sec. interval between trials. -->


手続きと実験計画：各被験者は 2 試行ブロックを行った。各ブロックでは、録音された 50 個の刺激音のランダムな配列に対して反応するよう求められた。そのうち 25 個は右耳に、25 個は左耳に聞こえるようにした。
被験者には、「この検査は、右耳か左耳のどちらかに聞こえる音に対して、どれだけ素早く反応し、動作できるかを調べる検査だ」と説明された。ある試行ブロックでは、被験者は次の教示を受けた:
<!-- Procedure and experimental design.-Each S performed on two blocks of trials. Each block involved responding to a recorded random sequence of 50 stimulus tones, 25 in the right ear and 25 in the left. The S was told, "This is a test to see how quickly you can react and move in response to a tone which you will hear either in your right ear or left ear." In one block of trials, he was instructed to-->

> 刺激を受けた耳の反対側へ操作レバーを動かしてください。つまり、左耳で音が聞こえたら操作レバーをできるだけ速く右へ動かし、右耳に音が聞こえたら操作レバーをできるだけ速く左へ動かすしてください。
<!-- > move the control handle away from the side of the ear stimulated. In other words, when you hear the tone in your left ear, move the control handle to the right as quickly as possible, and when you hear the tone in your right ear, move the control handle to the left as quickly as possible. -->

第 2 試行ブロックでは、被験者 S は同じ刺激音のシーケンスを聞いたが、今回は「刺激を受けた耳の側に向かって操作レバーを動かす」よう指示された。各テスト試行ブロックの前には、右耳用 2 回、左耳用 2 回の計 4 回の練習試行が行われた。
<!-- In the second block of trials, S heard the same sequence of stimulus tones, but this time was instructed to "move the control handle toward the side of the ear stimulated." Each block of test trials was preceded by four practice trials, two in the right ear and two in the left.-->

男性と女性の各半数は、「離隔」ブロックを先に、「接近」ブロックを後に実施し、各群の残りの半数はその逆の順序で実施した。各「性別×順序」下位群の被験者の半数については、2 つの刺激チャンネル間に存在し得た差異を相殺するため、イヤホンの装着側を逆にした。
<!--Half of the males and half of the females performed the "away" block first and the "toward" block second, while the other half of each group performed in the reverse sequence. For half of the Ss in each Sex X Sequence subgroup, the earphones were reversed to balance out any differences that may have existed between the two stimulus channels. -->


**基本的な発見**
- 刺激音の提示側の耳と反応の位置にレバーを動かすと速い
- 対応しないと遅い（干渉）
- **課題には関係ない空間情報が反応に影響**

**例**
- 左耳に音 → 操作レバーを動かす
- 左側に倒す：速い（一致）
- 右側に倒す：遅い（不一致）

---

## Simon 課題の基本設定

```
画面中央の注視点
    ↓
左耳または右耳に音刺激を提示
    ↓
聞こえた耳に応じてキー押し
```

Stroop 課題と同じ視覚処理課題にすれば，

**課題**: 赤なら左キー、青なら右キー

| 刺激 | 位置 | 正解 | 条件 | 予測RT |
|------|------|------|------|--------|
| 🔴 | 左 | 左キー | 一致 | 速い |
| 🔴 | 右 | 左キー | 不一致 | 遅い |
| 🔵 | 右 | 右キー | 一致 | 速い |
| 🔵 | 左 | 右キー | 不一致 | 遅い |

**Simon効果** = 不一致RT - 一致RT

**条件**
- **一致条件**: 刺激位置と反応位置が同じ側
- **不一致条件**: 刺激位置と反応位置が反対側

**重要**: 位置情報は課題に無関連なのに影響する


---

## Stroopとの比較（1）

### 類似点

**両者とも干渉効果**
- 課題無関連情報が処理に影響
- 自動的な処理
- 反応時間の増加

**認知的メカニズム**
- 複数の情報源の競合
- 反応選択の困難

---

## Stroopとの比較（2）

### 相違点

| 特徴 | Stroop 課題 | Simon 課題 |
|------|-----------|----------|
| **課題関連** | 色 | 色 |
| **課題無関連** | 文字の意味 | 刺激の位置 |
| **干渉の性質** | 意味的・言語的 | 空間的 |
| **効果量** | 大（150-250ms） | 中（50-100ms） |
| **エラー率** | やや高い | 低い |

---

## なぜ位置が影響するのか？

**刺激-反応適合性（S-R Compatibility）**

1. **自動的な空間符号化**
   - 刺激位置が自動的に符号化される
   - 意図的に無視できない

2. **反応の空間的性質**
   - 左右のキー押しは空間的
   - 刺激位置と反応位置が対応すると促進

3. **競合の解決**
   - 不一致時は競合を解決する必要
   - 認知的コストが発生

---

## 理論的意義

**自動的注意**
- 課題無関連でも処理される情報
- 空間位置は特に顕著

**反応選択過程**
- 刺激-反応 写像の自動活性化
- 意図的制御の必要性

**応用**
- インターフェース設計
- 交通信号の配置
- ヒューマンエラーの理解

---

## 実験デザイン

**独立変数**
- 空間的一致性（2水準）
  - 一致条件
  - 不一致条件

**従属変数**
- 反応時間（RT）
- 正答率

**計画**
- 参加者内計画（Within-subjects design）

---

## 予測される結果

**仮説**
1. 不一致条件の反応時間が長い
2. 一致条件の反応時間が短い
3. Simon効果: 約50-100ms

**統計的検定**
- 対応のあるt検定（Paired t-test）
- 効果量の算出（Cohen's d）

---

## 本日の実習

**実装内容**
1. Simon 課題のシミュレーション
2. 模擬データの生成
3. 記述統計と可視化
4. 対応のあるt検定
5. **Stroop課題との比較**
6. 練習効果の分析

**Google Colabで実施**

---

## まとめ

1. **Simon効果**: 空間的一致性が反応時間に影響
2. **刺激-反応適合性**: 自動的な空間コーディング
3. **Stroopとの違い**: 意味的 vs 空間的干渉
4. **理論的意義**: 自動的注意と反応選択
5. **応用**: インターフェース設計、エラー予防

**共通点**: 課題無関連情報の自動処理

---

## 次回予告

**第4回：Flanker課題**
- 妨害刺激の影響
- 選択的注意
- StroopとSimonとの比較

**準備学習課題**
- Simon効果について説明（100字）
- 日常生活での例を挙げる
- S-R適合性について調べる（50字）

---
