"""
python application to make relation with sql file
@author = mcaptain79
"""
import datetime
import sys
import mysql.connector
myDB = mysql.connector.connect(user = 'root',password = None,host = 'localhost',database = 'mySql')
cursor = myDB.cursor()
#code below is used for insertion in customers
#instructor
add_instructor = ('insert into instructor'
                  '(nationalCode,name,family,instructorId,university,userName,password)'
                  'values (%s,%s,%s,%s,%s,%s,%s)')
add_instructor_account = ('insert into instructor_account'
                         '(nationalCode,balance,createDate)'
                         'values (%s,%s,%s)')
#student
add_student = ('insert into student'
               '(nationalCode,name,family,studentId,university,userName,password)'
               'values (%s,%s,%s,%s,%s,%s,%s)')
add_student_account = ('insert into student_account'
                       '(nationalCode,balance,createDate)'
                       'values (%s,%s,%s)')
#ordinary
add_ordinary = ('insert into ordinary'
                '(nationalCode,name,family,job,userName,password)'
                'values (%s,%s,%s,%s,%s,%s)')
add_ordinary_account = ('insert into ordinary_account'
                        '(nationalCode,balance,createDate)'
                        'values (%s,%s,%s)')
#function below is for validation of a password
def isValidPass(password):
    hasDigit = 0
    hasChar = 0
    if len(password) < 8:
        return False
    #statement below checks if password contains bow digit and char
    for i in password:
        if i.isdigit():
            hasDigit = 1
        else:
            hasChar = 1
    if hasDigit == 1 and hasChar == 1:
        return True
    else:
        return False
#function below is for collecting usernames
def userNameSet():
    userSet = set()
    query1 = ('select userName from student')
    cursor.execute(query1)
    for userName in cursor:
        userSet.add(userName[0])
    query2 = ('select userName from instructor')
    cursor.execute(query2)
    for userName in cursor:
        userSet.add(userName[0])
    query3 = ('select userName from ordinary')
    cursor.execute(query3)
    for userName in cursor:
        userSet.add(userName[0])
    return userSet
#saving user names in a set
userNames = userNameSet()
print(userNames)
#function below is for collecting national codes
def nationalCodeSet():
    nationalCodes = set()
    query1 = ('select nationalCode from student')
    cursor.execute(query1)
    for nationalCode in cursor:
        nationalCodes.add(nationalCode[0])
    query2 = ('select nationalCode from instructor')
    cursor.execute(query2)
    for nationalCode in cursor:
        nationalCodes.add(nationalCode[0])
    query3 = ('select nationalCode from ordinary')
    cursor.execute(query3)
    for nationalCode in cursor:
        nationalCodes.add(nationalCode[0])
    return nationalCodes
#saving national codes in a set
nationalCodes = nationalCodeSet()
print(nationalCodes)
#saving histories in a set
def historySet():
    histories = set()
    query = ('select historyId from history')
    cursor.execute(query)
    for historyId in cursor:
        histories.add(historyId[0])
    return histories
#saving history ids in aset
histories = historySet()
print(histories)
#function below is for saving book id and number of books with that id
def bookDict():
    myDict = dict()
    query = ('select bookId,count(*) as num from book group by bookId')
    cursor.execute(query)
    for (bookId,num) in cursor:
        myDict[bookId] = num
    return myDict
#saving results in a dictionary
books = bookDict()
print(books)
#pannel for teachers
def instructor():
    while True:
        nationalCode = input('national code: ')
        name = input('name: ')
        family = input('family: ')
        instructorId = input('instructor id: ')
        university = input('university: ')
        userName = input('user name: ')
        password = input('password: ')
        if userName.upper() in {x.upper() for x in userNames}:
            print('this user name already exist')
        elif not isValidPass(password):
            print('your password must contain chars and numbers')
        elif nationalCode in nationalCodes:
            print('this national code already exists')
        elif len(nationalCode) != 10:
            print('invalid national code')
        else:
            cursor.execute(add_instructor,(nationalCode,name,family,instructorId,university,
                                           userName,password))
            cursor.execute(add_instructor_account,(nationalCode,0,datetime.date.today()))
            myDB.commit()
            userNames.add(userName)
            nationalCodes.add(nationalCode)
            print('your account made succesfully')
            cursor.close()
            myDB.close()
            break
