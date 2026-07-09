#include <stdio.h>
#include <unistd.h>

void main() {
  int pid = fork();
  if (pid == 0)
    printf("Child pid = %d\n", pid);
  else
    printf("Parent pid = %d\n", pid);
  return;
}
