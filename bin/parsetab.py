
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOPTASUleftOPKAKERUAPPEND CLASS CONMA ELSE EQOP EQUALS GLOBAL ID IF INCLUDE KAKKO KOKKA LAMDA LBRACE LEN LISL LISR LIST NUMBER OPKAKERU OPMIN OPTASU OPWARU PASS PIRIOD QOT RBRACE RESERV RETURN SEMI STR STRUCT TYPE TYPEF WHILE colon dainari syounari yaji\n        teigilist : teigi\n                | teigilist teigi\n    \n        paramlist : param\n                  | paramlist CONMA param\n    \n        param : TYPE ID\n              | TYPE\n    \n    bun : ID EQUALS LAMDA KAKKO paramlist KOKKA LBRACE bunlist RBRACE SEMI\n    \n    bun : ID KAKKO shiki KOKKA SEMI\n    \n    teigi : STR\n    \n    bun : ID EQUALS ID SEMI\n    \n    teigi : TYPE ID KAKKO paramlist KOKKA yaji TYPE LBRACE bunlist RBRACE\n    \n    teigi : TYPE ID yaji TYPE LBRACE bunlist RBRACE\n    \n    teigi : STRUCT ID LBRACE teigilist RBRACE\n    \n    class : classf\n    \n    class : class classf\n    \n    teigi : CLASS ID LBRACE class RBRACE\n    \n    teigi : INCLUDE LBRACE shiki RBRACE\n    \n    classf : ID KAKKO paramlist KOKKA yaji TYPE LBRACE bunlist RBRACE\n    \n    bun : ID PIRIOD ID KAKKO shiki KOKKA SEMI\n    \n    bun : PASS SEMI\n    \n    bunlist : bun\n    \n    bunlist : bunlist bun\n    \n    bun : TYPE ID EQUALS shiki SEMI\n    \n    bun : TYPE ID EQUALS LISL shiki LISR SEMI\n    \n    bun : TYPE ID EQUALS ID LISL NUMBER LISR SEMI\n    \n    bun : ID EQUALS LISL LISR SEMI\n    \n    bun : ID EQUALS ID OPTASU NUMBER SEMI\n        | ID EQUALS ID OPKAKERU NUMBER SEMI\n        | ID EQUALS ID OPMIN NUMBER SEMI\n        | ID EQUALS ID OPWARU NUMBER SEMI\n    \n    shiki : TYPEF KAKKO shiki KOKKA\n    \n    shiki : TYPE KAKKO shiki KOKKA\n    \n    shiki : RESERV KAKKO shiki KOKKA\n    \n    bun : RETURN shiki SEMI\n        | RETURN bun\n    \n    bun : IF hikaku LBRACE bunlist RBRACE \n    \n    bun : IF hikaku LBRACE bunlist RBRACE ELSE LBRACE bunlist RBRACE\n    \n    bun : WHILE shiki LBRACE bunlist RBRACE \n    \n    hikaku : shiki\n    \n     hikaku : hikaku EQOP shiki\n            | hikaku dainari shiki\n            | hikaku syounari shiki\n    \n    shiki : NUMBER\n    \n    shiki : ID\n    \n    shiki : TYPE\n    \n    shiki : STR\n    \n    bun : PASS \n        | PASS KAKKO KOKKA\n        | PASS KAKKO PASS KOKKA SEMI\n    \n    shiki : LEN KAKKO shiki KOKKA\n    \n    bun : ID LISL shiki LISR EQUALS shiki SEMI\n    \n    shiki : OPMIN NUMBER\n    \n    shiki : shiki CONMA shiki\n    \n    shiki : shiki OPTASU shiki\n          | shiki OPKAKERU shiki\n          | shiki OPMIN shiki\n          | shiki OPWARU shiki\n    \n    shiki : KAKKO shiki KOKKA\n    \n    shiki : shiki CONMA ID       \n    \n    bun : RESERV ID LISL NUMBER LISR EQUALS STR SEMI\n        | RESERV ID LISL ID LISR EQUALS STR SEMI\n        | RESERV ID LISL NUMBER LISR EQUALS ID SEMI\n        | RESERV ID LISL ID LISR EQUALS ID SEMI\n    \n    bun : RESERV KAKKO shiki KOKKA SEMI\n    \n    shiki : ID KAKKO shiki KOKKA\n    \n    shiki : ID KAKKO KOKKA\n    \n    bun : TYPE TYPE LBRACE letlist RBRACE SEMI\n    \n    bun : GLOBAL TYPE LBRACE letlist RBRACE SEMI\n     \n    letlist : ID EQUALS STR SEMI \n            | ID EQUALS NUMBER SEMI \n            | letlist ID EQUALS STR SEMI\n            | letlist ID EQUALS NUMBER SEMI\n    \n    bun : ID EQUALS ID OPTASU STR SEMI\n        | ID EQUALS STR OPTASU ID SEMI\n    \n    bun : ID OPTASU OPTASU SEMI\n        | STR OPTASU OPTASU SEMI\n    '
    
