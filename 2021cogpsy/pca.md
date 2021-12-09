---
title: pca
author: 浅川伸一
---


自己組織化は、多次元刺激として与えられる情報を、その刺激が持つ規則性に従って 2 次元の皮質上へ照射する対応問題と見なすことができる。
すなわち入力層の空間多次元多様体から 2 次元部分空間への写像である。
このような立場から、統計学の用語を用いて説明を試みる。

通常の意味での主成分分析では列方向に変数 ($p$)、行方向にデータ数 ($n$)、となる行列を仮定する ($\mathbf{X}=\Brc{x_{ij}}$, $\Brc{1\le i\le n, 1\le j\le p}$) ことが多いが、ここではニューラルネットワークとの関連を考え通常の意味でのデータ行列の転置を入力データ行列 $\mathbf{X}$ 
とする($\mathbf{X}=\Brc{x_{ij}}$,$\Brc{1\le i\le p, 1\le j\le n}$)。
主成分分析とは
<!-- % $\mathbf{X}$ 分散共分散行列を最大化するベクトルを
%見出すことである。
%\begin{equation}
%\mathbf{X}'\mathbf{X}\mathbf{g}_j = \lambda_j\mathbf{g}_j,\qquad\Brc{j=1,2,\ldots,p}
%\end{equation}
%および
%\begin{equation}
%\mathbf{X}\mathbf{X}'\mathbf{f}_j = \tilde\lambda_j\mathbf{f}_j\qquad\Brc{j=1,2,\ldots,n}
%\end{equation}
%ここに$\lambda_j=\tilde\lambda_j (j=1,2,\ldots,n)$ である。
%
%このとき -->
適当な線形結合
\begin{eqnarray}
\mathbf{y}_1 &=& w_{11} \mathbf{x}_1 + w_{12} \mathbf{x}_2 + \cdots + w_{1p} \mathbf{x}_p\\
         &=& \mathbf{X} \mathbf{w}_1,
