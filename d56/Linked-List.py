class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def insert_node(self, position, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
            return
        elif position == 1:
            tmp = self.head
            self.head = node
            self.head.next = tmp
        else:
            header = self.head
            i = 2
            while i < position:
                header = header.next
                i += 1
            tmp = header.next
            header.next = node
            node.next = tmp
        # @param position, an integer
        # @param value, an integer

    def delete_node(self, position):
        header = self.head

        if position == 1:
            if self.head is not None:
                self.head = self.head.next
        else:
            i = 2
            while i < position and header is not None:
                header = header.next
                i += 1
            if header is not None and header.next is not None:
                header.next = header.next.next
        # @param position, integer
        # @return an integer

    def print_ll(self):
        # Output each element followed by a space
        header = self.head
        while header is not None:
            if header.next is None:
                print(header.val)
            else:
                print(header.val, end=" ")

            header = header.next


ll = LinkedList()


def insert_node(position, value):
    ll.insert_node(position, value)


def delete_node(position):
    ll.delete_node(position)


def print_ll():
    ll.print_ll()


# if __name__ == "__main__":
#     insert_node(1, 2)
#     insert_node(2, 3)
#     insert_node(3, 4)
#     insert_node(4, 5)
#     print_ll()
#     delete_node(3)
#     print_ll()
