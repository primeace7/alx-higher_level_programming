#include "lists.h"

/**
 * insert_node - insert node with a given number in a sorted singly linked list
 * @head: pointer to the head pointer of the list
 * @number: the number to insert in the new node
 * Return: pointer to the newly added node, or NULL if the operation failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *new, *iter;
	int counter;

	iter = *head;
	prev = iter;

	for (counter = 0; iter != NULL && number > iter->n; counter++)
	{
		prev = iter;
		iter = iter->next;
	}

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->next = iter;
	new->n = number;
	if (counter == 0)
		*head = new;
	else
		prev->next = new;

	return (new);
}
