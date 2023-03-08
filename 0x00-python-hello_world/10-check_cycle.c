#include "lists.h"

/**
 * check_cycle - check if a linked list is circular or not
 * @list: pointer to the head node of the list
 * Return: 1, if the list is circular, or 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *first_node;

	first_node = list;

	if (first_node == NULL)
		return (0);
	while (1)
	{
		if (list->next == first_node)
			return (1);
		else if (list->next == NULL)
			return (0);
		list = list->next;
	}
}
