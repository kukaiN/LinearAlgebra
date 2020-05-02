# markov chains are processes where the next state is only dependent on the state before it
# all my ideas as class structure of markov_chain


def markov_after_n_steps(n):
    pass

def state_distribution(initial_state, n):
    """returns the distribution of the states that it has visited in n steps
    might add std_deviation, variance, frequency analysis, etc"""
    pass

def SSRW(outcomes, probabilities, n):
    """ simple_symmetric_random_walk --> SSRW
    gets the outcome and the probabilities that are assigned to it, then simulates the random walks
    then return valuable informations after n steps
    """
    pass

def symmetric_SSRW(outcome, n):
    """special case of SSRW, all probabilities of an event in the outcome space are equal
    then there are special properties that we can access
    after doing simulations, returns the valuable information after n steps"""
    pass

def gamblers_ruin(outcome, probabilities, n):
    """ simple random walk used to solve the gambler's ruin problem"""
    pass

def boundary_solutions(p, q):
    """ solutions to the boundary conditions of the gambler's ruin problem"""
    pass

def general_form_solution(p, q):
    """ general form solution to the gambler's ruin problem """
    pass

## tells the apreiodic nature
# given p and q, p is the probability of moving forward, q is moving backwards
# we can interpert p and q as the probability of winning and losing in a gambling game
# then we can use it to sove gambling problems
# these functions should also be included in the probability program files 



class Markov_chain:
    def __init__(self, matrix=[[1,0], [0, 1]], output_space = )
        self.matrix = matrix

    def get_type(self):
        # check if the matrix is irreducible or reducible
        pass

    def communication_class():
        # returns the communication class of a markov matrix
        # return None if it doesnt exist
        pass

    def communication_class_period():
        # sub function of communication_class function
        # returns the period of the communication classes in the matrix

    def invariant_measure():
        # gets the invariant measure of the matrix
        pass

    def get_reccurence_class():
        # returns the reccurent communication classes 
        pass

    def get_transient_state():
        # self-explanitory
        pass

    def show_PTM_graph():
        # visualizes the markov chain as a directed graph (graph in terms of nodes and edges)