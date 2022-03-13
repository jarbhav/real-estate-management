import tkinter as tk
import random
import tkinter.font as tkFont
import psycopg2
from login import *
from disp import *

root=tk.Tk()
root.geometry("900x800")

heading = tk.Label(root, text="Real Estate Database",fg = "red",bg = "light blue",font = "Helvetica 16 bold italic")
heading.place(relx = 0.5,rely = 0.03,anchor = 'center')

def register(uname):
    p_id = tk.Label(root, text = 'Property/Plot ID', font=('calibre',10, 'bold'))
    p_id_entry = tk.Entry(root, font=('calibre',10,'normal'))
  
    buy_rent = tk.Label(root, text = 'Type', font = ('calibre',10,'bold'))
    buy_rent_entry = tk.Entry(root, font = ('calibre',10,'normal'))

    R_for = tk.Label(root, text = 'Reg_For', font=('calibre',10, 'bold'))
    R_for_entry = tk.Entry(root, font=('calibre',10,'normal'))

    p_id.place(x=10,y=40)
    p_id_entry.place(x=80,y=40)
    buy_rent.place(x=10,y=60)
    buy_rent_entry.place(x=80,y=60)
    R_for.place(x=10,y=80)
    R_for_entry.place(x=80,y=80)

    GButton_ = tk.Button(root, text = 'Register', bg='blue',command=lambda: insertbuy(p_id_entry.get(), uname, buy_rent_entry.get(), R_for_entry.get()))
    GButton_.place(x=50,y=110)

# Display properties based on facilities

def facilities():
    Security = tk.StringVar()
    Gym = tk.StringVar()
    Pool = tk.StringVar()
    Plumber = tk.StringVar()
    Electrician = tk.StringVar()

    H2 = tk.Label(root, text="Filter Properties on the basis of Facilities",fg = "red", font=('Arial', 10, 'bold'))
    H2.place(x=50,y=140)

    R1 = tk.Radiobutton(root, text='Security' , variable=Security, value=True)
    R1.place(x=20,y=180)

    R2 = tk.Radiobutton(root, text='Gym' , variable=Gym, value=True)
    R2.place(x=80,y=180)

    R3 = tk.Radiobutton(root, text='Pool' , variable=Pool, value=True)
    R3.place(x=140,y=180)

    R4 = tk.Radiobutton(root, text='Plumber' , variable=Plumber, value=True)
    R4.place(x=220,y=180)

    R5 = tk.Radiobutton(root, text='Electrician' , variable=Electrician, value=True)
    R5.place(x=300,y=180)

    GButton_ = tk.Button(root, text = 'Display', bg='blue', command=lambda:facility_filter(Security.get(),Gym.get(),Pool.get(), Plumber.get(), Electrician.get()))
    GButton_.place(x=150,y=210)

    R1.deselect()
    R2.deselect()
    R3.deselect()
    R4.deselect()
    R5.deselect()

def disp_plpot_prop():
    H2 = tk.Label(root, text="Filter Property/Plot on basis of Price",fg = "red", font=('Arial', 10, 'bold'))
    H2.place(x=50,y=240)

    Plot = tk.StringVar()
    Property = tk.StringVar()
    asc = tk.StringVar()
    desc = tk.StringVar()

    R1 = tk.Radiobutton(root, text='Plot' , variable=Plot, value=1)
    R1.place(x=20,y=270)

    R2 = tk.Radiobutton(root, text='Property' , variable=Property, value=1)
    R2.place(x=80,y=270)

    R3 = tk.Radiobutton(root, text='Ascending' , variable=asc, value=1)
    R3.place(x=140,y=270)

    R4 = tk.Radiobutton(root, text='Descending' , variable=desc, value=1)
    R4.place(x=220,y=270)

    GButton_ = tk.Button(root, text = 'Display', bg='blue', command=lambda: filter_plot_prop(Plot.get(), Property.get(), asc.get(), desc.get()))
    GButton_.place(x=150,y=300)

