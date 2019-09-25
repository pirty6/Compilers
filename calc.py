from ply import lex
import ply.yacc as yacc
import decimal


# -------------------------------------------------------
#                   LIST OF TOKENS
# -------------------------------------------------------

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
    r'(true)'
    t.value = True
    return t

def t_FALSE(t):
    r'(false)'
    t.value = False
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if reserved.has_key(t.value):
        t.type = reserved[t.value]
    return t

def t_NUMBER( t ) :
    r'[+-]?\d+'
    try:
        t.value = int( t.value )
    except ValueError:
        print("Value too long ", t.value)
        t.value = 0
    return t

def t_STRING(t):
    r'"[^\n]*?(?<!\\)"'
    t.value = t.value[1:-1]
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
  print("Illegal character '{0}' at line {1}" .format(t.value[0], t.lineno))
  t.lexer.skip( 1 )

# -------------------------------------------------------
#                   RULES
# -------------------------------------------------------


def p_start( p ):
    'start : function'
    print("Successfully Parsed")

def p_function( p ):
    'function : constants VOID MAIN LPAREN params RPAREN LBRACE expressions RBRACE constants'

def p_params( p ):
    '''
    params :  STR LSQUARE RSQUARE ID
            | empty
    '''

def p_expressions( p ):
    '''
    expressions :     expressions expression
                    | expression
    '''
    pass

def p_expression( p ):
    '''
    expression :   constants
                 | while
                 | if
                 | ID assigned SEMICOLON
                 | print
                 | get
                 | empty
    '''


def p_while( p ):
    '''
    while : WHILE LPAREN statement RPAREN LBRACE expressions RBRACE
    '''

def p_if( p ):
    '''
    if :   IF LPAREN statement RPAREN LBRACE expressions RBRACE
         | IF LPAREN statement RPAREN LBRACE expressions RBRACE ELSE LBRACE expressions RBRACE
    '''

def p_statement( p ):
    '''
    statement :   type logic_op type
    '''

def p_logic_op( p ):
    '''
    logic_op :    EQ
                | NOT_EQ
                | GREATER
                | GREATER_EQ
                | LESS
                | LESS_EQ
    '''

def p_variable( p ):
    '''
    variable :   var_type ID assigned SEMICOLON
    '''

def p_var_type( p ):
    '''
    var_type :    INT
                | STR
                | BOOL
    '''

def p_assigned( p ):
    '''
    assigned :    ASSIGN type
                | empty
    '''

def p_type( p ):
    '''
    type :    NUMBER
            | STRING
            | boolean
            | ID
    '''

def p_boolean( p ):
    '''
    boolean :   TRUE
              | FALSE
    '''

def p_constants( p ):
    '''
    constants :   constants constant
                | constants variable
                | constant
                | variable
    '''

def p_constant( p ):
    '''
    constant :    ENUM ID ASSIGN NUMBER SEMICOLON
                | ENUM ID ASSIGN STRING SEMICOLON
                | ENUM ID ASSIGN boolean SEMICOLON
                | ENUM ID SEMICOLON
                | empty
    '''


def p_print( p ):
    '''
    print :   WRITELN LPAREN ID RPAREN SEMICOLON
            | WRITELN LPAREN STRING RPAREN SEMICOLON
            | WRITELN LPAREN NUMBER RPAREN SEMICOLON
            | WRITELN LPAREN boolean RPAREN SEMICOLON
    '''

def p_get( p ):
    '''
    get :     READF LPAREN STRING COMMA AMPERSAND ID RPAREN SEMICOLON
    '''

def p_empty( p ):
    'empty :'

def p_error( p ):
    print("Syntax error at line {0}" .format(p.lineno))

def process(data):
    lexer = lex.lex()
    lexer.input(data)
    #while True:
    #    tok = lexer.token()
    #    if not tok:
    #        break      # No more input
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
