from typing import *
import sys


class Node:
    val = 0
    next = None

    def __init__(self, val):
        self.val = val


class LL:
    head = None

    def __init__(self):
        self.head = None

    def insert_node(self, position, value):

        header = self.head

        if position < 1:
            return

        if position == 1:
            self.head = Node(value)
            self.head.next = header
            return self.head
        iter_head = self.head
        while iter_head is not None and iter_head.next is not None and position > 2:
            iter_head = iter_head.next
            position -= 1

        if position != 2:
            return

        if iter_head is None:
            return

        tmp = iter_head.next
        iter_head.next = Node(value)
        iter_head.next.next = tmp

        return

    def delete_node(self, position):

        if position < 1:
            return

        if position == 1:
            if self.head is None:
                return None
            header = self.head.next
            self.head = header
            return
        iter_head = self.head
        while iter_head is not None and position > 2:
            iter_head = iter_head.next
            position -= 1

        if iter_head is None or iter_head.next is None:
            return

        iter_head.next = iter_head.next.next
        return
        # @param position, integer
        # @return an integer

    def print_ll(self):
        header = self.head
        while self.head is not None:
            if self.head.next is None:
                print(self.head.val, end="")
            else:
                print(self.head.val, end=" ")
            self.head = self.head.next
        self.head = header
        return
        # Output each element followed by a space


linkedlist = LL()


def insert_node(position, value):
    linkedlist.insert_node(position, value)


def print_ll():
    linkedlist.print_ll()
    print()


def delete_node(position):
    linkedlist.delete_node(position)

#
# print("Hi")
# t = int(input())
#
# while t > 0:
#     arr = sys.stdin.readline().strip().split()
#     if arr[0] == 'i':
#         insert_node(int(arr[1]), int(arr[2]))
#     if arr[0] == 'p':
#         print_ll()
#     if arr[0] == 'd':
#         delete_node(int(arr[1]))
#     t -= 1
