# Linear Regression
Implements a Python executable file called linear_regression.py that uses linear regression to fit a polynomial function to the data.

## Arguments
1. The first argument, \<training_file>, is the path name of the training file, where the training data is stored. The path name can specify any file stored on the local computer.

2. The second argument, \<degree> is an integer between <sub>1</sub> and <sub>1</sub>0. We will not test your code with any other values. The degree specifies what function φ you should use.
> Suppose that you have an input vector x = (x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>D</sub>)<sup>T</sup>
   > * If the degree is 1, then φ(x) = (1, x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>D</sub>)<sup>T</sup>.
   > * If the degree is 2, then φ(x) = (1, x<sub>1</sub>, (x<sub>1</sub>)<sup>2</sup>, x<sub>2</sub>, (x<sub>2</sub>)<sup>2</sup>..., x<sub>D</sub>, (x<sub>D</sub>)<sup>2</sup>)<sup>T</sup>.
   > * If the degree is 3, then φ(x) = (1, x<sub>1</sub>, (x<sub>1</sub>)<sup>2</sup>, (x<sub>1</sub>)<sup>3</sup>, x<sub>2</sub>, (x<sub>2</sub>)<sup>2</sup>, (x<sub>2</sub>)<sup>3</sup>, ..., x<sub>D</sub>, (x<sub>D</sub>)<sup>2</sup>, (x<sub>D</sub>)<sup>3</sup>)<sup>T</sup>.

3. The third argument, \<λ>, is a non-negative real number (it can be zero or greater than zero). This is the value of λ that you should use for regularization. If λ = 0, then no regularization is used.

4. The fourth argument, \<test_file>, is the path name of the test file, where the test data is stored. The path name can specify any file stored on the local computer.

## Test Cases
* Degree = 1 and λ = 0
* Degree = 1 and λ = 1
* Degree = 2 and λ = 0
* Degree = 2 and λ = 1
