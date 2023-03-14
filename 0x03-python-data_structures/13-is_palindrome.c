#include "lists.h"

/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: pointer to the head pointer of the list to check
 * Return: 1 if the list is palindromic, 0 if it isn't
 */

int is_palindrome(listint_t **head)
{
	listint_t *list;
	int i, list_len, midpoint, counter, first, last;

	list = *head;

	if (list == NULL || list->next == NULL)
		return (1);
	for (list_len = 1; list->next != NULL; list_len++)
		list = list->next;

	midpoint = list_len / 2;
	list_len -= 1;
	list = *head;

	for (i = 0; i < midpoint; i++)
	{
		for (list = *head, counter = 0; counter < i; counter++)
			list = list->next;
		first = list->n;

		for (list = *head, counter = 0; counter < list_len - i; counter++)
			list = list->next;
		last = list->n;

		if (first != last)
			return (0);
	}
	return (1);
}
