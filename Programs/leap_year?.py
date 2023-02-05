# Check the given year is a Leap Year or not

def leap_year():
    print(" *** Leap Year or Not... ***")
    year = int(input("Enter a year: "))
    if (year % 400 == 0) and (year % 100 == 0):
        print(f"{year} is a leap year")
    elif (year % 4 == 0) and (year % 100 != 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year...")


if __name__ == '__main__':
    leap_year()
