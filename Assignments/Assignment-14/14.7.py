Divby5 = lambda No1: True if No1%5 == 0 else False

def main():
    No1 = int(input("Enter your Number : "))
    ret = Divby5(No1)

    if(ret == True):
        print("It is Divisible by 5")
    else:
        print("It is not Divisible by 5")


if __name__ == "__main__":
    main()
