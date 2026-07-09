# Interprocess Communication IPC


- IPC : a set of methods for the exchange of data among multiple threads in one or more processes
- Independent process : cannot affect ofr be affected
- Cooperating process: otherwise

## Why IPC?

- Info sharing
- Computation speedup
- Convenience
- Modularity

## Methods

### Shared memory

- Require careful user synchronization (Race condition)
- Use memory address to access data

!!! problem "Consumer & Producer Problem"

    Producer process produces information that is consumed by a consumer process

!!! example "A solution"

    Buffer size `B`.

    - next free : `in`
    - first avaliable: `out`
    - empty: `in == out`
    - full: `(in + 1)% B == out`

    A round-robin solution.

    - at most `B-1` item in the buffer, otherwise cannot tell if the buffer is full or empty

    
    


### Message passing

- More efficient for small data
- Send or recieve message
- Uses system call
- Synchronization


    
    
    


### Socket

- IP & port (port = process)
- Exchange unstructured stream of bytes

### RPC/gRPC

- Remotely call a procedure


