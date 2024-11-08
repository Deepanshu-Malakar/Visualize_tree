from customtkinter import *
from tkinter import *
from PIL import Image,ImageTk
import pywinstyles
import pyglet
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import networkx as nx
# import torch
# from utils import plotting

set_appearance_mode("dark")
set_default_color_theme("green")

background=CTkImage(Image.open("assets/background.jpg"),size=(1080,720))
titleImg=CTkImage(Image.open("assets/tree logo.png"),size=(263/3,263/3))
root=CTk()

pywinstyles.change_header_color(root,"#346B3E")
pywinstyles.change_border_color(root,"#346B3E")
pyglet.font.add_file("fonts/SairaStencilOne-Regular.ttf")
sairaStencil=CTkFont(family='Saira Stencil One', size=40)
sansation=CTkFont(family="Sansation",size=16)

root.title("Tree Visualizer")
root.geometry("1080x720")
backgroundLabel=CTkLabel(root,image=background,text="")
backgroundLabel.place(x=0,y=0)
#created the background image

titleLabel=CTkLabel(root,image=titleImg,text="Welcome to Tree Visualizer",compound=LEFT,font=sairaStencil,fg_color="#346B3E")
pywinstyles.set_opacity(titleLabel,0.9)
titleLabel.pack(padx=0,pady=0,fill="x")

canvasFrame=CTkScrollableFrame(root,fg_color="white",corner_radius=0,border_color="black",border_width=0)
sideFrame=CTkFrame(root,corner_radius=0,fg_color="#579A63")
bottomFrame=CTkFrame(root,fg_color="#403B33",corner_radius=0)
pywinstyles.set_opacity(sideFrame,0.9)
pywinstyles.set_opacity(bottomFrame,0.8)


bottomFrame.pack(side=BOTTOM,padx=0,pady=0,fill="x")
sideFrame.pack(side=LEFT,padx=0,pady=0,fill="y")
canvasFrame.pack(padx=0,pady=0,fill="both",expand=True)

#creating the main layout
class Inputs:
    def __init__(self,job:str,r):
        self.image=CTkImage(Image.open("assets/insert logo.png"),size=(20,20))
        self.frame=CTkFrame(sideFrame,fg_color="transparent")
        self.entry=CTkEntry(self.frame,width=200,fg_color="white",placeholder_text=f"Enter value to {job} ",corner_radius=0,border_width=0,border_color="black",font=("Sansation",12),text_color="Black")
        self.label=CTkLabel(self.frame,text=f"{job}",font=("Sansation",12,"bold"),text_color="white",justify="left")
        self.button=CTkButton(self.frame,text="",image=self.image,compound=LEFT,width=50,corner_radius=0,fg_color="#346B3E")

        self.label.grid(row=0,column=0)
        self.frame.grid(row=r,column=0,padx=10,pady=10)
        self.entry.grid(row=1,column=0,columnspan=10)
        self.button.grid(row=1,column=11)
        pywinstyles.set_opacity(self.button,1)
        pywinstyles.set_opacity(self.label,1)
        pywinstyles.set_opacity(self.entry,1)
        # pywinstyles.set_opacity(self.image,1)

insert_input=Inputs("Insert",0)
delete_input=Inputs("Delete",2)
titleImg=CTkImage(Image.open("assets/tree logo.png"),size=(263,263))
logoLabel=CTkLabel(sideFrame,image=titleImg,text="")
logoLabel.grid(row=4,column=0)
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
selectTreeLabel=CTkLabel(bottomFrame,text="Select Tree to Visualize",font=sansation)
selectTraversalLabel=CTkLabel(bottomFrame,text="Select Traversal for tree to Visualize",font=sansation)
_label=CTkLabel(bottomFrame,text="",width=50)
selectTreeLabel.grid(row=0,column=0,columnspan=4)
selectTraversalLabel.grid(row=0,column=5,columnspan=3)
_label.grid(row=0,column=4)


class FooterButton:
    def __init__(self,name:str,c):
        self.button=CTkButton(bottomFrame,text=name,font=sansation,corner_radius=0,fg_color="#252424",width=150,height=50)
        self.button.grid(row=1,column=c)

BinaryTreeBtn=FooterButton("Binary Tree",0)
BinarySearchTreeBtn=FooterButton("Binary Search Tree",1)
AvlTreeBtn=FooterButton("AVL Tree",2)
RedBlackTreeBtn=FooterButton("Red Black Tree",3)
PreorderBtn=FooterButton("Pre-order",5)
InorderBtn=FooterButton("In-order",6)
PostorderBtn=FooterButton("Post-order",7)
root.mainloop()
