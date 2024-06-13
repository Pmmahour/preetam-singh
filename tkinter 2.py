import tkinter 
from tkinter import*
#screen create 
t=tkinter.Tk()
#size
t.geometry('800x800')
#title of screen
t.title('my first screen')
#show screen
c=Canvas(t,height=700,width=700,bg='pink')
c.place(x=10,y=10)
c.create_rectangle(100,50,300,200,fill='red')
c.create_oval(100,350,300,550,fill='yellow')
p=[50,300,250,100,350,300]
c.create_polygon(p,fill='green')
c.create_text(200,600,text='PYTHON')
t.mainloop()