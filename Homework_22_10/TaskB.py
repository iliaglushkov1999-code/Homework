a = int(input("Введите сторону a: "))
b = int(input("Введите сторону b: "))
c = int(input("Введите сторону c: "))

exists = (a + b > c) and (a + c > b) and (b + c > a)

result = exists and (a != b) and (a != c) and (b != c)
print(result)
