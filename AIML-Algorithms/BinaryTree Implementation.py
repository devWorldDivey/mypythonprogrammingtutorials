class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    def BFS(self):
        current_node = self.root
        queue = []
        result = []
        queue.append(current_node)
        while len(queue)>0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return result

my_tree = BST()
my_tree.insert(47)
my_tree.insert(26)
my_tree.insert(51)
my_tree.insert(18)
my_tree.insert(23)
my_tree.insert(29)
my_tree.insert(53)
print(my_tree.BFS())