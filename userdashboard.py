import tkinter
from tkinter import *
from stockinsave import *
from stockindelete import *
from stockinupdate import *
from stockinfind import *
from stockinshow import *
from customersave import *
from customershow import *
from customerupdate import *
from customerfind import *
from customerdelete import *
from dispatchsave import *
from dispatchdelete import *
from dispatchshow import *
from dispatchupdate import *
from dispatchfind import *
from ordersave import *
from orderdelete import *
from orderfind import *
from ordershow import *
from orderupdate import *
from productcatdelete import *
from productcatsave import *
from productcatshow import *
from productcatfind import *
from productcatupdate import *
from storesave import *
from storedelete import *
from storeshow import *
from storeupdate import *
from storefind import *
from productsave import *
from productfind import *
from productshow import *
from supplierfind import *
from suppliershow import *





t=tkinter.Tk()
t.geometry('600x600')
t.title('Stock Management-Dashboard')

def close():
    t.destroy()


can1=Canvas(t,height=450,width=105,bg='grey')
can1.place(x=5,y=5)

can2=Canvas(t,height=30,width=480,bg='grey')
can2.place(x=110,y=5)

can3=Canvas(t,height=415,width=480,bg='light grey')
can3.place(x=110,y=40)

can4=Canvas(t,height=540,width=580,bg='grey')
can4.place(x=5,y=450)

btn1=Button(t,text='Back to Login',bg='light green')
btn1.place(x=18,y=12)

btn2=Button(t,text='Close Panel',bg='red',command=close)
btn2.place(x=515,y=10)

h1=Label(t,text='User Panel',font=40,bg='grey')
h1.place(x=290,y=10)

a1=Label(t,text='Store:',font=20,bg='grey')
a1.place(x=20,y=50)


b4=Button(t,text='Find',command=storefindscreen,bg='light blue',width=8)
b4.place(x=220,y=50)
b5=Button(t,text='Show',command=storeshowscreen,bg='light blue',width=8)
b5.place(x=320,y=50)

a2=Label(t,text='Prod.Catg:',font=20,bg='grey')
a2.place(x=20,y=100)

c4=Button(t,text='Find',command=productcatfindscreen,bg='light blue',width=8)
c4.place(x=220,y=100)
c5=Button(t,text='Show',command=productcatshowscreen,bg='light blue',width=8)
c5.place(x=320,y=100)

a3=Label(t,text='Products:',font=20,bg='grey')
a3.place(x=20,y=150)

d4=Button(t,text='Find',bg='light blue',width=8,command=productfindscreen)
d4.place(x=220,y=150)
d5=Button(t,text='Show',bg='light blue',width=8,command=productshowscreen)
d5.place(x=320,y=150)

a4=Label(t,text='Supplier:',font=20,bg='grey')
a4.place(x=20,y=200)

e4=Button(t,text='Find',bg='light blue',width=8,command=supplierfindscreen)
e4.place(x=220,y=200)
e5=Button(t,text='Show',bg='light blue',width=8,command=suppliershowscreen)
e5.place(x=320,y=200)


a5=Label(t,text='Stockinreg:',font=20,bg='grey')
a5.place(x=20,y=250)

f4=Button(t,text='Find',command=stockinfindscreen,bg='light blue',width=8)
f4.place(x=220,y=250)
f5=Button(t,text='Show',command=stockinshowscreen,bg='light blue',width=8)
f5.place(x=320,y=250)

a6=Label(t,text='Customer:',font=20,bg='grey')
a6.place(x=20,y=300)

g4=Button(t,text='Find',command=customerfindscreen,bg='light blue',width=8)
g4.place(x=220,y=300)
g5=Button(t,text='Show',command=customershowscreen,bg='light blue',width=8)
g5.place(x=320,y=300)

a7=Label(t,text='Orders:',font=20,bg='grey')
a7.place(x=20,y=350)

h4=Button(t,text='Find',command=orderfindscreen,bg='light blue',width=8)
h4.place(x=220,y=350)
h5=Button(t,text='Show',command=ordershowscreen,bg='light blue',width=8)
h5.place(x=320,y=350)



a8=Label(t,text='Disptchbill',font=20,bg='grey')
a8.place(x=20,y=400)

i4=Button(t,text='Find',command=dispatchfindscreen,bg='light blue',width=8)
i4.place(x=220,y=400)
i5=Button(t,text='Show',command=dispatchshowscreen,bg='light blue',width=8)
i5.place(x=320,y=400)

t.mainloop()






