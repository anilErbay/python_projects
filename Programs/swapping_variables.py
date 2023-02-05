# swap variables

def user_input(x, y):
    x = int(input("Enter value of x in integer: "))
    y = int(input("Enter value of y in integer: "))
    print("** ** **")
    print(f"x: {x}\ny: {y}")
    print()

    def swap(x, y):
        temp = x
        x = y
        y = temp
        print("After Swapping")
        print(f"Value of x: {x}")
        print(f"Value of y: {y}")
    swap(x, y)
    return True


def main():
    x = 0
    y = 0
    result = user_input(x, y)


if __name__ == '__main__':
    main()
