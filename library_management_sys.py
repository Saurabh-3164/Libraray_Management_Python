# from asyncio.windows_events import NULL
from distutils.cmd import Command
from operator import le
from tkinter import *
from tkinter import ttk
from turtle import bgcolor
from PIL import Image,ImageTk
import mysql.connector as c
import tkinter.messagebox as tmsg
import string 
con=c.connect(host="Localhost",user="root",passwd="Cammilt@10",database="login")
def Returnn():
    Return=Toplevel(options)
    def search():
        cursor=con.cursor()
        query2="select * from books"
        cursor.execute(query2)
        data=cursor.fetchall()
        l1=[]
        for i in range(len(data)):
            for j in range(1):
                l1.append(data[i][0])
        if Return_bid_val.get() in l1:
            issu_query=f"update books set statuss ='availble' where id_no={Return_bid_val.get()}"
            cursor.execute(issu_query)
            con.commit()
            tmsg.showinfo("Message","Thank you for returning")
            Return.destroy()
        else:
            tmsg.showwarning("Warning","Galat ID daal diya be chal firse daal")
    Return.title("Library Management System - login/register-Options-Return")
    Return.geometry("765x700")
    Return.configure(background="tan")
    Return_bid_val=IntVar()
    Label(Return,text="Return Book",font="lucida 20 bold",bg="navy blue",fg="white",border=7,relief=SUNKEN).place(relx=0.3,rely=0.1)
    Label(Return,text="Enter Book ID",bg="grey",border=5,relief=GROOVE).place(relx=0.3,rely=0.2)
    Entry(Return,textvariable=Return_bid_val,bg="white",border=2,relief=GROOVE).place(relx=0.5,rely=0.2,height=30,width=100)
    Button(Return,text="Submit",font="lucida 10 bold",border=3,relief=GROOVE,bg="grey",command=search).place(relx=0.5,rely=0.3)
    Return.mainloop()
def Issue():
    issue=Toplevel(options)
    def search():
        cursor=con.cursor()
        query2="select * from books"
        cursor.execute(query2)
        data=cursor.fetchall()
        l1=[]
        for i in range(len(data)):
            for j in range(1):
                l1.append(data[i][0])
        if  issue_bid_val.get() in l1:
            issu_query=f"update books set statuss ='unavailble' where id_no={issue_bid_val.get()}"
            cursor.execute(issu_query)
            con.commit()
            tmsg.showinfo("Issue","Succesfully Issued! It is not be delivered to your home😂")
            issue.destroy()
        else:
            tmsg.showwarning("Warning","Galat ID daal diya be chal firse daal")
    issue.title("Library Management System - login/register-Options-Issue")
    issue.geometry("765x700")
    issue.configure(background="tan")
    issue_bid_val=IntVar()
    Label(issue,text="Issue Book",font="lucida 20 bold",bg="navy blue",fg="white",border=7,relief=SUNKEN).place(relx=0.3,rely=0.1)
    Label(issue,text="Enter Book ID",bg="grey",border=5,relief=GROOVE).place(relx=0.3,rely=0.2)
    Entry(issue,textvariable=issue_bid_val,bg="white",border=2,relief=GROOVE).place(relx=0.5,rely=0.2,height=30,width=100)
    Button(issue,text="Submit",font="lucida 10 bold",border=3,relief=GROOVE,bg="grey",command=search).place(relx=0.5,rely=0.3)
    issue.mainloop()
