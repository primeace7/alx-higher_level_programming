#include "lists.h"

/**
 * check_cycle - check if a linked list is circular or not
 * @list: pointer to the head node of the list
 * Return: 1, if the list has a cycle, or 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *current_node, *head;
	int counter, i = 0;

	head = list;

	if (list == NULL)
		return (0);
	while (1)
	{
		if (list->next == NULL)
			return (0);
		else if (list->next == list)
			return (1);
		else
		{
			list = list->next;
			i++;
		}

		current_node = head;

		for (counter = 0; counter < i; counter++)
		{
			if (current_node == list)
				return (1);
			current_node = current_node->next;
		}
	}
}
