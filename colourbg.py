from tkinter import *
from tkinter import font

gui = Tk()
gui.geometry("650x550")
gui.title("Colour BG Changer")
gui.config(background="pale green")
print(font.families())

def add_colour():
    global colours
    colour = entry1.get()
    if colour.lower() not in colours:
        colours.append(colour)
    make()

def delete_colour():
    global colours
    colour = entry1.get()
    if colour.lower() in colours:
        colours.remove(colour)
    make()


frame1 = Frame(gui,bg="light pink",height= 150)
frame1.pack(fill=X)

label1 = Label(gui,text = "Colour BG Changer", bg = "light pink", fg = "gray0", font=("Arial",30))
label1.place(x= 140, y=30)

entry1 = Entry(gui,bg="gray99", fg= "gray0", font=("Arial",18),width=25)
entry1.place(x=165 ,y=195)

colours = ["white", "red", "blue", "green", "orange", "pink", "purple", "black"]

select = StringVar(value="pale green")

def make():
    global select, colours
    for widget in gui.winfo_children():
        if isinstance(widget, Radiobutton):
            widget.destroy()
    y_pos=230
    for L in colours:
        Radiobutton(gui,text=L,variable=select,value=L,bg="pale green",command=change_colour).place(x=170,y=y_pos)
        y_pos += 30
    gui.update()
def change_colour():
    global select
    selection = select.get()
    gui.config(bg=selection)
    gui.update()
make()

add = Button(gui,highlightbackground="gray99",fg="gray0",text = "ADD",font=("Arial",18),command=add_colour)
add.place(x=500 ,y=195)    

delete = Button(gui,highlightbackground="gray99",fg="gray0",text = "DELETE",font=("Arial",18),command=delete_colour)
delete.place(x=500 ,y=235)    

gui.mainloop()
