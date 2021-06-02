import math

def getNumber01(num):
    while type:
        getNumber = input('Введите число ' + num + ': ')
        try:
            getTempNumber = float(getNumber)
        except ValueError:
            print('"' + getNumber + '"' + ' - не является числом')
        else:
            break
    return float(getNumber)

a = getNumber01("a")
b = getNumber01("b")
c = getNumber01("c")

discr = (b ** 2) - (4*a*c)
print("Дискриминант D: ", discr)
if a == 0:
    x = c / b
    print("x =  %.2f" % x)
elif discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2*a)
    print("x =  %.2f" % x)
else:
    print("Нет действительных корней")
