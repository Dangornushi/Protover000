
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOPTASUleftOPKAKERUAPPEND CLASS CONMA ELSE EQOP EQUALS GLOBAL ID IF INCLUDE INLINE KAKKO KOKKA LAMDA LBRACE LEN LISL LISR LIST NUMBER OPKAKERU OPMIN OPTASU OPWARU PASS PIRIOD QOT RBRACE RESERV RETURN SEMI STR STRUCT TYPE TYPEF WHILE colon dainari syounari yaji\n        teigilist : teigi\n                | teigilist teigi\n    \n        paramlist : param\n                  | paramlist CONMA param\n    \n        param : TYPE ID\n              | TYPE\n    \n    bun : ID EQUALS LAMDA KAKKO paramlist KOKKA LBRACE bunlist RBRACE SEMI\n    \n    bun : ID KAKKO shiki KOKKA SEMI\n    \n    bun : INLINE KAKKO shiki KOKKA SEMI\n    \n    teigi : STR\n    \n    bun : ID EQUALS ID SEMI\n    \n    teigi : TYPE ID KAKKO paramlist KOKKA yaji TYPE LBRACE bunlist RBRACE\n    \n    teigi : TYPE ID yaji TYPE LBRACE bunlist RBRACE\n    \n    teigi : STRUCT ID LBRACE teigilist RBRACE\n    \n    class : classf\n    \n    class : class classf\n    \n    teigi : CLASS ID LBRACE class RBRACE\n    \n    teigi : INCLUDE LBRACE shiki RBRACE\n    \n    classf : ID KAKKO paramlist KOKKA yaji TYPE LBRACE bunlist RBRACE\n    \n    bun : ID PIRIOD ID KAKKO shiki KOKKA SEMI\n    \n    bun : PASS SEMI\n    \n    bunlist : bun\n    \n    bunlist : bunlist bun\n    \n    bun : TYPE ID EQUALS shiki SEMI\n    \n    bun : TYPE ID EQUALS LISL shiki LISR SEMI\n    \n    bun : TYPE ID EQUALS ID LISL NUMBER LISR SEMI\n    \n    bun : ID EQUALS LISL LISR SEMI\n    \n    bun : ID EQUALS ID OPTASU NUMBER SEMI\n        | ID EQUALS ID OPKAKERU NUMBER SEMI\n        | ID EQUALS ID OPMIN NUMBER SEMI\n        | ID EQUALS ID OPWARU NUMBER SEMI\n    \n    shiki : TYPEF KAKKO shiki KOKKA\n    \n    shiki : TYPE KAKKO shiki KOKKA\n    \n    shiki : RESERV KAKKO shiki KOKKA\n    \n    bun : RETURN shiki SEMI\n        | RETURN bun\n    \n    bun : IF hikaku LBRACE bunlist RBRACE \n    \n    bun : IF hikaku LBRACE bunlist RBRACE ELSE LBRACE bunlist RBRACE\n    \n    bun : WHILE shiki LBRACE bunlist RBRACE \n    \n    hikaku : shiki\n    \n     hikaku : hikaku EQOP shiki\n            | hikaku dainari shiki\n            | hikaku syounari shiki\n    \n    shiki : NUMBER\n    \n    shiki : ID\n    \n    shiki : TYPE\n    \n    shiki : STR\n    \n    bun : PASS \n        | PASS KAKKO KOKKA\n        | PASS KAKKO PASS KOKKA SEMI\n    \n    shiki : LEN KAKKO shiki KOKKA\n    \n    bun : ID LISL shiki LISR EQUALS shiki SEMI\n    \n    shiki : OPMIN NUMBER\n    \n    shiki : shiki CONMA shiki\n    \n    shiki : shiki OPTASU shiki\n          | shiki OPKAKERU shiki\n          | shiki OPMIN shiki\n          | shiki OPWARU shiki\n    \n    shiki : KAKKO shiki KOKKA\n    \n    shiki : shiki CONMA ID       \n    \n    bun : RESERV ID LISL NUMBER LISR EQUALS STR SEMI\n        | RESERV ID LISL ID LISR EQUALS STR SEMI\n        | RESERV ID LISL NUMBER LISR EQUALS ID SEMI\n        | RESERV ID LISL ID LISR EQUALS ID SEMI\n    \n    bun : RESERV KAKKO shiki KOKKA SEMI\n    \n    shiki : ID KAKKO shiki KOKKA\n    \n    shiki : ID KAKKO KOKKA\n    \n    shiki : ID LISL shiki LISR\n    \n    bun :  TYPE LBRACE letlist RBRACE SEMI\n    \n    bun : GLOBAL TYPE LBRACE letlist RBRACE SEMI\n     \n    letlist : ID EQUALS STR SEMI \n            | ID EQUALS NUMBER SEMI \n            | letlist ID EQUALS STR SEMI\n            | letlist ID EQUALS NUMBER SEMI\n    \n    bun : ID EQUALS ID OPTASU STR SEMI\n        | ID EQUALS STR OPTASU ID SEMI\n    \n    bun : ID OPTASU OPTASU SEMI\n        | STR OPTASU OPTASU SEMI\n    '
    
