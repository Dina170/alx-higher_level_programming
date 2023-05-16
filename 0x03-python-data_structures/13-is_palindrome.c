#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * reverseList - reverse linked list
 * @ptr: pointer to the first node in list
 *
 * Return: previous pointer
 */
listint_t *reverseList(listint_t *ptr)
{
	listint_t *prev = NULL;

	while (ptr)
	{
		listint_t *next = ptr->next;

		ptr->next = prev;
		prev = ptr;
		ptr = next;
	}
	return (prev);
}
/**
 * is_palindrome - checks if linked list is palindrome or not
 * @head: pointer to pointer to head
 *
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head, *temp = *head;

	if (head == NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	slow->next = reverseList(slow->next);
	slow = slow->next;
	while (slow)
	{
		if (temp->n != slow->n)
			return (0);
		temp = temp->next;
		slow = slow->next;
	}
	return (1);
}
