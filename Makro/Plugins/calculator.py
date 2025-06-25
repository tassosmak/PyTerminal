from src.utils import add_depend, sys
add_depend(sys.argv[1])
from Makro.MakroCore.RendererKit import Renderer as RD

# Define a dictionary to store variables and their values
variables = {}

# Define a dictionary to store user-defined functions
functions = {}

# Define a list to store the history of calculations
history = []

def calculate(expression):
    """
    Evaluate an arithmetic expression and return the result.
    """
    # Evaluate variables and functions
    expression = evaluate_variables(expression)
    expression = evaluate_functions(expression)

    # Evaluate the expression
    try:
        result = eval(expression, variables)
    except ZeroDivisionError:
        result = 'Infinity'
    except Exception as e:
        result = 'Error: ' + str(e)

    # Save the result to the history
    history.append(expression + ' = ' + str(result))

    return result

def evaluate_variables(expression):
    """
    Replace variables in an expression with their values.
    """
    for var in variables:
        expression = expression.replace(var, str(variables[var]))
    return expression

def evaluate_functions(expression):
    """
    Replace function calls in an expression with their results.
    """
    for func in functions:
        while func in expression:
            start = expression.index(func)
            end = start + len(func)
            depth = 0
            for i, c in enumerate(expression[end:]):
                if c == '(':
                    depth += 1
                elif c == ')':
                    if depth == 0:
                        arg = expression[end:end+i]
                        result = str(functions[func](arg))
                        expression = expression[:start] + result + expression[end+i+1:]
                        break
                    else:
                        depth -= 1
    return expression

def parse_assignment(expression):
    """
    Parse an assignment expression of the form "var = expression".
    """
    try:
        var, expression = expression.split('=')
        var = var.strip()
        expression = expression.strip()
        result = calculate(expression)
        variables[var] = result
        return var + ' = ' + str(result)
    except:
        return 'Error: Invalid assignment'

def parse_function(expression):
    """
    Parse a function definition expression of the form "def func(arg) = expression".
    """
    try:
        name, args = expression.split('(')
        args = args.strip(')').split(',')
        expression = args.pop().strip()
        name = name[4:].strip()
        args = [a.strip() for a in args]
        functions[name] = lambda x: calculate(expression, dict(zip(args, x.split(','))))
        return 'Defined function: ' + name
    except:
        return 'Error: Invalid function definition'

def parse_expression(expression):
    """
    Parse an expression and return the result.
    """
    if '=' in expression:
        return parse_assignment(expression)
    elif expression.startswith('def '):
        return parse_function(expression)
    else:
        return str(calculate(expression))

def print_history():
    """
    Print the history of calculations.
    """
    for h in history:
        RD.CommandShow(msg=h).Info()

# Define the main loop
while True:
    # Get input from the user
    expression = RD.CommandShow(msg='Enter Your Operation', header='Calculator').Input()
    
    # Exit the program if the user types "exit"
    if expression == 'exit':
        break

    # Print the history if the user types "history"
    if expression == 'history':
        print_history()
        continue

    # Parse and evaluate the expression
    result = parse_expression(expression)
    RD.CommandShow(f'Your Result Is {result}', 'Calculator').Push()