_lr_action_items = {'STR':([0,1,2,3,8,12,15,19,31,35,36,37,38,39,40,41,43,44,45,46,51,52,54,73,74,75,76,77,78,91,92,94,96,97,98,101,110,114,116,126,127,128,129,130,131,132,133,134,140,145,146,147,155,157,161,165,169,172,175,177,185,187,189,190,193,194,197,199,200,201,206,207,208,209,210,212,216,217,218,219,225,226,227,228,229,237,238,239,240,241,242,243,245,246,],[3,3,-1,-9,-2,24,3,24,3,-17,24,24,24,24,24,24,24,24,24,24,80,-13,-16,80,-21,-47,105,24,24,120,24,24,-12,-22,-20,-35,24,80,24,-48,-34,24,24,80,24,24,24,80,80,24,-10,180,24,-75,80,80,-76,-11,202,-23,-26,-8,24,-49,-36,-38,-64,80,-67,220,-27,-73,-28,-29,-30,-74,231,233,-68,80,-24,80,-19,-51,80,-25,80,80,-63,-61,-62,-60,-37,-7,]),'TYPE':([0,1,2,3,8,12,13,14,15,19,31,35,36,37,38,39,40,41,43,44,45,46,50,51,52,53,54,69,71,73,74,75,76,77,78,81,92,94,96,97,98,101,102,110,114,116,126,127,128,129,130,131,132,133,134,139,140,145,146,151,155,157,161,165,169,172,177,185,187,189,190,193,194,197,199,200,206,207,208,209,210,212,218,219,225,226,227,228,229,237,238,239,240,241,242,243,245,246,],[4,4,-1,-9,-2,20,27,30,4,20,4,-17,20,20,20,20,20,20,20,20,20,20,27,71,-13,27,-16,88,89,71,-21,-47,102,20,20,112,20,20,-12,-22,-20,-35,89,20,71,20,-48,-34,20,20,71,20,20,20,71,171,71,20,-10,27,20,-75,71,71,-76,-11,-23,-26,-8,20,-49,-36,-38,-64,71,-67,-27,-73,-28,-29,-30,-74,-68,71,-24,71,-19,-51,71,-25,71,71,-63,-61,-62,-60,-37,-7,]),'STRUCT':([0,1,2,3,8,15,31,35,52,54,96,172,],[5,5,-1,-9,-2,5,5,-17,-13,-16,-12,-11,]),'CLASS':([0,1,2,3,8,15,31,35,52,54,96,172,],[6,6,-1,-9,-2,6,6,-17,-13,-16,-12,-11,]),'INCLUDE':([0,1,2,3,8,15,31,35,52,54,96,172,],[7,7,-1,-9,-2,7,7,-17,-13,-16,-12,-11,]),'$end':([1,2,3,8,35,52,54,96,172,],[0,-1,-9,-2,-17,-13,-16,-12,-11,]),'RBRACE':([2,3,8,17,20,22,23,24,31,33,34,35,47,52,54,55,56,57,58,59,60,61,63,67,73,74,75,83,84,85,86,87,96,97,98,101,126,127,140,141,146,157,161,165,169,170,172,177,185,187,190,193,194,197,200,206,207,208,209,210,212,218,219,222,223,225,227,228,234,235,236,237,238,239,240,241,242,243,245,246,],[-1,-9,-2,35,-45,-43,-44,-46,52,54,-14,-17,-52,-13,-16,-15,-53,-44,-54,-55,-56,-57,-58,-66,96,-21,-47,-31,-32,-33,-65,-50,-12,-22,-20,-35,-48,-34,172,173,-10,-75,193,194,-76,198,-11,-23,-26,-8,-49,-36,-38,-64,-67,-27,-73,-28,-29,-30,-74,-68,234,-69,-70,-24,-19,-51,-18,-71,-72,-25,244,245,-63,-61,-62,-60,-37,-7,]),'ID':([4,5,6,12,16,19,27,33,34,36,37,38,39,40,41,43,44,45,46,51,55,71,73,74,75,76,77,78,79,91,92,93,94,97,98,101,102,103,110,114,115,116,126,127,128,129,130,131,132,133,134,135,138,140,141,145,146,153,155,157,161,165,169,170,177,185,187,189,190,193,194,197,199,200,206,207,208,209,210,212,216,217,218,219,222,223,225,226,227,228,229,234,235,236,237,238,239,240,241,242,243,245,246,],[9,10,11,23,32,23,48,32,-14,57,23,23,23,23,23,23,23,23,23,72,-15,90,72,-21,-47,104,23,23,109,117,23,122,23,-22,-20,-35,90,109,23,72,142,143,-48,-34,23,23,72,23,23,23,72,166,142,72,174,23,-10,186,23,-75,72,72,-76,174,-23,-26,-8,23,-49,-36,-38,-64,72,-67,-27,-73,-28,-29,-30,-74,230,232,-68,72,-69,-70,-24,72,-19,-51,72,-18,-71,-72,-25,72,72,-63,-61,-62,-60,-37,-7,]),'LBRACE':([7,10,11,20,22,23,24,30,47,56,57,58,59,60,61,63,67,83,84,85,86,87,88,89,106,107,108,112,162,163,164,171,211,215,],[12,15,16,-45,-43,-44,-46,51,-52,-53,-44,-54,-55,-56,-57,-58,-66,-31,-32,-33,-65,-50,114,115,130,-39,134,138,-40,-41,-42,199,226,229,]),'KAKKO':([9,12,18,19,20,21,23,25,32,36,37,38,39,40,41,43,44,45,46,57,72,75,76,77,78,79,92,94,102,103,104,110,116,118,122,128,129,131,132,133,143,145,155,189,],[13,19,41,19,43,44,45,46,53,19,19,19,19,19,19,19,19,19,19,45,92,99,19,19,19,110,19,19,43,128,129,19,19,151,155,19,19,19,19,19,45,19,19,19,]),'yaji':([9,49,113,],[14,69,139,]),'TYPEF':([12,19,36,37,38,39,40,41,43,44,45,46,76,77,78,92,94,110,116,128,129,131,132,133,145,155,189,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'RESERV':([12,19,36,37,38,39,40,41,43,44,45,46,51,73,74,75,76,77,78,92,94,97,98,101,110,114,116,126,127,128,129,130,131,132,133,134,140,145,146,155,157,161,165,169,177,185,187,189,190,193,194,197,199,200,206,207,208,209,210,212,218,219,225,226,227,228,229,237,238,239,240,241,242,243,245,246,],[21,21,21,21,21,21,21,21,21,21,21,21,79,79,-21,-47,103,21,21,21,21,-22,-20,-35,21,79,21,-48,-34,21,21,79,21,21,21,79,79,21,-10,21,-75,79,79,-76,-23,-26,-8,21,-49,-36,-38,-64,79,-67,-27,-73,-28,-29,-30,-74,-68,79,-24,79,-19,-51,79,-25,79,79,-63,-61,-62,-60,-37,-7,]),'NUMBER':([12,19,26,36,37,38,39,40,41,43,44,45,46,76,77,78,92,94,110,116,128,129,131,132,133,135,145,147,148,149,150,155,175,176,189,201,],[22,22,47,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,167,22,179,181,182,183,22,203,204,22,221,]),'LEN':([12,19,36,37,38,39,40,41,43,44,45,46,76,77,78,92,94,110,116,128,129,131,132,133,145,155,189,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'OPMIN':([12,17,19,20,22,23,24,36,37,38,39,40,41,42,43,44,45,46,47,56,57,58,59,60,61,62,63,64,65,66,67,68,76,77,78,83,84,85,86,87,92,94,100,102,104,105,107,108,110,116,117,121,123,128,129,131,132,133,136,143,144,145,155,159,160,162,163,164,178,188,189,191,192,214,],[26,39,26,-45,-43,-44,-46,26,26,26,26,26,26,39,26,26,26,26,-52,39,-44,-54,-55,39,39,39,-58,39,39,39,-66,39,26,26,26,-31,-32,-33,-65,-50,26,26,39,-45,-44,-46,39,39,26,26,149,39,39,26,26,26,26,26,39,-44,39,26,26,39,39,39,39,39,39,39,26,-33,-65,39,]),'CONMA':([17,20,22,23,24,27,28,29,42,47,48,56,57,58,59,60,61,62,63,64,65,66,67,68,70,82,83,84,85,86,87,100,102,104,105,107,108,121,123,136,143,144,159,160,162,163,164,178,184,188,191,192,214,],[36,-45,-43,-44,-46,-6,50,-3,36,-52,-5,36,-44,-54,-55,36,36,36,-58,36,36,36,-66,36,-4,50,-31,-32,-33,-65,-50,36,-45,-44,-46,36,36,36,36,36,-44,36,36,36,36,36,36,36,50,36,-33,-65,36,]),'OPTASU':([17,20,22,23,24,42,47,56,57,58,59,60,61,62,63,64,65,66,67,68,72,80,83,84,85,86,87,95,100,102,104,105,107,108,111,117,120,121,123,136,143,144,159,160,162,163,164,178,188,191,192,214,],[37,-45,-43,-44,-46,37,-52,37,-44,-54,-55,37,37,37,-58,37,37,37,-66,37,95,111,-31,-32,-33,-65,-50,124,37,-45,95,111,37,37,137,147,153,37,37,37,-44,37,37,37,37,37,37,37,37,-33,-65,37,]),'OPKAKERU':([17,20,22,23,24,42,47,56,57,58,59,60,61,62,63,64,65,66,67,68,83,84,85,86,87,100,102,104,105,107,108,117,121,123,136,143,144,159,160,162,163,164,178,188,191,192,214,],[38,-45,-43,-44,-46,38,-52,38,-44,38,-55,38,38,38,-58,38,38,38,-66,38,-31,-32,-33,-65,-50,38,-45,-44,-46,38,38,148,38,38,38,-44,38,38,38,38,38,38,38,38,-33,-65,38,]),'OPWARU':([17,20,22,23,24,42,47,56,57,58,59,60,61,62,63,64,65,66,67,68,83,84,85,86,87,100,102,104,105,107,108,117,121,123,136,143,144,159,160,162,163,164,178,188,191,192,214,],[40,-45,-43,-44,-46,40,-52,40,-44,-54,-55,40,40,40,-58,40,40,40,-66,40,-31,-32,-33,-65,-50,40,-45,-44,-46,40,40,150,40,40,40,-44,40,40,40,40,40,40,40,40,-33,-65,40,]),'KOKKA':([20,22,23,24,27,28,29,42,45,47,48,56,57,58,59,60,61,62,63,64,65,66,67,68,70,82,83,84,85,86,87,99,121,125,129,136,159,160,184,188,],[-45,-43,-44,-46,-6,49,-3,63,67,-52,-5,-53,-44,-54,-55,-56,-57,83,-58,84,85,86,-66,87,-4,113,-31,-32,-33,-65,-50,126,154,158,67,168,191,192,211,213,]),'SEMI':([20,22,23,24,47,56,57,58,59,60,61,63,67,75,83,84,85,86,87,100,102,104,105,117,124,137,143,144,152,154,158,168,173,179,180,181,182,183,186,191,192,198,202,203,205,213,214,220,221,224,230,231,232,233,244,],[-45,-43,-44,-46,-52,-53,-44,-54,-55,-56,-57,-58,-66,98,-31,-32,-33,-65,-50,127,-45,-44,-46,146,157,169,-44,177,185,187,190,197,200,206,207,208,209,210,212,197,187,218,222,223,225,227,228,235,236,237,240,241,242,243,246,]),'EQOP':([20,22,23,24,47,56,57,58,59,60,61,63,67,83,84,85,86,87,106,107,162,163,164,],[-45,-43,-44,-46,-52,-53,-44,-54,-55,-56,-57,-58,-66,-31,-32,-33,-65,-50,131,-39,-40,-41,-42,]),'dainari':([20,22,23,24,47,56,57,58,59,60,61,63,67,83,84,85,86,87,106,107,162,163,164,],[-45,-43,-44,-46,-52,-53,-44,-54,-55,-56,-57,-58,-66,-31,-32,-33,-65,-50,132,-39,-40,-41,-42,]),'syounari':([20,22,23,24,47,56,57,58,59,60,61,63,67,83,84,85,86,87,106,107,162,163,164,],[-45,-43,-44,-46,-52,-53,-44,-54,-55,-56,-57,-58,-66,-31,-32,-33,-65,-50,133,-39,-40,-41,-42,]),'LISR':([20,22,23,24,47,56,57,58,59,60,61,63,67,83,84,85,86,87,119,123,166,167,178,204,],[-45,-43,-44,-46,-52,-53,-44,-54,-55,-56,-57,-58,-66,-31,-32,-33,-65,-50,152,156,195,196,205,224,]),'PASS':([51,73,74,75,76,97,98,99,101,114,126,127,130,134,140,146,157,161,165,169,177,185,187,190,193,194,197,199,200,206,207,208,209,210,212,218,219,225,226,227,228,229,237,238,239,240,241,242,243,245,246,],[75,75,-21,-47,75,-22,-20,125,-35,75,-48,-34,75,75,75,-10,-75,75,75,-76,-23,-26,-8,-49,-36,-38,-64,75,-67,-27,-73,-28,-29,-30,-74,-68,75,-24,75,-19,-51,75,-25,75,75,-63,-61,-62,-60,-37,-7,]),'RETURN':([51,73,74,75,76,97,98,101,114,126,127,130,134,140,146,157,161,165,169,177,185,187,190,193,194,197,199,200,206,207,208,209,210,212,218,219,225,226,227,228,229,237,238,239,240,241,242,243,245,246,],[76,76,-21,-47,76,-22,-20,-35,76,-48,-34,76,76,76,-10,-75,76,76,-76,-23,-26,-8,-49,-36,-38,-64,76,-67,-27,-73,-28,-29,-30,-74,-68,76,-24,76,-19,-51,76,-25,76,76,-63,-61,-62,-60,-37,-7,]),'IF':([51,73,74,75,76,97,98,101,114,126,127,130,134,140,146,157,161,165,169,177,185,187,190,193,194,197,199,200,206,207,208,209,210,212,218,219,225,226,227,228,229,237,238,239,240,241,242,243,245,246,],[77,77,-21,-47,77,-22,-20,-35,77,-48,-34,77,77,77,-10,-75,77,77,-76,-23,-26,-8,-49,-36,-38,-64,77,-67,-27,-73,-28,-29,-30,-74,-68,77,-24,77,-19,-51,77,-25,77,77,-63,-61,-62,-60,-37,-7,]),'WHILE':([51,73,74,75,76,97,98,101,114,126,127,130,134,140,146,157,161,165,169,177,185,187,190,193,194,197,199,200,206,207,208,209,210,212,218,219,225,226,227,228,229,237,238,239,240,241,242,243,245,246,],[78,78,-21,-47,78,-22,-20,-35,78,-48,-34,78,78,78,-10,-75,78,78,-76,-23,-26,-8,-49,-36,-38,-64,78,-67,-27,-73,-28,-29,-30,-74,-68,78,-24,78,-19,-51,78,-25,78,78,-63,-61,-62,-60,-37,-7,]),'GLOBAL':([51,73,74,75,76,97,98,101,114,126,127,130,134,140,146,157,161,165,169,177,185,187,190,193,194,197,199,200,206,207,208,209,210,212,218,219,225,226,227,228,229,237,238,239,240,241,242,243,245,246,],[81,81,-21,-47,81,-22,-20,-35,81,-48,-34,81,81,81,-10,-75,81,81,-76,-23,-26,-8,-49,-36,-38,-64,81,-67,-27,-73,-28,-29,-30,-74,-68,81,-24,81,-19,-51,81,-25,81,81,-63,-61,-62,-60,-37,-7,]),'EQUALS':([72,90,104,142,156,174,195,196,],[91,116,91,175,189,201,216,217,]),'PIRIOD':([72,104,],[93,93,]),'LISL':([72,91,104,109,116,143,],[94,119,94,135,145,176,]),'LAMDA':([91,],[118,]),'ELSE':([193,],[215,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'teigilist':([0,15,],[1,31,]),'teigi':([0,1,15,31,],[2,8,2,8,]),'shiki':([12,19,36,37,38,39,40,41,43,44,45,46,76,77,78,92,94,110,116,128,129,131,132,133,145,155,189,],[17,42,56,58,59,60,61,62,64,65,66,68,100,107,108,121,123,136,144,159,160,162,163,164,178,188,214,]),'paramlist':([13,53,151,],[28,82,184,]),'param':([13,50,53,151,],[29,70,29,29,]),'class':([16,],[33,]),'classf':([16,33,],[34,55,]),'bunlist':([51,114,130,134,199,226,229,],[73,140,161,165,219,238,239,]),'bun':([51,73,76,114,130,134,140,161,165,199,219,226,229,238,239,],[74,97,101,74,74,74,97,97,97,74,97,74,74,97,97,]),'hikaku':([77,],[106,]),'letlist':([115,138,],[141,170,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> teigilist","S'",1,None,None,None),
  ('teigilist -> teigi','teigilist',1,'p_teigilist_0','compile.py',43),
  ('teigilist -> teigilist teigi','teigilist',2,'p_teigilist_0','compile.py',44),
  ('paramlist -> param','paramlist',1,'p_paramlist','compile.py',53),
  ('paramlist -> paramlist CONMA param','paramlist',3,'p_paramlist','compile.py',54),
  ('param -> TYPE ID','param',2,'p_param','compile.py',65),
  ('param -> TYPE','param',1,'p_param','compile.py',66),
  ('bun -> ID EQUALS LAMDA KAKKO paramlist KOKKA LBRACE bunlist RBRACE SEMI','bun',10,'p_lamda','compile.py',75),
  ('bun -> ID KAKKO shiki KOKKA SEMI','bun',5,'p_call','compile.py',81),
  ('teigi -> STR','teigi',1,'p_comment','compile.py',87),
  ('bun -> ID EQUALS ID SEMI','bun',4,'p_instance','compile.py',93),
  ('teigi -> TYPE ID KAKKO paramlist KOKKA yaji TYPE LBRACE bunlist RBRACE','teigi',10,'p_teigi_0','compile.py',99),
  ('teigi -> TYPE ID yaji TYPE LBRACE bunlist RBRACE','teigi',7,'p_teigi_void','compile.py',105),
  ('teigi -> STRUCT ID LBRACE teigilist RBRACE','teigi',5,'p_teigi_1','compile.py',111),
  ('class -> classf','class',1,'p_class_f','compile.py',117),
  ('class -> class classf','class',2,'p_class_f_2','compile.py',123),
  ('teigi -> CLASS ID LBRACE class RBRACE','teigi',5,'p_class','compile.py',129),
  ('teigi -> INCLUDE LBRACE shiki RBRACE','teigi',4,'p_include','compile.py',135),
  ('classf -> ID KAKKO paramlist KOKKA yaji TYPE LBRACE bunlist RBRACE','classf',9,'p_classfunc','compile.py',141),
  ('bun -> ID PIRIOD ID KAKKO shiki KOKKA SEMI','bun',7,'p_class_fc','compile.py',147),
  ('bun -> PASS SEMI','bun',2,'p_pass','compile.py',153),
  ('bunlist -> bun','bunlist',1,'p_bunlist_0','compile.py',159),
  ('bunlist -> bunlist bun','bunlist',2,'p_bunlist_1','compile.py',165),
  ('bun -> TYPE ID EQUALS shiki SEMI','bun',5,'p_bun_type','compile.py',173),
  ('bun -> TYPE ID EQUALS LISL shiki LISR SEMI','bun',7,'p_bun_lis','compile.py',180),
  ('bun -> TYPE ID EQUALS ID LISL NUMBER LISR SEMI','bun',8,'p_bun_deflis','compile.py',186),
  ('bun -> ID EQUALS LISL LISR SEMI','bun',5,'p_bun_newlis','compile.py',192),
  ('bun -> ID EQUALS ID OPTASU NUMBER SEMI','bun',6,'p_add','compile.py',198),
  ('bun -> ID EQUALS ID OPKAKERU NUMBER SEMI','bun',6,'p_add','compile.py',199),
  ('bun -> ID EQUALS ID OPMIN NUMBER SEMI','bun',6,'p_add','compile.py',200),
  ('bun -> ID EQUALS ID OPWARU NUMBER SEMI','bun',6,'p_add','compile.py',201),
  ('shiki -> TYPEF KAKKO shiki KOKKA','shiki',4,'p_shiki_type','compile.py',208),
  ('shiki -> TYPE KAKKO shiki KOKKA','shiki',4,'p_shiki_int','compile.py',214),
  ('shiki -> RESERV KAKKO shiki KOKKA','shiki',4,'p_shiki_input','compile.py',220),
  ('bun -> RETURN shiki SEMI','bun',3,'p_bun_return','compile.py',226),
  ('bun -> RETURN bun','bun',2,'p_bun_return','compile.py',227),
  ('bun -> IF hikaku LBRACE bunlist RBRACE','bun',5,'p_bun_if1','compile.py',233),
  ('bun -> IF hikaku LBRACE bunlist RBRACE ELSE LBRACE bunlist RBRACE','bun',9,'p_bun_if2','compile.py',239),
  ('bun -> WHILE shiki LBRACE bunlist RBRACE','bun',5,'p_bun_while','compile.py',245),
  ('hikaku -> shiki','hikaku',1,'p_hikaku_1','compile.py',251),
  ('hikaku -> hikaku EQOP shiki','hikaku',3,'p_hikaku_2','compile.py',257),
  ('hikaku -> hikaku dainari shiki','hikaku',3,'p_hikaku_2','compile.py',258),
  ('hikaku -> hikaku syounari shiki','hikaku',3,'p_hikaku_2','compile.py',259),
  ('shiki -> NUMBER','shiki',1,'p_shiki_num','compile.py',265),
  ('shiki -> ID','shiki',1,'p_shiki_id','compile.py',271),
  ('shiki -> TYPE','shiki',1,'p_shiki_void','compile.py',277),
  ('shiki -> STR','shiki',1,'p_shiki_str','compile.py',283),
  ('bun -> PASS','bun',1,'p_shiki_pass','compile.py',289),
  ('bun -> PASS KAKKO KOKKA','bun',3,'p_shiki_pass','compile.py',290),
  ('bun -> PASS KAKKO PASS KOKKA SEMI','bun',5,'p_shiki_pass','compile.py',291),
  ('shiki -> LEN KAKKO shiki KOKKA','shiki',4,'p_shiki_len','compile.py',297),
  ('bun -> ID LISL shiki LISR EQUALS shiki SEMI','bun',7,'p_bun_append','compile.py',303),
  ('shiki -> OPMIN NUMBER','shiki',2,'p_shiki_MINNUM','compile.py',309),
  ('shiki -> shiki CONMA shiki','shiki',3,'p_shiki_conma','compile.py',315),
  ('shiki -> shiki OPTASU shiki','shiki',3,'p_shiki_enzan','compile.py',324),
  ('shiki -> shiki OPKAKERU shiki','shiki',3,'p_shiki_enzan','compile.py',325),
  ('shiki -> shiki OPMIN shiki','shiki',3,'p_shiki_enzan','compile.py',326),
  ('shiki -> shiki OPWARU shiki','shiki',3,'p_shiki_enzan','compile.py',327),
  ('shiki -> KAKKO shiki KOKKA','shiki',3,'p_shiki_kakko','compile.py',333),
  ('shiki -> shiki CONMA ID','shiki',3,'p_shiki_args','compile.py',339),
  ('bun -> RESERV ID LISL NUMBER LISR EQUALS STR SEMI','bun',8,'p_bun_insert','compile.py',348),
  ('bun -> RESERV ID LISL ID LISR EQUALS STR SEMI','bun',8,'p_bun_insert','compile.py',349),
  ('bun -> RESERV ID LISL NUMBER LISR EQUALS ID SEMI','bun',8,'p_bun_insert','compile.py',350),
  ('bun -> RESERV ID LISL ID LISR EQUALS ID SEMI','bun',8,'p_bun_insert','compile.py',351),
  ('bun -> RESERV KAKKO shiki KOKKA SEMI','bun',5,'p_bun_reserv','compile.py',357),
  ('shiki -> ID KAKKO shiki KOKKA','shiki',4,'p_shiki_func_ret','compile.py',363),
  ('shiki -> ID KAKKO KOKKA','shiki',3,'p_shiki_call_void','compile.py',369),
  ('bun -> TYPE TYPE LBRACE letlist RBRACE SEMI','bun',6,'p_lets','compile.py',375),
  ('bun -> GLOBAL TYPE LBRACE letlist RBRACE SEMI','bun',6,'p_letsglobal','compile.py',381),
  ('letlist -> ID EQUALS STR SEMI','letlist',4,'p_letslis','compile.py',387),
  ('letlist -> ID EQUALS NUMBER SEMI','letlist',4,'p_letslis','compile.py',388),
  ('letlist -> letlist ID EQUALS STR SEMI','letlist',5,'p_letslis','compile.py',389),
  ('letlist -> letlist ID EQUALS NUMBER SEMI','letlist',5,'p_letslis','compile.py',390),
  ('bun -> ID EQUALS ID OPTASU STR SEMI','bun',6,'p_str_add','compile.py',399),
  ('bun -> ID EQUALS STR OPTASU ID SEMI','bun',6,'p_str_add','compile.py',400),
  ('bun -> ID OPTASU OPTASU SEMI','bun',4,'p_add_add_num','compile.py',406),
  ('bun -> STR OPTASU OPTASU SEMI','bun',4,'p_add_add_num','compile.py',407),
]
