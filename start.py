def Welcome_message():
    file=open("welcome.txt","r")
    str=file.read()
    print(str)

def ty():
    print(" ",'\n','~' * 28,'\n'," " * 20, "***** THANK YOU !!! *****",'\n','~' * 28)

import mysql.connector as mycon

def show_Database(db):
    con=mycon.connect(host="localhost",user="root",password="root",database=db)
    cursor=con.cursor()
    print(" ",'\n',"These are the following tables in the database :")
    cursor.execute("show tables")
    data=cursor.fetchall()
    count=cursor.rowcount
    table,show_Database.T=[],[]
    for row in data:
        table=[row]
        for x in range ( len(table) ):
            for i in range ( len(table[x]) ):
                show_Database.T=show_Database.T+[ table[x][i] ]
    for a in show_Database.T:
        print("==>",a)
    show_Database.t=input("Select table :")
    presentation(db,show_Database.t)
    if show_Database.t in show_Database.T:
        cursor.execute("select * from {}".format(show_Database.t))
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            print(row)
    else:
        print(" ",'\n',"-"*10,'\n',"Please select from the below options.")
        show_Database(db)

def display_Database(tablename,db): 
    con=mycon.connect(host="localhost",user="root",password="root",database=db)
    cursor=con.cursor()
    cursor.execute("select * from {}".format(tablename))
    data=cursor.fetchall()
    count=cursor.rowcount
    presentation(db,tablename)
    display_Database.count=0
    for row in data:
        display_Database.count+=1
        print(row)

def display_table(db):
    con=mycon.connect(host="localhost",user="root",password="root",database=db)
    cursor=con.cursor()
    print(" ",'\n',"These are the following tables in the database :")
    cursor.execute("show tables")
    data=cursor.fetchall()
    cunt=cursor.rowcount
    table,T=[],[]
    for row in data:
        table=[row]
        for x in range ( len(table) ):
            for i in range ( len(table[x]) ):
                T=T+[ table[x][i] ]
    for a in T:
        print("==>",a) 

def presentation(database,table_name):
    if (database=="Admin" ):
        if (table_name == "customer") :
            print("_"*44,'\n',"| CI  | Cname   | cusername | cpassword |",'\n',"_"*44)
    elif (database == "Genre" ):  
        print("_"*55,'\n',"| SNo | Book_Name | Author | Price_of_each_book |",'\n',"_"*55)

def who():
    print(" ",'\n',"Who is trying to login?",'\n',"(1)Admin" ,'\n',"(2)Customer")
    w=input("Enter choice [1/2] :")
    if w.isdigit() :
        w=int(w)
        if (w==1):
            print(" ",'\n'," "*50,"~"*11,'\n'," "*50,"!!"," "*5,"ADMIN"," "*5,"!!",'\n'," "*50,"`"*25,'\n'," ")
            ADMIN()
        elif (w==2):
            print(" ",'\n'," "*50,"~"*13,'\n'," "*50,"!!"," "*5,"CUSTOMER"," "*5,"!!",'\n'," "*50,"`"*30,'\n'," ")
            Customer_Login()
        else :
            print("Please choose an appropriate option .")
            Project()
    else :
        print(" ",'\n',"Please select number from the given option.",'\n',"")
        who()

def Customer_Login():
    c=input("Do you already have an existing account ? [1. YES or 2.NO] : ")
    if (c=="1"):
            c_login()
    elif (c=="2"):
        create_c()
        c_login()
    else :
        print(" ",'\n',"Please choose an appropriate option.",'\n'," ")
        Customer_Login()


def ci(Customer_id):
    con=mycon.connect(host="localhost",user="root",password="root",database="Admin")
    cursor=con.cursor()
    cursor.execute("select * from customer where CI='{}'".format(Customer_id))
    data=cursor.fetchall()
    count=cursor.rowcount
    for row in data:
        print(row)

