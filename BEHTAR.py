from tkinter import*
import random
from tkinter import messagebox


def new():
        
        import sqlite3
        
        import random
        window=Tk()
        window.geometry("600x300")
        window.configure(bg="light green")




        def login():
                
                def login_database():
                        conn=sqlite3.connect("1.db")
                        cur=conn.cursor()
                        cur.execute("SELECT * FROM test WHERE email=? AND password=?",(e1.get(),e2.get()))
                        row=cur.fetchall()
                        conn.close()
                        print(row)
                        if row!=[]:
                                user_name=row[0][1]
                                l3.config(text="user name found with name: "+user_name)
                                window.destroy()
                                login_window.destroy()
                                
						
                        else:
                                l3.config(text="user not found ")

                

	
                login_window=Tk()
                login_window.geometry("500x450")
                login_window.configure(bg="light green")
                l1=Label(login_window,text="EMAIL",font=('Times', 16, 'bold'),bg="light green")
                l1.place(x=10,y=50)
                l2=Label(login_window,text="PASSWORD",font=('Times', 16, 'bold'),bg="light green")
                l2.place(x=10,y=100)
                l3=Label(login_window,font=('Times', 16, 'bold'),bg="light green")
                l3.place(x=50,y=300)

                email_text=StringVar()
                e1=Entry(login_window,textvariable=email_text,font=('Times', 16, 'bold'),bg="light green")
                e1.place(x=200,y=50)
                password_text=StringVar()
                e2=Entry(login_window,textvariable=password_text,show="*",font=('Times', 16, 'bold'),bg="light green")
                e2.place(x=200,y=100)


                b1=Button(login_window,text="login",width=20,font=('Times', 16, 'bold'),bg="goldenrod",command=login_database)
                b1.place(x=100,y=200)
                login_window.mainloop()




        def signup():


                def signup_database():
                        conn=sqlite3.connect("1.db")
                        cur=conn.cursor()
                        cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name text,email text, password text)")
                        cur.execute("INSERT INTO test Values(Null,?,?,?)",(e1.get(),e2.get(),e3.get()))
                        l4=Label(signup_window,text="account created",font="times 15")
                        l4.grid(row=6,column=2)
                        conn.commit()
                        conn.close()





	
                signup_window=Tk()
                signup_window.geometry("600x400")
                signup_window.configure(bg="light green")
                l1=Label(signup_window,text="USE NAME",font="times 25",bg="light green")
                l1.grid(row=1,column=1)
                l2=Label(signup_window,text="USER EMAIL",font="times 25",bg="light green")
                l2.grid(row=2,column=1)
                l3=Label(signup_window,text="USER PASSWORD",font="times 25",bg="light green")
                l3.grid(row=3,column=1)


                name_text=StringVar()
                e1=Entry(signup_window,textvariable=name_text,font=('Times', 16, 'bold'))
                e1.grid(row=1,column=2)
                email_text=StringVar()
                e2=Entry(signup_window,textvariable=email_text,font=('Times', 16, 'bold'))
                e2.grid(row=2,column=2)
                password_text=StringVar()
                e3=Entry(signup_window,textvariable=password_text,show="*",
                         font=('Times', 16, 'bold'))
                e3.grid(row=3,column=2)

                b1=Button(signup_window,text="login",width=20,font=('Times', 16, 'bold'),bg="goldenrod",command=signup_database)
                b1.grid(row=4,column=1)
                window.mainloop()








        l1=Label(window,text="ORDER MANAGEMENT SYSTEM",font="times 30")
        l1.grid(row=1,column=2,columnspan=2)

        b1=Button(window,text="LOGIN",width=20,font=('Times', 16, 'bold'),command=login,bg="goldenrod")
        b1.grid(row=5,column=2)

        b2=Button(window,text="SIGNUP",width=20,font=('Times', 16, 'bold'),command=signup,bg="goldenrod")
        b2.grid(row=5,column=3)


        window.mainloop()






        
new()
root=Tk()
root.geometry("1600x8000")
root.title("ORDER MANAGEMENT SYSTEM")
root.configure(bg='light green')
Tops=Frame(root, width=1600)
Tops.pack()

f1=Frame(root,width=800,height=700,relief=SUNKEN,bg="light green")
f1.pack()



