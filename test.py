import collections
import os
import time
import sys

import random
import string 

from collections import Counter 

inp = "(1 + 4) / 5 * 10"
#print(int(inp))


def parse_input(input_str):
    #stack = collections.deque()
    small_stack = collections.deque()
    input_str = "(" + normalize_expression(input_str) +")"
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
                for i in range(starting_index, ending_index+1):
                    pass     





"""
t1 = time.time()
N = 1000000
sentence = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
t2=time.time()
print("took this much to make word: ", t2-t1)
print(sentence[:100])

x = Counter(sentence)['E']
t3 = time.time()
print(x) #0.05
print("first method: ", t3-t2)

count = sum(map(lambda x : 1 if 'E' in x else 0, sentence)) 
t4=time.time()
print(count)#0.12
print("second method: ", t4-t3)
"""