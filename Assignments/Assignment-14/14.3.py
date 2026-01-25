Maximum = lambda No1, No2: No1 if No1 > No2 else No2

def main():
    No1 = int(input("Enter your Number : "))
    No2 = int(input("Enter your Number : "))
    ret = Maximum(No1, No2)
    print("Maximum is:", ret)

if __name__ == "__main__":
    main()
