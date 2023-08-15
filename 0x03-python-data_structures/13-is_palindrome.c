#include <stddef.h>
#include "lists.h"

/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to the head of the linked list.
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 * Return: 0 if not a palindrome, 1 if a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/* Find the middle of the list */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	/* Reverse the second half of the list */
	second_half = reverse_list(slow);
	slow = *head;

	/* Compare the first half with the reversed second half */
	while (second_half != NULL)
	{
		if (second_half->n != slow->n)
		{
			is_palindrome = 0;
			break;
		}
		second_half = second_half->next;
		slow = slow->next;
	}

	/* Restore the original second half */
	reverse_list(second_half);

	return (is_palindrome);
}
