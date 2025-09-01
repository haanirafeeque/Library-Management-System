#IN MYSQL
#CREATE DATABASE LIBRARY
#USE LIBRARY
#CREATE TABLE MEMBER_INFO (NAME varchar(20),AGE int,Country varchar(40),STATE varchar(50),Phone_No int,Email varchar(40));
#CREATE TABLE BOOK_RECORDS (NAME varchar(20),BOOK_NAME VARCHAR(20),DATE_BORROWED date, DATE_RETURNED date);
#CREATE TABLE ALL_BOOKS(BOOK_NO INT,BOOK_NAME VARCHAR(50),AUTHOR VARCHAR(50),GENRE VARCHAR(50),STATUS VARCHAR(50) DEFAULT 'AVAILABLE')
# CREATE TABLE USERS(NAME varchar(20),PASSWORD varchar(20));


import mysql.connector 
con=mysql.connector.connect(host='localhost',user='root',password='haani2007',database='library')
cur=con.cursor()
def login():    
    while True:
        print("\n" + "=" * 80)
        print("\nLibrary Management System\n")
        print("=" * 80)
        print('1. User Login')
        print('2. Admin Login')
        print('3. New Registration')
        print('0. Exit')
        opt=input('Enter Your choice: ')
        print("=" * 80)   
        if opt=='1':
            user_login()
            return
        elif opt=='2':
            admin_login()
            return
        elif opt=='3':
            NewRegistration()
            return
        
        elif opt=='0':
            return
        else:
            print('\nInvalid input try again')


def user_login():
    while True:
        name=input('Enter Your Name: ')
        password=input('Please enter your password: ')
        print("=" * 80)
        b=cur.execute('SELECT * FROM USERS WHERE NAME=%s',(name,))
        fetch=cur.fetchall()
        if fetch==[]:
            print('\nUser does not exist!')
            login()
        else:
            for i in fetch:
                if password==i[1]:
                    print('\nLogin was Succesfull!')
                    main_menu()
                    return
                else:
                    print('\nIncorrect Password Try Again!\n')
                    print("=" * 80)


def admin_login():
    while True:
        username=input('Enter Your Username: ')
        password=input('Enter Your Password: ')
        if username.lower()=='admin' and password=='admin123':
            print("=" * 80)
            print('\nLogin was Succesfull')
            admin_menu()
            break
        else:
            print('\nInvalid input please try again')
    

def admin_menu():
    while True:
        print("\n" + "=" * 80)
        print("\nLibrary Management System\n")
        print('='*80)
        print('1. View all books')
        print('2. View books that have been borrowed')
        print('3. View all membership')
        print('4. Delete membership')
        print('0. Exit')
        opt=input('Enter Your choice: ')
        print('='*80)
        if opt=='1':
            books_admin()
        elif opt=='2':
            borrowed_books()
        elif opt=='3':
            all_membership()
        elif opt=='4':
            delete_membership()
        elif opt=='0':
            print("\n\tExiting the system. Thank you!")
            print('\t  Have A Great Day Ahead!')
            print("\n" + "=" * 80)
            break
            False
        else:
            print('\nInvalid Input,Please Try again')



def books_admin():
    print('='*80)
    print('Filter Books by')
    print('1. All Books')
    print('2. Authors')
    print('3. Genre')
    opt=input('Enter your choice: ')
    print('='*80)
    if opt=='1':
        ALL_BOOKS()
    elif opt=='2':
        authors()
    elif opt=='3':
        genre()
    admin_menu() 
        


def all_membership():
    # Execute the SQL query to select all members from the MEMBER_INFO table
    cur.execute('SELECT * FROM MEMBER_INFO')
    fetch = cur.fetchall()

    # Adjust column width for proper spacing and to print all columns (Name, Age, Country, State, Phone No, Email)
    print('{:<20} {:<10} {:<20} {:<20} {:<20} {:<40}'.format('Name', 'Age', 'Country', 'State', 'Phone No', 'Email'))
    print('-' * 130)  # Print separator line to improve readability

    # Loop through each record and print formatted rows
    for i in fetch:
        # Print the member information in the appropriate column format
        print('{:<20} {:<10} {:<20} {:<20} {:<20} {:<40}'.format(i[0], i[1], i[2], i[3], i[4], i[5]))





        
