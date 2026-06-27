# Diagonalization

???+ abstract "對角化"
        
    設$A\in\text{M}_{n\times n}(F)$可對角化

    - 找特徵值 [(How?)](./eigenvalue-calculations.md)
    - 找出$\ker(A-\lambda_i I)$的基底，就是特徵向量
    - 把特徵向量對照特徵值排好，當列向量放進$S\in\text{M}_{n\times n}(F)$中
    - $A=SDS^{-1}$
    
???+ abstract "正交對角化"
        
    設$A\in\text{M}_{n\times n}(F)$可正交對角化

    - 找特徵值 [(How?)](./eigenvalue-calculations.md)
    - 找出$\ker(A-\lambda_i I)$的基底，就是特徵向量
    - 特徵多項式有重根，也就是說如果$(\lambda-\lambda_i)^2\mid\det(A-tI)$，就對$\ker(A-\lambda_i I)$的基底做[Gram Schmidt](./gram-schmidt.md)
    - 把所有特徵向量單位化，也就是除掉本身長度
    - 把特徵向量對照特徵值排好，當列向量放進$S\in\text{M}_{n\times n}(F)$中
    - $A=SDS^{-1}$
    
    ???+ notes

        - $A\in\text{M}_{n\times n}(\mathbb{R})$可正交對角化$\iff A^T=A$
        - $A\in\text{M}_{n\times n}(\mathbb{C})$可正交對角化$\iff A^*A=AA^*$
        - 不同特徵值所對應的特徵向量必正交
        - $F=\mathbb{R}\implies S\in O(n)\iff SS^T=I$
        - $F=\mathbb{C}\implies S\in U(n)\iff SS^*=I$
