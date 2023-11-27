def area_of_perimeter(l, w):
    return l * w * (l == w) + ( 2 * (w + l) * (l != w))

squareRectangle = lambda l, w: l * w if l == w else (l + w) * 2

print(area_of_perimeter(2,4))
print(area_of_perimeter(4,4))

print(squareRectangle(2,4))
print(squareRectangle(4,4))