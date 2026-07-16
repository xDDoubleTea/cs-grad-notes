# Page and frames

## Paging

- Divide physical memory into fixed-sized blocks called *frames*
- Divide logical address space into blocks of the same size called *pages*
- $n$ pages need $n$ free frames
- **keep track of free frames**

!!! note

    - **Physical** $\to$ **Frames**
    - **Logical** $\to$ **Pages**

### Benifit

- Allow physical address space to be noncontiguous
- Avoid external fragmentation $\because$ **fixed-size**
- Limited internal fragmentation (Maybe many page tables)
- Provide **shared memory/pages** (Can support dynamic linking for example)

## Page table

- Each entry maps to the **base address of a pages** in physical memory
- **Maintained by OS for each process**

!!! note

    - Page table includes only pages owned by a process
    - Process cannot access memory outside its space

## Address Translation

### Logical address

- Page number $p$, $N$ bit means process can allocate at most $2^N$ pages.
    - A process can allocate at most $2^N\times\text{Page size}$ memory

- Page offset $d$
    - $K$ bit means page size is $2^K$ bit

$$
\text{Physical addr}=p+d
$$


### How to allocate frame

- Maintain a *free-frame list*

### Page / Frame Size

- Defined by hardware
- A power of $2$
- Ranging from $512$ bytes to $16$ MB per page (larger page size may cause more internal fragmentation)
- $4$ KB or $8$ KB page size
- $64$ bit systems will cause page number to increase

!!! note

    - Page size have grown over time so that page table can be smaller

    - OS maintains a copy of the **page table for each process**
    - OS maintains a **frame table** for managing physical memory
        - Maybe useful sometimes but typically not used

    - Translation is done using hardware!!!!!

## Implementation of page table


### Page table base register (PTBR)

- The **Physical memory address** of the page table
- The PTBR value is stored in the **PCB** of a process
- Need to change the value of PTBR during **Context switch** 

!!! note

    - With PTBR only, each memory reference results in $2$ memory reads
    - Use a cache ([TLB](#translation-look-aside-buffers-tlb)) to speed up the common case
    - PTBR and TLB are hardware implementations


### Translation Look-aside Buffers (TLB)

- Implemented by **Associative memory** (can do parallel search)
- **A cache for page table shared by all processes** 
- TLB must be flushed after a context switch
    - Otherwise, TLB entry must has a PID field (address-space identifiers (ASIDs))
    - Mostly just flushes everything, because the modern process uses a lot of memory so that the TLB is basically full after context switch



### Effective Memory-Access Time

$$
\begin{cases}
r=\text{TLB hit rate}\\
T_s=\text{TLB search time}\\
T_M=\text{Memory access time}
\end{cases}
$$


$$
\text{EMAT}=r(T_s+T_M)+(1-r)\times(T_s+2T_M)
$$

!!! note

    - The modern TLB hit-ratio can be up to $98\%$, because usually the memory access has locality, and a page has $4$ KB

> vs. [AMAT](../../computer-architecture/memory-hierarchy/#amat)

## Memory protection

- Each page is associated with a set of **protection bit** in the page table

!!! example "Valid-invalid bit"
    - Valid: the page/frame is **in the process' logical address space** 
    - Invalid: well, it is not Valid

    !!! note "Issues"
        - Un-used page entry cause memory waste
        - The process may not access the memory on the boundary of a page

    !!! note "Solutions"
        - Use a page table length register (PTLR)
        - Use memory limit register

## Shared pages

- Paging allows processes share common code, which must be **reentrant** 
- **Only one copy** of the shared code needs to be kept in physical memory
- **Two (several) virtual addresses** are mapped to one physical address

### Reentrant code (pure code)

- Never change during execution
- Text editors, compilers, web servers, etc...




