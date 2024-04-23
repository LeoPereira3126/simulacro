def llenar_matiz(n):
    matriz = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i < n // 2:
                if j < n // 2:
                    matriz[i][j] = 1
                else:
                    matriz[i][j] = 2
            else:
                if j < n // 2:
                    matriz[i][j] = 3
                else:
                    matriz[i][j] = 4
        return matriz

def matriz(m):
    for fila in m:
        for elemento in fila:
            print(elemento, end= "")
            print()
        
num = int(input("Por favor ingrese un número par para el tamaño de la matriz "))
if num % 2 != 0:
    print("Por favor ingrese un número par")
else:
    llenar_matiz(num)
    matriz(num)



        