class DoublyLinked:
    class Node:
        __slots__ = 'element', 'next', 'previous'

        def __init__(self, _element=None, _next=None, _previous=None):
            self.element = _element
            self.next = _next
            self.previous = _previous

    def __init__(self, element):
        self._head = self.Node(element, None, None)
        self._tail = self.Node(element, None, None)
        self.size = 0

    def insert_first(self, element):
        if self.size == 0:
            new = self.Node(element, None, None)
            self._tail = self._head
        self.size += 1
        new = self.Node(element, self._head, None)
        self._head.previous = new
        self._head = new
        return new

    def insert_last(self, element):
        if self.size == 0:
            new = self.Node(element, None, None)
        self.size += 1
        new = self.Node(element, None, self._tail)
        self._tail.next = new
        self._tail = new

    def delete_first(self):
        if self.size == 0:
            print("Лист пуст")
        value = self._head.element
        if self.size == 1:
            self._head = None
            self.tail = None
        else:
            self._head = self._head.next
            self._head.previous = None
        self.size -= 1
        return value

    def delete_last(self):
        if self.size == 0:
            print("Лист пуст")
        value = self._tail.element
        if self.size == 1:
            self._head = None
            self.tail = None
        else:
            self._tail = self._tail.previous
            self._tail.next = None
        self.size -= 1
        return value

    def get_size(self):
        return self.size

    def print_all(self):
        if self.get_size() == 0:
            print("Лист пуст")
        buf = self._head
        while (buf != None):
            print(buf.element)
            buf = buf.next

    def delete_all(self):
        while self.get_size() != 0:
            self.delete_first


if __name__ == "__main__":
    dll = DoublyLinked("Privet")
    dll.insert_first("Bimba")
    dll.insert_last("Bombita!")
    dll.insert_first("Belissimo!")
    dll.print_all()
