import numpy as np
import pprint

def calculate(list):

    # A lista precisa ter exatamente nove itens
    if len(list) != 9:
        return 'Erro! A lista precisa ter exatos 9 elementos numéricos.'
    else:  

        # Transforma a lista python em um array numpy, que facilia o uso da biblioteca.
        # Também model a lista pra um formato de matriz 3 por 3 
        arr = np.array(list).reshape(3,3)

        # Cria o dicionário
        # tolist() faz o papel contrário do np.array(). Transforma uma array numpy em uma lista comum do python. 
        # O último resultado não precisa do tolist pois representa um único valor, não uma lista.
        calculations = {
            'mean': [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr)], 
            'standard dev': [np.std(arr, axis=0).tolist(), np.std(arr, axis=0).tolist(), np.std(arr)], 
            'varience': [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr)], 
            'min': [np.amin(arr, axis=0).tolist(), np.amin(arr, axis=1).tolist(), np.amin(arr)],
            'max': [np.amax(arr, axis=0).tolist(), np.amax(arr, axis=1).tolist(), np.amax(arr)], 
            'sum': [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr)]
        }

    return calculations

answer = calculate([2, 3, 4, 5, 6, 7, 8, 9, 2])
pprint.pprint(answer)