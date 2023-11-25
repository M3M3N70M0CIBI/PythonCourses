# Your task is to find the first element of an array that is not consecutive.

# By not consecutive we mean not exactly 1 larger than the previous element of the array.

# E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's the first non-consecutive number.

# If the whole array is consecutive then return null2.

# The array will always have at least 2 elements1 and all elements will be numbers. 

# The numbers will also all be unique and in ascending order. The numbers could be positive or negative and the first non-consecutive could be either too!

CONST_EXAMPLE = {'1': [1,3,4,5,6,7],
                 '2': [-2,-1,0,1,2,3,1,4,7],
                 '3': [-3,-1,0,1,2,3,4,5,6]}

def consecutive(array):
    for i in range(1, len(array)):
        if array[i - 1] + 1 != array[i]:
            return array[i]

print(consecutive(CONST_EXAMPLE['2']))