#pannel for students
def student():
    while True:
        nationalCode = input('national code: ')
        name = input('name: ')
        family = input('family: ')
        studentId = input('student id: ')
        university = input('university: ')
        userName = input('user name: ')
        password = input('password: ')
        if userName.upper() in {x.upper() for x in userNames}:
            print('this user name already exist')
        elif not isValidPass(password):
            print('your password must contain chars and numbers')
        elif nationalCode in nationalCodes:
            print('this national code already exists')
        elif len(nationalCode) != 10:
            print('invalid national code')
        else:
            cursor.execute(add_student,(nationalCode,name,family,studentId,university,
                                           userName,password))
            cursor.execute(add_student_account,(nationalCode,0,datetime.date.today()))
            myDB.commit()
            userNames.add(userName)
            nationalCodes.add(nationalCode)
            print('your account made succesfully')
            cursor.close()
            myDB.close()
            break
#pannel for ordinary people
def ordinary():
    while True:
        nationalCode = input('national code: ')
        name = input('name: ')
        family = input('family: ')
        job = input('job: ')
        userName = input('user name: ')
        password = input('password: ')
        if userName.upper() in {x.upper() for x in userNames}:
            print('this user name already exist')
        elif not isValidPass(password):
            print('your password must contain chars and numbers')
        elif nationalCode in nationalCodes:
            print('this national code already exists')
        elif len(nationalCode) != 10:
            print('invalid national code')
        else:
            cursor.execute(add_ordinary,(nationalCode,name,family,job,userName,password))
            cursor.execute(add_ordinary_account,(nationalCode,0,datetime.date.today()))
            myDB.commit()
            userNames.add(userName)
            nationalCodes.add(nationalCode)
            print('your account made succesfully')
            cursor.close()
            myDB.close()
            break
#function for sign up
def signUp():
    print('1)ordinary\n2)student\n3)instructor')
    choice = int(input('please enter your type: '))
    if choice == 1:
        ordinary()
    elif choice == 2:
        student()
    elif choice == 3:
        instructor()
    else:
        print('invalid input')
        signUp()
#functions below are for ordinary pannel choice
#address adding
def ordinaryAddAddress(userName):
    addressSet = set()
    query = ('select address from ordinary_address where userName = %s')
    cursor.execute(query,(userName,))
    for i in cursor:
        addressSet.add(i[0])
    address = input('enter your address: ')
    if address in addressSet:
        print('this address already exists')
    else:
        query = ('insert into ordinary_address (userName,address) values (%s,%s)')
        cursor.execute(query,(userName,address))
        myDB.commit()
        print('address added successfully')
#phone number adding
def ordinaryAddPhoneNum(userName):
    phoneNumSet = set()
    query = ('select phoneNum from ordinary_phoneNum where userName = %s')
    cursor.execute(query,(userName,))
    for i in cursor:
        phoneNumSet.add(i[0])
    phoneNum = input('enter your phone number: ')
    if phoneNum in phoneNumSet:
        print('this phone number already exists')
    elif  len(phoneNum) != 11 or not phoneNum.isdigit():
        print('invalid phone number')
    else:
        query = ('insert into ordinary_phoneNum (userName,phoneNum) values (%s,%s)')
        cursor.execute(query,(userName,phoneNum))
        myDB.commit()
        print('phone number added successfully')
#showing address and phone numbers
def ordinaryShow_addressAndPhoneNum(userName):
    query1 = ('select address from ordinary_address where userName = %s')
    cursor.execute(query1,(userName,))
    print('address:')
    for address in cursor:
        print(address[0])
    query2 = ('select phoneNum from ordinary_phoneNum where userName = %s')
    cursor.execute(query2,(userName,))
    print('phone Numbers:')
    for phoneNum in cursor:
        print(phoneNum[0])
def ordinary_increase_balance(nationalCode):
    query = ('update ordinary_account set balance = balance + %s where nationalCode = %s')
    money = float(input('enter how much you want add to your account: '))
    cursor.execute(query,(money,nationalCode))
    myDB.commit()
    print('your balance increased successfully')
