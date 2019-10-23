# Author: Mariana Perez
# D compiler
# Can be run using the following command: python calc.py

from ply import lex
import ply.yacc as yacc
from ast import *


# -------------------------------------------------------
#                   LIST OF TOKENS
# -------------------------------------------------------

# List of reserved words
reserved = {
    'bool'      : 'BOOL',
    'else'      : 'ELSE',
    'enum'      : 'ENUM',
    'if'        : 'IF',
    'int'       : 'INT',
    'main'      : 'MAIN',
    'readf'     : 'READF',
    'string'    : 'STR',
    'void'      : 'VOID',
    'while'     : 'WHILE',
    'writeln'   : 'WRITELN',
}

# List of available tokens
tokens = [
    'AMPERSAND',
    'ASSIGN',
    'COMMA',
    'EQ',
    'GREATER',
    'GREATER_EQ',
    'ID',
    'LBRACE',
    'LESS',
    'LESS_EQ',
    'LPAREN',
    'NOT_EQ',
    'NUMBER',
    'RBRACE',
    'RPAREN',
    'SEMICOLON',
    'STRING',
    'TRUE',
    'FALSE',
    'LSQUARE',
    'RSQUARE',
    'GET_INT',
    'GET_STRING',
    'GET_BOOL',
]

tokens = reserved.values() + tokens


# -------------------------------------------------------
#                   SIMPLE TOKENS
# -------------------------------------------------------
t_ignore = ' \t'

# Regular expression rules

t_LPAREN        = r'\('
t_RPAREN        = r'\)'
t_LBRACE        = r'\{'
t_RBRACE        = r'\}'
t_LSQUARE       = r'\['
t_RSQUARE       = r'\]'
t_SEMICOLON     = r'\;'
t_COMMA         = r'\,'
t_ASSIGN        = r'='
t_GREATER       = r'>'
t_LESS          = r'<'
t_EQ            = r'=='
t_NOT_EQ        = r'!='
t_GREATER_EQ    = r'>='
t_LESS_EQ       = r'<='
t_AMPERSAND     = r'\&'


# -------------------------------------------------------
#                   COMPLEX TOKENS
# -------------------------------------------------------

def t_TRUE(t):
    r'(true)' # regex for true
    t.value = True
    return t

def t_FALSE(t):
    r'(false)'  # regrex for false
    t.value = False
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*' # regex for the name of the variables and constants
    if reserved.has_key(t.value): # Checks if the value is present the reserved words first
        t.type = reserved[t.value] # If true then it is a reserved word, otherwise it is an id
    return t

def t_NUMBER( t ):
    r'[+-]?\d+' # regex for positive and negative numbers
    try:
        t.value = int( t.value ) # try to put the number into an int
    except ValueError: #If it is not possible raise error
        print("Value too long ", t.value)
        t.value = 0
    return t

def t_GET_INT( t ):
    r'("%i")'
    return t

def t_GET_STRING( t ):
    r'("%s")'
    return t

def t_GET_BOOL( t ):
    r'("%d")'
    return t

def t_STRING(t):
    r'"[^\n]*?(?<!\\)"' #regex to match everything that is surrounded by ""
    t.value = t.value[1:-1]
    return t

def t_newline( t ):
  r'\n+'    # regex for a new line
  t.lexer.lineno += len( t.value )

# -------------------------------------------------------
#                   IGNORED TOKENS
# -------------------------------------------------------

# Ignore comments with //
def t_COMMENT(t):
    r'//.*'
    t.lineno += t.value.count('\n')
    pass

# Ignore comments with /* */
def t_LARGERCOMMENT(t):
    r'/\*[\w\W]*?\*/'
    t.lineno += t.value.count('\n')
    pass

# -------------------------------------------------------
#                   ERROR HANDLER
# -------------------------------------------------------

# If there is a character that doesn't match any of the previous rules throw an error
def t_error( t ):
  print("Illegal character '{0}' at line {1}" .format(t.value[0], t.lineno))
  t.lexer.skip( 1 )


# -------------------------------------------------------
#                      PRECEDENCE
# -------------------------------------------------------

predecende = (
    ('left', 'COMMA'),
    ('right', 'EQUALS'),
)


# -------------------------------------------------------
#                      CLASSES
# -------------------------------------------------------
class Node:
    pass

class Iden(Node):
    def __init__(self, name, lineno):
        self.name = name
        self.lineno = lineno

class Start(Node):
    def __init__(self, Function):
        self.name = 'Start'
        self.Function = Function
        self.show()

    def show(self):
        print("Start => Function")
        self.Function.show()

