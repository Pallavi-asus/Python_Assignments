Odd = lambda No1: True if No1%2 != 0 else False

def main():
    No1 = int(input("Enter your Number : "))
    ret = Odd(No1)

    if(ret == True):
        print("It is a odd number")
    else:
        print("It is not a odd number")


if __name__ == "__main__":
    main()
