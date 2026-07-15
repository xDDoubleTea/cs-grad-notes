# Linear Maps

!!! definition "Linear Transformation (Map)"
    
    Let $V,W$ be vector spaces over $F$ and let $T:V\to W$ be a function.

    We say $T$ is a *linear transformation from* $V$ *to* $W$ if for all $v_1,v_2\in V,\alpha\in F$, we have

    $$
    \begin{cases}
    T(v_1+v_2)=T(v_1)+T(v_2)\\
    T(\alpha v_1)=\alpha T(v_1)
    \end{cases}
    $$

    Also call $T$ a linear map, or $T$ is linear.

!!! definition "Range and kernel"
    
    Let $T$ be a linear transformation from $V$ to $W$.
    
    The *range* of $T$, denoted as $\mathsf{R}(T)$, is the set

    $$
    \mathsf{R}(T):=\{T(v)\mid v\in V\}.
    $$


    The *kernel* of $T$, denoted as $\mathrm{ker}(T)$, is the set

    $$
    \mathrm{ker}(T):=\{v\in V\mid T(v)=0_W\}.
    $$

???+ theorem "One step verification"
    
    Let $V,W$ be vector spaces over $F$ and let $T:V\to W$ be a function.

    $T$ is linear if and only if for all $v_1,v_2\in V,\alpha\in F$, we have $T(v_1+\alpha v_2)=T(v_1)+\alpha T(v_2)$.


???+ theorem "Properties of linear transformation"
    
    Let $T$ be a linear transformation from vector spaces $V$ to $W$.

    1. $T(0_V)=0_W$
    2. If $S$ is a linearly independent set in $V$ and $|S|\le\dim(W)$, then $T(S)$ is a linearly independent set in $W$.
    3. If $S$ is a linearly independent set in $V$ and $|S|>\dim(W)$, then $T(S)$ is a linearly dependent set in $W$.
    4. If $S\subset V$ is a set and $T(S)$ is linearly independent, then $S$ is a linearly independent set in $V$.
    5. If $\beta$ is a basis for $V$ and $\dim(W)=\dim(V)$, then $T(\beta)$ is a basis for $W$.
    6. $\mathsf{R}(T)$ and $\mathrm{ker}(T)$ are subspaces of $W$ and $V$, respectively.
    

!!! example 
    
    Let $V=\mathsf{C}([a,b],\mathbb{R})$ and $F=\mathbb{R}$ where $a,b\in\mathbb{R}$. Let $T:V\to\mathbb{R}$ be defined by

    $$
    T(f):=\int_{a}^{b}f(x)dx.
    $$

    Then $T$ is linear.


