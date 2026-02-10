import math

def getList():
    nums = input("Enter numbers separated by spaces: ")
    return [int(x) for x in nums.split()]

def printList(lst):
    print("List:", lst)

def getMin(lst):
    minimum = lst[0]
    for num in lst:
        if num < minimum:
            minimum = num
    return minimum

def getMax(lst):
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum

def getMean(lst):
    total = 0
    for num in lst:
        total += num
    return total / len(lst)

def getMedian(lst):
    sorted_list = sorted(lst)
    n = len(sorted_list)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        return sorted_list[mid]

def getStdDev(lst):
    mean = getMean(lst)
    total = 0

    for num in lst:
        total += (num - mean) ** 2

    variance = total / len(lst)   # population variance
    return math.sqrt(variance)

def printMenu():
    print("\nStatistics Calculator")
    print("1. Get Minimum")
    print("2. Get Maximum")
    print("3. Get Mean")
    print("4. Get Median")
    print("5. Get Standard Deviation")
    print("6. Exit")