# Issue()
def Add():
    add=Toplevel(options)
    def add_book():
        if str(book_id_val.get()) and book_nameval.get() and authorval.get()!="":
            cursor=con.cursor()
            add_query="insert into "+'books'+" values ('"+str(book_id_val.get())+"','"+str(book_nameval.get())+"','"+authorval.get()+"','available')"
            cursor.execute(add_query)
            con.commit()
            add.destroy()
        else:
            tmsg.showwarning("warning","please fill the boxes")
    add.title("Library Management System - login/register-Options-Add a book")
    add.geometry("765x700")
    add.configure(background="brown")
    Label(add,text="Add a Book",font="lucida 20 bold",bg="green",fg="white",border=7,relief=SUNKEN).place(relx=0.3,rely=0.1)
    Label(add,text="Enter Book Name",bg="grey",border=5,relief=GROOVE).place(relx=0.3,rely=0.2)
    Label(add,text="Enter Author Name",bg="grey",border=5,relief=GROOVE).place(relx=0.3,rely=0.3)
    Label(add,text="Enter Book ID",bg="grey",border=5,relief=GROOVE).place(relx=0.3,rely=0.4)
    book_nameval=StringVar()
    authorval=StringVar()
    book_id_val=IntVar()
    Entry(add,textvariable=book_nameval,bg="white",border=2,relief=GROOVE).place(relx=0.5,rely=0.2,height=30,width=100)
    Entry(add,textvariable=authorval,bg="white",border=2,relief=GROOVE).place(relx=0.5,rely=0.3,height=30,width=100)
    Entry(add,textvariable=book_id_val,bg="white",border=2,relief=GROOVE).place(relx=0.5,rely=0.4,height=30,width=100)
    Button(add,text="Submit",font="lucida 10 bold",border=3,relief=GROOVE,bg="grey",command=add_book).place(relx=0.5,rely=0.5)
    add.mainloop()

def view():
    views=Toplevel(options)
    def Quit():
        views.destroy()
    views.title("Library Management System - login/register-Options")
    views.geometry("765x700")
    views.configure(background="grey")
    Label(views,text="Available books",border=20,bg="black",fg="white",relief=SUNKEN,font="lucida 10 bold").place(relx=0.3,rely=0.0,height=90,width=450)
    cursor=con.cursor()
    view_query="select * from books"
    cursor.execute(view_query)
    data=cursor.fetchall()
    x=0.3
    y=0.3
    view_f=Frame(views,bg="black").place(relx=0.3,rely=0.2,height=800,width=800)
    Label(views,text="BID",bg="black",fg="white",font="lucida 15 bold").place(relx=0.4,rely=0.2)
    Label(views,text="---------------------------------------------------------------------------------------------------------------------------------------------------------------",bg="black",fg="white").place(relx=0.3,rely=0.3)
    Label(views,text="Book name",bg="black",fg="white",font="lucida 15 bold").place(relx=0.5,rely=0.2)
    Label(views,text="Author",bg="black",fg="white",font="lucida 15 bold").place(relx=0.6,rely=0.2)
    Label(views,text="status",bg="black",fg="white",font="lucida 15 bold").place(relx=0.7,rely=0.2)
    for i in range(len(data)):
        y=y+0.1
        for j in range(4):
            x=x+0.1
            Label(views,text=data[i][j],bg="black",fg="white",font="lucida 10 bold").place(relx=x,rely=y)
        x=0.3
    Button(views,text="Quit",font="lucida 10 bold",command=Quit).place(relx=0.9,rely=0.6,height=30,width=40)
    views.mainloop()
def options():
    global options
    options=Toplevel(login_reg)
    options.title("Library Management System - login/register-Options")
    options.geometry("765x700")
    options.configure(background="grey")
    Label(options,text="You have following options",border=20,bg="black",fg="white",relief=SUNKEN,font="lucida 10 bold").place(relx=0.3,rely=0.0,height=70,width=400)
    view_button=Button(options,text="Views books",border=3,bg="green",fg="white",relief=SUNKEN,font="lucida 10 bold",command=view).place(relx=0.4,rely=0.2,height=50,width=150)
    add_button=Button(options,text="Add books",border=3,bg="green",fg="white",relief=SUNKEN,font="lucida 10 bold",command=Add).place(relx=0.4,rely=0.3,height=50,width=150)
    issue_button=Button(options,text="Issue book",border=3,bg="green",fg="white",relief=SUNKEN,font="lucida 10 bold",command=Issue).place(relx=0.4,rely=0.4,height=50,width=150)
    return_button=Button(options,text="Return books",border=3,bg="green",fg="white",relief=SUNKEN,font="lucida 10 bold",command=Returnn).place(relx=0.4,rely=0.5,height=50,width=150)

    options.mainloop()
