class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.val = key

    def inoder_traversal(node):
        if node:
            inoder_traversal(node.left)
            print("(" + str(node.val) + ")", end = " ")
            inoder_traversal(node.rights)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inoder TRaversal:")
    inoder_traversal(root)