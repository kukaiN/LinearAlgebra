import numpy as np
import fractions


def gaussian_elimination(matrix_A, augmented=True, RREF=True):
    # RREF: Reduced Row Echelon Form
    # if RREF is False then it does row reduction until REF
    if augmented:
        for i in range len(matrix_A): # go through each row, and do reow reduction
            # row reduction


            if RREF: # keep on going and reduce it until 
                pass



def gaussian_elimination_return_transformation(matrix_A, augmented=True, RREF=True):
    transformation = []
    # modify matrix

    if augmented:
        for i in range(len(matrix_A)):
            # row reduction 
            # and store the simple transfrmation 

    # return transformation