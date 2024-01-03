#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list) {
    listint_t *slow, *fast;

    if (list == NULL || list->next == NULL) {
        return 0;  /* No cycle if the list is empty or has only one node */
    }

    slow = list;
    fast = list->next;

    while (fast != NULL && fast->next != NULL) {
        if (slow == fast) {
            return 1;  /* Cycle detected */
        }
        slow = slow->next;
        fast = fast->next->next;
    }

    return 0;  /* No cycle */
}
