from AlgoHybridSort import AlgoHybridSort
from MergeSort import MergeSort
from QuickSort import QuickSort
from SelectionSort import SelectionSort

lista_original = [11,7,12,14,19,1,6,18,8,20]
resulta_esperado = [1,6,7,8,11,12,14,18,19,20]

hibri = AlgoHybridSort()  
lista = lista_original.copy()
hibri.sort(lista)
print('AlgoHybridSort Ordenado?', lista == resulta_esperado)

merge = MergeSort()  
lista = lista_original.copy()
merge.sort(lista)
print('MergeSort Ordenado?', lista == resulta_esperado)

quick = QuickSort()  
lista = lista_original.copy() 
quick.sort(lista)
print('QuickSort Ordenado?', lista == resulta_esperado)

selection = SelectionSort()  
lista = lista_original.copy() 
selection.sort(lista)
print('SelectionSort Ordenado?', lista == resulta_esperado)

