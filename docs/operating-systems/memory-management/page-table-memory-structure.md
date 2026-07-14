# Page Table Memory Structure

## Problem

- Page table could be huge and difficult to be loaded, because it is hard to find a **contiguous** chunk of memory that is huge
- Need to break it into several smaller page tables


## Solutions

### Hierarchical Paging

- Break up the logical address space into **multiple page tables** 
- Typically a tree like structure

!!! quote
    - 就是page table的page table的page table套娃

!!! problem

    - $64$ bit address need more levels, which will cause more memory accesses (slow)

### Hash Page Tables

- Hash virutal page number into a hash table
- More buckets then the overflow list is then shorter

!!! problem

    - Pointers waste memory
    - Traverse linked list waste time and cause additional memory references

### Inverted Page Table

- Maintains NO page table for each process
- Maintains a *frame table* for the whole memory
- Each entry contains PID and Page Number
- No memory needed for page tables, but increase memory access time
    - Each access needs to search the whole frame table
    - Can use hashing for frame table
- Hard to support **shared page/memory**

## Solutions are slow??

!!! note 

    - Yes they are slow if TLB does not exist. The TLB hit-rate is so high (up to $99\%$) so that the penalty is basically just the TLB lookup time and one memory access time.
    - Modern 64-bit Linux (x86_64) uses 4-level paging, and recently added support for $5$ level paging


    !!! example "Gemini這樣說"
        Linux kernel 7.1 uses a 5-level page table abstraction internally (PGD, P4D, PUD, PMD, PTE).

        The actual number of levels utilized depends on the hardware:

        * **Default (x86_64):** 4-level paging (48-bit virtual addresses).
        * **Extended (x86_64):** 5-level paging (LA57) for modern processors requiring 57-bit virtual addresses.

        When running on hardware that only requires 4 levels, the kernel folds (bypasses) the P4D level to prevent performance overhead.
