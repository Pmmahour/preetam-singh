import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def storedeletescreen():
    t=tkinter.Tk()
    t.geometry('600x600')
    t.title('store')

    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select custid from customers"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
        
    def deletedata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')#common step
        cur=db.cursor()#common step
        sql="delete from store where storeid=%d" %(xa) 
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','deleted')
        aa.delete(0,100)
    
    can1=Canvas(t,height=40,width=580,bg='light blue')
    can1.place(x=10,y=10)
    can2=Canvas(t,height=540,width=580,bg='pink')
    can2.place(x=10,y=50)
    h1=Label(t,text='Store Data',fg='white',font=60,bg='light blue')
    h1.place(x=220,y=20)
    
    a=Label(t,text='Store id:',font=20,fg='black',bg='pink')
    a.place(x=100,y=200)
    aa=ttk.Combobox(t,width=37)
    aa.place(x=170,y=200)
    filldata()
    aa['values']=xt
        
    h=Button(t,text='Delete',command=deletedata,width=8,bg='light grey')
    h.place(x=200,y=250)
    i=Button(t,text='Close',width=8,bg='light grey')
    i.place(x=320,y=250)
    t.mainloop()
