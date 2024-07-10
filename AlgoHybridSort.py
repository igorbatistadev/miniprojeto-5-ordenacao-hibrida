class AlgoHybridSort:
    def __init__(self, limitSubList=164):
        self.limitSubList = limitSubList
        
    def sort(self, list):
        self.__quickSortHelper(list,0,len(list)-1)

    def __quickSortHelper(self, alist, first, last):
        if last - first + 1 <= self.limitSubList:
            self.__selectionSort(alist, first, last)
        elif first < last:
            splitpoint = self.__partition(alist, first, last)
            self.__quickSortHelper(alist, first, splitpoint - 1)
            self.__quickSortHelper(alist, splitpoint + 1, last)


    def __partition(self, alist,first,last):
        
        middle = (first + last) // 2
        pivot_candidates = [(alist[first], first), (alist[middle], middle), (alist[last], last)]
        
        pivot_candidates.sort()
        pivotvalue, pivotindex = pivot_candidates[1]

        alist[first], alist[pivotindex] = alist[pivotindex], alist[first]

        leftmark = first+1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark -1

            if rightmark < leftmark:
                done = True
            else:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp

        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp

        return rightmark
    
    
    def __selectionSort(self, uma_lista, first, last):
        for posicao_verificada in range(last, first, -1):
            posicao_maior = 0
            for posicao in range(1,posicao_verificada+1):
                if uma_lista[posicao]>uma_lista[posicao_maior]:
                    posicao_maior = posicao
                
            temp = uma_lista[posicao_verificada]
            uma_lista[posicao_verificada] = uma_lista[posicao_maior]
            uma_lista[posicao_maior] = temp