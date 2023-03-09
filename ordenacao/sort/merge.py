def intercala(lista, inicio, meio, fim):
    i = inicio
    j = meio

    aux = []
    while i<meio and j<fim:
        if lista[i]<lista[j]:
            aux.append(lista[i])
            i+=1
        else:
            aux.append(lista[j])
            j+=1
    # fim while -> i < meio ou j < fim
    while i<meio:
        aux.append(lista[i])
        i+=1
    while j<fim:
        aux.append(lista[j])
        j+=1
    print(lista)
    print(aux)
    #return aux

def merge_sort(inicio, fim, lista):
    if inicio < fim-1:
        meio = (inicio+fim)//2
        print(f'{inicio}\t|{fim}\t|{fim-1}\t|{meio}',end='\t')
        print(lista[inicio:fim])
        merge_sort(inicio, meio, lista)
        merge_sort(meio, fim, lista)
        intercala(lista,inicio,meio,fim)
    

L = [0,1,6,20,4,5,7,10, 3, 2]
print(L)
#print('inicio\t|fim\t|fim-1\t|meio')
#merge_sort(0,len(L),L)
#print(L)
L_O = intercala(L, 0, 5, len(L))
#print(L_O)
# L_O = [0,1,4,5,6,7,10,20]