def log_reg1():
    global login_reg
    login_reg=Toplevel(root)
    def reg_submit():
        try:
            len_pass=len(passval.get())
            len_phone=len(str(no_val.get()))
            if len_pass<6:
                tmsg.showwarning("Warning","password must not be less than 6 characters")
                login_reg.destroy()
            elif len_phone!=10:
                tmsg.showwarning("Warning","length of phone no must be 10 number")
                login_reg.destroy()
            else:
                cursor =con.cursor()
                query1="insert into "+'login_user1(pasword,mobile_no)'+" values ('"+passval.get()+"','"+str(no_val.get())+"')"
                cursor.execute(query1)
                con.commit()
                query2="select * from login_user1"
                cursor.execute(query2)
                data=cursor.fetchall()
                l=[]
                for i in range(len(data)):
                    l.append(data[i][0])
                tmsg.showinfo("submittion status",f"succesfully submitted \n please note your id no. \n id no. is {l[-1]}")
                login_reg.destroy()
        except:
            Label(login_reg,text="An error occured! \n click to close button and please try again......",fg="red",bg="powder blue").place(relx=0.2,rely=0.5)
    def log_submit():
        len_pass=len(passval.get())
        len_phone=len(str(no_val.get()))
        cursor=con.cursor()
        query2="select * from login_user1"
        cursor.execute(query2)
        data=cursor.fetchall()
        l1=[]
        l2=[]
        for i in range(len(data)):
            for j in range(1):
                l1.append(data[i][j])
                l2.append(data[i][j+1])
        d=0
        for i in range(len(l1)):
            if l1[i]==int(ad_idval.get()) and l2[i]==str(ad_passval.get()):
                d=1
                # options()
                break
        # print(i)
        if(d==0):
            tmsg.showwarning("Warning  ","you have filled wrong information...........please login again")
            login_reg.destroy()
        else:
            options()
    login_reg.title("Library Management System - login/register")
    login_reg.geometry("765x700")
    login_reg.configure(background="skyblue")
    reg_user=Label(login_reg,text="Register as user",font="lucida 10 bold",bg="powder blue",border=3,relief=GROOVE)
    reg_user.place(relx=0.0,rely=0.1,height=30,width=250)
    passval=StringVar()
    no_val=IntVar()
    ad_idval=IntVar()
    ad_passval=StringVar()
    Label(login_reg,text="create password",font="lucida 10 bold",bg="powder blue",border=3,relief=GROOVE).place(relx=0.0,rely=0.2,height=30,width=130)
    reg_u_e=Entry(login_reg,textvariable=passval)
    reg_u_e.place(relx=0.1,rely=0.2,height=30,width=150)
    Label(login_reg,text="Mobile No",font="lucida 10 bold",bg="powder blue",border=3,relief=GROOVE).place(relx=0.0,rely=0.3,height=30,width=100)
    reg_u_ew=Entry(login_reg,textvariable=no_val,border=3,relief=SUNKEN)
    reg_u_ew.place(relx=0.1,rely=0.3,height=30,width=150)
    Button(login_reg,text="submit",font="lucida 10 bold",border=3,relief=GROOVE,bg="grey",command=reg_submit).place(relx=0.1,rely=0.4,height=40,width=100)
    log_user=Label(login_reg,text="login as user",font="lucida 10 bold",bg="powder blue",border=3,relief=GROOVE)
    log_user.place(relx=0.1,rely=0.6,height=30,width=250)
    Label(login_reg,text="Enter Id No.",font="lucida 10 bold",bg="powder blue",border=3,relief=GROOVE).place(relx=0.0,rely=0.7,height=30,width=130)
    log_u_e=Entry(login_reg,textvariable=ad_idval)
    log_u_e.place(relx=0.1,rely=0.7,height=30,width=150)
    Label(login_reg,text="Enter Password",font="lucida 10 bold",bg="powder blue",border=3,relief=GROOVE).place(relx=0.0,rely=0.8,height=30,width=100)
    log_u_ew=Entry(login_reg,textvariable=ad_passval,border=3,relief=SUNKEN,show="*")
    log_u_ew.place(relx=0.1,rely=0.8,height=30,width=150)
    Button(login_reg,text="submit",font="lucida 10 bold",border=3,relief=GROOVE,bg="grey",command=log_submit).place(relx=0.1,rely=0.9,height=40,width=100)
    login_reg.mainloop()
