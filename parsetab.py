
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSAND ASSIGN BOOL COMMA ELSE ENUM EQ FALSE GET_BOOL GET_INT GET_STRING GREATER GREATER_EQ ID IF INT LBRACE LESS LESS_EQ LPAREN LSQUARE MAIN NOT_EQ NUMBER RBRACE READF RPAREN RSQUARE SEMICOLON STR STRING TRUE VOID WHILE WRITELN\n    start : function\n    \n    start :  constants function\n    function : new_scope VOID MAIN LPAREN params RPAREN LBRACE expressions RBRACE end_scopefunction : new_scope VOID MAIN LPAREN params RPAREN LBRACE RBRACE end_scope\n    params :  STR LSQUARE RSQUARE ID\n    \n    params : empty\n    \n    expressions :     expressions expression\n    \n    expressions : expression\n    \n    expression :   constants\n                 | while\n                 | if\n                 | assigned\n                 | print\n                 | get\n    \n    assigned : ID ASSIGN type SEMICOLON\n    \n    while : WHILE LPAREN statement RPAREN LBRACE  expressions  RBRACE\n    \n    if :   IF LPAREN statement RPAREN LBRACE expressions RBRACE\n    \n    if :  IF LPAREN statement RPAREN LBRACE  expressions RBRACE ELSE LBRACE  expressions  RBRACE\n    \n    statement :   type logic_op type\n    \n    logic_op :    EQ\n                | NOT_EQ\n                | GREATER\n                | GREATER_EQ\n                | LESS\n                | LESS_EQ\n    \n    variable :    var_type init SEMICOLON\n    \n    init :  ID ASSIGN type\n    \n    init : ID\n    \n    var_type :    INT\n                | STR\n                | BOOL\n    \n    type :    NUMBER\n            | STRING\n            | boolean\n            | ID\n    \n    boolean :   TRUE\n              | FALSE\n    \n    constants :   constants constant\n                | constants variable\n    \n    constants :    constant\n                |  variable\n    \n    constant :    ENUM init SEMICOLON\n    \n    print :   WRITELN LPAREN type RPAREN SEMICOLON\n    \n    get :     READF LPAREN gets COMMA AMPERSAND ID RPAREN SEMICOLON\n    \n    gets :    GET_INT\n            | GET_STRING\n            | GET_BOOL\n    empty :new_scope : emptyend_scope : empty'
    
