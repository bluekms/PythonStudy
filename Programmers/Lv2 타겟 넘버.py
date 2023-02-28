class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.left is None:
            self.left = Node(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.left.insert(data)
    def PreOrder(self):
        traverse = []
        if self.data != "":
            traverse.append(self.data)
        if self.left:
            traverse += self.left.PreOrder()
        if self.right:
            traverse += self.right.PreOrder()
        return traverse

def solution(numbers, target):
    root = Node("")
    for i in range(6):
        if i % 2 == 0:
            root.insert("+")
        else:
            root.insert("-")
    print(root.PreOrder())
    answer = 0
    return answer

print(solution([1, 1, 1, 1, 1], 3))
#print(solution([4, 1, 2, 1], 4))
#print(solution())

"""
"""