def create_customer_id():
    import random
    digits="0123456789"
    create_customer_id.ci=""
    con=mycon.connect(host="localhost",user="root",password="root",database="Admin")
    cursor=con.cursor()
    cursor.execute("select CI from customer")
    data=cursor.fetchall()
    count=cursor.rowcount
    LI,L=[],[]         
    for row in data :
        LI=LI+[row]
    for x in range (len(LI)):
        for i in range (len(LI[x])):
            L=L+[LI[x][i]]
    create_customer_id.ci+="CI"+str(random.randint(0,100))
    if create_customer_id.ci not in L:
        return ("Dear customer , your customer ID is :",create_customer_id.ci)
        exit()
    else :
        create_customer_id()

def create_c():
    con=mycon.connect(host="localhost",user="root",password="root",database="Admin")
    cursor=con.cursor()
    create_customer_id()
    c_id=create_customer_id.ci
    print("Your customer ID is :",c_id)
    name , un , pw=input("Enter your name please :") , input("Enter username :") , input("Enter password :")
    cursor.execute("insert into Customer (CI , Cname , cusername , cpassword) values ('{}','{}','{}','{}') ".format(c_id,name,un,pw))
    con.commit()
    print("Dear Customer ,", name.upper() , "," " Your account is created Successfully ! :) ")
    ci(c_id)


def c_login():
    print("You will have 3 trials to login into your account.") 
    for i in range (3):
        if (i==0):
            print("-"*25,'\n',"First try.")
            c()
        elif (i==1):
            print("-"*25,'\n',"Second try.")
            c()
        elif (i==2):
            print("-"*25,'\n',"Third try.",'\n',"This will be your last try.")
            c()
            backup()

def c():
    c.ci , c.cu , c.cp=input("Enter your Customer ID please :") , input("Enter your username dear customer :") , input("Enter your password :")
    cid_check()

def cid_check():
    con=mycon.connect(host="localhost",user="root",password="root",database="Admin")
    cursor=con.cursor()
    cursor.execute("select CI from customer")
    data=cursor.fetchall()
    count=cursor.rowcount
    cn,c_sorted=[],[]
    for row in data:
        cn=[row]
        for x in range (len(cn)) :
            for i in range (len(cn[x])):
                c_sorted=c_sorted+[cn[x][i]]
    if c.ci not in c_sorted :
        print("This customer id ", c.ci ," doesnt exist." ,'\n',"Please try again.")
    else :
        username_check()    

def username_check():
    con=mycon.connect(host="localhost",user="root",password="root",database="Admin")
    cursor=con.cursor()
    cursor.execute("select cusername from customer where CI='{}'".format(c.ci))
    data=cursor.fetchall()
    count=cursor.rowcount
    un,u=[],[]        
    for row in data:
        un=[row]
        for x in range (len(un)) :
            for i in range (len(un[x])):
                u=u+[un[x][i]]
        for a in u:
            username_check.u=a
    if (c.cu != username_check.u) :
        print("Incorrect username.")
    else :
        password_check()

def password_check():
    con=mycon.connect(host="localhost",user="root",password="root",database="Admin")
    cursor=con.cursor()
    cursor.execute("select cpassword from customer where CI='{}'".format(c.ci))
    data=cursor.fetchall()
    count=cursor.rowcount
    pw,p=[],[]
    for row in data:
        pw=[row]
        for x in range (len(pw)) :
            for i in range (len(pw[x])):
                p=p+[pw[x][i]]
        for a in p:
            password_check.p=a
    if (c.cp==password_check.p ):
        con=mycon.connect(host="localhost",user="root",password="root",database="Admin")
        cursor=con.cursor()
        cursor.execute("select Cname from Customer where CI='{}'".format(c.ci))
        data=cursor.fetchall()
        count=cursor.rowcount
        n,name=[],[]
        for row in data:
            n=[row]
        for x in range ( len(n) ):
            for i in range ( len(n[x]) ):
                name=name+[ n[x][i] ]
        for i in name:
            password_check.name=i
        print('\n',"Login Successfull ! !",'\n'," ",'\n',"_"*25,'\n',"Now you can start your online shopping....",'\n'," ",'\n',"The categories of the bookshop are as shown. Please select the genre from which you want to buy book.",'\n'," ",'\n',"-"*25,'\n',"")
        buy_Genre()
        exit()
    else :
        print("Incorrect password.")