_lr_action_items = {'LSQUARE':([32,],[35,]),'LESS_EQ':([24,25,26,27,28,30,64,],[-37,-33,-36,-32,-34,-35,74,]),'LPAREN':([22,41,47,50,51,],[31,54,59,61,62,]),'LESS':([24,25,26,27,28,30,64,],[-37,-33,-36,-32,-34,-35,77,]),'VOID':([0,1,4,6,9,10,17,19,21,23,],[-48,-40,15,-49,-41,-48,-38,-39,-26,-42,]),'NUMBER':([20,54,59,60,61,74,75,76,77,78,79,80,],[27,27,27,27,27,-25,27,-22,-24,-20,-23,-21,]),'GREATER_EQ':([24,25,26,27,28,30,64,],[-37,-33,-36,-32,-34,-35,79,]),'WHILE':([1,9,17,19,21,23,38,40,42,43,44,46,49,52,53,56,82,85,87,88,90,91,93,94,97,98,99,100,],[-40,-41,-38,-39,-26,-42,41,-12,41,-11,-13,-14,-9,-10,-8,-7,-15,41,-43,41,41,41,-16,-17,-44,41,41,-18,]),'TRUE':([20,54,59,60,61,74,75,76,77,78,79,80,],[26,26,26,26,26,-25,26,-22,-24,-20,-23,-21,]),'STRING':([20,54,59,60,61,74,75,76,77,78,79,80,],[25,25,25,25,25,-25,25,-22,-24,-20,-23,-21,]),'RSQUARE':([35,],[37,]),'RPAREN':([24,25,26,27,28,30,31,33,34,39,63,66,68,86,92,],[-37,-33,-36,-32,-34,-35,-48,36,-6,-5,73,81,83,-19,95,]),'SEMICOLON':([13,14,16,24,25,26,27,28,29,30,67,81,95,],[-28,21,23,-37,-33,-36,-32,-34,-27,-35,82,87,97,]),'GET_INT':([62,],[71,]),'COMMA':([69,70,71,72,],[-47,-46,-45,84,]),'NOT_EQ':([24,25,26,27,28,30,64,],[-37,-33,-36,-32,-34,-35,80,]),'ASSIGN':([13,48,],[20,60,]),'$end':([5,7,18,45,55,57,58,65,],[0,-1,-2,-48,-48,-4,-50,-3,]),'GET_BOOL':([62,],[69,]),'RBRACE':([1,9,17,19,21,23,38,40,42,43,44,46,49,52,53,56,82,87,90,91,93,94,97,99,100,],[-40,-41,-38,-39,-26,-42,45,-12,55,-11,-13,-14,-9,-10,-8,-7,-15,-43,93,94,-16,-17,-44,100,-18,]),'ENUM':([0,1,9,10,17,19,21,23,38,40,42,43,44,46,49,52,53,56,82,85,87,88,90,91,93,94,97,98,99,100,],[8,-40,-41,8,-38,-39,-26,-42,8,-12,8,-11,-13,-14,8,-10,-8,-7,-15,8,-43,8,8,8,-16,-17,-44,8,8,-18,]),'ELSE':([94,],[96,]),'WRITELN':([1,9,17,19,21,23,38,40,42,43,44,46,49,52,53,56,82,85,87,88,90,91,93,94,97,98,99,100,],[-40,-41,-38,-39,-26,-42,47,-12,47,-11,-13,-14,-9,-10,-8,-7,-15,47,-43,47,47,47,-16,-17,-44,47,47,-18,]),'AMPERSAND':([84,],[89,]),'STR':([0,1,9,10,17,19,21,23,31,38,40,42,43,44,46,49,52,53,56,82,85,87,88,90,91,93,94,97,98,99,100,],[2,-40,-41,2,-38,-39,-26,-42,32,2,-12,2,-11,-13,-14,2,-10,-8,-7,-15,2,-43,2,2,2,-16,-17,-44,2,2,-18,]),'EQ':([24,25,26,27,28,30,64,],[-37,-33,-36,-32,-34,-35,78,]),'ID':([1,2,3,8,9,11,12,17,19,20,21,23,37,38,40,42,43,44,46,49,52,53,54,56,59,60,61,74,75,76,77,78,79,80,82,85,87,88,89,90,91,93,94,97,98,99,100,],[-40,-30,13,13,-41,-29,-31,-38,-39,30,-26,-42,39,48,-12,48,-11,-13,-14,-9,-10,-8,30,-7,30,30,30,-25,30,-22,-24,-20,-23,-21,-15,48,-43,48,92,48,48,-16,-17,-44,48,48,-18,]),'IF':([1,9,17,19,21,23,38,40,42,43,44,46,49,52,53,56,82,85,87,88,90,91,93,94,97,98,99,100,],[-40,-41,-38,-39,-26,-42,50,-12,50,-11,-13,-14,-9,-10,-8,-7,-15,50,-43,50,50,50,-16,-17,-44,50,50,-18,]),'LBRACE':([36,73,83,96,],[38,85,88,98,]),'FALSE':([20,54,59,60,61,74,75,76,77,78,79,80,],[24,24,24,24,24,-25,24,-22,-24,-20,-23,-21,]),'GREATER':([24,25,26,27,28,30,64,],[-37,-33,-36,-32,-34,-35,76,]),'READF':([1,9,17,19,21,23,38,40,42,43,44,46,49,52,53,56,82,85,87,88,90,91,93,94,97,98,99,100,],[-40,-41,-38,-39,-26,-42,51,-12,51,-11,-13,-14,-9,-10,-8,-7,-15,51,-43,51,51,51,-16,-17,-44,51,51,-18,]),'INT':([0,1,9,10,17,19,21,23,38,40,42,43,44,46,49,52,53,56,82,85,87,88,90,91,93,94,97,98,99,100,],[11,-40,-41,11,-38,-39,-26,-42,11,-12,11,-11,-13,-14,11,-10,-8,-7,-15,11,-43,11,11,11,-16,-17,-44,11,11,-18,]),'GET_STRING':([62,],[70,]),'BOOL':([0,1,9,10,17,19,21,23,38,40,42,43,44,46,49,52,53,56,82,85,87,88,90,91,93,94,97,98,99,100,],[12,-40,-41,12,-38,-39,-26,-42,12,-12,12,-11,-13,-14,12,-10,-8,-7,-15,12,-43,12,12,12,-16,-17,-44,12,12,-18,]),'MAIN':([15,],[22,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'constant':([0,10,38,42,49,85,88,90,91,98,99,],[1,17,1,1,17,1,1,1,1,1,1,]),'var_type':([0,10,38,42,49,85,88,90,91,98,99,],[3,3,3,3,3,3,3,3,3,3,3,]),'assigned':([38,42,85,88,90,91,98,99,],[40,40,40,40,40,40,40,40,]),'boolean':([20,54,59,60,61,75,],[28,28,28,28,28,28,]),'expressions':([38,85,88,98,],[42,90,91,99,]),'if':([38,42,85,88,90,91,98,99,],[43,43,43,43,43,43,43,43,]),'end_scope':([45,55,],[57,65,]),'new_scope':([0,10,],[4,4,]),'start':([0,],[5,]),'init':([3,8,],[14,16,]),'params':([31,],[33,]),'statement':([54,61,],[63,68,]),'print':([38,42,85,88,90,91,98,99,],[44,44,44,44,44,44,44,44,]),'gets':([62,],[72,]),'type':([20,54,59,60,61,75,],[29,64,66,67,64,86,]),'empty':([0,10,31,45,55,],[6,6,34,58,58,]),'function':([0,10,],[7,18,]),'get':([38,42,85,88,90,91,98,99,],[46,46,46,46,46,46,46,46,]),'variable':([0,10,38,42,49,85,88,90,91,98,99,],[9,19,9,9,19,9,9,9,9,9,9,]),'constants':([0,38,42,85,88,90,91,98,99,],[10,49,49,49,49,49,49,49,49,]),'logic_op':([64,],[75,]),'while':([38,42,85,88,90,91,98,99,],[52,52,52,52,52,52,52,52,]),'expression':([38,42,85,88,90,91,98,99,],[53,56,53,53,56,56,53,56,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> function','start',1,'p_start','calc.py',291),
  ('start -> constants function','start',2,'p_start_constants','calc.py',301),
  ('function -> new_scope VOID MAIN LPAREN params RPAREN LBRACE expressions RBRACE end_scope','function',10,'p_function','calc.py',314),
  ('function -> new_scope VOID MAIN LPAREN params RPAREN LBRACE RBRACE end_scope','function',9,'p_empty_function','calc.py',318),
  ('params -> STR LSQUARE RSQUARE ID','params',4,'p_params','calc.py',325),
  ('params -> empty','params',1,'p_empty_params','calc.py',335),
  ('expressions -> expressions expression','expressions',2,'p_list_expressions','calc.py',342),
  ('expressions -> expression','expressions',1,'p_expressions','calc.py',348),
  ('expression -> constants','expression',1,'p_expression','calc.py',356),
  ('expression -> while','expression',1,'p_expression','calc.py',357),
  ('expression -> if','expression',1,'p_expression','calc.py',358),
  ('expression -> assigned','expression',1,'p_expression','calc.py',359),
  ('expression -> print','expression',1,'p_expression','calc.py',360),
  ('expression -> get','expression',1,'p_expression','calc.py',361),
  ('assigned -> ID ASSIGN type SEMICOLON','assigned',4,'p_assigned','calc.py',367),
  ('while -> WHILE LPAREN statement RPAREN LBRACE expressions RBRACE','while',7,'p_while','calc.py',374),
  ('if -> IF LPAREN statement RPAREN LBRACE expressions RBRACE','if',7,'p_if','calc.py',381),
  ('if -> IF LPAREN statement RPAREN LBRACE expressions RBRACE ELSE LBRACE expressions RBRACE','if',11,'p_if_else','calc.py',387),
  ('statement -> type logic_op type','statement',3,'p_statement','calc.py',397),
  ('logic_op -> EQ','logic_op',1,'p_logic_op','calc.py',404),
  ('logic_op -> NOT_EQ','logic_op',1,'p_logic_op','calc.py',405),
  ('logic_op -> GREATER','logic_op',1,'p_logic_op','calc.py',406),
  ('logic_op -> GREATER_EQ','logic_op',1,'p_logic_op','calc.py',407),
  ('logic_op -> LESS','logic_op',1,'p_logic_op','calc.py',408),
  ('logic_op -> LESS_EQ','logic_op',1,'p_logic_op','calc.py',409),
  ('variable -> var_type init SEMICOLON','variable',3,'p_variable','calc.py',419),
  ('init -> ID ASSIGN type','init',3,'p_init_value','calc.py',429),
  ('init -> ID','init',1,'p_init','calc.py',435),
  ('var_type -> INT','var_type',1,'p_var_type','calc.py',442),
  ('var_type -> STR','var_type',1,'p_var_type','calc.py',443),
  ('var_type -> BOOL','var_type',1,'p_var_type','calc.py',444),
  ('type -> NUMBER','type',1,'p_type','calc.py',453),
  ('type -> STRING','type',1,'p_type','calc.py',454),
  ('type -> boolean','type',1,'p_type','calc.py',455),
  ('type -> ID','type',1,'p_type','calc.py',456),
  ('boolean -> TRUE','boolean',1,'p_boolean','calc.py',463),
  ('boolean -> FALSE','boolean',1,'p_boolean','calc.py',464),
  ('constants -> constants constant','constants',2,'p_list_constants','calc.py',471),
  ('constants -> constants variable','constants',2,'p_list_constants','calc.py',472),
  ('constants -> constant','constants',1,'p_constants','calc.py',483),
  ('constants -> variable','constants',1,'p_constants','calc.py',484),
  ('constant -> ENUM init SEMICOLON','constant',3,'p_constant','calc.py',495),
  ('print -> WRITELN LPAREN type RPAREN SEMICOLON','print',5,'p_print','calc.py',510),
  ('get -> READF LPAREN gets COMMA AMPERSAND ID RPAREN SEMICOLON','get',8,'p_get','calc.py',519),
  ('gets -> GET_INT','gets',1,'p_gets','calc.py',525),
  ('gets -> GET_STRING','gets',1,'p_gets','calc.py',526),
  ('gets -> GET_BOOL','gets',1,'p_gets','calc.py',527),
  ('empty -> <empty>','empty',0,'p_empty','calc.py',533),
  ('new_scope -> empty','new_scope',1,'p_new_scope','calc.py',541),
  ('end_scope -> empty','end_scope',1,'p_end_scope','calc.py',546),
]
