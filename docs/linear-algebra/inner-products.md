# Inner products

!!! definition "Inner product"
    Let $V$ be a vector space over $F$. An inner product on $V$ is a map $\langle\cdot,\cdot\rangle:V\times V\to V$ that satisfies

    $$
    \forall y\in V,\langle\cdot,y\rangle\in V^*,
    $$
    
    $$
    \langle x,y\rangle=\overline{\langle y,x\rangle},
    $$

    $$
    \langle x,x\rangle\ge0,\langle x,x\rangle=0\iff x=0.
    $$

!!! example
    Let $V=\mathscr{C}\left(\left[0,1\right],\mathbb{C}\right)$ be the vector space of all continuous functions defined on $[0,1]$ with codomain $\mathbb{C}$. Let

    $$
    \langle f(x),g(x)\rangle:=\int_{0}^{1}f(x)\overline{ g(x) }dx,
    $$

    then it is an inner product on $V$.
