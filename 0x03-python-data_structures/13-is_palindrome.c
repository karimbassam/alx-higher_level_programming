#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the first node of listint_t list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev_slow = NULL;
	listint_t *second_half, *mid_node = NULL;
	int palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		/* Reverse the first half of the list */
		listint_t *temp = slow;
		slow = slow->next;
		temp->next = prev_slow;
		prev_slow = temp;
	}

	/* If the list has an odd number of elements, skip the middle one */
	if (fast != NULL)
	{
		mid_node = slow;
		slow = slow->next;
	}

	/* Compare the reversed first half with the second half */
	second_half = slow;
	while (prev_slow != NULL && second_half != NULL)
	{
		if (prev_slow->n != second_half->n)
		{
			palindrome = 0;
			break;
		}

		prev_slow = prev_slow->next;
		second_half = second_half->next;
	}

	/* Restore the reversed first half */
	while (prev_slow != NULL)
	{
		listint_t *temp = prev_slow->next;
		prev_slow->next = mid_node;
		mid_node = prev_slow;
		prev_slow = temp;
	}

	return palindrome;
}
