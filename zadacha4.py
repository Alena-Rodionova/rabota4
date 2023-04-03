a=input('Введите номер: ',)
r=len(a)
if r%2==0:
    t=list(a)
    i=0
    p=0
    k=0
    while i<(r/2):
        p=p+int(a[i])
        i+=1
    while i<r:
        k=k+int(a[i])
        i+=1
    if k != p:
        print('Билет не счасливый')
    else:
        print('Билет счасливый')
else:
    print ('Количество цифр нечетное')
