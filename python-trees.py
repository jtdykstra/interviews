class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

# constructing the tree (bottom up)
'''
       0
      / \
     1   2
    / \ / \
   3  4 5  6
'''
six = TreeNode(data=6)
five = TreeNode(data=5)
four = TreeNode(data=4)
three = TreeNode(data=3)
two = TreeNode(2, left=five, right=six)
one = TreeNode(1, left=three, right=four)

root = TreeNode(0, left=one, right=two)

# in order
def inorder(node):
    if(node==None):
        return
    # move print to get preorder, post order
    print(node.data)
    inorder(node.left)
    inorder(node.right)
print("inorder")
inorder(root)

# BST (with queue)
import collections

def bst(root):

    visited = {}    
    q = collections.deque()
    q.append(root)

    while(len(q) != 0):
        n = q.popleft()

        if (n != None and visited.get(n, False) == False):
            print(n.data)
            q.append(n.left)
            q.append(n.right)
            visited[n] = True
print("bst")
bst(root)

def dfs(root):
    visited = {}
    s = [] # stack

    s.append(root)

    while(len(s) != 0):
        n = s.pop()

        if (n != None and visited.get(n, False) != True):
            print(n.data)
            s.append(n.left)
            s.append(n.right)
            visited[n] = True
print("dfs")
dfs(root)