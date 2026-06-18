# Singular Value Decoposition

## Theory

## Calculations


!!! abstract "如何算奇異值分解？"
    Let $A\in\text{M}_{m\times n}(\mathbb{R})$.

    - Diagnoalize $AA^T$, obtaining eigenvalues $\lambda_1\ge\lambda_2\ge\dots\ge\lambda_m$ and its corresponding eigenvectors $u_i\in\mathbb{R}^m,i=1,2,\dots,m$.

    - Find $\Sigma\in\text{M}_{m\times n}(\mathbb{R})$, where

    \[
    \Sigma_{ij}=\begin{cases}\sqrt{\lambda_i},&\text{if }i=j\\0,&\text{if }i\neq j\end{cases}\quad.
    \]

    - Solve the equation $\det(A^TA-\lambda_iI_n)=0$ to obtain the eigenvectors $v_i\in\mathbb{R}^n,i=1,2,\dots,n$ of $A^TA$ corresponding to $\lambda_i$.

    - We now get two matrices $U$ and $V$

    $$
    U=\begin{pmatrix}\dfrac{1}{\sigma_1}u_1&\cdots&\dfrac{1}{\sigma_m}u_m\end{pmatrix}\in\text{M}_{m\times m}(\mathbb{R}),
    $$

    $$
    V=\begin{pmatrix}\dfrac{1}{\sigma_1}v_1&\cdots&\dfrac{1}{\sigma_m}v_m\end{pmatrix}\in\text{M}_{n\times n}(\mathbb{R}).
    $$

    - The singular value decomposition of $A$ is

    $$
    A=U\Sigma V^T.
    $$
