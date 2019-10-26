from ply import lex
import ply.yacc as yacc
#import pprint as pp
import sys

# -------------------------------------------------------
#                   DEFINE SCOPE CLASS
# -------------------------------------------------------

class Scope(object):
    def __init__(self):
        self.i = 1
        self.path = [1]
        self.good = True

def add_scope():
    scope.i = scope.i + 1

def get_scope():
    return scope.i

def reset_scope():
    scope.i = 1
    scope.path = [1]
    scope.good = True

def not_good():
    scope.good = False

def get_good():
    return scope.good

def add_to_path():
    scope.path.append(get_scope())

def get_path():
    return scope.path

def pop_path():
    scope.path.pop()

class Scope_table(object):
    def __init__(self):
        self.table = {}

def add_table(scope, data):
    if scope in scope_table.table:
        scope_table.table[scope].update(data)
    else:
        scope_table.table[scope] = data

def clear_table():
    scope_table.table.clear()

scope = Scope()
scope_table = Scope_table()

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
    ('nonassoc', 'IF'),
    ('nonassoc', 'ELSE'),
    ('left', 'COMMA'),
    ('right', 'EQUALS'),
    ('nonassoc', 'EQ', 'NOT_EQ', 'LESS_EQ', 'GREATER_EQ'),
)


# -------------------------------------------------------
#                      CLASSES
# -------------------------------------------------------

class Node:
    pass

class ErrorNode(Node):
    pass

class Start(Node):
    def __init__(self, Function, constants = None):
        self.Function = Function
        self.constants = constants

class Variable(Node):
    def __init__(self, type, init, pos):
        self.type = type
        self.init = init
        self.pos = pos

class Init(Node):
    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

class Function(Node):
    def __init__(self, params, expression):
        self.params = params
        self.expression = expression

class Expressions(Node):
    def __init__(self, expressions):
        self.expressions = expressions

class ConstantList(Node):
    def __init__(self, constants):
        self.type = 'constants'
        self.constants = constants

class Constant(Node):
    def __init__(self, init, pos):
        self.type = 'constant'
        self.pos = pos
        self.init = init

class Statement(Node):
    def __init__(self, left, op, right, pos):
        self.left = left
        self.op = op
        self.right = right
        self.pos = pos

class While(Node):
    def __init__(self, kw, cond, instr):
        self.keyword = kw
        self.cond = cond
        self.instr = instr


class If(Node):
    def __init__(self, cond, ithen, ielse = None):
        self.cond = cond
        self.ithen = ithen
        self.ielse = ielse

class Get(Node):
    def __init__(self, type, id):
        self.type = type
        self.id = id

class Args(Node):
    def __init__(self, type, id):
        self.type = type
        self.id = id

class Assigment(Node):
    def __init__(self, id, expr, pos):
        self.type = 'assigment'
        self.id = id
        self.expr = expr
        self.pos = pos

# -------------------------------------------------------
#                   RULES
# -------------------------------------------------------

# Starting rule
def p_start( p ):
    '''
    start : function
    '''
    p[0] = Start(p[1])
    #pp.pprint(vars(scope_table))
    if get_good():
        print("Successfully Parsed")
    clear_table()
    reset_scope()

def p_start_constants( p ):
    '''
    start :  constants function
    '''

    p[0] = Start(p[2], p[1])
    #pp.pprint(vars(scope_table))
    if get_good():
        print("Successfully Parsed")
    clear_table()
    reset_scope()


# Rule that defines consonants and variables before and after the main function, where the main can have parameters
# and inside the main an expression
def p_function( p ):
    'function : new_scope VOID MAIN LPAREN params RPAREN LBRACE expressions RBRACE'
    p[0] = Function(p[4], p[7])

def p_empty_function( p ):
    'function : new_scope VOID MAIN LPAREN params RPAREN LBRACE RBRACE'
    p[0] = Function(p[4], [])
    pop_path()

# Rule that defines the parameters that are passed to the main function, they can be empty or string[] args
# where args can be any name
def p_params( p ):
    '''
    params :  STR LSQUARE RSQUARE ID
    '''
    p[0] = Args(p[1], p[4])
    entry = {
        p[0].id : ('array', 'str[]', 'params')
    }
    add_table(tuple(get_path()), entry)

def p_empty_params( p ):
    '''
    params : empty
    '''
    p[0] = []

# Recursive rule that defines that an expression can have at least one expression or multiple expressions
def p_list_expressions( p ):
    '''
    expressions :     expressions expression
    '''
    p[0] = Expressions(p[1].expressions + [p[2]])

