class Node:
    def __init__(self, info=None, next=None):
        self.info=info
        self.next=next

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.info == other.info
        return False
