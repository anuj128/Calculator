from tkinter import*

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
     if scvalue.get().isdigit():
            value= int(scvalue.get())
     else:
         try:
                value=eval(screen.get())

         except Exception as e:
             print(e)
             scvalue.set("Error")
             screen.update()


     scvalue.set(value)
     screen.update()
            
    elif text =="C":
        scvalue.set("")
        screen.update()
    else:
                         scvalue.set(scvalue.get()+ text)
                         screen.update()


root=Tk()

root.title("My First Calculatior")
root.configure(background="grey")
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 16 bold")
screen.pack(ipadx=8,pady=10,padx=10)

f=Frame(root,bg="grey")
b=Button(f,text="9",padx=14,pady=8,font="lucida 12 bold")
b.pack(side=LEFT,padx=12,pady=3)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="8",padx=14,pady=8,font="lucida 12 bold")
b.pack(side=LEFT,padx=12,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="7",padx=14,pady=8,font="lucida 12 bold")
b.pack(side=LEFT,padx=12,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="6",padx=14,pady=8,font="lucida 12 bold")
b.pack(side=LEFT,padx=12,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="5",padx=14,pady=8,font="lucida 12 bold")
b.pack(side=LEFT,padx=12,pady=5)
b.bind("<Button-1>",click)
f.pack()
b=Button(f,text="4",padx=14,pady=8,font="lucida 12 bold")
b.pack(side=LEFT,padx=12,pady=5)
b.bind("<Button-1>",click)
f.pack()
b=Button(f,text="3",padx=14,pady=8,font="lucida 12 bold")
b.pack(side=LEFT,padx=12,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="2",padx=14,pady=8,font="lucida 12 bold")
b.pack(side=LEFT,padx=12,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="1",padx=14,pady=8,font="lucida 12 bold")
b.pack(side=LEFT,padx=12,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="0",padx=14,pady=8,font="lucida 12 bold")
b.pack(side=LEFT,padx=12,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="+",padx=14,pady=8,font="lucida 12 bold")
b.pack(side=LEFT,padx=12,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="-",padx=14,pady=8,font="lucida 12 bold")
b.pack(side=LEFT,padx=12,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="*",padx=14,pady=8,font="lucida 12 bold")
b.pack(side=LEFT,padx=12,pady=3)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="/",padx=14,pady=8,font="lucida 12 bold")
b.pack(side=LEFT,padx=12,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="%",padx=14,pady=8,font="lucida 12 bold")
b.pack(side=LEFT,padx=12,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="=",padx=14,pady=8,font="lucida 12 bold")
b.pack(side=LEFT,padx=12,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="C",padx=14,pady=8,font="lucida 12 bold")
b.pack(side=LEFT,padx=12,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text=".",padx=14,pady=8,font="lucida 12 bold")
b.pack(side=LEFT,padx=12,pady=5)
b.bind("<Button-1>",click)
f.pack()
b=Button(f,text="00",padx=14,pady=8,font="lucida 12 bold")
b.pack(side=LEFT,padx=12,pady=5)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()
