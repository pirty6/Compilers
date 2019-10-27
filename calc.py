from ply import lex
import ply.yacc as yacc
#import pprint as pp
import sys

# -------------------------------------------------------
#                   DEFINE SCOPE CLASS
# -------------------------------------------------------

# Scope class that will use the i as an index, a stack of scopes
# called path and a boolean variable to verify if the program was
# parse correctly
class Scope(object):
    def __init__(self):
        self.i = 1
        self.path = [1]
        self.good = True

# Function that will ad a 1 to the current level of the scope
def add_scope():
    scope.i = scope.i + 1

# Function to get the current level of the scope
def get_scope():
    return scope.i

# Function that will reset all the variables to the class Scope in order to test
# more than 1 test case consecutively
def reset_scope():
    scope.i = 1
    scope.path = [1]
    scope.good = True

# Function that will say that there were errors on the program
def not_good():
    scope.good = False

# Function to verify if the program was parsed Successfully or not
def get_good():
    return scope.good

# Function that will append the current scope level into the path
def add_to_path():
    scope.path.append(get_scope())

# Function that will return the current path
def get_path():
    return scope.path

# Function to get the first item out from the stack
def pop_path():
    scope.path.pop()

# Class that will define the Symbols table
class Scope_table(object):
    def __init__(self):
        self.table = {}

# Function that adds data to the Symbols table, it verifies if the path
# already exist in the table, if so append the new information if not
# create a new entry
def add_table(scope, data):
    # We will use the stack of scopes as the key to keep everything in their corresponding scope
    if scope in scope_table.table:
        scope_table.table[scope].update(data)
    else:
        scope_table.table[scope] = data

# Function to clear all the entries in the table to be able to use it again
def clear_table():
    scope_table.table.clear()

# Initialize classes
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

# Base class of a Node
class Node:
    pass

# Class that will define the Start
class Start(Node):
    # Start is composed of constants that can be empty and a function that will be the main
    def __init__(self, Function, constants = None):
        self.Function = Function
        self.constants = constants

# Class that defines a variable
class Variable(Node):
    # Variable has a type of variable (int, string, bool) and an object init
    def __init__(self, type, init, pos):
        self.type = type
        self.init = init
        self.pos = pos

# Class that defines an Init which is an id and an expression (a = 3)
class Init(Node):
    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

# Class that defines the function, which takes parameters and an expression
class Function(Node):
    def __init__(self, params, expression):
        self.params = params
        self.expression = expression

# Class that defines an expression which can consist of one or more expressions
class Expressions(Node):
    def __init__(self, expressions):
        self.expressions = expressions

# Class that defines a list of constants that receive the constants
class ConstantList(Node):
    def __init__(self, constants):
        self.type = 'constants'
        self.constants = constants

# Class that defines a constant using an Init object
class Constant(Node):
    def __init__(self, init, pos):
        self.type = 'constant'
        self.pos = pos
        self.init = init

# Class that defines an stament such as x == 1
# where x is the left == is the op and 1 is the right
class Statement(Node):
    def __init__(self, left, op, right, pos):
        self.left = left
        self.op = op
        self.right = right
        self.pos = pos

# Class that defines a while loop, using the condition (x < 1) and the instructions (x = 2;)
class While(Node):
    def __init__(self, kw, cond, instr):
        self.keyword = kw
        self.cond = cond
        self.instr = instr

# Class that defines an If that takes as paramenters a Statement object (x == 1)
# The instructions of the if and the instructions for the else segment which as set as
# default to None
class If(Node):
    def __init__(self, cond, ithen, ielse = None):
        self.cond = cond
        self.ithen = ithen
        self.ielse = ielse

# Class that defines a writeln("%i", &x) where x is the id and "%i" is the type
class Get(Node):
    def __init__(self, type, id):
        self.type = type
        self.id = id

# Class that defines the parameters
class Args(Node):
    def __init__(self, type, id):
        self.type = type
        self.id = id

# Class that defines an assigment (x = 2) where x is the id and 2 is the expr
class Assigment(Node):
    def __init__(self, id, expr, pos):
        self.type = 'assigment'
        self.id = id
        self.expr = expr
        self.pos = pos

