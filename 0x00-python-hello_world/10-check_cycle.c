#include "lists.h"

/**
 * check_cycle - check if a linked list is circular or not
 * @list: pointer to the head node of the list
 * Return: 1, if the list has a cycle, or 0 otherwise
 */

int check_cycle(listint_t *list)
{

	if (list == NULL)
		return (0);
	while (1)
	{
		if (list->next >= list)
			return (1);
		else if (list->next == NULL)
			return (0);
		list = list->next;
	}
}
