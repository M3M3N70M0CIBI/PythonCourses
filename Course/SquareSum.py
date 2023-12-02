# Complete the square sum function so that it squares each number passed into it and then sums the results together.


a = [1, 2, 2]


def square_sum(x):
    return sum(list(map(lambda a: a ** 2, x)))
    


print(square_sum(a))