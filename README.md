# Linear Algebra using python

Linear algebra algorithms and programs made with python

## Important Info:
 - Use numpy's implimentation instead of this, if performnace is a factor.
 - the code here is to showcase the inner workings of the algorithm and is a form of note taking so that I don't forget the teachings in linear algebra.  

 - main.py and test.py are test files that i use to check the validity of the code so it is separate from the linear algebra repo

 - many topics in linear algebra overlaps with topics in discrete math, so if an algorithm is not in this repo, check the discrete math repo to check if its not there.

## Table of contents
- [general](#general)
    - [Dependencies](#depen)
    - [updates and future plans](#plans)
- [description of files](#info)
- 




---
<a id = "general"></a> 

## General


---
<a id = "depen"></a> 

## dependencies/ used libraries:
- numpy (most functions have the option of using numpy and works together with matplotlib)
- pandas (used to store data)
- pickle (used to save data as a .pkl file)
- matplotlib (used for visualization)
- collections (used in few files to access stacks and queues)
- random
- math (used for trig functions)
- itertools
- fractions (used to reduce errors in things like row reduction)
- string (used to parse string inputs)


<a id = "plans"></a>

## updates and future plans

### updates:
 - as of 4/21/2020, working on finishing the fundamental ideas in Lin-algebra, applications will be touched after everything is done. 

### future plans:
 - first I will continue and finish the files that are in the repo 
 - Then I will go into applications in physics and modeling


<a id = "info"></a> 
---

## file descriptions
The following are short description of the files in this repo, comments with the same level of detail is also in their respective file.  The short description are just overviews, so further info are most likely in the comments of the file.

The description will include the type of the file, whether it is a theory/foundation or if its an application of linear algebra

*The files that are applications will be written after the foundational files are finished*

### complex_number.py
type: theory/foundation
This is a file that manipulates matricies with imaginary values.  There's a class for entries with imaginary numbers and have special methods for addition and matrix multiplication 

### computer_graphics.py
type: applications
This is a file that impliments gaussian blur and other graphics related functions.


### determinant.py
type: theory/foundation
The file contains multiple methods of finding determinants and contains other functions that are related to the determinant of the matrix


### differential_equation_with_matrix.py
type: application and theory/foundation for population growth.py
the file contains functions that takes in a matrix with differential equations (first order), and have methods of finding stable configurations. Also have simple simulations of the matrix.

### eigenvalue.py
type: theory/foundation
The file contains methods of finding eigenvalues and using the eigenvalues to gain insightful information of the matrix

### electrical_circuits.py
type: application
The file takes in an electrical circuits that with informations about resistance, amp, and current, then returns the value of a missing value or returns some information about the grid

### fourier_series.py
type: theory/foundation and applications
Im still learning fourier series so this will come later, but probably contain functions that approximate shapes and some functions related to audio. 

### fractals.py
type: theory/applications and applications
This will contain functions that visualizes a fractal using lin algebra

### game_theory.py
type: application
This will contain functions that take in a matrix that represent outcomes of actions taken by each party and find some strategy or will simulate the outcome.
2 player games will have alot of functions, but multiplayer(3+) games will not have nice ways of disecting information so it will most likely return outcomes of simulations.


### gaussian_elimination.py
type: theory/application
Contains functions that returns the REF or RREF of any matrix.  Also functions that returns information about the cardinality of the number of solution (zero, one, or infinite solutions to the system of equations)


### least_square_methods.py
type: applications
Contains functions related to the least square method, it may be merged with other files with similar functionalities

### linear_transformations.py
type theory/foundation
Convert basis, visualize the transformation, find one transformation matrix given multiple transformations
return information about the transformation, whether it's surjective, injective, or both(bijection)

### LU_decomposition.py
type application
given a matrix A, convert it into lower and upper matrices (L and U) then takes in a vector b to find the x vector.  helps speed up the calculation of Ax = b if matrix A is constant and we're looking for x vector for different b vectors

### markov_chain.py
type theory/foundation and applications
uses a matrix filled with probability and simulate the process.  will contain functions related to invarant measure, the state of the matrix, and visualization of the matrix and the simulation. 

### mathparser.py
type: applications(?)
file that contains functions that parses strings to get mathematical statements and evaluates it.
The reason for making this file is because many online linear algebra calculators only takes in int or floats and doesnt allow expression.



### optimization_with_quadratic_form.py
type: application
simple optimization using quadratic form

### population_model.py
type: application
simulate animal populations (rabbits and wolves) using matrices

### QR_decomposition.py
type: applications
probably will be merged with LU_decomposition.py as decomposition.py
same idea as LU decomp, QR will decompose the matrix to simplify the number of opperation if the same matrix is used multiple times.

### random_walks.py
type: theory/foundation
this file contains many functions from the brownian_motion file in the physics repository.
contains brownian motion, random walk on Z^n (integr structure), convergence or divergence of the walk, and simulations of the walk

### singular_value_decomp.py
type: application
thinking whether or not this should be merged witht the decomposition file
contains the decomposition method and the applications


### vector_spaces.py
type: theory/foundation
contain functions related to null, row, column space. and other related info