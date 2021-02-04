import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ujjw@l.16")
cur = mydb.cursor()
cur.execute('create database if not exists electronics')
cur.execute('use electronics')
mydb.commit()

device = '''
INSERT INTO all_devices(
item_id, Device, Brand, Model, Quantity, Price_per_unit, MRP)
VALUES
('','','','',,'',''),
('','','','',,'',''),
('','','','',,'',''),
('','','','',,'',''),
('','','','',,'',''),
('','','','',,'','')
'''
cur.execute(device)

emp = '''
INSERT INTO emp( 
f_name, l_name, modile_no, address, salary)
VALUES
('','','','',''),
('','','','',''),
('','','','',''),
('','','','',''),
('','','','',''),
('','','','','')
'''
cur.execute(emp)

cus = '''
INSERT INTO emp( 
f_name, l_name, modile_no, address, email)
VALUES
('','','','',''),
('','','','',''),
('','','','',''),
('','','','',''),
('','','','',''),
('','','','','')
'''
cur.execute(cus)
