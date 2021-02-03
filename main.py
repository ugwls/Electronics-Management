import db
from device import d


k = True
while k:
    d.clear()
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
        d.clear()
        if menu == 1:
            d.clear()
            d.add_device()
            d.clear()
        elif menu == 2:
            d.clear()
            d.add()
            d.clear()
        elif menu == 3:
            d.clear()
            d.update()
            d.clear()
        elif menu == 4:
            d.clear()
            db.delete()
            d.clear()
        elif menu == 5:
            d.clear()
            db.see_details()
            d.clear()
    elif menu == 6:
        d.clear()
        d.end()
        break
    else:
        d.clear()
        print('Invalid Option...')
        input('Press Enter to continue...')
        continue
