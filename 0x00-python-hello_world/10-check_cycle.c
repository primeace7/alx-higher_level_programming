#include "lists.h"

/**
 * check_cycle - check if a linked list is circular or not
 * @list: pointer to the head node of the list
 * Return: 1, if the list has a cycle, or 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *head, *iter;

	head = list;

	if (list == NULL)
		return (0);
	while (1)
	{
		iter = head;
		while (iter != list)
		{
			if (list->next == iter)
				return (1);
			iter = iter->next;
		}
		list = list->next;
		if (list->next == NULL)
			return (0);
	}
}
