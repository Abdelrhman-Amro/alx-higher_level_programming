#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: head of the list
 * Return: 0 OR 1
*/
int check_cycle(listint_t *list)
{
	listint_t *slw = list;
	listint_t *fst = list;

	if (!list)
		return (0);
	while (slw && fst && fst->next)
	{
		slw = slw->next;
		fst = fst->next->next;
		if (slw == fst)
			return (1);
	}
	return (0);
}
