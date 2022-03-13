\c restate;

INSERT into CUSTOMER values('sumit11','Sumit','Kumar','1988-01-21','M','1111111111','sumit@gmail.com','Dwarka Nagar');
INSERT into CUSTOMER values('mahesh22','Mahesh','Singh', '1981-02-22','M','222222222','sumit@gmail.com','Rajarajeshwari Nagar');
INSERT into CUSTOMER values('rohit33','Rohit','Pratap', '1991-03-21','M','333333333','sumit@gmail.com','JP Nagar 1st street');
INSERT into CUSTOMER values('shivam44','Shivam','Singh', '1975-01-21','M','444444444','sumit@gmail.com','Church Street');
INSERT into CUSTOMER values('piyush55','Piyush','Pushkar','1997-04-07','M','5555555555','sumit@gmail.com','MG Road');
INSERT into CUSTOMER values('aryan66','Aryan','Raj','1995-01-29','M','6666666666','sumit@gmail.com','Hosarkerehalli');
INSERT into CUSTOMER values('archit77','Archit','Raj','1996-07-22','M','7777777777','sumit@gmail.com','Kormangla');
INSERT into CUSTOMER values('tejasva88','Tejasva','Singh','1978-05-21','M','8888888888','sumit@gmail.com','Jay Nagar');

INSERT into PLOT values(2,'sumit11', 'Electronic City Phase II','Near Pes College',3000, FALSE, 10000);
INSERT into PLOT values(3,'sumit11', 'Chikka Tirupathi','Near Temple',2600, FALSE, 11000);
INSERT into PLOT values(5,'rohit33', 'Uttarahalli','Near Highway',3600, FALSE, 8000);
INSERT into PLOT values(8,'rohit33', 'Lingadheeranahalli','Near Highway',6000, TRUE, 12000);
INSERT into PLOT values(13,'aryan66', 'Kothanur','Outskirts of city',6000, TRUE, 12000);
INSERT into PLOT values(21,'aryan66', 'Gandhi Bazar','Outskirts of city',2020, TRUE, 12000);
INSERT into PLOT values(34,'archit77','Whitefield','Behind School',1500, TRUE, 8000);
INSERT into PLOT values(56,'archit77','Thanisandra','Behind School',1600, TRUE, 9000);

INSERT into PROPERTY values(101,'shivam44','Rajaji Nagar','Society',3300, TRUE, 'HOME', 100000);
INSERT into PROPERTY values(102,'shivam44','Marathahalli','Outside City',1140, FALSE, 'HOME', 200000);
INSERT into PROPERTY values(103,'shivam44','Whitefield','Near Higway',1800, TRUE, '2BHK', 100000);
INSERT into PROPERTY values(104,'piyush55','7th Phase JP Nagar','Behind School',1000, TRUE, '3BHK', 300000);
INSERT into PROPERTY values(105,'piyush55','Mysore Road','Near Higway',1140, FALSE, '4BHK', 500000);
INSERT into PROPERTY values(106,'piyush55','Raja Rajeshwari Nagar','Near Pes College',1540, TRUE, 'Mall', 1000000);
INSERT into PROPERTY values(107,'tejasva88','Kormangla','Behind Pub',2000, TRUE, 'Shop', 10000);
INSERT into PROPERTY values(108,'tejasva88','Jay Nagar','Behind School',1600, TRUE, 'Commercial Space', 100000);

INSERT into FACILITIES values(101,TRUE,TRUE,TRUE,TRUE,TRUE);
INSERT into FACILITIES values(102,TRUE,TRUE,FALSE,TRUE,FALSE);
INSERT into FACILITIES values(103,TRUE,FALSE,FALSE,FALSE,FALSE);
INSERT into FACILITIES values(104,FALSE,FALSE,FALSE,FALSE,FALSE);
INSERT into FACILITIES values(105,TRUE,FALSE,FALSE,TRUE,TRUE);
INSERT into FACILITIES values(106,TRUE,FALSE,FALSE,TRUE,TRUE);
INSERT into FACILITIES values(107,TRUE,TRUE,TRUE,TRUE,TRUE);
INSERT into FACILITIES values(108,TRUE,FALSE,TRUE,FALSE,TRUE);


INSERT into PLOTREGISTRATION values(2,'sumit11','PLOT','BUY');
INSERT into PLOTREGISTRATION values(3,'mahesh22','PLOT','BUY');
INSERT into PLOTREGISTRATION values(5,'rohit33','PLOT','BUY');

INSERT into PROPREGISTRATION values(102,'shivam44','PROPERTY','RENT');
INSERT into PROPREGISTRATION values(105,'piyush55','PROPERTY','BUY');


INSERT into RENT values(101,20000,8,100000);
INSERT into RENT values(102,15000,7,80000);
INSERT into RENT values(103,21000,9,110000);
INSERT into RENT values(104,11000,8,70000);
INSERT into RENT values(105,22000,8,110000);


INSERT INTO LOGIN VALUES('sumit11','sumit');
INSERT INTO LOGIN VALUES('mahesh22','mahesh');
INSERT INTO LOGIN VALUES('rohit33','Rohit');
INSERT INTO LOGIN VALUES('shivam44','Shivam');
INSERT INTO LOGIN VALUES('piyush55','Piyush');
INSERT INTO LOGIN VALUES('aryan66','Aryan');
INSERT INTO LOGIN VALUES('archit77','Archit');
INSERT INTO LOGIN VALUES('tejasva88','Tejasva');

--ALTER TABLE BUY ADD CONSTRAINT prop_key2 FOREIGN KEY (PropID) REFERENCES PROPERTY(P_id) ON DELETE SET NULL;
--ALTER TABLE BUY ADD CONSTRAINT plot_key2 FOREIGN KEY (PlotID) REFERENCES PLOT(P_id) ON DELETE SET NULL; 