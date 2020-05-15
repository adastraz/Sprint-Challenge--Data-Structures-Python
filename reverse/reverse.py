class Node:
    def __init__(self, value=None, next_node=None, prev=None):
        self.value = value
        self.next_node = next_node
        self.prev = prev

    def get_value(self):
        return self.value

    def get_next(self):
        # return self.prev
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def set_prev(self, prev):
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)
            self.head.set_prev(node)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # if not node.next: 
        #     self.head = node
        #     node.set_next('end')
        #     print(node)
        #     self.reverse_list(node.prev)
        # if node.prev:
        #     print(node)
        #     self.reverse_list(node.prev)
        # else:
        #     print(node)
        head = self.head
        prev = None
        while head is not None:
            next_node = head.next_node
            head.next_node = prev
            prev = head
            head = next_node
        self.head = prev