class Function(Node):
    def __init__(self, constants1, params, expression, constants2):
        self.name = 'Function'
        self.constants = constants1
        self.params = params
        self.expression = expression
        self.constants = constants2

    def show(self):
        print("Function => constants VOID MAIN LPAREN params RPAREN LBRACE expression RBRACE constants")


# -------------------------------------------------------
#                   RULES
# -------------------------------------------------------

# Starting rule
def p_start( p ):
    'start : function'
    p[0] = Start(p[1])
    print("Successfully Parsed")

# Rule that defines consonants and variables before and after the main function, where the main can have parameters
# and inside the main an expression
def p_function( p ):
    'function : constants VOID MAIN LPAREN params RPAREN LBRACE expressions RBRACE constants'
    p[0] = Function(p[1], p[5], p[8], p[10])

# Rule that defines the parameters that are passed to the main function, they can be empty or string[] args
# where args can be any name
def p_params( p ):
    '''
    params :  STR LSQUARE RSQUARE ID
            | empty
    '''
# Recursive rule that defines that an expression can have at least one expression or multiple expressions
def p_expressions( p ):
    '''
    expressions :     expressions expression
                    | expression
    '''
# Rule that defines the type of expression, this can be variable and constants declarations, while loop, if condition,
# print a value in the console, get value from the console or be empty (via the constant rule)
def p_expression( p ):
    '''
    expression :   constants
                 | while
                 | if
                 | ID assigned SEMICOLON
                 | print
                 | get
    '''

# Rule that defines the while loop, inside the while loop it is possible to have multiple expressions
def p_while( p ):
    '''
    while : WHILE LPAREN statement RPAREN LBRACE expressions RBRACE
    '''

# Rule that defines the if statement, this statment can have an else
def p_if( p ):
    '''
    if :   IF LPAREN statement RPAREN LBRACE expressions RBRACE
         | IF LPAREN statement RPAREN LBRACE expressions RBRACE ELSE LBRACE expressions RBRACE
    '''

# Rule that defines the statments that are inside the while loop and if condition, they have a type which is translated to
# numbers, strings, and boolean values or ids and a logic_op that stands for logical operator that can be ==, <=, >=, <, > and !=
# Example: x == 1
def p_statement( p ):
    '''
    statement :   type logic_op type
    '''

# Rule that states the possible value for the logical operator
def p_logic_op( p ):
    '''
    logic_op :    EQ
                | NOT_EQ
                | GREATER
                | GREATER_EQ
                | LESS
                | LESS_EQ
    '''

# Rule that defines that a variable should have a type which is the var_type, an id and assigned statment and finish with a
# semicolon. The current var types are int, string, and bool.
# Example: int x = 12;
# Example: string y;
def p_variable( p ):
    '''
    variable :   var_type ID assigned SEMICOLON
    '''

# Rule that states all the possible values for the type of variables: int, string and bool
def p_var_type( p ):
    '''
    var_type :    INT
                | STR
                | BOOL
    '''

# Rule that states that an assigment could be the assigned value (=) and a type of value (number, boolean, string or another id),
# or an assigment can also be empty in order to just declare the variable without assigning anything
def p_assigned( p ):
    '''
    assigned :    ASSIGN type
                | empty
    '''

# Rule that states the different types of values: number(1,2,5,-5,-7, ...), string("Hello", "", "kd", ...), boolean(true, false)
# and id(var_x, x, Var_x, ...)
def p_type( p ):
    '''
    type :    NUMBER
            | STRING
            | boolean
            | ID
    '''

# Rule that defines the only two values in a boolean
def p_boolean( p ):
    '''
    boolean :   TRUE
              | FALSE
    '''

# Rule that defines constants and variables, it uses recursion to be able to have more than one constant or variable
def p_constants( p ):
    '''
    constants :   constants constant
                | constants variable
                | constant
                | variable
    '''

# Rule that states that a constant always start with the reserved word enum then an id and then the assigned statement and finish
# with a semicolon, it also states that constant can be empty
def p_constant( p ):
    '''
    constant :    ENUM ID assigned SEMICOLON
                | empty
    '''

# Rule that states that a print statment starts with the reserved word writeln then a left parenthesis then a different type of value
# followed by a right parenthesis and finish with a semicolon
# The types of possible values can be a number, a string, a boolean value or a variable (id)
# Example: writeln(x);
def p_print( p ):
    '''
    print :   WRITELN LPAREN type RPAREN SEMICOLON
    '''

