# Block matrices multiplication

!!! definition "Partitions of matrices"
    
    Let $A\in\text{M}_{m\times n}(F)$, where $m$ and $n$ are both integers greater than or equal to $2$.
    
    We write

    $$
    A=\left(\begin{array}{c|c}A_{11} & A_{12}\\\hline A_{21} & A_{22}\end{array}\right),
    $$

    where

    $$
    \begin{cases}
    A_{11}\in\text{M}_{p\times q}(F)\\
    A_{12}\in\text{M}_{p\times (n-q)}(F)\\
    A_{21}\in\text{M}_{(m-p)\times q}(F)\\
    A_{22}\in\text{M}_{(m-p)\times(n-q)}(F)\\
    \end{cases}
    $$
    
    if $(A_{11})_{ij}=A_{ij}$, $(A_{12})_{ij}=A_{i(j+q)}$, $(A_{21})_{ij}=A_{(i+p)j}$, and $(A_{22})_{ij}=A_{(i+p)(j+q)}$.

    We say that $A$ is partitioned to four blocks in this case.

    Simillarly, we can define partitions with more blocks.

???+ theorem

    Let $A\in\text{M}_{m\times n}(F)$ and $B\in\text{M}_{n\times r}(F)$ be partitioned as
    

    $$
    A=\left(\begin{array}{c|c}A_{11} & A_{12}\\\hline A_{21} & A_{22}\end{array}\right),
    $$

    $$
    B=\left(\begin{array}{c|c}B_{11} & B_{12}\\\hline B_{21} & B_{22}\end{array}\right),
    $$

    where

    $$
    \begin{cases}
    A_{11}\in\text{M}_{p\times q}(F),B_{11}\in\text{M}_{q\times s}(F)\\
    A_{12}\in\text{M}_{p\times (n-q)}(F),B_{12}\in\text{M}_{q\times(r-s)}(F)\\
    A_{21}\in\text{M}_{(m-p)\times q}(F),B_{21}\in\text{M}_{(n-q)\times s}(F)\\
    A_{22}\in\text{M}_{(m-p)\times(n-q)}(F),B_{22}\in\text{M}_{(n-q)\times(r-s)}(F)\\
    \end{cases}
    $$

    Then

    $$
    AB=\left(\begin{array}{c|c}A_{11}B_{11}+A_{12}B_{21} & A_{11}B_{12}+A_{12}B_{22}\\\hline A_{21}B_{11}+A_{22}B_{21} & A_{21}B_{12}+A_{22}B_{22}\end{array}\right).
    $$


## Why?

> Because


計算的時候把好算的放一堆乘在一起會更快


## Some techniques

???+ tip

    !!! example
        
        Let

        $$
        A=(1,2,-1,67)^T, B=(3,4,1,6),C=AB.
        $$

        Find $C^{100}$.


        ??? abstract "Solution"
            
            $$
            C=\begin{pmatrix}
            3 & 4 & 1 & 6\\
            6 & 8 & 2 & 12\\
            -3 & -4 & -1 & -6\\
            201 & 268 & 67 & 402
            \end{pmatrix}
            $$

            Calculating $C^2$ will be a nightmare if doing entry-wise multiplication. Notice that

            $$
            C^2=C\cdot C=\left(\begin{array}{c|c}3A & 4A & A & 6A\end{array}\right)\cdot\left(\begin{array}{c}B\\\hline 2B\\\hline -B\\\hline 67B\end{array}\right)=\text{tr}(C)C
            $$

            Therefore, $C^{n}$ is actually just $(\text{tr}(C))^{n-1}C$ for $n\ge 1$, by mathematical induction. Therefore $C^{100}=(\text{tr}(C))^{99}C$.


    !!! example

        Show that

        $$
        O(n)\cap O(p,q)\simeq O(p)\times O(q)
        $$