def backup():
    print("-"*5,'\n',"Choose 1 if you want to create a new account.",'\n',"Choose 2 if you dont wanna backup. ")
    value=input("Enter your choice [1/2] :")
    if (value=="1") :
        create_c()
        c_login()
    elif (value=="2"):
        print("-"*25,'\n',"You havent logged into account! Do come again.",'\n',"Thank You !!")
        main()
    else :
        print("Please choose an appropriate option.")
        backup()

def buy_Genre():
    print(" ",'\n',"Choose 1 if you want to buy books.",'\n',"Choose 2 if you are over with your shopping.")
    ch=input("Enter choice [1/2] :")
    if (ch=="1"):
        buy()
    elif (ch=="2"):
        bill()
    else :
        print("Please choose an appropriate option.")
        buy_Genre()

def buy():
    buy.Order,buy.amount=[],[]
    ans="yes"
    while ans.lower()=="yes":
        con = mycon.connect(host="localhost", user="root", password="root", database="Genre")
        cursor = con.cursor()
        show_Database("genre")
        xy="yes"
        while xy.lower()=="yes":
            ch=int(input("Enter the book ID you want to buy : "))
            cursor.execute("select * from {} where SNo={}".format(show_Database.t, ch))
            data = cursor.fetchall()
            count = cursor.rowcount
            for row in data:
                buy.Order+=[row]
            cursor.execute("select Price_of_each_book from {} where SNo={}".format(show_Database.t,ch))
            data = cursor.fetchall()
            count = cursor.rowcount
            for price in data:
                buy.amount+=list(price)
            xy=input("Do you want to buy more books from this genre? :")
        ans = input('Do you wanna buy books from different genre : (yes/no)')
    buy_Genre()

def bill():
    Order,am= buy.Order,buy.amount
    print(" ",'\n',"-"*50,'\n',' '*20,'TAX INVOICE',' '*10,'\n','-'*50,'\n',"Order :")
    for a in Order:
        print(a)
    print(" ",'\n',"Tax Inclusive :",'\n'," "*25,"Before VAT :"," "*11, sum(am),'\n'," "*25 ,"After VAT :"," "*14 , 1.05 *sum(am),'\n',"Total Amount to pay :"," "*22,1.05*sum(am))
    ty()
    exit()

def ADMIN():
    import csv
    adminlist=[]
    f=open("admin.csv","r")
    f1=csv.reader(f)
    for row in f1:
        if row!=[]:
            adminlist=row
    admin_username,admin_password=adminlist[0],adminlist[1]
    print(" ",'\n',"Admin , You will have 3 trials to login .")
    def a_check():
        if ((a.u ==admin_username)and(a.p==admin_password)):
            print(" "*50,"_"*25,'\n'," "*50,"|  Login Successfull ! !  |",'\n'," "*50,"_"*25,'\n'," ",'\n'," "*50,"WELCOME ADMIN !!",'\n'," ")
            admin_mainmenu ()
            exit()
        else:
            if (a.u != admin_username) :
                print("Incorrect username.")
            if (a.p != admin_password):
                print("Incorrect password.")
    def a():
        a.u=input("Admin enter your username : ")
        a.p=input("Admin enter your password : ")
        a_check()
    def admin_try3():
        for i in range (3):
            if (i==0):
                print("-"*25,'\n',"First try.")
                a()
            elif (i==1):
                print("-"*25,'\n',"Second try.")
                a()
            elif (i==2):
                print("-"*25,'\n',"Third try.",'\n',"This will be your last try.")
                a()
                print("Your all trials are over.",'\n',"Thank You!!")     
    admin_try3()

