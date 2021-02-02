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
create table if not exists all_devices(
item_no int  AUTO_INCREMENT, 
item_id varchar(50), 
Device varchar(50),
Brand varchar(30),
Model varchar(50),
Quantity int,
Price_per_unit varchar(30),
MRP varchar(30),
primary key (item_no))
'''
cur.execute(table)
mydb.commit()


def add_devices(db_device):
    print('Enter the details :')
    s = 'insert into all_devices (item_id, device, brand, model, quantity, price_per_unit, MRP)' \
        'values(%s,%s,%s,%s,%s,%s,%s) '
    item_id = input('Enter Item id: ')
    device = db_device
    brand = input('Enter Brand name: ')
    model = input('Enter Model name: ')
    quantity = int(input('Enter Quantity: '))
    price = input('Enter Price: ')
    mrp = input('Enter MRP: ')
    value = (item_id, device, brand, model,
             quantity, 'Rs.' + price, 'Rs.' + mrp)
    cur.execute(s, value)
    mydb.commit()
    print("Successfully updated!!!!!!!!")


def delete():
    item_id = input('Enter item id you want to delete: ')
    s = 'DELETE FROM all_devices WHERE item_id = %s'
    value = (item_id,)
    cur.execute(s, value)
    mydb.commit()
    print('Successfully deleted!!!!!!')
    input('Press ENTER to continue.....')


def update(db_device):
    s1 = 'select * from all_devices where device=%s'
    value = (db_device,)
    cur.execute(s1, value)
    result = cur.fetchall()
    for rec in result:
        print(rec)
    s = "update all_devices set item_id= %s, brand= %s, model= %s, quantity= %s, price_per_unit= %s, " \
        "MRP= %s where item_no= %s "
    item_no = int(input('Enter Item no.: '))
    item_id = input('Enter Item id: ')
    brand = input('Enter Brand name: ')
    model = input('Enter Model name: ')
    quantity = int(input('Enter Quantity: '))
    price = input('Enter Price: ')
    mrp = input('Enter MRP: ')
    value = (item_id, brand, model, quantity,
             'Rs.' + price, 'Rs.' + mrp, item_no)
    cur.execute(s, value)
    mydb.commit()
    print("Successfully updated!!!!!!!!")


def see_details():
    s = 'select * from all_devices'
    cur.execute(s)
    result = cur.fetchall()
    for rec in result:
        print(rec)
    input('Press ENTER to continue.....')
