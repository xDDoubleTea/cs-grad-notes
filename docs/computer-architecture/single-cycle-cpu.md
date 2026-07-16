# Single cycle CPU

![Single-cycle CPU](../assets/single-cycle-cpu.png)

## How to execute an instruction

### Instruction Fetch (IF)

- Fetches the instruction pointed to by PC from instruction memory

!!! note

    Also calculates PC + 4 for the next instruction (PC + $x$) where $x$ is the size (in bytes) of current instruction


### Instruction Decode (ID)

- Decode and **read register operands (rs2, rs1)**

### Execute (EX)

- Execute according to instruction type

### Memory Reference (MEM)

- **Memory access** 

!!! note

    For instruction `sd`, it will store `rs2` to memory and *write PC + 4* into PC

### Register Write Back (WB)

- **Write register back to RF and PC** 

## Components

- ALU
- PC
- Adder
- Register file
- Instruction memory
- Data memory
- Control signals
- Sign extension unit



## Control Signals






## Combinational / Sequential Circuit


