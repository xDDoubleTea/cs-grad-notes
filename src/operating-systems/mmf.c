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
