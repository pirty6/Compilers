from ply import lex
import ply.yacc as yacc


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
    def __init__(self, type, children=None, leaf=None):
        self.type = type
        if children:
            self.children = children
        else:
            self.children = [ ]
        self.leaf = leaf

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.type)
        if self.leaf:
            ret += " => " + self.leaf + "\n"
        else:
            ret += "\n"

        for child in self.children:
            ret += child.__str__(level+1)
        return ret

class ErrorNode(Node):
    pass

class Start(Node):
    def __init__(self, Function, pos, constants = None):
        self.Function = Function
        self.pos = pos
        self.constants = constants

class Type(Node):
    def __init__(self, value):
        self.value = value

class Integer(Type):
    pass

class String(Type):
    pass

class Boolean(Type):
    pass

class ID(Node):
    def __init__(self, id, pos):
        self.id = id
        self.pos = pos

class Variable(Node):
    def __init__(self, type, inits, pos):
        self.type = type
        self.inits = inits
        self.pos = pos

class InitList(Node):
    def __init__(self, inits):
        self.inits = inits

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
        self.constants = constants

class Constant(Node):
    def __init__(self, inits, pos):
        self.inits = inits
        self.pos = pos

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
    p[0] = Start(p[1], p.lineno)
    print("Successfully Parsed")
    pass

def p_start_constants( p ):
    '''
    start :  constants function
    '''
    p[0] = Start(p[2], p.lineno, p[1])
    print("Successfully Parsed")
    pass


# Rule that defines consonants and variables before and after the main function, where the main can have parameters
# and inside the main an expression
def p_function( p ):
    'function : VOID MAIN LPAREN params RPAREN LBRACE expressions RBRACE'
    p[0] = Function(p[4], p[7])

def p_empty_function( p ):
    'function : VOID MAIN LPAREN params RPAREN LBRACE RBRACE'
    p[0] = Function(p[4], [])

# Rule that defines the parameters that are passed to the main function, they can be empty or string[] args
# where args can be any name
def p_params( p ):
    '''
    params :  STR LSQUARE RSQUARE ID
    '''
    p[0] = Args(p[1], p[4])

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

# Rule that defines the while loop, inside the while loop it is possible to have multiple expressions
def p_while( p ):
    '''
    while : WHILE LPAREN statement RPAREN LBRACE expressions RBRACE
    '''
    p[0] = While(p[1], p[2], p[6])

# Rule that defines the if statement, this statment can have an else
def p_if( p ):
    '''
    if :   IF LPAREN statement RPAREN LBRACE expressions RBRACE
    '''
    p[0] = If(p[3], p[6])

def p_if_else( p ):
    '''
    if :  IF LPAREN statement RPAREN LBRACE expressions RBRACE ELSE LBRACE expressions RBRACE
    '''
    p[0] = If(p[3], p[6], p[10])


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
    variable :    var_type inits SEMICOLON
    '''
    p[0] = Variable(p[1], p[2], p.lineno)

def p_inits( p ):
    '''
    inits : inits COMMA init
    '''
    p[0] = InitList(p[1].inits + [p[3]])

def p_inits_single( p ):
    '''
    inits : init
    '''
    p[0] = InitList([p[1]])

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
def p_type_integer( p ):
    '''
    type : NUMBER
    '''
    p[0] = Integer(p[1])

def p_type_string( p ):
    '''
    type : STRING
    '''
    p[0] = String(p[1])

def p_type_boolean( p ):
    '''
    type : boolean
    '''
    p[0] = Boolean(p[1])

def p_type_id( p ):
    '''
    type : ID
    '''
    p[0] = ID(p[1], p.lineno)

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
    constant :    ENUM inits SEMICOLON
    '''
    p[0] = Constant(p[2], p.lineno)


# Rule that states that a print statment starts with the reserved word writeln then a left parenthesis then a different type of value
# followed by a right parenthesis and finish with a semicolon
# The types of possible values can be a number, a string, a boolean value or a variable (id)
# Example: writeln(x);
def p_print( p ):
    '''
    print :   WRITELN LPAREN type RPAREN SEMICOLON
    '''
    p[0] = p[3]

# Rule that states a get statement wich states that is starts with the reserved word readf followed by a left parenthesis, a string
# a comma, and ampersand, an id, a right parenthesis and finish with a semicolon
# Example: readf("%i", &x);
def p_get( p ):
    '''
    get :     READF LPAREN gets COMMA AMPERSAND ID RPAREN SEMICOLON
    '''
    p[0] = Get(p[3], p[6])

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


def handle_error(self, where, p):
    print("Syntax error in %s at line %d, column %d, at token LexToken(%s, '%s')" %\
      (where, p.lineno, self.scanner.find_tok_column(p), p.type, p.value))

# Error handler for when it passed the lexer but failed at the grammatic rules
def p_error( p ):
    if not p:
        print("Syntax error at EOF")


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
