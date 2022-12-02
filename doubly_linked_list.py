class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return '(' + str(self.data) + ')'


class DoublyLinkedList:
    def __init__(self, data=None):
        self.root = data
        self.last = data
        self.size = 0

    def add(self, data):
        if self.size == 0:
            self.root = Node(data)
            self.last = self.root
        else:
            new_node = Node(data, self.root)
            self.root.prev = new_node
            self.root = new_node
        self.size += 1

    def find(self, data):
        tmp_node = self.root
        while tmp_node.next is not None:
            if tmp_node.data == data:
                return tmp_node
            elif tmp_node.next is None:
                return False
            # else:
            tmp_node = tmp_node.next

    def remove(self, data):
        tmp_node = self.root
        while tmp_node.next is not None:
            if tmp_node.data == data:
                if tmp_node.prev is not None:
                    if tmp_node.next is not None:  # delete node from middle
                        tmp_node.prev.next = tmp_node.next
                        tmp_node.next.prev = tmp_node.prev
                    else:  # delete node at the end
                        tmp_node.prev.next = None
                        self.last = tmp_node.prev
                else:  # delete root node
                    self.root = tmp_node.next
                    tmp_node.next.prev = self.root
                self.size -= 1
                return True
            else:
                tmp_node = tmp_node.next
        return False

    def print(self):
        if self.root is None:
            return "Empty"
        tmp_node = self.root
        while True:
            print(tmp_node, end="->")
            if tmp_node.next is None:
                break
            tmp_node = tmp_node.next
        # print(tmp_node, end="->")
        # while tmp_node is not None:
        #     tmp_node = tmp_node.next
        #     print(tmp_node, end="->")
        print()


if __name__ == '__main__':

    linked_list = DoublyLinkedList()
    for i in "987654321" + "0987654321"[-1:0:-1]:
        # for i in "987654321123456789":
        linked_list.add(int(i))

    linked_list.print()
    print(linked_list.remove(1))
    linked_list.print()
    print(linked_list.find(1))
    print(linked_list.find(10))
    print(linked_list.last.prev.prev)
