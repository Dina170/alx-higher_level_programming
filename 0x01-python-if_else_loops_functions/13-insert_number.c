#include "lists.h"
#include <stdlib.h>

/**
  * insert_node - Inserts a number into a sorted singly linked list
  * @head: The head of the sorted singly linked list
  * @number: The number to inserts in the singly linked list
  *
  * Return: The singly linked list with the new number added
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *current = NULL;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	if (!*head || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (*head);
	}
	else
	{
		current = *head;
		while (current->next && current->next->n < new_node->n)
			current = current->next;

		new_node->next = current->next;
		current->next = new_node;
		return (*head);
	}
}