_lr_action_items = {'STR':([0,1,2,3,8,12,15,19,31,35,36,37,38,39,40,41,43,44,45,46,47,52,53,55,75,76,78,79,80,81,95,96,98,100,101,102,103,106,115,119,120,133,134,135,136,137,138,139,140,141,142,148,151,154,155,156,164,166,172,176,180,183,184,185,187,188,197,199,201,202,203,207,208,211,213,220,221,222,223,224,226,230,231,232,233,235,238,239,240,241,247,248,249,250,251,252,253,255,256,],[3,3,-1,-10,-2,24,3,24,3,-18,24,24,24,24,24,24,24,24,24,24,24,83,-14,-17,83,-22,-48,110,24,24,126,24,24,-13,-23,24,-21,-36,24,83,24,-49,-35,24,24,24,83,24,24,24,83,83,24,189,-11,192,24,-77,83,83,-78,-12,24,-24,-69,216,-27,-8,24,-9,-50,-37,-39,-65,83,-28,-75,-29,-30,-31,-76,243,245,-70,83,-25,83,-20,-52,83,-26,83,83,-64,-62,-63,-61,-38,-7,]),'TYPE':([0,1,2,3,8,12,13,14,15,19,31,35,36,37,38,39,40,41,43,44,45,46,47,51,52,53,54,55,71,75,76,78,79,80,81,84,96,98,100,101,102,103,106,115,119,120,133,134,135,136,137,138,139,140,141,142,147,148,151,155,160,164,166,172,176,180,183,184,185,187,197,199,201,202,203,207,208,211,213,220,221,222,223,224,226,232,233,235,238,239,240,241,247,248,249,250,251,252,253,255,256,],[4,4,-1,-10,-2,20,27,30,4,20,4,-18,20,20,20,20,20,20,20,20,20,20,20,27,73,-14,27,-17,92,73,-22,-48,107,20,20,117,20,20,-13,-23,20,-21,-36,20,73,20,-49,-35,20,20,20,73,20,20,20,73,182,73,20,-11,27,20,-77,73,73,-78,-12,20,-24,-69,-27,-8,20,-9,-50,-37,-39,-65,73,-28,-75,-29,-30,-31,-76,-70,73,-25,73,-20,-52,73,-26,73,73,-64,-62,-63,-61,-38,-7,]),'STRUCT':([0,1,2,3,8,15,31,35,53,55,100,183,],[5,5,-1,-10,-2,5,5,-18,-14,-17,-13,-12,]),'CLASS':([0,1,2,3,8,15,31,35,53,55,100,183,],[6,6,-1,-10,-2,6,6,-18,-14,-17,-13,-12,]),'INCLUDE':([0,1,2,3,8,15,31,35,53,55,100,183,],[7,7,-1,-10,-2,7,7,-18,-14,-17,-13,-12,]),'$end':([1,2,3,8,35,53,55,100,183,],[0,-1,-10,-2,-18,-14,-17,-13,-12,]),'RBRACE':([2,3,8,17,20,22,23,24,31,33,34,35,48,53,55,56,57,58,59,60,61,62,64,68,75,76,78,86,87,88,89,90,91,100,101,103,106,121,133,134,148,155,166,172,176,180,181,183,185,187,197,199,202,203,207,208,211,218,219,220,221,222,223,224,226,232,233,235,236,237,239,240,246,247,248,249,250,251,252,253,255,256,],[-1,-10,-2,35,-46,-44,-45,-47,53,55,-15,-18,-53,-14,-17,-16,-54,-45,-55,-56,-57,-58,-59,-67,100,-22,-48,-32,-33,-34,-66,-68,-51,-13,-23,-21,-36,152,-49,-35,183,-11,-77,207,208,-78,212,-12,-24,-69,-27,-8,-9,-50,-37,-39,-65,-71,-72,-28,-75,-29,-30,-31,-76,-70,246,-25,-73,-74,-20,-52,-19,-26,254,255,-64,-62,-63,-61,-38,-7,]),'ID':([4,5,6,12,16,19,27,33,34,36,37,38,39,40,41,43,44,45,46,47,52,56,73,75,76,78,79,80,81,82,94,95,96,97,98,101,102,103,106,107,108,115,119,120,121,133,134,135,136,137,138,139,140,141,142,143,146,148,151,155,162,164,166,172,176,180,181,184,185,187,197,199,201,202,203,207,208,211,213,218,219,220,221,222,223,224,226,230,231,232,233,235,236,237,238,239,240,241,246,247,248,249,250,251,252,253,255,256,],[9,10,11,23,32,23,49,32,-15,58,23,23,23,23,23,23,23,23,23,23,74,-16,93,74,-22,-48,109,23,23,114,122,123,23,128,23,-23,23,-21,-36,93,114,23,74,149,153,-49,-35,23,23,23,74,23,23,23,74,177,122,74,23,-11,198,23,-77,74,74,-78,153,23,-24,-69,-27,-8,23,-9,-50,-37,-39,-65,74,-71,-72,-28,-75,-29,-30,-31,-76,242,244,-70,74,-25,-73,-74,74,-20,-52,74,-19,-26,74,74,-64,-62,-63,-61,-38,-7,]),'LBRACE':([7,10,11,20,22,23,24,30,48,57,58,59,60,61,62,64,68,73,86,87,88,89,90,91,92,107,111,112,113,117,173,174,175,182,225,229,],[12,15,16,-46,-44,-45,-47,52,-53,-54,-45,-55,-56,-57,-58,-59,-67,94,-32,-33,-34,-66,-68,-51,119,94,138,-40,142,146,-41,-42,-43,213,238,241,]),'KAKKO':([9,12,18,19,20,21,23,25,32,36,37,38,39,40,41,43,44,45,46,47,58,74,77,78,79,80,81,82,96,98,102,107,108,109,115,120,124,128,135,136,137,139,140,141,149,151,164,184,201,],[13,19,41,19,43,44,45,47,54,19,19,19,19,19,19,19,19,19,19,19,45,96,102,104,19,19,19,115,19,19,19,43,135,136,19,19,160,164,19,19,19,19,19,19,45,19,19,19,19,]),'yaji':([9,50,118,],[14,71,147,]),'TYPEF':([12,19,36,37,38,39,40,41,43,44,45,46,47,79,80,81,96,98,102,115,120,135,136,137,139,140,141,151,164,184,201,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'RESERV':([12,19,36,37,38,39,40,41,43,44,45,46,47,52,75,76,78,79,80,81,96,98,101,102,103,106,115,119,120,133,134,135,136,137,138,139,140,141,142,148,151,155,164,166,172,176,180,184,185,187,197,199,201,202,203,207,208,211,213,220,221,222,223,224,226,232,233,235,238,239,240,241,247,248,249,250,251,252,253,255,256,],[21,21,21,21,21,21,21,21,21,21,21,21,21,82,82,-22,-48,108,21,21,21,21,-23,21,-21,-36,21,82,21,-49,-35,21,21,21,82,21,21,21,82,82,21,-11,21,-77,82,82,-78,21,-24,-69,-27,-8,21,-9,-50,-37,-39,-65,82,-28,-75,-29,-30,-31,-76,-70,82,-25,82,-20,-52,82,-26,82,82,-64,-62,-63,-61,-38,-7,]),'NUMBER':([12,19,26,36,37,38,39,40,41,43,44,45,46,47,79,80,81,96,98,102,115,120,135,136,137,139,140,141,143,151,154,156,157,158,159,164,184,188,201,],[22,22,48,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,178,22,190,191,193,194,195,22,214,217,22,]),'LEN':([12,19,36,37,38,39,40,41,43,44,45,46,47,79,80,81,96,98,102,115,120,135,136,137,139,140,141,151,164,184,201,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'OPMIN':([12,17,19,20,22,23,24,36,37,38,39,40,41,42,43,44,45,46,47,48,57,58,59,60,61,62,63,64,65,66,67,68,69,70,79,80,81,86,87,88,89,90,91,96,98,102,105,107,109,110,112,113,115,120,123,127,129,131,135,136,137,139,140,141,144,149,150,151,164,169,170,171,173,174,175,184,186,200,201,204,205,206,214,228,],[26,39,26,-46,-44,-45,-47,26,26,26,26,26,26,39,26,26,26,26,26,-53,39,-45,-55,-56,39,39,39,-59,39,39,39,-67,39,39,26,26,26,-32,-33,-34,-66,-68,-51,26,26,26,39,-46,-45,-47,39,39,26,26,158,39,39,39,26,26,26,26,26,26,39,-45,39,26,26,39,39,39,39,39,39,26,39,39,26,-34,-66,-68,-44,39,]),'CONMA':([17,20,22,23,24,27,28,29,42,48,49,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,85,86,87,88,89,90,91,105,107,109,110,112,113,127,129,131,144,149,150,169,170,171,173,174,175,186,196,200,204,205,206,214,228,],[36,-46,-44,-45,-47,-6,51,-3,36,-53,-5,36,-45,-55,-56,36,36,36,-59,36,36,36,-67,36,36,-4,51,-32,-33,-34,-66,-68,-51,36,-46,-45,-47,36,36,36,36,36,36,-45,36,36,36,36,36,36,36,36,51,36,-34,-66,-68,-44,36,]),'OPTASU':([17,20,22,23,24,42,48,57,58,59,60,61,62,63,64,65,66,67,68,69,70,74,83,86,87,88,89,90,91,99,105,107,109,110,112,113,116,123,126,127,129,131,144,149,150,169,170,171,173,174,175,186,200,204,205,206,214,228,],[37,-46,-44,-45,-47,37,-53,37,-45,-55,-56,37,37,37,-59,37,37,37,-67,37,37,99,116,-32,-33,-34,-66,-68,-51,130,37,-46,99,116,37,37,145,156,162,37,37,37,37,-45,37,37,37,37,37,37,37,37,37,-34,-66,-68,-44,37,]),'OPKAKERU':([17,20,22,23,24,42,48,57,58,59,60,61,62,63,64,65,66,67,68,69,70,86,87,88,89,90,91,105,107,109,110,112,113,123,127,129,131,144,149,150,169,170,171,173,174,175,186,200,204,205,206,214,228,],[38,-46,-44,-45,-47,38,-53,38,-45,38,-56,38,38,38,-59,38,38,38,-67,38,38,-32,-33,-34,-66,-68,-51,38,-46,-45,-47,38,38,157,38,38,38,38,-45,38,38,38,38,38,38,38,38,38,-34,-66,-68,-44,38,]),'OPWARU':([17,20,22,23,24,42,48,57,58,59,60,61,62,63,64,65,66,67,68,69,70,86,87,88,89,90,91,105,107,109,110,112,113,123,127,129,131,144,149,150,169,170,171,173,174,175,186,200,204,205,206,214,228,],[40,-46,-44,-45,-47,40,-53,40,-45,-55,-56,40,40,40,-59,40,40,40,-67,40,40,-32,-33,-34,-66,-68,-51,40,-46,-45,-47,40,40,159,40,40,40,40,-45,40,40,40,40,40,40,40,40,40,-34,-66,-68,-44,40,]),'KOKKA':([20,22,23,24,27,28,29,42,45,48,49,57,58,59,60,61,62,63,64,65,66,67,68,70,72,85,86,87,88,89,90,91,104,127,131,132,136,144,169,170,196,200,],[-46,-44,-45,-47,-6,50,-3,64,68,-53,-5,-54,-45,-55,-56,-57,-58,86,-59,87,88,89,-67,91,-4,118,-32,-33,-34,-66,-68,-51,133,163,167,168,68,179,204,205,225,227,]),'LISR':([20,22,23,24,48,57,58,59,60,61,62,64,68,69,86,87,88,89,90,91,125,129,171,177,178,186,214,],[-46,-44,-45,-47,-53,-54,-45,-55,-56,-57,-58,-59,-67,90,-32,-33,-34,-66,-68,-51,161,165,206,209,210,215,234,]),'SEMI':([20,22,23,24,48,57,58,59,60,61,62,64,68,78,86,87,88,89,90,91,105,107,109,110,123,130,145,149,150,152,161,163,167,168,179,189,190,191,192,193,194,195,198,204,205,206,212,215,216,217,227,228,234,242,243,244,245,254,],[-46,-44,-45,-47,-53,-54,-45,-55,-56,-57,-58,-59,-67,103,-32,-33,-34,-66,-68,-51,134,-46,-45,-47,155,166,180,-45,185,187,197,199,202,203,211,218,219,220,221,222,223,224,226,211,199,-68,232,235,236,237,239,240,247,250,251,252,253,256,]),'EQOP':([20,22,23,24,48,57,58,59,60,61,62,64,68,86,87,88,89,90,91,111,112,173,174,175,],[-46,-44,-45,-47,-53,-54,-45,-55,-56,-57,-58,-59,-67,-32,-33,-34,-66,-68,-51,139,-40,-41,-42,-43,]),'dainari':([20,22,23,24,48,57,58,59,60,61,62,64,68,86,87,88,89,90,91,111,112,173,174,175,],[-46,-44,-45,-47,-53,-54,-45,-55,-56,-57,-58,-59,-67,-32,-33,-34,-66,-68,-51,140,-40,-41,-42,-43,]),'syounari':([20,22,23,24,48,57,58,59,60,61,62,64,68,86,87,88,89,90,91,111,112,173,174,175,],[-46,-44,-45,-47,-53,-54,-45,-55,-56,-57,-58,-59,-67,-32,-33,-34,-66,-68,-51,141,-40,-41,-42,-43,]),'LISL':([23,58,74,95,109,114,120,149,],[46,46,98,125,137,143,151,184,]),'INLINE':([52,75,76,78,79,101,103,106,119,133,134,138,142,148,155,166,172,176,180,185,187,197,199,202,203,207,208,211,213,220,221,222,223,224,226,232,233,235,238,239,240,241,247,248,249,250,251,252,253,255,256,],[77,77,-22,-48,77,-23,-21,-36,77,-49,-35,77,77,77,-11,-77,77,77,-78,-24,-69,-27,-8,-9,-50,-37,-39,-65,77,-28,-75,-29,-30,-31,-76,-70,77,-25,77,-20,-52,77,-26,77,77,-64,-62,-63,-61,-38,-7,]),'PASS':([52,75,76,78,79,101,103,104,106,119,133,134,138,142,148,155,166,172,176,180,185,187,197,199,202,203,207,208,211,213,220,221,222,223,224,226,232,233,235,238,239,240,241,247,248,249,250,251,252,253,255,256,],[78,78,-22,-48,78,-23,-21,132,-36,78,-49,-35,78,78,78,-11,-77,78,78,-78,-24,-69,-27,-8,-9,-50,-37,-39,-65,78,-28,-75,-29,-30,-31,-76,-70,78,-25,78,-20,-52,78,-26,78,78,-64,-62,-63,-61,-38,-7,]),'RETURN':([52,75,76,78,79,101,103,106,119,133,134,138,142,148,155,166,172,176,180,185,187,197,199,202,203,207,208,211,213,220,221,222,223,224,226,232,233,235,238,239,240,241,247,248,249,250,251,252,253,255,256,],[79,79,-22,-48,79,-23,-21,-36,79,-49,-35,79,79,79,-11,-77,79,79,-78,-24,-69,-27,-8,-9,-50,-37,-39,-65,79,-28,-75,-29,-30,-31,-76,-70,79,-25,79,-20,-52,79,-26,79,79,-64,-62,-63,-61,-38,-7,]),'IF':([52,75,76,78,79,101,103,106,119,133,134,138,142,148,155,166,172,176,180,185,187,197,199,202,203,207,208,211,213,220,221,222,223,224,226,232,233,235,238,239,240,241,247,248,249,250,251,252,253,255,256,],[80,80,-22,-48,80,-23,-21,-36,80,-49,-35,80,80,80,-11,-77,80,80,-78,-24,-69,-27,-8,-9,-50,-37,-39,-65,80,-28,-75,-29,-30,-31,-76,-70,80,-25,80,-20,-52,80,-26,80,80,-64,-62,-63,-61,-38,-7,]),'WHILE':([52,75,76,78,79,101,103,106,119,133,134,138,142,148,155,166,172,176,180,185,187,197,199,202,203,207,208,211,213,220,221,222,223,224,226,232,233,235,238,239,240,241,247,248,249,250,251,252,253,255,256,],[81,81,-22,-48,81,-23,-21,-36,81,-49,-35,81,81,81,-11,-77,81,81,-78,-24,-69,-27,-8,-9,-50,-37,-39,-65,81,-28,-75,-29,-30,-31,-76,-70,81,-25,81,-20,-52,81,-26,81,81,-64,-62,-63,-61,-38,-7,]),'GLOBAL':([52,75,76,78,79,101,103,106,119,133,134,138,142,148,155,166,172,176,180,185,187,197,199,202,203,207,208,211,213,220,221,222,223,224,226,232,233,235,238,239,240,241,247,248,249,250,251,252,253,255,256,],[84,84,-22,-48,84,-23,-21,-36,84,-49,-35,84,84,84,-11,-77,84,84,-78,-24,-69,-27,-8,-9,-50,-37,-39,-65,84,-28,-75,-29,-30,-31,-76,-70,84,-25,84,-20,-52,84,-26,84,84,-64,-62,-63,-61,-38,-7,]),'EQUALS':([74,93,109,122,153,165,206,209,210,],[95,120,95,154,188,201,201,230,231,]),'PIRIOD':([74,109,],[97,97,]),'LAMDA':([95,],[124,]),'ELSE':([207,],[229,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'teigilist':([0,15,],[1,31,]),'teigi':([0,1,15,31,],[2,8,2,8,]),'shiki':([12,19,36,37,38,39,40,41,43,44,45,46,47,79,80,81,96,98,102,115,120,135,136,137,139,140,141,151,164,184,201,],[17,42,57,59,60,61,62,63,65,66,67,69,70,105,112,113,127,129,131,144,150,169,170,171,173,174,175,186,200,69,228,]),'paramlist':([13,54,160,],[28,85,196,]),'param':([13,51,54,160,],[29,72,29,29,]),'class':([16,],[33,]),'classf':([16,33,],[34,56,]),'bunlist':([52,119,138,142,213,238,241,],[75,148,172,176,233,248,249,]),'bun':([52,75,79,119,138,142,148,172,176,213,233,238,241,248,249,],[76,101,106,76,76,76,101,101,101,76,101,76,76,101,101,]),'hikaku':([80,],[111,]),'letlist':([94,146,],[121,181,]),}

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
  ('bun -> INLINE KAKKO shiki KOKKA SEMI','bun',5,'p_bun_inline','compile.py',87),
  ('teigi -> STR','teigi',1,'p_comment','compile.py',93),
  ('bun -> ID EQUALS ID SEMI','bun',4,'p_instance','compile.py',99),
  ('teigi -> TYPE ID KAKKO paramlist KOKKA yaji TYPE LBRACE bunlist RBRACE','teigi',10,'p_teigi_0','compile.py',105),
  ('teigi -> TYPE ID yaji TYPE LBRACE bunlist RBRACE','teigi',7,'p_teigi_void','compile.py',111),
  ('teigi -> STRUCT ID LBRACE teigilist RBRACE','teigi',5,'p_teigi_1','compile.py',117),
  ('class -> classf','class',1,'p_class_f','compile.py',123),
  ('class -> class classf','class',2,'p_class_f_2','compile.py',129),
  ('teigi -> CLASS ID LBRACE class RBRACE','teigi',5,'p_class','compile.py',135),
  ('teigi -> INCLUDE LBRACE shiki RBRACE','teigi',4,'p_include','compile.py',141),
  ('classf -> ID KAKKO paramlist KOKKA yaji TYPE LBRACE bunlist RBRACE','classf',9,'p_classfunc','compile.py',147),
  ('bun -> ID PIRIOD ID KAKKO shiki KOKKA SEMI','bun',7,'p_class_fc','compile.py',153),
  ('bun -> PASS SEMI','bun',2,'p_pass','compile.py',159),
  ('bunlist -> bun','bunlist',1,'p_bunlist_0','compile.py',165),
  ('bunlist -> bunlist bun','bunlist',2,'p_bunlist_1','compile.py',171),
  ('bun -> TYPE ID EQUALS shiki SEMI','bun',5,'p_bun_type','compile.py',179),
  ('bun -> TYPE ID EQUALS LISL shiki LISR SEMI','bun',7,'p_bun_lis','compile.py',186),
  ('bun -> TYPE ID EQUALS ID LISL NUMBER LISR SEMI','bun',8,'p_bun_deflis','compile.py',192),
  ('bun -> ID EQUALS LISL LISR SEMI','bun',5,'p_bun_newlis','compile.py',198),
  ('bun -> ID EQUALS ID OPTASU NUMBER SEMI','bun',6,'p_add','compile.py',204),
  ('bun -> ID EQUALS ID OPKAKERU NUMBER SEMI','bun',6,'p_add','compile.py',205),
  ('bun -> ID EQUALS ID OPMIN NUMBER SEMI','bun',6,'p_add','compile.py',206),
  ('bun -> ID EQUALS ID OPWARU NUMBER SEMI','bun',6,'p_add','compile.py',207),
  ('shiki -> TYPEF KAKKO shiki KOKKA','shiki',4,'p_shiki_type','compile.py',214),
  ('shiki -> TYPE KAKKO shiki KOKKA','shiki',4,'p_shiki_int','compile.py',220),
  ('shiki -> RESERV KAKKO shiki KOKKA','shiki',4,'p_shiki_input','compile.py',226),
  ('bun -> RETURN shiki SEMI','bun',3,'p_bun_return','compile.py',232),
  ('bun -> RETURN bun','bun',2,'p_bun_return','compile.py',233),
  ('bun -> IF hikaku LBRACE bunlist RBRACE','bun',5,'p_bun_if1','compile.py',239),
  ('bun -> IF hikaku LBRACE bunlist RBRACE ELSE LBRACE bunlist RBRACE','bun',9,'p_bun_if2','compile.py',245),
  ('bun -> WHILE shiki LBRACE bunlist RBRACE','bun',5,'p_bun_while','compile.py',251),
  ('hikaku -> shiki','hikaku',1,'p_hikaku_1','compile.py',257),
  ('hikaku -> hikaku EQOP shiki','hikaku',3,'p_hikaku_2','compile.py',263),
  ('hikaku -> hikaku dainari shiki','hikaku',3,'p_hikaku_2','compile.py',264),
  ('hikaku -> hikaku syounari shiki','hikaku',3,'p_hikaku_2','compile.py',265),
  ('shiki -> NUMBER','shiki',1,'p_shiki_num','compile.py',271),
  ('shiki -> ID','shiki',1,'p_shiki_id','compile.py',277),
  ('shiki -> TYPE','shiki',1,'p_shiki_void','compile.py',283),
  ('shiki -> STR','shiki',1,'p_shiki_str','compile.py',289),
  ('bun -> PASS','bun',1,'p_shiki_pass','compile.py',295),
  ('bun -> PASS KAKKO KOKKA','bun',3,'p_shiki_pass','compile.py',296),
  ('bun -> PASS KAKKO PASS KOKKA SEMI','bun',5,'p_shiki_pass','compile.py',297),
  ('shiki -> LEN KAKKO shiki KOKKA','shiki',4,'p_shiki_len','compile.py',303),
  ('bun -> ID LISL shiki LISR EQUALS shiki SEMI','bun',7,'p_bun_append','compile.py',309),
  ('shiki -> OPMIN NUMBER','shiki',2,'p_shiki_MINNUM','compile.py',315),
  ('shiki -> shiki CONMA shiki','shiki',3,'p_shiki_conma','compile.py',321),
  ('shiki -> shiki OPTASU shiki','shiki',3,'p_shiki_enzan','compile.py',330),
  ('shiki -> shiki OPKAKERU shiki','shiki',3,'p_shiki_enzan','compile.py',331),
  ('shiki -> shiki OPMIN shiki','shiki',3,'p_shiki_enzan','compile.py',332),
  ('shiki -> shiki OPWARU shiki','shiki',3,'p_shiki_enzan','compile.py',333),
  ('shiki -> KAKKO shiki KOKKA','shiki',3,'p_shiki_kakko','compile.py',339),
  ('shiki -> shiki CONMA ID','shiki',3,'p_shiki_args','compile.py',345),
  ('bun -> RESERV ID LISL NUMBER LISR EQUALS STR SEMI','bun',8,'p_bun_insert','compile.py',354),
  ('bun -> RESERV ID LISL ID LISR EQUALS STR SEMI','bun',8,'p_bun_insert','compile.py',355),
  ('bun -> RESERV ID LISL NUMBER LISR EQUALS ID SEMI','bun',8,'p_bun_insert','compile.py',356),
  ('bun -> RESERV ID LISL ID LISR EQUALS ID SEMI','bun',8,'p_bun_insert','compile.py',357),
  ('bun -> RESERV KAKKO shiki KOKKA SEMI','bun',5,'p_bun_reserv','compile.py',363),
  ('shiki -> ID KAKKO shiki KOKKA','shiki',4,'p_shiki_func_ret','compile.py',369),
  ('shiki -> ID KAKKO KOKKA','shiki',3,'p_shiki_call_void','compile.py',375),
  ('shiki -> ID LISL shiki LISR','shiki',4,'p_shiki_list','compile.py',381),
  ('bun -> TYPE LBRACE letlist RBRACE SEMI','bun',5,'p_lets','compile.py',387),
  ('bun -> GLOBAL TYPE LBRACE letlist RBRACE SEMI','bun',6,'p_letsglobal','compile.py',393),
  ('letlist -> ID EQUALS STR SEMI','letlist',4,'p_letslis','compile.py',399),
  ('letlist -> ID EQUALS NUMBER SEMI','letlist',4,'p_letslis','compile.py',400),
  ('letlist -> letlist ID EQUALS STR SEMI','letlist',5,'p_letslis','compile.py',401),
  ('letlist -> letlist ID EQUALS NUMBER SEMI','letlist',5,'p_letslis','compile.py',402),
  ('bun -> ID EQUALS ID OPTASU STR SEMI','bun',6,'p_str_add','compile.py',411),
  ('bun -> ID EQUALS STR OPTASU ID SEMI','bun',6,'p_str_add','compile.py',412),
  ('bun -> ID OPTASU OPTASU SEMI','bun',4,'p_add_add_num','compile.py',418),
  ('bun -> STR OPTASU OPTASU SEMI','bun',4,'p_add_add_num','compile.py',419),
]
