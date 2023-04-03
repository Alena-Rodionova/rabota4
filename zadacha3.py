import sys
a=input("введите дату: ", )
r=a. split('.')
p=len(r)
if p<3 or int(r[0])<1 or int(r[0])>31 or int(r[1])<1 or int(r[1])>12 or int(r[2])<1:
    print('Такой даты не бывает')
    sys.exit
else:
    t=int(r[0])
    v=int(r[1])
    o=int(r[2])%100
    if t*v==o:
        print('Дата счасливая')
    else:
        print('Дата не счасливая')