import numpy as np

def four_indices(array):
    indices = []
    
    shape = array.shape        
    nbRw, nbCl = shape[0], shape[1]

    for i in range(0, nbRw):
        for j in range(0, nbCl):
            #horizontal
            if i < nbRw and j + 3 < nbCl:
                indices.append([(i, j + k) for k in range(0, 4)])

    for i in range(0, nbRw):
        for j in range(0, nbCl):
            #horizontal
            if i + 3 < nbRw and j < nbCl:
                indices.append([(i + k, j) for k in range(0, 4)])

    for i in range(0, nbRw):
        for j in range(0, nbCl):
            #diagonal from upper left to lower right
            if i + 3 < nbRw and j + 3 < nbCl:
                indices.append([(i + k, j + k) for k in range(0, 4)])

    for i in range(0, nbRw):
        for j in range(0, nbCl):
            #diagonal from lower left to upper right
            if i - 3 > - 1 and j + 3 < nbCl:
                indices.append([(i - k, j + k) for k in range(0, 4)])

    return indices     
