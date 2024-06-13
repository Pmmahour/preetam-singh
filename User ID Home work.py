import tkinter 
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
#screen create 
t=tkinter.Tk()
#size
t.geometry('800x800')
def login():
    r=b.get()
    s=d.get()
    if r=='test' and s=='123':
        messagebox.showinfo('hi','success')
    else:
         messagebox.showinfo('hi','failed')
#title of screen
t.title('login ID')
a=Label(t,text='NAME', font=16)
a.place(x=200,y=200)
b=Entry(t,width=25)
b.place(x=350,y=200)
c=Label(t,text='PASSWORD', font=16)
c.place(x=200,y=250)
d=Entry(t,width=25, show='*')
d.place(x=350,y=250)
b1=Button(t,text='Ok',command=login)
b1.place(x=300,y=320)
b2=Button(t,text='Cancel')
b2.place(x=380,y=320)
t.config(bg='sea green')
t.mainloop()