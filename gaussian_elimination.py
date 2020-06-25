import numpy as np
import fractions


def gaussian_elimination(matrix_A, augmented=False, square_matrix=True, RREF=True):
    # gaussian jordan is O(n^3)
    # RREF: Reduced Row Echelon Form
    # if RREF is False then it does row reduction until REF
    # make sure that the matrix is not sparce, meaning dont use this for matrices that have specialized algorithms    
    row_num = len(matrix_A)
    col_len = len(matrix_A[0]) 

    # forward elimination
    for pivot_ij in range(row_num):
        current_pivot = matrix_A[pivot_ij][pivot_ij]
        pivot_num, pivot_denom = current_pivot.numerator, current_pivot.denominator
        flipped_pivot = fractions.Fraction(numerator=pivot_denom, denominator=pivot_num)
        for j in range(pivot_ij, col_len):
            matrix_A[pivot_ij][j]*=flipped_pivot
    if square_matrix == False or RREF == False: # return REF (not unique)
        return matrix_A
    
    # backward elimination

    for pivot_ij in reversed(range(0, row_num)):
        for row_index in reversed(range(0, pivot_ij)):
            print(pivot_ij, row_index)
            curr_row = matrix_A[pivot_ij]
            non_zero = matrix_A[row_index][pivot_ij]
            if non_zero != 0:
                numer, denom = non_zero.numerator, non_zero.denominator
                flipped_row = matrix_A[pivot_ij]
                for j in range(pivot_ij+1, col_len):
                    matrix_A[pivot_ij][j]+=-flipped_row[j]



    return matrix_A
    
    
        
def print_matrix(matrix):
    for row in matrix:
        print([frac if frac.denominator != 1 else frac.numerator for frac in row])
    print("*" * 20)
        


def gaussian_elimination_return_transformation(matrix_A, augmented=True, RREF=True):
    transformation = []
    # modify matrix
    matrix_A = [[fractions.fractions(value) for value in row] for row in matrix_A]
    if augmented:
        for i in range(len(matrix_A)):
            pass
            # row reduction 
            # and store the simple transfrmation 

    # return transformation

def convert_to_fractions(matrix):
    # returns the matrix but convert all entries into fractional object to reduce the amount of error
    # runtime O(size of matrix) = O(n^2)
    return [[fractions.Fraction(entry) for entry in row] for row in matrix]


def main():
    matrix = [[1, 2, 3, 4],
            [0, 6, 7, 8],
            [0, 0, 11, 12],
            [0, 0, 0, 16]]

    matrix = convert_to_fractions(matrix)
    gauss = gaussian_elimination(matrix, augmented=False, square_matrix=True, RREF=True)
    print_matrix(gauss)



if __name__ == "__main__":
    main()