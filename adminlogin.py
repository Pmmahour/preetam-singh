import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql 
from adminpanel import *

t=tkinter.Tk()
t.geometry('800x500')
t.title('Login Dashboard')

def login():
    username='admin'
    password='root'
    if ent1.get()==username and ent2.get()==password:
        adminpanelscreen()
       
    else:
        messagebox.showerror('Error','Usernmae and Password are incorrect')

#creating Canvas For login Page
can1=Canvas(t,height=500,width=800,bg='aquamarine')
can1.place(x=0,y=0)
can2=Canvas(t,height=350,width=300,bg='gray55')
can2.place(x=250,y=100)

#Creating Heading of login page
lbl1=Label(can2,text='Admin Login',bg='gray',font=('times new roman bold',15))
lbl1.place(x=100,y=20)

#creating Labels for username and password
lbl2=Label(can2,text='USER NAME:',bg='gray55',font=('times new roman bold',12))
lbl2.place(x=20,y=100)
ent1=Entry(can2,width=40)
ent1.place(x=20,y=120)

lbl3=Label(can2,text='PASSWORD:',bg='gray55',font=('times new roman bold',12))
lbl3.place(x=20,y=170)
ent2=Entry(can2,width=40,show='*')
ent2.place(x=20,y=190)

#creating Buttons For login Page
btn1=Button(can2,text='Login',bg='green',width=8,font=('times new roman bold',12),command=login)
btn1.place(x=110,y=240)


t.mainloop()