# Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).
#  The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.


dad = 36

son = 7

def twice_as_old(dad_years_old, son_years_old):
    return abs((dad_years_old - 2 * son_years_old))

print(twice_as_old(dad, son))