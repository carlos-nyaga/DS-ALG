"""
Linked List :
    --> Has nodes:
        Each Node has:
            [+] Data
                --> The actual data the node holds
            [+] Next
                --> A reference to the next node
                    --> Moves left to right
                    --> Is null if is last node
    --> Head:
        --> Reference to the 1st node
        --> Is null if Linked List is empty
"""




class Node:
    data = ''
    next = None
    def __init__(self, data):
        self.data = data





class LinkedList:
    head = None

    def is_empty(self):
        return self.head is None

    def insert_first(self, new_node_data):
        new_node = Node(new_node_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, pred_node_data, new_node_data):
        pred = self.head
        while pred is not None and pred.data != pred_node_data:
            pred = pred.next

        if pred:
            new_node = Node(new_node_data)
            new_node.next = pred.next
            pred.next = new_node
        else:
            raise IndexError(f"Fail: the node {pred_node_data} is no found")

    def insert_last(self, new_node_data):
        if self.is_empty():
            self.head = Node(new_node_data)
            return
        pred = self.head
        while pred.next is not None:
            pred = pred.next
        pred.next = Node(new_node_data)


    def delete_first_occurrence(self, delete_node_data):
        if self.is_empty():
            raise ValueError("list is empty")

        pred = self.head
        if pred.data == delete_node_data:
            self.head = self.head.next
            return pred

        while pred is not None and pred.next and  pred.next.data != delete_node_data:
            pred = pred.next
        if pred:
            temp = pred.next
            if temp:
                pred.next = temp.next
                return temp
            else:
                raise IndexError(f"Fail: the node {delete_node_data} is no found")
        else:
            raise IndexError(f"Fail: the node {delete_node_data} is no found")


    def delete_first(self):
        if self.is_empty():
            raise IndexError("list is empty")
        temp = self.head
        self.head = self.head.next
        return temp


    def delete_last(self):
        if self.is_empty():
            raise IndexError("list is empty")
            return None

        pred = self.head
        if pred.next is None:
            self.head = None
            return pred

        while pred is not None and pred.next.next is not None:
            pred = pred.next

        temp = pred.next
        pred.next =  None
        return temp


    def __len__(self):
        count = 0
        for _ in self:
            count += 1
        return count

    def __node_iter(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __iter__(self):
        """:returns values iterator"""
        return iter(map(lambda node: node.data, self.__node_iter()))
