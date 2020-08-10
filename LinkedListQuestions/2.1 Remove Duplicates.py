class Node:
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def remove_at(self, index):
        if index <= 0 or index >= self.get_length():
            print("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head

        while itr.next:

            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def get_length(self):

        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    def print(self):
        if self.head is None:
            print("The linked list is empty")

        llstr = ""
        itr = self.head

        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next

        print(llstr)

    def insert_values(self, data_list):
        if self.head is not None:
            for data in data_list:
                self.insert_at_end(data)
        else:
            self.head = None
            for data in data_list:
                self.insert_at_end(data)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

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

    def remove_duplicates(self):

        if self.head is None:
            print("There is no duplicates to remove")

        count = 0
        itr = self.head
        temp = 0

        while itr:
            self.print()
            print(temp)
            print(itr.data)
            print(count)
            if temp == itr.data:
                self.remove_at(count)
                count -= 1
            temp = itr.data

            itr = itr.next
            count += 1


# 2.1 Remove Duplicates: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

def main():
    ll = LinkedList()
    ll.insert_values([1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 7, 8, 9, 10])
    ll.remove_duplicates()
    ll.print()


main()

