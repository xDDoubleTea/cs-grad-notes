# Contiguous memory allocation


## Fixed partition allocation

- Well, memory size is fixed

## Variable size partition

- Well, memory size is variable
- Hole: block of contiguous free memory
- Holes of various size are scattered in memory

## Dynamic storage allocation problem


!!! problem "How to satisfy a request of size $n$ from a list of free holes?"

    - First-fit : allocate the 1st hole that fits
    - Best-fit : allocate the smallest hole that fits
    - Worst-fit: allocate the largest hole


## Fragmentation
    

### External fragmentation


- Total is big enough, but not contiguous
- Occur in variable-size allocation


### Internal fragmentation


- Memory that is internal to a partition but not being used
- Occur in fixed-partition allocation


### Solution

!!! example Compaction

    - Shuffle memory contents to place all free memory together in one large block at runtime
    - Only if binding is done at runtime

