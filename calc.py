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
    'false'     : 'FALSE',
    'if'        : 'IF',
    'int'       : 'INT',
    'main'      : 'MAIN',
    'readf'     : 'READF',
    'string'    : 'STR',
    'true'      : 'TRUE',
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
]

tokens += reserved.values()


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
t_AMPERSAND     = r'\&'


# -------------------------------------------------------
#                   COMPLEX TOKENS
# -------------------------------------------------------

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if reserved.has_key(t.value):
        t.type = reserved[t.value]
    return t

def t_NUMBER( t ) :
    r'[+-]?\d+'
    t.value = int( t.value )
    return t

def t_STRING(t):
    r'"[^\n]*?(?<!\\)"'
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


def p_start( p ):
    'start : function'
    print("Successfully Parsed")
    p[0] = p[1]

def p_function( p ):
    'function : constants VOID MAIN LPAREN RPAREN LBRACE expressions RBRACE constants'
    pass


def p_expressions( p ):
    '''
    expressions :     expressions expression
                    | expression
    '''
    pass

def p_expression( p ):
    '''
    expression :   variable
                 | while
                 | if
                 | assigned
                 | print
                 | get
                 | empty
    '''
    pass

def p_while( p ):
    '''
    while : WHILE LPAREN statement RPAREN LBRACE expressions RBRACE
    '''
    pass

def p_if( p ):
    '''
    if :   IF LPAREN statement RPAREN LBRACE expressions RBRACE
         | IF LPAREN statement RPAREN LBRACE expressions RBRACE ELSE LBRACE expression RBRACE
    '''
    pass

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
                | ID EQ boolean
                | ID NOT_EQ boolean
                | boolean EQ ID
                | boolean NOT_EQ ID
    '''
    pass

def p_variable( p ):
    '''
    variable :   INT ID SEMICOLON
               | INT ID ASSIGN NUMBER SEMICOLON
               | STR ID ASSIGN STRING SEMICOLON
               | STR ID SEMICOLON
               | BOOL ID SEMICOLON
               | BOOL ID ASSIGN boolean SEMICOLON
    '''
    pass

def p_boolean( p ):
    '''
    boolean :   TRUE
              | FALSE
    '''
    pass

def p_constants( p ):
    '''
    constants :   constants constant
                | constants variable
                | constant
                | variable
    '''
    pass

def p_constant( p ):
    '''
    constant :    ENUM ID ASSIGN NUMBER SEMICOLON
                | ENUM ID ASSIGN STRING SEMICOLON
                | ENUM ID ASSIGN boolean SEMICOLON
                | ENUM ID SEMICOLON
                | empty
    '''
    pass


def p_print( p ):
    '''
    print :   WRITELN LPAREN ID RPAREN SEMICOLON
            | WRITELN LPAREN STRING RPAREN SEMICOLON
            | WRITELN LPAREN NUMBER RPAREN SEMICOLON
            | WRITELN LPAREN boolean RPAREN SEMICOLON
    '''
    pass

def p_get( p ):
    '''
    get :     READF LPAREN STRING COMMA AMPERSAND ID RPAREN SEMICOLON
    '''
    pass


def p_assigned( p ):
    '''
    assigned :    ID ASSIGN NUMBER SEMICOLON
                | ID ASSIGN STRING SEMICOLON
                | ID ASSIGN boolean SEMICOLON
    '''
    pass

def p_empty( p ):
    'empty :'
    pass

def p_error( p ):
    print("ERROR: Syntax error in input!")
    pass

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


# -------------------------------------------------------
#                       PASSING TESTS
# -------------------------------------------------------

if __name__ == "__main__":
    import sys

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

    print("Test 13: Cadena en un lugar no permitido")
    f = open('./Tests/Test13.d', 'r')
    data = f.read()
    f.close()
    process(data)
