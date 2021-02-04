import emp_main as emp
import billing as b
import device_main as device
import pyfiglet as pf
import random as r
from os import system


def clear(): return system('cls')


def end():
    with open("font.txt", "r") as f:
        font = f.readlines()
        font = [x.strip('\n') for x in font]
    print(pf.figlet_format("Thank You", font=r.choice(font)))


k = True
while k == True:
    clear()
    print('\t\t\t\tMenu', end='')
    print('''
1.Device Management
2.Employee Management
3.Billing Management
4.Exit
        ''')
    menu = int(input('Enter your option(1/4): '))
    if menu <= 3:
        clear()
        if menu == 1:
            clear()
            device.submenu()
            clear()
        elif menu == 2:
            clear()
            emp.submenu()
            clear()
        elif menu == 3:
            clear()
            b.submenu()
            clear()
    elif menu == 4:
        clear()
        end()
        break
    else:
        clear()
        print('Invalid Option...')
        input('Press Enter to continue...')
        continue
