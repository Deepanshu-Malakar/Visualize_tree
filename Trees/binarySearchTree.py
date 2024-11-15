class Treenode:
    def __init__(self,val:int):
        self.data=val
        self.left:Treenode=None
        self.right:Treenode=None

def minimumRightSubTree(root:Treenode):
    temp=root.right
    while(temp.left is not None):
        temp=temp.left
    return temp

def insert(root:Treenode,key)->Treenode:
    if(root is None):
        root=Treenode(key)
        root.left=None
        root.right=None
        return root
    elif(key>root.data):
        root.right=insert(root.right,key)
        return root
    elif(key<root.data):
        root.left=insert(root.left,key)
        return root

def inorder(root:Treenode):
    if(root is None):
        return 0
    inorder(root.left)
    print(root.data,end=",")
    inorder(root.right)

def delete(root:Treenode,key:int)->Treenode:
    if(root is None):
        return -1
    elif(key>root.data):
        root.right=delete(root.right,key)
        return root
    elif(key<root.data):
        root.left=delete(root.left,key)
        return root
    #one child
    if(root.left is None):
        temp=root.right
        return temp
    elif(root.right is None):
        temp=root.left
        return temp
    else:
        temp:Treenode=minimumRightSubTree(root)
        root.data=temp.data
        root.right=delete(root.right,temp.data)
        return root
root=None