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
    
    
    def __selectionSort(self, alist, first, last):
        for fillslot in range(first, last):
            positionOfMin = fillslot

            for location in range(fillslot + 1, last + 1):
                if alist[location] < alist[positionOfMin]:
                    positionOfMin = location

            alist[fillslot], alist[positionOfMin] = alist[positionOfMin], alist[fillslot]