def loc_price():
    H2 = tk.Label(root, text="Filter on Locality below given Price",fg = "red", font=('Arial', 10, 'bold'))
    H2.place(x=550,y=140)


    locality = tk.Label(root, text = 'Locality', font=('calibre',10, 'bold'))
    locality_entry = tk.Entry(root, font=('calibre',10,'normal'))

    price = tk.Label(root, text = 'Price', font=('calibre',10, 'bold'))
    price_entry = tk.Entry(root, font=('calibre',10,'normal'))

    locality.place(x=420,y=180)
    locality_entry.place(x=490,y=180)

    price.place(x=630,y=180)
    price_entry.place(x=680,y=180)

    GButton_ = tk.Button(root, text = 'Display', bg='blue', command=lambda: filter_price(locality_entry.get(), price_entry.get()))
    GButton_.place(x=620,y=210)

def avg_price_loc():
    H2 = tk.Label(root, text="Display Price Based on Locality having the requested facilities",fg = "red", font=('Arial', 10, 'bold'))
    H2.place(x=495,y=240)

    locality = tk.Label(root, text = 'Locality', font=('calibre',10, 'bold'))
    locality_entry = tk.Entry(root, font=('calibre',10,'normal'))

    locality.place(x=420,y=270)
    locality_entry.place(x=500,y=270)

    Security = tk.StringVar()
    Gym = tk.StringVar()
    Pool = tk.StringVar()
    Plumber = tk.StringVar()
    Electrician = tk.StringVar()

    facility = tk.Label(root, text = 'Facilities', font=('calibre',10, 'bold'))
    facility.place(x=420,y=300)

    R5 = tk.Radiobutton(root, text='Security' , variable=Security, value=1)
    R5.place(x=500,y=300)

    R1 = tk.Radiobutton(root, text='Gym' , variable=Gym, value=1)
    R1.place(x=580,y=300)

    R2 = tk.Radiobutton(root, text='Pool' , variable=Pool, value=1)
    R2.place(x=640,y=300)

    R3 = tk.Radiobutton(root, text='Plumber' , variable=Plumber, value=1)
    R3.place(x=720,y=300)

    R4 = tk.Radiobutton(root, text='Electrician' , variable=Electrician, value=1)
    R4.place(x=800,y=300)


    GButton_ = tk.Button(root, text = 'Display', bg='blue', command=lambda: price_loc_faci(Security.get(),Gym.get(),Pool.get(), Plumber.get(), Electrician.get(), locality_entry.get()))
    GButton_.place(x=620,y=330)

def rating():
    H2 = tk.Label(root, text="Property for rent under a certain cost and above a certain rating in a Locality",fg = "red", font=('Arial', 10, 'bold'))
    H2.place(x=50,y=360)

    locality = tk.Label(root, text = 'Locality', font=('calibre',10, 'bold'))
    locality_entry = tk.Entry(root, font=('calibre',10,'normal'))

    rent = tk.Label(root, text = 'Rent', font=('calibre',10, 'bold'))
    rent_entry = tk.Entry(root, font=('calibre',10,'normal'))

    rating = tk.Label(root, text = 'Rating', font=('calibre',10, 'bold'))
    rating_entry = tk.Entry(root, font=('calibre',10,'normal'))


    locality.place(x=20,y=390)
    locality_entry.place(x=80,y=390)
    rent.place(x=200,y=390)
    rent_entry.place(x=240,y=390)
    rating.place(x=380,y=390)
    rating_entry.place(x=420,y=390)

    GButton_ = tk.Button(root, text = 'Display', bg='blue',command = lambda:filter_prop_loc_rating(locality_entry.get(), rent_entry.get(), rating_entry.get()))
    GButton_.place(x=150,y=420)

