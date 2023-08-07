#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/* Function to add a new node at the beginning of the list */
listint_t *add_nodeint(listint_t **head, const int n) {
    listint_t *new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return NULL;

    new_node->n = n;
    new_node->next = *head;
    *head = new_node;
    return new_node;
}

/* Function to print the list */
size_t print_listint(const listint_t *h) {
    size_t count = 0;
    while (h != NULL) {
        printf("%d\n", h->n);
        h = h->next;
        count++;
    }
    return count;
}

/* Function to check if a singly linked list has a cycle */
int check_cycle(listint_t *list) {
    listint_t *pointer1 = list;
    listint_t *pointer2 = list;

    while (pointer2 != NULL && pointer2->next != NULL) {
        pointer1 = pointer1->next;
        pointer2 = pointer2->next->next;

        /* If pointer2 catches pointer1, there is a cycle */
        if (pointer1 == pointer2) {
            return 1;
        }
    }

    /* If the loop exits, there is no cycle */
    return 0;
}

/* Function to free the list */
void free_listint(listint_t *head) {
    listint_t *current;
    while (head != NULL) {
        current = head;
        head = head->next;
        free(current);
    }
}
