def getMin(userList):
    min_value = userList[0]
    
    i = 1
    while i < len(userList):
        if userList[i] < min_value:
            min_value = userList[i]
        i += 1
    
    return min_value

list1 = [1, 2, 3, 4]
list2 = [4, 2, 1, 3]

print(getMin(list1)) 
print(getMin(list2)) 