class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if self.value:
            if value < self.value or value == self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)


def inorder(root, res):
    if root:
        inorder(root.left, res)
        res.append(root.value)
        inorder(root.right, res)


def tree_sort(arr):
    if len(arr) == 0:
        return arr
    root = Node(arr[0])
    for i in range(1, len(arr)):
        root.insert(arr[i])
    res = []
    inorder(root, res)
    return res


if __name__ == '__main__':
    print(tree_sort([1, 2.6, 9, 8, 8, 10, 5, 7, 0.1]))
