import db
import add
import update
import random
import pyfiglet
from os import system


def clear(): return system('cls')


def end():
    with open("font.txt", "r") as f:
        font = f.readlines()
        font = [x.strip('\n') for x in font]
    print(pyfiglet.figlet_format("Thank You", font=random.choice(font)))


def add_device():
    name = input('Enter device name: ')
    with open('devices.txt', "a") as f:
        f.write(f'{name}\n')


k = True
while k:
    clear()
    print('\t\t\t\tMenu', end='')
    print('''
1.Add Device in Database
2.Add record in tables
3.Update a table
4.Delete a Item
5.See Details
6.Exit
        ''')
    menu = int(input('Enter your option(1/6): '))
    if menu <= 5:
        clear()
        if menu == 1:
            clear()
            add_device()
            clear()
        elif menu == 2:
            clear()
            add.submenu()
            clear()
        elif menu == 3:
            clear()
            update.submenu()
            clear()
        elif menu == 4:
            clear()
            db.delete()
            clear()
        elif menu == 5:
            clear()
            db.see_details()
            clear()
    elif menu == 6:
        clear()
        end()
        break
    else:
        clear()
        print('Invalid Option...')
        input('Press Enter to continue...')
        continue
