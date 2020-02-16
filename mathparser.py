import collections
import os
import time
import sys
import math
import random
import string 

from collections import Counter 


def normalize_expression(input_str): # makes "(1+2)(5-3)" ==> "(1+2)*(5-3)" to make the parser understand it's a multiplication
    length = len(input_str)
    if length > 1: 
        current_index, next_char = 1, input_str[1]
        while current_index < length:
            current_char, next_char = next_char, input_str[current_index]
            if (current_char == ")" and next_char == "(") or (current_char == "]" and next_char == "["):
                input_str = input_str[:current_index] + "*" + input_str[(current_index):] 
                length+=1
                current_index+=1 #if there is a ")(" match the same pattern will not appear in the next index, or else it's invalid
            current_index+=1
    return input_str

def check_parenthetical_elements(in_str):
    counter1, counter2, counter3 = 0, 0, 0
    for i in in_str:
        if not(i.isalnum()):
            if i == "(": counter1+=1
            elif i == ")": counter1-=1
            elif i == "[": counter2+=1
            elif i == "]":counter2-=1
            elif i == "{":counter3+=1
            elif i == "}":counter3-=1
    if counter1 == 0 and counter1 == counter2 == counter3:
        return True
    return False

def smarter_check_and_normalizer(in_str):
    """
    does the same task as checking valid and invalid strings, and does minor transformations into a standard expression

    return a list where the first element is a bool that represnts if the sentence is valid or not, and the second value is the new expression
    """
    counter1, counter2, counter3 = 0, 0, 0
    length, bool_val = len(input_str), False
    if length > 0: 
        bool_val = True
        curr_index, next_index = 0, 1
        curr_word, next_word = "", ""
        while current_index < length:
          pass  


    return [bool_val, input_str]


def evaluate_expression(in_str):
    """
    takes an input string and returns the value of the whole expression
    """
    answer = 0
    # key-value pairs keys are the mathematical expressions and the values are the weights that represents the order of oeprations
    # higher weights represnts the expressions to evaluate first, while keys with value 0 are not used yet, they are modifiable
    expression = {"+" : 5, "-" : 5,
                "/" : 10, "*" : 10,
                "**" : 15,
                "%" : 20, "//": 20,
                "&" : 0, "#" : 0, "!" : 0, "|" : 0, ":" : 0, ";" : 0, "?": 0
                }

    return answer



def recursive_eval(in_str):
    for i in index:
        
    recursive_eval(in_str[:index])

    evaluate = in_str

def evaluate_expression(in_str):
    in_str.split()
