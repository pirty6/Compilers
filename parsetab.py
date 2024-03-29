
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSAND ASSIGN BOOL COMMA ELSE ENUM EQ FALSE GET_BOOL GET_INT GET_STRING GREATER GREATER_EQ ID IF INT LBRACE LESS LESS_EQ LPAREN LSQUARE NOT_EQ NUMBER RBRACE READF RPAREN RSQUARE SEMICOLON STR STRING TRUE VOID WHILE WRITELN\n    start : exprs\n    \n    exprs : exprs expr\n    \n    exprs : expr\n    \n    expr :    constant\n            | function\n            | variable\n    function : new_scope VOID ID LPAREN params RPAREN LBRACE expressions RBRACEfunction :  new_scope VOID ID LPAREN params RPAREN LBRACE RBRACE\n    params :  STR LSQUARE RSQUARE ID\n    \n    params : empty\n    \n    expressions :     expressions expression\n    \n    expressions : expression\n    \n    expression :   constants\n                 | while\n                 | if\n                 | assigned\n                 | print\n                 | get\n                 | call\n    \n    call : ID LPAREN RPAREN SEMICOLON\n    \n    assigned : ID ASSIGN type SEMICOLON\n    \n    while : WHILE LPAREN statement RPAREN LBRACE new_scope expressions RBRACE\n    \n    if :   IF LPAREN statement RPAREN LBRACE new_scope expressions RBRACE\n    \n    if :  IF LPAREN statement RPAREN LBRACE new_scope expressions RBRACE ELSE LBRACE new_scope expressions  RBRACE\n    \n    statement :   type logic_op type\n    \n    logic_op :    EQ\n                | NOT_EQ\n                | GREATER\n                | GREATER_EQ\n                | LESS\n                | LESS_EQ\n    \n    variable :    var_type init SEMICOLON\n    \n    init :  ID ASSIGN type\n    \n    init : ID\n    \n    var_type :    INT\n                | STR\n                | BOOL\n    \n    type :    NUMBER\n            | STRING\n            | boolean\n            | ID\n    \n    boolean :   TRUE\n              | FALSE\n    \n    constants :   constants constant\n                | constants variable\n    \n    constants :    constant\n                |  variable\n    \n    constant :    ENUM init SEMICOLON\n    \n    print :   WRITELN LPAREN type RPAREN SEMICOLON\n    \n    get :     READF LPAREN gets COMMA AMPERSAND ID RPAREN SEMICOLON\n    \n    gets :    GET_INT\n            | GET_STRING\n            | GET_BOOL\n    empty :new_scope : empty'
    
