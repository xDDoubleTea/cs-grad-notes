# System structure

## Simple OS Architecture

- Only one or two levels of code
- Drawbacks: Un-safe, difficult to enhance and maintain

!!! example "Examples"
    - MS-DOS
    - UNIX

## Layered OS Architecture

- $N$-th layer can only access services provided by $0$ to $(N-1)$-th layer
- Less efficient, difficult to define layers

## Microkernel OS

- Kernel is responsible for commuicating between *modules* and modules live in "user" space

!!! example 
    
    - QNX : commuication, scheduling, web and signals
    - Mach


## Modular OS Architecture

- Object-oriented
- Core component is separated

[https://wiki.archlinux.org/title/Kernel_module](https://wiki.archlinux.org/title/Kernel_module)

## Virtual Machine

- Hard : the kernel of the VM think it is in kernel mode
- Sol : Let the vm implementation do system call for it

However, it is slower because it might do more than 2 system calls.

???+ example "Another solution: KVM (Kernel-based virtual machine)"
    
    Modern CPUs introduces another privileged level below ring 0 (kernel) for virtualization. It still blocks some sensitive instructions, but it enables most of the privileged instructions so that KVM can directly execute instead of doing system calls.
    

??? example "Why is KVM so much faster?"

    ???+ note
        Because it runs basically any instruction directly on the host's CPU, except for the sensitive ones.

    To tie this perfectly into your OS studies, there is just one slight terminology tweak to make your understanding flawless: in traditional VMs, the Guest OS isn't voluntarily making a "system call" to the Host. Instead, it's triggering an **Exception (or Fault)**.

    Here is the exact breakdown of why traditional VMs suffer such massive performance penalties compared to KVM:

    ### The Traditional VM Nightmare (Trap-and-Emulate)

    Because the traditional VM guest kernel is forced to run in User Mode (Ring 3), it lacks the actual hardware privileges it thinks it has.

    Imagine the Guest OS simply wants to do something basic for a kernel, like updating its own internal page tables (Memory Management).

    1. The Guest OS executes the privileged instruction.
    2. The physical CPU sees a User Mode program trying to do kernel work and **throws a hardware fault (trap)**.
    3. The CPU context-switches to the Host OS (Ring 0).
    4. The Host OS context-switches to the VM software (e.g., VirtualBox) running in User Mode (Ring 3).
    5. The VM software analyzes the fault, realizes the Guest OS was just trying to update its page tables, and **emulates** the result in software memory.
    6. The CPU context-switches *back* to the Host OS (Ring 0).
    7. The CPU context-switches *back* to the Guest OS (Ring 3) to resume execution.

    This violent chain of context switches happens **thousands of times per second**. It absolutely shreds CPU performance and destroys cache locality.

    ### The KVM Elegance (Hardware-Assisted)

    Because KVM uses the CPU's VMX extensions to give the Guest OS a true (but sandboxed) Ring 0:

    1. The Guest OS executes the exact same privileged instruction to update its page tables.
    2. The physical CPU sees the Guest OS is in the Non-Root Ring 0, realizes this instruction only affects the VM's isolated sandbox, and **executes it natively in the silicon**.

    **Zero faults. Zero context switches. Zero emulation.** KVM only steps in (via VM-Exit) for the absolute bare minimum of operations—specifically, when the Guest OS tries to touch shared physical hardware, like sending a packet out of the physical network card or writing to the physical SSD.

    By eliminating the massive overhead of software exceptions for internal kernel operations, KVM allows the virtual machine to run at what is commonly called **near bare-metal performance**.

??? problem "Why VM?"

    - Honey pot
    - Trying out different OS
    

### Docker

- Docker is not a VM, it is a container.

- Docker is faster than VM, because it can do system calls directly to the kernel.

=== "bash"
    ```bash
    docker run -it ubuntu uname -r
    ```

> This returns the host's kernel name


## Full virtualization

- VMware : Runs in user mode
- KVM : Hardware support

## Para-virtualization

- Xen

## JVM

Consists of

- Class loader
- Class verifier
- Runtime interpreter
- JIT compilers
