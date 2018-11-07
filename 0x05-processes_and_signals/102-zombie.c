#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * main - zombies
 *
 * Description: make five zombies
 * Return: 0 for success
 */
int main(void)
{
	int i;
	pid_t pidme;

	i = 0;
	while (i < 5)
	{
		pidme = fork();
		if (pidme)
			printf("Zombie process created, PID: %i\n", pidme);
		else
			exit(0);
		i++;
	}
	sleep(100);
	return (0);
}
