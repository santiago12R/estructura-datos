class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


myNode = Node(10)
print("The data in the node is:", myNode.data)
print("The next attribute in the node is:", myNode.next)