def percent(strk):
    uppers = lowers = 0
    for i in strk:
        if i.isalpha():
            if i.islower():
                lowers += 1
            else:
                uppers += 1
    y = uppers + lowers
    x = (uppers*100)//y
    return {'Заглавных':x,'Строчных':100-x};
print(percent(input('Введите строку:')))