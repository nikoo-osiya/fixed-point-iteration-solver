import math

def fixed_point_iteration(g_func, f_func, x0, tol, max_iterations=1000):
    
   
    def f(x):
        
        return eval(f_func, {
            "x": x,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "pow": math.pow,
            "abs": abs,
            "radians": math.radians
        })
   
   
   
   
   
   
   
    def g(x):
      
        return eval(g_func, {
            "x": x,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "pow": math.pow,
            "abs": abs,
            "radians": math.radians
        })

    

    x = x0
    iteration = 1

    while iteration <= max_iterations:
        x_next = g(x)
        print(f"Iteration {iteration}: x = {x_next}, f(x_next) = {abs(f(x_next))}")

        if abs(f(x_next)) < tol:  # Stopping condition
            print(f"Root found: x ≈ {x_next}, after {iteration} iterations.")
            return x_next
        
        # Update x for the next iteration
        x = x_next
        iteration += 1

    # If max_iterations is reached without convergence
    print("Warning: Maximum iterations reached. The method may not have converged.")
    return None

     
    

    


print("Fixed-Point Iteration Method Solver")


f_input = input("Enter the function f(x) in Python syntax (e.g., 'x**2 - 4'): ")
print("You need to rearrange f(x) = 0 into the form x = g(x).")
g_input = input("Enter the function g(x) (e.g., '4/x' or '(x**2 + 4)/2'): ")

root_min = float(input("Enter the minimum of the root range: "))
root_max = float(input("Enter the maximum of the root range: "))

if root_min >= root_max:
    print("Invalid range. The minimum must be less than the maximum.")
else:

    x0 = (root_min + root_max) / 2
    print(f"Initial guess (x0): {x0}")

    tol = float(input("Enter the tolerance (default 1e-3): ") or 1e-3)

    result = fixed_point_iteration(g_input, f_input, x0, tol)
    
    if result is not None:
        print(f"Approximated root: {result}")
    else:
        print("The method did not converge. Try a different g(x) or initial guess.")