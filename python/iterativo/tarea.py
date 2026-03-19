
def suma_pares(num1, num2):
    next = num1 if num1 % 2 == 0 else num1 + 1
    last = num2 if num2 % 2 == 0 else num2 - 1

    return sum(list(range(next, last + 1, 2)))

print(suma_pares(1, 10))
print(suma_pares(2, 10))

print(suma_pares(5, 15))