#include "lists.h"

/**
 * check_list - iterate through a list and check for a cycle
 * @head: pointer to the first node in the list
 * @list: pointer to the current node in the list
 * @i: the index in the list where @list currently points to
 * Return: 1 if the list has a cycle, 0 otherwise
 */

int check_list(listint_t *head, listint_t *list, int i)
{
	listint_t *current_node;
	int counter;

	current_node = head;

	for (counter = 0; counter < i; counter++)
	{
		if (current_node == list)
			return (1);
		current_node = current_node->next;
	}
	return (0);
}

/**
 * check_cycle - check if a linked list is circular or not
 * @list: pointer to the head node of the list
 * Return: 1, if the list has a cycle, or 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *head;
	int i = 0;

	head = list;

	if (list == NULL)
		return (0);
	while (1)
	{
		if (list->next == NULL)
			return (0);
		else if (list->next == list)
			return (1);
		list = list->next;
		i++;

		if (check_list(head, list, i))
			return (1);
	}
}
