import datetime
while True:
    date_ = input('Введите дату в формате день месяц год: ')
    if date_ == ('help'):
        print('тут должен быть комментарий')
        quit()

    day , month, year = date_.split(' ')

    d = int(day)
    m = int(month)
    y = int(year)

    def checkday(d):
        if not(0 < d < 32):
            print('Ты дуралей...')
            quit()
    def checkmonth(m):
        if not(0 < m < 12):
            print('Ок, ну ты и задал жару')
            quit()
    def checkyear(y):
        if not(0 < y < 2022):
            print('А вот так нельзя')
            quit()
    def February(d, m):
        if m == 2 and d == 29:
            n = input('Это високосный год?')
            if n != 'y':
                print('С днем бетона!')
                quit()

    def April(d):
        if m==1 and 0 < d < 31:
            print('ну да, конечно')
            quit()
    def June(d):
        if m==1 and 0 < d < 31:
            print('ну да, конечно')
            quit()
    def September(d):
        if m==1 and 0 < d < 31:
            print('ну да, конечно')
            quit()

    def November(d):
        if m==1 and 0 < d < 31:
            print('ну да, конечно')
            quit()

    checkday(d)
    checkmonth(m)
    checkyear(y)
    February(d, m)

    print('Ну это собственно правильно', day, month, year)