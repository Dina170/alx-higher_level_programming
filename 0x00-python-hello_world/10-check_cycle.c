#include "lists.h"
#include <stdio.h>

/**
  * check_cycle - Checks if a singly linked list has a cycle in it
  * @list: The singly linked list to check
  *
  * Return: 1 if has a cycle in it or 0 if not
  */
int check_cycle(listint_t *list)
{
	while (list < list->next)
	{
		/* The address of the head gradually increases */
		list = list->next;
	}
	/* if the address is smaller then we are back in the cycle */
	if (list)
		return (1);
	else
		return (0);
}