\end{eqnarray}
によって合成変量 $\mathbf{y}$ を最大化するベクトル $\mathbf{w}$ を見つけることであ
る。このことは線形数学では固有値問題を解くことと同義である。
合成変量 $\mathbf{y}$ の分散を最大化するには、
データ行列$\mathbf{X}$ の分散共分散行列の最大固有値に対応する固有ベクトル
を求めればよい。
%$\mathbf{x}$ は素データからその変数の平均をひいた平均偏差ベクトルであるとすれば、
%素データベクトルを $\mathbf{x}^{(r)}$ として
%\begin{equation}
%\mathbf{x}=\BRc{\mathbf{I}-\mathbf{1}_n\Brc{\mathbf{1}'_n\mathbf{1}_n}^{-1}\mathbf{1}'_n}\mathbf{x}^{(r)}
%\end{equation}
%と表わされる。

\subsection{パーセプトロンモデル}
上記の主成分分析を神経回路網の立場で表現する。

$\mathbf{X}$ は入力データセットで、$p$ 個のユニットからなる入力層に与えられる 
$n$ 個のサンプルデータであると考える。これらのユニットから $m$ 個の出力層
ユニットに全結合しているモデルを考える。

簡単のため出力層のニューロンが $1$ 個しかない場合 ($m=1$)
を考えると、
$k$ 番目の入力パターンに対する出力層ユニットの出力は以下の式、
\begin{equation}
y_k = \sum_i^p w_{i}x_{ki} = \IP{\mathbf{w}}{\mathbf{x}_k}.
\end{equation}
に従う、すなわち線形出力ユニットを考える。
ここで、$w_{i}$ は
パターン $k$ が与えられたときの
 $i$ 番目の入力層ユニット
$x_{ki}\,(1\le i\le p, 1\le k\le n)$ 
と出力層のユニットとの結合係数である。
%
%仮に
パターン $k$ が与えられたときの $i$ 番目の入力層ユニットから出力層ユニット
への結合強度 $w_i$ が式(\ref{pca_hebbian})のようなヘッブ則
\begin{equation}
\Delta w_i = \eta\, y_k\,x_{ki}\label{pca_hebbian},
\end{equation}
を用いて更新されたとすると、$w_i$ の漸化式は以下のようになる
\begin{equation}
\Delta w_i(t+1) 
= w_i(t) + \Delta w_i
= w_i(t) + \eta\,y_k\,x_i
= w_i(t) + \eta\,\sum_i^p w_{i}x_{ki},\,\,\mbox{(for all $k$)}.
\end{equation}
$w_i$ をまとめて $\mathbf{w}$ とベクトル表現すれば
\begin{equation}
\Delta \mathbf{w}(t+1) 
= \mathbf{w}(t) + \Delta\mathbf{w}
= \mathbf{w}(t) + \eta\,\IP{\mathbf{x}_k}{\mathbf{w}}\mathbf{x}_k,%\;\;\mbox{(for all $k$)}.
\end{equation}
である。

学習が成立(収束)した時点での $\Delta\mathbf{w}$ は $\mathbf{0}$ になる
(すなわち結合係数の更新が行なわれない)ことが期待されるので、
全入力パターンの平均を考えて
\begin{equation}
\mathbf{0} 
= \frac{1}{n}\sum_{k=1}^n \Delta\mathbf{w}^{(k)}
%= \eta\,\frac{1}{n}\,\sum_{k=1}^n y^{(k)} x^{(k)}
= \eta\,\frac{1}{n}\,\sum_{k=1}^n \IP{\mathbf{w}}{\mathbf{x}^{(k)}} \mathbf{x}^{(k)}
= \eta\,\frac{1}{n}\,\mathbf{X}'\mathbf{X}\mathbf{w}\label{eq:myeq1}
\end{equation}
%
%\begin{equation}
%0 = \frac{1}{n}\sum_{k=1}^n \Delta w_{i}
%= \eta \frac{1}{n}\sum_{k=1}^n y_k x_k
%= \eta \frac{1}{n}\sum_{k=1}^n \Brc{\sum_i^p x_{ki}w_{i}}x_{ki}
%= \eta \Brc{\frac{1}{n} \mathbf{X}'\mathbf{X}}\mathbf{w}
%\end{equation}
%
が成り立っていなければならない。
%
ところが $\mathbf{X}'\mathbf{X}$ は、実対称行列であり、
固有値はすべて正で固有ベクトルは直交する。
すなわちヘッブの学習則では有限回の学習によって
解が求められない(実際には最大固有値に対応する固有ベクトルの方向に際限無く大きくなっていく)\footnote{$\mathbf{0}$ 以外に解がない}。
%$\mathbf{X}^{(r)}\rightarrow\mathbf{X}$ を求める際の中心化によって
%rank($\mathbf{X}$)$=m-1$ だから、少なくとも 1 つ 0 固有値が存在する。
%すななち、
%$\mathbf{X}'\mathbf{X}$ が(統計学の意味で)分散共分散行列になっていればヘッブ則
%によって $w$ は最大固有値に対応する固有ベクトルの方向を向くことが期待さ
%れる。

そこで、式(\ref{pca_hebbian}) を修正して
\begin{equation}
\Delta w_i = \eta\, y_k\Brc{1-y_k}\,x_{ki}
\end{equation}
のように変形すると結合強度ベクトルは最大固有値の方向を向き、かつ収束することが
Oja\citeyear{Oja1988}によって証明されている。
すなわち、
ヘッブ則を使った自己組織化アルゴリズムを用いて
入力データの統計的な性質をネットワークに学習させることができる。


$\mathbf{X}$ が 2 重中心化されていれば、rank$\Brc{\mathbf{X}}=p-1$ が保証されるこ
とになる。
\begin{equation}
\mathbf{X}'\mathbf{X} 
= \Brc{\mathbf{P}_M^\bot \mathbf{X}\mathbf{P}_M^\bot}'
  \Brc{\mathbf{P}_M^\bot \mathbf{X}\mathbf{P}_M^\bot}
= L\Brc{\mathbf{X}'\mathbf{X}} - L^\bot\Brc{\mathbf{X}'\mathbf{X}} 
\end{equation}
ここで、すべての要素が $1$ であるベクトルへの射影演算を $L(\cdot)$ と表わ
した。直交射影行列の固有値は常に $1$ であることを考慮すると、式
(\ref{eq:myeq1}) の固有値問題は
\begin{equation}
 \mathbf{w} 
= \mathbf{X}'\mathbf{X}\mathbf{w}\label{eq:myeq2}
\end{equation}
となって固有値 $1$ に対応する固有ベクトルを求める問題と同一になる。
%
%さらに、$\mathbf{X}$ が Young--Householder 変換によって 2 重中心化されていれ
%ば、Hebb 則によって得られる解と古典的多次元尺度構成法の解が一致すること
%になります。

\subsubsection{$|\mathbf{w}|=1$ になることの証明}
出力 $x$ の分散を考えれば
\begin{equation}
\frac{1}{n}\sum^n_{k=1}y^2_k = \mathbf{w}'\mathbf{X}'\mathbf{X}\mathbf{w}
\end{equation} 
である。ここで$\IP{\mathbf{w}}{\mathbf{w}}=1$ の条件のもとで $x$ の分散を最大化す
ることを考える。$\mathbf{w}$ は Lagrange の未定乗数 $\lambda$ を用いて
\begin{equation}
E= \mathbf{w}'\mathbf{X}'\mathbf{X}\mathbf{w} - \lambda\Brc{\mathbf{w}'\mathbf{w}-1}
\end{equation} 
を $\mathbf{w}$ で偏微分して $0$ とおいた式
\begin{equation}
\frac{E}{\partial \mathbf{w}} = 2 \mathbf{X}\mathbf{w} - 2\lambda\mathbf{w} = 0
\end{equation} 
を解いて
\begin{equation}
\mathbf{X}\mathbf{w} = \lambda\mathbf{w}\label{eq:myeq3}
\end{equation} 
が平衡状態で成り立つことになる。式(\ref{eq:myeq3}) は式(\ref{eq:myeq2}) と
同じ形をしている。ここで
\begin{equation}
\lambda = \mathbf{w}'\mathbf{X}\mathbf{w} = \mathbf{w}'\lambda\mathbf{w} = \lambda|\mathbf{w}|^2
\end{equation} 
となるので、$|\mathbf{w}|=1$ が証明された。

%
%\subsection{$\mathbf{w}$ が最大固有値に対応する固有ベクトルの方向に収束することの証明}
%

\subsubsection{出力層が複数ある場合}
出力ニューロンが $j$ 個 $(1\le j\le m)$ の場合は、
\begin{equation}
\Delta \mathbf{w}_{ij} = \eta \mathbf{y}_j\BRc{\Brc{x_j-\sum x_kw_k}}\mathbf{x}_i
\end{equation}
を用いて更新すればよいことが\cite{Sanger1989}によって示された。
Sanger の考え方は、Gram--Schimidt の直交化をそのまま
ニューラルネット上で実現したものととらえることができる。


%\bibliographystyle{mslapa}
%\bibliography{/Users/asakawa/study/bib/asakawa,/Users/asakawa/study/Alexia2000/alexia}


%\end{document}
