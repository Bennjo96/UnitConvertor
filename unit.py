# Project 1
# Simple Unit convertor Program Demo.

def print_menu():
    print('1. kilometers to miles')
    print('2. miles to kilometers')
    print('3. close the program')

    while True:
        choice = input('Enter your number of choice (1, 2 or 3)?: ')
        if choice == "1":
            km_miles()
        elif choice == "2":
            miles_km()
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


print_menu()
