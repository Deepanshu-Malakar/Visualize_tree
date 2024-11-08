from customtkinter import *
from tkinter import *
from PIL import Image,ImageTk
import pywinstyles
import pyglet


set_appearance_mode("dark")
set_default_color_theme("green")

background=CTkImage(Image.open("assets/background.jpg"),size=(1080,720))
titleImg=CTkImage(Image.open("assets/logo.png"),size=(263/4,263/4))
root=CTk()
pywinstyles.change_header_color(root,"#346B3E")
pywinstyles.change_border_color(root,"#346B3E")
pyglet.font.add_file("fonts/SairaStencilOne-Regular.ttf")
sairaStencil=CTkFont(family='Saira Stencil One', size=40)
root.geometry("1080x720")
backgroundLabel=CTkLabel(root,image=background,text="")
backgroundLabel.place(x=0,y=0)
#created the background image

titleLabel=CTkLabel(root,image=titleImg,text="Welcome to Tree Visualizer",compound=LEFT,font=sairaStencil,fg_color="#346B3E")
pywinstyles.set_opacity(titleLabel,0.9)
titleLabel.pack(padx=0,pady=0,fill="x")

canvasFrame=CTkScrollableFrame(root,fg_color="white",corner_radius=0,border_color="black",border_width=0)
sideFrame=CTkFrame(root,corner_radius=0,fg_color="#579A63")
bottomFrame=CTkFrame(root,fg_color="#334037",corner_radius=0)
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
        self.entry=CTkEntry(self.frame,width=200,fg_color="white",placeholder_text=f"Enter value to {job} ",corner_radius=0,border_width=0,border_color="black",font=("Sansation",12))
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



root.mainloop()
