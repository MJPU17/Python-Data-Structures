class MNode:

    def __init__(self, key=None, info=None, next=None):
        self.key = key
        self.info = info
        self.next = next

    def __eq__(self, other):
        if isinstance(other, MNode):
            return self.key==other.key and self.info==other.info
        return False

