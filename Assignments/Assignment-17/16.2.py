Even = lambda No1: True if No1 % 2 == 0 else False

def main():
    No1 = int(input("Enter your Number : "))
    ret = Even(No1)

    if(ret == True):
        print("It is an even number")
    else:
        print("It is a Odd number")


if __name__ == "__main__":
    main()