# -------------------------------------------------------
#                   RULES
# -------------------------------------------------------

# Starting rule for when there are no constants
def p_start( p ):
    '''
    start : function
    '''
    p[0] = Start(p[1])
    #pp.pprint(vars(scope_table))
    # If after parsing the code everything was good
    if get_good():
        # Print success message
        print("Successfully Parsed")
    # Reset everything
    clear_table()
    reset_scope()

# Starting rule for when there are constants
def p_start_constants( p ):
    '''
    start :  constants function
    '''

    p[0] = Start(p[2], p[1])
    #pp.pprint(vars(scope_table))
    # If after the parsing the code everything was good
    if get_good():
        # Print success message
        print("Successfully Parsed")
    # Reset everything
    clear_table()
    reset_scope()


# Rule that defines consonants and variables before and after the main function, where the main can have parameters
# and inside the main an expression
# Rule that defines a function with an expression
def p_function( p ):
    # At the start of the rule a new scope is added and added to the current stack
    'function : new_scope VOID MAIN LPAREN params RPAREN LBRACE expressions RBRACE'
    p[0] = Function(p[4], p[7])
    # After parsing the function rule pop the stack to return to the previous scope
    pop_path()

# Rule that defines a function withouth an expression inside
def p_empty_function( p ):
    # At the start of the rule a new scope is added and added to the current stack
    'function : new_scope VOID MAIN LPAREN params RPAREN LBRACE RBRACE'
    p[0] = Function(p[4], [])
    # After parsing the function rule pop the stack to return to the previous scope
    pop_path()

# Rule that defines the parameters that are passed to the main function, they can be empty or string[] args
# where args can be any name
# Rule that defines the basic declaration of parameters
def p_params( p ):
    '''
    params :  STR LSQUARE RSQUARE ID
    '''
    p[0] = Args(p[1], p[4])
    # Create an entry that the key will be the ID and will have the type as value
    entry = {
        p[0].id : ('array', 'str[]', 'params')
    }
    # Add the entry to the table
    add_table(tuple(get_path()), entry)

# Rule that defines that no parameters were given
def p_empty_params( p ):
    '''
    params : empty
    '''
    # Return nothing
    p[0] = []

# Recursive rule that defines that an expression can have at least one expression or multiple expressions
# Rule that defines more than one expression
def p_list_expressions( p ):
    '''
    expressions :     expressions expression
    '''
    p[0] = Expressions(p[1].expressions + [p[2]])

# Rule that defines a single expression
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

# Rule that defines an assigment to an existing variable
def p_assigned( p ):
    '''
    assigned : ID ASSIGN type SEMICOLON
    '''
    p[0] = Assigment(p[1], p[3], p.lineno)
    # Get the current path
    path = get_path()[:]
    exist = False # Boolean variable to verify if the variable already exist
    exit = False # Boolean variable that defines if there was an error in the parsing
    while(path): # While the path is not empty
        if tuple(path) in scope_table.table: # Check if the table contains the current stack of scopes
            if p[1] in scope_table.table[tuple(path)]: # If it does check if that entry contains the id that we are assigning
                temp = scope_table.table[tuple(path)][p[1]] #If it does check the type of variable that it is
                # Check if we are assigning the correct value according to the type of the variable if not print an error and declare that the parsing was not succesful
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
                break # Get out of the loop
        path.pop() # If the value was not found then pop the stack to check the variables in the parents
    if exist == False:
        print('ERROR: Variable "' +  str(p[1]) + '" was not declared') # If the stack is empty and the variable was not found throw error
        exit = True
    if exit == True:
        not_good()


# Rule that defines the while loop, inside the while loop it is possible to have multiple expressions
def p_while( p ):
    # before the expression create a new scope and add it to the stack of paths
    '''
    while : WHILE LPAREN statement RPAREN LBRACE new_scope expressions RBRACE
    '''
    p[0] = While(p[1], p[2], p[7])
    # Return to the previous scope (parent)
    pop_path()

