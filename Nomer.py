t = input("Введите имя: ")
k = input("Введите номер: ")
g = {}
while k != "q" and t != "q":
    if len(k) == 16 and k[0] + k[2] + k[6] + k[10] + k[13] == "+----" and (
            k[1] + k[3] + k[4] + k[5] + k[7] + k[8] + k[9] + k[11] + k[12] + k[14] + k[15]).isdigit():
        g[t] = k
        print("Номер добавлен")
    else:
        print("Неправильный номер")
    t = input("Введите имя: ")
    k = input("Введите номер: ")
print(g)