import random
import timeit

from AlgoHybridSort import AlgoHybridSort
from GenerateInfo import GenerateInfo
from MergeSort import MergeSort
from QuickSort import QuickSort
from SelectionSort import SelectionSort

def testQuickSort(numeros):
    quick = QuickSort()
    quick.sort(numeros)
    
def testSelectionSort(numeros):
    selection = SelectionSort()
    selection.sort(numeros)

def testHybridSort(numeros, limitSubList):
    hybrid = AlgoHybridSort(limitSubList)
    hybrid.sort(numeros)
    
def testMergeSort(numeros):
    merge = MergeSort()
    merge.sort(numeros)
    
def testPerformance(algorithms, dataset):
    results = {}
    rep = 3

    for algorithm_name, algorithm_func in algorithms.items():
        algorithm_results = []
        for size, data in dataset.items():
            time_taken = timeit.timeit(lambda: algorithm_func(data.copy()), number=rep)
            avg_time = time_taken / rep
            algorithm_results.append(avg_time)
        results[algorithm_name] = algorithm_results

    return results    
    

if __name__ == '__main__':
    
    algorithms = {
        'SelectionSort': testSelectionSort,
        'QuickSort': testQuickSort,
        'MergeSort': testMergeSort,
        'AlgoHybridSort with limit 16': lambda arr: testHybridSort(arr, 16), 
        'AlgoHybridSort with limit 64': lambda arr: testHybridSort(arr, 64), 
        'AlgoHybridSort with limit 256': lambda arr: testHybridSort(arr, 256),  
    }

    dataset = { 
        1000: [random.randint(0, 1000000) for _ in range(1000)], 
        10000: [random.randint(0, 1000000) for _ in range(10000)], 
        50000: [random.randint(0, 1000000) for _ in range(50000)], 
        500000: [random.randint(0, 1000000) for _ in range(500000)],
    }

    results = testPerformance(algorithms, dataset)

    generateInfo = GenerateInfo()

    generateInfo.generateOutputResults(results, dataset)

    generateInfo.generateLineGraph(dataset, results)

    generateInfo.generateBarGraph(dataset, results, algorithms)
