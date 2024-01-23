class DNode:

    def __init__(self, info=None, previous=None, next=None):
        self.info=info
        self.previous=previous
        self.next=next

    def __eq__(self, other):
        if isinstance(other,DNode):
            return self.info==other.info
        return False
