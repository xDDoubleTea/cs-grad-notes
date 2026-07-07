# Mainframe systems

## Batch

- One job at a time
- No interaction between users and jobs
- CPU is often idle

### Tasks

- No decision need to be made by os

## Multi-programming

- Overlaps IO and computations
- Spooling (Simultaneous Peripheral Operation On-Line)
    - IO is done with no CPU intervention
    - CPU just needs to be notified when IO is done

### Tasks

- Memory management
- CPU scheduling
- IO system

## Time-sharing

- Interactive
- Multiple users can share the computer simultaneously

### Tasks

- Virtual memory (prevent program accessing each others memory)
- File system
- Disk management
- Process synchronization
- Deadlock
