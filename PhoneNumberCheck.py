x = input("Имя: ")
y = input("Номер: ")
z = {}
while y != "q" and x != "q":
    if len(y) == 16 and y[0] + y[2] + y[6] + y[10] + y[13] == "+----" and (
            y[1] + y[3] + y[4] + y[5] + y[7] + y[8] + y[9] + y[11] + y[12] + y[14] + y[15]).isdigit():
        z[x] = y
        print("Номер принят")
    else:
        print("Номер не подходит")
    x = input("Имя: ")
    y = input("Номер: ")
print(z)