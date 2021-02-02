import db
import random
import pyfiglet
from os import system


class func():

    def clear(self):
        return system('cls')

    @staticmethod
    def end():
        with open("font.txt", "r") as f:
            font = f.readlines()
            font = [x.strip('\n') for x in font]
        print(pyfiglet.figlet_format("Thank You", font=random.choice(font)))

    @staticmethod
    def add_device(self):
        name = input('Enter device name: ')
        with open('devices.txt', "a") as f:
            f.write(f'{name}\n')

    @staticmethod
    def add(self):
        with open("devices.txt", "r") as f:
            d = f.readlines()
            d = [x.strip('\n') for x in d]
            d_name = {}
            for index, value in enumerate(d):
                d_name[index+1] = value

        l = len(d)
        k = True
        while k == True:
            self.clear()
            print('\t\t\tSelect the Device to Add')
            for i in d_name:
                print(f'Enter {i} for {d_name[i]}')
            print(f"Enter {l + 1} to go to Main Menu")
            n = int(input('Enter your option: '))
            if n <= l:
                self.clear()
                for i in d_name:
                    if n == i:
                        db.add_devices(d_name[i])
                        k = False
            elif n == l + 1:
                self.clear()
                break
            else:
                self.clear()
                print('Invalid Option...')
                input('Press Enter to continue...')
                continue

    @staticmethod
    def update(self):
        with open("devices.txt", "r") as f:
            d = f.readlines()
            d = [x.strip('\n') for x in d]
            d_name = {}
            for index, value in enumerate(d):
                d_name[index+1] = value

        l = len(d)
        k = True
        while k == True:
            self.clear()
            print('\t\t\tSelect the Device to Update')
            for i in d_name:
                print(f'Enter {i} for {d_name[i]}')
            print(f"Enter {l + 1} to go to Main Menu")
            n = int(input('Enter your option: '))
            if n <= l:
                self.clear()
                for i in d_name:
                    if n == i:
                        db.update(d_name[i])
                        k = False
            elif n == l + 1:
                self.clear()
                break
            else:
                self.clear()
                print('Invalid Option...')
                input('Press Enter to continue...')
                continue
