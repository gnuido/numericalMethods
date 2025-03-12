#evaluateFunction.py

def evaluateFunction(function, value):
    stringValue = str(value)            #.replace() is used with two strings only
    evaluateFunction = function.replace('x', stringValue)   
    evaluationResult = eval(evaluateFunction)       #eval() does evaluate down to a value, albeit only from a string that describes an equation
    return(evaluationResult)
