---
title: "第04回 2024年度開講 駒澤大学 認知心理学研究"
author: "浅川 伸一"
layout: home
---
<link href="/assets/css/asamarkdown.css" rel="stylesheet">

<div align="right">
<a href='mailto:educ0233@komazawa-u.ac.jp'>Shin Aasakawa</a>, all rights reserved.<br>
Date: 11/Oct/2024<br/>
Appache 2.0 license<br/>
</div>

$$
\newcommand{\of}[1]{\left(#1\right)}
\newcommand{\Of}[1]{\left[#1\right]}
\newcommand{\KL}[2]{\operatorname{KL}\left(\left.{#1}\right\|{#2}\right)}
\newcommand{\given}[1]{\left|{#1}\right.}
$$


<div class="memo">
クリストフ・コロンブスのアメリカ発見について，そもそも彼の偉大な点はどこにあるか，ということをきく人があるならば，それは西回りのルートでインドへ旅行するのに，地球が球形であることを利用するというアイディアではなかった，と答えなければならないだろう。
このアイディアはすでに他の人々によって考えられたものであったし，彼の探検の慎重な準備，船の専門的な装備などということでもなかった。
それらのことは，他の人でもやろうとすればやれたに違いない。
そうではなくて，この発見的航海で最も困難であったことは，既知の陸地を完全に離れ，残余の貯えでは引き返すことがもはや不可能であった地点から，さらに西へ西へと船を走らせるという決心であったに違いない。<br>
<div style="text-align:right">「部分と全体」ハイゼンベルク，山崎和夫訳，みすず書房，p.115，「VI 新世界への出発 1926-1927年」冒頭部</div>
</div>


<div class="figcenter">
<img src="/assets/2019Glaser_fig2.jpg" width="39%">
<img src="/2024assets/2008Kriegeskorte_fig3.jpg" width="39%">
<div class="memo">

左: Glaser+(2019) Fig.2, 右: Kriegeskorte+(2008) Fig.3

機械学習の 4 つ役割
1. 工学問題の解として
2. 予測変数の特定と改善
3. 単純モデルの評価とベンチマーク
4. 脳のモデルとして<br/>


図 3. 異なる表現を関連付けるハブとしての表現非類似性行列<!-- FIGURE 3. The representational dissimilarity matrix as a hub that relates different representations. --><br/>

A: システム神経科学は，3つの主要な研究分野，行動実験，脳活動実験，計算モデリングを関連付けるのに苦労してきた。
これまでは，これらの分野は主に 2 つのレベルで相互に作用してきた。
(1) 言語理論のレベルでの相互作用。すなわち，個別の分析から導き出された結論を比較することによる相互作用。
このレベルは不可欠であるが，定量的ではない。
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
</div></div>

## 本日のメニュー

1. Git のインストール
2. 機械学習モデルの説明，ロジスティック回帰，k-means, SVM, 判別分析
3. [Python の基礎](python_numpy_intro_ja)
4. [フレームワーク](/eco/)
5. CNN


# 1. Git のインストールと実行

## 1.1 コマンドライン版 `git` のインストール

[Git の公式ページ](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git){:target="_blank"} によれば，Windows へのインストールには複数の方法がある。

* [Git for Windows プロジェクト版 https://git-scm.com/download/win]
* [Chocolatoey package 版](https://community.chocolatey.org/kackages/git)

Chocolatory は総合パッケージ管理と呼ばれる複数のソフトウェアを矛盾なく管理するためのツールである。
個々のソフトウェアを個別にインストールすると，バージョン管理が煩雑であるため，chocolatory 管理を任せるという選択肢は一考に値する。

Chocolaty がインストールしてあれば，以下のコマンドを実行すれば git がインストールされる。
Chocolaty のインストールには，次節を参照のこと

```bash
choco install git.install --params "'/GitAndUnixtoolsOnPath /WindowsTerminal /NoAutoCrlf'"
```

## 1.2 Chocolaty のインストール

1. 管理者権限で `powershell.exe` を実行する
2. `powershell.exe` 上に下記コマンドをコピーする:
```bash
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
3. エンターキーを押下して上記コマンドを実行する。
もし `Get-ExcutionPolicy` を実行して，`Restricted` が帰ってきたら，`Set-ExecutionPolicy Allsigned` もしくは `Set-ExecutionPolicy Bypass -Scope Process` を実行する必要がある。
4. インストールが終了するまでしばらく待つ。
5. エラーメッセージが表示されなければ，`choco -?` を実行して確認作業を行う。


<!-- 4. First, ensure that you are using an administrative shell - you can also install as a non-admin, check out Non-Administrative Installation.
5. Install with powershell.exe
```bash
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
1. Paste the copied text into your shell and press Enter.
2. Wait a few seconds for the command to complete.
3. If you don't see any errors, you are ready to use Chocolatey! Type choco or choco -? now, or see Getting Started for usage instructions. -->

## 1.3 Git コマンドの実際

Windows Powershell のコマンドラインで必要なコマンドは，`git clone`, `git status`, `git pull` くらいでろう。
他のコマンドは，必要に応じて習得すれば良い。

Github 上のリポジトリ `CSAILVision` を自身の Windows PC のカレントディレクトリへ保存する場合， `git clone` コマンドを用いて，以下のように操作する:
```bash
git clone https://github.com/CSAILVision/places365.git
```

上例の場合，カレントディレクトリに `places365` というディレクトリが作成される。
`git clone 第一引数 第二引数` のように指定すると，`places366` ではなく，第二引数で指定されたディレクトリ名で，リポジトリが作成される。
`2024palces365.git` というディレクトリ名にしたければ，以下のようにする:<br/>
`git clone https://github.com/CSAILVision/places365.git 2024places365.git`

上記のコマンドで，`2024places365.git` ディレクトリ内に全リポジトリが格納されている。
Git 上でコードやデータが変更されていれば，最新の状態へ変更する必要が生じる。
この状態をチェックするコマンドが `git status` であり，最新の状態へ混交するコマンドが `git pull` である。
`git status` と `git pull` コマンドは，カレントディレクトリを該当ディレクトリ内へ変更してから実行する必要がある。
なぜなら，各リポジトリが格納されているディレクトリ内に，更新情報が格納されているからである。
`git pull` コマンドは，カレントディレクトリ内にある (具体的には隠しディレクトリ `.git` 以下) 更新場をサーバ側の更新情報と比較して，最新のデータを取得するからである。

## ロジスティック回帰，k-means, SVM (サポートベクターマシン)，および線形判別分析の相互関係

先週の竹市先生の授業回で説明のあった 3 手法に線形判別分析を加えて 4 手法の相互関係について補足していく。

復習: 機械学習の教師あり学習は，分類問題と回帰問題とに大別される。
これらは，教師信号が離散量か連続量かの違いである。
唯一紛らわしい用語にロジスティック回帰 (Logistic regressions) がある。
ロジスティック回帰は回帰ではなく，分類問題に用いられる。
すなわち線形問題の典型である単回帰 simple regressions: $y=f(x)=ax+b$ に対して，出力を $[0,1]$ の範囲に限定すれば，出力確率とみなしうる。
このため，単回帰式に対して $\displaystyle[1-e^{-y}]^{-1}=[1-e^{-(ax+b)}]^{-1}=\frac{1}{1+e^{-(ax+b)}}$ なる変換を考える。
この変換のことをロジスティック変換と呼び，この手法の名前の由来となっている。

ロジスティック変換は，ロジスティックシグモイド変換，あるいは単に，シグモイド関数と呼ばれることもある。
ロジスティック回帰の起源は，一説によれば人口動態を記述した Mathus(1789) であるとされる([Cramer2002](https://papers.tinbergen.nl/02119.pdf))。

任意のデータ $x\in[1,D]$ に対して，真偽，賛否，あるいは，あるクラスに属するか否かを定めるためのデータ，もしくは特徴を $x$ とする。
$x$ の範囲は $x\in(-\infty,+\infty)$ であるので，$P(x) + P(\neg x) = 1$ を満たすためには，$f(x)>0$ かつ $x>y\rightarrow f(x)>(y)$ を満たす変換を考えれば良い。





## [世界モデル](https://worldmodels.github.io/){:target="_blank"}

先週取り上げた変分符号化器モデルの応用として，[世界モデル](https://arxiv.org/abs/1803.10122) を取り上げます。

<div style="text-align: center;">
<img src="/2023assets/2018Ha_Schmithuber_world_model_schematic.svg" style="width:49%">
<div class="figcaption">

エージェントモデルのフロー図。
未加工の観測データは，まず各時間ステップ t で視覚 V によって処理され，潜在変数 z_t が生成される。
コントローラ C への入力はこの潜在ベクトル z_t と各時間ステップでのメモリ M の隠れ状態 h_t が結合されたものである。
コントローラ C は次に，運動制御のための行動ベクトル a_t を出力する。
メモリ M は現在の潜在変数 z_t と行動 a_t を入力として，自身の隠れ状態を更新し，時間 t+1 で使用するh_{t+1} を生成する。
</div></div>


世界モデルの考え方は，比較的単純であり，1) 外界とのインターフェイス，2) 内部モデル，3) コントローラ，から成り立っている。

<div style="text-align: center;">
<img src="/2023assets/world_models_1990.jpeg" style="width:44%;"/>
<img src="/2023assets/world_models_1990_feedback.jpeg" style="width:44%;"/>
<!-- <img src="/2023assets/world_models_1990.jpeg" style="display: block; margin: auto; width: 44%;"/>
<img src="/2023assets/world_models_1990_feedback.jpeg" style="display: block; margin: auto; width: 44%;"/> -->
</div>
<div style="text-align: center;">
世界 RNN モデルを内蔵したコントローラ。

環境と相互作用する RNN ベースのコントローラの図 (Schmithuber1990)
<!-- A controller with internal RNN model of the world.
Ancient drawing (1990) of a RNN-based controller interacting with an environment. [20] -->
</div>

## マルチモーダルインテグレーション，マルチタスク，トップダウン流とボトムアップ流

* [系列探索と逆行流: 視覚野における双方向情報フローの計算モデル](/2023cogpsy/2021Ullman_bu_td_ja.pdf)
* [ボトムアップ・トップダウンの反復処理による画像解釈](/2023cogpsy/1995Ullman_bidirectional_cortex_ja.pdf)