# root=Tk()

def main():
    global root
    root=Tk()
    def show_user():
        if  ad_logval.get()=="Saurabh@10":
            show=Tk()
            def Quit():
                show.destroy()
            show.title("Library Management System - Admin Access")
            show.geometry("765x700")
            show.configure(background="skyblue")
            cursor=con.cursor()
            query2="select * from login_user1"
            cursor.execute(query2)
            data=cursor.fetchall()
            l1=[]
            x=0.3
            y=0.3
            view_f=Frame(show,bg="black").place(relx=0.3,rely=0.2,height=800,width=800)
                # Label(show,text="BID",bg="black",fg="white",font="lucida 15 bold").place(relx=0.4,rely=0.2)
                # Label(showtext="---------------------------------------------------------------------------------------------------------------------------------------------------------------",bg="black",fg="white").place(relx=0.3,rely=0.3)
            Label(show,text="ID NO",bg="black",fg="white",font="lucida 15 bold").place(relx=0.4,rely=0.2)
            Label(show,text="Mobile no",bg="black",fg="white",font="lucida 15 bold").place(relx=0.6,rely=0.2)
            for i in range(len(data)):
                y=y+0.1
                for j in range(3):
                    x=x+0.1             
                    if j==1:
                        continue
                    else:
                        Label(show,text=data[i][j],bg="black",fg="white",font="lucida 10 bold").place(relx=x,rely=y)
                x=0.3
            Button(show,text="Quit",font="lucida 10 bold",command=Quit).place(relx=0.9,rely=0.6,height=30,width=40)
        else:
            tmsg.showwarning("Warning","wrong Password")
    def log_reg():
        log_reg1()
    root.title("Library Management System")
    p1=PhotoImage(file="library-icon.png")
    root.iconphoto(False,p1)
    root.geometry("765x600")
    root.configure(background="skyblue")
    image=Image.open("library image.jpg")
    image=image.resize((1400,2050))
    photo=ImageTk.PhotoImage(image)
    label=Label(image=photo)
    label.place(relx=0.0,rely=-1.02,height=1400,width=2050)
    mainmenu=Menu(root,background="red")
    m1=Menu(mainmenu,tearoff=0)
    mainmenu.add_command(label="Help",font="lucida 19 bold")
    mainmenu.add_command(label="About us",font="lucida 19 bold")
    root.config(menu=mainmenu)
    Label(text="👨‍🏫",fg="green",bg="powder blue",font="lucida 30 bold").place(relx=0.3,rely=0.1,height=100,width=570)
    log_user=Label(root,text=" click here for Login/register as User",font="lucida 10 bold",border=3,relief=GROOVE)
    log_user.place(relx=0.0,rely=0.0,height=40,width=250)
    Button(root,text="Login/Register",font="lucida 10 bold",border=1,relief=GROOVE,command=log_reg1).place(relx=0.0,rely=0.1,height=50,width=150)
    Label(text="Welcome to Tripathi Library",fg="green",bg="powder blue",font="lucida 30 bold").place(relx=0.3,rely=0.2,height=100,width=570)
    log_admin=Label(root,text="Login as Admin",font="lucida 10 bold",border=3,relief=GROOVE)
    log_admin.place(relx=0.0,rely=0.3,height=40,width=250)
    ad_logval=StringVar()
    Entry(root,textvariable=ad_logval,relief=GROOVE,show="*").place(relx=0.1,rely=0.4,height=40,width=150)
    Label(root,text="Enter Password",font="lucida 10 bold",border=3,relief=SUNKEN).place(relx=0.0,rely=0.4,height=40,width=150)
    Button(root,text="Submit",font="lucida 10 bold",border=3,relief=SUNKEN,command=show_user).place(relx=0.0,rely=0.5,height=40,width=150)
    Label(root,text="Location - Golden Jublie Boys Hostel Balrampur",bg="black",fg="white").place(relx=0.0,rely=0.8,height=40,width=450)
    Label(root,text="contact us - +918738091695/+917317572015",bg="black",fg="white").place(relx=0.0,rely=0.9,height=40,width=450)
    root.mainloop()
main()
# log_reg1()
# options()
# Add()
# view()