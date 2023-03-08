#include "lists.h"

/**
 * insert_node - insert node with a given number in a sorted singly linked list
 * @head: pointer to the head pointer of the list
 * @number: the number to insert in the new node
 * Return: pointer to the newly added node, or NULL if the operation failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *new;

	for (prev = *head; number > (*head)->n; *head = (*head)->next)
		prev = *head;

	new = malloc(sizeof(**head));
	if (new == NULL)
		return (NULL);

	new->next = *head;
	new->n = number;
	prev->next = new;

	return (new);
}