_lr_action_items = {'LSQUARE':([31,],[34,]),'LESS_EQ':([23,24,25,26,27,29,67,],[-43,-39,-42,-38,-40,-41,77,]),'LPAREN':([21,41,48,50,52,53,],[30,56,59,61,64,65,]),'LESS':([23,24,25,26,27,29,67,],[-43,-39,-42,-38,-40,-41,80,]),'VOID':([0,1,4,6,7,9,11,12,18,20,22,46,57,],[-54,-4,16,-55,-5,-6,-3,-54,-2,-32,-48,-8,-7,]),'NUMBER':([19,56,59,60,64,77,78,79,80,81,82,83,],[26,26,26,26,26,-31,26,-28,-30,-26,-29,-27,]),'GREATER_EQ':([23,24,25,26,27,29,67,],[-43,-39,-42,-38,-40,-41,82,]),'WHILE':([6,20,22,37,39,40,42,43,44,45,47,49,51,54,55,58,62,63,85,86,89,91,92,94,95,97,98,100,101,102,104,105,106,107,],[-55,-32,-48,41,-46,-16,41,-15,-17,-19,-18,-47,-13,-14,-12,-11,-44,-45,-21,-20,-54,-49,-54,41,41,41,41,-22,-23,-50,-54,41,41,-24,]),'TRUE':([19,56,59,60,64,77,78,79,80,81,82,83,],[25,25,25,25,25,-31,25,-28,-30,-26,-29,-27,]),'RBRACE':([20,22,37,39,40,42,43,44,45,47,49,51,54,55,58,62,63,85,86,91,97,98,100,101,102,106,107,],[-32,-48,46,-46,-16,57,-15,-17,-19,-18,-47,-13,-14,-12,-11,-44,-45,-21,-20,-49,100,101,-22,-23,-50,107,-24,]),'RSQUARE':([34,],[36,]),'RPAREN':([23,24,25,26,27,29,30,32,33,38,61,66,68,71,90,96,],[-43,-39,-42,-38,-40,-41,-54,35,-10,-9,70,76,84,87,-25,99,]),'SEMICOLON':([14,15,17,23,24,25,26,27,28,29,69,70,84,99,],[-34,20,22,-43,-39,-42,-38,-40,-33,-41,85,86,91,102,]),'GET_INT':([65,],[74,]),'COMMA':([72,73,74,75,],[-53,-52,-51,88,]),'NOT_EQ':([23,24,25,26,27,29,67,],[-43,-39,-42,-38,-40,-41,83,]),'ASSIGN':([14,50,],[19,60,]),'$end':([1,5,7,9,11,12,18,20,22,46,57,],[-4,0,-5,-6,-3,-1,-2,-32,-48,-8,-7,]),'STRING':([19,56,59,60,64,77,78,79,80,81,82,83,],[24,24,24,24,24,-31,24,-28,-30,-26,-29,-27,]),'ENUM':([0,1,6,7,9,11,12,18,20,22,37,39,40,42,43,44,45,46,47,49,51,54,55,57,58,62,63,85,86,89,91,92,94,95,97,98,100,101,102,104,105,106,107,],[8,-4,-55,-5,-6,-3,8,-2,-32,-48,8,-46,-16,8,-15,-17,-19,-8,-18,-47,8,-14,-12,-7,-11,-44,-45,-21,-20,-54,-49,-54,8,8,8,8,-22,-23,-50,-54,8,8,-24,]),'ELSE':([101,],[103,]),'WRITELN':([6,20,22,37,39,40,42,43,44,45,47,49,51,54,55,58,62,63,85,86,89,91,92,94,95,97,98,100,101,102,104,105,106,107,],[-55,-32,-48,48,-46,-16,48,-15,-17,-19,-18,-47,-13,-14,-12,-11,-44,-45,-21,-20,-54,-49,-54,48,48,48,48,-22,-23,-50,-54,48,48,-24,]),'AMPERSAND':([88,],[93,]),'STR':([0,1,6,7,9,11,12,18,20,22,30,37,39,40,42,43,44,45,46,47,49,51,54,55,57,58,62,63,85,86,89,91,92,94,95,97,98,100,101,102,104,105,106,107,],[2,-4,-55,-5,-6,-3,2,-2,-32,-48,31,2,-46,-16,2,-15,-17,-19,-8,-18,-47,2,-14,-12,-7,-11,-44,-45,-21,-20,-54,-49,-54,2,2,2,2,-22,-23,-50,-54,2,2,-24,]),'EQ':([23,24,25,26,27,29,67,],[-43,-39,-42,-38,-40,-41,81,]),'ID':([2,3,6,8,10,13,16,19,20,22,36,37,39,40,42,43,44,45,47,49,51,54,55,56,58,59,60,62,63,64,77,78,79,80,81,82,83,85,86,89,91,92,93,94,95,97,98,100,101,102,104,105,106,107,],[-36,14,-55,14,-35,-37,21,29,-32,-48,38,50,-46,-16,50,-15,-17,-19,-18,-47,-13,-14,-12,29,-11,29,29,-44,-45,29,-31,29,-28,-30,-26,-29,-27,-21,-20,-54,-49,-54,96,50,50,50,50,-22,-23,-50,-54,50,50,-24,]),'IF':([6,20,22,37,39,40,42,43,44,45,47,49,51,54,55,58,62,63,85,86,89,91,92,94,95,97,98,100,101,102,104,105,106,107,],[-55,-32,-48,52,-46,-16,52,-15,-17,-19,-18,-47,-13,-14,-12,-11,-44,-45,-21,-20,-54,-49,-54,52,52,52,52,-22,-23,-50,-54,52,52,-24,]),'LBRACE':([35,76,87,103,],[37,89,92,104,]),'FALSE':([19,56,59,60,64,77,78,79,80,81,82,83,],[23,23,23,23,23,-31,23,-28,-30,-26,-29,-27,]),'GREATER':([23,24,25,26,27,29,67,],[-43,-39,-42,-38,-40,-41,79,]),'READF':([6,20,22,37,39,40,42,43,44,45,47,49,51,54,55,58,62,63,85,86,89,91,92,94,95,97,98,100,101,102,104,105,106,107,],[-55,-32,-48,53,-46,-16,53,-15,-17,-19,-18,-47,-13,-14,-12,-11,-44,-45,-21,-20,-54,-49,-54,53,53,53,53,-22,-23,-50,-54,53,53,-24,]),'INT':([0,1,6,7,9,11,12,18,20,22,37,39,40,42,43,44,45,46,47,49,51,54,55,57,58,62,63,85,86,89,91,92,94,95,97,98,100,101,102,104,105,106,107,],[10,-4,-55,-5,-6,-3,10,-2,-32,-48,10,-46,-16,10,-15,-17,-19,-8,-18,-47,10,-14,-12,-7,-11,-44,-45,-21,-20,-54,-49,-54,10,10,10,10,-22,-23,-50,-54,10,10,-24,]),'GET_STRING':([65,],[73,]),'BOOL':([0,1,6,7,9,11,12,18,20,22,37,39,40,42,43,44,45,46,47,49,51,54,55,57,58,62,63,85,86,89,91,92,94,95,97,98,100,101,102,104,105,106,107,],[13,-4,-55,-5,-6,-3,13,-2,-32,-48,13,-46,-16,13,-15,-17,-19,-8,-18,-47,13,-14,-12,-7,-11,-44,-45,-21,-20,-54,-49,-54,13,13,13,13,-22,-23,-50,-54,13,13,-24,]),'GET_BOOL':([65,],[72,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'constant':([0,12,37,42,51,94,95,97,98,105,106,],[1,1,39,39,62,39,39,39,39,39,39,]),'var_type':([0,12,37,42,51,94,95,97,98,105,106,],[3,3,3,3,3,3,3,3,3,3,3,]),'assigned':([37,42,94,95,97,98,105,106,],[40,40,40,40,40,40,40,40,]),'boolean':([19,56,59,60,64,78,],[27,27,27,27,27,27,]),'expressions':([37,94,95,105,],[42,97,98,106,]),'if':([37,42,94,95,97,98,105,106,],[43,43,43,43,43,43,43,43,]),'new_scope':([0,12,89,92,104,],[4,4,94,95,105,]),'start':([0,],[5,]),'init':([3,8,],[15,17,]),'params':([30,],[32,]),'statement':([56,64,],[66,71,]),'print':([37,42,94,95,97,98,105,106,],[44,44,44,44,44,44,44,44,]),'call':([37,42,94,95,97,98,105,106,],[45,45,45,45,45,45,45,45,]),'gets':([65,],[75,]),'type':([19,56,59,60,64,78,],[28,67,68,69,67,90,]),'empty':([0,12,30,89,92,104,],[6,6,33,6,6,6,]),'function':([0,12,],[7,7,]),'get':([37,42,94,95,97,98,105,106,],[47,47,47,47,47,47,47,47,]),'variable':([0,12,37,42,51,94,95,97,98,105,106,],[9,9,49,49,63,49,49,49,49,49,49,]),'constants':([37,42,94,95,97,98,105,106,],[51,51,51,51,51,51,51,51,]),'logic_op':([67,],[78,]),'expr':([0,12,],[11,18,]),'exprs':([0,],[12,]),'while':([37,42,94,95,97,98,105,106,],[54,54,54,54,54,54,54,54,]),'expression':([37,42,94,95,97,98,105,106,],[55,58,55,55,58,58,55,58,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> exprs','start',1,'p_start','calc.py',493),
  ('exprs -> exprs expr','exprs',2,'p_list_exprs','calc.py',506),
  ('exprs -> expr','exprs',1,'p_exprs','calc.py',513),
  ('expr -> constant','expr',1,'p_expr','calc.py',520),
  ('expr -> function','expr',1,'p_expr','calc.py',521),
  ('expr -> variable','expr',1,'p_expr','calc.py',522),
  ('function -> new_scope VOID ID LPAREN params RPAREN LBRACE expressions RBRACE','function',9,'p_function','calc.py',530),
  ('function -> new_scope VOID ID LPAREN params RPAREN LBRACE RBRACE','function',8,'p_empty_function','calc.py',542),
  ('params -> STR LSQUARE RSQUARE ID','params',4,'p_params','calc.py',557),
  ('params -> empty','params',1,'p_empty_params','calc.py',571),
  ('expressions -> expressions expression','expressions',2,'p_list_expressions','calc.py',581),
  ('expressions -> expression','expressions',1,'p_expressions','calc.py',588),
  ('expression -> constants','expression',1,'p_expression','calc.py',596),
  ('expression -> while','expression',1,'p_expression','calc.py',597),
  ('expression -> if','expression',1,'p_expression','calc.py',598),
  ('expression -> assigned','expression',1,'p_expression','calc.py',599),
  ('expression -> print','expression',1,'p_expression','calc.py',600),
  ('expression -> get','expression',1,'p_expression','calc.py',601),
  ('expression -> call','expression',1,'p_expression','calc.py',602),
  ('call -> ID LPAREN RPAREN SEMICOLON','call',4,'p_call','calc.py',610),
  ('assigned -> ID ASSIGN type SEMICOLON','assigned',4,'p_assigned','calc.py',631),
  ('while -> WHILE LPAREN statement RPAREN LBRACE new_scope expressions RBRACE','while',8,'p_while','calc.py',670),
  ('if -> IF LPAREN statement RPAREN LBRACE new_scope expressions RBRACE','if',8,'p_if','calc.py',680),
  ('if -> IF LPAREN statement RPAREN LBRACE new_scope expressions RBRACE ELSE LBRACE new_scope expressions RBRACE','if',13,'p_if_else','calc.py',690),
  ('statement -> type logic_op type','statement',3,'p_statement','calc.py',704),
  ('logic_op -> EQ','logic_op',1,'p_logic_op','calc.py',836),
  ('logic_op -> NOT_EQ','logic_op',1,'p_logic_op','calc.py',837),
  ('logic_op -> GREATER','logic_op',1,'p_logic_op','calc.py',838),
  ('logic_op -> GREATER_EQ','logic_op',1,'p_logic_op','calc.py',839),
  ('logic_op -> LESS','logic_op',1,'p_logic_op','calc.py',840),
  ('logic_op -> LESS_EQ','logic_op',1,'p_logic_op','calc.py',841),
  ('variable -> var_type init SEMICOLON','variable',3,'p_variable','calc.py',851),
  ('init -> ID ASSIGN type','init',3,'p_init_value','calc.py',864),
  ('init -> ID','init',1,'p_init','calc.py',871),
  ('var_type -> INT','var_type',1,'p_var_type','calc.py',878),
  ('var_type -> STR','var_type',1,'p_var_type','calc.py',879),
  ('var_type -> BOOL','var_type',1,'p_var_type','calc.py',880),
  ('type -> NUMBER','type',1,'p_type','calc.py',889),
  ('type -> STRING','type',1,'p_type','calc.py',890),
  ('type -> boolean','type',1,'p_type','calc.py',891),
  ('type -> ID','type',1,'p_type','calc.py',892),
  ('boolean -> TRUE','boolean',1,'p_boolean','calc.py',900),
  ('boolean -> FALSE','boolean',1,'p_boolean','calc.py',901),
  ('constants -> constants constant','constants',2,'p_list_constants','calc.py',908),
  ('constants -> constants variable','constants',2,'p_list_constants','calc.py',909),
  ('constants -> constant','constants',1,'p_constants','calc.py',919),
  ('constants -> variable','constants',1,'p_constants','calc.py',920),
  ('constant -> ENUM init SEMICOLON','constant',3,'p_constant','calc.py',931),
  ('print -> WRITELN LPAREN type RPAREN SEMICOLON','print',5,'p_print','calc.py',956),
  ('get -> READF LPAREN gets COMMA AMPERSAND ID RPAREN SEMICOLON','get',8,'p_get','calc.py',981),
  ('gets -> GET_INT','gets',1,'p_gets','calc.py',1015),
  ('gets -> GET_STRING','gets',1,'p_gets','calc.py',1016),
  ('gets -> GET_BOOL','gets',1,'p_gets','calc.py',1017),
  ('empty -> <empty>','empty',0,'p_empty','calc.py',1023),
  ('new_scope -> empty','new_scope',1,'p_new_scope','calc.py',1032),
]
