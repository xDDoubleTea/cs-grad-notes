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

# Norm

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

# Metric

!!! definition "Metric"
    Let $V$ be a vector space over $F$, where $F$ is either $\mathbb{R}$ or $\mathbb{C}$. A *metric on $V$ is a map $d:V\times V\to\mathbb{R}$ that satisfies

    $$
    \forall x\in V d(x,y)\ge0,\,\text{and }d(x,y)=0\iff x=y
    $$
    
    $$
    \forall x,y\in V,d(x,y)=d(y,x),
    $$

    $$
    \forall x,y\in V,d(x,z)+d(z,y)\ge d(x,y).
    $$


???+ theorem
    
    Let $V$ be an inner product space over $F$. Then the map $\|\cdot\|:V\to\mathbb{R}$ defined as
    
    $$
    \|x\|:=\langle x,x\rangle
    $$
    
    is a norm on $V$.

???+ theorem
