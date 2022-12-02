class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return '(' + str(self.data) + ')'


class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def find(self, data):
        tmp_node = self.root
        while tmp_node is not None:
            if tmp_node.data == data:
                return '(' + str(data) + ')'
            else:
                tmp_node = tmp_node.next
        return "Not Found"

    def remove(self, data):
        tmp_node = self.root
        prev_node = None
        while tmp_node is not None:
            if tmp_node.data == data:
                if prev_node is not None:
                    prev_node.next = tmp_node.next
                else:
                    self.root = tmp_node.next
                self.size -= 1
                return True
            else:
                prev_node = tmp_node
                tmp_node = tmp_node.next
        return False

    def print(self):
        tmp_node = self.root
        while tmp_node is not None:
            print(tmp_node, end="->")
            tmp_node = tmp_node.next
        print("None")


if __name__ == '__main__':

    linked_list = LinkedList()
    for i in "987654321123456789":
        linked_list.add(int(i))

    linked_list.print()
    linked_list.remove(1)
    linked_list.print()
    print(linked_list.find(1))
