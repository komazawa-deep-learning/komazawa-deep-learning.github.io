---
title: 第 07 回 2026 年度開講 心理学特講 IIIA 駒澤大学 
author: 浅川 伸一
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="center">
<font size="+1" color="navy"><strong>計算モデルによる課題の理解：認知課題から神経心理学検査への適用</strong></font><br/><br/>
</div>

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 29/May/2026<br/>
Appache 2.0 license<br/>
</div>

# 07440 心理学特講ⅢA - 第 07 回: IAM, Dell モデル

* [課題提出フォルダ](https://drive.google.com/drive/u/6/folders/1wYaBn4dovEwtlOfOhcAFP2bJdyDqM9ZL){:target="_blank"}
* [実習コード <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2026notebooks/2026psy3a_lect07_iam_dell_model.ipynb){:target="_blank"}


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

# Dell model (Foygell & Dell, 2000)


<div class="figcenter">
<img src="/2026assets/2000Foygell_Dell_fig1.png" width="33%">
</div>

⸻

1. 研究の目的と背景

本論文の目的は、失語症者（特に音韻性錯語を示す症例）における語彙アクセス障害を、計算モデルによって説明・分類することであった。
背景には以下の問題意識：

* 失語症の語産生エラー（意味錯語・音韻錯語・混合錯語）はどの処理段階の障害から生じるのか？
* 単に「意味段階が壊れている」「音韻段階が壊れている」という局所的説明だけで十分か？
* 単一モデルで多様な失語パターンを説明できるのか？

この文脈で、著者らは Dell の相互活性化モデル（interactive spreading activation model） を基盤として、障害をパラメータ操作として定式化する。

⸻

2. 基本モデル：相互活性化型語彙産生モデル

モデルは以下の3層構造を持つ：

1. 意味層 (semantic features)
2. 語彙層 (lexical nodes)
3. 音韻層 (phonemes)

特徴：

* 活性化は双方向に伝播（top-down & bottom-up）
* 競合とノイズを含む確率的選択
* 語彙選択と音韻符号化が分離しつつ相互依存

⸻

3. 障害のモデル化（Impairment Manipulations）

本論文の核心は、障害を「どこが壊れたか」ではなく「どの計算的性質が変化したか」で表現する点にあります。

著者は主に以下の2系統の障害を操作します。

(A) 活性化伝播の低下（Connection Strength Reduction）

* 意味→語彙
* 語彙→音韻
* 双方向リンクの弱体化

(B) ノイズ増大（Increased Noise）

* 活性化更新過程にランダム性を注入

これらを連続量パラメータとして変化させることで、
異なる失語症プロファイルを再現。

⸻

4. シミュレーション結果：失語パターンの再現

4.1 音韻失語（phonological aphasia）

* 音韻錯語が多い
* 意味は保たれる

➡ 語彙→音韻結合の弱体化 + ノイズ増加で再現可能

⸻

4.2 意味失語（semantic aphasia）

* 意味錯語が多い
* 音韻構造は比較的正確

➡ 意味→語彙結合の弱体化で再現

⸻

4.3 混合錯語（mixed errors）

* 意味的にも音韻的にも関連する錯語（例：cat → rat）

➡ 双方向モデルでのみ自然に出現
➡ 一方向モデルでは説明困難

⸻

5. 重要な理論的主張

5.1 「段階特異的障害」への批判

* 同じエラー分布が
    異なるパラメータ組み合わせから生じうる
* 「意味段階が壊れている」という説明は過度に単純

👉 障害は連続的・分布的

⸻

5.2 単一アーキテクチャ仮説

* 健常者と失語症者で
    モデル構造は同一
* 違いは パラメータ値のみ

👉 これは後の

* connectionist neuropsychology
* graded impairment view
    の基礎となる考え方

⸻

6. 本論文の位置づけと影響

* Dell 系モデルを
    臨床失語データに本格適用
* 「障害＝構造破壊」から
    「計算特性の歪み」へ
* 混合錯語の説明における
    相互活性化モデルの優位性を明示

<!-- ⸻

7. 一文でのまとめ

Foygel & Dell (2000) は、語彙アクセス障害を「どの処理段階が壊れたか」ではなく、「相互活性化モデルにおける連結強度やノイズの連続的変化」として捉え、単一の計算アーキテクチャで多様な失語症エラーパターンを説明できることを示した。

⸻

もしご希望があれば次に：

* CDP / WEAVER++ / Levelt モデルとの対比
* 日本語音読・失語データへの適用可能性
* GP / VAE 的再解釈（ノイズ＝潜在変数）
* 図解（層構造＋障害操作）

などにも展開できます。 -->