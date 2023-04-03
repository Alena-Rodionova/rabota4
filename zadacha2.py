def sto():
    while type:
        a = input('Введите число: ')
        try:
            b = int(a)
        except ValueError:
            print('"' + a + '"' + ' - не является числом')
        else:
            try:
                k=100/int(a)
            except ZeroDivisionError:
                print('На ноль делить не стоит')
            else:
                k = 100 / int(a)
                print('100/', a, "=", k)
                break


print(sto())

