import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class GenerateInfo:
    def __init__(self):
        pass
        
    def generateOutputResults(self, results, dataset):
        print("Resultados do Teste de Desempenho:")
        print("Tamanho do Array | Tempo Médio (s) para cada algoritmo")
        print("-" * 50)
        index = 0
        for size in dataset.keys():
            print(f"Tamanho {size}:")
            for algorithm_name, times in results.items():
                avg_time = times[index]
                print(f"    {algorithm_name}: {avg_time:.6f} segundos")
            print("-" * 50)
            index += 1
        
        index = 0
        with open('algorithms_performance.txt', 'w') as f:
            f.write("Resultados do Teste de Desempenho:\n")
            f.write("===============================================\n")
            for size in dataset.keys():
                f.write(f"Tamanho do Array: {size}\n")
                for algorithm_name, times in results.items():
                    avg_time = times[index]
                    f.write(f"    {algorithm_name}: {avg_time:.6f} segundos\n")
                f.write("===============================================\n")
                index += 1
        
        
    def generateLineGraph(self, dataset, results):
        plt.figure(figsize=(10, 6)) 

        for algorithm_name, times in results.items():
            plt.plot(dataset.keys(), times, marker='o', label=algorithm_name)

        plt.xlabel('Tamanho do Array')
        plt.ylabel('Tempo Médio (s)')
        plt.title('Desempenho dos Algoritmos')
        plt.legend()  

        plt.savefig('performance_plot.png')
        
        
    def generateBarGraph(self, dataset, results, algorithms):        
        x = np.arange(len(dataset.keys()))
        width = 0.1 

        fig, ax = plt.subplots(figsize=(20, 20))

        for i, (algorithm_name, times) in enumerate(results.items()):
            ax.bar(x + i * (width + 0.05), times, width, label=algorithm_name)

        ax.set_xlabel('Tamanho do Array')
        ax.set_ylabel('Tempo Médio (s)')
        ax.set_title('Desempenho dos Algoritmos')
        ax.set_xticks(x + width * (len(algorithms) - 1) / 2)
        ax.set_xticklabels(dataset.keys())
        ax.legend()

        def autolabel(rects):
            for rect in rects:
                height = rect.get_height()
                ax.annotate(f'{height:.3f}',
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3), 
                            textcoords="offset points",
                            ha='center', va='bottom')

        for container in ax.containers:
            autolabel(container)

        
        plt.savefig('performance_bar.png')
        self.generateBarGraphForSize(dataset, results, algorithms)
        
        
    def generateBarGraphForSize(self, dataset, results, algorithms):
        index = 0
        for size, times in dataset.items():
            x = np.arange(len(algorithms))  
            width = 0.35 

            fig, ax = plt.subplots(figsize=(10, 6))

            for i, algorithm_name in enumerate(algorithms):
                ax.bar(x[i], results.get(algorithm_name)[index], width, label=algorithm_name)

            ax.set_xlabel('Algoritmo')
            ax.set_ylabel('Tempo Médio (s)')
            ax.set_title(f'Desempenho dos Algoritmos para Tamanho do Array: {size}')
            ax.legend()

            def autolabel(rects):
                for rect in rects:
                    height = rect.get_height()
                    ax.annotate(f'{height:.3f}',
                                xy=(rect.get_x() + rect.get_width() / 2, height),
                                xytext=(0, 3),
                                textcoords="offset points",
                                ha='center', va='bottom')


            for container in ax.containers:
                autolabel(container)

            plt.savefig(f'performance_bar_{size}.png')
            plt.close(fig)
            index += 1


   