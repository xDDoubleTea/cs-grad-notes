# The Rank Nullity Theorem

???+ theorem "Rank-Nullity theorem"

    Let $V,W$ be vector spaces over $F$ and $T:V\to W$ be linear.

    $$
    \dim(V)=\text{rank}(T)+\text{nullity}(T)
    $$
    

???+ theorem

    Let $V,W$ be vector spaces over $F$ and let $T:V\to W$ be linear. $\text{ker}(T)=\{0\}$ if and only if $T$ is injective.
    

???+ theorem
    
    Let $V,W$ be finite dimensional vector spaces over $F$ with same dimensions, and let $T:V\to W$ be linear. TFAE

    1. $T$ is injective.
    2. $T$ is surjective.
    3. $\text{ker}(T)=\{0\}$.
    4. $\text{range}(T)=W$.
    5. $T$ is invertible.


## Results of the injectivity and surjectivity of linear maps

???+ theorem
    
    Let $V$ and $W$ be vector spaces over $F$ and suppose $\dim(V)>\dim(W)$. There is no injective linear map from $V$ to $W$.

    ??? note "Why?"
        If $T:V\to W$ is linear and injective, then by the rank-nullity theorem

        $$
        \text{rank}(T)\le\dim(W)<\dim(V)=\text{rank}(T)+\underbrace{\text{nullity}(T)}_{0}=\text{rank}(T),
        $$
        
        which is a contradiction.

???+ theorem
    
    Let $V$ and $W$ be vector spaces over $F$ and suppose $\dim(V)<\dim(W)$. There is no surjective linear map from $V$ to $W$.

    ??? note "Why?"
        If $T:V\to W$ is linear and surjective, then by the rank-nullity theorem

        $$
        \dim(W)>\dim(V)=\text{rank}(T)+\text{nullity}(T)=\dim(W)+\text{nullity}(T)\ge\dim(W)
        $$
        
        which is a contradiction.