def admin_mainmenu ():
    print("-" * 10)
    f=open("admin.txt","r")
    str=f.readlines()
    for a in str:
        print(a)
    print()
    xa=input("Please choose what you wanna do? [1/2/3/4/5] :")
    if (xa=="1"):
        change_admin_details()
    elif (xa=="2"):
        view_customer_details()
    elif (xa=="3"):
        change_customer_details()
    elif (xa=="4"):
        update_genre()
    elif(xa=="5"):
        print()
        print("Thank You!!!")
        main()
    else:
        print("-"*3)
        print("Please select number from the given option.")
        admin_mainmenu ()

# OPTION 1 if you want to CHANGE ADMIN DETAILS .   #csv
def change_admin_details():
    print("-"*10,'\n',"==+> To change admin details.",'\n',"Choose 1 to change admin username.",'\n',"Choose 2 to change admin password.",'\n',"Choose 3 if you are done with changing admin details.")
    import csv
    adminlist = []
    f = open("admin.csv", "r")
    f1 = csv.reader(f)
    for row in f1:
        if row != []:
            adminlist = row
    admin_username= adminlist[0]
    admin_password= adminlist[1]
    f.close()
    a=input("What do you wanna do? [1/2/3] :")
    if (a=="1"):
        newau = input("Enter new admin username :")
        newap=admin_password
    elif (a=="2"):
        newau=admin_username
        newap = input("Enter new admin password :")
    elif (a=="3"):
        print(" ",'\n',"`"*20,'\n',"Admin details changed successfully.",'\n',"~"*20,'\n',"Please login again.")
        ADMIN()
        exit()
    else:
        print("-"*5,'\n',"Please choose an appropriate number")
        change_admin_details()
    f = open("admin.csv", "w")
    f1 = csv.writer(f)
    f1.writerow([newau, newap])
    f.close()
    change_admin_details()

#OPTION 2 if you want to view CUSTOMER DETAILS .
def view_customer_details():
    print("-" * 10,'\n',"==+> To view customer details.",'\n',"Choose 1 to view customer detail.",'\n',"Choose 2 if done with customer detials.")
    a = input("What do you wanna do? [1/2] :")
    if (a == "1"):
        display_Database("customer", "Admin")
        view_customer_details()
    elif (a == "2"):
        admin_mainmenu ()
        exit()
    else:
        print("-" * 5,'\n',"Please choose an appropriate number")
        view_customer_details()
        exit()

#OPTION 3 if you want to CHANGE CUSTOMER DETAILS.
def change_customer_details():
    print("-"*10,'\n',"==+> To change customer details.",'\n',"Choose 1 to change Customer ID",'\n',"Choose 2 to change username OR password of a particular customer.",'\n',"Choose 3 to delete a particular customer details.",'\n',"Choose 4 if done with changing customer details.")
    a=input("What do you wanna do? [1/2/3/4] :")
    if (a=="1"):
        change_customer_id()
    elif (a=="2"):
        change_customer_usernameORpassword()
    elif (a=="3"):
        delete_customer_details()
    elif (a=="4"):
        print(" ",'\n'," "*10,"~"*28,'\n'," "*10,"||","Customer details changed successfully !!!""||",'\n'," "*10,"~"*28,'\n'," ")
        admin_mainmenu ()
    else:
        print("-"*5,'\n',"Please choose an appropriate number")
        change_customer_details()
