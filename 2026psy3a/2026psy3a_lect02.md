---
title: 第 02 回 2026 年度開講 心理学特講 IIIA 駒澤大学 
author: 浅川 伸一
layout: home
---

<link href="/css/asamarkdown.css" rel="stylesheet">
<div align="center">
<font size="+1" color="navy"><strong>計算モデルによる課題の理解：認知課題から神経心理学検査への適用</strong></font><br/><br/>
</div>

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 24/Apr/2026<br/>
Appache 2.0 license<br/>
</div>


* [実習ファイル  <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2026notebooks/2026psy3a_lect02.ipynb){:target="_blank"}
* [課題提出用フォルダ](https://drive.google.com/drive/u/6/folders/1wYaBn4dovEwtlOfOhcAFP2bJdyDqM9ZL){:target="_blank"}

# 計算モデルによる課題の理解：認知課題から神経心理学検査への適用

## 第 02 回：行動指標の基礎

## 本日の内容

1. 前回の復習
2. Stroop効果とは
3. 理論的背景
4. 実験デザイン
5. データ分析方法
6. 実習：Stroop課題の実装と分析

---

## 前回の復習

**反応時間（RT）分析の基本**
- 刺激提示から反応までの時間
- 認知処理の速度を反映
- ミリ秒（ms）単位で測定

**基本的な統計**
- 平均値、標準偏差
- 箱ひげ図、ヒストグラム
- 外れ値の処理

---

## Stroop効果とは

**古典的実験（Stroop, 1935）**

<span style="color: red;">赤</span>　← 一致条件（速い）
<span style="color: blue;">赤</span>　← 不一致条件（遅い）
<span style="color: red;">XXX</span>　← 中性条件（中間）

**課題**: 文字の色を答える（文字の意味は無視）

---

## Stroop効果の発見

**John Ridley Stroop (1935)**
- Journal of Experimental Psychology, 18(6), 643-662
- 色と単語の干渉効果を初めて実証
- 認知心理学の古典的研究の一つ

**主要な発見**
- 不一致条件で反応時間が有意に増加
- 文字の読み取りは自動的に起こる
- 意図的な抑制が必要

---

## 3つの条件

| 条件 | 刺激例 | 予測 |
|------|--------|------|
| **一致** | <span style="color: red;">赤</span> | 最も速い |
| **中性** | <span style="color: red;">XXX</span> | 中間 |
| **不一致** | <span style="color: blue;">赤</span> | 最も遅い |

**典型的な結果**
一致（600ms）< 中性（700ms）< 不一致（850ms）

---

## 理論的背景（1）

**自動処理 vs 統制処理**

**自動処理（Automatic Processing）**
- 意識的な努力が不要
- 高速
- 例：熟練者の文字読み

**統制処理（Controlled Processing）**
- 意識的な注意が必要
- 低速
- 例：色の命名

---

## 理論的背景（2）

**処理速度の理論**
- 文字の読み取り（速い・自動的）
- 色の命名（遅い・意図的）
- 両者が競合 → 干渉効果

**自動性の獲得**
- 練習により処理が自動化
- 抑制が困難になる
- 日常生活での経験（読字）が影響

---

## 干渉のメカニズム

```
刺激「赤」（青色で表示）
    ↓
┌──────────┬──────────┐
│文字処理   │色処理     │
│（自動的） │（意図的） │
│「赤」     │「青」     │
└──────────┴──────────┘
    ↓
  競合・干渉
    ↓
反応時間の増加
```

---

## 実験デザイン

**独立変数**
- 刺激タイプ（3水準）
  - 一致条件
  - 中性条件
  - 不一致条件

**従属変数**
- 反応時間（RT）
- 正答率

**参加者内計画（Within-subjects design）**

---

## 予測される結果

**仮説**
1. 不一致条件の反応時間が最も長い
2. 一致条件の反応時間が最も短い
3. 中性条件は両者の中間

**統計的検定**
- 一要因分散分析（One-way ANOVA）
- 多重比較（事後検定）
- 効果量の算出（Cohen's d）

---

## データ分析の流れ

1. **データの確認**
   - 欠損値、外れ値のチェック

2. **記述統計**
   - 平均、標準偏差、範囲

3. **可視化**
   - 箱ひげ図、バイオリンプロット

4. **推測統計**
   - 分散分析、多重比較、効果量

---

## 本日の実習

**実装内容**
1. Stroop刺激の作成
2. 模擬データの生成
3. 記述統計と可視化
4. 一要因分散分析
5. 多重比較
6. 効果量の計算

**Google Colabで実施**

---

## Stroop課題の応用

**臨床場面での利用**
- 注意機能の評価
- 実行機能の評価
- 認知機能低下の検出

**研究分野**
- 加齢研究
- 神経心理学
- 認知神経科学

---

## まとめ

1. **Stroop効果**: 色と単語の干渉現象
2. **自動処理**: 文字読みは自動的に起こる
3. **統制処理**: 色の命名には意図的な注意が必要
4. **干渉**: 両者の競合が反応時間を増加させる
5. **応用**: 注意・実行機能の評価に利用

---

## 次回予告

**第3回：Simon課題**
- 刺激-反応適合性
- 空間的干渉効果
- Stroopとの比較

**準備学習課題**
- Stroop効果について説明（100字）
- 日常生活での例を挙げる
- 臨床的応用について調べる（50字）

---