# Rule that states a get statement wich states that is starts with the reserved word readf followed by a left parenthesis, a string
# a comma, and ampersand, an id, a right parenthesis and finish with a semicolon
# Example: readf("%i", &x);
def p_get( p ):
    '''
    get :     READF LPAREN gets COMMA AMPERSAND ID RPAREN SEMICOLON
    '''

def p_gets( p ):
    '''
    gets :    GET_INT
            | GET_STRING
            | GET_BOOL
    '''

# Rule that states an empty state
def p_empty( p ):
    'empty :'
    pass

# Error handler for when it passed the lexer but failed at the grammatic rules
def p_error( p ):
    print("Syntax error at line {0}" .format(p.lineno))

# Function to give the data from the files to the lexer and then to the yacc
def process(data):
    lexer = lex.lex()
    lexer.input(data)
    #while True:
    #    tok = lexer.token()
    #    if not tok:
    #       break      # No more input
    #    print(tok)
    yacc.yacc()
    yacc.parse(data)



if __name__ == "__main__":
    import sys

    # -------------------------------------------------------
    #                       PASSING TESTS
    # -------------------------------------------------------
    print("--------Valid Tests--------")
    # Test1: Un programa sencillo con un comentario de una palabra
    print("Test 1: Comentario de una palabra")
    f = open('./Tests/Test1.d', 'r')
    data = f.read()
    f.close()
    process(data)

    #Test2: Un programa sencillo con un comentario de una linea
    print("Test 2: Comentario de una linea")
    f = open('./Tests/Test2.d', 'r')
    data = f.read()
    f.close()
    process(data)

    # Test3: Un programa sencillo con la definicion de una variable.
    print("Test 3: Definicion de una variable")
    f = open('./Tests/Test3.d', 'r')
    data = f.read()
    f.close()
    process(data)

    # Test4: Un programa sencillo con la definicion de una constante.
    print("Test 4: Definicion de una constante")
    f = open('./Tests/Test4.d', 'r')
    data = f.read()
    f.close()
    process(data)

    # Test5: Un programa sencillo con cadenas.
    print("Test 5: Programa con cadenas")
    f = open('./Tests/Test5.d', 'r')
    data = f.read()
    f.close()
    process(data)

    # Test6: Un programa sencillo con variables de todos los tipos de datos.
    print("Test 6: Todos los tipos de datos")
    f = open('./Tests/Test6.d', 'r')
    data = f.read()
    f.close()
    process(data)

    # Test7: Un programa sencillo con un ciclo y una condicional.
    print("Test 7: ciclo y una condicional")
    f = open('./Tests/Test7.d', 'r')
    data = f.read()
    f.close()
    process(data)

    # Test8: Un programa sencillo con un ciclo y una condicional anidada.
    print("Test 8: ciclo y una condicional anidados")
    f = open('./Tests/Test8.d', 'r')
    data = f.read()
    f.close()
    process(data)

    # Test9: Un programa sencillo usando las instrucciones de entrada y salida.
    print("Test 9: Instrucciones de entrada y de salida")
    f = open('./Tests/Test9.d', 'r')
    data = f.read()
    f.close()
    process(data)

    # Test10: Un programa sencillo con todas las instrucciones que has definido.
    print("Test 10: Todas las instrucciones definidas")
    f = open('./Tests/Test10.d', 'r')
    data = f.read()
    f.close()
    process(data)

# -------------------------------------------------------
#                       FAILING TESTS
# -------------------------------------------------------

    # Test11 y 12: Un programa sencillo con la definicion de una variable en el lugar incorrecto y en el orden incorrecto.
    print("\n--------Invalid tests--------")
    print("Test 11: Variable en el lugar incorrecto")
    f = open('./Tests/Test11.d', 'r')
    data = f.read()
    f.close()
    process(data)

    print("Test 12: Varible en el orden incorrecto.")
    f = open('./Tests/Test12.d', 'r')
    data = f.read()
    f.close()
    process(data)

    # Test13: Un programa sencillo que utiliza una cadena, variable y constante en un lugar que no esta permitido.
    print("Test 13: Cadena en un lugar no permitido")
    f = open('./Tests/Test13.d', 'r')
    data = f.read()
    f.close()
    process(data)

    # Test14: Un programa sencillo con un ciclo definido pero usando una gramatica incorrecta.
    print("Test 14: Ciclo definido pero usando gramatica incorrecta")
    f = open('./Tests/Test14.d', 'r')
    data = f.read()
    f.close()
    process(data)

    print("Test 15: Constante en el lugar incorrecto")
    f = open('./Tests/Test15.d', 'r')
    data = f.read()
    f.close()
    process(data)
