cube = lambda No1 : No1*No1*No1

def main():

    No1 = int(input("Enter your Number :"))
    ret = cube(No1)
    print("cube is:",ret)

if __name__ == "__main__":
    main()