def insert():
    H2 = tk.Label(root, text="Insert Prop/Plot for selling",fg = "red", font=('Arial', 10, 'bold'))
    H2.place(x=50,y=450)

    Prop_plot = tk.Label(root, text = 'Prop_plot', font=('calibre',10, 'bold'))
    Prop_plot_entry = tk.Entry(root, font=('calibre',10,'normal'))

    location = tk.Label(root, text = 'Location', font=('calibre',10, 'bold'))
    location_entry = tk.Entry(root, font=('calibre',10,'normal'))

    locality = tk.Label(root, text = 'Locality', font=('calibre',10, 'bold'))
    locality_entry = tk.Entry(root, font=('calibre',10,'normal'))

    area = tk.Label(root, text = 'Area', font=('calibre',10, 'bold'))
    area_entry = tk.Entry(root, font=('calibre',10,'normal'))

    ptype = tk.Label(root, text = 'Ptype', font=('calibre',10, 'bold'))
    ptype_entry = tk.Entry(root, font=('calibre',10,'normal'))

    price = tk.Label(root, text = 'Price', font=('calibre',10, 'bold'))
    price_entry = tk.Entry(root, font=('calibre',10,'normal'))

    #rent_buy = tk.Label(root, text = 'Rent/Buy', font=('calibre',10, 'bold'))
    #rent_buy_entry = tk.Entry(root, font=('calibre',10,'normal'))

    Prop_plot.place(x=20,y=480)
    Prop_plot_entry.place(x=100,y=480)    
    locality.place(x=220,y=480)
    locality_entry.place(x=300,y=480)  
    area.place(x=420,y=480)
    area_entry.place(x=460,y=480)
    location.place(x=600,y=480)
    location_entry.place(x=670,y=480)
    ptype.place(x=20,y=510)
    ptype_entry.place(x=80,y=510)
    price.place(x=220,y=510)
    price_entry.place(x=270,y=510)
    #rent_buy.place(x=390,y=510)
    #rent_buy_entry.place(x=480,y=510)

    GButton_ = tk.Button(root, text = 'Display', bg='blue', command=lambda:insertsell(Prop_plot_entry.get(), locality_entry.get(), location_entry.get(), area_entry.get(),ptype_entry.get(),price_entry.get()))
    GButton_.place(x=150,y=540)
    #lambda:filter_prop_loc_rating(Prop_plot_entry.get(), locality_entry.get(), area_entry.get(),location_entry.get(),ptype_entry.get(),price_entry.get(),rent_buy_entry.get()))

## Backend


def assign_tf(val):
    if val == '1':
        val = True
    else:
        val = False
    return val
# To Get the Property type, location, area and Name, Phone, Email of in charge of properties which have the facilities.
def facility_filter(Security,Gym,Pool, Plumber, Electrician):
    ps_connect = psycopg2.connect(user='postgres',password='postgres',host='127.0.0.1',port="5432",database='restate')
    cur = ps_connect.cursor()
    
    Security = assign_tf(Security)
    Gym = assign_tf(Gym)
    Pool = assign_tf(Pool)
    Plumber = assign_tf(Plumber)
    Electrician = assign_tf(Electrician)

    cur.execute(f"SELECT ptype, p_id, location, area, price FROM property AS P WHERE P.available=TRUE AND P.p_id IN ( SELECT p_id FROM facilities WHERE security={Security} AND gym={Gym} AND pool={Pool} AND plumber={Plumber} AND electrician={Electrician} )")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    '''
    Debugging Data
    print('--Selected Values--')
    print(Security,Gym,Pool, Plumber, Electrician)
    '''
    titles = ['Prop_type', 'P_ID', 'Location', 'Area', 'Price']
    display(rows,titles,len(rows))
    ps_connect.close()

