class Node:
    def __init__(self, g, f, position, father = None):
        self.g = g
        self.f = f
        self.position = position
        self.father = father
    
    def get_father(self):
        return self.father
    
    def get_position(self):
        return self.position
    
    def __eq__(self, obj):
        return self.position == obj.position