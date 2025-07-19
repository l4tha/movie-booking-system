import mysql.connector
import random
conn=mysql.connector.connect(host="localhost",username="root",password="baheakai")
my_cursor=conn.cursor()
my_cursor.execute("drop database if exists movie_ticket1")
my_cursor.execute("create database movie_ticket1")
my_cursor.execute("use movie_ticket1")


my_cursor.execute('''create table movies1 (sno int primary key not null auto_increment,
                  MOVIES varchar(58),
                  AUDI varchar(100),
                  DATE varchar(20),
                  TIMING varchar(78),
                  PRICE int)''')
my_cursor.execute('''INSERT INTO movies1 VALUES(1,"LEO","2","19 OCT","|4:20am|",200),
                  (2,"JAPPAN","1","12 NOV","|9:30am|",190),
                  (3,"PS2","2","2 OCT","|9:30am|",230),
                  (4,"JAILER","4","14 NOV","|6:30am|",190),
                  (5,"VAATHI","1","30 OCT","|8:15am|",180),
                  (6,"VIKRAM","2","12 NOV","|4:30am|",220),
                  (7,"VINNAITHANDHI VARUVAIYA","3","23 OCT","|5:15am|",200)''')
my_cursor.execute('''create table tickets1 ( name varchar(10),
                  MOVIES varchar(58),
                  AUDI varchar(100),
                  DATE varchar(20),
                  TIMING varchar(78),
                  PRICE int,
                  seatnum int)''')

conn.commit()




print("\n########## NSN PRODUCTIONS ##########")
print("\n ********** VANAKAM TO PALAZZO TICKET BOOKING SYSTEM !! **********")
acc=input("\n DO YOU HAVE A ACCOUNT (Y/N)")
em=[]
if acc=="y" or acc=="yes"or acc=="YES":
    email=input("email id :")
    em.append(email)
    pw=input("\n ENTER YOUR PASSWORD:")
    otp=int(input("\nENTER A OTP CODE ON YOUR EMAIL AND PHONE NO:"))
    print("\n Hurray! login successfull")
else:
    nam=input("\n ENTER YOUR NAME:")
    pn=int(input("\nENTER YOUR PHONE NUMBER:"))
    city=input("\nENTER CITY:")
    state=input("\nENTER STATE:")
    em=(input("\n ENTER YOUR EMAIL ID:"))
    pw=input("\nENTER PASSWORD:")
    print(f"\n otp send to {pn} and {em}")
    otp=int(input("\nENTER THE OTP NO:"))
    print("\n ---------YOUR ACCOUNT IS CREATED SUCCESSFULLY--------")
print("\n THESE ARE THE LATEST MOVIES")
query1="select MOVIES,DATE,TIMING,PRICE from movies1"
my_cursor.execute(query1)
for a in my_cursor:
    print(a)
name=[]
mname=input("\n Which movie you want to watch?")
tik=int(input("\n Enter number of tickets you want:"))
if tik>10:
    print("Maximum ticket that can be booked at once is 10, TRY again!")
    exit()
for b in range(tik):
    nam=input("\n ENTER NAME:")
    if nam=='':
        print("please enter the name of the customer.TRY gain from the first!:")
        exit()
    else:
        name.append(nam)
audi=[]
date=[]
timing=[]
price=[]
query2="select AUDI from movies1 where movies='{}'".format(mname)
my_cursor.execute(query2)
for c in my_cursor:
        audi.append(c)
query3="select DATE from movies1 where movies='{}'".format(mname)
my_cursor.execute(query3)
for d in my_cursor:
    date.append(d)
query4="select TIMING from movies1 where movies='{}'".format(mname)
my_cursor.execute(query4)
for e in my_cursor:
    timing.append(e)
query5="select PRICE *{} from movies1 where movies='{}'".format(tik,mname)
my_cursor.execute(query5)
for f in my_cursor:
    price.append(f)

seatnum=random.randint(1,200)
print(f"YOU HAVE TO PAY {price} RUPEES")
pay=input("enter (P) to pay:")

print("\nYour ticket is here:")
my_cursor.execute("insert into tickets1 values (%s, %s, %s, %s, %s, %s, %s);", (str(name[0]), str(mname), str(audi[0]), str(date[0]), str(timing[0]), int(price[0][0]), seatnum))
conn.commit()
if tik==1:
    print(f"\nNAME={name}     MOVIE NAME={mname}   AUDI={audi}")
    print(f"TIMING={timing}   DATE={date}          PRICE={price}     ")
    print(f"SEAT NUMBER={seatnum}")
    print(f"Your ticket has been send to your mail {em}")

if tik>1:
    print(f"\nNAME={name}     MOVIE NAME={mname}   AUDI={audi}")
    print(f"TIMING={timing}   DATE={date}          PRICE={price}     ")
    print(f"SEAT NUMBER={seatnum} to {seatnum+(tik-1)}")
    print(f"Your ticket has been send to your mail {em}")
    print(" THANK YEWW FOR CHOOSING PALAZZO!!")
conn.close()










    
           
    

