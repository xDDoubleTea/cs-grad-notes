# Demand Paging

## What is demand paging

- A page is brought into memory only when it is needed
- Page is needed when there is a reference to the page
- **Pure demand paging** 
    - Start a process with no page
    - Never bring a page into memory until it is reqired.

!!! note 
    
    - Basically lazy loading

## How to do demand paging

- **Swapper** manipulates the entire process, while a pager is concerned with the individual pages of a process.
### Hardware support

- **Page Table** : a valid-invalid bit
    - `1` means page in memory, `0` means not
    - All bits are set to `0` initially.

- Secondary memory is used.

## Page Fault

- First reference to a page will trap to OS, called **page-fault trap** 

- OS will look at the internal talbe in PCB to see if it is a valid reference
- Get an empty frame
- Swap the page from disk into the frame
- Reset page table setting the valid-invalid bit to `1`
- ***Restart the instruction*** (`PC -= 4`)

## Demand Paging Performance

- Effective Access Time

$$
\text{EAT}=(1-p)\times ma+p\times pft
$$

where $ma$ is the memory access time (from memory to CPU register), $pft$ is page fault time, and $p$ is page fault rate.

Programs tend to have locality of reference (unless you use linked list for every thing), since a single page fault brings in 4KB of memory content, the page fault rate is reduced greatly.

- Page fault time is dominated by disk access time


