#数あてgame
import random
a = random.randint(0, 9)
print(a)

b = input("数を入れてね>")
print(b)

if a == b:
    print("当たり")
else:
    print("はずれ")