def borrowed_books():
    cur.execute('SELECT * FROM ALL_BOOKS WHERE STATUS="BORROWED"')
    fetch=cur.fetchall()
    print('\n{:<10} {:<30} {:<20} {:<15} {:<10}'.format('Book_No', 'Book_Name', 'Author', 'Genre', 'Status'))
    print('-' * 90)
    for i in fetch:
        print('{:<10} {:<30} {:<20} {:<15} {:<10}'.format(i[0], i[1], i[2], i[3], i[4]))
    admin_menu()

def delete_membership():
    print('='*80)
    name1=input('Enter The name whose membership is to be deleted: ')
    confirm=input('Please Confirm (Y/N)')
    print('='*80)
    if confirm=='y'or confirm=='Y':
        cur.execute('SELECT * FROM MEMBER_INFO WHERE NAME=%s',(name1,))
        result=cur.fetchone()
        if result is None:
            print('\nThe member does not exits!')
        else:
            cur.execute('DELETE FROM MEMBER_INFO WHERE NAME = %s',(name1,))
            con.commit()
            print('\nThe membership has succesfully been deleted!')
            admin_menu()
    else:
        admin_menu()



def NewRegistration():
    print("="*80)
    name2=input('Please Enter Your Name: ')
    age=int(input('Please Enter Your Age: '))
    Country=input('Please Enter Your Country: ')
    State=input('Please Enter Your State: ')
    phone_number=int(input('Please Enter Your Phone Number: '))
    email=input('Enter Your email id: ')
    password=input('Please Create A Password For Your Account: ')
    print("="*80)
    insert='INSERT INTO MEMBER_INFO VALUES (%s,%s,%s,%s,%s,%s) '
    values=(name2,age,Country,State,phone_number,email)
    cur.execute(insert,values)
    con.commit()
    cur.execute('INSERT INTO USERS VALUES(%s,%s)',(name2,password))
    con.commit()
    print()
    print('\nNew Member Successfully Added!\n')
    
    login()

def addbook():
    try:
        name=input('Please Enter Your Name: ')
        book_name=input('Please Enter The Name Of The Book : ')
        borrow_Date=input('Enter the Date The Book Has Been Borrowed (Format - YYYY-MM-DD): ')
        return_date=input('Enter The Date The Book Will Be Returned (Format - YYYY-MM-DD): ')
        print("="*80)
        insert='INSERT INTO BOOK_RECORDS VALUES (%s,%s,%s,%s)'
        values=(name,book_name,borrow_Date,return_date)
        cur.execute(insert,values)
        con.commit()
        cur.execute('UPDATE ALL_BOOKS SET STATUS="BORROWED" WHERE BOOK_NAME=%s',(book_name,))
        print('\nBook Successfully Added!')
    except:
        print('\nThe book is currently not available :(')
    main_menu()

def Search_Book():
    print()
    book_name=input('Please Enter The Name Of The Book You Would Like To Search For: ')
    print()
    print("=" * 80)
    cur.execute('SELECT * FROM ALL_BOOKS WHERE BOOK_NAME=%s',(book_name,))
    result=cur.fetchone()
    if result:
        if result[4].upper() == "BORROWED":  
            print('\nThe Book Is Currently Not Available. Sorry! :(')
        else:
            print('\nThe Book is Currently Available! :)')
    else:
        print('\nNo book found with the given name.')

    main_menu()

def return_book():
    name=input('Please Enter Your Name: ')
    book_name=input('Please Enter The Name Of The Book You have Returned: ')
    cur.execute('SELECT BOOK_NAME FROM BOOK_RECORDS WHERE BOOK_NAME=%s ',(book_name,))
    result=cur.fetchone()
    if result is None:
        print("="*80)
        print("\n  INVALID ENTRY! Book not found, please try again.")
    else:
        cur.execute("DELETE FROM BOOK_RECORDS WHERE NAME = %s AND BOOK_NAME = %s", (name, book_name))
        cur.execute("UPDATE ALL_BOOKS SET STATUS = 'AVAILABLE' WHERE BOOK_NAME = %s", (book_name,))
        con.commit()
        print("="*80)
        print('\n  You have Successfully Returned The Book!')
        print('\tHave A Great Day Ahead!\n')
        print("="*80)
    main_menu()

def Membership_Details():
    print("="*80)
    name=input('\nEnter Your Name:  ')
    cur.execute('SELECT * FROM MEMBER_INFO WHERE NAME=\'{}\' '.format(name))
    fetch=cur.fetchall()
    for i in fetch:
        print('\n'+"="*80,'\n')
        print('Name:        \t ',i[0])
        print('Age:         \t ',i[1])
        print('Country:     \t ',i[2])
        print('State:       \t ',i[3])
        print('Phone Number:\t',i[4])
        print('Email:       \t',i[5])
    main_menu()

