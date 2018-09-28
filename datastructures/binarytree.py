#class to define binary tree
class BinTree:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key

#function to insert nodes in binary tree	 
def insert(root, node):     
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
                
#function to do inorder traversal of binary tree
def treetraversal(tree):
    if tree != None:
        treetraversal(tree.left)
        print(tree.val)
        treetraversal(tree.right)
	 
#Insert the root node
RootNode = int(input("Enter the Root Node:"))
Tree = BinTree(RootNode)

while True:
    try:
        Inp = int(input("Enter the Other Nodes:"))
        insert(Tree,BinTree(Inp))
    except:
        break    
treetraversal(Tree)

