#include "lists.h"

/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: pointer to the head pointer of the list to check
 * Return: 1 if the list is palindromic, 0 if it isn't
 */

int is_palindrome(listint_t **head)
{
	listint_t *list;
	int i, list_len, midpoint;

	list = *head;
	for (list_len = 1; list->next != NULL; list_len++)
		list = list->next;

	midpoint = list_len / 2;
	--list_len;
	list = *head;

	for (i = 0; i < midpoint; i++)
	{
		if ((list - i)->n != (list - list_len + i)->n)
			return (0);
	}
	return (1);
}
