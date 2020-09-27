def Prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return 0
        else:
            return 1
    else:
        return 0


def Ferma(n):
    return pow(2, pow(2, n)) + 1


x = 0
while Prime(Ferma(x)):
    x += 1
print(Ferma(x), 'is not a prime.')