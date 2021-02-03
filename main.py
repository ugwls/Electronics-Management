import device_db as db
from device import d


k = True
while k:
    d.clear()
    print('\t\t\t\tMenu', end='')
    print('''
1.Add Device in device list
2.Add Device Info
3.Update Decvice Info
4.Delete Decvie in device list
5.Delete Decvie Info
6.See Device list
7.See Device Info
8.Exit
    ''')
    menu = int(input('Enter your option(1/8): '))
    if menu <= 7:
        d.clear()
        if menu == 1:
            d.clear()
            d.list_add()
            d.clear()
        elif menu == 2:
            d.clear()
            d.info_add()
            d.clear()
        elif menu == 3:
            d.clear()
            d.info_update()
            d.clear()
        elif menu == 4:
            d.clear()
            d.list_delete()
            d.clear()
        elif menu == 5:
            d.clear()
            db.delete()
            d.clear()
        elif menu == 6:
            d.clear()
            d.list_see()
            d.clear()
        elif menu == 7:
            d.clear()
            db.see_details()
            d.clear()
    elif menu == 8:
        d.clear()
        d.end()
        break
    else:
        d.clear()
        print('Invalid Option...')
        input('Press Enter to continue...')
        continue
