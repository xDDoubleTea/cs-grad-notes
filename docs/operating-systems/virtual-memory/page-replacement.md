# Page Replacement

## What if no free frame whne a page fault occurs?

- We need an algorithm to decide which page to swap back to disk, then swap the page to the frame

- Use a dirty bit to reduce overhead of page transfers, i.e., only modified pages are written to disk

- There are 2 algorithms need to 

## Algorithm

- Goal: **lowest page-fault rate** 
- Evaluation: running against a string of memory references and computing the number of page faults

- FIFO algorithm
- Optimal algorithm
- LRU algorithm
- Counting algorithm
    - **LFU** 
    - MFU

### FIFO


- Oldest page in a FIFO queue (fixed size) is replaced

!!! note "Belady's Anomaly"
    
    - More frame does not imply less page faults
    - Very bad :(

### Optimal (Belady) Algorithm

- Replace the page that will not be used for *the longest period of time*

> Needs future knowledge

- In practice we don't have future knowledge :(

### LRU

- Let's just look backward (program has locality)
- Replaces the page that has not been used for the longest period of time
- Often used, and is considered as quite good

!!! example "Counter implementation"

    - Page referenced: time stamp is copied into the counter
    - replacement: remove the one with the oldest counter (so needs linear search)
    - **time stamp** is copied into the counter

!!! example "Stack implementation"
    
    - Page referenced: move to top of the double-linked list
    - Replacement: remove the page at the bottom
    - We can use hash map to find the referenced page

    > 簡單來說就是沒用到的每次都往後推，有用到的放最上面（參考zoxide）

!!! definition "Stack Algorithm"

    - A **property** of algorithm 
    
    - **Stack algorithm**: the set of pages in memory for $n$ frames is always a subset of the set of pages that would be in memory with $n+1$ frames 

    > 就是只進不出

    - **Stack algorithms do not suffer from Belady's anomaly** 

    - Both optimal algorithm and LRU algorithm are stack algorithms

### LRU approximation algorithms

- **Few systems** provide sufficient hardware support for the LRU page-replacement
    - additional-reference-bits algorithms
    - second-chance algorithm
    - enhanced second-chance algorithm



### LFU Algorithm (Least Frequently Used)

- Global
- Replacement: replace the least frequently used
- If one page is used in a burst, and never used after the burst, the page may be stuck in the frames


### MFU Algorithm (Most Frequently Used)

- Local
- Replacement: replace the most frequently used
- Idea: The page with smallest count was probably just brought in and has yet to be used

!!! danger
    
    LFU and MFU are not common, because implementation is expensive, and is not that trivial
