# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

TestArr = [59, 230, 5593, 1923, 2045, 1200]

century = lambda year: print(1) if year <= 100 else print(year // 100) if (year % 100 == 0) else print(year // 100 + 1) 

for obj in TestArr:
    century(obj)
