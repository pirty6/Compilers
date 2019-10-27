
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSAND ASSIGN BOOL COMMA ELSE ENUM EQ FALSE GET_BOOL GET_INT GET_STRING GREATER GREATER_EQ ID IF INT LBRACE LESS LESS_EQ LPAREN LSQUARE NOT_EQ NUMBER RBRACE READF RPAREN RSQUARE SEMICOLON STR STRING TRUE VOID WHILE WRITELN\n    start : exprs\n    \n    exprs : exprs expr\n    \n    exprs : expr\n    \n    expr :   constants\n            | functions\n    \n    start :  constants functions\n    \n    functions :    functions function\n    \n    functions : function\n    function : new_scope VOID ID LPAREN params RPAREN LBRACE expressions RBRACEfunction :  new_scope VOID ID LPAREN params RPAREN LBRACE RBRACE\n    params :  STR LSQUARE RSQUARE ID\n    \n    params : empty\n    \n    expressions :     expressions expression\n    \n    expressions : expression\n    \n    expression :   constants\n                 | while\n                 | if\n                 | assigned\n                 | print\n                 | get\n                 | call\n    \n    call : ID LPAREN RPAREN SEMICOLON\n    \n    assigned : ID ASSIGN type SEMICOLON\n    \n    while : WHILE LPAREN statement RPAREN LBRACE new_scope expressions RBRACE\n    \n    if :   IF LPAREN statement RPAREN LBRACE new_scope expressions RBRACE\n    \n    if :  IF LPAREN statement RPAREN LBRACE new_scope expressions RBRACE ELSE LBRACE new_scope expressions  RBRACE\n    \n    statement :   type logic_op type\n    \n    logic_op :    EQ\n                | NOT_EQ\n                | GREATER\n                | GREATER_EQ\n                | LESS\n                | LESS_EQ\n    \n    variable :    var_type init SEMICOLON\n    \n    init :  ID ASSIGN type\n    \n    init : ID\n    \n    var_type :    INT\n                | STR\n                | BOOL\n    \n    type :    NUMBER\n            | STRING\n            | boolean\n            | ID\n    \n    boolean :   TRUE\n              | FALSE\n    \n    constants :   constants constant\n                | constants variable\n    \n    constants :    constant\n                |  variable\n    \n    constant :    ENUM init SEMICOLON\n    \n    print :   WRITELN LPAREN type RPAREN SEMICOLON\n    \n    get :     READF LPAREN gets COMMA AMPERSAND ID RPAREN SEMICOLON\n    \n    gets :    GET_INT\n            | GET_STRING\n            | GET_BOOL\n    empty :new_scope : empty'
    
