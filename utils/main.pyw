from tkinter import *
from customtkinter import *

class node:
    def __init__(self,val=0,left=None,right=None) -> None:
        self.data=val
        self.left:node=left
        self.right:node=right
        self.button=CTkButton(root,text=val,corner_radius=10,fg_color="green")
        self.high=1
    def insert(self,data):
        parent:node=self
        temp:node=self
        if(temp==None):
            temp=node(data)
            return -1
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
        #find height
        if(parent.left==None):
            h1=0
        else:
            h1=parent.left.high
        if(parent.right==None):
            h2=0
        else:
            h2=parent.right.high
        parent.high=1+max(h1,h2)

    def height(self,parent):
        parent:node=self
        if(parent==None):
            return 0
        else:
            return 1+max(parent.left.high,parent.right.high)
    def delete(self,key):
        temp:node=self
        parent:node=temp
        while(temp.data!=key):
            if(temp==None):
                print("node not found")
                return -1
            elif(key>temp.data):
                parent=temp
                temp=temp.right
            elif(key<temp.data):
                parent=temp
                temp=temp.left
        if(temp.left==None):
            if(temp==parent.right):
                parent.right=temp.right
            elif(temp==parent.left):
                parent.left=temp.right
        elif(temp.right==None):
            if(temp==parent.right):
                parent.right=temp.left
            else:
                parent.left=temp.left
        else:
            #find lowest number from the right sub tree
            temp2:node=temp.right
            parent2:node=temp
            while(temp2.left!=None):
                parent2=temp2
                temp2=temp2.left
            temp.data=temp2.data
            if(temp2==parent2.left):
                parent2.left=None
            elif(temp2==parent2.right):
                parent2.right=None

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

def draw_tree():
    ...        



set_appearance_mode("dark")
root=CTk()
root.geometry("800x500")
root.title("Tree Visualiser")
root_node:node=node(-100)

buttons_frame=CTkFrame(root,corner_radius=1,border_color="black",border_width=1)
buttons_frame.pack(side=LEFT,fill="y",padx=0,pady=0)

label=CTkLabel(buttons_frame,text="What would you like to do")
label.pack(padx=10,pady=1)


buttons_grid=CTkFrame(buttons_frame,border_width=0,fg_color="transparent")
buttons_grid.pack(padx=10,pady=10)

insert_entry=CTkEntry(buttons_grid,placeholder_text="value to be inserted",corner_radius=1,border_color="black",border_width=0,width=150)
insert_entry.grid(padx=0,pady=10,row=0,column=0)
# start=0
def insert_callback():
    e=int(insert_entry.get())
    if(root_node.data==-100):
        root_node.data=e
    else:
        root_node.insert(e)
    print(f"preorder: {root_node.preorder(root_node)}")
    print(f"inorder: {root_node.inorder(root_node)}")
    print(f"postorder: {root_node.postorder(root_node)}")
    print("-------------------------------------")
    draw_tree()
insert_btn=CTkButton(buttons_grid,width=50,text="Insert",corner_radius=1,command=insert_callback)
insert_btn.grid(padx=0,pady=10,row=0,column=1)

delete_entry=CTkEntry(buttons_grid,placeholder_text="value to be deleted",corner_radius=1,border_color="black",border_width=0,width=150)
delete_entry.grid(padx=0,pady=10,row=1,column=0)

def delete_callback():
    pass
delete_btn=CTkButton(buttons_grid,width=50,text="Delete",corner_radius=1,command=delete_callback)
delete_btn.grid(padx=0,pady=10,row=1,column=1)



root.mainloop()
