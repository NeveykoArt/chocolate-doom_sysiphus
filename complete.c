#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <libgen.h>
#include <sys/types.h>

int main(int argc, char *argv[]) {
    // ДИАГНОСТИКА: показываем ID до setuid
    printf("=== ДО setuid ===\n");
    printf("Real UID: %d\n", getuid());
    printf("Effective UID: %d\n", geteuid());
    printf("Real GID: %d\n", getgid());
    printf("Effective GID: %d\n", getegid());
    
    // Пытаемся повысить привилегии
    if (setuid(0) != 0) {
        perror("setuid(0) failed");
    }
    if (setgid(0) != 0) {
        perror("setgid(0) failed");
    }
    
    // ДИАГНОСТИКА: показываем ID после setuid
    printf("\n=== ПОСЛЕ setuid ===\n");
    printf("Real UID: %d\n", getuid());
    printf("Effective UID: %d\n", geteuid());
    
    // Получаем путь к скрипту
    char path[1024];
    ssize_t len = readlink("/proc/self/exe", path, sizeof(path) - 1);
    
    if (len == -1) {
        perror("readlink");
        return 1;
    }
    
    path[len] = '\0';
    char *dir = dirname(path);
    
    char script_path[1024];
    snprintf(script_path, sizeof(script_path), "%s/script.sh", dir);
    
    printf("\nПуть к скрипту: %s\n", script_path);
    printf("Запускаю скрипт...\n\n");
    
    // Запускаем скрипт
    execl("/bin/bash", "bash", script_path, NULL);
    
    perror("execl");
    return 1;
}
