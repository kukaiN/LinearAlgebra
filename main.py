import math
import random
import pandas as pd
import numpy as np
import pickle
import itertools
import collections

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
    
    def parse_input(input_str):
        stack = collections.deque()
        small_stack = collections.deque()
        input_str = "(" + input_str +")"
        if check_parenthetical_elements(input_str):
            change = True
            index = 0
            starting_index = 0
            ending_index = 0
            while change:
                letter = input_str[index]
                if letter == "(" or letter == "[" or letter == "{":
                    small_stack.clear()
                    starting_index = index
                if letter == ")" or letter == "]" or letter == "}":
                    
                    ending_index = index
        #empty bool
        #append and pop 
        #check for (3-5)(7-5)

    # example input 
    "((5-3)/3)"
    def check_parenthetical_elements(in_str)
        counter = 0
        for i in range(len(in_str)):
            letter = in_str[i]
            if letter == "(" or letter == "[" or letter == "{": counter+=1
            if letter == ")" or letter == "]" or letter == "}": counter-=1
        if counter == 0:
            return True
        return False

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