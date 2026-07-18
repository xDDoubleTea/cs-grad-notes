# Virtual memory

## Why?

- We don't want to load every program directly into memory
- Use hard drive as memory

## Separation of user logical memory

!!! note "Benifits"

    - Run a extremely large process
    - Increase CPU/resources utilization
    - Simplify programming task
    - Run programs faster (less IO)

## Implementation of Virtual memory

- [Demand Paging](./demand-paging)
- Demand segmentation: more complicated due to variable sizes


## Process and Virtual Memory

- Copy-on Write (lazy copy): the parent and the child process share the same frames initially, and frame-copy when a page is written 
- Memory-Mapped File: map a file into the virtual address space to bypass file system calls

### Copy-on-Write

- It's literally lazy copying
- Free frames are allotcated from a pool of zeroed-out frames (怕有人不小心找到別的process的資料然後裡面剛好有機密文件之類的)

### Memory-Mapped Files (MMF)

- Allows file IO to be treaded as *routine memory access* by mapping a disk block to a memory frame
- File is read using demand paging. Subsequent reads/writes from/to the file are treated as ordinary memory access

!!! note "Benifits"

    - Faster file access by using memory access rather than `read()` or `write()` system calls
    - Allows several processes to map the same file allowing the pages in memory to be shared


!!! note

    - 當bound沒算好或是被人更改就炸了
    - Need more programming efforts (checking permissions, checking bounds)
    - Data lost (power cut then everything is wiped in memory)

!!! example "Systems that uses MMF"

    1. GPU rendering
    2. Database Engines
    3. Dynamic shared libraries

    !!! example "如何不用stdio.h寫67到終端機？"

        第一步： `touch data.bin`  
        第二步：跑以下`python`腳本

        ```python
        with open("data.bin", "w") as file:
            file.write("1"*67+"2"*67)
        ```
        第三步：編譯並執行以下`C`程式

        ```C
        #include <fcntl.h>
        #include <sys/mman.h>
        #include <sys/stat.h>
        #include <unistd.h>
        int main() {
          int fd = open("data.bin", O_RDWR);
          struct stat s;
          fstat(fd, &s);
          char *mapped =
              mmap(NULL, s.st_size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);

          int i = 0;
          while (i <= s.st_size) {
            if (mapped[i] == '2')
              break;
            i++;
          }

          char buf[10] = "000000000";

          int ptr = 0;
          while (i > 0) {
            buf[ptr++] = (i % 10) + '0';
            i /= 10;
          }

          int j = 0;
          char tmp;
          int len = ptr;
          ptr--;
          while (ptr >= j) {
            tmp = buf[ptr];
            buf[ptr] = buf[j];
            buf[j] = tmp;
            j++;
            ptr--;
          }
          buf[len] = '\n';
          write(STDOUT_FILENO, buf, len + 1);

          munmap(mapped, s.st_size);
          close(fd);
          return 0;
        }
        ```
        第四步：發現第一跟第二步都是多餘的，`mmf`也是多餘的

