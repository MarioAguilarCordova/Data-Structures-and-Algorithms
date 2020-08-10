class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
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
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_beginning(data)

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        # search for first occurrence of data_after value in linked list
        # Now insert data to insert after data_after node

        if self.head is None:
            print("There is no ", data_after, "to insert after")

        itr = self.head

        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            if itr.data == data_after and itr.next is None:
                self.insert_at_end(data_to_insert)

            itr = itr.next

    def remove_by_value(self, data):
        # Remove first node that contains data

        if self.head is None:
            print("There is nothing to remove")

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


def main():
    ll = LinkedList()
    '''ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.print()
    ll.insert_at_end(7)
    ll.insert_at_end(79)
    '''
    ll.insert_values(['banana', 'mango', 'grapes', 'orange'])
    # print("Length: ", ll.get_length())
    # ll.remove_at(2)
    # ll.remove_at(-1)
    # ll.insert_at(0, 'apples')
    # ll.insert_at(2, 'figs')
    # ll.insert_after_value('orange', 'apples')
    # ll.insert_after_value('banana', 'figs')
    # ll.insert_after_value('mango', 'cherries')
    ll.remove_by_value('mango')
    ll.print()


main()