lblInfo=Label(Tops,font=('Times',50,'bold'),text="ORDER MANAGEMENT SYSTEM",fg="Black",bg="bisque2",bd=15,anchor='w')
lblInfo.grid(row=0,column=0)




  

def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)
    print(x)

    if (P1.get()==""):
        CoP1=0
    else:
        CoP1=float(P1.get())


    
    if (P2.get()==""):
        CoP2=0
    else:
        CoP2=float(P2.get())



    if (P3.get()==""):
        CoP3=0
    else:
        CoP3=float(P3.get())



    if (P4.get()==""):
        CoP4=0
    else:
        CoP4=float(P4.get())

        
    if (P5.get()==""):
        CoP5=0
    else:
        CoP5=float(P5.get())

     

        
    if (P7.get()==""):
        CoP7=0
    else:
        CoP7=float(P7.get())
        
    if (P6.get()==""):
        CoP6=0
    else:
        CoP6=float(P6.get())

    if (P8.get()==""):
        CoP8=0
    else:
        CoP8=float(P8.get())

    if (P9.get()==""):
        CoP9=0
    else:
        CoP9=float(P9.get())

    if (P10.get()==""):
        CoP10=0
    else:
        CoP10=float(P10.get())

    if (P11.get()==""):
        CoP11=0
    else:
        CoP11=float(P11.get())

    if (P12.get()==""):
        CoP12=0
    else:
        CoP12=float(P12.get())

    if (P13.get()==""):
        CoP13=0
    else:
        CoP13=float(P13.get())

    if (P14.get()==""):
        CoP14=0
    else:
        CoP14=float(P14.get())

    if (P15.get()==""):
        CoP15=0
    else:
        CoP15=float(P15.get())

                   
    CostofP1 =CoP1 * 13999
    CostofP6=CoP6 * 999
    CostofP2 = CoP2* 7999
    CostofP3 = CoP3 * 14999
    CostofP4 = CoP4* 17999
    CostofP5=CoP5 * 900
    CostofP7=CoP7*999
    CostofP8=CoP8*13990
    CostofP9=CoP9*14999
    CostofP10=CoP10*7999
    CostofP11=CoP11*9999
    CostofP12=CoP12*6990
    CostofP13=CoP13*5499
    CostofP14=CoP14*21999
    CostofP15=CoP15*7999



    Costof= "Rs", str('%.2f' % (CostofP1+CostofP2+CostofP3+CostofP4+CostofP5+CostofP6+CostofP7+CostofP8+CostofP9+CostofP10+CostofP11+CostofP12+CostofP13+CostofP14+CostofP15))

    PayTax=((CostofP1+CostofP2+CostofP3+CostofP4+CostofP5+CostofP6+CostofP7+CostofP8+CostofP9+CostofP10+CostofP11+CostofP12+CostofP13+CostofP14+CostofP15) * 0.05)

    TotalCost=(CostofP1+CostofP2+CostofP3+CostofP4+CostofP5+CostofP6+CostofP7+CostofP8+CostofP9+CostofP10+CostofP11+CostofP12+CostofP13+CostofP14+CostofP15)
    
 
    

   

    OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost))

    PaidTax= "Rs", str ('%.2f' % PayTax)

    
    Cost.set(Costof)
    Tax.set(PaidTax)
    Total.set(OverAllCost)

    
    
def qExit():
    root.destroy()

def Reset():
    rand.set("") 
    P1.set("")
    P2.set("")
    P3.set("")
    
    Total.set("")
    P6.set("")
    Tax.set("")
    Cost.set("")
    P4.set("")
    P5.set("")
    P7.set("")
    P8.set("")
    P9.set("")
    P10.set("")
    P11.set("")
    P12.set("")
    P13.set("")
    P14.set("")
    P15.set("")
    
    


rand = StringVar()
P1=StringVar()
P2=StringVar()
P3=StringVar()
Total=StringVar()
P6=StringVar()
Tax=StringVar()
Cost=StringVar()
P4=StringVar()
P5=StringVar()
P7=StringVar()
P8=StringVar()
P9=StringVar()
P10=StringVar()
P11=StringVar()
P12=StringVar()
P13=StringVar()
P14=StringVar()
P15=StringVar()

