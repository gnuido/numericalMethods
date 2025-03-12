#bisection.py

#bisection is a closed numerical method, used to find a function's real roots.
#[a, b] are the values used in the iterations as the starting and ending points, accordingly.

import verifyInput
print('Enter the iteration interval\'s starting point')
a = verifyInput.verifyInteger()
print('Enter the iteration interval\'s ending point')
b = verifyInput.verifyInteger()

print('Enter the desired absolute error tolerance percentage(%): ')
tolerance = verifyInput.verifyFloatingPoint()

function = input('Enter the function f(x)= \n(mind the syntax)\n')

#-------------
iteration = 0      #iteration indexing

import evaluateFunction
f_a = evaluateFunction.evaluateFunction(function, a)
f_b = evaluateFunction.evaluateFunction(function, b)

if f_a * f_b > 0:
    print('Error, no real roots present in the given interval')
    continue
elif f_a * f_b < 0:
        
else:
    if f_a == 0:
        print(f 'x = {a} is a root for the f function',
                'Absolute error = 0%')

    elif f_b == 0:
        print(f 'x = {b} is a root for the f function',
              'Absolute_error = 0%')
