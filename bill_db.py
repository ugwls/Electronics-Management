import mysql.connector
import datetime as dt
import random as r

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ujjw@l.16")
cur = mydb.cursor()
cur.execute('create database if not exists electronics')
cur.execute('use electronics')
mydb.commit()

table = '''
create table if not exists cus(
cus_no int  AUTO_INCREMENT, 
f_name varchar(50), 
l_name varchar(50),
modile_no varchar(30),
address varchar(50),
email varchar(50),
primary key (cus_no))
'''
cur.execute(table)
mydb.commit()


def add_devices():
    k = True
    while k == True:
        print('Enter the details :')
        s = 'insert into cus (f_name, l_name, modile_no, address, email)' \
            'values(%s,%s,%s,%s,%s) '
        f_name = input('Enter First name: ')
        l_name = input('Enter Last name: ')
        modile_no = input('Enter modile no.: ')
        address = input('Enter address: ')
        email = input('Enter email: ')
        value = (f_name, l_name, modile_no, address, email)
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
    s1 = 'select * from cus'
    cur.execute(s1)
    result = cur.fetchall()
    for rec in result:
        print(rec)
    cus_no = input('Enter cus no. you want to delete: ')
    s = 'DELETE FROM cus WHERE cus_no = %s'
    value = (cus_no,)
    cur.execute(s, value)
    mydb.commit()
    print('Successfully deleted!!!!!!')
    input('Press ENTER to continue.....')


def update():
    s1 = 'select * from cus'
    cur.execute(s1)
    result = cur.fetchall()
    for rec in result:
        print(rec)
    cus_no = input('Enter cus no.: ')
    s = "update cus set f_name= %s, l_name= %s, modile_no= %s, address= %s, email= %s where cus_no= %s "
    f_name = input('Enter First name: ')
    l_name = input('Enter Last name: ')
    modile_no = input('Enter modile no.: ')
    address = input('Enter address: ')
    email = input('Enter email: ')
    value = (f_name, l_name, modile_no, address, email, cus_no)
    cur.execute(s, value)
    mydb.commit()
    print("Successfully updated!!!!!!!!")
    input('Press ENTER to continue.....')


def see_details():
    s = 'select * from cus'
    cur.execute(s)
    result = cur.fetchall()
    for rec in result:
        print(rec)
    input('Press ENTER to continue.....')


def bill_gen():
    s = 'select * from cus'
    cur.execute(s)
    result = cur.fetchall()
    for rec in result:
        print(rec)
    cus_no = input('Enter Customer no. of whom you want to Generate Bill: ')
    device = input('Enter which Device you have purchased: ')
    brand = input('Enter Brand name: ')
    model = input('Enter Model: ')
    qty = int(input('Enter Quantity: '))

    # updating device table
    s1 = 'select * from all_devices where device=%s and brand=%s and model=%s '
    value = (device, brand, model)
    cur.execute(s1, value)
    result = cur.fetchall()
    for rec in result:
        s = 'insert into all_devices (item_id, device, brand, model, quantity, price_per_unit, MRP)' \
            'values(%s,%s,%s,%s,%s,%s,%s) '
        quantity = rec[5] - qty
        if quantity < 0:
            a = input(f'''We don't have enough {device} available,
                    we only have{rec[5]} do you want continue with this only(y / n). ''')
            if a == 'y':
                quantity = rec[5]
            elif a == 'n':
                print('Sorry')
                break
        value = (rec[1], device, brand, model,
                 quantity, rec[6], rec[7])
        cur.execute(s, value)
        # (1, 'lap001', 'Laptops', 'samsung', 'i7', 5, 'Rs.39999', 'Rs.34999')
        up = int(rec[6].lstrip('Rs.'))

    # Generating Bill
    s2 = 'select * from cus where cus_no= %s'
    value = (cus_no,)
    cur.execute(s2, value)
    result = cur.fetchall()
    for rec in result:
        f_name = f'bill-{rec[1]}.txt'
        with open(f_name, 'w+') as f:
            f.write(f'''
                        Bill
XYZ Company
Gurugram                                   INVOICE
1200-800-444                                {dt.datetime.now().date()}
                                        {r.randint(10001, 99999)}
------------------------------------------------------
Bill To
Contact Name: {rec[1]}
Phone: {rec[3]}
Address: {rec[4]}
Email: {rec[5]}

|    DESCRIPTION    |  QTY  |  UNIT PRICE  |  TOTAL  |
{brand, model}      | {qty} | {up}         | {qty*up}|

                                Subtotal:{qty*up}
                                Discount: 20%
                                Tax Rate: 18%
                               Total Tax:{(qty*up)*.18 }
                               -----------------------
                             Balance Due:{(qty*up)+((qty*up)*.18)-((qty*up)*.2)}
            
                    ''')
        pass
