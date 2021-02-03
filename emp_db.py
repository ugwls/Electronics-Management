import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ujjw@l.16")
cur = mydb.cursor()
cur.execute('create database if not exists electronics')
cur.execute('use electronics')
mydb.commit()

table = '''
create table if not exists emp(
emp_no int  AUTO_INCREMENT, 
f_name varchar(50), 
l_name varchar(50),
modile_no varchar(30),
address varchar(50),
salary varchar(50),
primary key (emp_no))
'''
cur.execute(table)
mydb.commit()


def add_devices():
    k = True
    while k == True:
        print('Enter the details :')
        s = 'insert into emp (f_name, l_name, modile_no, address, salary)' \
            'values(%s,%s,%s,%s,%s) '
        f_name = input('Enter First name: ')
        l_name = input('Enter Last name: ')
        modile_no = input('Enter modile no.: ')
        address = input('Enter address: ')
        salary = input('Enter salary: ')
        value = (f_name, l_name, modile_no, address, 'Rs.' + salary)
        cur.execute(s, value)
        mydb.commit()
        a = input(
            'Do you want to add more record in (y/n): ').lower()
        if a == 'y':
            continue
        else:
            k = False
        print("Successfully updated!!!!!!!!")


def delete():
    emp_no = input('Enter emp no. you want to delete: ')
    s = 'DELETE FROM emp WHERE emp_no = %s'
    value = (emp_no,)
    cur.execute(s, value)
    mydb.commit()
    print('Successfully deleted!!!!!!')
    input('Press ENTER to continue.....')


def update():
    s1 = 'select * from emp'
    cur.execute(s1)
    result = cur.fetchall()
    for rec in result:
        print(rec)
    emp_no = input('Enter emp no.: ')
    s = "update emp set f_name= %s, l_name= %s, modile_no= %s, address= %s, salary= %s where emp_no= %s "
    f_name = input('Enter First name: ')
    l_name = input('Enter Last name: ')
    modile_no = input('Enter modile no.: ')
    address = input('Enter address: ')
    salary = input('Enter salary: ')
    value = (f_name, l_name, modile_no, address, 'Rs.' + salary, emp_no)
    cur.execute(s, value)
    mydb.commit()
    print("Successfully updated!!!!!!!!")
    input('Press ENTER to continue.....')


def see_details():
    s = 'select * from emp'
    cur.execute(s)
    result = cur.fetchall()
    for rec in result:
        print(rec)
    input('Press ENTER to continue.....')
