# Gram Schmidt

???+ theorem "Gram Schmidt"

    Let $V$ be a finite dimensional inner product space and $\{v_1,\dots,v_k\}$ be a linearly independent subset of $V$. The vectors $w_i$ recursively defined by

    $$
    w_1=v_1,w_j=v_j-\sum_{i=1}^{j-1}\frac{\langle v_j,w_{i}\rangle}{\|w_{i}\|^2}w_{i},2\le j\le k
    $$

    form an linearly independent and orthogonal set. Moreover, the span of $\{v_1,\dots,v_k\}$ is equal to the span of $\{w_1,\dots,w_k\}$.
    
???+ quote
    Gram Schmidt 就是把下一個向量扣掉關於排在他前面的所有向量的正射影，得到的其實就是垂直分量。
