import tkinter as tk
#from backend import *
import tkinter.font as tkFont
import psycopg2

def display(rows,titles,l):
    
    window=tk.Tk()
    window.geometry("1200x200")
    total_rows = len(rows)
    total_columns = len(titles)
    
    def table(listbox):
        x=0
        for i in range(0,total_rows):
            for j in range(total_columns):
                if(i==l and x==0):
                    e = tk.Label(listbox, width=10, fg='#e27013',font=('Arial', 10, 'bold'), text='Property', borderwidth=1, relief="groove")
                    e.grid(row=i+1, column=j)
                    x+=1
                e = tk.Label(listbox, width=20, fg='#3d8f17',
                          font=('Arial', 10, 'bold'), text=rows[i][j], borderwidth=1, relief="groove")
                e.grid(row=i+1+x, column=j)

    #rows = cursor.fetchall()

    listbox = tk.Listbox(window, width=20, height=3)
    listbox["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=12)
    listbox["font"] = ft
    listbox["fg"] = "#000"
    listbox["justify"] = "center"
    listbox.place(x=20, y=20, width=1200, height=200)
    #header=['Prop_type', 'P_ID', 'LOcation', 'Area', 'INcharge_Name','Phone_NO']
    header = []
    for i in titles:
        header.append(i)
    for k in range(len(header)):
        e = tk.Label(listbox, width=10, fg='#e27013',font=('Arial', 10, 'bold'), text=header[k], borderwidth=1, relief="groove")
        e.grid(row=0, column=k)
    table(listbox)
    window.mainloop()