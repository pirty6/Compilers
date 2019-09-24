from ply import lex
import ply.yacc as yacc
import decimal


# -------------------------------------------------------
#                   LIST OF TOKENS
# -------------------------------------------------------


tokens = (
    'LPAREN',
    'RPAREN',
    'NUMBER',
    'ID',
    'COMMA',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'ASSIGN',
    'GREATER',
    'LESS',
    'EQ',
    'NOT_EQ',
    'GREATER_EQ',
    'LESS_EQ',
    'MAIN',
    'AUTO',
    'EXTRN',
    'STRING',
    'WHILE',
    'IF',
    'ELSE',
)

reserved = {
    'while' : 'WHILE',
    'if'    : 'IF',
    'else'  : 'ELSE',
    'auto'  : 'AUTO',
    'extrn' : 'EXTRN',
    'main'  : 'MAIN',
}


# -------------------------------------------------------
#                   SIMPLE TOKENS
# -------------------------------------------------------
t_ignore = ' \t'

# Regular expression rules

t_LPAREN        = r'\('
t_RPAREN        = r'\)'
t_LBRACE        = r'\{'
t_RBRACE        = r'\}'
t_SEMICOLON     = r'\;'
t_COMMA         = r'\,'
t_ASSIGN        = r'='
t_GREATER       = r'>'
t_LESS          = r'<'
t_EQ            = r'=='
t_NOT_EQ        = r'!='
t_GREATER_EQ    = r'>='
t_LESS_EQ       = r'<='

# -------------------------------------------------------
#                   COMPLEX TOKENS
# -------------------------------------------------------

def t_NUMBER( t ) :
    r'[+-]?([0-9]*[.])?[0-9]+'
    t.value = decimal.Decimal( t.value )
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if reserved.has_key(t.value):
        t.type = reserved[t.value]
    return t

def t_STRING(t):
    r"'[^\n]*?(?<!\\)'"
    temp_str = t.value.replace(r'\\', '')
    return t

def t_newline( t ):
  r'\n+'
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

def t_error( t ):
  print("Invalid Token:",t.value[0])
  t.lexer.skip( 1 )


# -------------------------------------------------------
#                   RULES
# -------------------------------------------------------


def p_function( p ):
    'function : MAIN LPAREN RPAREN LBRACE expression RBRACE'

def p_expression( p ):
    '''
    expression :   variable
                 | expression expression
                 | while
                 | if
                 | assigned
                 | EPSILON
    '''

def p_while( p ):
    '''
    while : WHILE LPAREN statement RPAREN LBRACE expression RBRACE
    '''

def p_if( p ):
    '''
    if :   IF LPAREN statement RPAREN LBRACE expression RBRACE
         | IF LPAREN statement RPAREN LBRACE expression RBRACE ELSE LBRACE expression RBRACE
    '''

def p_statement( p ):
    '''
    statement :   ID EQ ID
                | ID NOT_EQ ID
                | ID GREATER ID
                | ID GREATER_EQ ID
                | ID LESS ID
                | ID LESS_EQ ID
                | NUMBER EQ ID
                | NUMBER NOT_EQ ID
                | NUMBER GREATER ID
                | NUMBER GREATER_EQ ID
                | NUMBER LESS ID
                | NUMBER LESS_EQ ID
                | ID EQ NUMBER
                | ID NOT_EQ NUMBER
                | ID GREATER NUMBER
                | ID GREATER_EQ NUMBER
                | ID LESS NUMBER
                | ID LESS_EQ NUMBER
    '''

def p_variable( p ):
    '''
    variable :   AUTO ID SEMICOLON
               | AUTO ID ASSIGN NUMBER SEMICOLON
               | AUTO ID ASSIGN STRING SEMICOLON
    '''

def p_assigned( p ):
    '''
    assigned :    ID ASSIGN NUMBER SEMICOLON
                | ID ASSIGN STRING SEMICOLON
    '''


def p_error( p ):
    print("ERROR: Syntax error in input!")


def process(data):
    lex.lex()
    yacc.yacc()
    yacc.parse(data)


# -------------------------------------------------------
#                       PASSING TESTS
# -------------------------------------------------------

if __name__ == "__main__":
    import sys

    # Test1: Un programa sencillo con un comentario de una palabra
    print("Test 1: Comentario de una palabra")
    f = open('./Tests/Test1.b', 'r')
    data = f.read()
    f.close()
    process(data)

    #Test2: Un programa sencillo con un comentario de una palabra

    # Test3: Un programa sencillo con la definicion de una variable.
    print("Test 3: Variable definition")
    f = open('./Tests/Test3.b', 'r')
    data = f.read()
    f.close()
    process(data)

    # Test4:


    # Test5: Un programa sencillo con cadenas.
    print("Test 5: Strings")
    f = open('./Tests/Test5.b', 'r')
    data = f.read()
    f.close()
    process(data)

    # Test6: Un programa sencillo con variables de todos los tipos de datos.
    print("Test 6: Different types of variables")
    f = open('./Tests/Test6.b', 'r')
    data = f.read()
    f.close()
    process(data)

    # Test7: Un programa sencillo con un ciclo y una condicional.
    print("Test 7: Cycle and Conditional")
    f = open('./Tests/Test7.b', 'r')
    data = f.read()
    f.close()
    process(data)

    # Test8: Un programa sencillo usando las instrucciones de entrada y salida.

    # Test9: Un programa sencillo con todas las instrucciones que has definido.
    #print("Test 9: All instructions")
    #f = open('./Tests/Test9.b', 'r')
    #data = f.read()
    #f.close()
    #process(data)

# -------------------------------------------------------
#                       FAILING TESTS
# -------------------------------------------------------
    print("Invalid tests")
    print("Test 10: Variable en el lugar incorrecto")
    f = open('./Tests/Test10.b', 'r')
    data = f.read()
    f.close()
    process(data)

    print("Test 11: Varibale en el orden incorrecto.")
    f = open('./Tests/Test11.b', 'r')
    data = f.read()
    f.close()
    process(data)

    print("Test 12: Cadena en un lugar no permitido")
    #f = open('./Test')
