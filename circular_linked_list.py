class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return '(' + str(self.data) + ')'


class CircularLinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, data):
        if self.size == 0:
            self.root = Node(data)
            self.root.next = self.root
        else:
            new_node = Node(data, self.root.next)
            self.root.next = new_node
        self.size += 1

    def find(self, data):
        tmp_node = self.root
        while True:
            if tmp_node.data == data:
                return '(' + str(data) + ')'
            elif tmp_node.next == self.root:
                return False
            tmp_node = tmp_node.next

    def remove(self, data):
        tmp_node = self.root
        prev_node = None
        while True:
            if tmp_node.data == data:
                if prev_node is not None:
                    prev_node.next = tmp_node.next
                else:
                    while tmp_node.next != self.root:
                        tmp_node = tmp_node.next
                    tmp_node.next = self.root.next
                self.size -= 1
                return True
            elif tmp_node.next == self.root:
                return False
            prev_node = tmp_node
            tmp_node = tmp_node.next

    def print(self):
        if self.root is None:
            return "Empty"
        tmp_node = self.root
        while True:
            print(tmp_node, end="->")
            if tmp_node.next == self.root:
                break
            tmp_node = tmp_node.next
        print()


if __name__ == '__main__':

    linked_list = CircularLinkedList()
    for i in "987654321" + "0987654321"[-1:0:-1]:
        # for i in "987654321123456789":
        linked_list.add(int(i))

    linked_list.print()
    print(linked_list.remove(1))
    linked_list.print()
    print(linked_list.find(1))
