import emp_db as db
from os import system
import random


def clear(): return system('cls')


def submenu():
    k = True
    while k:
        clear()
        print('\t\t\t\tEmployee Management', end='')
        print('''
1.Add Employee Info
2.Update Employee Info
3.Delete Employee Info
4.See Employee Info
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
