import random
def orden (n):
    return n % 10

def divisores(num):
    lista_div = []
    div = 1
    while div <= num:
        if num % div == 0:
            lista_div.append(div)
        div += 1
    return lista_div
lista = []
while True:
    num = random.randint(0,999)
    if num == 0:
        break
    print(num, end=" ")
    lista.append(num)
ordenanza = sorted(lista,key=orden)
mayor = max(lista)
divisores_maximo = divisores(mayor)
suma = sum(divisores_maximo)
print()
print()
print("la cantidad de veces que el 0 está en la lista es de", lista.count(0))
print()
print(ordenanza)
print()
print("El número mayor es",mayor,)
print(divisores_maximo)
print("La suma de sus divisores es", suma)



