# Inner products

!!! definition "Inner product"
    Let $V$ be a vector space over $F$, where $F$ is either $\mathbb{R}$ or $\mathbb{C}$. An *inner product* on $V$ is a map $\langle\cdot,\cdot\rangle:V\times V\to V$ that satisfies

    $$
    \forall y\in V,\langle\cdot,y\rangle\in V^*,
    $$
    
    $$
    \langle x,y\rangle=\overline{\langle y,x\rangle},
    $$

    $$
    \langle x,x\rangle\ge0,\langle x,x\rangle=0\iff x=0.
    $$

    $V$ together with an inner product is called an inner product space.

!!! example
    Let $V=\mathsf{C}\left(\left[0,1\right],\mathbb{C}\right)$ be the vector space of all continuous functions defined on $[0,1]$ with codomain $\mathbb{C}$. Let

    $$
    \langle f(x),g(x)\rangle:=\int_{0}^{1}f(x)\overline{ g(x) }dx,
    $$

    then it is an inner product on $V$.

## Norm

!!! definition "Norm"
    Let $V$ be a vector space over $F$, where $F$ is either $\mathbb{R}$ or $\mathbb{C}$. A *norm* on $V$ is a map $\|\cdot\|:V\to\mathbb{R}_{\ge0}$ that satisfies

    $$
    \forall x\in V,\|x\|\ge0,\text{ and }\|x\|=0\iff x=0,
    $$

    $$
    \forall x,y\in V,\|x\|+\|y\|\ge\|x+y\|,
    $$
    
    $$
    \forall\alpha\in F, x\in V, \|\alpha x\|=|\alpha|\|x\|,
    $$

    where $|\alpha|$ is the absolute value on $F$.

    $V$ together with a norm is called a normed vector space.

## Metric

!!! definition "Metric"
    Let $V$ be a vector space over $F$, where $F$ is either $\mathbb{R}$ or $\mathbb{C}$. A *metric* on $V$ is a map $d:V\times V\to\mathbb{R}$ that satisfies

    $$
    \forall x\in V d(x,y)\ge0,\,\text{and }d(x,y)=0\iff x=y
    $$
    
    $$
    \forall x,y\in V,d(x,y)=d(y,x),
    $$

    $$
    \forall x,y\in V,d(x,z)+d(z,y)\ge d(x,y).
    $$


??? theorem "Inner product induces norm"
    
    Let $V$ be an inner product space over $F$. Then the map $\|\cdot\|:V\to\mathbb{R}$ defined as
    
    $$
    \|x\|:=\sqrt{\langle x,x\rangle}
    $$
    
    is a norm on $V$.

??? theorem "Norm induces metric"
    
    Let $V$ be a normed vector space over $F$. Then the map $d:V\times V\to\mathbb{R}$ defined as


    $$
    d(x,y):=\|x-y\|
    $$

    is a metric on $V$.


??? note

    The converse fails for both of the theorems above.

    For example, let $V=\mathbb{R}^2$, $F=\mathbb{R}$ and define $\|(a,b)\|:=|a|+|b|$. Assume that there is an inner product such that

    $$
    \left\langle (a,b),(a,b)\right\rangle=\left(|a|+|b|\right)^2
    $$

    Then

    $$
    \begin{align*}
    4=\left\langle(1,-1),(1,-1)\right\rangle&=\left\langle(1,0),(1,1)\right\rangle+\langle(0,-1),(1,1)\rangle\\
                                        &=\langle(1,0),(1,0)\rangle+\langle(1,0),(0,1)\rangle+\langle(0,-1),(1,0)\rangle+\langle(0,-1),(0,1)\rangle\\
                                        &=1+\langle(1,0),(0,1)\rangle-\langle(0,1),(1,0)\rangle-1\\
                                        &=1+\langle(1,0),(0,1)\rangle-\langle(1,0),(0,1)\rangle-1\\
                                        &=0\rightarrow\leftarrow
    \end{align*}
    $$

    The discrete metric does not induce a norm on $\mathbb{R}^2$. Since if $x\neq0$, then $d(x,0)=\|x\|=1$, and this causes $1=d(2x,0)=\|2x\|=2\|x\|=2$.

## Cauchy-Schwarz inequality


???+ theorem "Cauchy-Schwarz inequality"
    Let $V$ be an inner product space.

    The inequality

    $$
    \|x\|\|y\|\ge|\langle x,y\rangle|
    $$

    holds for all $x,y\in V$

## Remarks

???+ theorem "The other side of the triangle inequality"

    Let $V$ be a normed vector space, then

    $$
    \|x-y\|\ge\left|\|x\|-\|y\|\right|
    $$

    holds for all $x,y\in V$.

???+ theorem "The parallelogram law"

    Let $V$ be an inner product space. Then the norm induced by the inner product satisfies

    $$
    2(\|x\|^2+\|y\|^2)=\|x+y\|^2+\|x-y\|^2
    $$
    
    holds for all $x,y\in V$.
    
???+ theorem "Norm with parallelogram law induces inner product"
     
    Let $V$ be a normed vector space. The norm satisfies the parallelogram law if and only if the norm is induced by some inner product on $V$.