# Rule that defines the if statement without else
def p_if( p ):
    # Before the expression inside the if create a new scope and add it to the stack
    '''
    if :   IF LPAREN statement RPAREN LBRACE new_scope expressions RBRACE
    '''
    p[0] = If(p[3], p[7])
    # Return to the previos scope (parent)
    pop_path()

# Rule that defines an if statement with an else
def p_if_else( p ):
    # Before both expressions create a new scope and add it to the stack
    '''
    if :  IF LPAREN statement RPAREN LBRACE new_scope expressions RBRACE ELSE LBRACE new_scope expressions  RBRACE
    '''
    p[0] = If(p[3], p[7], p[12])
    # Return to the parent scope
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
    # Create a new entry that will have as the key the id of the variable, and as values the expression of the variable and the type of variable
    p[0] = Variable(p[1], p[2], p.lineno)
    entry = {
        p[0].init.id : (p[0].init.expr, p[1], 'variable')
    }
    # Append it to the table
    add_table(tuple(get_path()), entry)

# Rule that defines that an initialization of a variable (int x = 10;)
def p_init_value( p ):
    '''
    init :  ID ASSIGN type
    '''
    p[0] = Init(p[1], p[3])

# Rule that defines the initialization of a variable without assigning any value to it
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

# Rule that defines a single constant or variable
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
    # Check what type of constant it is (int, string or bool) according to their assigned value
    if (isinstance(p[0].init.expr, int)):
        type = 'int'
    elif (isinstance(p[0].init.expr, str)):
        type = 'string'
    elif (p[0].init.expr == 'False' or p[0].init.expr == 'True'):
        type = 'bool'
    # Create a new entry where the key is the id of the constant
    entry = {
        p[0].init.id : (p[0].init.expr, type ,'constant')
    }
    # Add it to the table on it corresponding path of scopes
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
    # Check that the value is not a string, a boolean or an int, if it is not any of those values then it is an id and validation should take place
    if not (str(p[3]).startswith('"') and str(p[3]).endswith('"')) and not (isinstance(p[3], int)):
        path = get_path()[:] # Get the current path
        exist = False
        exit = False
        while(path): # Iterate the stack until it is empty
            if tuple(path) in scope_table.table: # if the path exists in the table
                if p[3] in scope_table.table[tuple(path)]: # Check if the variable exists in that scope
                    exist = True # If it exist get out of the loop
                    break
            path.pop() # If it not exist check the parent scope to check if the variable exist
        if exist == False: # If the variable does not exisit throw an error
            print('ERROR: Variable "' + str(p[3]) + '" was not declared')
            exit = True
        if exit == True: # Define that there are errors in the program
            not_good()

# Rule that states a get statement wich states that is starts with the reserved word readf followed by a left parenthesis, a string
# a comma, and ampersand, an id, a right parenthesis and finish with a semicolon
# Example: readf("%i", &x);
def p_get( p ):
    '''
    get :     READF LPAREN gets COMMA AMPERSAND ID RPAREN SEMICOLON
    '''
    p[0] = Get(p[3], p[6])
    path = get_path()[:] # Get the current path
    exist = False
    exit = False
    while(path): # Meanwhile the stack is not empty
        if tuple(path) in scope_table.table: # If the path exists in the table
            if p[6] in scope_table.table[tuple(path)]: # if the variable we are trying to access exists in that scope
                temp = scope_table.table[tuple(path)][p[6]] # Verify that the get ("%i", "%s", "%d") corresponds to the variable type
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
                break # Get out of the loop
        path.pop() # If the variable was not found in that scope try on the parent scope
    if exist == False: # If the variable was not found in any scope throw error
        print('ERROR: Variable "' + str(p[6]) + '" was not declared')
        exit = True
    if exit == True: # Define that there are errors in the program
        not_good()

# Rule that defines the different types of get in the readf command ("%i", "%s", "%d")
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

# Rule that defines a new scope and adds that scope to the current stack of scopes
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
    if not p: # Critical error
        print("Syntax error at EOF")
    else :
        print("Syntax error at line {0}" .format(p.lineno))
    # Reset everything to start again
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
