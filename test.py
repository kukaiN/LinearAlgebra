inp = "(1 + 4) / 5 * 10"
#print(int(inp))

add = "+"
minus = "-"
divide = "/"
times = "*"
mod = "%"
remainder = "//"
power1 = "**"
power2 = "^"

def parse_input(input_str):
    stack = collections.deque()
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

def normalize_expression(in_str):
    
    new_str = in_str
    print("rtecieved", new_str)
    length = len(new_str)
    current_index, next_char = 1, new_str[1]
    if length > 1:
        print(current_index, length)
        while current_index < length:
            print('loop')
            current_char, next_char = next_char, new_str[current_index]
            if (current_char == ")" or current_char == "]") and (current_char == "(" or current_char == "["):
                print(current_char, next_char)
                new_str = new_str[:current_index] + "*" + new_str[(current_index+1):] 
                length+=1
                current_index-=4
            current_index+=1
    return new_str

def check_parenthetical_elements(in_str):
    counter = 0
    for i in range(len(in_str)):
        letter = in_str[i]
        if letter == "(" or letter == "[" or letter == "{": counter+=1
        if letter == ")" or letter == "]" or letter == "}": counter-=1
    if counter == 0:
        return True
    return False


print(normalize_expression("(11*)(1)(1)()()()"))