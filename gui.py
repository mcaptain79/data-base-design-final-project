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
#pannel for ordinary people
def ordinaryPannel(userName):
    query = ('select * from ordinary where userName = %s')
    print('your information:')
    cursor.execute(query,(userName,))
    for i in cursor.fetchall():
        print(i)
    cursor.close()
    myDB.close()
#pannel for teachers
def instructorPannel(userName):
    query = ('select * from instructor where userName = %s')
    print('your information:')
    cursor.execute(query,(userName,))
    for i in cursor.fetchall():
        print(i)
    cursor.close()
    myDB.close()
#pannel for students
def studentPannel(userName):
    query = ('select * from student where userName = %s')
    print('your information:')
    cursor.execute(query,(userName,))
    for i in cursor.fetchall():
        print(i)
    cursor.close()
    myDB.close()
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