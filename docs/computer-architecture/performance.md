# Performance

!!! definition "名詞"

    - Latency (Response time, execution time) : 工作開始到完成的時間
    - Throughput : 生產量


    !!! definition "Performance of computer X"
        
        $$
        \text{Performance}_X:=\dfrac{1}{\text{Latency}_X}
        $$

    
    !!! definition "Performance comparison"
    
        $X$ is faster than $Y$ by $n$ times means

        $$
        \dfrac{\text{Performance}_X}{\text{Performance}_Y}=\dfrac{\text{Latency}_Y}{\text{Latency}_X}=n
        $$

## CPI

[CPI](./cpi.md)

## Amdahl's law

???+ theorem "Amdahl's Law"

    $$
    \text{Latency}'=\dfrac{\text{Latency}_s}{F}+\text{Latency}_n
    $$
    

    - $\text{Latency}_s$ is the original latency of the part that will speed up after the improvement.
    - $\text{Latency}_n$ is the original latency of the part that will not speed up after the improvement.
    - $F$ is the speedup factor.

    ???+ theorem "Speedup factor"
        
        $$
        S=\frac{1}{r/F+(1-r)}
        $$

        - $S$ is the speedup after improvement
        - $F$ is the improvement factor
        - $r$ is the fraction of the program that is affected by the improvement

    > Therefore, we can **make common case fast** to obtain significant speedup.


## Performance summary

???+ definition "Geometric mean"
    
    
