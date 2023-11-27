testNumb = 548702838394


def digitize(numb):
    revList = []
    revStr = str(numb)[::-1]
    for i in range(len(revStr)):
        revList.append(int(revStr[i]))
    return revList

def digitize_2(n):
    return [int(x) for x in str(n)[::-1]]


print(digitize(testNumb))
