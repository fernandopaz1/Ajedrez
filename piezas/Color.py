class Color:
    def __init__(self, color):
        self.__color = color
    
    @property
    def color(self):
        return self.__color
    
    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.color() == other.color()
    
    def __hash__(self):
        return hash(self.color())