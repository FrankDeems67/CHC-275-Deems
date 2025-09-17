"""x=1
while x <=10:
        print(x)
        x=x+1
"""
check = False
while check == False:
        print("option 1")
        print("option 2")
        print("option 3")
        option = input("Select your option or type quit to exit")
        if option == "1":
                print(1)
        elif option == "2":
                print(2)
        elif option == "3":
                print(3)
        elif option == "quit":
                check = True4