import math

print("Hello World!")
print("0度 ~ 90度每隔1分的三角函数表")
def Test():
    s0 = 0.000290888
    c0 = math.sqrt(1 - s0 ** 2)
    print("sin 1':")
    print(s0)
    s = s0
    c = c0
    n = 2
    while n <= 5400:
        s = s*c0 + c*s0
        c = math.sqrt(1 - s ** 2)
        print("sin" + str(n) + "'")
        print(s)
        n = n + 1

Test()
