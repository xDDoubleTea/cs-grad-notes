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


???+ example "Examples of vector spaces"

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
???+ example "Functions"
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
