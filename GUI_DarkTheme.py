from customtkinter import *
from tkinter import *
from PIL import Image,ImageTk
import pywinstyles
import pyglet
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import networkx as nx
from utils import colors
from Trees import binarySearchTree as BST


header_color=colors.dark_blue
side_frame_color=colors.dark_brown
bottom_frame_color=colors.dark_brown
bottom_button_color=colors.dark_gray
hover_color=colors.dark_blue
set_appearance_mode("dark")
set_default_color_theme("green")

background=CTkImage(Image.open("assets/background.jpg"),size=(1080,720))
titleImg=CTkImage(Image.open("assets/logo.png"),size=(263/3,263/3))
root=CTk()

pywinstyles.change_header_color(root,header_color)
pywinstyles.change_border_color(root,header_color)
pywinstyles.apply_style(root,"aero")
pyglet.font.add_file("fonts/SairaStencilOne-Regular.ttf")
sairaStencil=CTkFont(family='Saira Stencil One', size=40)
sansation=CTkFont(family="Sansation",size=16)

root.title("Tree Visualizer")
root.geometry("1080x720")
backgroundLabel=CTkLabel(root,image=background,text="")
# backgroundLabel.place(x=0,y=0)
#created the background image

titleLabel=CTkLabel(root,image=titleImg,text="Welcome to Tree Visualizer",compound=LEFT,font=sairaStencil,fg_color=header_color)
pywinstyles.set_opacity(titleLabel,0.9)
titleLabel.pack(padx=0,pady=0,fill="x")

canvasFrame=CTkFrame(root,fg_color="white",corner_radius=0,border_color="black",border_width=0)
sideFrame=CTkFrame(root,corner_radius=0,fg_color=side_frame_color)
bottomFrame=CTkFrame(root,fg_color=bottom_frame_color,corner_radius=0)
pywinstyles.set_opacity(sideFrame,0.9)
pywinstyles.set_opacity(bottomFrame,0.8)
pywinstyles.set_opacity(canvasFrame,0.9)


bottomFrame.pack(side=BOTTOM,padx=0,pady=0,fill="x")
sideFrame.pack(side=LEFT,padx=0,pady=0,fill="y")
canvasFrame.pack(padx=0,pady=0,fill="both",expand=True)

#creating the main layout
class Inputs:
    def __init__(self,job:str,r):
        self.image=CTkImage(Image.open("assets/insert logo.png"),size=(20,20))
        self.frame=CTkFrame(sideFrame,fg_color="transparent")
        self.entry=CTkEntry(self.frame,width=200,fg_color="white",placeholder_text=f"Enter value to {job} ",corner_radius=0,border_width=1,border_color=header_color,font=("Sansation",12),text_color="Black")
        self.label=CTkLabel(self.frame,text=f"{job}",font=("Sansation",12,"bold"),text_color="white",justify="left")
        self.button=CTkButton(self.frame,text="",image=self.image,compound=LEFT,width=50,corner_radius=0,fg_color=bottom_button_color,hover_color=hover_color,command=self.click)

        self.label.grid(row=0,column=0)
        self.frame.grid(row=r,column=0,padx=10,pady=10)
        self.entry.grid(row=1,column=0,columnspan=10)
        self.button.grid(row=1,column=11)
        pywinstyles.set_opacity(self.button,1)
        pywinstyles.set_opacity(self.label,1)
        pywinstyles.set_opacity(self.entry,1)
        # pywinstyles.set_opacity(self.image,1)
    def click(self):
        pass

insert_input=Inputs("Insert",0)
delete_input=Inputs("Delete",2)
titleImg=CTkImage(Image.open("assets/tree logo.png"),size=(263,263))
logoLabel=CTkLabel(sideFrame,image=titleImg,text="")
# logoLabel.grid(row=4,column=0)
#creating the canvas
# fig=Figure(figsize=(5,5),dpi=100)
# x=torch.arange(1,100,0.1)
# y=torch.sin(x)
# fig.add_subplot(111).plot(x,y)

G=nx.DiGraph()
G.add_edge(5,6)
G.add_edge(5,4)
pos={5:(2,0),6:(3,-1),4:(1,-1)}
fig=Figure(figsize=(5,5))
a=fig.add_subplot(111)
nx.draw(G,with_labels=True,pos=pos,node_color="skyblue",ax=a)
canvas=FigureCanvasTkAgg(fig,master=canvasFrame)
canvas.draw()
canvas.get_tk_widget().pack(fill="both",expand=True)



#creating footer buttons
tree_type_frame=CTkFrame(bottomFrame,fg_color="transparent")
tree_type_frame.pack(side=LEFT,padx=0,pady=0)

tree_traversal_frame=CTkFrame(bottomFrame,fg_color="transparent")
tree_traversal_frame.pack(side=RIGHT,padx=0,pady=0)

selectTreeLabel=CTkLabel(tree_type_frame,text="Select Tree to Visualize",font=sansation)
selectTraversalLabel=CTkLabel(tree_traversal_frame,text="Select Traversal for tree to Visualize",font=sansation)
# _label=CTkLabel(bottomFrame,text="",width=50)
selectTreeLabel.grid(row=0,column=0,columnspan=4)
selectTraversalLabel.grid(row=0,column=0,columnspan=3)
# _label.grid(row=0,column=4)


class FooterButton:
    def __init__(self,name:str,c,frame=""):
        self.button=CTkButton(frame,text=name,font=sansation,corner_radius=0,fg_color=bottom_button_color,width=150,height=50,hover_color=hover_color,command=self.click)
        self.button.grid(row=1,column=c)
    def click(self):
        pass

