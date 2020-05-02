import matplotlib.pyplot as plt
import numpy as np
import random

class uniform_dis:
    def __init__(self, a=0, b=1):
        if b < a: a, b = b, a
        self.a = a
        self.b = b
    
    def __setAB__(self, a, b):
        self.__setA__(a)
        self.__setB__(b)
        self.__updateVal__()

    def __setA__(self, a):
        self.a = a
    def __setB__(self, b):
        self.b = b

    def __updateVal__(self):
        self.pdf = self.__pdf__
        self.cdf = self.__cdf__
        self.mean = self.b-self.a 
        self.median = (self.b-self.a) / 2
        self.var = (self.b-self.a)**2 / 12
        self.skewness = 0
        self.kurtosis = 9/5
        
    def __sample__(self, number_of_samples):
        for _ in ra

    def __pdf__(self): 
        return [(0, "for x < {}".format(self.a)), 
                (1/(self.b-self.a) , "for {0} <= x <= {1}".format(self.a, self.b)),
                (0, "for x > {}".format(self.b))]

    def __cdf__(self):
        return [(0,  "for x < {}".format(self.a)),
                ("x-{0} / x-{1}", "for {0} <= x <= {1}".format(self.a, self.b)),
                (0, "for x > {}".format(self.b))]

class normal_dis:
    def __init__(self, mean =0, std_dev=1):
        self.mean=mean
        self.std_dev=1
    def __updateVal__(self):
        self.var = self.std_dev**2
        
    def Zscore(self, x):
        return (x-self.mean) / self.std_dev

    def Zscore_to_x(self, z_score)
        return self.mean + z_score*self.std_dev

class lognormal_dis:
    pass
class poisson:
    pass
class gamma_dis:
    pass
class exp_dis:
    pass
class geometric_dis:
    pass
class hypergeometric_dis:
    pass

class bernoulli_dis:
    def __init__(self):
        self.success_rate = 1
        self.success_outcome = 1

class binomial_dis:
    def __init__(self, n = 10, p = 1/2):
        self.trials = n
        self.success_rate = p

    def outcome_probability(success_num = 0):
        return 
x = uniform_dis()
x.__setAB__(10, 80)