def change_customer_id():
    print(" ",'\n',"="*50,'\n',"To change Customer ID")
    display_Database("customer","Admin")
    con = mycon.connect(host="localhost", user="root", password="root", database="Admin")
    cursor = con.cursor()
    cursor.execute("select CI from customer")
    data = cursor.fetchall()
    count = cursor.rowcount
    LI, L = [], []
    for row in data:
        LI = LI + [row]
        for x in range(len(LI)):
            for i in range(len(LI[x])):
                L = L + [LI[x][i]]
    def change_customer_id_new_id():
        change_customer_id_new_id.i=input("Enter new Customer ID [should start with CI ] : ")
        if change_customer_id_new_id.i[:2]=="CI" :
            if change_customer_id_new_id.i not in L :
                con=mycon.connect(host="localhost",user="root",password="root",database="Admin")
                cursor=con.cursor()
                cursor.execute("update customer set CI='{}' where CI='{}'".format(change_customer_id_new_id.i,change_customer_id_old_id.i))
                con.commit()
                print(" ",'\n',"_"*42,'\n',"|","Customer ID changed successfully!!","|",'\n',"_"*42,'\n'," ")
                ci(change_customer_id_new_id.i)
                print(" ")
                change_customer_details()
            else:
                print("-"*5,'\n',"Please choose id which doesnt exits.")
                change_customer_id_new_id()
        else:
            print("-"*2,'\n',"Please start customer id with CI ")
            change_customer_id_new_id()
    def change_customer_id_old_id():
        change_customer_id_old_id.i=input("Select the customer ID to change its ID : ")
        if change_customer_id_old_id.i in L :
            change_customer_id_new_id()
        else:
            print("-"*5,'\n',"Please choose id which exits.")
            change_customer_id_old_id()
    change_customer_id_old_id()
def change_customer_usernameORpassword():
    print(" ", '\n', "=" * 50, '\n', "To change username OR password of a particular customer.")
    display_Database("customer", "Admin")
    def UPask():
        con = mycon.connect(host="localhost", user="root", password="root", database="Admin")
        cursor = con.cursor()
        cursor.execute("select CI from customer")
        data = cursor.fetchall()
        count = cursor.rowcount
        LI, L = [],[]  # List of IDs   #[('CI0',)]                  #['CI0']
        for row in data:
            LI = LI + [row]
            for x in range(len(LI)):
                for i in range(len(LI[x])):
                    L = L + [LI[x][i]]
        i=input("Select the customer ID to change its username/password :")
        if i in L:
            print(" ", '\n', "Choose 1 if you want to change username of a particular customer.", '\n',"Choose 2 if you want to change password of a particular customer", '\n',"Choose 3 if are done changing username/password of customer.")
            def u():
                up = input("Enter your choice [1/2/3] :")
                if (up == "1"):
                    print(" ", '\n', " ", '\n', "=" * 50, '\n', "To change username of a particular customer.")
                    new=input("Enter new username : ")
                    UP="cusername"
                    cursor.execute("update customer set {}='{}' where CI='{}'".format(UP, new, i))
                    con.commit()
                    print()
                    ci(i)
                    change_customer_details()
                elif (up == "2"):
                    print(" ", '\n', " ", '\n', "=" * 50, '\n', "To change password of a particular customer.")
                    new = input("Enter new password : ")
                    UP="cpassword"
                    cursor.execute("update customer set {}='{}' where CI='{}'".format(UP, new, i))
                    con.commit()
                    print()
                    ci(i)
                    change_customer_details()
                elif (up=="3"):
                    print(" ",'\n',"Customer details changed successfully!!")
                    change_customer_details()
                else :
                    print("Please choose an appropriate option.")
                    u()
            u()
        else:
            print("Please choose id which exists.")
            UPask()
    UPask()
def delete_customer_details():
    print(" ",'\n',"="*50,'\n',"To delete a particular customer details.")
    display_Database("customer","Admin")
    def delete_c_id():
        delete_c_id.i=input("Select the customer ID to delete record : ")
        con=mycon.connect(host="localhost",user="root",password="root",database="Admin")
        cursor=con.cursor()
        cursor.execute("select CI from customer")
        data=cursor.fetchall()
        count=cursor.rowcount
        LI,L=[],[]  
        for row in data :
            LI=[row]
            for x in range (len(LI)):
                for i in range (len(LI[x])):
                    L=L+[LI[x][i]]
        if delete_c_id.i in L :
            cursor.execute("delete from customer where CI='{}'".format(delete_c_id.i))
            con.commit()
            print(" ",'\n',"_"*42,'\n',"|","Customer ID deleted successfully!!","|",'\n',"_"*42,'\n'," ")
            change_customer_details()
            exit()
        else:
            print("-"*5,'\n',"Please choose id which exits.")
            delete_c_id()
    delete_c_id()

