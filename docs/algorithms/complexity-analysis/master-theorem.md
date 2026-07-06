# The Master Theorem


???+ theorem "The Master Theorem (From Discrete mathematics)"
    
    Let $f(n),g(n)$ be a functions that satisfies

    $$
    f(n)=af\left(\dfrac{n}{b}\right)+cn^d,
    $$
    
    whenever $n=b^k$, where $k$ is a positive integer, $a\ge 1,b>1$ are constants, and $c>0$ and $d\ge0$ are real numbers.

    Then

    $$
    f(n)=\begin{cases}O(n^d),&\text{if }\log_b a<d\\O(n^d\log n),&\text{if }\log_b a=d\\O(n^{\log_{n}a}),&\text{if }\log_b a>d\end{cases}.
    $$

!!! example

    The time complexity of the merge sort algorithm is $O(n\log n)$.

    !!! abstract "proof"
        
        Let $T(n)$ be the time required to sort $n$ numbers using merge sort. Then it is easy to see that

        $$
        T(n)=2T\left(\frac{n}{2}\right)+n^1
        $$

        By the Master Theorem, since $\log_2 2=1$, $T(n)=O(n\log n)$.

    
???+ theorem "The Master theorem (From [wikipedia](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)) and some modified notations)"
    
    Let $T(n)$ denote the total time for the algorithm on an input size of $n$, and let $f(n)$ denote the amount of time taken at the top level of the recurrence, then

    $$
    T(n)=aT\left(\frac{n}{b}\right)+f(n)
    $$

    where $a\ge 1$ and $b>1$. $a$ is the number of subproblems in the recursion, and $b$ is the size of the subproblem. The reason $b>1$ is that we have to make the problem become smaller to eventually hit the base case.


    Let $d:=\log_b a$. Then


    $$
    T(n)=\begin{cases}\Theta\left(n^d\right),&\text{if }\exists\varepsilon>0,\text{s.t. }f(n)=O\left(n^{d-\varepsilon}\right)\\\Theta\left(n^d\log^k n\right),&\text{if }f(n)=\Theta\left(n^d\log^{k+1} n\right),k\ge 0\\\Theta(f(n)),&\text{if }\exists\varepsilon>0,k<1,n_0\in\mathbb{N},\text{s.t. }f(n)=\Omega\left(n^{d+\varepsilon}\right)\text{ and }n\ge n_0\implies af\left(\dfrac{n}{b}\right)\le kf(n)\end{cases}
    $$