#function for borrowing books for ordinary people
def ordinaryBorrowBook(nationalCode):
    nonReturnedSet = set()
    query = ('select * from ordinary_account_history natural join history where nationalCode = %s')
    cursor.execute(query,(nationalCode,))
    for i in cursor.fetchall():
        if i[4] == None:
            nonReturnedSet.add(i[6]+'-'+str(i[7]))
    bookId = input('enter book id: ')
    bookNumber = int(input('enter book number: '))
    if bookId+'-'+str(bookNumber) in nonReturnedSet:
        print('you already borrowed this book')
        return
    if bookId not in books:
        print('invalid id')
    elif bookNumber > books[bookId] or bookNumber < 1:
        print('invalid number')
    else:
        query = ('select price from book where bookId = %s and bookNumber = %s')
        cursor.execute(query,(bookId,bookNumber))
        for price in cursor:
            cost = float(price[0])/20
        query1 = ("insert into history (historyId,receivedDate,remainingDays,returnedDate,cost,bookId,bookNumber) values (%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(query1,(len(histories)+1,datetime.date.today(),20,None,cost,bookId,bookNumber))
        query2 = ('insert into ordinary_account_history (nationalCode,historyId) values (%s,%s)')
        cursor.execute(query2,(nationalCode,len(histories)+1))
        histories.add(len(histories)+1)
        myDB.commit()
        print('borrow done successfully')
#function below is for returning book for ordinary people
def ordinaryReturnBook(nationalCode):
    returnedSet = set()
    nonReturnedSet = set()
    query = ('select * from ordinary_account_history natural join history where nationalCode = %s')
    cursor.execute(query,(nationalCode,))
    for i in cursor.fetchall():
        if i[4] == None:
            nonReturnedSet.add(i[6]+'-'+str(i[7]))
        else:
            returnedSet.add(i[6]+'-'+str(i[7]))
    print('returned:')
    print(returnedSet)
    print('non returned')
    print(nonReturnedSet)
    bookId = input('book id: ')
    bookNumber = int(input('book number: '))
    if bookId+'-'+str(bookNumber) not in nonReturnedSet:
        print('invalid book id or number')
    else:
        bquery1 = ('select historyId from ordinary_account_history natural join history where nationalCode = %s and bookId = %s and bookNumber = %s')
        cursor.execute(bquery1,(nationalCode,bookId,bookNumber))
        hId = ''
        for historyId in cursor:
            hId = historyId[0]
        bquery2 = ('update history set returnedDate = %s where historyId = %s')
        cursor.execute(bquery2,(datetime.date.today(),hId))
        myDB.commit()
        print('book returned successfully')
#pannel for ordinary people
def ordinaryPannel(userName):
    while True:
        myNationalCode = ''
        query = ('select * from ordinary where userName = %s')
        print('your information:')
        cursor.execute(query,(userName,))
        for i in cursor.fetchall():
            myNationalCode = i[0]
            print(i)
        print('1)add address\n2)add phone number\n3)increase balcnce\n4)return book\n5)borrow book\n6)search books\n7)see addresses and phone nums\n8)exit')
        choice = int(input('enter the operation you want to do: '))
        if choice == 1:
            ordinaryAddAddress(userName)
        elif choice == 2:
            ordinaryAddPhoneNum(userName)
        elif choice == 3:
            ordinary_increase_balance(myNationalCode)
        elif choice == 4:
            ordinaryReturnBook(myNationalCode)
        elif choice == 5:
            ordinaryBorrowBook(myNationalCode)
        elif choice == 6:
            bookQuery = ('select * from book where field != %s and field != %s')
            cursor.execute(bookQuery,('refrence','educational'))
            print('search result:')
            for i in cursor.fetchall():
                print(i)
        elif choice == 7:
            ordinaryShow_addressAndPhoneNum(userName)
        elif choice == 8:
            cursor.close()
            myDB.close()
            sys.exit()
        else:
            print('invalid input')
#functions below are for teachers pannel choice
#address adding
def instructorAddAddress(userName): 
    addressSet = set()
    query = ('select address from instructor_address where userName = %s')
    cursor.execute(query,(userName,))
    for i in cursor:
        addressSet.add(i[0])
    address = input('enter your address: ')
    if address in addressSet:
        print('this address already exists')
    else:
        query = ('insert into instructor_address (userName,address) values (%s,%s)')
        cursor.execute(query,(userName,address))
        myDB.commit()
        print('address added successfully')
#phone number adding
def instructorAddPhoneNum(userName):
    phoneNumSet = set()
    query = ('select phoneNum from instructor_phoneNum where userName = %s')
    cursor.execute(query,(userName,))
    for i in cursor:
        phoneNumSet.add(i[0])
    phoneNum = input('enter your phone number: ')
    if phoneNum in phoneNumSet:
        print('this phone number already exists')
    elif  len(phoneNum) != 11 or not phoneNum.isdigit():
        print('invalid phone number')
    else:
        query = ('insert into instructor_phoneNum (userName,phoneNum) values (%s,%s)')
        cursor.execute(query,(userName,phoneNum))
        myDB.commit()
        print('phone number added successfully')
#showing address and phone numbers
def instructorShow_addressAndPhoneNum(userName):
    query1 = ('select address from instructor_address where userName = %s')
    cursor.execute(query1,(userName,))
    print('address:')
    for address in cursor:
        print(address[0])
    query2 = ('select phoneNum from instructor_phoneNum where userName = %s')
    cursor.execute(query2,(userName,))
    print('phone Numbers:')
    for phoneNum in cursor:
        print(phoneNum[0])
#teachers increase balance
def instructor_increase_balance(nationalCode):
    query = ('update instructor_account set balance = balance + %s where nationalCode = %s')
    money = float(input('enter how much you want add to your account: '))
    cursor.execute(query,(money,nationalCode))
    myDB.commit()
    print('your balance increased successfully')
#function for borrowing books for instructors
def instructorBorrowBook(nationalCode):
    nonReturnedSet = set()
    query = ('select * from instructor_account_history natural join history where nationalCode = %s')
    cursor.execute(query,(nationalCode,))
    for i in cursor.fetchall():
        if i[4] == None:
            nonReturnedSet.add(i[6]+'-'+str(i[7]))
    bookId = input('enter book id: ')
    bookNumber = int(input('enter book number: '))
    if bookId+'-'+str(bookNumber) in nonReturnedSet:
        print('you already borrowed this book')
        return
    if bookId not in books:
        print('invalid id')
    elif bookNumber > books[bookId] or bookNumber < 1:
        print('invalid number')
    else:
        query = ('select price from book where bookId = %s and bookNumber = %s')
        cursor.execute(query,(bookId,bookNumber))
        for price in cursor:
            cost = float(price[0])/20
        query1 = ("insert into history (historyId,receivedDate,remainingDays,returnedDate,cost,bookId,bookNumber) values (%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(query1,(len(histories)+1,datetime.date.today(),20,None,cost,bookId,bookNumber))
        query2 = ('insert into instructor_account_history (nationalCode,historyId) values (%s,%s)')
        cursor.execute(query2,(nationalCode,len(histories)+1))
        histories.add(len(histories)+1)
        myDB.commit()
        print('borrow done successfully')
#function below is for returning book for teachers
def instructorReturnBook(nationalCode):
    returnedSet = set()
    nonReturnedSet = set()
    query = ('select * from instructor_account_history natural join history where nationalCode = %s')
    cursor.execute(query,(nationalCode,))
    for i in cursor.fetchall():
        if i[4] == None:
            nonReturnedSet.add(i[6]+'-'+str(i[7]))
        else:
            returnedSet.add(i[6]+'-'+str(i[7]))
    print('returned:')
    print(returnedSet)
    print('non returned')
    print(nonReturnedSet)
    bookId = input('book id: ')
    bookNumber = int(input('book number: '))
    if bookId+'-'+str(bookNumber) not in nonReturnedSet:
        print('invalid book id or number')
    else:
        bquery1 = ('select historyId from instructor_account_history natural join history where nationalCode = %s and bookId = %s and bookNumber = %s')
        cursor.execute(bquery1,(nationalCode,bookId,bookNumber))
        hId = ''
        for historyId in cursor:
            hId = historyId[0]
        bquery2 = ('update history set returnedDate = %s where historyId = %s')
        cursor.execute(bquery2,(datetime.date.today(),hId))
        myDB.commit()
        print('book returned successfully')
#pannel for teachers
def instructorPannel(userName):
    while True:
        myNationalCode = ''
        query = ('select * from instructor where userName = %s')
        print('your information:')
        cursor.execute(query,(userName,))
        for i in cursor.fetchall():
            myNationalCode = i[0]
            print(i)
        print('1)add address\n2)add phone number\n3)increase balcnce\n4)return book\n5)borrow book\n6)search books\n7)see addresses and phone nums\n8)exit')
        choice = int(input('enter the operation you want to do: '))
        if choice == 1:
            instructorAddAddress(userName)
        elif choice == 2:
            instructorAddPhoneNum(userName)
        elif choice == 3:
            instructor_increase_balance(myNationalCode)
        elif choice == 4:
            instructorReturnBook(myNationalCode)
        elif choice == 5:
            instructorBorrowBook(myNationalCode)
        elif choice == 6:
            bookQuery = ('select * from book')
            cursor.execute(bookQuery) 
            print('search result:')
            for i in cursor.fetchall():
                print(i)
        elif choice == 7:
            instructorShow_addressAndPhoneNum(userName)
        elif choice == 8:
            cursor.close()
            myDB.close()
            sys.exit()
        else:
            print('invalid input')
#functions below are for student pannel choices
#address adding
def studentAddAddress(userName):
    addressSet = set()
    query = ('select address from student_address where userName = %s')
    cursor.execute(query,(userName,))
    for i in cursor:
        addressSet.add(i[0])
    address = input('enter your address: ')
    if address in addressSet:
        print('this address already exists')
    else:
        query = ('insert into student_address (userName,address) values (%s,%s)')
        cursor.execute(query,(userName,address))
        myDB.commit()
        print('address added successfully')
#phone number adding
def studentAddPhoneNum(userName):
    phoneNumSet = set()
    query = ('select phoneNum from student_phoneNum where userName = %s')
    cursor.execute(query,(userName,))
    for i in cursor:
        phoneNumSet.add(i[0])
    phoneNum = input('enter your phone number: ')
    if phoneNum in phoneNumSet:
        print('this phone number already exists')
    elif  len(phoneNum) != 11 or not phoneNum.isdigit():
        print('invalid phone number')
    else:
        query = ('insert into student_phoneNum (userName,phoneNum) values (%s,%s)')
        cursor.execute(query,(userName,phoneNum))
        myDB.commit()
        print('phone number added successfully')
#showing addresses and phone numbers
def studentShow_addressAndPhoneNum(userName):
    query1 = ('select address from student_address where userName = %s')
    cursor.execute(query1,(userName,))
    print('address:')
    for address in cursor:
        print(address[0])
    query2 = ('select phoneNum from student_phoneNum where userName = %s')
    cursor.execute(query2,(userName,))
    print('phone Numbers:')
    for phoneNum in cursor:
        print(phoneNum[0])
#increase student balance
def student_increase_balance(nationalCode):
    query = ('update student_account set balance = balance + %s where nationalCode = %s')
    money = float(input('enter how much you want add to your account: '))
    cursor.execute(query,(money,nationalCode))
    myDB.commit()
    print('your balance increased successfully')
#function for borrowing books for students
def studentBorrowBook(nationalCode):
    nonReturnedSet = set()
    query = ('select * from student_account_history natural join history where nationalCode = %s')
    cursor.execute(query,(nationalCode,))
    for i in cursor.fetchall():
        if i[4] == None:
            nonReturnedSet.add(i[6]+'-'+str(i[7]))
    bookId = input('enter book id: ')
    bookNumber = int(input('enter book number: '))
    if bookId+'-'+str(bookNumber) in nonReturnedSet:
        print('you already borrowed this book')
        return
    if bookId not in books:
        print('invalid id')
    elif bookNumber > books[bookId] or bookNumber < 1:
        print('invalid number')
    else:
        query = ('select price from book where bookId = %s and bookNumber = %s')
        cursor.execute(query,(bookId,bookNumber))
        for price in cursor:
            cost = float(price[0])/20
        query1 = ("insert into history (historyId,receivedDate,remainingDays,returnedDate,cost,bookId,bookNumber) values (%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(query1,(len(histories)+1,datetime.date.today(),20,None,cost,bookId,bookNumber))
        query2 = ('insert into student_account_history (nationalCode,historyId) values (%s,%s)')
        cursor.execute(query2,(nationalCode,len(histories)+1))
        histories.add(len(histories)+1) 
        myDB.commit()
        print('borrow done successfully')
#function below is for returning book for students
def studentReturnBook(nationalCode):
    returnedSet = set()
    nonReturnedSet = set()
    query = ('select * from student_account_history natural join history where nationalCode = %s')
    cursor.execute(query,(nationalCode,))
    for i in cursor.fetchall():
        if i[4] == None:
            nonReturnedSet.add(i[6]+'-'+str(i[7]))
        else:
            returnedSet.add(i[6]+'-'+str(i[7]))
    print('returned:')
    print(returnedSet)
    print('non returned')
    print(nonReturnedSet)
    bookId = input('book id: ')
    bookNumber = int(input('book number: '))
    if bookId+'-'+str(bookNumber) not in nonReturnedSet:
        print('invalid book id or number')
    else:
        bquery1 = ('select historyId from student_account_history natural join history where nationalCode = %s and bookId = %s and bookNumber = %s')
        cursor.execute(bquery1,(nationalCode,bookId,bookNumber))
        hId = ''
        for historyId in cursor:
            hId = historyId[0]
        bquery2 = ('update history set returnedDate = %s where historyId = %s')
        cursor.execute(bquery2,(datetime.date.today(),hId))
        myDB.commit()
        print('book returned successfully') 
#pannel for students
def studentPannel(userName):
    while True:
        myNationalCode = ''
        query = ('select * from student where userName = %s')
        print('your information:')
        cursor.execute(query,(userName,))
        for i in cursor.fetchall():
            myNationalCode = i[0]
            print(i)
        print('1)add address\n2)add phone number\n3)increase balcnce\n4)return book\n5)borrow book\n6)search books\n7)see addresses and phone nums\n8)exit')
        choice = int(input('enter the operation you want to do: '))
        if choice == 1:
            studentAddAddress(userName)
        elif choice == 2:
            studentAddPhoneNum(userName)
        elif choice == 3:
            student_increase_balance(myNationalCode)
        elif choice == 4:
            studentReturnBook(myNationalCode)
        elif choice == 5:
            studentBorrowBook(myNationalCode)
        elif choice == 6:
            bookQuery = ('select * from book where field != %s')
            cursor.execute(bookQuery,('refrence',))
            print('search result:')
            for i in cursor.fetchall():
                print(i)
        elif choice == 7:
            studentShow_addressAndPhoneNum(userName)
        elif choice == 8:
            cursor.close()
            myDB.close()
            sys.exit()
        else:
            print('invalid input')
#sign in pannel for students
def studentSignIn():
    userName = ''
    password = ''
    while True:
        userName = input('please enter your userName: ')
        password = input('please enter your password: ')
        if userName not in userNames:
            print('no such user name')
        else:
            query = ('select password from student where userName = %s')
            cursor.execute(query,(userName,))
            #extracting password
            for i in cursor.fetchall():
                x = i[0]
            if password == x:
                break
            else:
                print('wrong password')
    studentPannel(userName)            
#sign in pannel for teachers
def instructorSignIn():
    userName = ''
    password = ''
    while True:
        userName = input('please enter your userName: ')
        password = input('please enter your password: ')
        if userName not in userNames:
            print('no such user name')
        else:
            query = ('select password from instructor where userName = %s')
            cursor.execute(query,(userName,))
            #extracting password
            for i in cursor.fetchall():
                x = i[0]
            if password == x:
                break
            else:
                print('wrong password')
    instructorPannel(userName)
#sign in pannel for ordinary people
def ordinarySignIn():
    userName = ''
    password = ''
    while True:
        userName = input('please enter your userName: ')
        password = input('please enter your password: ')
        if userName not in userNames:
            print('no such user name')
        else:
            query = ('select password from ordinary where userName = %s')
            cursor.execute(query,(userName,))
            #extracting password
            for i in cursor.fetchall():
                x = i[0]
            if password == x:
                break
            else:
                print('wrong password')
    ordinaryPannel(userName)
#function for sign in
def signIn():
    print('1)student\n2)instructor\n3)ordinary')
    type = int(input('enter which type are you: '))
    if type == 1:
        studentSignIn()
    elif type == 2:
        instructorSignIn()
    elif type == 3:
        ordinarySignIn()
    else:
        print('invalid input')
        signIn()
#function below is for sing in/up
def signInOrUp():
    print('1)sign in\n2)sign up')
    choice = int(input('please enter action you want to do: '))
    if choice == 1:
        signIn()
    elif choice == 2:
        signUp()
    else:
        print('invalid input')
        signInOrUp()
#this func is for admin pannel
def adminPannel():
    userName = input('enter user name: ')
    password = input('enter password: ')
#function below is for showing main pannel
def mainPannel():
    print('1)admin\n2)user\n3)exit')
    myType = int(input('please insert your type: '))
    if myType == 1:
        adminPannel()
    elif myType == 2:
        signInOrUp()
    elif myType == 3:
        cursor.close()
        myDB.close()
        sys.exit()
    else:
        print('ivalid input')
        mainPannel()
mainPannel()