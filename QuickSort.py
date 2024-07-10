class QuickSort:
    
    def __init__(self):
        pass
    
    def sort(self, alist):
        self.__quickSortHelper(alist,0,len(alist)-1)

    def __quickSortHelper(self, alist,first,last):
        if first<last:

            splitpoint = self.__partition(alist,first,last)

            self.__quickSortHelper(alist,first,splitpoint-1)
            self.__quickSortHelper(alist,splitpoint+1,last)


    def __partition(self, alist,first,last):
        pivotvalue = alist[first]

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