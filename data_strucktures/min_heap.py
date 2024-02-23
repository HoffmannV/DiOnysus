from data_strucktures.node import Node


class MinHeap:
    def __init__(self, value=None):
        self.root = Node(value)
        self.node = None
        self.count = 0
        self.depth = 0

    def insert(self, value):
        if self.node is None:
            self.node = self.root
        # Exit condition
        if self.node.prev:
            self.node = self.node.prev
            self.insert(value)
        elif self.node.next:
            self.node = self.node.next
            self.insert(value)
        else:
            if self.node.prev is None:
                self.node.prev = Node(value)
                return
            if self.node.next is None:
                self.node.next = Node(value)
                return


    def remove(self, ):
        pass

    def heapify_up(self):
        pass

    def traverse(self):
        pass
