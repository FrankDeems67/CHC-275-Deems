
def makeList():
    nums = []
    user_input = input("Enter a number or type 'stop': ")

    while user_input != "stop":
        nums.append(int(user_input))
        user_input = input("Enter a number or type 'stop': ")

    return nums


list1 = makeList()
print(list1)

list2 = makeList()
print(list2)