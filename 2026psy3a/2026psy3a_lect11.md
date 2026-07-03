---
title: 第 11 回 2026 年度開講 心理学特講 IIIA 駒澤大学 
author: 浅川 伸一
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="center">
<font size="+1" color="navy"><strong>計算モデルによる課題の理解：認知課題から神経心理学検査への適用</strong></font><br/><br/>
</div>

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 03/Jul/2026<br/>
Appache 2.0 license<br/>
</div>

# 07440 心理学特講ⅢA - 第 11 回

* [課題提出フォルダ](https://drive.google.com/drive/u/6/folders/1wYaBn4dovEwtlOfOhcAFP2bJdyDqM9ZL){:target="_b
  lank"}

* [線分二等分課題 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_1210bit_line_bisection.ipynb){:target="_blank"}
* [文字抹消課題 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/ShinAsakawa/ShinAsakawa.github.io/blob/master/2022notebooks/2022_1029bit_letter_cancellation_colab.ipynb){:target="_blank"}



* [フィラデルフィア絵画命名検査課題 PNT を転移学習 <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2021notebooks/2021_0618pnt_transfer_learning.ipynb){:target="_blank"}
* [転移学習による Stroop 効果のデモ  <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2023notebooks/2023_1123Stroop_model.ipynb)


## 半側空間無視


### BIT (Behavioral Inattention Tasks):

1. [線分抹消試験](/2026assets/IMG_LineCancellation.jpeg){:target="_blank"}
2. 文字抹消試験
3. [星印抹消試験](/2026assets/IMG_StarCancellation.jpeg){:target="_blank"}
4. 模写試験
5. [線分二等分試験](/2026assets/IMG_LineBisection.jpeg){:target="_blank"}
6. 描画試験

行動検査
1. 写真課題
2. 電話課題
3. メニュー課題
4. 音読課題
5. 時計課題
6. 硬貨課題
7. 書写課題
8. 地図課題
9. トランプ課題

### 症例

* [症例](/2026assets/2022_1017tateba_neglect_patient.jpg){:target="_blank"}
* [MRI 画像](/2026assets/IMG_BrainImage.jpeg){:target="_blank"}

### Parr & Friston (2017) の注意モデル

<div class="figcenter">
<img src="/2026assets/2017Parr_Friston_active_construction_fig3.jpg" width="49%">
</div>
<div class="figcaption">

Parr & Friston (2017) Fig. 3<br/>

背側および腹側の注意ネットワーク。
背側ネットワークと腹側ネットワークは、それぞれ前頭葉および頭頂葉の領域を包含している。背側領域 (前頭眼野（FEF）、外側頭頂内側野（LIP）、頭頂内側溝（IPS）などの領域を含む)  は上丘（SC）へと投射しており、これらの領域が眼球運動の制御に直接関与していることを示唆している。なお、これらの頭頂野は、頭頂眼野（Shipp, 2004）と呼ばれることもある。これらの領域は、上縦束第 1 枝（SLF I）によって接続されている。腹側ネットワークは、腹側前頭皮質（VFC）の領域と、側頭頭頂接合部（TPJ）に近い領域から構成されている。これらは、上縦束第 3 枝（SLF III）によって接続されている。SLF II は、腹側ネットワークの頭頂部と背側ネットワークの前頭部を接続している。この模式図は、（Corbetta and Shulman, 2002）および（Thiebaut de Schotten et al., 2011）の記述に基づく。
<!-- The dorsal and ventral attentional networks.
The dorsal and ventral networks each involve both frontal and parietal regions. The dorsal areas – including those in the region of the frontal eye fields (FEF), the lateral intraparietal (LIP) area and the intraparietal sulcus (IPS) – project to the superior colliculus (SC), suggesting a direct involvement of these areas in the control of eye movements. Note that these parietal areas are sometimes referred to as the parietal eye fields (Shipp, 2004). These areas are connected by the first branch of the superior longitudinal fasciculus (SLF I). The ventral network is made up of areas in the ventral frontal cortex (VFC) and areas close to the temporoparietal junction (TPJ). These are connected by the third branch of the SLF (SLF III). SLF II connects the parietal part of the ventral network to the frontal part of the dorsal network. This schematic is based on the descriptions in (Corbetta and Shulman, 2002) and in (Thiebaut de Schotten et al., 2011). -->

</div>


### 大脳皮質の接続と注意<!-- ### 4. Cortical connections and attention-->

上丘に直接投射する大脳皮質領域には、「背側注意ネットワーク」（Corbetta et al., 2000; Szczepanski et al., 2013）に関連する前頭葉（Künzle and Akert, 1977）および頭頂葉（Gaymard et al., 2003）領域の両方が含まれる。これは、fMRI を用いて、注意課題中の信号変化に基づいて定義された一連の大脳皮質領域である（Corbetta and Shulman, 2002）。これらの領域における活動は主に両側性である（Kastner et al., 1999; Hopfinger et al., 2000）が、一部の課題では非対称性が確認されている（Corbetta et al., 2002; Szczepanski et al., 2010）。背側ネットワークの各領域における半球間の差異は、経頭蓋磁気刺激（TMS）を含む因果的操作によっても引き出されている（Szczepanski and Kastner, 2013）。ただし、ネットワーク全体としてはほぼ対称であることが判明している。眼球運動の制御に関与する領域として予想される通り、注意が向けられた視野の対側半球において、より大きな反応が認められた。これらの領域は、上縦束（SLF）と呼ばれる白質束によって接続されている。SLF は 3 つの枝から構成されており（Makris, Kennedy et al., 2004）、そのうち最初の枝が前頭頭頂野の背側ネットワークを接続している（Thiebaut de Schotten et al., 2011）（図 3 参照）。残りの 2 つの枝は、「腹側注意ネットワーク」の各領域同士を結びつけ、また背側ネットワークと腹側ネットワークを相互に接続している。
<!--The cortical regions that project directly to the superior colliculus include both frontal (Künzle and Akert, 1977) and parietal (Gaymard et al., 2003) areas associated with the ‘dorsal attentional network’ (Corbetta et al., 2000; Szczepanski et al., 2013). This is a set of cortical regions which have been defined, using fMRI, on the basis of their signal changes during attentional tasks (Corbetta and Shulman, 2002). The activity in these areas is largely bilateral (Kastner et al., 1999; Hopfinger et al., 2000), but asymmetries have been found for some tasks (Corbetta et al., 2002; Szczepanski et al., 2010). Interhemispheric differences in regions of the dorsal network have also been elicited through causal manipulations, including transcranial magnetic stimulation (Szczepanski and Kastner, 2013), although the network as a whole was found to be approximately symmetrical. As might be expected for a region involved in directing eye movements, greater responses were found in the hemisphere contralateral to the visual field which was attended. These regions are connected by a white matter tract called the superior longitudinal fasciculus (SLF). The SLF is made up of three branches (Makris, Kennedy et al., 2004), and it is the first of these which connects the dorsal network of frontoparietal areas (Thiebaut de Schotten et al., 2011) (see Fig. 3). The other two branches connect the regions of the ‘ventral attention network’ to each other, and connect the dorsal and ventral networks to one another. -->


<!--#### 4.1. 前運動の野理論<!-- #### 4.1. The premotor theory-->

<!-- 注意に関する前運動野理論（Rizzolatti et al., 1987）は、これらの解剖学的観察結果から根拠を得ている。というのも、「注意」ネットワークは、眼球運動の制御に関与するネットワークと大幅に重なっているからである（Büchel et al., 1998; Corbetta et al., 1998; Nobre et al., 2000）。この理論の前提は、特定の場所への（顕在的な）注意の配分が、その場所へのサッカードを行うことと同等であるというものである。また、たとえそのサッカードが実行されなくても、ある位置へのサッカードを計画することで、その位置に（顕在的ではない）注意を向けることもできる。この理論を裏付ける行動学的証拠は、アイトラッキング研究から得られており、そこでは、顕在的でない注意の向け方がサッカードの軌道を体系的に変化させることが示されている（Sheliga et al., 1994, 1995）。心理物理学的測定結果もこれと一致しており、サッカード目標位置では、視野の他の位置と比較して刺激の識別能力が高まっている（Deubel and Schneider, 1996）。さらなる証拠は、外転神経（CN VI）の麻痺を有する患者から得られている（図1参照）。これらの損傷により、患側で眼を外転させることができなくなる。検出課題において、前運動理論と一致して、これらの患者は、サッカードを向けることが不可能な位置に刺激が提示された場合、隠れた注意に特徴的な反応時間の短縮を示さない（Craighero et al., 2001）。この理論を支持する生理学的証拠は説得力がある。サルの前頭眼野ニューロンを刺激することで、サッカード眼球運動を引き起こすことが可能である。これらの同じ細胞に対して閾値以下の刺激を与えると、そのニューロンのサッカード標的位置に提示された刺激の検出性能が向上する（Moore and Fallah, 2001）。議論の余地がないわけではないが（Smith and Schenk, 2012）、前運動理論は、注意と眼球運動の間の重要な関係、および両者に共通する解剖学的構造を浮き彫りにしている。 -->
<!--The premotor theory of attention (Rizzolatti et al., 1987) draws evidence from these anatomical observations, as ‘attentional’ networks overlap substantially with those involved in eye movement control (Büchel et al., 1998; Corbetta et al., 1998; Nobre et al., 2000). The premise of this theory is that the allocation of (overt) attention to a given location is equivalent to making a saccade to that location. Attention can also be covertly directed to a location by planning a saccade to it, even if this saccade is not performed. The behavioural evidence for this theory comes from eye tracking studies in which the deployment of covert attention has been shown to systematically alter the trajectory of saccades (Sheliga et al., 1994, 1995). Psychophysical measures are consistent with this, as stimulus discrimination is enhanced at saccade target locations compared to other visual field locations (Deubel and Schneider, 1996). Further evidence comes from patients with palsies of the abducens (CN VI) nerve (see Fig. 1). These injuries result in an inability to abduct the eye on the affected side. In a detection task, consistent with the premotor theory, these patients do not show the reduced reaction time characteristic of covert attention when the stimulus is placed in a location which is impossible for them to perform a saccade to (Craighero et al., 2001). Physiological evidence in favour of the theory is compelling. By stimulating frontal eye field neurons in the monkey, it is possible to cause saccadic eye movements. Subthreshold stimulation of these same cells increases detection performance of stimuli presented at the saccadic target location of those neurons (Moore and Fallah, 2001). While not uncontroversial (Smith and Schenk, 2012), the premotor theory highlights the important relationship between attention and eye movements, and the anatomical structures common to both. -->

<!--#### 4.2. アクティブ推論<!-- #### 4.2. Active inference-->

<!-- 顕著な位置が（潜在的または顕在的な）サッカード目標としてどのように選択されるかという問題は、多くの理論的研究を喚起してきた。この問題に取り組むために、ベイズ的枠組みが広く用いられてきた（Chikkerur et al., 2010）。これには、情報理論的な量を用いて顕著性や驚きを定義することも含まれる（Itti and Koch, 2000; Itti and Baldi, 2006）。さらに最近では、この問題はアクティブ推論の観点から定式化されている（Friston et al., 2012a, b; Mirza et al., 2016）。これは、適応的な（生きた）系が、有意義な形で存続し続けるためには、その状態の分散を最小限に抑えなければならないという原理から導かれた理論である（Friston et al., 2006）。この理論の帰結として、生物は、自身の感覚の原因に関する不確実性を最も解消できる感覚環境の部分を（例えば、サッカードを行うことによって）サンプリングすべきである。この過程に最も適した位置を選択するために、生物は感覚データがどのように生成されるかに関する確率モデルを備えており、これには自身の行動に関する信念が含まれている（Friston et al., 2012a, b）。これは、生物が遭遇する感覚に関する予測を生成するために用いられる。感覚データが与えられた際、このモデルに対して近似ベイズ逆推定を行うことにより、生物は自身の最適なポリシー（行動の連鎖）を推論することができる。この文脈における「最適」とは、不確実性を最大程度に低減させる、あるいは同等に言えば、最大の情報利得をもたらす感覚を能動的にサンプリングすることを意味する。これは「内在的価値」としても知られており、数学的には、前述の定式化における顕著性を裏付ける期待ベイジアン・サプライズである（Itti and Koch, 2000; Itti and Baldi, 2006）。一連の古典的な反射弧は、暗黙の生成モデルに基づいてなされた予測を満たすことができる（Friston et al., 2016a, b）。このベイズ最適・認識論的・不確実性解消型の定式化の重要な側面は、すべての可能なサッカードの位置の表象の中から、その顕著性または認識論的価値に基づいて最適なサッカードが選択されることを示唆している。ひいては、これは顕著性マップの存在を意味する。そこでは、考えられるすべてのサッカード位置の認識的価値が評価される。これは、上丘の深層における活動のモデルとして上述したアトラクタダイナミクスに対する補完的な視点、すなわち顕著性の符号化を提供する可能性がある。 -->
<!--The question of how a salient location is selected as a (covert or overt) saccadic target has stimulated much theoretical study. Bayesian frameworks have been extensively employed to address this question (Chikkerur et al., 2010), including definitions of salience, and surprise, in terms of information theoretic quantities (Itti and Koch, 2000; Itti and Baldi, 2006). More recently, this question has been formulated in terms of Active Inference (Friston et al., 2012a, b; Mirza et al., 2016). This is a theory derived from the principle that adaptive (living) systems must minimise the dispersion of their states in order to continue to exist in a meaningful way (Friston et al., 2006). A consequence of this theory is that organisms should sample (e.g. by performing a saccade to) the parts of the sensory environment that resolve most uncertainty about the causes of their sensations. In order to select the locations that best serve this process, they are equipped with a probabilistic model of how sensory data is generated, which includes beliefs about their own actions (Friston et al., 2012a, b). This is used to generate predictions about the sensations they will encounter. By performing an approximate Bayesian inversion of this model, given sensory data, organisms are able to infer their own optimal policy (sequence of actions). Optimal in this context means the active sampling of sensations that afford the greatest reduction in uncertainty or, equivalently, the greatest information gain. This is also known as intrinsic value and, mathematically, is the expected Bayesian surprise that underwrites salience in the earlier formulations above (Itti and Koch, 2000; Itti and Baldi, 2006). A set of classical reflex arcs can then fulfil the predictions made under the implicit generative model (Friston et al., 2016a, b). A key aspect of this Bayes optimal, epistemic, uncertainty resolving formulation implies that the best saccade is selected from representations of all possible saccades, according to their salience or epistemic value. In turn, this implies the existence of a salience map; where the epistemic values of all possible saccade locations are evaluated. This may provide a complementary perspective on the attractor dynamics discussed above as models of activity in the deep layers of the superior colliculus; namely, an encoding of salience.  -->

#### 空間的半側無視と注意ネットワーク<!-- #### 4.3. Spatial hemineglect and attentional networks-->

空間的半側無視の患者では、皮質病変により、場面のサッカードによるサンプリングに側方への偏りが生じることがある。典型的には、空間の右側へのサッカードの頻度が、左側と比較して増加する。これは、無視された半視野へのサッカード生成の障害というよりは、サッカードの標的選択に関連しているようである（Bartolomeo and Chokron, 2002）。直感的には、病変部位はサッカード制御に直接関与する背側前頭葉および頭頂葉領域に対応すると予想される。しかし、無視に関連する皮質病変は前頭葉および頭頂葉の両方に生じ得るものの、通常は前頭眼野や頭頂間溝よりも腹側に位置している（Corbetta and Shulman, 2002）。前頭眼野を病変させると無視に類似した症候群が誘発される（Latto and Cowey, 1971）が、これは一時的なものに過ぎない。さらに、前述の通り、「背側注意ネットワーク」は左右対称に分布している。これは、右半球の病変後に空間的半側無視がはるかに多く見られるという観察結果とは対照的である。行動上の相関関係から、皮質に起因する半側無視が背側ネットワークの機能障害を排除するとは考えにくいものの、上記の観察結果からは、これが他の構造の機能障害に二次的に起因している可能性が高いことが示唆される。
<!--In spatial hemineglect patients, cortical lesions can induce a lateral bias in the saccadic sampling of a scene. Typically, the frequency of saccades to the right side of space is increased, compared to the left. This appears to be related to the selection of saccadic targets, rather than an impairment in the production of saccades to the neglected hemifield (Bartolomeo and Chokron, 2002). Intuitively, one might expect the lesion sites to correspond to the dorsal frontal and parietal regions directly involved in saccadic control. However, although cortical lesions associated with neglect can occur in both frontal and parietal regions, they are typically more ventral than the frontal eye fields or the intraparietal sulcus (Corbetta and Shulman, 2002). A neglect-like syndrome can be elicited by lesioning the frontal eye fields (Latto and Cowey, 1971), but this is only temporary. Additionally, as noted above, the ‘dorsal attentional network’ is symmetrically distributed. This contrasts with the observation that spatial hemineglect is much more common following a right hemispheric lesion. While the behavioural correlates render it unlikely that cortically driven neglect precludes no dysfunction of the dorsal network, the above observations indicate that this is likely to be secondary to the disruption of other structures. -->

無視症におけるサッカード運動の側方偏位は、上丘への皮質からの入力がしばしば保たれているという事実と整合する。無視症に関連するより腹側の前頭頭頂野は、「腹側注意ネットワーク」（Corbetta and Shulman, 2002, 2011）と重なり合っている。背側ネットワークとは対照的に、腹側ネットワークは右半球でより顕著であり、これは右半球の病変に続く空間無視の頻度が高いこととも一致している。これらの領域は SLF 第 3 枝によって接続されており、この第 3 枝は右半球で体積が大きいことが知られている（Thiebaut de Schotten et al., 2011）。このネットワークの腹側頭頂葉領域は、SLF 第 2 枝を介して背側ネットワークの前頭葉領域と接続されている。これは、腹側ネットワークが、脳幹のサッカード生成領域へ投射する皮質部位に直接影響を及ぼすことを意味する。
<!-- The lateral biasing of saccadic movements in neglect can be reconciled with the fact that the cortical inputs to the superior colliculus are often preserved. The more ventral frontoparietal regions which are associated with neglect overlap with the ‘ventral attentional network’ (Corbetta and Shulman, 2002, 2011). In contrast to the dorsal network, the ventral network is more prominent in the right hemisphere, consistent with the greater frequency of spatial neglect following right hemispheric lesions. These regions are connected by the third branch of the SLF, which is known to have a greater volume in the right hemisphere (Thiebaut de Schotten et al., 2011). The ventral parietal regions of this network are connected to the frontal regions of the dorsal network by the second branch of the SLF. This means that the ventral network directly influences the cortical sites that project to the saccade generating areas of the brainstem. -->

SLF 第 2 枝は、いくつかの興味深い側性化した行動的相関と関連している。健常者では、特定の条件下で「疑似無視」が誘発されることがある（Bowers and Heilman, 1980; Jewell and McCourt, 2000）。これは、半側無視の評価にも用いられる「線分二等分課題」において実証されている。この課題では、被験者は水平線の中心点と思われる位置に印をつける。半側無視患者は通常、正中線の右側に印をつけるが、健常者においても左側へのわずかなずれが生じることがある。この「疑似無視」が生じる程度は、右 SLF II の体積と関連している。その体積が大きいほど、左側へのずれは大きくなる（Thiebaut de Schotten et al., 2011）。無視は、SLF を介した前頭頭頂間の相互作用が断絶された「断絶症候群」であるとの仮説が提唱されている（Bartolomeo et al., 2007; He et al., 2007）。この構造的観点に基づく仮説は、正常な注意機能には背側ネットワークと腹側ネットワーク間の相互作用が必要であるという機能的観点からの提唱を補完するものである（Corbetta and Shulman, 2002）。病変研究からも、これを裏付ける証拠がいくつか存在する。例えば、患者間の病変の重複を調べたある研究では、SLF において皮質下領域の重複が最大であることが示された（Doricchi and Tomaiuolo, 2003）。症例報告（Ciaraffa et al., 2013）もこの知見を裏付けており、SLF II の損傷が半側無視の有力な予測因子であるという観察結果によって、この知見はさらに強められている（Thiebaut de Schotten et al., 2014; Lunven et al., 2015）。これに加え、手術中に電気刺激によって右 SLF を不活性化すると、線分二等分課題において一時的な右側への逸脱が生じた（Thiebaut de Schotten et al., 2005）。
<!-- The second branch of the SLF has been associated with some interesting lateralised behavioural correlates. In normal subjects, under certain conditions, a ‘pseudo-neglect’ can be elicited (Bowers and Heilman, 1980; Jewell and McCourt, 2000). This has been shown for a line bisection task, also used to assess hemineglect, in which a subject marks what they believe to be the midpoint of a horizontal line. While hemineglect patients typically mark to the right of the midline, small deviations to the left can occur in healthy subjects. The degree to which this ‘pseudo-neglect’ occurs is related to the volume of the right SLF II. The larger this is, the greater the leftward deviation (Thiebaut de Schotten et al., 2011). It has been proposed that neglect represents a disconnection syndrome, in which the frontoparietal interactions mediated by the SLF have been disrupted (Bartolomeo et al., 2007; He et al., 2007). This structurally motivated hypothesis complements the functionally motivated suggestion that an interaction between the dorsal and ventral networks is necessary for normal attentional function (Corbetta and Shulman, 2002). There is some evidence for this from lesion studies. For example, one study looking at lesion overlaps between patients found maximal subcortical overlaps in the SLF (Doricchi and Tomaiuolo, 2003). Case reports (Ciaraffa et al., 2013) endorse this finding, which is further strengthened by the observation that SLF II damage is a good predictor of hemineglect (Thiebaut de Schotten et al., 2014; Lunven et al., 2015). In addition to this, inactivation of the right SLF by electrical stimulation during surgery caused a temporary rightward deviation in the line bisection task (Thiebaut de Schotten et al., 2005).  -->


#### 背側と腹側<!-- #### 4.4. Dorsal versus ventral-->

背側ネットワークと腹側ネットワークの区別は、背側視覚経路と腹側視覚経路の区別を反映している（Goodale and Milner, 1992）。これらはしばしば「何  what」の視覚経路と「どこ where」の視覚経路と呼ばれ、前者は刺激の同一性を、後者は刺激の位置を表しているように見える（Ungerleider and Haxby, 1994）。物体は空間内の位置にかかわらずその同一性を保つことを踏まえると、脳はこれらを独立した要因として扱っているようだ。確率的推論において、これは「平均場近似」と呼ばれる（Friston and Buzsáki, 2016）。もし背側および腹側の注意ネットワークが同様の因数分解を表しているならば、これは後者のネットワークの側性化と、前者の対称性について直感的な説明となり得る。各半球には、空間の対側に関する地図が含まれていると考えられている（Wandell et al., 2007）。したがって、「どこ where」経路に関連するより背側の領域が比較的対称的であることは驚くべきことではない。しかし、これらの変数の因数分解により、刺激の同一性は特定の場所での表象を必要としない。そのため、「何 what」流路には片側性の表象で十分である。これは臨床神経心理学的観察とも一致する。すなわち、右腹側視覚経路の領域に病変が生じると物体認識障害を引き起こす可能性がある（Warrington and James, 1967, 1988; Warrington and Taylor, 1973）一方で、左側の同所性領域は物体の命名困難と関連する可能性が高いからである（Kirshner, 2003）。これは腹側ネットワークの側性化を説明し得るものであり、背側ネットワークに対するその影響を考慮すれば、右半球に病変を持つ患者において空間的無視の有病率が高いこととも整合する。2 つのネットワーク間の接続は、刺激や場面の同一性に関する不確実性を解消するために、視線を異なる位置に向ける必要性によって必然的に求められるものとなる。この見解によれば、右 SLF II は同一性を表す領域と左方向への眼位を表す領域とを接続しているため、この構造の損傷は左側のサッカード標的の選択を損なうことになる。なお、この病理学的非対称性に関する一般的な代替説として、右半球は空間の左右両方を表象するのに対し、左半球は右側のみを表象するという説がある（Mesulam, 1999）。また、腹側ネットワークの病変が、対側領域よりも右背側ネットワークに及ぶ可能性が高いという説も妥当である。この説明によれば、半側無視は両方のネットワークに病変が生じた場合に発生するとされる。
<!--The distinction between the dorsal and ventral networks mirrors the distinction between the dorsal and ventral visual pathways (Goodale and Milner, 1992). These are often referred to as the ‘what’ and ‘where’ visual pathways, as the former appears to represent stimulus identity, while the latter represents stimulus location (Ungerleider and Haxby, 1994). Given that an object retains its identity, regardless of its position in space, the brain appears to have treated these as independent factors. In probabilistic inference, this is referred to as a ‘mean field approximation’ (Friston and Buzsáki, 2016). If the dorsal and ventral attention networks represent a similar factorisation, this could provide an intuitive explanation for the lateralisation of the latter network, and the symmetry of the former. Each hemisphere is thought to contain maps of the contralateral side of space (Wandell et al., 2007). It is unsurprising then that more dorsal regions, associated with the ‘where’ pathway, are relatively symmetrical. However, stimulus identity does not require representation in a specific location, due to the factorisation of these variables. As such, a unilateral representation is sufficient for the ‘what’ stream. This is consistent with clinical neuropsychological observations, as lesions to regions in the right ventral visual pathway are can give rise to disorders of object recognition (Warrington and James, 1967, 1988; Warrington and Taylor, 1973), while the homologous regions on the left are more likely to be associated with difficulty naming objects (Kirshner, 2003). This could explain the lateralisation of the ventral network and, given its influence over the dorsal network, is consistent with the higher prevalence of spatial neglect among patients with right hemispheric lesions. The connection between the two networks would be mandated by the need to direct the eyes to different locations to resolve uncertainty about a stimulus or scene identity. According to this view, as the right SLF II connects the regions representing identity to those representing eye positions towards the left, damage to this structure impairs the selection of left sided saccadic targets. Note that a popular alternative explanation for this pathological asymmetry is that the right hemisphere represents both left and right sides of space, while the left represents only the right side (Mesulam, 1999). It is also plausible that lesions to the ventral network are more likely to extend to the right dorsal network than to contralateral regions. This explanation requires that hemineglect occurs when there are lesions of both networks. -->



### deSchotten らの実験

<div class="figcenter">
<img src="/2026assets/2011deSchotten_latelized_fig1.png" style="width:44%;">
<img src="/2026assets/2011deSchotten_latelized_fig2.svg" style="width:44%;">
</div>
<div class="figcatpion">

**左:** 上縦束 第一，二，三肢 (SLF I, SLF II, SLF III) のサル (a) とヒト (b) の比較<br/>
**右:** 上縦束の解剖学的，行動的左右局在化。**a** 解剖学的所見，**b** 上縦束 第二肢 (SLF II) と線分二等分線の偏差との相関，**c** SLF II と Posner 課題における反応時間との相関，**d** 線分二等分課題と Posner 課題との相関
</div>


<!-- # モデル要約

* Corbetta モデルとは，左右の脳が独立に物体認識を行う物体認識器を有するが，回路切断器 (circuit braker) は右脳にのみ存在すると仮定する。
* Corbetta モデルにおいて，hemi-neglect とは回路切断機が動作しなければ，patinets with hemi-neglect は，新たな視覚対象を検出することができない。
* 半側空間無視患者の，左視野内にある視覚対象は，右脳の回路遮断器に信号を送ることができない，もしくは，回路遮断器への信号経路が途中で断線しているため，右半球頭頂葉に存する回路遮断器が動作しないと考
える。
* 腹側経路 what と背側経路 where とを別経路で処理する。
<!-- * 深層モデルは ResNet をバックボーンとして採用した。 -->
  <!-- * Regional CNN では，where にあたる bounding box の座標，例えば，網膜 2 次元地図上で，右上
と左下を表す 4 スカラを回帰させる，
  * および，その bounding box 内には何があるか what という 2 課題を分離可能である。 -->
<!-- * Faster R-CNN を用いて，腹側経路と背側経路を分離した。 -->
* 左右視野に S 字曲線上の検出率を仮定。 -->



<div class="figcenter">
<img src="/2022assets/2002CorbettaShulman_fig7.svg" width="49%">
<div style="width:77%;text-align:left;background-color:cornsilk">
</div>
</div>

### 転移学習の模式図

<div class="figcenter">
<img src="/assets/2017Ruder_fig1.jpg" width="39%">
<div style="width:77%;text-align:center; background-color:cornsilk">
</div></div>


### 二経路回路の例

<div class="figcenter">
<img src="/assets/ResNet_Fig2.svg" width="39%">
<img src="/assets/2016duelingNet.svg" width="39%">
<img src="/assets/1982Ungerleider_Mishkin.jpg" width="49%">
<div style="width:77%;text-align:center; background-color:cornsilk">
</div></div>


#### BIT 注意検査の線分二等分線課題のシミュレーション

<div class="figcenter">
<img src="/2026assets/2024_1109line_bisection_grandtruth.png" style="width:30%">
<img src="/2026assets/2024_1109line_bisection_prediction.png" style="width:30%">
<img src="/2026assets/2024_1109line_bisection_output.png" style="width:30%">
</div>


<div class="figcenter">
<img src="/2026assets/2023_0721bit_line_bisection_demo0.svg" width="42%">
<img src="/2026assets/2023_0721bit_line_bisection_demo1.svg" width="42%">
<div class="figcaption">
浅川・武藤 (準備中) より
</div></div>


#### 文字抹消課題

<div class="figcenter">
<img src="/2026assets/2024_1109letter_cancellation_grandtruth2.png" style="width:30%">
<img src="/2026assets/2024_1109letter_cancellation_prediction2.png" style="width:30%">
</div>


<div class="figcenter">
<img src="/2026assets/2024_1109line_cancellation_demo.png" style="width:30%">
<img src="/2026assets/2024_1109letter_cancellation_demo.png" style="width:30%">
</div>



# 考察とまとめ

一般画像認識モデルに対して，神経心理学検査における下位課題ごとに転移学習を行うことで，任意の課題を
解く健常モデルを作成し，
この健常モデルに対して，半側空間無視症例データを用いて，症状を模す症例モデルを提案した。
本研究に示す方法を用いることで，一般画像認識と，神経心理課題に特化した課題を解くモデルが作成できる
。
更に，症例ごとに微調整を行うことで，症状を記述するモデルを作成することが可能となった。

本研究で示した方法に従うことにより，画像認識モデルと人間の知覚あるいは認知課題との関係を考察するこ
とが可能となる。
このことは，臨床応用事例としても興味深く，今後，方法論の精緻化を進めることで，医療応用への発展が期
待できる。