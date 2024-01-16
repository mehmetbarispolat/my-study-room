from .linked_list import LinkedList, Node


class Stack:
    def __init__(self) -> None:
        self._top = Node()

    def push(self, item):
        next_ = self._top
        self._top = Node(item, next_)
        self._top.next = next_
        return self

    def preview(self) -> str:
        return LinkedList(self._top).get_tree()


if __name__ == "__main__":
    stack = Stack().push(5).push(10).push(15).preview()
    print(stack)
