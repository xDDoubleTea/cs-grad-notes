# Applications OS interface

## System calls

- Request OS services

!!! example 
    
    - Process control
    - File management
    - Device management
    - Information maintenance
    - Communications

- OS interface to run a program
- Request to kernel made via **Software interrupt**


!!! example "Print hello world to stdout using System call in linux"

    ```cpp
    #include <syscall.h>
    #include <unistd.h>

    int main() {
        syscall(SYS_write, 1, "hello world\n", 12);
        // Or do
        // write(STDOUT_FILENO, "hello world\n", 12);
        return 0;
    }
    ```

### Passing parameters


!!! example "Methods"
    - Pass parameters in registers

    ??? example "Print hello world using system call in x86 NASM"
        ```asm

        # Code Listing 2.3:
        # An assembly-language “hello world” program with system calls

        .global _start	

        .text
        _start:
        # write(1, message, 13)

        # write to stdout
        mov $1, %rax                # system call 1 is write
        mov $1, %rdi                # file handle 1 is stdout


        # write message
        mov $message, %rsi          # address of string to output

        # the length of the message
        mov $13, %rdx               # number of bytes

        # do the system call
        syscall                     # invoke OS to write to stdout
        # the OS checks the values in the registers and decides what to do
        # -> pass parameters in registers


        # exit(0)
        mov $60, %rax               # system call 60 is exit
        xor %rdi, %rdi              # we want return code 0
        syscall                     # invoke OS to exit

        .data
        message:
        .ascii "Hello, world\n"

        ```

    - Store parameters in a table in memory
    - Push parameters onto the stack of the program, then OS will pop them of


## API


- Users program against API instead of system call
- Maybe won't do system calls

!!! example

    - C library
    - Java API for JVM
    - POSIX API
    - Win32 API for windows



