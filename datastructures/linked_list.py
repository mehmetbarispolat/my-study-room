class Node:
    def __init__(self, item: int | str = None, next_=None) -> None:
        self.item = item
        self.next = next_

    def __str__(self) -> str:
        return f"{self.item}"


class LinkedList:
    def __init__(self, head: Node) -> None:
        self.head = head

    def get_tree(self) -> str:
        node: Node = self.head
        res = ""
        while node:
            res += f"{node} -> "
            node = node.next
        return res


# def add(value: int, next_id: int):  # |5||-> |3|| ->
# if
# return {"value": value, "next": None}


def main():
    node2 = Node(3, None)
    node1 = Node(5, node2)
    tree = LinkedList(head=node1).get_tree()
    print(tree)


if __name__ == "__main__":
    # we have a list for storing linked lists. linked_lists belongs to dict of key value pair
    # linked_lists = [{"value": 5, "next": 1}]
    main()
