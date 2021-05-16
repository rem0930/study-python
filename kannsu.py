def tasizan(a,b):
    total = 0
    for i in range(a, b + 1 ):
        total = total + i
    return total
c = tasizan(1, 5)
print(c)

def test(a,b,c,d=20,e=25):
    set_sum = a+b+c+d+e
    return set_sum

y = test(5,10,15,d=30 ,e=40)
print(y)

set_sum = 300

def test(a ,b ,c , d=20, e=25):
    global set_sum
    print(set_sum)
    set_sum = a+b+c+d+e
    return set_sum

y = test(5,10,15,d=30,e=40)
print(y)
print(set_sum)


