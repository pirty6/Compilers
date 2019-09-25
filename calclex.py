import ply.lex as lex


# -------------------------------------------------------
#                   LIST OF TOKENS
# -------------------------------------------------------

# List of token names
tokens = [
    'NUMBER',
    'STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
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
]

# List of reserved words
reserved = {
    'while' : 'WHILE',
    'else'  : 'ELSE',
    'if'    : 'IF',
    'auto'  : 'AUTO',
    'extrn' : 'EXTRN',
    'return': 'RETURN',
}

tokens += reserved.values()

# -------------------------------------------------------
#                   SIMPLE TOKENS
# -------------------------------------------------------

# Regular expression rules
t_PLUS          = r'\+'
t_MINUS         = r'-'
t_TIMES         = r'\*'
t_DIVIDE        = r'/'
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

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[A-Za-z_][\w]*'
    if reserved.has_key(t.value):
        t.type = reserved[t.value]
    return t

def t_STRING(t):
    r"'[^\n]*?(?<!\\)'"
    temp_str = t.value.replace(r'\\', '')
    return t

# Rule that keeps track of line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# -------------------------------------------------------
#                   IGNORED TOKENS
# -------------------------------------------------------

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

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

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer


# Give the lexer some input
#Test

def process(data):
    lexer = lex.lex()
    lexer.input(data)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)



if __name__ == "__main__":
    f = open('helper.c', "r")
    data = f.read()
    f.close()
    process(data)
