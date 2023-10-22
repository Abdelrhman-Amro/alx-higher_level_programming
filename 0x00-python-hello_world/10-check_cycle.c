#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: head of the list
 * Return: 0 OR 1
*/
int check_cycle(listint_t *list)
{
	listint_t *tail = list;

	if (!list)
		return (0);

	tail = list->next;
	while (tail != list)
	{
		if (!tail)
			return (0);
		tail = tail->next;
	}
	return (1);
}