# Display all the plots in ascending order of their price.
def filter_plot_prop(plot, prop, asc, desc):
    ps_connect = psycopg2.connect(user='postgres',password='postgres',host='127.0.0.1',port="5432",database='restate')
    cur = ps_connect.cursor()
    cur2 = ps_connect.cursor()
    if (plot == '1'):
        if (asc == '1'):    
            cur.execute("SELECT p_id, location, locality, area*costpersqft AS Price FROM PLOT WHERE available=TRUE ORDER BY Price ASC")
        if (desc == '1'):
            cur.execute("SELECT p_id, location, locality, area*costpersqft AS Price FROM PLOT WHERE available=TRUE ORDER BY Price DESC")
    if (prop == '1'):
        if (asc == '1'):    
            cur2.execute("SELECT p_id, location, locality, price FROM PROPERTY WHERE available=TRUE ORDER BY Price ASC")
        if (desc == '1'):
            cur2.execute("SELECT p_id, location, locality, price FROM PROPERTY WHERE available=TRUE ORDER BY Price DESC")

    titles = ['P_ID','Location','Locality','Price']
    rows = cur.fetchall()
    x=len(rows)
    for i in rows:
        print(i)
    #display(rows,titles)
    rows2 = cur2.fetchall()
    for i in rows2:
        rows.append(i)
    display(rows,titles,x)
    ps_connect.close()

# Display plot property in a locality under a certain price
def filter_price(loc, price):
    ps_connect = psycopg2.connect(user='postgres',password='postgres',host='127.0.0.1',port="5432",database='restate')
    cur1 = ps_connect.cursor()
    cur2 = ps_connect.cursor()

    cur1.execute(f"SELECT p_id, location, locality, area*costpersqft AS Price FROM PLOT WHERE available=TRUE AND area*costpersqft <= {price} AND locality={loc}")
    cur2.execute(f"SELECT p_id, location, locality, price FROM Property WHERE available=TRUE AND price <= {price} AND locality={loc}")
    titles = ['P_ID','Location','Locality','Price']
    rows = cur1.fetchall()
    x=len(rows)
    for i in rows:
        print(i)
    rows2 = cur2.fetchall()
    for i in rows2:
        rows.append(i)

    display(rows,titles,x)
    ps_connect.close()

# Price based on locality and facilities
def price_loc_faci(Security,Gym,Pool, Plumber, Electrician, locality):
    ps_connect = psycopg2.connect(user='postgres',password='postgres',host='127.0.0.1',port="5432",database='restate')
    cur = ps_connect.cursor()
    
    Security = assign_tf(Security)
    Gym = assign_tf(Gym)
    Pool = assign_tf(Pool)
    Plumber = assign_tf(Plumber)
    Electrician = assign_tf(Electrician)

    cur.execute(f"SELECT P.p_id, P.ptype, P.location, P.locality, P.price AS Price FROM property AS P WHERE locality={locality} AND P.available=TRUE AND P.p_id IN ( SELECT p_id FROM facilities WHERE security={Security} AND gym={Gym} AND pool={Pool} AND plumber={Plumber} AND electrician={Electrician} )")
    rows = cur.fetchall()
    titles = ['P_id','Propt_Type','Location','Locality','Price']
    for i in rows:
        print(i)
    display(rows,titles, len(rows))
    ps_connect.close()

# Display property for rent under a certain cost and above a certain rating in a locality
def filter_prop_loc_rating(loc, rent, rating):
    ps_connect = psycopg2.connect(user='postgres',password='postgres',host='127.0.0.1',port="5432",database='restate')
    cur1 = ps_connect.cursor()
    #cur2 = ps_connect.cursor()

    #cur1.execute(f"SELECT p_id, location, locality, area*costpersqft AS Price FROM PLOT, BUY WHERE p_id=plotid AND area*costpersqft <= {price} AND locality={loc}")

    cur1.execute(f"SELECT P.p_id, P.location, P.locality, R.cautiondeposit, R.rating, rent_per_month FROM PROPERTY AS P, RENT AS R WHERE P.p_id=R.p_id AND P.available=TRUE AND R.rent_per_month <= {rent} AND R.rating >= {rating} AND P.locality={loc}")
    rows = cur1.fetchall()
    for i in rows:
        print(i)
    titles={'P_Id','Location','Locality','Caut_Deposit','Rating','Rent'}
    display(rows, titles, len(rows))
    ps_connect.close()

