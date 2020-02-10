import math
import random

class matrix():
    def __init__(self): # initiate matrix
        self._height = 0
        self._width = 0
        self._square = False
        self._augmented = False
        self._fractions = False
        self._matrix = [[]]
        self._complexValues = False

    def matrix_size(self, width, height):
        self._height = height
        self._width = width
        self._width = True if height == width else False

    def modify_entry(self, i, j, value):
        if x < self._width and y < self._height and 0 < x and 0 < y:
            self._matrix[j][i] = value
        else:
            print("the index provided is not valid")

    def modify_row(self, row_index, row_list):

        for i in range(self._height):
            self._matrix[row_index] = 
    
    def modify_column(self, column_index, list):
        pass
    
    def LUdecompositions():
        pass

    def GaussJordanElimination():
        pass

    def multiply_matrix():
        pass

    def dot_product():
        pass

    def matrix_addition():
        pass
    
    def cross_product():
        pass

    def crammersRule():
        pass

    def find_inverse():
        pass

    def Transpose():
        pass

    def find_determinant():

    def find_eigenvalues():
        pass

    def find_eigenvectors():
        pass

    def nullspace():    
        pass
    
    def rowspace():
        pass
    
    def columnspace():
        pass

    def diagonalize():
    
    def fibonacci():

    def span():

    def dualSpace():

def main():
    print("what is it that you want to do?")



if "__name__" = "__main__":
    main()