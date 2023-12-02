# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?


make_negative = lambda x: x*-1 if x > 0 else x


print(make_negative(-5))