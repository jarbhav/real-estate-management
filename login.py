from tkinter import *

import psycopg2
#defining login function

def login():
    #getting form data
    global uname
    uname=username.get()
    pwd=password.get()
    #applying empty validation
    ps_connect = psycopg2.connect(user='postgres',password='postgres',host='127.0.0.1',port="5432",database='restate')
    cur = ps_connect.cursor()
    cur.execute("select * from login")
    rows = cur.fetchall()
    for i in rows:
        if(i[0]==uname and i[1]==pwd):
            print("Login Successful")
            print(f"You are logged in as {uname}")
            break
    login_screen.destroy()
    ps_connect.close()
    return uname

def user_():
    return uname
#defining loginform function
def Loginform():
    global login_screen
    login_screen = Tk()
    #Setting title of screen
    login_screen.title("Login Form")
    #setting height and width of screen
    login_screen.geometry("300x250")
    #declaring variable
    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Creating layout of login form
    Label(login_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    #Username Label
    Label(login_screen, text="Username * ").place(x=20,y=40)
    #Username textbox
    Entry(login_screen, textvariable=username).place(x=90,y=42)
    #Password Label
    Label(login_screen, text="Password * ").place(x=20,y=80)
    #Password textbox
    Entry(login_screen, textvariable=password ,show="*").place(x=90,y=82)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message).place(x=95,y=100)
    #Login button
    Button(login_screen, text="Login", width=10, height=1, bg="orange",command=login).place(x=105,y=130)
    login_screen.mainloop()
#calling function Loginform
Loginform()