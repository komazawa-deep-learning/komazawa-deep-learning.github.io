---
title: 第 08 回 2026 年度開講 心理学特講 IIIA 駒澤大学 
author: 浅川 伸一
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="center">
<font size="+1" color="navy"><strong>計算モデルによる課題の理解：認知課題から神経心理学検査への適用</strong></font><br/><br/>
</div>

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 05/Jun/2026<br/>
Appache 2.0 license<br/>
</div>

# 07440 心理学特講ⅢA - 第 08 回

* [課題提出フォルダ](https://drive.google.com/drive/u/6/folders/1wYaBn4dovEwtlOfOhcAFP2bJdyDqM9ZL){:target="_blank"}
* [実習コード <img src="/assets/colab_icon.svg">](){:target="_blank"}

<!-- https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2026notebooks/2026psy3a_lect07_iam_dell_model.ipynb){:target="_blank"}
 -->

<!-- 以下に、第7回の授業資料（Google Colaboratory用ノートブックおよび講義スライドの統合案）を提示する。学生の暗記主義を完全に破壊し、数理モデルを通じた神経心理学的症状の逆算を強制する設計としている。 -->

---

<!-- # 07440 心理学特講ⅢA - 第7回: 語彙アクセスのモデル化（局所表現とWABへの接続）

## 1. 授業の戦略的要件

本日の目的は、単語を読むという行為が「単一のブラックボックス」ではなく、複数の経路（カスケード）と階層間の相互作用によって成立している事実を、数理的に証明することである。
現象（例：単語優位効果や失読症）の名前を暗記することは一切評価しない。「ネットワークのどの行列（重み）が機能したか」、あるいは「どこが物理的に断線したか」というアーキテクチャの観点からのみ事象を語れ。 -->

## 2. 局所表現ネットワークと対話活性化モデル（IAM）

視覚的な単語認知は、「特徴層」→「文字層」→「単語層」という階層構造を持つ。
ここで決定的に重要なのは、情報が下から上（ボトムアップ）へ流れるだけでなく、**上の階層（単語）から下の階層（文字）へ向けた興奮性のフィードバック（トップダウン）が存在する**という構造的制約である。

### 2.1. 実習：単語優位効果のシミュレーション

人間は、ランダムな文字列（非語）の中にある文字よりも、意味のある単語の中にある文字の方を速く正確に認識できる（単語優位効果）。これを「意味があるから速い」という文学的な解釈で終わらせてはならない。
以下のコードを実行し、ネットワーク構造がこの現象をどう必然的に引き起こすかを観察せよ。

```python
import numpy as np
import matplotlib.pyplot as plt

def simulate_word_superiority(condition, cycles=50):
    # --- 1. ネットワークの初期化 ---
    # 文字層 (5ノード): [ T(1文字目), D(1文字目), X(1文字目), O(2文字目), X(2文字目) ]
    letters = np.zeros(5)
    # 単語層 (2ノード): [ "TO", "DO" ]
    words = np.zeros(2)

    # --- 2. 重み行列の定義 (アーキテクチャの配線) ---
    # 【ボトムアップ重み】 (文字層 -> 単語層)
    W_L2W = np.array([
        [ 1.0, -0.2], # T(1) は TO を興奮させ、DO を抑制
        [-0.2,  1.0], # D(1) は DO を興奮させ、TO を抑制
        [-0.5, -0.5], # X(1) は どの単語の構成要素でもないため両方を抑制
        [ 1.0,  1.0], # O(2) は TO と DO の両方を興奮
        [-0.5, -0.5]  # X(2) は 両方を抑制
    ])

    # 【トップダウン重み】 (単語層 -> 文字層)
    # ※ここが単語優位効果のコアエンジンである
    W_W2L = np.array([
        [ 1.0,  0.0,  0.0,  1.0,  0.0], # "TO" が発火すれば、T(1) と O(2) にフィードバックを送る
        [ 0.0,  1.0,  0.0,  1.0,  0.0]  # "DO" が発火すれば、D(1) と O(2) にフィードバックを送る
    ])

    # 【単語層内の側抑制】 (層内の競合)
    W_W2W_inh = np.array([
        [ 0.0, -0.5],
        [-0.5,  0.0]
    ])

    # --- 3. 入力刺激の設定 ---
    # ターゲットは「2文字目の 'O' (インデックス3)」の活性化速度
    if condition == "word":
        ext_input = np.array([1.0, 0.0, 0.0, 1.0, 0.0]) # "TO"
    elif condition == "nonword":
        ext_input = np.array([0.0, 0.0, 1.0, 1.0, 0.0]) # "XO"
    else:
        raise ValueError("無効な条件")

    tau = 0.1
    decay = 0.05
    history_target_O = []

    # --- 4. 時間ステップごとの情報処理 ---
    for _ in range(cycles):
        # 単語層の更新: (ボトムアップ) + (側抑制)
        net_words = np.dot(letters, W_L2W) + np.dot(words, W_W2W_inh)
        words = np.maximum(0, words + tau * net_words - decay * words)

        # 文字層の更新: (視覚入力) + (トップダウン)
        net_letters = ext_input + np.dot(words, W_W2L)
        letters = np.maximum(0, letters + tau * net_letters - decay * letters)

        history_target_O.append(letters)

    return history_target_O

# --- 実行と可視化 ---
cycles = 50
history_word = simulate_word_superiority("word", cycles)
history_nonword = simulate_word_superiority("nonword", cycles)

plt.figure(figsize=(10, 6))
plt.plot(history_word, label="Target 'O' in Word ('TO')", color="blue", linewidth=3)
plt.plot(history_nonword, label="Target 'O' in Non-Word ('XO')", color="red", linestyle='--', linewidth=3)
plt.title("Simulation of Word Superiority Effect (IAM)", fontsize=14)
plt.xlabel("Time Steps (Processing Time)")
plt.ylabel("Activation of Target Letter Node 'O'")
plt.axhline(y=2.5, color='gray', linestyle=':', label="Recognition Threshold")
plt.legend()
plt.grid(True)
plt.show()

```

