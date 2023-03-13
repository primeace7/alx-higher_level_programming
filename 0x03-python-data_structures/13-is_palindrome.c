#include "lists.h"

/**
 * list_index - get the data at an index of a linked list
 * @list: pointer to the first node in the list
 * @n: the index to get
 * Return: the data at index n
 */

int list_index(listint_t *list, int n)
{
	int i;
	if (n = 0)
		return (list->n);
	for (i = 0; i < n; i++)
		list = list->next;
	return (list->n);
}

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
	list = *head;

	for (i = 0; i < midpoint; i++)
	{
		if (list != list_index(*head, list_len - i -1))
			return (0);
		list = list->next;
	}
	return (1);
}
