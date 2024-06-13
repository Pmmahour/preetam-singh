import tkinter
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def stockindeletescreen():
    t=tkinter.Tk()
    t.geometry('600x600')
    t.title('Stock Management System')
    
    
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select stockinid from stockin"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    
    
    
    
    def deletedata():
        xa=int(aa.get())
       
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="delete from stockin where stockinid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','deleted')
        
    def close():
        t.destroy()
    
    
    can1=Canvas(t,height=40,width=580,bg='light blue')
    can1.place(x=10,y=10)
    can2=Canvas(t,height=540,width=580,bg='pink')
    can2.place(x=10,y=50)
    h1=Label(t,text='Stockin Register',fg='white',font=60,bg='light blue')
    h1.place(x=220,y=20)
    
    
    a=Label(t,text='Stockin.id:',font=20,bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(t,width=37)
    aa.place(x=170,y=100)
    filldata()
    aa['values']=xt
    
    
    
    bt2=Button(t,text='Delete',command=deletedata,width=8,bg='light grey')
    bt2.place(x=180,y=150)
    
    bt3=Button(t,text='Close',command=close,width=8,bg='light grey')
    bt3.place(x=270,y=150)
    
    
    
    
    
    
    
    
    t.mainloop()
    
