---
title: 2026 年度開講 人工知能 I および II 駒澤大学 
author: 浅川 伸一
date: 20260417
layout: home
---

<link href="/css/asamarkdown.css" rel="stylesheet">
<div align="center">
<font size="+1" color="navy"><strong>人工知能</strong></font>
</div>
<div style="text-align:right">
<img src="/2026assets/2026ai_exported_qrcode_image_600.png" style="width:19%"><br/>
<font size="+3">URL: https://komazawa-deep-learning.github.io/2026ai/</font>
</div>

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 17/Apr./2026<br/>
Appache 2.0 license<br/><br/>
</div>


# 人工知能 I - 第1回: イントロダクション

[cite_start]**開講年度・期**: 2026年前期   
[cite_start]**担当教員**: 浅川 伸一   
[cite_start]**資料公開先**: [GitHub Repository](https://komazawa-deep-learning.github.io/2026ai) 

---

## 1. 授業計画（教員用メモ・タイムテーブル）
* **13:00 - 13:15**: 授業全体のオリエンテーション（シラバス説明、評価基準）
* **13:15 - 13:30**: AI の概観と「人工知能 I」から「人工知能 II」への接続
* **13:30 - 13:50**: 実行環境（Google Colaboratory）の導入と基本操作
* **13:50 - 14:15**: 学習の前提概念（データ・モデル・評価）
* **14:15 - 14:30**: 小テストと質疑応答、次回予告

---

## 2. 本日のねらい（学生向け）
[cite_start]本授業（人工知能 I）は、データサイエンス・機械学習・ニューラルネットワークの基礎概念を学ぶための第一歩です 。
第 1 回となる本日は、以下の達成を目標とします。
1. [cite_start]**授業の全体像を把握する**: 前期の「I」から後期の「II」へとどのように繋がるのかを理解する。
2. [cite_start]**実行環境に慣れる**: 今後の授業で必須となる Python (Google Colaboratory) の基本的な使い方を身につける。
3. [cite_start]**基礎用語の定義を知る**: 機械学習における「データ」「モデル」「評価」という 3 つの必須概念を理解する。

> **💡 履修上の重要ポイント**
> [cite_start] 本授業では、数式の導出やゼロからのプログラミング（コーディング）は求めません [cite: 30][cite_start]。
> 配布する Python コードを実行し、出てきた結果（グラフや表）を「読み取り、解釈する」ことを最も重視します 。

---

## 3. 講義資料

### 3.1. AIの概観と授業の全体像
* 人工知能（AI）とは何か？現在の立ち位置
* [cite_start]人工知能 I（前期）のスコープ：回帰、分類、評価、画像認識の基礎 
* [cite_start]人工知能 II（後期）への接続：自然言語処理、強化学習への展開 [cite: 39]

### 3.2. 実行環境：Google Colaboratoryの使い方
[cite_start]Google Colaboratory（通称 Colab）は、ブラウザのみで利用可能で、事前の環境構築が不要な強力なツールです 。

* [cite_start]**アクセス方法**: Googleアカウントでログインし、[Google Colab](https://colab.research.google.com/) にアクセスする 。
* **セルの種類**: テキストセル（Markdown）とコードセル（Python）の違い。
* **実行方法**: `Shift + Enter` でコードを実行してみよう。

```python
# 確認用サンプルコード
print("人工知能 I の環境構築が完了しました！")
import numpy as np
import matplotlib.pyplot as plt

# 簡単なグラフの描画テスト
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Test Plot")
plt.show()
```


### 3.3. 学習の前提概念
機械学習を理解する上で、以下の 3 つの概念がすべての基礎となります。

1. データ (Data): 学習の源泉。入力変数と出力変数（正解ラベル）。
2. モデル (Model): データから規則性を学習し、未知のデータに対して予測を行うための数理的な枠組み。
3. 評価 (Evaluation): モデルがどれくらい正確に予測できているかを測る指標。

## 4. 本日の小テスト（理解度確認）

アクティブラーニングの一環として、毎回小テストを実施します 。

**Q1**. Google Colabを利用する上で、手元のPCに複雑なソフトウェアのインストール（環境構築）は必要ですか？

* [ ] はい
* [ ] いいえ

**Q2**. 今日の講義で説明した「データ」「モデル」「評価」という 3 つの用語について、それぞれ 1 行で簡潔に定義を記述してください 。

* データ: [                           ]
* モデル: [                           ]
* 評価: [                           ]

5. 次回への準備学習（予習・復習）
次回のテーマは「AIの背景と論点（チューリングテスト、中国語の部屋など）」です 。


課題: 「AI と心理学の関係」について、自分なりの考えを 200〜300 字でまとめてきてください 。

目安学習時間: 60分 
提出方法: （※ここにLMS等での提出方法を記載）

---


第1回「人工知能 I」の授業で、学生が実際にGoogle Colaboratory上で動かして「データ」「モデル」「評価」の3要素を視覚的に体感できるサンプル教材（Markdown形式）を作成しました。

シラバスにもある通り、学生には「数式の導出や独力でのコーディングは求めない」 ため、コードはできるだけシンプルにし、実行結果（グラフ）を見て直感的に理解できる構成にしています。題材としては、心理学を学ぶ学生にも馴染み深い「勉強時間とテストの点数」の仮想データを用いた単回帰分析の例を採用しました。

以下のMarkdownをそのままColabのテキストセルとコードセルに貼り付けてご活用いただけます。

```markdown
## 3.4. 実習：AIの基本要素（データ・モデル・評価）を体感しよう

ここからは、実際にPythonのコードを実行して、AI（機械学習）の基本となる「データ」「モデル」「評価」の3つのステップを視覚的に確認してみましょう。

**※注意※**
ここにあるプログラムの書き方を今すぐ覚える必要はありません。「Shift + Enter」でコードを実行し、表示されるグラフを見て、AIが何をしているのかを直感的に掴むことが本日の目標です。

### ステップ1：準備
まずは、グラフを描画したり、計算を行ったりするための便利な道具（ライブラリ）を読み込みます。下のセルを選択して、「Shift + Enter」を押してください。

```python
# 必要なライブラリの読み込み（おまじないだと思って実行してください）
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

print("準備が完了しました！")

```

---

### ステップ2：【データ】を用意する

AIが学習するための「材料」を用意します。
ここでは、「心理学統計法の勉強時間（時間）」と「実際の小テストの点数（点）」という仮想のデータ（20人分）を作ってみます。

```python
# 1. データの作成（勉強時間とテストの点数）
np.random.seed(42) # 毎回同じ結果になるように固定

# 勉強時間（1時間〜10時間の間でばらつくように20人分生成）
study_hours = np.random.uniform(1, 10, 20).reshape(-1, 1)

# テストの点数（勉強時間に比例して上がるが、少しノイズ（個人差）を入れる）
test_scores = 10 * study_hours + np.random.normal(0, 10, (20, 1))

# グラフに描画して確認
plt.figure(figsize=(8, 5))
plt.scatter(study_hours, test_scores, color='blue', label='Student Data')
plt.xlabel('Study Hours (時間)')
plt.ylabel('Test Score (点)')
plt.title('[1. Data] 勉強時間とテストの点数の関係')
plt.legend()
plt.grid(True)
plt.show()

```

**【読み取りポイント】**
青い点が、集められた「データ」です。勉強時間が長いほど、点数が高い傾向があることが視覚的にわかりますね。これがAIに入力する手がかりとなります。

---

### ステップ3：【モデル】に学習させる

次に、このデータから規則性を学習する「モデル」を作成します。
今回は、データの間を通る最適な直線を引く「線形回帰」というシンプルなモデルを使います。

```python
# 2. モデルの作成と学習
# 直線を引くための空っぽのモデルを用意
model = LinearRegression()

# データ（勉強時間と点数）を渡して、規則性を学習（フィット）させる
model.fit(study_hours, test_scores)

# 学習したモデルに、グラフ用の直線を引かせる
x_line = np.linspace(0, 11, 100).reshape(-1, 1)
y_pred_line = model.predict(x_line)

# グラフに描画して確認
plt.figure(figsize=(8, 5))
plt.scatter(study_hours, test_scores, color='blue', label='Student Data')
plt.plot(x_line, y_pred_line, color='red', linewidth=3, label='AI Model (Predictive Line)')
plt.xlabel('Study Hours (時間)')
plt.ylabel('Test Score (点)')
plt.title('[2. Model] モデルが学習した規則性（赤い直線）')
plt.legend()
plt.grid(True)
plt.show()

```

**【読み取りポイント】**
赤い直線が、AI（モデル）が学習して導き出した「勉強時間と点数の関係性のルール」です。この赤い線を使えば、「7.5時間勉強した人は何点くらい取れそうか？」という**未知のデータの予測**ができるようになります。

---

### ステップ4：【評価】を行う

最後に、この赤い直線（モデル）が、実際のデータにどれくらい上手く当てはまっているか（どれくらい正確か）を「評価」します。今回は、実際の点（データ）と赤い線（モデルの予測）の「ズレ」を可視化してみましょう。

```python
# 3. 評価（予測と実際のズレを確認）
# 現在のデータに対するモデルの予測値を計算
predicted_scores = model.predict(study_hours)

# グラフに描画してズレを可視化
plt.figure(figsize=(8, 5))
plt.scatter(study_hours, test_scores, color='blue', label='Actual Data')
plt.plot(x_line, y_pred_line, color='red', linewidth=2, label='AI Model')

# 実際の点とモデルの予測（赤い線）のズレを緑の点線で表示
for i in range(len(study_hours)):
    plt.plot([study_hours[i], study_hours[i]], 
             [test_scores[i], predicted_scores[i]], 
             color='green', linestyle='--', alpha=0.6)

plt.xlabel('Study Hours (時間)')
plt.ylabel('Test Score (点)')
plt.title('[3. Evaluation] 実際のデータとモデルの予測のズレ（緑の点線）')
plt.legend()
plt.grid(True)
plt.show()

# ズレの大きさを数値で計算（平均二乗誤差）
error = mean_squared_error(test_scores, predicted_scores)
print(f"評価結果: モデルの予測と実際のデータのズレ（誤差の指標）は {error:.2f} です。")
print("※この数値が小さいほど、優秀なモデルと言えます。")

```

**【読み取りポイント】**
緑の点線が「予測と現実のズレ（誤差）」です。「評価」とは、このズレの大きさを客観的な数値で計算し、モデルの性能をテストすることです。

```

---

この構成であれば、「データ（青い点）を用意する」→「モデル（赤い線）を当てはめる」→「評価（緑の点線）でズレを確認する」というAIの基本サイクルを、数学の知識がなくても視覚的なストーリーとして理解できるはずです。

[cite_start]第1回の教材の骨格はこれでかなり固まりましたね。このまま第2回（AIの背景と論点）の構成案に進みましょうか？それとも、第3回の「機械学習の枠組み（交差検証など）」[cite: 30] のような、少し踏み込んだ内容のマテリアルを先に検討しますか？

```