def p_expressions( p ) :
    '''
    expressions : expression
    '''
    p[0] = Expressions([p[1]])

# Rule that defines the type of expression, this can be variable and constants declarations, while loop, if condition,
# print a value in the console, get value from the console or be empty (via the constant rule)
def p_expression( p ):
    '''
    expression :   constants
                 | while
                 | if
                 | assigned
                 | print
                 | get
    '''
    p[0] = p[1]

def p_assigned( p ):
    '''
    assigned : ID ASSIGN type SEMICOLON
    '''
    p[0] = Assigment(p[1], p[3], p.lineno)
    path = get_path()[:]
    exist = False
    exit = False
    while(path):
        if tuple(path) in scope_table.table:
            if p[1] in scope_table.table[tuple(path)]:
                temp = scope_table.table[tuple(path)][p[1]]
                if temp[1] == 'int':
                    if not isinstance(p[3], int):
                        print('ERROR : Cannot assign "' + str(p[3]) + '" to ' + str(temp[1]))
                        exit = True
                elif temp[1] == 'string':
                    if not isinstance(p[3], str):
                        print('ERROR : Cannot assign "' + str(p[3]) + '" to ' + str(temp[1]))
                        exit = True
                elif temp[1] == 'bool':
                    if p[3] != False and p[3] != True:
                        print('ERROR : Cannot assign "' + str(p[3]) + '" to ' + str(temp[1]))
                        exit = True
                exist = True
                break
        path.pop()
    if exist == False:
        print('ERROR: Variable "' +  str(p[1]) + '" was not declared')
        exit = True
    if exit == True:
        not_good()


# Rule that defines the while loop, inside the while loop it is possible to have multiple expressions
def p_while( p ):
    '''
    while : WHILE LPAREN statement RPAREN LBRACE new_scope expressions RBRACE
    '''
    p[0] = While(p[1], p[2], p[7])
    pop_path()

# Rule that defines the if statement, this statment can have an else
def p_if( p ):
    '''
    if :   IF LPAREN statement RPAREN LBRACE new_scope expressions RBRACE
    '''
    p[0] = If(p[3], p[7])
    pop_path()

def p_if_else( p ):
    '''
    if :  IF LPAREN statement RPAREN LBRACE new_scope expressions RBRACE ELSE LBRACE new_scope expressions  RBRACE
    '''
    p[0] = If(p[3], p[7], p[12])
    pop_path()
    pop_path()


# Rule that defines the statments that are inside the while loop and if condition, they have a type which is translated to
# numbers, strings, and boolean values or ids and a logic_op that stands for logical operator that can be ==, <=, >=, <, > and !=
# Example: x == 1
def p_statement( p ):
    '''
    statement :   type logic_op type
    '''
    p[0] = Statement(p[1], p[2], p[3], p.lineno)

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
    p[0] = p[1]

# Rule that defines that a variable should have a type which is the var_type, an id and assigned statment and finish with a
# semicolon. The current var types are int, string, and bool.
# Example: int x = 12;
# Example: string y;
def p_variable( p ):
    '''
    variable :    var_type init SEMICOLON
    '''
    p[0] = Variable(p[1], p[2], p.lineno)
    entry = {
        p[0].init.id : (p[0].init.expr, p[1], 'variable')
    }
    add_table(tuple(get_path()), entry)

def p_init_value( p ):
    '''
    init :  ID ASSIGN type
    '''
    p[0] = Init(p[1], p[3])

def p_init( p ):
    '''
    init : ID
    '''
    p[0] = Init(p[1], [])

# Rule that states all the possible values for the type of variables: int, string and bool
def p_var_type( p ):
    '''
    var_type :    INT
                | STR
                | BOOL
    '''
    p[0] = p[1]


# Rule that states the different types of values: number(1,2,5,-5,-7, ...), string("Hello", "", "kd", ...), boolean(true, false)
# and id(var_x, x, Var_x, ...)
def p_type( p ):
    '''
    type :    NUMBER
            | STRING
            | boolean
            | ID
    '''
    p[0] = p[1]

# Rule that defines the only two values in a boolean
def p_boolean( p ):
    '''
    boolean :   TRUE
              | FALSE
    '''
    p[0] = p[1]

# Rule that defines constants and variables, it uses recursion to be able to have more than one constant or variable
def p_list_constants( p ):
    '''
    constants :   constants constant
                | constants variable
    '''
    if p[2]:
        p[0] = ConstantList(p[1].constants + [p[2]])
    else:
        p[0] = p[1]



