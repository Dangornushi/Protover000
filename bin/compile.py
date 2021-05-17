import inspect, sys
from os import device_encoding
import ply.yacc as yacc
from lex import tokens

filename = sys.argv[1]

intd = {}
strd = {}
funcd = {}

iflis = []
funclis = []
ast_2 = []

kataw = ""

iflisc = 0
ifc = 0
lisc = 0
icj = 0

precedence = (
    ('left', 'OPTASU'),
    ('left', 'OPKAKERU'),
)

def p_teigilist_0(p):
    '''
        teigilist : teigi
                | teigilist teigi
    '''
    if (len(p) == 2):
        p[0] = (p[1])
    elif (len(p) == 3):
        p[0] = (p[1],p[2])

def p_include(p):
    """
    bun : INCLUDE STR SEMI
    """
    p[0] = ("INC", p[2])

def p_paramlist(p):
    '''
        paramlist : param
                | paramlist CONMA param
    '''
    if (len(p) == 2):
        p[0] = [p[1]]
    elif (len(p) == 4):
        l = p[1]
        l.append(p[3])
        p[0] = l

def p_param(p):
    '''
        param : TYPE ID
            | TYPE
    '''
    if (len(p) == 2):
        p[0] = ('PARAM',p[1])
    elif (len(p) == 3):   
        p[0] = ('PARAM',p[1],p[2])

def p_call(p):
    '''
    bun : ID KAKKO shiki KOKKA SEMI
    '''
    p[0] = ( "CALL", p[1], p[3] )

def p_teigi_0(p):
    '''
    teigi : TYPE ID KAKKO paramlist KOKKA yaji TYPE LBRACE bunlist RBRACE
    '''
    p[0] = ('DEF',p[7],p[2],p[4],p[9])

def p_bunlist_0(p):
    '''
    bunlist : bun
    '''
    p[0] = [p[1]]

def p_bunlist_1(p):
    '''
    bunlist : bunlist bun
    '''
    l = p[1]
    l.append(p[2])
    p[0] =  l

def p_bun_type(p):
    '''
    bun : TYPE ID colon colon TYPE EQUALS NUMBER SEMI
        | TYPE ID colon colon TYPE EQUALS STR SEMI
    '''
    p[0] = ('SENGEN',p[5],p[2],p[7])

def p_bun_lis(p):
    '''
    bun : TYPE ID colon colon TYPE EQUALS LISL STR LISR SEMI
    '''
    p[0] = ( 'LISTD', p[2], p[8] )

def p_bun_deflis(p):
    """
    bun : TYPE ID colon colon TYPE EQUALS ID LISL NUMBER LISR SEMI
        | TYPE ID colon colon TYPE EQUALS ID LISL ID LISR SEMI
    """
    p[0] = ( 'LISTARG', p[2], p[7], p[9], p[5] )

def p_bun_newlis(p):
    """
    bun : TYPE ID colon colon TYPE EQUALS LISL LISR SEMI
    """
    p[0] = ( "NEWLIS", p[2])

def p_add(p):
    '''
    bun : ID EQUALS ID OPTASU NUMBER SEMI
        | ID EQUALS ID OPKAKERU NUMBER SEMI
        | ID EQUALS ID OPMIN NUMBER SEMI
        | ID EQUALS ID OPWARU NUMBER SEMI
    '''
    p[0] = ( 'DAINYU', p[1], p[3], p[4], p[5] )

def p_bun_return(p):
    '''
    bun : RETURN shiki SEMI
        | RETURN bun
    '''
    p[0] = ('RETURN',p[2])

def p_bun_if1(p):
    '''
    bun : IF hikaku LBRACE bunlist RBRACE 
    '''
    p[0] = ('IF',p[2],p[4])

def p_bun_if2(p):
    '''
    bun : IF hikaku LBRACE bunlist RBRACE ELSE LBRACE bunlist RBRACE
    '''
    p[0] = ('IF-ELSE',p[2],p[4],p[8])

def p_bun_while(p):
    '''
    bun : WHILE shiki LBRACE bunlist RBRACE 
    '''
    p[0] = ( 'WHILE', p[2], p[4] )

def p_hikaku_1(p):
    '''
    hikaku : shiki
    '''
    p[0] = ('exp',p[1])

