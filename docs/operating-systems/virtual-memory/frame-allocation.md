# Allocation of Frames

- Each process needs **minimum** number of frames

## Allocation Policies

- **Fixed allocation**
    - Equal allocation : 100 frames and 5 processes, then allocate 20 frames per processes
    - Proportional allocation: Allocate according to the size of the process

- **Priority allocation**
    
    - Using propotional allocation based on priority, instead of size
    - if process P generates a page fault
        - select for replacement one of its frames
        - select for replacement from a process with lower priority

- **Local allocation** : each process select from its own set of allocated frames
- **Global allocation** : process selects a replacement frame frome the set of all frames
    - one process can take away a frame of another process
    - e.g., allow a high-priority process to take frames from a low-priority process
    - good system performance and thus is common used
    - A minimum number of frames must be maintained for each process to prevent [thrashing](./thrashing.md)