### 2.2. 破壊的検証（Lesion Simulation）

グラフを見て満足するな。この現象のメカニズムを証明するために、自らの手でモデルの脳を「損傷」させよ。

* **課題**: コード内の `W_W2L`（トップダウン重み行列）の要素をすべて `0.0` に書き換え、フィードバック経路を物理的に切断して再度実行せよ。
* **考察**: 青い線と赤い線が完全に重なることを確認しろ。これは、単語優位効果が「単語層からの逆流信号による文字ノードの底上げ」という数理的構造のみに依存していることの完全な証明である。

## 3. アーキテクチャの拡張：二重経路カスケードモデル（DRC）

IAM を拡張し、文字から音声へ至る全体像を定義する。読字の経路は 1 本ではない。

* **非語彙的経路（ルールベース）**
* 入力された文字を、音韻変換規則に従って機械的に音声に変換する経路。
* 日本語の「仮名」や、初めて見る単語（非語）の処理を担う。意味の理解は伴わない。


* **語彙・意味的経路（レキシコン経由）**
* 視覚的単語表象から「意味システム」を経由し、対応する音韻を出力する経路。
* 日本語の「漢字」や、例外的な読み方をする単語の処理を担う。


## 4. 臨床への接続：WAB（失語症検査）

神経心理学における失読症や錯読は、「魔法」でも「不可解な症状」でもない。DRCモデルの配線図における「特定の経路の断線（行列のゼロ化）」に過ぎない。

**思考実験：**
WABの検査対象者が以下の症状を示したとする。モデルの「どこ」が断線しているか特定せよ。

1. **表層失読（Surface Dyslexia）**
* **症状**: 「仮名」や無意味な文字列はすらすら読める。しかし、「漢字」が読めない、あるいは漢字を無理やり仮名読みのルールで読もうとする。
* **モデル解釈**: 経路A（非語彙的経路）は完全に生きている。しかし、**経路B（語彙・意味的経路）が断線している**ため、意味アクセスを必要とする表意文字の処理がバイパスされ、機械的な音声変換プロセスだけが空回りしている状態である。


2. **音韻失読（Phonological Dyslexia）**
* **症状**: 日常的に使う単語や「漢字」は読める。しかし、初めて見る無意味な文字列（非語）を与えられると全く読めなくなる。
* **モデル解釈**: 経路B（語彙・意味的経路）は生きている。しかし、**経路A（非語彙的経路）が断線している**ため、既存の辞書（レキシコン）に登録されていない新しい入力を、ルールに従って音に変換する機能が喪失している。



## 5. 小テスト（本質的理解の測定）

**Q1.**
WABの物品呼称検査（絵を見て名前を答える）において、「リンゴ」の絵を見て「ミカン」と答えてしまう（意味性錯語）患者がいる。しかし、この患者は「リンゴ」という単語の音声を聞かせると、正しく「リンゴ」と復唱することは可能である。
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