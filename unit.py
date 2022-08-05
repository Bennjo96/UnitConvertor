# Project 1
# Simple Unit convertor Program Demo.

def print_menu():
    print('1. kilometers to miles')
    print('2. miles to kilometers')
    print('3. hours to minutes')
    print('4. minutes to hours')
    print('5. close the program')

    while True:
        choice = input('Enter your number of choice (1, 2 , 3, 4 or 5)?: ')
        if choice == "1":
            km_miles()
        elif choice == "2":
            miles_km()
        elif choice == "3":
            min_hr()
        elif choice == "4":
            hr_min()
        else:
            print('Exiting...')
            break


def km_miles():
    km = float(input('Enter a distance in km : '))
    miles = km / 1.609
    print(f"Distance in miles : {miles}")


def miles_km():
    miles = float(input('Enter a distance in miles : '))
    km = miles * 1.609
    print(f"Distance in kilometres : {km}")


def min_hr():
    min = float(input('Enter time in minutes : '))
    hr = min / 60
    print(f"minutes in Hours : {hr}")


def hr_min():
    hr = float(input('Enter time in hours : '))
    min = hr * 60
    print(f"minutes in Hours : {min}")


print_menu()
