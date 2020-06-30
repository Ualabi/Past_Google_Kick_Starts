class TreeNode():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class BST():
    def __init__(self):
        self.head = None
        
def putIn(val,Tree):
    if Tree.head == None:
        Tree.head = TreeNode(val,BST(),BST())
    elif Tree.head.val < val:
        putIn(val,Tree.head.right)
    else:
        putIn(val,Tree.head.left)

def putOut(val,Tree):
    if Tree.head == None:
        return None
    elif Tree.head.val == val:
        if Tree.head.left.head:
            rightTree = Tree.head.right
            Tree.head = Tree.head.left.head
            if rightTree.head:
                insertTree(Tree,rightTree)
        elif Tree.head.right.head:
            Tree.head = Tree.head.right.head
        else:
            Tree.head = None
    elif Tree.head.val < val:
        aux = putOut(val,Tree.head.right)
    else:
        aux = putOut(val,Tree.head.left)

def insertTree(Tree,auxTree):
    if Tree.head == None:
        Tree.head = auxTree.head
    elif Tree.head.val < auxTree.head.val:
        insertTree(Tree.head.right,auxTree)
    else:
        insertTree(Tree.head.left,auxTree)

def getMin(Tree):
    if Tree.head:
        if Tree.head.left.head:
            return getMin(Tree.head.left)
        else:
            return Tree.head.val
    else:
        return None
    
def getMax(Tree):
    if Tree.head:
        if Tree.head.right.head:
            return getMax(Tree.head.right)
        else:
            return Tree.head.val
    else:
        return None
    
def getDif(self,Tree):
    maxim = getMax(Tree)
    minim = getMin(Tree)
    if maxim != None and minim != None:
        return maxim - minim
    else:
        return None

aux = BST()

putIn(5,aux)
putIn(10,aux)
putIn(12,aux)
putIn(1,aux)
putIn(4,aux)
putIn(5,aux)
putIn(7,aux)
putOut(5,aux)
putIn(-1,aux)

print(aux.head.val)
print(aux.head.left.head.val)
print(aux.head.right.head.val)
