---
title: "第01回 2026年度開講 駒澤大学 認知心理学研究 2b"
author: "浅川 伸一"
layout: home
mermaid: true
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="right">
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 18/Nov/2026<br/>
Appache 2.0 license<br/>
</div>

$$
\newcommand{\of}[1]{\left(#1\right)}
\newcommand{\Of}[1]{\left[#1\right]}
\newcommand{\KL}[2]{\operatorname{KL}\left(\left.{#1}\right\|{#2}\right)}
\newcommand{\given}[1]{\left|{#1}\right.}
\newcommand{\mb}[1]{\mathbf{#1}}
$$


* [オリベッティ顔データベースを用いた機械学習と畳み込みニューラルネットワーク <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2026notebooks/2026_0914olivetti_face_classification_demo.ipynb){:target="_blank"}

<div class="figcenter">
<img src="/assets/2019Glaser_fig2.jpg" width="39%">

<div class="memo">

左: Glaser+(2019) Fig.2, 右: Kriegeskorte+(2008) Fig.3

機械学習の 4 つ役割
1. 工学問題の解として
2. 予測変数の特定と改善
3. 単純モデルの評価とベンチマーク
4. 脳のモデルとして<br/>

</div></div>

<br/><br/>

<div class="figcenter" style="width:99%;">
<img src="/2024assets/2008Kriegeskorte_fig3.jpg" style="width:33%">　　　　　　<hspace style="width:33%"></hspace>
<img src="/2025assets/2020Bahg_GP_fig1.svg" style="width:44%">
<div class="figcaption">

左 Kriegeskorte+(2008) 図 3. 異なる表現を関連付けるハブとしての表現非類似性行列<!-- FIGURE 3. The representational dissimilarity matrix as a hub that relates different representations. --><br/>

A: システム神経科学は，3つの主要な研究分野，行動実験，脳活動実験，計算モデリングを関連付けるのに苦労してきた。
これまでは，これらの分野は主に 2 つのレベルで相互に作用してきた。<br/>
(1) 言語理論のレベルでの相互作用。すなわち，個別の分析から導き出された結論を比較することによる相互作用。
このレベルは不可欠であるが，定量的ではない。<br/>
(2) 特性関数のレベルで相互作用，例えば，心理測定関数と神経測定関数との比較。
この種の分野間の接触は同様に不可欠であり，定量的なものである。
しかし，特性関数は通常，少数のデータ点しか含まないため，そのインタフェースは情報的に豊かではない。
ここで示されている RDM は 4 つの条件のみに基づいているため，($(4^2-4)/2=$) 6 つのパラメータしか得られないことに注意。
しかし，パラメータの数は条件の数の 2 乗に比例して増えるため，RDM は異なる表現を関連付けるための情報豊富なインターフェースを提供できる。
例えば，ここで取り上げている 96 画像の実験では，行列のパラメータ数は $(96^{2}−96)/2=4,560$ となる。
<!-- **A**: Systems neuroscience has struggled to relate its three major branches of research: behavioral experimentation, brain-activity experimentation, and computational modeling.
So far these branches have interacted largely on two levels:
(1) They have interacted on the level of verbal theory, i.e., by comparing conclusions drawn from separate analyses.
This level is essential, but it is not quantitative.
(2) They have interacted at the level characteristic functions, e.g., by comparing psychometric and neurometric functions.
This form of bringing the branches in touch is equally essential and can be quantitative.
However, characteristic functions typically contain only a small number of data points, so the interface is not informationally rich. Note that the RDM shown is based on only four conditions, yielding only (42−4)/2=6 parameters.
However, since the number of parameters grows as the square of the number of conditions, the RDM can provide an informationally rich interface for relating different representations.
Consider for example the 96-image experiment we discuss, where the matrix has (962−96)/2=4,560 parameters. --><br/>

B: RDM が提供する量的インタフェースを介して，どのような異なる表現が関連付けられるかをより詳細に説明している。
ここでは，確立可能なモダリティ内での関係を説明するために，fMRI の例を任意に選択した。
これらの関係は，いずれも確立が困難であることに注意 (灰色の双方向矢印)。
<!-- **B**: This panel illustrates in greater detail what different representations can be related via the quantitative interface provided by the RDM.
We arbitrarily chose the example of fMRI to illustrate the within-modality relationships that can be established.
Note that all these relationships are difficult to establish otherwise (gray double arrows). -->

右: Bahg+(2020) 図 1. 心，脳，行動をつなぐフレームワーク<br/>
実験情報と構造情報が脳機能の生成モデルの構造を規定する。生成モデルは，反応時間，血中酸素濃度依存反応，脳波活動など，利用可能なすべての顕在変数を共同で説明するために使用される。本論文では，潜在ガウス過程を用いて顕在変数を連結し，モデルをデータに適合させることにより，最も妥当な連結関数が現れるようにする
</div></div>

```mermaid
graph TB
    LGN["LGN 網膜部位対応の明暗コントラスト情報"]
    LVC["LVC 低次視覚特徴表象"]
    VWFA["VWFA 書記素的単語形態表象"]
    ThalPulv["Thal-Pulv 選択的関与制御信号"]
    AG["AG 書記素音素意味統合表象"]
    STGPhon["STG-Phon 語彙的音韻表象"]
    SemSys["SemSys アモーダルな語彙概念的意味表象"]
    SMG["SMG 音韻系列の一時保持表象"]
    PFCBroca["PFC-Broca 構音音韻系列化情報"]
    PMPFC["PM-PFC 発話運動の時空間的系列計画情報"]
    ThalMot["Thal-Mot 統合された皮質運動野向け中継信号"]
    Cereb["Cereb 系列運動の時間的協調予測信号"]
    M1["M1-Artic 構音運動出力の終点"]
    Concept["ConceptSys 意味理解出力の終点"]

    LGN -->|網膜部位対応の明暗コントラスト情報| LVC
    LVC -->|低次視覚特徴表象| VWFA
    LVC -->|低次視覚特徴表象| ThalPulv
    ThalPulv -->|選択的関与制御信号| VWFA
    ThalPulv -->|選択的関与制御信号| AG
    ThalPulv -->|選択的関与制御信号| SemSys
    PFCBroca -->|関与駆動信号| ThalPulv
    ThalPulv -->|選択的関与制御信号| PFCBroca
    VWFA -->|書記素的単語形態表象| AG
    VWFA -->|書記素的単語形態表象| STGPhon
    AG -->|書記素音素意味統合表象| STGPhon
    AG -->|書記素音素意味統合表象| SemSys
    STGPhon -->|語彙的音韻表象| SemSys
    STGPhon -->|語彙的音韻表象| SMG
    SemSys -->|アモーダルな語彙概念的意味表象| PFCBroca
    SemSys -->|アモーダルな語彙概念的意味表象| Concept
    SMG -->|音韻系列の一時保持表象| PFCBroca
    PFCBroca -->|構音音韻系列化情報| PMPFC
    Cereb -->|系列運動の時間的協調予測信号| ThalMot
    PMPFC -->|発話運動の時空間的系列計画情報| ThalMot
    ThalMot -->|統合された中継信号| PMPFC
    ThalMot -->|統合された中継信号| M1

    classDef roiIn fill:#fff59d,stroke:#333,color:#000
    classDef noRoiInput fill:#90caf9,stroke:#333,color:#000
    classDef noRoiOutput fill:#a5d6a7,stroke:#333,color:#000

    class LVC,VWFA,ThalPulv,AG,STGPhon,SemSys,SMG,PFCBroca,PMPFC,ThalMot roiIn
    class LGN,Cereb noRoiInput
    class M1,Concept noRoiOutput

    subgraph legend["凡例"]
        L1["ROI内"]:::roiIn
        L2["noROI input"]:::noRoiInput
        L3["noROI output"]:::noRoiOutput
    end
```

## 色の凡例

- 黄色（roiIn）: ROI内のUC（`LVC`, `VWFA`, `Thal-Pulv`, `AG`, `STG-Phon`, `SemSys`, `SMG`, `PFC-Broca`, `PM-PFC`, `Thal-Mot`）
- 青色（noRoiInput）: ROI外からの入力UC（`LGN`, `Cereb`）
- 緑色（noRoiOutput）: ROI外への出力UC（`M1-Artic`, `ConceptSys`）

