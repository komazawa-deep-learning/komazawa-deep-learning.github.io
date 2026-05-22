---
title: 第 06 回 2026 年度開講 心理学特講 IIIA 駒澤大学 
author: 浅川 伸一
layout: home
---
<link href="/css/asamarkdown.css" rel="stylesheet">

<div align="center">
<font size="+1" color="navy"><strong>計算モデルによる課題の理解：認知課題から神経心理学検査への適用</strong></font><br/><br/>
</div>

<div align='right'>
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 22/May/2026<br/>
Appache 2.0 license<br/>
</div>

# 07440 心理学特講ⅢA - 第6回: 視覚探索課題

* [課題提出フォルダ](https://drive.google.com/drive/u/6/folders/1wYaBn4dovEwtlOfOhcAFP2bJdyDqM9ZL){:target="_blank"}
* [実習コード <img src="/assets/colab_icon.svg">](https://colab.research.google.com/github/komazawa-deep-learning/komazawa-deep-learning.github.io/blob/master/2026notebooks/2026psy3a_lect06_visual_search.ipynb){:target="_blank"}



<div class="figcenter">
<img src="/2026assets/1980Treisman_fig1.svg" width="33%">
<img src="/2026assets/1980Treisman_tab1.svg" width="60%">
</div>

* **刺激**: 刺激の表示は、白いカードに文字のステンシルと色インクを用いて手作業で作成した。妨害刺激は、体系的な無作為化手順は用いなかったものの、ランダムに見える位置にカード上に散りばめられた。各条件において、1、5、15、30 個の項目からなる 4 種類の表示サイズが用いられた。すべての表示サイズにおいて、14×8° の視野角が用いられた。これにより、項目数が少ない表示は密度が低くなるが、中心窩からの平均距離はほぼ一定に保たれた。各文字の視野角は 0.8×0.6° であった。条件間で目標の位置が体系的に変動しないようにするため、各カードの領域は 8 つのセクションに分割された。これは、2 本 の対角線と、8.5°×5.5° の視角を占める内側の楕円形の境界線を重ね合わせることで行われた。各条件および各表示サイズについて、8 枚のカードが作成され、それぞれに生成された 8 つの領域（上外側、上内側、左外側、左内側、右外側など）のいずれかにターゲットがランダムに配置された。また、各条件および表示サイズごとに、ターゲットが含まれていないカードがさらに 8 枚用意された。
<!-- Stimuli. The stimulus displays were made by hand, using letter stencils and colored inks on white cards. The distractors were scattered over the card in positions which appeared random, although no systematic randomization procedure was used. Four different display sizes, consisting of 1, 5, 15, and 30 items were used in each condition. An area subtending 14x8° was used for all display sizes, so that the displays with fewer items were less densely packed, but the average distance from the fovea was kept approximately constant. Each letter subtended 0.8 x 0.6°. To ensure that the target locations did not vary systematically across conditions, the area of each card was divided into eight sections. This was done by superimposing a tracing of the two diagonals and an inner elliptical boundary, which subtended 8.5° x 5.5°. For each condition and each display size, eight cards were made, one with a target randomly placed in each of the resulting eight areas (top outer, top inner, left outer, left inner, right outer, etc.). Another eight cards in each condition and display size contained no target.-->

両条件における妨害刺激は、$T_{茶} と X_{緑} であり、各カード上で可能な限り同数になるように配置された。結合条件におけるターゲットは T_{緑} であり、特徴条件では青い文字または S であった。青い文字（T_{青} または X_{青}）は形状において半数の妨害刺激と一致し、S（S_{茶} または S_{緑}）は色において半数の妨害刺激と一致した。特徴条件では 4 つの異なる目標刺激が存在した（定義上は「青 または S」のみとされていた）という事実が、むしろ結合条件に比べて成績を低下させるはずである。
<!-- The distractors in both conditions were T_{brown} and X_{green} in as near equal numbers on each card as possible. The target in the conjunction condition was T_{green} in the feature condition, it was either a blue letter or an S. The blue letter (T_{blue} or X_{blue}) matched half the distractors in shape, and the S (S_{borwn} or S_{green}) matched half the distractors in color. The fact that there were four possible disjunctive targets in the feature condition (although the definition specified only "blue or S"), should, if anything, impair performance relative to the conjunction condition. -->

* **手続き**: 刺激カードは Electronics Development 社製の 3 フィールドタキストスコープで提示され、反応時間は以下に記述するように記録された。
<!-- Procedure.  The stimulus cards were presented in an Electronics Development three field tachistoscope and RT was recorded as described below. -->

各試行の開始時、被験者はタキストスコープ内で無地の白いカードを視認し、両手の親指をそれぞれ反応キーの上に置いた。実験者は ready と声に出して合図し、ボタンを押して中央に注視点を有する 2 枚目の白いカードを表示した。このカードは 1 秒間表示された後、直ちに検索配列を記載したカードに置き換えられた。被験者には、ターゲットを検出した場合は利き手で、それ以外の場合は非利き手でキーを押すよう指示し、誤答をせずに可能な限り迅速に反応するよう求めた。反応時間は、検索配列の提示開始時に作動し、反応キーが押された時点で停止するデジタルタイマー[Advance Electronics, TC11]を用いて、1 ミリ秒単位で記録された。誤答があった試行は、検査セッションの後半で再試行され、各誤答の後にはダミー試行が行われたが、その結果は記録されなかった。被験者には各試行後に反応時間と正誤が伝えられたが、データから誤答後の遅い反応を除外することを目的としたダミー試行の手順については、伝えられなかった。
<!-- At the beginning of each trial, subjects viewed a plain white card in the tachistoscope, and each of their index fingers rested on a response key. The experimenter gave a verbal "Ready" signal and pressed a button to display a second white card bearing a central fixation spot, which remained in view for 1 sec and was then immediately replaced in the field of view by a card bearing a search array. Subjects were instructed to make a key press with the dominant hand if they detected a target and w ith the nondominant hand otherwise, and to respond as quickly as possible without making any errors. RT was recorded to the nearest millisecond on a digital timer [Advance Electronics, TC11], which was triggered by the onset of the search array and stopped when a response key was pressed. Trials on which an error was made were repeated later in the testing session, and following each error a dummy trial was given, the results of which were not recorded. Subjects were told their RT and whether or not they were correct after each trial; they were not however informed of the dummy trials procedure, the purpose of which was to exclude slow posterror responses from the data. -->

各被験者は、ABBAAB 順に従い、別々のセッションで結合課題と特徴課題の両方についてテストを受けた。被験者の半数は特徴ターゲットから、残りの半数は結合ターゲットから開始した。6 名の被験者は各条件で 128 試行からなる 3 ブロックを実施した後、そのうち 2 名が結合条件でさらに 4 ブロック、別の 2 名がさらに 10 ブロックを自発的に継続し、合計 13 ブロック（計 1,664 試行）となった。これら 2 名の被験者の最初の 3ブロックにおける平均反応時間は、集団平均値に極めて近似していた。
<!-- Each subject was tested both on conjunctions and on features in separate sessions following an ABBAAB order. Half the subjects began with the feature targets and half with the conjunction targets. Six subjects did 3 blocks of 128 trials each in each condition, then two of these subjects volunteered to continue for another 4 blocks in the conjunction condition and two for another 10 blocks, making 1 3 altogether (a total of 1 664 trials). The mean RTs for these two subjects on the first 3 blocks closely approximated the group means. -->

各ブロック内では、正試行と負試行、および異なる表示サイズの提示順序がランダム化されていた。したがって、各ブロックにおいて被験者はターゲットや 2 つの代替ターゲットが何であるかは知っていたが、特定の試行における配列サイズがどうなるかは知らなかった。各ブロックには、各表示サイズにつき 16 の正試行と 16 の負試行が含まれていた。
<!--Within each block the presentation order of positive and negative trials and of different display sizes was randomized; thus in each block the subject knew what the target or the two alternative targets were, but did not know what the array size would be on any given trial. Each block contained 16 positive and 16 negative trials for each display size. -->

* **結果**:<!-- Results-->

図 1 は、各条件における第 2 および第 3 ブロックの 6 名の被験者の平均探索時間を示している。第 1 ブロックは練習として扱われた。表 1 は、これらのデータに対する線形回帰分析の詳細を示している。結果によると、結合条件では探索時間が表示サイズに比例して増加し、その線形成分が表示サイズによる分散の 99% 以上を占めていた。結合条件における正の傾きと負の傾きの比は 0.43 であり、これはほぼ半分に近い値である。これらの結果は、探索が逐次的かつ自己終結的であり、項目あたりの走査速度が約 60 ミリ秒であることを示唆している。分散は、負の試行よりも正の試行においてより急激に増加し、正の試行では、逐次的自己終結的探索で予測される通り、反応時間の二乗平均平方根がディスプレイサイズに比例して増加した。
<!--Figure 1 shows the mean search times for the six subjects over the second and third blocks in each condition; the first block was treated as practice. Table 1 gives the details of linear regression analyses on these data. The results show that search time increased linearly with display size in the conjunction condition, the linear component accounting for more than 99% of the variance due to display size. The ratio of the positive to the negative slopes in the conjunction condition was 0.43 , which is quite close to half. These results suggest that search is serial and self terminating with a scanning rate of about 60 msec per item. The variances increased more steeply for positive than for negative trials, and for positives the root mean square of the RTs increased linearly with display size as predicted for serial self-terminating search.-->

特徴ターゲットを用いた場合、結果は大きく異なった。正試行では、検索時間は妨害刺激の数にほとんど影響を受けず、傾きの平均はわずか 3.1 ミリ秒であった。直線性からの逸脱は有意であり、直線成分はディスプレイサイズによる分散の 68% しか説明しなかった。負試行の場合、直線成分はディスプレイサイズによる分散の 96% を説明し、直線性からの逸脱は有意水準に達しなかった。しかし、その傾きは結合否定刺激の場合の半分以下であった。特徴ターゲットを用いた場合の肯定刺激と否定刺激の傾きの比率はわずか 0.12 であった。いずれの条件においても、被験者全員で同様の結果パターンが示され、個人間の差異は主に傾きの絶対値と切片の値に見られた。
<!--With the feature targets, the results were very different. For the positive displays, search times were hardly affected by the number of distractors, the slopes averaging only 3.1 msec. Deviations from linearity were significant, and the linear component accounted for only 68% of the variance due to display size. For the negatives, the linear component accounted for 96% of the variance due to display size, and departures from linearity did not reach significance. The slope was, however, less than half the slope for conjunction negatives. The ratio of positive to negative slopes with feature targets was only 0. 1 2 . In both conditions, all subjects showed the same pattern of results, with individuals varying mainly in the absolute values of slope s and intercepts. -->

