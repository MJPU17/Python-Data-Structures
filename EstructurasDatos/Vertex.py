class Vertex:

    def __init__(self, number=None, weigth=None):
        self.number = number
        self.weigth = weigth

    def __eq__(self, other):
        if isinstance(other,Vertex):
            return self.weigth==other.weigth
        return False

    def __ge__(self, other):
        if isinstance(other,Vertex):
            return self.weigth>=other.weigth
        return NotImplemented

    def __le__(self, other):
        if isinstance(other,Vertex):
            return self.weigth<=other.weigth
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other,Vertex):
            return self.weigth>other.weigth
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other,Vertex):
            return self.weigth<other.weigth
        return NotImplemented

