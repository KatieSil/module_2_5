def get_matrix(n, m, value) :
    matrix = []
    for i in range(n) :   # строки
        row = []
        for j in range(m) :   # столбцы
            row.append(value)
        matrix.append(row)
    return matrix

n = int(input('n: '))
m = int(input('m: '))
value = int(input('value: '))
result1 = get_matrix(n, m, value)
print(result1)