def p_constants( p ):
    '''
    constants :    constant
                |  variable
    '''
    if p[1]:
        p[0] = ConstantList([p[1]])
    else:
        p[0] = ConstantList([])

# Rule that states that a constant always start with the reserved word enum then an id and then the assigned statement and finish
# with a semicolon, it also states that constant can be empty
def p_constant( p ):
    '''
    constant :    ENUM init SEMICOLON
    '''
    p[0] = Constant(p[2], p.lineno)
    type = None
    if (isinstance(p[0].init.expr, int)):
        type = 'int'
    elif (isinstance(p[0].init.expr, str)):
        type = 'string'
    elif (p[0].init.expr == 'False' or p[0].init.expr == 'True'):
        type = 'bool'
    entry = {
        p[0].init.id : (p[0].init.expr, type ,'constant')
    }
    add_table(tuple(get_path()), entry)


# Rule that states that a print statment starts with the reserved word writeln then a left parenthesis then a different type of value
# followed by a right parenthesis and finish with a semicolon
# The types of possible values can be a number, a string, a boolean value or a variable (id)
# Example: writeln(x);
def p_print( p ):
    '''
    print :   WRITELN LPAREN type RPAREN SEMICOLON
    '''
    p[0] = p[3]
    if not (isinstance(p[3], str)) and not (isinstance(p[3], int)):
        path = get_path()[:]
        exist = False
        exit = False
        while(path):
            if tuple(path) in scope_table.table:
                if p[3] in scope_table.table[tuple(path)]:
                    exist = True
                    break
            path.pop()
        if exist == False:
            print('ERROR: Variable "' + str(p[3]) + '" was not declared')
            exit = True
        if exit == True:
            not_good()

# Rule that states a get statement wich states that is starts with the reserved word readf followed by a left parenthesis, a string
# a comma, and ampersand, an id, a right parenthesis and finish with a semicolon
# Example: readf("%i", &x);
def p_get( p ):
    '''
    get :     READF LPAREN gets COMMA AMPERSAND ID RPAREN SEMICOLON
    '''
    p[0] = Get(p[3], p[6])
    path = get_path()[:]
    exist = False
    exit = False
    while(path):
        if tuple(path) in scope_table.table:
            if p[6] in scope_table.table[tuple(path)]:
                temp = scope_table.table[tuple(path)][p[6]]
                if temp[1] == 'int':
                    if str(p[3]) != '"%i"':
                        print('ERROR: Cannot use "' + str(p[3]) + ' to get an int')
                        exit = True
                elif temp[1] == 'string':
                    if str(p[3]) != '"%s"':
                        print('ERROR: Cannot use "' + str(p[3]) + 'to get a string')
                        exit = True
                elif temp[1] == 'bool':
                    if str(p[3]) != '"%d"':
                        print('ERROR: Cannot use "' + str(p[3]) + 'to get a bool')
                        exit = True
                exist = True
                break
        path.pop()
    if exist == False:
        print('ERROR: Variable "' + str(p[6]) + '" was not declared')
        exit = True
    if exit == True:
        not_good()

def p_gets( p ):
    '''
    gets :    GET_INT
            | GET_STRING
            | GET_BOOL
    '''
    p[0] = p[1]

# Rule that states an empty state
def p_empty( p ):
    'empty :'
    pass

# -------------------------------------------------------
#                  SCOPE RULES
# -------------------------------------------------------

def p_new_scope( p ):
    'new_scope : empty'
    add_scope()
    add_to_path()

# -------------------------------------------------------
#                   ERROR HANDLERS
# -------------------------------------------------------

def handle_error(self, where, p):
    print("Syntax error in %s at line %d, column %d, at token LexToken(%s, '%s')" %\
      (where, p.lineno, self.scanner.find_tok_column(p), p.type, p.value))

# Error handler for when it passed the lexer but failed at the grammatic rules
def p_error( p ):
    if not p:
        print("Syntax error at EOF")
    else :
        print("Syntax error at line {0}" .format(p.lineno))
    clear_table()
    reset_scope()



# Function to give the data from the files to the lexer and then to the yacc
def process(data):
    lexer = lex.lex()
    lexer.input(data)
    #while True:
    #    tok = lexer.token()
    #    if not tok:
    #       break      # No more input
    #    print(tok)
    parser = yacc.yacc()
    parser.parse(data)
