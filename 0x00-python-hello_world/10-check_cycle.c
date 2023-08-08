#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/* Function to check if a singly linked list has a cycle */
int check_cycle(listint_t *list)
{
	listint_t *pointer1 = list;
	listint_t *pointer2 = list;

	while (pointer2 != NULL && pointer2->next != NULL)
	{
		pointer1 = pointer1->next;
		pointer2 = pointer2->next->next;

		/* If pointer2 catches pointer1, there is a cycle */
		if (pointer1 == pointer2)
		{
			return (1);
		}
	}

	/* If the loop exits, there is no cycle */
	return (0);
}
