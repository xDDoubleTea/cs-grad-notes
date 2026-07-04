# Vector spaces

## Field
!!! definition "Field"
    A **Field** $F$ is a commutative division ring with $0\neq 1$. that is, it is a commutative ring and every elements except $0$ in $F$ has a multiplicative inverse in $F$.

!!! problem "What is a field?"
    1. Is $\mathbb{Z}$, the set of all integers, a field?
    2. Is $\mathbb{Z}/2\mathbb{Z}$ a field? Find a sufficient condition for $\mathbb{Z}/m\mathbb{Z}$ to be a field, where $m\in\mathbb{N},m\ge2$.

??? exercise "Ans"
    1. No. $2$ has no multiplicative inverse in $\mathbb{Z}$.
    2. Yes. If $m$ is a prime, then it is a field by the Lagrange theorem of subgroups.

!!! definition "Characteristic of a ring"

    Let $R$ be a ring. The *characteristic* of $R$, denoted by $\text{char}(R)$, is the number

    $$
    \text{char}(R)=\min\left\{n\in\mathbb{Z}_{\ge0}\,\middle|\,\underbrace{1+1+\dots+1}_{n}=0\right\}.
    $$


## Vector space

!!! definition "Vector space"
    Let $(V,+)$ be an abelian group and $F$ be a field.

    A vector space is $(V,+,\cdot)$ where $\cdot:F\times V\to V$ is a group action that satisfies

    $$
    \begin{cases}
    c_1(v_1+v_2)&=c_1v_1+c_1v_2\\
    (c_1+c_2)v_1&=c_1v_1+c_2v_1
    \end{cases}
    $$

    for all $c_1,c_2\in F,v_1,v_2\in V$.

??? definition "Module (generalized vector spaces)"

    Reqires same conditions except that $F$ can be a ring.


## Examples
???+ example 

    Assume that the following uses component wise addition and component wise scalar multiplication.

    - $F^n$ is a vector space over $F$ where $F$ is a field.
    - $\mathbb{R}^n$ is a vector space over $\mathbb{Q}$, and it is infinite dimensional.
    - $\mathbb{C}^n$ is a vector space over $\mathbb{R}$ and its dimension is $2n$.
    - $\mathbb{Q}$ is not a vector space over $\mathbb{R}$.

??? example "Polynomials"

    Let $F$ be a field. The *polynomials in* $x$ with coefficients in $F$ is the set

    $$
    F[x]:=\left\{a_nx^n+a_{n-1}x^{n-1}+\dots+a_1x+a_0\,\middle|\,a_i\in F,n\in\mathbb{Z}_{\ge0}\right\}.
    $$

    The *degree* of a polynomial $f(x)\in F[x]$, denoted by $\deg(f)$, is the largest integer $n$ such that $a_n\neq0$.

    Define addition between $\displaystyle f(x)=\sum_{i=0}^n a_ix^i,g(x)=\sum_{i=0}^m b_ix^i\in F[x]$, where $n=\deg(f)\ge m=\deg(g)$, as

    $$
    f(x)+g(x)=a_nx^n+a_{n-1}x^{n-1}+\dots+(a_m+b_m)x^m+(a_{m-1}+b_{m-1})x^{m-1}+\dots+(a_0+b_0).
    $$

    Define scalar multiplication between $c\in F,f(x)\in F[x]$ by

    $$
    c\cdot f(x)=\sum_{i=0}^{n}(ca_n)x^n.
    $$

    Then $F[x]$ is a vector space over $F$. In linear algebra for undergraduates, the textbooks often write this as $\mathsf{P}(F)$.

    Additionally, given $k\in\mathbb{Z}_{\ge0}$, $\mathsf{P}_k(F)$ is the set that contains all polynomials with degree less or equal to $k$, and inherits the addition and scalar multiplication from $\mathsf{P}(F)$, which becomes a vector space over $F$, and is a subspace of $\mathsf{P}(F)$.

