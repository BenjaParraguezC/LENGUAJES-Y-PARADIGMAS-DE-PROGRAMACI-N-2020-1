from functools import reduce
from operator import add

#Codigo hecho por Benjamin Parraguez 
#Seccion 1
#Lenguaje y paradigmas de la programacion 2020/1


lista =[1,50,12,5,10,0,-3]


def Sort(lista):
    if reduce(add, [1 for _ in lista], 0) == 0: #Largo de la lista
        return lista
    else:
        tmp = lista[0]    #ordenamiento de la lista

        elem_comparativo = [x for x in lista if x == tmp]

        elem_menor = Sort([x for x in lista if x < tmp])

        elem_mayor = Sort([x for x in lista if x > tmp])

        return elem_menor + elem_comparativo + elem_mayor

print("La lista original es: ",lista)
print("")
print("La lista ordenada es: ",Sort(lista))
print("")




def merge_sort(values): 
  
    if len(values)>1: 
        m = len(values)//2
        left = values[:m] 
        right = values[m:] 
        left = merge_sort(left) 
        right = merge_sort(right) 
  
        values =[] 
  
        while len(left)>0 and len(right)>0: 
            if left[0]<right[0]: 
                values.append(left[0]) 
                left.pop(0) 
            else: 
                values.append(right[0]) 
                right.pop(0) 
  
        for i in left: 
            values.append(i) 
        for i in right: 
            values.append(i) 
                  
    return values

lista2 = merge_sort(lista) 

print("Lista original es: ",lista)
print("")
print("La lista ordenada es: ")
print(*lista2)
print("")

