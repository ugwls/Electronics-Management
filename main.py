import db
from func import func


k = True
while k:
    func.clear()
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
        func.clear()
        if menu == 1:
            func.clear()
            func.add_device()
            func.clear()
        elif menu == 2:
            func.clear()
            func.add()
            func.clear()
        elif menu == 3:
            func.clear()
            func.update()
            func.clear()
        elif menu == 4:
            func.clear()
            db.delete()
            func.clear()
        elif menu == 5:
            func.clear()
            db.see_details()
            func.clear()
    elif menu == 6:
        func.clear()
        func.end()
        break
    else:
        func.clear()
        print('Invalid Option...')
        input('Press Enter to continue...')
        continue