def mybook():
    name=input('\nPlease Enter Your Name: ')
    print('\n'+"="*80)
    cur.execute('SELECT * FROM BOOK_RECORDS WHERE NAME =\'{}\''.format(name))
    c=cur.fetchall()
    if c==[]:
        print('\nYou have not borrowed a book!')
        
    for i in c:
        print()
        print('Name:                  \t ',i[0])
        print('Book_Name:             \t ',i[1])
        print('Date Borrowed:         \t ',i[2])
        print('Date To Be Returned By:\t ',i[3])
    main_menu()

def books():
    print('='*80)
    print('Filter Books by')
    print('1. All Books')
    print('2. Authors')
    print('3. Genre')
    print('4. Availability')
    opt=input('Enter your choice: ')
    print('='*80)
    if opt=='1':
        ALL_BOOKS()
    elif opt=='2':
        authors()
    elif opt=='3':
        genre()
    elif opt=='4':
        available()
    main_menu()

def available():
    cur.execute('SELECT * FROM ALL_BOOKS WHERE STATUS="AVAILABLE"')
    fetch = cur.fetchall()
    print('\n{:<10} {:<30} {:<20} {:<15} {:<10}'.format('Book_No', 'Book_Name', 'Author', 'Genre', 'Status'))
    print('-' * 90)
    for i in fetch:
        print('{:<10} {:<30} {:<20} {:<15} {:<10}'.format(i[0], i[1], i[2], i[3], i[4]))
        
    return

def ALL_BOOKS():
    cur.execute('SELECT * FROM ALL_BOOKS')
    fetch = cur.fetchall()
    print('\n{:<10} {:<30} {:<20} {:<15} {:<10}'.format('Book_No', 'Book_Name', 'Author', 'Genre', 'Status'))
    print('-' * 90)
    for i in fetch:
        print('{:<10} {:<30} {:<20} {:<15} {:<10}'.format(i[0], i[1], i[2], i[3], i[4]))
        
    return



def authors():
    print()
    author_name=input('Enter the name of the author whose book you want to search by: ')
    print()
    print('='*80)
    cur.execute('SELECT * FROM ALL_BOOKS WHERE AUTHOR=%s',(author_name,))
    fetch=cur.fetchall()
    print('\n{:<10} {:<30} {:<20} {:<15} {:<10}'.format('Book_No', 'Book_Name', 'Author', 'Genre', 'Status'))
    print('-' * 90)
    for i in fetch:
        print('{:<10} {:<30} {:<20} {:<15} {:<10}'.format(i[0], i[1], i[2], i[3], i[4]))
    return

def genre():
    print()
    genre_name=input('Enter the genre of which book you want to search by: ')
    print()
    print('='*80)
    cur.execute('SELECT * FROM ALL_BOOKS WHERE GENRE=%s',(genre_name,))
    fetch=cur.fetchall()
    print('\n{:<10} {:<30} {:<20} {:<15} {:<10}'.format('Book_No', 'Book_Name', 'Author', 'Genre', 'Status'))
    print('-' * 90)
    for i in fetch:
        print('{:<10} {:<30} {:<20} {:<15} {:<10}'.format(i[0], i[1], i[2], i[3], i[4]))
    return





def main_menu():
    while True:
        print("\n" + "=" * 80)
        print("\nLibrary Management System\n")
        print("=" * 80)
        print("1) Access Your Membership Details")
        print('2) Books in the library')
        print("3) Check For The Availability Of A Book")
        print("4) Borrow A Book")
        print('5) Books Borrowed')
        print("6) Return A Book")
        print("0) Exit")
        choice = input("Please select an option (0-6): ")
        print("=" * 80)
        if choice == '1':
            Membership_Details()
        elif choice == '2':
            books()
        elif choice == '3':
            Search_Book()
        elif choice == '4':
            addbook()
        elif choice == '5':
            mybook()
        elif choice == '6':
            return_book()
        elif choice == '0':
            print("\n\tExiting the system. Thank you!")
            print('\t  Have A Great Day Ahead!')
            print("\n" + "=" * 80)
            False
            return
            break

        else:
            print("\nInvalid choice. Please try again.")
        
            
login()


    



