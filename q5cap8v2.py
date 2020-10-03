
list = []
aux = []
listaR = []

n= ''

while n !=0:
    n = int(input('Give me a number... '))
    try:
        int(n)
    except:
        print("xd")
        exit()
    if n != 0:
        list.append(n)
        aux.append(n) 
        listaR.append(n)


# print(sorted(list))
list.sort()
print(list)
print(aux)
i=0
q = -1

while list[0]!=aux[0] and 3<len(aux):
    if list[0]<aux[q]:
        aux.pop()
    i += 1

listaR.insert(0, list[0])
listaR.insert(i, aux[0])

print(listaR)

    # if q+3 == len(aux):
    #     aux.append[10000]