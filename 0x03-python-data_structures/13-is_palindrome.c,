#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *temp = *head;
    int array[2048];
    int i = 0;
    int start = 0;
    int end;

    if (head == NULL || *head == NULL)
        return (1);

    while (temp != NULL)
    {
        array[i] = temp->n;
        temp = temp->next;
        i++;
    }

    end = i - 1;

    while (start < end)
    {
        if (array[start] != array[end])
            return (0);
        start++;
        end--;
    }

    return (1);
}
