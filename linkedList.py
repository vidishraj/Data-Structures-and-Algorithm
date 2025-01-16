class Node:
    _data: str | int
    _next = None

    def __init__(self, data):
        self._data = data

    def attachNext(self, node):
        self._next = node

    def getNext(self):
        return self._next

    def getData(self):
        return self._data


class LinkedList:
    Start: Node | None

    def initList(self, firstValue):
        newNode = Node(firstValue)
        self.Start = newNode

    def addValue(self, newValue):
        prev = self.Start
        iterator = self.Start
        while iterator is not None:
            prev = iterator
            iterator = self.Start.getNext()
        newNode = Node(newValue)
        prev.attachNext(newNode)

    def getListOfValues(self):
        llList = []
        if self.Start is None:
            return llList
        else:
            iterator = self.Start
            while iterator is not None:
                llList.append(iterator.getData())
                iterator = iterator.getNext()
            return llList



