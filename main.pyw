import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = Tk(className=' VALORANT LINEUPS OVERLAY')
frame = tk.Frame(master = root , width=910, height=150)
frame['background']='#dc3d4b'

root.geometry("+5+5")
root.lift()
root.wm_attributes("-topmost", True)


Brim = Image.open('icons/Brim.png')
resize_image = Brim.resize((80, 80))
Brim_icon = ImageTk.PhotoImage(resize_image)

Viper = Image.open('icons/Viper.png')
resize_image = Viper.resize((80, 80))
Viper_icon = ImageTk.PhotoImage(resize_image)

Sova = Image.open('icons/Sova.png')
resize_image = Sova.resize((80, 80))
Sova_icon = ImageTk.PhotoImage(resize_image)

Sage = Image.open('icons/Sage.png')
resize_image = Sage.resize((80, 80))
Sage_icon = ImageTk.PhotoImage(resize_image)

Cypher = Image.open('icons/Cypher.png')
resize_image =Cypher.resize((80, 80))
Cypher_icon = ImageTk.PhotoImage(resize_image)

Killjoy = Image.open('icons/KILLJOY.png')
resize_image = Killjoy.resize((80, 80))
Killjoy_icon = ImageTk.PhotoImage(resize_image)

Phoenix = Image.open('icons/Phoenix.png')
resize_image = Phoenix.resize((80, 80))
Phoenix_icon = ImageTk.PhotoImage(resize_image)

Raze = Image.open('icons/Raze.webp')
resize_image = Raze.resize((80, 80))
Raze_icon = ImageTk.PhotoImage(resize_image)

KAYO = Image.open('icons/KAYO.png')
resize_image = KAYO.resize((80, 80))
KAYO_icon = ImageTk.PhotoImage(resize_image)

Fade = Image.open('icons/Fade.webp')
resize_image = Fade.resize((80, 80))
Fade_icon = ImageTk.PhotoImage(resize_image)

title = tk.Label(master=frame,text="valorant linups overlay",  width=30, height=2,font=("VALORANT","24"),bg="#dc3d4b")
Brim = tk.Button(master=frame,image=Brim_icon,width=75,height=80,bg="#364966",fg="yellow")
Viper = tk.Button(master=frame,image=Viper_icon,width=75,height=80,bg="#364966",fg="yellow")
Sova = tk.Button(master=frame,image=Sova_icon,width=75,height=80,bg="#364966",fg="yellow")
Sage = tk.Button(image=Sage_icon,master=frame,width=75,height=80,bg="#364966",fg="yellow")
Cypher = tk.Button(master=frame,image=Cypher_icon,width=75,height=80,bg="#364966",fg="yellow")
Killjoy = tk.Button(master=frame,image=Killjoy_icon,width=75,height=80,bg="#364966",fg="yellow")
Phoenix = tk.Button(master=frame,image=Phoenix_icon,width=75,height=80,bg="#364966",fg="yellow")
Raze = tk.Button(master=frame,image=Raze_icon,width=75,height=80,bg="#364966",fg="yellow")
KAYO = tk.Button(master=frame,image=KAYO_icon,width=75,height=80,bg="#364966",fg="yellow")
Fade = tk.Button(master=frame,image=Fade_icon,width=75,height=80,bg="#364966",fg="yellow")


Brim.place(x=10,y=50)
Viper.place(x=100,y=50)
Sova.place(x=190,y=50)
Sage.place(x=280,y=50)
Cypher.place(x=370,y=50)
Killjoy.place(x=460,y=50)
Phoenix.place(x=550,y=50)
Raze.place(x=640,y=50)
KAYO.place(x=730,y=50)
Fade.place(x=820,y=50)

title.place(x=165,y=0)

frame.pack()

root.mainloop()