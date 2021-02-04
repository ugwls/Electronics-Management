import bill_db as db
from os import system


def clear(): return system('cls')


def gen_bill():
    pass


def submenu():
    k = True
    while k:
        clear()
        print('\t\t\t\tCustomer Management', end='')
        print('''
1.Add Customer Info
2.Update Customer Info
3.Delete Customer Info
4.See Customer Info
5.Generate Bill
5.Go To Main Page
            ''')
        menu = int(input('Enter your option(1/5): '))
        if menu <= 4:
            clear()
            if menu == 1:
                clear()
                db.add_devices()
                clear()
            elif menu == 2:
                clear()
                db.update()
                clear()
            elif menu == 3:
                clear()
                db.delete()
                clear()
            elif menu == 4:
                clear()
                db.see_details()
                clear()
        elif menu == 5:
            clear()
            break
        else:
            clear()
            print('Invalid Option...')
            input('Press Enter to continue...')
            continue
