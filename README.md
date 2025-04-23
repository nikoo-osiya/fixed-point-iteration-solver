# Fixed-Point Iteration Method Solver

This is a Python implementation of the Fixed-Point Iteration method for solving nonlinear equations of the form **f(x) = 0**. Developed for a Numerical Analysis project at **Noshirvani Institute of Technology (NIT)**. The method transforms the equation into the form **x = g(x)** and then iteratively approximates the root.

## **How It Works**

You input:
	•	A function f(x) in Python syntax (e.g., x**2 - 4)
	•	A rearranged version of the function as g(x) (e.g., sqrt(x + 4) or (x**2 + 4)/2)
	•	A range within which the root is expected
	•	A desired tolerance (optional)

The program uses the midpoint of the given range as the initial guess and iteratively applies g(x) to approach the root. The process stops once f(x) is within the given tolerance.

## **Key Features**
	•	Uses eval() safely with support for common math functions (e.g., sin, cos, pow, etc.)
	•	Accepts user input for full customization
	•	Displays each iteration’s progress and convergence status

## **Example**
```bash
Enter the function f(x) in Python syntax (e.g., 'x**2 - 4'): x**2 - 4
You need to rearrange f(x) = 0 into the form x = g(x).
Enter the function g(x) (e.g., '4/x' or '(x**2 + 4)/2'): (x**2 + 4)/2
Enter the minimum of the root range: 0
Enter the maximum of the root range: 3
Initial guess (x0): 1.5
Enter the tolerance (default 1e-3): 0.001
```

## **Example output**
```bash
Iteration 1: x = 2.75, f(x_next) = 3.5625
Iteration 2: x = 3.78125, f(x_next) = 10.295654296875
...
Root found: x ≈ 2.00003, after 10 iterations.
```

## **Requirements**
	•	Python 3.x
	•	No external libraries needed (uses built-in math module)

## **How to Run**
	1.	Save the file as fixed_point.py
	2.	Open a terminal and navigate to the file’s directory
	3.	Run the script using:
 python fixed_point.py
 
## **Notes**
	•	The method may not converge for poorly chosen g(x) or initial values.
	•	Always ensure g(x) is a valid rearrangement of f(x) = 0.

##**Topics Covered**
	•	Numerical Methods
	•	Root Finding Algorithms
	•	Python Scripting
	•	Math Function Evaluation

**Author**
Seyedeh Nikoo Osiya
Third-Year Electrical Engineering Student
Noshirvani Institute of Technology (NIT)

---
**License**: MIT
