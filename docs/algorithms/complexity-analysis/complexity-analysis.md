# Asymptotic notations


!!! definition "Asymptotic Notations"
    
    Let $f,g\in\mathcal{F}(\mathbb{N},\mathbb{R}_{>0})$.
    !!! definition "Big-O notation"
        We say $f(n)=O(g(n))$ if there are $c>0$ and $n_0\in\mathbb{N}$, such that if $n\ge n_0$, then $f(n)\le cg(n)$.
        
    !!! definition "Big-Omega notation"
        We say $f(n)=\Omega(g(n))$ if there are $c>0$ and $n_0\in\mathbb{N}$, such that if $n\ge n_0$, then

        $$
        cf(n)\le g(n).
        $$

    !!! definition "Big-Theta notation"
        We say $f(n)=\Theta(g(n))$ if there are $c_1\ge c_2>0$ and $n_0\in\mathbb{N}$, such that if $n\ge n_0$, then 

        $$
        c_2g(n)\le f(n)\le c_1g(n).
        $$

    !!! definition "Small-o notation"
        We say $f(n)=o(g(n))$ if for all $\varepsilon>0$, there exists $n_0\in\mathbb{N}$, such that

        $$
        \dfrac{f(n)}{g(n)}<\varepsilon.
        $$

    !!! definition "Big-O notation"
        We say $f(n)=\omega(g(n))$ if for all $\varepsilon>0$, there exists $n_0\in\mathbb{N}$, such that

        $$
        \dfrac{g(n)}{f(n)}<\varepsilon.
        $$
    

???+ theorem "Properties of Asymptotic notations"

    - $f(n)=O(g(n))$ if and only if $g(n)=\Omega(f(n))$.
    - $f(n)=O(g(n))$ if and only if $f(n)=O(g(n)+C)$ where $C>0$ is a constant.
    - $f(n)=\Omega(g(n))$ if and only if $f(n)=\Omega(g(n)+C)$ where $C<0$ is a constant.
    - $f(n)=o(g(n))$ if and only if $f(n)=O(g(n))$ and $f(n)\neq\Theta(g(n))$.
    


???+ note
    演算法分析根本就是微積分