def p_hikaku_2(p):
    '''
     hikaku : hikaku EQOP shiki
            | hikaku dainari shiki
            | hikaku syounari shiki
    '''
    p[0] = ('HIKAKU1',p[1],p[2],p[3])

def p_shiki_num(p):
    '''
    shiki : NUMBER
    '''
    p[0] = ('NUM',p[1])

def p_shiki_id(p):
    '''
    shiki : ID
    '''
    p[0] = ('ID',p[1])

def p_shiki_str(p):
    '''
    shiki : STR
    '''
    p[0] = ('STR',p[1])

def p_shiki_pass(p):
    '''
    bun : PASS 
        | PASS KAKKO KOKKA
        | PASS KAKKO PASS KOKKA SEMI
    '''
    p[0] = ('PASS',p[1])

def p_shiki_enzan(p):
    '''
        shiki : shiki OPTASU shiki
              | shiki OPKAKERU shiki
              | shiki OPMIN shiki
              | shiki OPWARU shiki
    '''
    p[0] = ('OP',p[1],p[2],p[3])

def p_shiki_kakko(p):
    '''
    shiki : KAKKO shiki KOKKA
    '''
    p[0] = ('exp',p[2])

def p_shiki_fuc(p):
    """
    shiki : ID KAKKO shiki KOKKA 
    """
    p[0] = ( "CALL", p[1], p[3] )

def p_insert(p):
    """
    bun : RESERV ID LISL NUMBER LISR EQUALS STR SEMI
        | RESERV ID LISL ID LISR EQUALS STR SEMI
        | RESERV ID LISL NUMBER LISR EQUALS ID SEMI
        | RESERV ID LISL ID LISR EQUALS ID SEMI
    """
    p[0] = ( "RES", p[1], p[2], p[4], p[7] )

def p_reserv (p):
    '''
    bun : RESERV ID SEMI
        | RESERV STR SEMI
        | RESERV NUMBER SEMI
    '''
    p[0] = ( "RES",p[1],p[2] )

def p_lets(p):
    """
    bun : TYPE TYPE LBRACE letlist RBRACE SEMI
    """
    p[0] = ( "LETS", p[2], p[4] )

def p_letslis(p):
    """ 
    letlist : ID EQUALS STR SEMI 
            | ID EQUALS NUMBER SEMI 
            | letlist ID EQUALS STR SEMI
            | letlist ID EQUALS NUMBER SEMI
    """
    if type(p[1]) != tuple: 
        p[0] = ( p[1], p[3] )
    else:
        p[0] = [ p[1], (p[2], p[4])]

def p_str_add(p):
    """
    bun : ID EQUALS ID OPTASU STR SEMI
        | ID EQUALS STR OPTASU ID SEMI
    """
    p[0] = ( "STRADD", p[1], p[3], p[5] )

def p_add_add_num(p):
    """
    bun : ID OPTASU OPTASU SEMI
        | STR OPTASU OPTASU SEMI
    """
    p[0] = ('OPSTR',p[1],p[2],p[1])

# syntax error
def p_error(p):
    print ('Syntax error %s' % p)

parser = yacc.yacc()

