import db as db
from os import system


def clear(): return system('cls')


def submenu():
    with open("devices.txt", "r") as f:
        d = f.readlines()
        d = [x.strip('\n') for x in d]
        d_name = {}
        for index, value in enumerate(d):
            d_name[index+1] = value

    l = len(d)
    k = True
    while k == True:
        clear()
        print('\t\t\tSelect the Device to Add')
        for i in d_name:
            print(f'Enter {i} for {d_name[i]}')
        print(f"Enter {l + 1} to go to Main Menu")
        n = int(input('Enter your option: '))
        if n <= l:
            clear()
            for i in d_name:
                if n == i:
                    db.add_devices(d_name[i])
                    k = False
        elif n == l + 1:
            clear()
            break
        else:
            clear()
            print('Invalid Option...')
            input('Press Enter to continue...')
            continue
