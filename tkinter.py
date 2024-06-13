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
c.create_line(50,50,150,150)
c.create_line(70,70,70,200)
c.create_line(100,100,300,100)
t.mainloop()