import mysql.connector,emoji
import random,webbrowser
#from booking import *



mydb = mysql.connector.connect(host="localhost",user="root",passwd="password",database="Transport_db")



mycursor = mydb.cursor()



#mycursor.execute("create database Transport_db")
#mycursor.execute("show databases")

#mycursor.execute("create table User(User_id varchar(20) not null,User_name char(20),Gender char, Age int,primary key(User_id))")
#mycursor.execute("create table bus(Bus_no varchar(20) ,bus_name char(20),primary key(Bus_no))")
#ycursor.execute("create table Booking(booking_id int ,User_id varchar(20), User_name char(20),Source char(20),Destn char(20),bus_no varchar(20), primary key(booking_id))")


sqlform = "insert into User(User_id,User_name,Gender,Age) values(%s,%s,%s,%s)"

sqlform2 = "insert into bus(Bus_no,bus_name) values(%s,%s)"
sqlform3 = "insert into Booking(booking_id,User_id,User_name,Source,Destn,bus_no) values(%s,%s,%s,%s,%s,%s)"

#value = ("MB6141CE","Mumbai")

#webbrowser.open('http://www.python.org') 



#mycursor.execute(sqlform2,value)



#uservalue1 = ("101","afra","F",20)
#uservalue3 = ("Bee_Nawabi","Hyderabad")
#mycursor.execute(sqlform,uservalue)
#mycursor.execute(sqlform2, uservalue3)
#mydb.commit()


user_id=102

#add new column from command line bus_destn fill in values respectively


def Booking(val): 
    print("\n\n------------------ Welcome to Booking Section --------------------------------\n")
    sql = "select User_id from User where User_name = %s"
    addr = (val,)
    mycursor.execute(sql,addr)
    result = mycursor.fetchone()
    userid = result[0]
    source = input("\nEnter the Boarding place/Source : ")
    option = int(input("\nSelect Option 1 for Inter-State Travel       ||       Select Option 2 for Outer-State Travel : \nOption : "))
    if(option == 1):
        option2 = int(input("\n\n01-Gulbarga \t| 02-Shivamogga \t| 03-Mangalore  \t| 04-Mysore\n\nPlease Select Any one from 01,02,03 or 04 : "))
        list1=['Gulbarga','Shivamogga','Mangalore','Mysore']
        destination = list1[option2-1]
        sql2 = "select Bus_no from bus where bus_name = %s"
        addr2 = (destination,)
        mycursor.execute(sql2,addr2)
        result2 = mycursor.fetchone()
      
    if(option == 2):
        option3 = int(input("05 - Hyderabad \t| 06 - New_Delhi  \t| 07 - Agra   \t| 08 - Mumbai  \n\nPlease Select Any one from 05,06,07 or 08 : "))
        list2=['Hyderabad','New_Delhi','Agra','Mumbai']
        destn = list2[option3-5]
        sql3 = "select Bus_no from bus where bus_name = %s"
        addr3 = (destn,)
        mycursor.execute(sql3,addr3)
        result3 = mycursor.fetchone()
      
      
    booking_id = random.randint(3000,9000) + random.randint(1000,2000)
    
    if(option == 1):
        uservalue3  = (booking_id,userid,val,source,destination,result2[0])
        mycursor.execute(sqlform3,uservalue3)
        
    if(option == 2):
        uservalue4  = (booking_id,userid,val,source,destn,result3[0])
        mycursor.execute(sqlform3,uservalue4)
    mydb.commit()
    print("\n--->\n--->\n")
    print(val+" Your Booking is Confirmed!\n\nHERE ARE YOUR DETAILS")
    
    sql4 = "select * from booking where booking_id = %s"
    addr4 = (booking_id,)
    mycursor.execute(sql4,addr4)
    result4 = mycursor.fetchone()
    print(result4)
    print("\n============ Happy Journey =================!")


def Register():
    print("\n\n<----------Welcome to Registration----------------->\n\n")
    n = random.randint(0,20)
    m = random.randint(21,50)
    userid = user_id + n + m
    print(userid)
    name = input("\nEnter your name: ")
    gender = input("\nEnter 'M' for Male\n'F' for Female\n: ")    
    age = int(input("\nEnter your age: "))
    print("\nRe-Directing to Login page......\n")
    uservalue2 = (userid,name,gender,age)
    mycursor.execute(sqlform,uservalue2)
    mydb.commit()
    Login()
#list = [('m'),('a')]

def Login():
    print("\n\n***************-Welcome to transportDB-*********************\n\n")
    val = input("Please enter your name to Login  : ")
    counter = 0
    #print("\U0001f600")
    mycursor.execute("select User_name from user")
    result = mycursor.fetchall()
    #print(result)
    for x in result:
    #x[0]=afra
        i=0;
        
        if(x[i] == val):
            counter = 1
            print("You can proceed "+x[i])
            Booking(val)
            
        else:
            i=i+1
     
    if(counter == 0):
        print("User not registered!\n\nPlz register first....\n--->Directing to Registration.....\n")
        Register()
        
#print(emoji.emojize(":grinning_face_with_big_eyes:"))

Login()

