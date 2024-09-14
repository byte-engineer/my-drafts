# Draft/Librarys/sympy.py

import sympy as sym
import os
os.system('cls')

#|> This is built-in python module.
#|> This module deal with symbolic math in python
#|> You should open this library in .ipynb file.

# Numbers--------------------------------------------------------------------
# Float numbers in python (or most other languages) has about 15 digets presoin

# Store a rational number.
sym.Rational(22, 7)                                      # Return => 22/7

# Simplfy
sym.S('0.[3]')                                           # 0.[3] == 0.333. . .   # Return => 1/3

# Limit denominator.
sym.Rational('3.141592653589793').limit_denominator(10)  # Return => 22/7
sym.Rational('3.141592653589793').limit_denominator(100) # Return => 311/99


# Define a function----------------------------------------------------------

# First define the variables.
# We have several variables features:
# * real
# * positive
# * integer
# * seq                   --> is iterable

# Variables
x, a, b, c, d = sym.symbols("x a:d", cls= sym.var, real= True, positive= True)

# Functions
f, r = sym.symbols('f,r', cls= sym.Function)

# We can new write any symbolic math Function.
f = x**6 - 3*x**3 + x

# If we have a rational number use this method Don't write it 1/3 directly.
r = x**sym.Rational(1, 3)     


# Get Max & Min of function.
sym.maximum(f, x, domain= sym.Reals)
sym.minimum(f, x, domain= sym.Reals)

# Decreasing or Increacing
sym.is_decreasing(f, sym.Interval(0, sym.oo))
sym.is_increasing(f, sym.Interval(-80, 0))

# Solve equations--------------------------------------------------------------

equation = sym.Eq((x**2)-1, 0)       # Our equation => x^2 -1 = 0
solution = sym.solve(equation, x)    # Solve equation for 'x' Note: solution can be a number, interval or equation.

# Calculus---------------------------------------------------------------------

# Get the limit
lim = sym.limit(f, x, sym.oo)              # limit f(x) when x goes to 0

# We can get the Derivative.
df = sym.diff(f, x, 1)                     # Diff(function, with respect of, number of derivative)

# We can get the integration.
inte = sym.integrate(f, x)                 # Integral of f(x) in rspect of x


# Substitution-----------------------------------------------------------------

# Subtitute a variable.
f.subs(a, 3)                              # x^6 - 3x^3 + x

# Replacing a subexpression with another subexpression
f.subs(x, sym.sqrt(x))                    # Output => -a*x**(3/2) + sqrt(x) + x**3

# Get a float value if not.
f.subs((x, 2), (a, 1)).evalf(4)           # Output => 58.00     | We can write the number of digits that we whant to comput. 

# Get a normal python function 
lam_f = sym.lambdify((a, x), f)
lam_f(1, 2)                               # Output => 58


# Other computation-------------------------------------------------------------

# Integer least common multiple
sym.ilcm(5, 10, 15)                      # Output => 30

# Integer greatest common divisor
sym.igcd(5, 10, 15)                      # Output => 5
