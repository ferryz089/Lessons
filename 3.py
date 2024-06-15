name = ('кенгуру')
print((name[4:]) + (name[:4]))

a = str(input('Напечатайте слово "кенгуру"'))
k = len(a) // 2 + len(a) % 2
print(a[k:] + a[:k])