class CodeGenartor:
    mList = []

    global icj
    def __init__( self ):
        self.ifcj = icj

    def append(self , line):
        self.mList.append(line)
    
    def out_put( self ):
        wfile =  open ( filename+"s", "a", encoding="utf_8")
        wfile.truncate(0) 
        for item in self.mList:
            print ("".join( item), file=wfile)
    
    def add_define( self , info ):
        self.append( ["\n"+info['funcname']+':'] )
    
    def add_return( self , info ):
        self.append( ['','end;\ncb;\n'] )
        #TODO : end;cb;
        for name in iflis:
            self.if_write( name, funcd )

    def if_write( self, name, dic ):
        self.append( [ '',"\n"+name+"():" ] )
        for item in funcd[name][6:]:
            walker.step2( item )

    def add_num( self , info, arg, mode ):
        self.append( ['',"mode>"+mode+";\n"+"mov "+arg+" "+info[arg]+";" ])
    
    def add_deflis( self, arg, vall, mode, index ):
        self.append( ['',"mode>"+mode+";\n"+"mov "+arg+", "+vall+"["+index+"]"+";" ])

    def add_sym( self , arg, funcname ):
        self.append( ["ret "+funcname+", "+arg+";" ])
    
    def add_fode( self, fode ):
        self.append( [ '',"fode>"+fode+";" ] )

    def add_call ( self, name, vall ):
        self.append( [ "", "call "+name+"["+vall+"];" ] )

    def add_msg ( self, word ):
        self.append( [ "", "msg "+word+";" ])
    
    def add_input ( self, word ):
        self.append( [ "", "input "+word+";" ])

    def add_dainyu( self, ast ):
        if ast[3] == "+":
            self.append( ['','mode>int;\nadd ',ast[2],", ",ast[4],";\nmov ", ast[1], ", ", ast[2],";"] )
        
        if ast[3] == "-":
            self.append( ['','mode>int;\nsub ',ast[2],", ",ast[4],";\nmov ", ast[1], ", ", ast[2],";"] )
        
        if ast[3] == "*":
            self.append( ['','mode>int;\ndev ',ast[2],", ",ast[4],";\nmov ", ast[1], ", ", ast[2],";"] )
        
        if ast[3] == "/":
            self.append( ['','mode>int;\nmul ',ast[2],", ",ast[4],";\nmov ", ast[1], ", ", ast[2],";"] )
    
    def add_ifcall( self, word ):
        self.append( ['', word ] )
    
    def add_if ( self, name ):
        self.append( ['', name +"():\n"+funcd[name] ] )
    
    def add_while( self, loopn ):
        self.append( ['', "jmp "+str( loopn )+", L"+str( ifc )+";" ] )

    def add_vall( self, mode, data ):
        self.append( ['',"mode>"+mode+";\n"+"pop "+data+";" ] )

    def add_lis( self, ast ):
        self.append( [ '', "mode>lis;\nmov "+ast[1]+", "+ast[2]+";" ] )

    def add_insert( self, lisn, index, STR ):
        self.append( [ '', "mode>lisin;\nmov "+lisn+"["+index+"], "+STR+";" ] )



codegen = CodeGenartor()

def if_j( x, y, mode, kata ):
    if kata == "int":
        if mode == "==":
            if x in intd and y in intd and intd[x] == intd[y]:
                return 0
            elif x in intd and intd[x] == int( y ):
                return 0
            elif y in intd and intd[ y ] == int( x ):
                return 0
        elif mode == ">":
            if x in intd and y in intd and intd[x] > intd[y]:
                return 0
            elif x in intd and intd[x] > int( y ):
                return 0
            elif y in intd and intd[ y ] > int( x ):
                return 0
        elif mode == "<":
            if x in intd and y in intd and intd[x] < intd[y]:
                return 0
            elif x in intd and intd[x] < int( y ):
                return 0
            elif y in intd and intd[ y ] < int( x ):
                return 0
    elif kata == "str":
        if x[0] == "ID":
            x = strd[x[1]].replace( "\"", "'" ).replace( "' ", "" ).replace("'", "")
            y = y.replace( "\"", "'" ).replace("' ", "").replace( "'", "" )
            if x == y:
                return 0
        if y in strd:
            x = x.replace( "\"", "'" ).replace( "'", "" )
            y = strd[y].replace( "\"", "'" ).replace( "'", "" )
            if x == y:
                return 0
        else:
            return 1

