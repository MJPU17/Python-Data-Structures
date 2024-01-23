class TNode:

    def __init__(self, key=None, left=None, right=None):
        self.key=key
        self.left=left
        self.right=right

    def __eq__(self, other):
        if isinstance(other,TNode):
            return self.key==other.key
        return False

