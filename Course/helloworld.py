# course begin
print("Hello world")

print("3 + 5 =", str(3+5), sep= " ", end="!\n")

a, b, c = input("Your example: ").split()

a, c = int(a), int(c)

ArifFunc = {'+': a + c, '-': a - c, '*': a * c, '/': a / c}
    
print('Answer to:', str(a), b, str(c), '=', ArifFunc[b])