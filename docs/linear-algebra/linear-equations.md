# Linear equations

!!! definition "System of linear equations"
    
    Let $a_{i,j},b_i\in F$ be constants where $i=1,2,\dots,m,j=1,2,\dots,n$. The equations of the form

    $$
    \begin{cases}
    b_1&=a_{1,1}x_1+a_{1,2}x_2+\dots+a_{1,n}x_n\\
    b_2&=a_{2,1}x_1+a_{2,2}x_2+\dots+a_{2,n}x_n\\
         \vdots&\\
    b_m&=a_{m,1}x_1+a_{m,2}x_2+\dots+a_{m,n}x_n\\
    \end{cases}
    $$
    
    is called a *system of linear equations*.
    
    It is clear that we can write it as $Ax=b$ where $x,b\in F^m,A\in\text{M}_{m\times n}(F)$ and $A_{i,j}=a_{i,j}$.


!!! definition "Consistency"
    
    A system of linear equations $Ax=b$ is said to be *consistent* if there is $x_0\in F^m$ such that $Ax_0=b$. It is said to be *inconsistent* if it is not consistent.

!!! definition "Augmented matrix"
    
    Let $A\in\text{M}_{m\times n}(F),B\in\text{M}_{m\times p}(F)$ where $F$ is a field. The *augmented matrix* of $A$ and $B$, denoted by $[\,A\,|\,B\,]$ is a $m\times (n+p)$ matrix that

    $$
    [\,A\,|\,B\,]_{i,j}=\begin{cases}A_{i,j},&\text{if }j\le n\\B_{i,j},&\text{if }j>n\end{cases}
    $$

    We also say that $A$ is augmented with $B$ or $B$ augments with $A$ in this case.

???+ theorem "Gaussian elemination"

    [Gaussian elemination](./numerical-methods/gaussian.md)
