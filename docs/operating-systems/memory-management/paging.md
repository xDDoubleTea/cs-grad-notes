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


### Page table base register



