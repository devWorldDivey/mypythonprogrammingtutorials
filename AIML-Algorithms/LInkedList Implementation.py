class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def removeduplicates(self):
        if self.length > 0:
            temp = self.head
            while temp.next:
                if temp.value == temp.next.value:
                    temp.next = temp.next.next
                    self.length -=1
                else:
                    temp = temp.next



mylist = LinkedList(1)
mylist.append(2)
mylist.append(2)
mylist.append(3)
mylist.append(3)
mylist.append(4)


mylist.printlist()
mylist.removeduplicates()
print("-----------------------After-----------------------")
mylist.printlist()
print(mylist.length)