class Walker:
    uniqid = 0
    frame = {}
    stack = ['']
    funcs = {}

    def walk(self,ast):
        self.step2( ast )

    def step2(self,ast):

        self.uniqid += 10
        global  funcname, mode, funclis, kataw, ifc, iflisc, lisc, ast_2, funcd
        
        if ast[0] == 'exp':
            self.step2(ast[1])
        
        elif ast[0] == 'LISTD':
            codegen.add_lis( ast )

        elif ast[0] == "PASS":
            pass

        elif ast[0] == 'DEF':

            funcname = ast[2]
            size = 0
            vallw = ""

            try:
                for item in ast[3]:
                    vallw += item[1]+item[2]
                    size+=1
            except IndexError:
                    pass
                
            funcd[ast[2]] = ast[2:]
            self.stack.append (ast[2])
            codegen.add_define({'funcname':ast[2]+"("+vallw+")", 'localvarsize':size })

            for item in ast[3]:
                self.step2(item)
            for item in ast[4]:
                self.step2(item)

            codegen.add_return({'funcname':ast[2]})
        
        elif ast[0] == 'ID':
            pass
            #codegen.add_sym( ast[1], funcname)
        
        elif ast[0] == "WHILE":
            add = []
            codegen.add_while( ast[1][1] )
            for item in ast:
                add += item
            funcd["L"+str( ifc )] = (add)
            iflis.append( "L"+str( ifc ) )
            ifc+=1

        elif ast[0] == "HIKAKU1":
            if ast[2] == "==":
                jmode = "je"
            elif ast[2] == "<":
                jmode = "ja"
            elif ast[2] == ">":
                jmode = "jne"
            ifword = jmode+" "+ast[1][1][1]+", "+ast[3][1].replace( "\" ", "\"" )+", L"+str( ifc )+";"
            codegen.add_ifcall( ifword )

        elif ast[0] == 'IF':
            add = []
            self.step2(ast[0:2][1])#TODO : HIAKAKU
            for item in ast:
                add += item
            funcd["L"+str( ifc )] = (add)
            iflis.append( "L"+str( ifc ) )
            ifc+=1

        elif ast[0] == 'DAINYU':
            codegen.add_dainyu( ast )

        elif ast[0] == "LISTARG":
            codegen.add_deflis(ast[1], ast[2], "ind", ast[3] )
        
        elif ast[0] == 'PARAM':
            try:
                if ast[1] == "int":
                    codegen.add_vall(  ast[1], ast[2] )
                
                if ast[1] == "str":
                    codegen.add_vall(  ast[1], ast[2] )
            except IndexError:
                pass

        elif ast[0] == "CALL":
            size = 0
            vallw = ""

            self.step2(ast[2])
            if ast[2][0] == "OP":
                codegen.add_call( ast[1], ast[2][1][1] )
            else:
                codegen.add_call( ast[1], ast[2][1] )

            for item in funcd[ast[1]][1] :
                if item != "void":
                    vallw += item[1]+item[2]
                else:
                    vallw += "void"
            
            #codegen.add_define({'funcname':ast[1]+"("+vallw+")", 'localvarsize':size })

        elif ast[0] == "RES":
            if ast[1] == "put":
                codegen.add_msg( ast[2] )
                codegen.add_msg( "\"\\n\"" )
            elif ast[1] == "msg":
                codegen.add_msg( ast[2] )
            elif ast[1] == "input":
                codegen.add_input( ast[2] )
            elif ast[1] == "insert":
                codegen.add_insert( ast[2], ast[3], ast[4] )

        elif ast[0] == 'SENGEN':
            mode = ast[1]
            if mode == "int":
                intd[ast[2]] = int( ast[3] )
            if mode == "str":
                strd[ast[2]] = ast[3]
            codegen.add_num({ast[2]:ast[3]}, ast[2], ast[1])

        elif ast[0] == 'RETURN':
            self.step2( ast[1] )
            if type( ast[1][1] ) == tuple:
                codegen.add_sym( ast[1][1][1], funcname )
            else:
                codegen.add_sym( ast[1][1], funcname )
        
        elif ast[0] == "OP":
            item = ast[1:]
            for item2 in item:
                self.step2(item2)
            if ast[2] == "+":
                op = "add "

            elif ast[2] == "-":
                op = "sub "
            
            elif ast[2] == "*":
                op = "dev "
            
            elif ast[2] == "/":
                op = "mull "
            codegen.append( [ op+ast[1][1]+", "+ast[3][1]+";" ] )

        elif ast[0] == "OPSTR":
            codegen.append( [ "add "+ast[1]+", 1;" ] )

        elif ast[0] == "NEWLIS":
            codegen.add_lis(["", ast[1], "\"\""])

        elif ast[0] == "LETS":
            for msd in ast[2]:
                item = ( "SENGEN", ast[1], msd[0], msd[1] )
                self.step2(item)

        elif ast[0] == "STRADD":
            codegen.append( [ "stradd "+ast[2]+", "+ast[3]+";\nmov "+ast[1]+", "+ast[2]+";" ] )

walker = Walker()


if __name__ == '__main__':  
    file = open ( filename, "r", encoding="utf_8" ).read()
    for i in range ( len( file.split( "fn" ) ) ):
        if file.split("fn")[i] != "":
            result = parser.parse("fn"+file.split("fn")[i])
            walker.walk(result)
            codegen.out_put()
