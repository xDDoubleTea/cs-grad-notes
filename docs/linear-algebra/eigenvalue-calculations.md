# Eigenvalue calculations


!!! definition "Eigenvalue of a linear transformation"
    
    Let $V$ be a vector space over $F$ and let $T:V\to V$ be linear. We say $\lambda\in F$ is an *eigenvalue* of $T$ if 

    $$
    T(v)=\lambda v,
    $$

    for some $v\in V\backslash\{0\}$. Such $v$ is called an *eigenvector* corresponding to the eigenvalue $\lambda$.

!!! example "Example （我不知道我亂出的）"
    
    Let $V=\mathsf{P}(\mathbb{R})$, the vector space containing all real polynomials, and let $T:V\to V$ be defined by

    $$
    T(f(x))=\dfrac{d}{dx}f(x)+\int_{0}^{1}f(x)dx.
    $$

    1. Is $T$ linear?
    2. If $T$ is linear, find all of the eigenvalues of $T$.
    3. Is $T$ injective?
    


??? exercise "Solution"

    1. Yes, $T$ is linear.
    
    $$
    \begin{align*}
    T(f(x)+c\cdot g(x))&=\dfrac{d}{dx}(f(x)+c\cdot g(x))+\int_{0}^{1}(f(x)+c\cdot g(x))\\
                       &=\dfrac{d}{dx}f(x)+c\dfrac{d}{dx}g(x)+\int_{0}^{1}f(x)dx+c\int_{0}^{1}g(x)dx\\
                       &=\left(\dfrac{d}{dx}f(x)+\int_{0}^{1}f(x)dx\right)+c\left(\dfrac{d}{dx}g(x)+\int_{0}^{1}g(x)dx\right)\\
                       &=T(f(x))+cT(g(x))
    \end{align*}
    $$

    Since $T(1)=0+1=1$, $1$ is an eigenvalue of $T$. For $n\ge 1$, since
    
    $$
    T(x^n)=x^{n-1}+\frac{1}{n+1}\neq\lambda x^n,
    $$

    for any $\lambda\in\mathbb{R}$, the only eigenvalue of $T$ is $1$, and $1$ is an eigenvector corresponding to it.

    $T$ is not injective, since

    $$
    T(2x-3)=2+\int_{0}^{1}(2x-3)dx=2+(-2)=0=T(0).
    $$
    
    

???+ tip "觀察法"
    
    !!! danger "注意"
        只適用在有限維度！！！
    $A\in\text{M}_{n\times n}(F)$

    1. 看$A$行列式是不是$0$。[(How?)](./determinant.md)
    2. 猜一個整數$k$，看$A$對角線減去$k$行列式是不是$0$。
    3. 特徵值的和等於trace，特徵值的乘積等於對角線元素乘積，列方程，用上面的$k$化成$2$次式。
    4. 牛頓有理根檢驗法

???+ tip "公式解"
    
    - 若$A\in\text{M}_{3\times 3}(F)$，則

    $$
    \det(\lambda I-A)=\lambda^3-\text{tr}(A)\lambda^2+S_2\lambda-\det(A)
    $$

    - 若$A\in\text{M}_{2\times 2}(F)$，則

    $$
    \det(\lambda I-A)=\lambda^2-\text{tr}(A)\lambda+\det(A)
    $$

???+ tip "驗算法"

    設$A\in\text{M}_{n\times n}(F)$

    1. $\text{nullity}(A-\lambda_i I)$一定至少是$1$，也就是說$\text{rank}(A-\lambda_i I)<n$
    2. 檢驗$\text{tr}(A)=\sum\lambda_i$
    3. 檢驗$\prod_{i=1}^{n}a_{ii}=\prod_{i=1}^n\lambda_i$
    4. 檢驗$Av=\lambda_iv$，其中$v$是對應到$\lambda_i$的特徵向量
