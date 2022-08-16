import mysql.connector

def createdb():
    mycursor.execute("DROP DATABASE IF EXISTS STUDENTSEARCH")
    mycursor.execute("CREATE DATABASE STUDENTSEARCH ")

def createtable():
    mycursor.execute("DROP TABLE IF EXISTS SS")
    mycursor.execute("CREATE TABLE SS ( ROLL_NUMBER INTEGER PRIMARY KEY , NAME VARCHAR(100) , BRANCH VARCHAR(50),USER_ID VARCHAR(25))")

def insert_record():
    x=int(input("\nEnter the roll number of the student:"))
    y=input("\nEnter the name of the student:")
    z=input("\nEnter the branch of the student:")
    w=input("\nEnter the user id of the student;")
    mycursor.execute("INSERT INTO SS VALUES( x , 'y' , 'z' , 'w')")

def delete_record():
    x=int(input("Enter the roll number of the student you want to delete the records:"))
    mycursor.execute("DELETE FROM SS WHERE ROLL_NUMBER=x")

def filter_alphabetically():
    mycursor.execute("SELECT * FROM SS ORDER BY NAME")

def filter_rollnumberwise():
    mycursor.execute("UPDATE SS SET ROLL_NUMBER=x where ROLL_NUMBER=y")

def edit_roll():
    x=int(input("Enter the roll number you want to update: "))
    y=int(input("Enter the roll number you want to update to: "))
    mycursor.execute("UPDATE SS SET ROLL_NUMBER=x where ROLL_NUMBER=y")

def edit_name():
    x=input("Enter the name you want to update: ")
    y=input("Enter the name you want to update to: ")
    mycursor.execute("UPDATE SS SET NAME='x' where NAME='y'")

def edit_branch():
    x=input("Enter the branch you want to update: ")
    y=input("Enter the branch you want to update to: ")
    mycursor.execute("UPDATE SS SET BRANCH='x' where BRANCH='y")

def edit_user():
    x=input("Enter the user_id you want to update: ")
    y=input("Enter the user_id you want to update to: ")
    mycursor.execute("UPDATE SS SET USER_ID='x' where USER_ID='y")

def display_record():
    mycursor.execute("SELECT * FROM Vehicle")
    print("\nTABLE: STUDENT SEARCH RECORDS")
    for record in mycursor:
        print(record)

#main code starts here
mydab = mysql.connector.connect(host='localhost', user='root', passwd='riddhirids', database= 'mysql')
mycursor = mydab.cursor()

createdb()              #database_creation 
mydab.close()

mydab = mysql.connector.connect(host='localhost', user='root', passwd='riddhirids', database= 'STUDENTSEARCH')
mycursor = mydab.cursor()
mycursor.execute(" USE STUDENTSEARCH")

createtable()   #table_creation

choice = 'y'
while choice.lower() == 'y':             #choices to be made 
    print("-----------------------------------------------")
    print("1. INSERT A STUDENT ENTRY")
    print("2. DELETING A STUDENT ENTRY")
    print("3. FILTER A STUDENT ENTRY")
    print("4. EDIT A STUDENT ENTRY")
    print("5. DISPLAY OF RECORDS")
    print("-----------------------------------------------")

    ch1 = int(input("Enter your choice number : "))
    if ch1 == 1:
        insert_record()

    elif ch1 == 2:
        delete_record()

    elif ch1 == 3:
        print("1. Filter the records according to roll number")
        print("2. Filter the records in alphabetic order")
        x = int(input("Enter your choice number : "))
        if x == 2:
            filter_alphabetically()
        elif x == 1:
            filter_rollnumberwise()
        else:
            print("Invalid choice")

    elif ch1 == 4:
        print("1.Edit the roll number of the student")
        print("2.Edit the name of the student")
        print("3.Edit the branch of the student")
        print("4.Edit the user_id of the student")
        x = int(input("Enter your choice number : "))
        if x == 1:
            edit_roll()

        elif x == 2:
            edit_name()

        elif x==3:
            edit_branch()

        elif x==4:
            edit_user()

        else:
            print("Invalid choice")

    elif ch1 == 5:
        display_record()

    else:
        print("Invalid choice")

    choice = input("Do you wish to continue?(y/n)")
    