BinaryTreeBtn=FooterButton("Binary Tree",0,tree_type_frame)
BinarySearchTreeBtn=FooterButton("Binary Search Tree",1,tree_type_frame)
AvlTreeBtn=FooterButton("AVL Tree",2,tree_type_frame)
RedBlackTreeBtn=FooterButton("Red Black Tree",3,tree_type_frame)
PreorderBtn=FooterButton("Pre-order",0,tree_traversal_frame)
InorderBtn=FooterButton("In-order",1,tree_traversal_frame)
PostorderBtn=FooterButton("Post-order",2,tree_traversal_frame)



#functions...................
def resetAllTreeButtons():
    BinaryTreeBtn.button.configure(fg_color=bottom_button_color)
    BinarySearchTreeBtn.button.configure(fg_color=bottom_button_color)
    AvlTreeBtn.button.configure(fg_color=bottom_button_color)
    RedBlackTreeBtn.button.configure(fg_color=bottom_button_color)

def delete_canvas_frame():
    try:
        canvasFrame.destroy()
    except:
        pass

def delete_canvas():
    try:
        canvas.get_tk_widget().destroy()
    except:
        pass

def drawTree():
    delete_canvas_frame()
    global canvasFrame
    canvasFrame=CTkFrame(root,fg_color="white",corner_radius=0,border_color="black",border_width=0)
    canvasFrame.pack(padx=0,pady=0,fill="both",expand=True)
    global canvas
    canvas=FigureCanvasTkAgg(fig,master=canvasFrame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both",expand=True)


def BinarySearchTreeBtn_Callback():
    delete_canvas_frame()
    global canvasFrame
    canvasFrame=CTkFrame(root,fg_color="white",corner_radius=0,border_color="black",border_width=0)
    canvasFrame.pack(padx=0,pady=0,fill="both",expand=True)
    resetAllTreeButtons()
    BinarySearchTreeBtn.button.configure(fg_color=header_color)
    global tree_choice
    tree_choice=2
    BST.root=None
    global G
    G=nx.DiGraph()
    global fig
    global a
    fig=Figure(figsize=(5,5))
    a=fig.add_subplot(111)
    global canvas
    canvas=FigureCanvasTkAgg(fig,master=canvasFrame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both",expand=True)
    

def BinaryTreeBtn_Callback():
    delete_canvas_frame()
    global canvasFrame
    canvasFrame=CTkFrame(root,fg_color="white",corner_radius=0,border_color="black",border_width=0)
    canvasFrame.pack(padx=0,pady=0,fill="both",expand=True)
    resetAllTreeButtons()
    BinaryTreeBtn.button.configure(fg_color=header_color)
    global tree_choice
    tree_choice=1


def AvlTreeBtn_Callback():
    delete_canvas_frame()
    global canvasFrame
    canvasFrame=CTkFrame(root,fg_color="white",corner_radius=0,border_color="black",border_width=0)
    canvasFrame.pack(padx=0,pady=0,fill="both",expand=True)
    resetAllTreeButtons()
    AvlTreeBtn.button.configure(fg_color=header_color)
    global tree_choice
    tree_choice=3

def RedBlackTreeBtn_Callback():
    delete_canvas_frame()
    global canvasFrame
    canvasFrame=CTkFrame(root,fg_color="white",corner_radius=0,border_color="black",border_width=0)
    canvasFrame.pack(padx=0,pady=0,fill="both",expand=True)
    resetAllTreeButtons()
    RedBlackTreeBtn.button.configure(fg_color=header_color)
    global tree_choice
    tree_choice=4

BinarySearchTreeBtn.button.configure(command=BinarySearchTreeBtn_Callback)
BinaryTreeBtn.button.configure(command=BinaryTreeBtn_Callback)
AvlTreeBtn.button.configure(command=AvlTreeBtn_Callback)
RedBlackTreeBtn.button.configure(command=RedBlackTreeBtn_Callback)

#insert and delete functions
tree_choice=0
"""
treeChoice=1   Binary Tree
treeChoice=2   Binary Search Tree
treeChoice=3   Avl Tree
treeChoice=4   Red Black Tree

"""

def insert_button_callback():
    key=int(insert_input.entry.get())
    if(tree_choice==2):
        drawTree()
        G=nx.DiGraph()
        BST.root=BST.insert(BST.root,key)
        BST.inorder(BST.root)
        print("")
        pos={}
        def add_edges(node:BST.Treenode,x:int,y:int,dx):
            if node is not None:
                pos[node.data]=(x,y)
                if node.left:
                    G.add_edge(node.data,node.left.data)
                    add_edges(node.left,x-dx,y-1,dx/2)
                if node.right:
                    G.add_edge(node.data,node.right.data)
                    add_edges(node.right,x+dx,y-1,dx/2)
        add_edges(BST.root,0,0,4)
        nx.draw(G,with_labels=True,pos=pos,node_color="skyblue",ax=a)
        canvas.draw()

def delete_button_callback():
    key=int(delete_input.entry.get())
    if(tree_choice==2):
        drawTree()
        G=nx.DiGraph()
        BST.root=BST.delete(BST.root,key)
        BST.inorder(BST.root)
        print("")
        pos={}
        def add_edges(node:BST.Treenode,x:int,y:int,dx):
            if node is not None:
                pos[node.data]=(x,y)
                if node.left:
                    G.add_edge(node.data,node.left.data)
                    add_edges(node.left,x-dx,y-1,dx/2)
                if node.right:
                    G.add_edge(node.data,node.right.data)
                    add_edges(node.right,x+dx,y-1,dx/2)
        add_edges(BST.root,0,0,4)
        nx.draw(G,with_labels=True,pos=pos,node_color="skyblue",ax=a)
        canvas.draw()    

insert_input.button.configure(command=insert_button_callback)
delete_input.button.configure(command=delete_button_callback)


root.mainloop()
