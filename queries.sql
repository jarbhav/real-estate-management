--1
    cur.execute(f"SELECT ptype, p_id, location, area, price FROM property AS P WHERE P.available=TRUE AND P.p_id IN ( SELECT p_id FROM facilities WHERE security={Security} AND gym={Gym} AND pool={Pool} AND plumber={Plumber} AND electrician={Electrician} )")
--2
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
--3
    cur1.execute(f"SELECT p_id, location, locality, area*costpersqft AS Price FROM PLOT WHERE available=TRUE AND area*costpersqft <= {price} AND locality={loc}")
    cur2.execute(f"SELECT p_id, location, locality, price FROM Property WHERE available=TRUE AND price <= {price} AND locality={loc}")
--4
    cur.execute(f"SELECT P.p_id, P.ptype, P.location, P.locality, P.price AS Price FROM property AS P WHERE locality={locality} AND P.available=TRUE AND P.p_id IN ( SELECT p_id FROM facilities WHERE security={Security} AND gym={Gym} AND pool={Pool} AND plumber={Plumber} AND electrician={Electrician} )")
--5
    cur1.execute(f"SELECT P.p_id, P.location, P.locality, R.cautiondeposit, R.rating, rent_per_month FROM PROPERTY AS P, RENT AS R WHERE P.p_id=R.p_id AND P.available=TRUE AND R.rent_per_month <= {rent} AND R.rating >= {rating} AND P.locality={loc}")
--6
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
--7
    if plot_prop == 'PLOT':
        p_id = random.randint(1000, 1500)
        cursor1 = ps_connect.cursor()
        query1 = '''INSERT INTO PLOT(p_id, s_id, location, locality, area, available, costpersqft) VALUES (%s, %s,%s, %s, %s, %s, %s)'''
        cursor1.execute(query1, (p_id,s_id, location, locality, area, available, price))
        print("Your entry has been recorded!")
    elif plot_prop == 'PROPERTY':
        #Assuming all advertised properties are for sale only
        p_id = random.randint(1500, 2000)
        cursor2 = ps_connect.cursor()
        query2 = '''INSERT INTO PROPERTY(p_id, s_id, location, locality, area, available, ptype, price) VALUES (%s, %s,%s, %s, %s, %s, %s, %s)'''
        cursor2.execute(query2, (p_id,s_id, location, locality, area, available, ptype, price))
        faclticur = ps_connect.cursor()
        # Assuming every facility is available 
        faclticur.execute(f"INSERT INTO FACILITIES VALUES({p_id}, TRUE, TRUE, TRUE, TRUE, TRUE)")
        print("Your entry has been recorded!")
    else:
        print("Invalid Values")


--complex
(select PR.rcustomer_id, SUM(P.area * P.costpersqft) FROM PLOT AS P, PLOTREGISTRATION AS PR WHERE P.p_id=PR.id GROUP BY PR.rcustomer_id) UNION (select PR.rcustomer_id, SUM(P.price) FROM PROPERTY AS P, PROPREGISTRATION AS PR WHERE P.p_id=PR.id GROUP BY PR.rcustomer_id);

--Getting a summary of how much each customer has spent in total
CREATE TEMP VIEW summary AS 
    (select PR.rcustomer_id, SUM(P.area * P.costpersqft) FROM PLOT AS P, PLOTREGISTRATION AS PR WHERE P.p_id=PR.id GROUP BY PR.rcustomer_id) 
    UNION 
    (select PR.rcustomer_id, SUM(P.price) FROM PROPERTY AS P, PROPREGISTRATION AS PR WHERE P.p_id=PR.id GROUP BY PR.rcustomer_id);
select rcustomer_id, SUM(sum) AS Total FROM summary GROUP BY rcustomer_id;