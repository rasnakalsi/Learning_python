import tkinter as tk
from turtle import width 

window=tk.Tk()

canvas=tk.Canvas(window,width=500,height=500,bg="white")
#canvas.create_line(10,380,200,10,380,380,10,380,arrow="first")
#canvas.create_line(10,380,200,10,380,380,10,380,arrow=tk.BOTH,fill="red",smooth=True,width=3)
#canvas.create_polygon(20,380,200,68,380,380,fill="yellow",width=5,outline="red")
#canvas.create_rectangle(200,100,300,300,outline="white",width=5,fill="red")
#canvas.create_oval(100,100,200,200,outline="yellow",fill="cyan",width=5)
#canvas.create_arc(10,100,380,300,outline="red",width=5,extent=90)
#canvas.create_arc(10,100,380,300,outline="blue",width=5,style=tk.CHORD,start=90,fill="white")
#canvas.create_arc(10,100,380,300,outline="green",width=5,start=180,style=tk.ARC,extent=180)
image1=tk.PhotoImage(file="Rasna.png")
canvas.create_image(200,200,image=image1)
button=tk.Button(window,text="Quit",command=window.destroy)
#canvas.create_text(200,200,text="Mary\nhad\na\na\nlittle\nlamb",font=("Arial","40","bold"),justify=tk.CENTER,fill="red")

canvas.grid(row=0)
button.grid(row=1)

window.mainloop()