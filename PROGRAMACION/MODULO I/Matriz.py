#Matriz en pyhton
#Sumar elementos de la matriz
matriz = [[1,2,3],[2,5,1], [6,5,1]]

print (len(matriz))
suma = 0
for fila in matriz:
    for valor in fila:
        print("elemento:", valor)
        suma += valor
        #print(f"la suma por elementos es: {suma}")
        print (f"la suma por fila es: {suma}")

print(f"la suma de los elementos de la matriz es: {suma}")

#suma de diagonal de la matriz
matriz = [[1,2,3], [2,5,1], [6,5,1]]
suma = 0
i = 0
while(i<len(matriz)):
    fila = matriz[i]
    j = 0
    while(j<=len(fila)):
        if i==j:
            suma+= fila[j]
        j += 1
    i += 1
