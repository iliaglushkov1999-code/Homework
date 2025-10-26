x = int(input("Введите трёхзначное число: "))
a = x // 100
b = (x // 10) % 10
c = x % 10

result = (a + b + c) % 2 == 0
print(result)
