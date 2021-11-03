
strk = "THE man was on HIS way to a camp near HENDERSON Creek. His friends were already there. He expected to reach Henderson Creek by six o’clock that evening. It would be dark by then. His friends would have a fire and hot food ready for him."
a = strk.split()
def StrkList(a):
    uu = 0; ll = 0; bb = 0
    for i in range(len(a)):
        b = 0; l = 0
        for ii in range(len(a[i])):
            if a[i][ii].isupper():
                b +=1
            else:
                l += 1
        if b > l:
            uu +=1
        elif b < l:
            ll += 1
        else:
            bb += 1
    Uppersletters = uu / (uu + ll + bb) * 100
    Lowerletters = ll / (uu + ll + bb) * 100
    Both = bb / (uu + ll + bb) * 100
    return ('Процент заглавных' ,Uppersletters, 'Процент строчных' ,Lowerletters, 'Процент одинаковых' ,Both)
print(StrkList(a))
