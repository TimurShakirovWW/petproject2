ye = int(input("на сколько лет вы оформляете вклад?"))
ap = int(input("сумма вклада:"))
pa = 1.1

def task(a,y,p):
    for i in range(y):
        a=(1+p/100)*a
    print(a)

task(ap, ye, pa)