class Treenode:
    def __init__(self,value):
        self.right = None
        self.data = value
        self.left = None

class TreeDS:
    def createnode(self,data):
        return Treenode(data)
    def insert(self,node,data):
        if node is None:
            return self.createnode(data)
        if data < node.data:
            node.left = self.insert()