import sqlite3
def database():
    n1=rand.get()
    n2=P1.get()
    n3=P2.get()
    n4=P3.get()
    n5=P6.get()
    n6=P4.get()
    n7=P5.get()
    n8=P7.get()
    n9=P8.get()
    n10=P9.get()
    n11=P10.get()
    n12=P11.get()
    n13=P12.get()
    n14=P13.get()
    n15=P14.get()
    n16=P15.get()
    conn=sqlite3.connect("re2.db")
    #conn.execute("create table Lis(rand varchar(50), Samsung varchar(50), AppleWatch  varchar(50), Realme5Pro varchar(50), Shirt  varchar(50),InverterAC  varchar(50),TShirt  varchar(50),Wallet varchar(50),AirCooler varchar(50),POCOF1 varchar(50),WashingMachine varchar(50),PlayStation5 varchar(50),NikeShoes varchar(50),Jackets varchar(50),Wardrobes varchar(50),SofaBeds varchar(50));")
    conn.execute("insert into Lis(rand,Samsung,AppleWatch, Realme5Pro, Shirt,InverterAC,TShirt,Wallet,AirCooler,POCOF1,WashingMachine,PlayStation5,NikeShoes,Jackets,Wardrobes,SofaBeds)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,))
    c=conn.execute("select * from Lis ")
    for i in c:
                print("n1",i[0])
                print("n2",i[1])
                print("n3",i[2])
                print("n4",i[3])
                print("n5",i[4])
                print("n6",i[5])
                print("n7",i[6])
                print("n8",i[7])
                print("n9",i[8])
                print("n10",i[9])
                print("n11",i[10])
                print("n12",i[11])
                print("n13",i[12])
                print("n14",i[13])
                print("n15",i[14])
                print("n16",i[15])
                conn.commit()

    

def wish():
    def qui():
            allwin.destroy()
    allwin=Tk()
    allwin.title("CART")
    allwin.geometry("1000x550")
    allwin.configure(bg='light green')
    Label(allwin,text="PAYMENT",bg="light green",font=('Times', 40, 'bold')).place(x=200,y=0)
    t = Text(allwin)
    conn=sqlite3.connect("re2.db")
    for i in conn.execute('SELECT * FROM Lis'):
        t.insert(INSERT, i)
        t.insert(INSERT,'\n')

    t.pack()
    Button(allwin,padx=16,pady=8,bd=16,fg="black",font=('Times',16,'bold'),width=10,text="PAY",bg="goldenrod",command=paymnt).place(x=280,y=430)
    Button(allwin,padx=16,pady=8,bd=16,fg="black",font=('Times',16,'bold'),width=10,text="EXIT",bg="goldenrod",command=qui).place(x=600,y=430)
    
def paymnt():
        window=Tk()
        window.geometry("1100x800")
        window.configure(bg='light green')
        def exi():
                window.destroy()
        def pay():
                messagebox.showinfo("PAYMENT", "Payment Successfull")
                window.destroy()
        def cod():
                messagebox.showinfo("COD", "Order Placed")
                window.destroy()        

        
                
        Label(window,text="PAYMENT",bg="light green",font=('Times', 40, 'bold')).place(x=200,y=0)
        Label(window, font=('Times', 16, 'bold'),text="NAME",bd=16,bg="light green",anchor="w").place(x=0,y=100)
        
        Entry(window, font=('Times',10,'bold'),bd=10,insertwidth=2,bg="cyan",justify='right').place(x=250,y=100)
       

        Label(window, font=('Times', 16, 'bold'),text="ADDRESS",bd=16,bg="light green",anchor="w").place(x=0,y=200)
        
        Entry(window, font=('Times',10,'bold'),bd=10,insertwidth=2,bg="cyan",justify='right').place(x=250,y=200)
        


        Label(window, font=('Times', 16, 'bold'),text="MOBILE NUMBER",bd=16,bg="light green",anchor="w").place(x=0,y=300)
        
        Entry(window, font=('Times',10,'bold'),bd=10,insertwidth=2,bg="cyan",justify='right').place(x=250,y=300)
        Label(window, font=('Times', 16, 'bold'),text="UPI ID",bd=16,bg="light green",anchor="w").place(x=0,y=400)
        
        Entry(window, font=('Times',10,'bold'),bd=10,insertwidth=2,bg="cyan",justify='right').place(x=250,y=400)
        Button(window,padx=16,pady=8,bd=16,fg="black",font=('Times',16,'bold'),width=10,text="PAY",bg="goldenrod",command=pay).place(x=500,y=100)
        Button(window,padx=16,pady=8,bd=16,fg="black",font=('Times',16,'bold'),width=10,text="COD",bg="goldenrod",command=cod).place(x=500,y=200)
        
        Button(window,padx=16,pady=8,bd=16,fg="black",font=('Times',16,'bold'),width=10,text="EXIT",bg="goldenrod",command=exi).place(x=500,y=300)
        
        



lblReference= Label(f1, font=('Times', 16, 'bold'),text="ORDER ID",bd=16,bg="light green",anchor="w")
lblReference.grid(row=0, column=0)
txtReference=Entry(f1, font=('Times',10,'bold'),textvariable=rand,bd=10,insertwidth=2,bg="cyan",justify='right')
txtReference.grid(row=0,column=1)

lbl1= Label(f1, font=('Times', 16, 'bold'),text="Samsung M30",bd=16,bg="light green",anchor="w")
lbl1.grid(row=1, column=0)
txt1=Entry(f1, font=('Times',10,'bold'),textvariable=P1,bd=10,insertwidth=2,bg="cyan",justify='right')
txt1.grid(row=1,column=1)


lbl2= Label(f1, font=('Times', 16, 'bold'),text="Apple Watch",bd=16,bg="light green",anchor="w")
lbl2.grid(row=2, column=0)
txt2=Entry(f1, font=('Times',10,'bold'),textvariable=P2,bd=10,insertwidth=2,bg="cyan",justify='right')
txt2.grid(row=2,column=1)


lbl3= Label(f1, font=('Times', 16, 'bold'),text="realme 5 pro",bd=16,bg="light green",anchor="w")
lbl3.grid(row=3, column=0)
txt3=Entry(f1, font=('Times',10,'bold'),textvariable=P3,bd=10,insertwidth=2,bg="cyan",justify='right')
txt3.grid(row=3,column=1)

lbl4= Label(f1, font=('Times', 16, 'bold'),text="Inverter AC",bd=16,bg="light green",anchor="w")
lbl4.grid(row=4, column=0)
txt4=Entry(f1, font=('Times',10,'bold'),textvariable=P4,bd=10,insertwidth=2,bg="cyan",justify='right')
txt4.grid(row=4,column=1)

lbl5= Label(f1, font=('Times', 16, 'bold'),text="T-Shirt",bd=16,bg="light green",anchor="w")
lbl5.grid(row=5, column=0)
txt5=Entry(f1, font=('Times',10,'bold'),textvariable=P5,bd=10,insertwidth=2,bg="cyan",justify='right')
txt5.grid(row=5,column=1)




lbl6= Label(f1, font=('Times', 16, 'bold'),text="Shirt",bd=16,bg="light green",anchor="w")
lbl6.grid(row=0, column=2)
txt6=Entry(f1, font=('Times',10,'bold'),textvariable=P6,bd=10,insertwidth=2,bg="cyan",justify='right')
txt6.grid(row=0,column=3)

lbl7= Label(f1, font=('Times', 16, 'bold'),text="Wallet",bd=16,bg="light green",anchor="w")
lbl7.grid(row=1, column=2)
txt7=Entry(f1, font=('Times',10,'bold'),textvariable=P7,bd=10,insertwidth=2,bg="cyan",justify='right')
txt7.grid(row=1,column=3)

lbl8= Label(f1, font=('Times', 16, 'bold'),text="Air Coolers",bd=16,bg="light green",anchor="w")
lbl8.grid(row=2, column=2)
txt8=Entry(f1, font=('Times',10,'bold'),textvariable=P8,bd=10,insertwidth=2,bg="cyan",justify='right')
txt8.grid(row=2,column=3)

lbl9= Label(f1, font=('Times', 16, 'bold'),text="POCO F1",bd=16,bg="light green",anchor="w")
lbl9.grid(row=3, column=2)
txt9=Entry(f1, font=('Times',10,'bold'),textvariable=P9,bd=10,insertwidth=2,bg="cyan",justify='right')
txt9.grid(row=3,column=3)

lbl10= Label(f1, font=('Times', 16, 'bold'),text="Washing Machine",bd=16,bg="light green",anchor="w")
lbl10.grid(row=4, column=2)
txt10=Entry(f1, font=('Times',10,'bold'),textvariable=P10,bd=10,insertwidth=2,bg="cyan",justify='right')
txt10.grid(row=4,column=3)

lbl11= Label(f1, font=('Times', 16, 'bold'),text="Play Station 5",bd=16,bg="light green",anchor="w")
lbl11.grid(row=5, column=2)
txt11=Entry(f1, font=('Times',10,'bold'),textvariable=P11,bd=10,insertwidth=2,bg="cyan",justify='right')
txt11.grid(row=5,column=3)





lbl12= Label(f1, font=('Times', 16, 'bold'),text="Nike Shoes",bd=16,bg="light green",anchor="w")
lbl12.grid(row=0, column=4)
txt12=Entry(f1, font=('Times',10,'bold'),textvariable=P12,bd=10,insertwidth=2,bg="cyan",justify='right')
txt12.grid(row=0,column=5)

lbl13= Label(f1, font=('Times', 16, 'bold'),text="Jackets",bd=16,bg="light green",anchor="w")
lbl13.grid(row=1, column=4)
txt13=Entry(f1, font=('Times',10,'bold'),textvariable=P13,bd=10,insertwidth=2,bg="cyan",justify='right')
txt13.grid(row=1,column=5)

lbl14= Label(f1, font=('Times', 16, 'bold'),text="Wardrobes",bd=16,bg="light green",anchor="w")
lbl14.grid(row=2, column=4)
txt14=Entry(f1, font=('Times',10,'bold'),textvariable=P14,bd=10,insertwidth=2,bg="cyan",justify='right')
txt14.grid(row=2,column=5)

lbl15= Label(f1, font=('Times', 16, 'bold'),text="Sofa Beds",bd=16,bg="light green",anchor="w")
lbl15.grid(row=3, column=4)
txt15=Entry(f1, font=('arial',10,'bold'),textvariable=P15,bd=10,insertwidth=2,bg="cyan",justify='right')
txt15.grid(row=3,column=5)






lblCost= Label(f1, font=('Times', 16, 'bold'),text="COST ",bd=16,bg="light green",anchor="w")
lblCost.grid(row=6, column=0)
txtCost=Entry(f1, font=('Times',16,'bold'),textvariable=Cost,bd=10,insertwidth=2,bg="cyan",justify='right')
txtCost.grid(row=6,column=1)


lblStateTax= Label(f1, font=('Times', 16, 'bold'),text="GST",bd=16,bg="light green",anchor="w")
lblStateTax.grid(row=6, column=2)
txtStateTax=Entry(f1, font=('Times',16,'bold'),textvariable=Tax,bd=10,insertwidth=2,bg="cyan",justify='right')
txtStateTax.grid(row=6,column=3)



lblTotalCost= Label(f1, font=('Times', 16, 'bold'),text="TOTAL COST",bd=16,bg="light green",anchor="w")
lblTotalCost.grid(row=6, column=4)
txtTotalCost=Entry(f1, font=('Times',16,'bold'),textvariable=Total,bd=10,insertwidth=2,bg="cyan",justify='right')
txtTotalCost.grid(row=6,column=5)

btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('Times',16,'bold'),width=10,text="TOTAL",bg="goldenrod",command=Ref).grid(row=9,column=0,padx=5,pady=30)
btnTally=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('Times',16,'bold'),width=10,text="ADD TO CART",bg="goldenrod",command=database).grid(row=9,column=1,padx=5,pady=30)
btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('Times',16,'bold'),width=10,text="RESET",bg="goldenrod",command=Reset).grid(row=9,column=2,padx=5,pady=30)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('Times',16,'bold'),width=13,text="MOVE TO CART",bg="goldenrod",command=wish).grid(row=9,column=3,padx=5,pady=30)
btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('Times',16,'bold'),width=11,text="EXIT",bg="goldenrod",command=qExit).grid(row=9,column=4,padx=5,pady=30)

root.mainloop()
