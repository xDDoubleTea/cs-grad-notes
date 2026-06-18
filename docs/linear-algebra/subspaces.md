# Subspaces

!!! definition "Subspace"
    Let $V$ be a vector space over $F$. We say $W\subset V$ is a subspace of $V$ if

    1. It inherits the vector addition and the scalar multiplication structures of $V$.
    2. It is closed under both vector addition and scalar multiplication.
    3. $0\in W$.

???+ quote
    向量空間的子空間就是一個子集合且還是向量空間

!!! problem "是非題"

    1. 所有有限維度向量空間$V$只要不是零空間，則為無窮集合。
    2. 子空間的定義中，$0\in W$是多餘的。
    
??? exercise "答案"

    1. 否。考慮$F=\mathbb{Z}/2\mathbb{Z}$，並且將$F$當作$F$上的向量空間，則其是有限集合。
    2. 否。空集合滿足前兩條，但空集合不是向量空間，因為沒有$0$向量。

???+ theorem "子空間一步檢定"
    Let $V$ be a vector space over $F$. Then $W$ is a subspace of $V$ if and only if $w_1+cw_2\in W$ for every $w_1,w_2\in W, c\in F$, and $0\in W$.
    