#To insert into registration and other tables for buying only
def insertbuy(id, uname, r_type, rfor):
    ps_connect = psycopg2.connect(user='postgres',password='postgres',host='127.0.0.1',port="5432",database='restate')
    if r_type == 'PLOT':
        cursor1 = ps_connect.cursor()
        query1 = '''INSERT INTO PLOTREGISTRATION(id, rcustomer_id, rtype, rfor) VALUES (%s, %s, %s, %s)'''
        cursor1.execute(query1, (id, uname, r_type, rfor))
        curplot = ps_connect.cursor()
        #querypl = f"UPDATE PLOT SET Available=FALSE WHERE P_id={id}"
        curplot.execute(f"UPDATE PLOT SET Available=FALSE WHERE P_id={id}")
        print("Successfully bought")
    elif r_type == 'PROPERTY':
        cursor2 = ps_connect.cursor()
        query2 = '''INSERT INTO PROPREGISTRATION(id, rcustomer_id, rtype, rfor) VALUES (%s, %s, %s, %s)'''
        cursor2.execute(query2, (id, uname, r_type, rfor))
        curprop = ps_connect.cursor()
        #querypl = f"UPDATE PLOT SET Available=FALSE WHERE P_id={id}"
        curprop.execute(f"UPDATE PROPERTY SET Available=FALSE WHERE P_id={id}")
        print("Successfully bought")
    else:
        print("Invalid Values")

    ps_connect.commit()
    ps_connect.close()

#To insert into registration and other tables for selling
def insertsell(plot_prop, locality, location, area, ptype, price):
    available = 'TRUE'
    s_id = user_()
    ps_connect = psycopg2.connect(user='postgres',password='postgres',host='127.0.0.1',port="5432",database='restate')
    if plot_prop == 'PLOT':
        #p_id = random.randint(1000, 1500)
        tempcur = ps_connect.cursor()
        tempcur.execute("SELECT MAX(p_id) FROM PLOT")
        #print(tempcur.fetchall()[0][0])
        #print(type(tempcur.fetchall()))
        p_id = int(tempcur.fetchall()[0][0]) + 1
        print(p_id)
        cursor1 = ps_connect.cursor()
        query1 = '''INSERT INTO PLOT(p_id, s_id, location, locality, area, available, costpersqft) VALUES (%s, %s,%s, %s, %s, %s, %s)'''
        cursor1.execute(query1, (p_id,s_id, location, locality, area, available, price))
        print("Your entry has been recorded!")
    elif plot_prop == 'PROPERTY':
        #Assuming all advertised properties are for sale only
        #p_id = random.randint(1500, 2000)
        tempcur = ps_connect.cursor()
        tempcur.execute("SELECT MAX(p_id) FROM PROPERTY")
        p_id = int(tempcur.fetchall()[0][0]) + 1
        print(p_id)
        cursor2 = ps_connect.cursor()
        query2 = '''INSERT INTO PROPERTY(p_id, s_id, location, locality, area, available, ptype, price) VALUES (%s, %s,%s, %s, %s, %s, %s, %s)'''
        cursor2.execute(query2, (p_id,s_id, location, locality, area, available, ptype, price))
        faclticur = ps_connect.cursor()
        # Assuming every facility is available 
        faclticur.execute(f"INSERT INTO FACILITIES VALUES({p_id}, TRUE, TRUE, TRUE, TRUE, TRUE)")
        print("Your entry has been recorded!")
    else:
        print("Invalid Values")

    ps_connect.commit()
    ps_connect.close()

register(user_())
facilities()
disp_plpot_prop()
loc_price()
avg_price_loc()
rating()
insert()
root.mainloop()
