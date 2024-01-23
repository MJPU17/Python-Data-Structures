
class GTNode:

    def __init__(self, key=None, childs=None):
        self.key=key
        self.childs=childs

    def __eq__(self, other):
        if isinstance(other,GTNode):
            return self.key==other.key
        return False