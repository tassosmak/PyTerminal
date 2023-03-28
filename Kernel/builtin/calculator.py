from src.utils import add_depend, sys
add_depend(sys.argv[1])
from Kernel.RendererKit import Renderer as RD

import ply.lex as lex
import ply.yacc as yacc

# Define the tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Define the regular expressions for the tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Define how to handle the NUMBER token
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define how to handle whitespace
t_ignore = ' \t'

# Define how to handle errors
def t_error(t):
    RD.CommandSay(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Define the grammar
def p_expression(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[3] == 0:
            p[0] = None
        else:
            p[0] = p[1] / p[3]


def p_expression_number(p):
    '''
    expression : NUMBER
    '''
    p[0] = p[1]

def p_expression_parentheses(p):
    '''
    expression : LPAREN expression RPAREN
    '''
    p[0] = p[2]

def p_error(p):
    RD.CommandSay("Syntax error")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Define a function to evaluate the input expression
def evaluate_expression(expression):
    result = parser.parse(expression, lexer=lexer)
    if result is None:
        return "Error: division by zero"
    else:
        return result

operation = evaluate_expression(RD.CommandQuest(type='3', msg='Type Your Mathematic Operation'))
RD.CommandPush(f'Your Result Is {operation}')