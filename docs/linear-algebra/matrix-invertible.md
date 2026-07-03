# Invertible matrices


???+ theorem "Maxtrix invertibility"
    
    Let $A\in\text{M}_{n\times n}(F)$. TFAE:
    
    - $A$ is nonsingular
    - $\exists!B\in\text{M}_{n\times n}(F),\text{s.t. }AB=BA=I$
    - $0$ is not an eigenvalue of $A$
    - $\det(A)\neq0$
    - $\text{rank}(A)=n$
    - $\text{nullity}(A)=0$
    - Columns of $A$ form a basis of $F^n$
    - Rows of $A$ form a basis of $F^n$
    

???+ abstract "怎麼算反矩陣"
    
    - 對增廣矩陣$[\ A\ |\ I\ ]$做高斯消去法
    - 特殊矩陣如正交或么正算子，直接轉置取複數共軛
    - 對角矩陣直接把對角線元素倒數
