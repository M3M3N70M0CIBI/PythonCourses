# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

def find_next_square(sq):
    if sq ** 0.5 % 1 == 0:
        return int(sq ** 0.5 + 1) ** 2
    else:
        return -1

test = [1, 3, 2, 4, 121, 132, 625]

print(*list(map(find_next_square, test)))