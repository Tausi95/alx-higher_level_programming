#include "lists.h"
/**
* insert_node - Inserts a number into a sorted singly linked list.
* @head: A pointer to the pointer to the head of the linked list.
* @number: The number to be inserted.
*
* Return: The address of the new node, or NULL if it failed.
*
* This function inserts a new node with the specified number into a sorted
* singly linked list while maintaining the ascending order of elements.
* If the linked list is empty or the new number is smaller than the first
* node's value, the new node is inserted at the beginning of the list.
* Otherwise, the function iterates through the list to find the appropriate
* position for the new node.
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_node;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		current = *head;

		while (current->next != NULL && current->next->n < number)
		{
			current = current->next;
		}
		new_node->next = current->next;
		current->next = new_node;
	}
	return (new_node);
}
