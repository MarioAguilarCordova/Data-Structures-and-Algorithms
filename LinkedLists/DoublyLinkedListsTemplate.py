class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head, None)
        self.head.prev = node
        self.head = node

    def print(self):
        if self.head is None:
            print("The list is empty")

        itr = self.head
        llstr = ""

        while itr:
            llstr += "<-- " + str(itr.data) + " -->"
            itr = itr.next

        print(llstr)

    def print_forward(self):
        if self.head is None:
            print("The list is empty")

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + " -->"
            itr = itr.next

        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("The list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ""
        while itr:
            llstr += str(itr.data) + " -->"
            itr = itr.prev

        print("Linked List in reverse is: ", llstr)

    def get_last_node(self):
        itr = self.head

        while itr.next:
            itr = itr.next

        return itr

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_values(self, data_list):
        if self.head is None:
            for data in data_list:
                self.insert_at_end(data)
        else:
            for data in data_list:
                self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index <= 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head

        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_beginning(data)

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            print("There is nothing to insert after")

        itr = self.head

        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            if itr.data == data_after and itr.next is None:
                self.insert_at_end(data_to_insert)
                break

            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            print("There is nothing to remove")

        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None

        itr = self.head

        while itr:
            if itr.data == data:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next


def main():
    ll = DoublyLinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0, "jackfruit")
    ll.print_forward()
    ll.insert_at(6, "dates")
    ll.print_forward()
    ll.insert_at(2, "kiwi")
    ll.print()


main()
