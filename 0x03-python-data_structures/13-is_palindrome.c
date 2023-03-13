#include "lists.h"

/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: pointer to the head pointer of the list to check
 * Return: 1 if the list is palindromic, 0 if it isn't
 */

int is_palindrome(listint_t **head)
{
	listint_t *iter;
	int i, j, counter, midpoint;

	if ((*head)->next == NULL)
		return (0);
	if (*head == NULL)
		return (1);

	iter = *head;
	for (counter = 1; iter->next != NULL; counter++)
		iter = iter->next;

	midpoint = counter / 2;
	counter -= 2;

	for (i = 0; i < midpoint; i++)
	{
		if ((*head)->n != iter->n)
			return (0);
		for (iter = *head, j = 0; j < counter; j++)
			iter = iter->next;
		counter -= 2;
		*head = (*head)->next;
	}
	return (1);
}
