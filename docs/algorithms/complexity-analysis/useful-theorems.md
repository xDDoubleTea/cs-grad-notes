# Useful theorems

???+ theorem "Stirling's factorial approximation theorem"
    
    $$
    n!=\sqrt{2\pi n}\left(\dfrac{n}{e}\right)^n\left(1+\Theta\left(\dfrac{1}{n}\right)\right)=\Theta(n^{n+0.5}e^{-n})
    $$
    
???+ theorem
    
    $$
    f(n)+g(n)=\Theta(\max(f(n),g(n)))
    $$

???+ theorem

    Let $m\in\mathbb{N}$. Then

    $$
    \sum_{k=1}^{n}k^m=\Theta(n^{m+1}).
    $$

    ??? note "proof"
        
        For $m=1$, since
    
        $$
        \sum_{k=1}^{n}k=\frac{n(n+1)}{2}
        $$
        
        it is clear that the theorem holds.

        Assume the theorem holds for some $s\in\{1,2,\dots,m-1\}$, where $m\ge 2$. Since
    
        $$
        (k+1)^{m+1}-k^{m+1}=\sum_{s=1}^{m}\binom{m+1}{s}k^{s},
        $$

        $$
        \begin{align*}
        \sum_{k=1}^{n}\left((k+1)^{m+1}-k^{m+1}\right)&=1+n^{m+1}\\
                                    &=\left(\sum_{k=1}^n\sum_{s=1}^{m}\binom{m+1}{s}k^{s}\right)\\
                                    &=\left(\sum_{s=1}^{m}\binom{m+1}{s}\sum_{k=1}^{n}k^s\right)\\
        \end{align*}
        $$

        By induction hypothesis, for $s\in\{1,2,\dots,m-1\}$, we have

        $$
        \sum_{k=1}^{n}k^s=\Theta(n^{s+1})
        $$

        Since $1+n^{m+1}$ is of $\Theta(n^{m+1})$, RHS is also of $\Theta(n^{m})$, and combining the induction hypothesis,
        
        $$
        \begin{align*}
        \sum_{s=1}^{m}\binom{m+1}{s}\sum_{k=1}^{n}k^s&=(m+1)\sum_{k=1}^{n}k^{m}+\left(\sum_{s=1}^{m}\binom{m+1}{s}\sum_{k=1}^{n}k^s\right)\\
                                                       &=(m+1)\sum_{k=1}^{n}k^{m}+\Theta(n^{m}+n^{m-1}+\dots+n)=\Theta(n^{m+1}).
        \end{align*}
        $$

        Because $\Theta(n^m+n^{m-1}+\dots+n)=\Theta(n^{m})$, this forces $\sum_{k=1}^{n}k^{m}=\Theta(n^{m+1})$, which completes the induction.
        

???+ theorem
    
    
    
    $f(n)=\Theta(g(n))$ if and only if $f(n)=O(g(n))$ and $f(n)=\Omega(g(n))$.
    

    ??? note "usage"

        Show that

        $$
        \lg n!=\Theta(n\lg n).
        $$

        ??? note "proof"
            
            Since

            $$
            \lg n!=\sum_{k=1}^{n}\lg k\le \sum_{k=1}^{n}\lg n=n\lg n,
            $$
            
            $\lg n!=O(n\lg n)$.
        

            Since

            $$
            \lg n!=\sum_{k=1}^{n}\lg k\ge\sum_{k=\lceil\frac{n}{2}\rceil}^{n}\lg\left\lceil\frac{n}{2}\right\rceil\ge\left\lceil\frac{n}{2}\right\rceil\lg\left\lceil\frac{n}{2}\right\rceil,
            $$

            $\lg n!=\Omega(n\lg n)$.

## Polynomially boundedness

!!! definition "Polynomially boundedness"
    
    $f(n)$ is said to be *polynomially bounded* if $f(n)=\Theta(n^m)$ for some $m\in\mathbb{N}$.

???+ theorem

    $f$ is polynomially bounded if and only if $\lg f(n)=O(\lg n)$.
    
    ???+ note "proof"
        
        Suppose $f$ is polynomially bounded. There are $m,n_0\in\mathbb{N}$ and $c_1\ge c_2>0$ such that
        
        $$
        f(n)\le c_1n^m
        $$

        for $n\ge n_0$.

        Since $\lg x$ is strictly increasing, for $n\ge n_0$, we have
        
        $$
        \lg f(n)\le\lg c_1+m\lg n,
        $$
    
        i.e., $f(n)=O(\lg c_1+m\lg n)=O(\lg n)$.
        
        Suppose that $\lg f(n)=O(\lg n)$. Then there are $c_1\ge c_2>0$ and $n_0\in\mathbb{N}$ such that if $n\ge n_0$, 

        $$
        f(n)\le n^{c_1}
        $$

        Therefore, $f$ is polynomially bounded.
        
