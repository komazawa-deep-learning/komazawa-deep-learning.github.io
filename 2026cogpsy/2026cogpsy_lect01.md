---
title: "第01回 2026年度開講 駒澤大学 認知心理学研究 2b"
author: "浅川 伸一"
layout: home
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

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

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

