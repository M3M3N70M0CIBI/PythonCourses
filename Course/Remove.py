# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

TestArray = [1, 2, 3, 4, 5, 2, 5, 3, 3, 2, 1, 2, 34, 5, 345, 3, 1, 22, 3, 5, 4, 2, 4, 5, 2, 5, 2, 4, 5]

# def removeEveryOther(list):
#     eOTList = []
#     for i in range(len(list)):
#         if i % 2 == 0:
#             eOTList.append(list[i])
#     return eOTList

def remove_every_other(list):
    return list[::2]

print(remove_every_other(TestArray))