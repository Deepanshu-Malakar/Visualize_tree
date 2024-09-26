from tkinter import *
from customtkinter import *

class node:
    def __init__(self,val=0,left=None,right=None) -> None:
        self.data=val
        self.left:node=left
        self.right:node=right
    def insert(self,data):
        parent:node=self
        temp:node=self
        while(temp!=None):
            if(data>temp.data):
                parent=temp
                temp=temp.right
            elif(data<temp.data):
                parent=temp
                temp=temp.left
        if(data>parent.data):
            parent.right=node(data)
        elif(data  < parent.data):
            parent.left=node(data)
    def delete(self,key):
        ...
    def preorder(self,root):
        temp:node=root
        if(temp==None):
            return 0
        print(f"{temp.data}",end=", ")
        self.preorder(temp.left)
        self.preorder(temp.right)
        
    def inorder(self,root):
        temp:node=root
        if(temp==None):
            return 0
        self.inorder(temp.left)
        print(f"{temp.data}",end=", ")
        self.inorder(temp.right)

    def postorder(self,root):
        temp:node=root
        if(temp==None):
            return 0
        self.postorder(temp.left)
        self.postorder(temp.right)
        print(f"{temp.data}",end=", ")
        

root=node(10)
root.insert(20)
root.insert(2)
root.insert(0)
root.inorder(root)
print("")
root.postorder(root)
print("")
root.preorder(root)
print("")



