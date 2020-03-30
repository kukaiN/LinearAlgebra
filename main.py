import math
import random
import pandas as pd
import numpy as np
import pickle
import itertools
import collections


def matrix_pow(matrix_a, power):
    """matrix multiplication have the associative property, A(BC) == (AB)C"""
    if power < 2: return matrix_a
    else:
        m_product = matrix_pow(matrix_a, int(power/2))
        m_product = matrix_mul(m_product, m_product)
        if power&1:
            m_product = matrix_mul(m_product, matrix_a)
        return m_product

def matrix_mul(matrix_a, matrix_b):
        """first check the dimension of the two matrix, then do matrix multiplication, dot product """
        a_row, a_column = len(matrix_a), len(matrix_a[0])
        b_row, b_column = len(matrix_b), len(matrix_b[0])
        if a_column == b_row:
            new_matrix = [[0 for _ in range(b_column)] for _ in range(a_row)]
            for r_index in range(a_row):
                for c_index in range(b_column):
                    new_matrix[r_index][c_index] = dot_product([a for a in matrix_a[r_index]], [matrix_b[idx][c_index] for idx in range(b_row)])
        return new_matrix

def dot_product(list_a, list_b):
    """ hand made dot product, self-explanitory"""
    return sum([a*b for a, b in zip(list_a, list_b)])

def matrix_mul_np(a, b):
    if len(a[0]) == len(b):
        matrix_a, matrix_b = np.array(a), np.array(b)
        return matrix_a.dot(matrix_b)


class matrix():
    def __init__(self, x=2, y=2): # initiate matrix
        self._height = y
        self._width = x
        self._matrix_RealNum = pd.DataFrame(np.zeros((x, y)))
        self._matrix_RealDen = pd.DataFrame(np.ones((x, y)))
        self._matrix_ImgNum = pd.DataFrame(np.zeros((x, y)))
        self._matrix_ImgDen = pd.DataFrame(np.ones((x, y)))
        self._square = True if x == y else False
        self._augmented = False
        self._fractions = False
        self._complexValues = False

    def matrix_size(self, width, height):
        self._height = height
        self._width = width
        self._width = True if height == width else False

    def identity_matrix(self):
        if self._height == self._width:
            self._matrix = 

    def modify_entry(self, i, j, value):
        if x < self._width and y < self._height and 0 < x and 0 < y:
            self._matrix[j][i] = value
        else:
            print("the index provided is not valid")

    def modify_row(self, row_index, row_list):
        if len(row_list) == self._width:
            self._matrix[row_index] = row_list
        else: print("list length doesnt match width of matrix")
    
    def modify_column(self, column_index, column_list):
        if len(column_list) == self._height:
            for i in self._height:

        else: print("list length doesnt match height of matrix")
   
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
        pass

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
        pass

    def fibonacci():
        pass
    def span():
        pass
    def dualSpace():
        pass
    def QTQ():
        pass
    
    def compression():
        pass
    def markovchain():
        pass
    def stocastcic_processes():
        pass
    def ask_for_values(self):
        if !(self._height > 0 and self._width > 0): 
            while self._height < 1: self._height = int(input("please provide a valid height for the matrix: "))
            while self._width < 1: self._width = int(input("please provide a valid width for the matrix: "))
        

def main():
    print("what is it that you want to do?")



if "__name__" = "__main__":
    main()