_lr_action_items = {'LSQUARE':([38,],[41,]),'LESS_EQ':([30,31,32,33,34,36,70,],[-45,-41,-44,-40,-42,-43,80,]),'LPAREN':([28,47,54,55,57,58,],[37,61,64,66,67,68,]),'LESS':([30,31,32,33,34,36,70,],[-45,-41,-44,-40,-42,-43,83,]),'VOID':([0,1,4,5,7,8,10,11,13,14,18,21,22,23,24,25,27,29,52,62,],[-56,-48,-5,19,-57,-8,-49,-4,-3,-56,-7,-46,-56,-47,-4,-2,-34,-50,-10,-9,]),'NUMBER':([26,61,64,65,67,80,81,82,83,84,85,86,],[33,33,33,33,33,-33,33,-30,-32,-28,-31,-29,]),'GREATER_EQ':([30,31,32,33,34,36,70,],[-45,-41,-44,-40,-42,-43,85,]),'WHILE':([1,7,10,21,23,27,29,44,46,48,49,50,51,53,56,59,60,63,88,89,92,94,95,97,98,100,101,103,104,105,107,108,109,110,],[-48,-57,-49,-46,-47,-34,-50,47,-18,47,-17,-19,-21,-20,-15,-16,-14,-13,-23,-22,-56,-51,-56,47,47,47,47,-24,-25,-52,-56,47,47,-26,]),'TRUE':([26,61,64,65,67,80,81,82,83,84,85,86,],[32,32,32,32,32,-33,32,-30,-32,-28,-31,-29,]),'STRING':([26,61,64,65,67,80,81,82,83,84,85,86,],[31,31,31,31,31,-33,31,-30,-32,-28,-31,-29,]),'RSQUARE':([41,],[43,]),'RPAREN':([30,31,32,33,34,36,37,39,40,45,66,69,71,74,93,99,],[-45,-41,-44,-40,-42,-43,-56,42,-12,-11,73,79,87,90,-27,102,]),'SEMICOLON':([16,17,20,30,31,32,33,34,35,36,72,73,87,102,],[-36,27,29,-45,-41,-44,-40,-42,-35,-43,88,89,94,105,]),'GET_INT':([68,],[77,]),'COMMA':([75,76,77,78,],[-55,-54,-53,91,]),'NOT_EQ':([30,31,32,33,34,36,70,],[-45,-41,-44,-40,-42,-43,86,]),'ASSIGN':([16,55,],[26,65,]),'$end':([1,4,6,8,10,11,13,14,18,21,22,23,24,25,27,29,52,62,],[-48,-5,0,-8,-49,-4,-3,-1,-7,-46,-6,-47,-4,-2,-34,-50,-10,-9,]),'RBRACE':([1,10,21,23,27,29,44,46,48,49,50,51,53,56,59,60,63,88,89,94,100,101,103,104,105,109,110,],[-48,-49,-46,-47,-34,-50,52,-18,62,-17,-19,-21,-20,-15,-16,-14,-13,-23,-22,-51,103,104,-24,-25,-52,110,-26,]),'ENUM':([0,1,4,7,8,10,11,13,14,18,21,23,24,25,27,29,44,46,48,49,50,51,52,53,56,59,60,62,63,88,89,92,94,95,97,98,100,101,103,104,105,107,108,109,110,],[9,-48,-5,-57,-8,-49,9,-3,9,-7,-46,-47,9,-2,-34,-50,9,-18,9,-17,-19,-21,-10,-20,9,-16,-14,-9,-13,-23,-22,-56,-51,-56,9,9,9,9,-24,-25,-52,-56,9,9,-26,]),'ELSE':([104,],[106,]),'WRITELN':([1,7,10,21,23,27,29,44,46,48,49,50,51,53,56,59,60,63,88,89,92,94,95,97,98,100,101,103,104,105,107,108,109,110,],[-48,-57,-49,-46,-47,-34,-50,54,-18,54,-17,-19,-21,-20,-15,-16,-14,-13,-23,-22,-56,-51,-56,54,54,54,54,-24,-25,-52,-56,54,54,-26,]),'AMPERSAND':([91,],[96,]),'STR':([0,1,4,7,8,10,11,13,14,18,21,23,24,25,27,29,37,44,46,48,49,50,51,52,53,56,59,60,62,63,88,89,92,94,95,97,98,100,101,103,104,105,107,108,109,110,],[2,-48,-5,-57,-8,-49,2,-3,2,-7,-46,-47,2,-2,-34,-50,38,2,-18,2,-17,-19,-21,-10,-20,2,-16,-14,-9,-13,-23,-22,-56,-51,-56,2,2,2,2,-24,-25,-52,-56,2,2,-26,]),'EQ':([30,31,32,33,34,36,70,],[-45,-41,-44,-40,-42,-43,84,]),'ID':([1,2,3,7,9,10,12,15,19,21,23,26,27,29,43,44,46,48,49,50,51,53,56,59,60,61,63,64,65,67,80,81,82,83,84,85,86,88,89,92,94,95,96,97,98,100,101,103,104,105,107,108,109,110,],[-48,-38,16,-57,16,-49,-37,-39,28,-46,-47,36,-34,-50,45,55,-18,55,-17,-19,-21,-20,-15,-16,-14,36,-13,36,36,36,-33,36,-30,-32,-28,-31,-29,-23,-22,-56,-51,-56,99,55,55,55,55,-24,-25,-52,-56,55,55,-26,]),'IF':([1,7,10,21,23,27,29,44,46,48,49,50,51,53,56,59,60,63,88,89,92,94,95,97,98,100,101,103,104,105,107,108,109,110,],[-48,-57,-49,-46,-47,-34,-50,57,-18,57,-17,-19,-21,-20,-15,-16,-14,-13,-23,-22,-56,-51,-56,57,57,57,57,-24,-25,-52,-56,57,57,-26,]),'LBRACE':([42,79,90,106,],[44,92,95,107,]),'FALSE':([26,61,64,65,67,80,81,82,83,84,85,86,],[30,30,30,30,30,-33,30,-30,-32,-28,-31,-29,]),'GREATER':([30,31,32,33,34,36,70,],[-45,-41,-44,-40,-42,-43,82,]),'READF':([1,7,10,21,23,27,29,44,46,48,49,50,51,53,56,59,60,63,88,89,92,94,95,97,98,100,101,103,104,105,107,108,109,110,],[-48,-57,-49,-46,-47,-34,-50,58,-18,58,-17,-19,-21,-20,-15,-16,-14,-13,-23,-22,-56,-51,-56,58,58,58,58,-24,-25,-52,-56,58,58,-26,]),'INT':([0,1,4,7,8,10,11,13,14,18,21,23,24,25,27,29,44,46,48,49,50,51,52,53,56,59,60,62,63,88,89,92,94,95,97,98,100,101,103,104,105,107,108,109,110,],[12,-48,-5,-57,-8,-49,12,-3,12,-7,-46,-47,12,-2,-34,-50,12,-18,12,-17,-19,-21,-10,-20,12,-16,-14,-9,-13,-23,-22,-56,-51,-56,12,12,12,12,-24,-25,-52,-56,12,12,-26,]),'GET_STRING':([68,],[76,]),'BOOL':([0,1,4,7,8,10,11,13,14,18,21,23,24,25,27,29,44,46,48,49,50,51,52,53,56,59,60,62,63,88,89,92,94,95,97,98,100,101,103,104,105,107,108,109,110,],[15,-48,-5,-57,-8,-49,15,-3,15,-7,-46,-47,15,-2,-34,-50,15,-18,15,-17,-19,-21,-10,-20,15,-16,-14,-9,-13,-23,-22,-56,-51,-56,15,15,15,15,-24,-25,-52,-56,15,15,-26,]),'GET_BOOL':([68,],[75,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'constant':([0,11,14,24,44,48,56,97,98,100,101,108,109,],[1,21,1,21,1,1,21,1,1,1,1,1,1,]),'var_type':([0,11,14,24,44,48,56,97,98,100,101,108,109,],[3,3,3,3,3,3,3,3,3,3,3,3,3,]),'assigned':([44,48,97,98,100,101,108,109,],[46,46,46,46,46,46,46,46,]),'boolean':([26,61,64,65,67,81,],[34,34,34,34,34,34,]),'expressions':([44,97,98,108,],[48,100,101,109,]),'if':([44,48,97,98,100,101,108,109,],[49,49,49,49,49,49,49,49,]),'functions':([0,11,14,],[4,22,4,]),'new_scope':([0,4,11,14,22,92,95,107,],[5,5,5,5,5,97,98,108,]),'start':([0,],[6,]),'init':([3,9,],[17,20,]),'params':([37,],[39,]),'statement':([61,67,],[69,74,]),'print':([44,48,97,98,100,101,108,109,],[50,50,50,50,50,50,50,50,]),'call':([44,48,97,98,100,101,108,109,],[51,51,51,51,51,51,51,51,]),'gets':([68,],[78,]),'type':([26,61,64,65,67,81,],[35,70,71,72,70,93,]),'empty':([0,4,11,14,22,37,92,95,107,],[7,7,7,7,7,40,7,7,7,]),'function':([0,4,11,14,22,],[8,18,8,8,18,]),'get':([44,48,97,98,100,101,108,109,],[53,53,53,53,53,53,53,53,]),'variable':([0,11,14,24,44,48,56,97,98,100,101,108,109,],[10,23,10,23,10,10,23,10,10,10,10,10,10,]),'constants':([0,14,44,48,97,98,100,101,108,109,],[11,24,56,56,56,56,56,56,56,56,]),'logic_op':([70,],[81,]),'expr':([0,14,],[13,25,]),'exprs':([0,],[14,]),'while':([44,48,97,98,100,101,108,109,],[59,59,59,59,59,59,59,59,]),'expression':([44,48,97,98,100,101,108,109,],[60,63,60,60,63,63,60,63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> exprs','start',1,'p_start','calc.py',488),
  ('exprs -> exprs expr','exprs',2,'p_list_exprs','calc.py',500),
  ('exprs -> expr','exprs',1,'p_exprs','calc.py',507),
  ('expr -> constants','expr',1,'p_expr','calc.py',513),
  ('expr -> functions','expr',1,'p_expr','calc.py',514),
  ('start -> constants functions','start',2,'p_start_constants','calc.py',521),
  ('functions -> functions function','functions',2,'p_list_functions','calc.py',533),
  ('functions -> function','functions',1,'p_functions','calc.py',539),
  ('function -> new_scope VOID ID LPAREN params RPAREN LBRACE expressions RBRACE','function',9,'p_function','calc.py',547),
  ('function -> new_scope VOID ID LPAREN params RPAREN LBRACE RBRACE','function',8,'p_empty_function','calc.py',559),
  ('params -> STR LSQUARE RSQUARE ID','params',4,'p_params','calc.py',574),
  ('params -> empty','params',1,'p_empty_params','calc.py',588),
  ('expressions -> expressions expression','expressions',2,'p_list_expressions','calc.py',598),
  ('expressions -> expression','expressions',1,'p_expressions','calc.py',605),
  ('expression -> constants','expression',1,'p_expression','calc.py',613),
  ('expression -> while','expression',1,'p_expression','calc.py',614),
  ('expression -> if','expression',1,'p_expression','calc.py',615),
  ('expression -> assigned','expression',1,'p_expression','calc.py',616),
  ('expression -> print','expression',1,'p_expression','calc.py',617),
  ('expression -> get','expression',1,'p_expression','calc.py',618),
  ('expression -> call','expression',1,'p_expression','calc.py',619),
  ('call -> ID LPAREN RPAREN SEMICOLON','call',4,'p_call','calc.py',627),
  ('assigned -> ID ASSIGN type SEMICOLON','assigned',4,'p_assigned','calc.py',648),
  ('while -> WHILE LPAREN statement RPAREN LBRACE new_scope expressions RBRACE','while',8,'p_while','calc.py',687),
  ('if -> IF LPAREN statement RPAREN LBRACE new_scope expressions RBRACE','if',8,'p_if','calc.py',697),
  ('if -> IF LPAREN statement RPAREN LBRACE new_scope expressions RBRACE ELSE LBRACE new_scope expressions RBRACE','if',13,'p_if_else','calc.py',707),
  ('statement -> type logic_op type','statement',3,'p_statement','calc.py',721),
  ('logic_op -> EQ','logic_op',1,'p_logic_op','calc.py',853),
  ('logic_op -> NOT_EQ','logic_op',1,'p_logic_op','calc.py',854),
  ('logic_op -> GREATER','logic_op',1,'p_logic_op','calc.py',855),
  ('logic_op -> GREATER_EQ','logic_op',1,'p_logic_op','calc.py',856),
  ('logic_op -> LESS','logic_op',1,'p_logic_op','calc.py',857),
  ('logic_op -> LESS_EQ','logic_op',1,'p_logic_op','calc.py',858),
  ('variable -> var_type init SEMICOLON','variable',3,'p_variable','calc.py',868),
  ('init -> ID ASSIGN type','init',3,'p_init_value','calc.py',881),
  ('init -> ID','init',1,'p_init','calc.py',888),
  ('var_type -> INT','var_type',1,'p_var_type','calc.py',895),
  ('var_type -> STR','var_type',1,'p_var_type','calc.py',896),
  ('var_type -> BOOL','var_type',1,'p_var_type','calc.py',897),
  ('type -> NUMBER','type',1,'p_type','calc.py',906),
  ('type -> STRING','type',1,'p_type','calc.py',907),
  ('type -> boolean','type',1,'p_type','calc.py',908),
  ('type -> ID','type',1,'p_type','calc.py',909),
  ('boolean -> TRUE','boolean',1,'p_boolean','calc.py',917),
  ('boolean -> FALSE','boolean',1,'p_boolean','calc.py',918),
  ('constants -> constants constant','constants',2,'p_list_constants','calc.py',925),
  ('constants -> constants variable','constants',2,'p_list_constants','calc.py',926),
  ('constants -> constant','constants',1,'p_constants','calc.py',936),
  ('constants -> variable','constants',1,'p_constants','calc.py',937),
  ('constant -> ENUM init SEMICOLON','constant',3,'p_constant','calc.py',948),
  ('print -> WRITELN LPAREN type RPAREN SEMICOLON','print',5,'p_print','calc.py',973),
  ('get -> READF LPAREN gets COMMA AMPERSAND ID RPAREN SEMICOLON','get',8,'p_get','calc.py',998),
  ('gets -> GET_INT','gets',1,'p_gets','calc.py',1032),
  ('gets -> GET_STRING','gets',1,'p_gets','calc.py',1033),
  ('gets -> GET_BOOL','gets',1,'p_gets','calc.py',1034),
  ('empty -> <empty>','empty',0,'p_empty','calc.py',1040),
  ('new_scope -> empty','new_scope',1,'p_new_scope','calc.py',1049),
]
