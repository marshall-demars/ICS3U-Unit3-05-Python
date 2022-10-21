#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: October 2022
# This program uses select case to find months of the year
#    with user input


def main():
    # this uses  select case to find months of the year

    # input
    print("Each number represents a month of the year (ex 1 = december):")
    user_month = int(input("Enter a number between 1 and 12:"))

    # process and output
    match user_month:
        case 1:
            print("You chose January!")
        case 2:
            print("You chose February!")
        case 3:
            print("You chose March!")
        case 4:
            print("You chose April!")
        case 5:
            print("You chose May!")
        case 6:
            print("You chose June!")
        case 7:
            print("You chose July!")
        case 8:
            print("You chose August!")
        case 9:
            print("You chose September!")
        case 10:
            print("You chose October!")
        case 11:
            print("You chose November!")
        case 12:
            print("You chose December!")
        case _:
            print("Not a month.")

    print("\nDone.")


if __name__ == "__main__":
    main()