#OPTION 4 if you want to UPDATE a GENRE.
def update_genre():
    print("-" * 10,'\n',"==+> To update genre.",'\n',"Choose 1 to add book in genre.",'\n',"Choose 2 to delete book in genre.",'\n',"Choose 3 if done with updating genre.")
    a = input("What do you wanna do? [1/2/3] :")
    if(a=="1"):
        add_book_genre()
    elif (a=="2"):
        delete_book_genre()
    elif (a=="3"):
        print(" ",'\n'," " * 10, "~" * 28,'\n'," " * 10, "||", "Genre updated successfully !!!""||",'\n'," " * 10, "~" * 28,'\n'," ")
        admin_mainmenu ()
        exit()
    else:
        print("-" * 5,'\n',"Please choose an appropriate number")
        update_genre()
def add_book_genre():
    print(" ",'\n',"=" * 50,'\n',"To add book in genre")
    con=mycon.connect(host="localhost",user="root",password="root",database="Genre")
    cursor=con.cursor()
    def adding():
        print(" ",'\n',"Choose 1 if you want to add a book in genre.",'\n',"Choose 2 if you are done with adding book in genre.")
        a=input("Enter your choice [1/2] :")
        if (a=="1"):
            def a1():
                show_Database("Genre")
                sno , bn , an , price =input("Enter SNo :") , input("Enter Book Name :") , input("Enter Author Name :") , int(input("Enter price :"))
                cursor.execute("insert into {} (SNo , Book_Name , Author , Price_of_each_book) values ({},'{}','{}',{})".format(show_Database.t, sno, bn, an, price))
                con.commit()
                display_Database(show_Database.t, "genre")
                print(" ",'\n',"Book added successfully !",'\n'," ")
                x = input("Do you want to add more books? [1.yes 2.no] :")
                if (x == "1"):
                    a1()
                elif (x=="2"):
                    adding()
                    exit()
                else:
                    print("Please choose appropriate option.")
                    adding()
            a1()
        elif (a=="2"):
            print(" ",'\n'," " * 10, "~" * 28,'\n'," " * 10, "||", "Book added in Genre successfully !!!""||",'\n'," " * 10, "~" * 28,'\n'," ")
            update_genre()
            exit()
        else:
            print("-" * 5,'\n',"Please choose an appropriate number")
            add_book_genre()
    adding()
def delete_book_genre():
    print(" ",'\n',"=" * 50,'\n',"To delete book in genre")
    con = mycon.connect(host="localhost", user="root", password="root", database="Genre")
    cursor = con.cursor()
    print("Choose 1 if you want to delete a book from genre.",'\n',"Choose 2 if you are done with deleting book from genre.")
    a=input("Enter your choice [1/2] :")
    print()
    if (a=="1"):
        show_Database("Genre")
        sno=input("Enter the sno of the book you want to delete :")
        cursor.execute("delete from {} where SNo='{}' ".format(show_Database.t, sno))
        con.commit()
        display_Database(show_Database.t,"genre")
        print(" ",'\n',"Book deleted successfully.",'\n'," ")
        delete_book_genre()
        exit()
    elif (a=="2"):
        print(" " * 10, "~" * 28,'\n'," " * 10, "||", "Book deleted in Genre successfully !!!""||",'\n'," " * 10, "~" * 28,'\n'," ")
        update_genre()
        exit()
    else:
        print("-" * 5,'\n',"Please choose an appropriate number")
        delete_book_genre()

def main():
    print(" ",'\n',"~~> Choose 1 => if you want to LOGIN.",'\n',"~~> Choose 2 => if you want to EXIT."," ")
    x=input("Enter your choice [1/2] : ")
    if (x=="1"):
        who()
    elif (x=="2"):
        ty()
    else :
        print("-"*2,'\n',"Please choose an appropriate option.")
        main()

def Project():
    Welcome_message()
    main()

Project()