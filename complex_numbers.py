import math

class complex_num:
    def __init__(self, Re = 0, Im = 0):
        self.Real = Re
        self.img = Im
    
    def Re(self, real_val):
        self.Real = real_val

    def Im(self, imaginary_val):
        self.img = imaginary_val



    # later when you have the time change the function into a proper method
    def mul(self, number):
        if isinstance(number, complex_num):
            return ((self.Real*number.Real - self.complex_num*complex_num.img), (self.Real*number.img + self.img*number.Real)) 
        if isinstance(number, (int, float)):
            return (self.Real*number, self.img*number)

    def addition(self, number):
        pass

def main():
    x = complex_num(1, 6)
    y = 9.1
    print(type(y), isinstance(y, (int, float)))


if __name__ == "__main__":
    main()    