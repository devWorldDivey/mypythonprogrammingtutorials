class Node:
    def __init__(self, value):
        self.right = None
        self.data = value
        self.left = None


class Tree:
    def createNode(self, data):
        return Node(data)

    def insertNode(self, node, data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insertNode(node.left, data)
        else:
            node.right = self.insertNode(node.right, data)
        return node

    def traverseinorder(self,root):
        if root is not None:
            self.traverseinorder(root.left)
            print(root.data)
            self.traverseinorder(root.right)

tree = Tree()
root = tree.createNode(5)
tree.insertNode(root,2)
tree.insertNode(root,10)
tree.insertNode(root,7)
tree.insertNode(root,15)
tree.insertNode(root,12)
tree.insertNode(root,20)
tree.insertNode(root,30)
tree.insertNode(root,6)
tree.insertNode(root,8)
print(root.data,"-->",root.left.data,"--->",root.left.data)
print("-----> InOrder Traversal")
tree.traverseinorder(root)
