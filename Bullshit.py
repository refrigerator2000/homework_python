class Bullshit:
    def __init__(newm, mat):      #проверка длин строк матрицы 
        newm.mat = mat
        min = len(mat[0])
        t = True
        for i in range(len(mat)):
            if len(mat[i]) != min:
                t = False
        if not t:
            print("._.")

    def transpone(newm):      #транспонирую матрицу
        newmat = []
        i = 0
        for i in range(len(newm.mat[i])):
            b = []
            for j in range(len(newm.mat)):
                b.append(newm.mat[j][i])
            newmat.append(b)
        return newmat

matrix = Bullshit([[1, 7, 2], [0, 5, 5], [0, 0, 9], [0, 0, 0]])
try:
    print(matrix.transpone())
except:
    print("-")