??? example "Sequences"

    Let $F$ be a field. Let $V:=\{\{a_n\}_{n=1}^{\infty}:a_n\in F\}$, the set of all sequences in $F$.

    Define addition $\{a_n\}_{n=1}^{\infty}+\{b_n\}_{n=1}^{\infty}:=\{a_n+b_n\}_{n=1}^{\infty}$.

    Define scalar multiplication $c\{a_n\}_{n=1}^{\infty}:=\{ca_n\}_{n=1}^{\infty}$.

    Then $V$ is a vector space over $F$.

    ??? example "Usage"

        Let $\{f_n\}_{n=0}^{\infty}$ be the fibonacci sequence, i.e., $f_0=0,f_1=1$ and $f_{n}=f_{n-1}+f_{n-2}$ for $n\ge 2$.

        Let $W\subset V$ be defined by
        
        $$
        W:=\{\{w_n\}\,\mid\,w_n=w_{n-1}+w_{n-2},w_0,w_1\in\mathbb{R}\}
        $$

        Then it is a subspace of $V$. $\dim(W)=2$ because it is isomorphic to $\mathbb{R}^2$ by sending $w_0$ to $a_1$, $w_1$ to $a_2$ for all $\{w_n\}\in W,(a_1,a_2)\in\mathbb{R}^2$, for example.
        
        Therefore, the linearly independent set $\left\{\{\varphi^n\}_{n=0}^{\infty},\left\{\left(\dfrac{1}{\varphi}\right)^n\right\}_{n=0}^{\infty}\right\}\subset W$ spans $W$, where $\varphi=\frac{1+\sqrt{5}}{2}$. 
    
        Hence, we can find unique $\alpha,\beta\in\mathbb{R}$, such that

        $$
        \alpha\varphi^n+\beta\frac{1}{\varphi^n}=f_n
        $$
        
        for all $n\in\mathbb{N}$. Specifically, we can solve the equations

        $$
        \begin{cases}
        \alpha+\beta&=f_0\\
        \alpha\varphi+\frac{\beta}{\varphi}&=f_1
        \end{cases}
        $$

        and we obtain the Binet's formula:

        $$
        f_n=\frac{1}{\sqrt{5}}\left(\varphi^{n}-\frac{1}{\varphi^n}\right).
        $$

    !!! note
        The sequence space is useful for solving *homogeneous recurrence sequences*, in fact, the closed form formula of recurrence relations is related to the Jordan normal form of $A$ when solving for

        $$
        \begin{pmatrix}a_{n+k}\\a_{n+k-1}\\\vdots\\a_{n}\end{pmatrix}=A^n\begin{pmatrix}a_{k}\\a_{k-1}\\\vdots\\a_{1}\end{pmatrix}.
        $$
        
        This is why they are in a linear combination of geometric series, and the ratio may be complex numbers (irrational numbers) even if the original sequence is real (positive integers).
        
        

??? example "Functions"
    Let $S$ be a nonempty set and $F$ be a field. Let

    $$
    \mathcal{F}(S,F^n):=\left\{f\mid f:S\to F\text{ is a function}\right\}
    $$

    Define addition between $f,g\in\mathcal{F}(S,F)$ by $(f+g)(x)=f(x)+g(x),\forall x\in S$.

    Define scalar multiplication for $c\in F, f\in\mathcal{F}(S,F)$ by $(c\cdot f)(x)=cf(x),\forall x\in S$.

    Then $\mathcal{F}(S,F)$ is a vector space over $F$.

    > Note that the codomain of the function space must be a set with addition and scalar multiplication defined.


??? example "Continuous functions"

    Let $A\subset F^m$ and let $\mathsf{C}(A,F^n)$ be the subset of $\mathcal{F}(A,F^n)$ that contains all continuous functions from $A$ to $F^n$.

    Then it is a vector space over $F$.


??? example "Differentiable functions"
??? example "Analytic functions"
??? example "Riemann Integrable functions"
