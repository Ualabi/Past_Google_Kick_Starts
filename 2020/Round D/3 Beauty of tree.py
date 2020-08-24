class TreeNode():
    def __init__(self,val):
        self.val = val
        self.sons = []

class Tree():
    def __init__(self):
        self.values = {}
    
    def newTreeNode(self,val,father):
        newnode = TreeNode(val)
        self.values[val] = newnode
        if 0 < father:
            self.values[father].sons.append(newnode)

T = int(input())
for t in range(T):
    N, A, B = map(int,input().split())
    arr = list(map(int,input().split()))
    
    myTree = Tree()
    myTree.newTreeNode(1,-1)
    for x in range(N-1):
        myTree.newTreeNode(x+1,arr[x])
    
    ans = 0
    print('Case #{}: {}'.format(t+1,ans))