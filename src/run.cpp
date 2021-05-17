#include "main.hpp"

//2531.0,275,696.0
//-5861.3, 2.5, -1503.9
//Proro Mk.0
//VM

int qoc = 0;
map<string, map<string, string> > scop;
map<string, map<string, int> > scopint;
map<string, int> intvall;
map <string, string> strvall;
vector<string> funcnames;

void VM ( map<string, string> func, string funcname, int loopj ) {
    vector<string> vec = split( func[funcname], "3b" ), vec2, vec3;
    map <string, string> strin;
    string vdata, ans, a, b, mode, fode, anser;
    stringstream ss, ss2;

    int y, x, popc=-1, callc=0;

    funcnames.push_back(funcname);

    for ( int i = 0; i < vec.size(); i++ ) {
        vdata = vec[i];
        if ( vdata != "" ) {
            vdata = regex_replace( vdata, regex( "5c6e" ), "5c" );
            
            if ( strpri( vdata ).find( "stradd " ) != string::npos ) {
                string base = split( strpri( vdata ), "stradd " )[1];
                string x = split( base, ", " )[0];
                string y = split( strpri( vdata ), "stradd "+x+", " )[1];
                if ( keyfind( strvall, x ) ) {
                    if ( strvall[ x ].find( "\"" ) != string::npos ) {
                        strvall[ x ] = split( strvall[ x ], "\"" )[1]+split( y, "\"" )[1];
                    }
                    else{
                        strvall[ x ] = strvall[ x ]+split( y, "\"" )[1];
                    }
                }
            }
            
            else
            if ( vdata.find( "61646420" ) != string::npos ) {
                string mark = "616464" ;
                string base = replace( vdata, "61646420" );
                string ans = strpri( split( base, "2c20" )[0] );
                string vall = strpri( split( base, "2c20" )[1] );
                int a = intvall[ans];    
                intvall[ans] = a + atoi( vall.c_str() );
            }
            
            else
            if ( strpri(vdata).find( "sub " ) != string::npos ) {
                // TODO : This is sub / [-]
                string base = split( strpri( vdata ), "sub ")[1] ;
                string ans = split( base, "," )[0] ;
                string vall = split( base, "," )[1] ;
                int a = intvall[ans];
                intvall[ans] = a - atoi( vall.c_str() );
            }
            
            else
            if ( vdata.find( "6d756c20" ) != string::npos ) {
                string mark = "6d756c";
                string base = replace( vdata, "6d756c20" );
                string ans = strpri( split( base, "2c20" )[0] );
                string vall = strpri( split( base, "2c20" )[1] );
                int a = intvall[ans];
                intvall[ans] = intvall[ans] / atoi( vall.c_str() );
            }
            
            else
            if ( vdata.find( "6d736720" ) != string::npos ) {
                //TODO:msg
                if ( strpri( vdata ).find( "\"" ) != string::npos ) {
                    cout << regex_replace ( strpri( split( vdata, "6d736720" )[1] ), regex( "\"" ), "" ) << flush;
                }
                
                else
                if ( keyfind( strvall, strpri( split( vdata, "6d736720" )[1] )  ) ) {
                    cout << strvall[ strpri( split( vdata, "6d736720" )[1] ) ] << flush;
                }
                
                else {
                    cout << intvall[ strpri( split( vdata, "6d736720" )[1] ) ] << flush;
                }
            }

            else
            if ( vdata.find( "6d6f7620" ) != string::npos ) {
                /*
                TODO : This is mov
                */
                string ans = split( split( strpri(vdata), "mov " )[1], " " )[0] ;
                string a = split( strpri( vdata), "mov "+ans+" " )[1];
                string data = a;
                if( mode == "int" ) {
                    if ( intkeyfind ( intvall, data ) ) {
                        intvall[ans] = intvall[ data ];
                    }
                    else {
                        intvall[ans] = atoi( data.c_str() );
                    }
                }
                else
                if ( mode == "str" ) {
                    strvall[ans] = data;
                }
                else
                if ( mode == "ind" ) {
                    ans = split( ans, "," )[0];
                    if ( intkeyfind( intvall, split ( split( data, "[" )[1], "]" )[0] ) ) {
                        strvall[ ans ] = split (  strvall [ split( data, "[" )[0] ], "\", \"" ) [ intvall [ split ( split( data, "[" )[1], "]" )[0] ]  ];
                    }
                    else {
                        strvall[ ans ] = regex_replace( split (  strvall [ split( data, "[" )[0] ], "\", \"" ) [atoi( split ( split( data, "[" )[1], "]" )[0].c_str() )], regex( "\"" ), "" ) ;
                    }
                }
                else
                if ( mode == "lis" ) {
                    ans = split( ans, "," )[0];
                    strvall[ans] = split( strpri( vdata ), "mov "+ans+", " )[1] ;
                }
                else
                if ( mode == "lisin" ) {
                    string word = split ( split( strpri( vdata ), "mov " )[1], "[" ) [0];
                    string a = split( strvall [ word ], " ,  " )[ atoi( split( split ( strpri( vdata ), "[" )[1], "]" )[0].c_str())];
                    string arg = split ( strpri( vdata ), ",  " )[1];
                    if ( keyfind( strvall, arg ) ) {
                        strvall [ word ] = split( strvall [ word ], a )[0] + " " + strvall[ arg ] + " , " + a + split( strvall [ word ], a )[1] ;
                    }
                    else {
                        strvall [ word ] = split( strvall [ word ], a )[0] + " " + arg + " , " + a + split( strvall [ word ], a )[1] ;
                    }
                }
                scopint[funcname] = intvall;
            }

            else
            if ( vdata.find( "696e70757420" ) != string::npos ) {
                // TODO : This is input
                string inpw;
                if ( strpri( vdata ).find( ", " ) == string::npos ) {
                    cin >> inpw;
                    strvall[ strpri( split(vdata, "20")[1]) ] = inpw;
                }
            }
            
            else
            if ( vdata.find( "6d6f64653e" ) != string::npos ) {
                if ( split( vdata, "6d6f64653e" )[1] == "696e74" ) {
                    mode = "int";
                }
                else
                if ( split( vdata, "6d6f64653e" )[1] == "737472" ) {
                    mode = "str";
                }
                else
                if ( strpri( split( vdata, "6d6f64653e" )[1] ) == "lis" ) {
                    mode = "lis";
                }
                else
                if ( strpri( split( vdata, "6d6f64653e" )[1] ) == "ind" ) {
                    mode = "ind";
                }
                else
                if ( strpri( split( vdata, "6d6f64653e" )[1] ) == "lisin" ) {
                    mode = "lisin";
                }
            }
            
            else
            if ( vdata.find( "63616c6c20" ) != string::npos ) {
                /*TODO : This is "call"
                ？　（　より前の語句のみ格納されている、つまり呼び出しには　（　より前でのみ読み読み込みされれば良い。
                ？　（　よりあとかつ　）　の前での語句のみを独自に読み取り変数の受け渡しに使用
                ？　ただしそれには呼び出し時に引数を記述しなければならない
                ？　⇨　base : callを抜き出したもともとの文字列、呼び出し文
                ？　⇨　func : 呼び出しされる関数名
                ？　⇨　 arg : 受け渡される変数名が加わる文字列
                ? -> 鍵格好の判定まで実装埋み。ここからなんで呼び出されないのか研究
                */
                string arg = split( split( vdata, "5d" )[0], "5b" )[1], arg2;
                vector<string> vec;
                if ( arg.find( "2c" ) != string::npos ) {
                    vec = split( arg, "2c" );
                    for ( int i = 0; i < vec.size(); i++ ) {
                        vec[i] = strpri(vec[i]);
                        scop[ split ( split( vdata, "5b" )[0], "63616c6c20" )[1] ] [ to_string(i) ] = strvall[ vec[i] ] ;
                        scopint[ split ( split( vdata, "5b" )[0], "63616c6c20" )[1] ] [ to_string(i) ] = intvall[ vec[i] ] ;
                    }
                }
                else {
                    arg2 = strpri( arg );
                    scop[ split ( split( vdata, "5b" )[0], "63616c6c20" )[1] ] [ to_string( callc ) ] = strvall [ arg2 ] ;
                    scopint[ split ( split( vdata, "5b" )[0], "63616c6c20" )[1] ] [ to_string( callc ) ] = intvall [ arg2 ] ;
                    callc++;
                }
                intvall = scopint[split ( split( vdata, "5b" )[0], "63616c6c20" )[1]];
                strvall = scop[split ( split( vdata, "5b" )[0], "63616c6c20" )[1]];
                VM ( func, split ( split( vdata, "5b" )[0], "63616c6c20" )[1], loopj );
            }
            
            else
            if ( vdata.find( "6a6e7020" ) != string::npos ) {
                string base, c, badata;
                base = split( vdata, "6a6e7020" )[1];
                if ( base.find( "0c20" ) != string::npos ) { c = split( base, "0c20" )[1]; }
                else { c = split( base, "2c20" )[2]; }
                badata = strpri( vdata );
                if ( intifj( badata, intvall, "jnp" ) == 1 ) {
                    VM( func, c, loopj );
                }
            }
            
            else
            if ( vdata.find( "6a6e6520" ) != string::npos ) {
                string x, y, funcname;
                if ( vdata.find( "0c20" ) == string::npos ) {
                    funcname = split ( vdata, "2c20" )[2] ;
                    x = strpri( split( split( vdata, "20" )[1], "2c")[0] );
                    y =  strpri( split( vdata, "2c20" )[1] ) ;
                }
                if ( vdata.find( "0c20" ) != string::npos ) {
                    funcname = split( vdata, "20c20" )[1] ;
                    x = strpri( split( split( vdata, "20" )[1], "2c" )[0] );
                    y = strpri( split( split( vdata, "2c2020" )[1], "020" )[0] );
                }
                if ( intvall[ x ] > atoi( y.c_str() ) ){
                    VM( func, funcname, loopj );
                }
                else
                if ( atoi(  x.c_str() ) > intvall[ y ] ) {
                    VM( func, funcname, loopj );
                }
            }

            else
            if ( vdata.find( "6a616520" ) != string::npos ) {
                /*
                ? This is "jae"
                ? a == b { func[c] }
                ? summary : if ( equal )
                ? base : base string
                */
                string base, a, c;
                base = split( vdata, "6a616520" )[1];
                a = strpri( split( base, "2c20" )[0] );
                b = strpri( split( split( base, "2c20" )[1], "0c20" )[0] );
                if ( base.find( "0c20" ) != string::npos ) { c = split( base, "0c20" )[1]; }
                else { c = split( base, "2c20" )[2]; }
                if ( intkeyfind( intvall, a ) ) {
                    if ( intkeyfind( intvall, b ) ) {
                        if ( atoi( a.c_str() ) == atoi( b.c_str() ) ) {
                            VM( func, c, loopj );
                        }
                    }
                    else 
                    if ( atoi( a.c_str() ) == intvall[b] ) {
                        VM( func, c, loopj );
                    }
                }                
            }

            else
            if ( vdata.find( "706f7020" ) != string::npos ) {
                // TODO : This is "pop"
                string arg = strpri( split( vdata, "706f7020" )[1]);
                if ( mode == "str" ) strvall [ arg ] = strvall[ to_string( popc+1 ) ];
                if ( mode == "int" ) intvall [ arg ] = intvall[ to_string( popc+1 ) ];
            }

            else
            if ( vdata.find( "72657420" ) != string::npos ) {
                // TODO : This is return ( ret )
                string base = split( vdata, "72657420" )[1];
                string funcn, arg;
                if ( vdata.find( "0c20" ) != string::npos ) {
                    funcn = split( base, "c20" )[0];
                    arg = split( base, "c20" )[1];
                }
                else {
                    funcn = split( base, "2c20" )[0];
                    arg = split( base, "2c20" )[1];
                }
                if ( fode == "int" ) {
                    intvall [ strpri( funcn ) ] = atoi( strpri( arg ).c_str() ) ;
                }
                else
                if ( fode == "str" ) {
                    strvall [ strpri( funcn ) ] = strpri( arg.c_str() ) ;
                }// TODO
                //break;
            }

            else
            if ( vdata.find( "666f64653e" ) != string::npos ) {
                fode = strpri( split( vdata, "3e" )[1] );
            }

            else
            if ( vdata.find( "6a6520" ) != string::npos ) {
                string x, y, funcname;
                if ( vdata.find( "0c20" ) == string::npos ) {
                    funcname = split ( vdata, "2c20" )[2] ;
                    x = strpri( split( split( vdata, "20" )[1], "2c")[0] );
                    y =  strpri( split( split( vdata, "2c2020" )[1], "202c20" )[0] ) ;
                }
                if ( vdata.find( "0c20" ) != string::npos ) {
                    funcname = split( vdata, "20c20" )[1] ;
                    x = strpri( split( split( vdata, "20" )[1], "2c" )[0] );
                    y = strpri( split( split( vdata, "2c2020" )[1], "020" )[0] );
                }

                if ( strvall[ x ] == y ){
                    VM( func, funcname, loopj );
                }
                else
                if ( strvall[ y ] == x ){
                    VM( func, funcname, loopj );
                }
            }

            else
            if ( vdata.find( "6a6d7020" ) != string::npos ) {
                //TODO : jmp : 6a6d702031302c204c30
                int loopj = 0;
                if ( intkeyfind( intvall, split( strpri( split( vdata, "20" )[1] ), ",")[0] ) ) {
                    loopj = intvall [ split( strpri( split( vdata, "20" )[1] ), ",")[0] ] ;
                }
                else {
                    loopj = atoi( split( strpri( split( vdata, "20" )[1] ), ",")[0].c_str() );
                }
                funcname = split( vdata, "2c20" )[1];

                if ( loopj == 1) {
                    while ( 1 ) {
                        VM( func, funcname, loopj );
                    }
                }
                else {
                    for ( int whilen = 0; whilen < loopj; whilen ++) {
                        VM( func, funcname, loopj );
                    }
                }
            }

            else
            if ( strpri( vdata ).find("ja ") != string::npos ) {
                // TODO : This is ja
                string x, y, funcname;
                if ( vdata.find( "0c20" ) == string::npos ) {
                    funcname = split ( vdata, "2c20" )[2] ;
                    x = strpri( split( split( vdata, "20" )[1], "2c")[0] );
                    y =  strpri( split( vdata, "2c20" )[1] ) ;
                }
                if ( vdata.find( "0c20" ) != string::npos ) {
                    funcname = split( vdata, "20c20" )[1] ;
                    x = strpri( split( split( vdata, "20" )[1], "2c" )[0] );
                    y = strpri( split( split( vdata, "2c2020" )[1], "020" )[0] );
                }
                if ( intvall[ x ] < atoi( y.c_str() ) ){
                    VM( func, funcname, loopj );
                }
                else
                if ( intvall[ y ] > atoi( x.c_str() ) ){
                    VM( func, funcname, loopj );
                }
            }
            
            else
            if ( strpri( vdata ) == "end") {
                intvall = scopint[ funcnames[vecindex( funcnames, funcname )-1 ] ];
                strvall = scop[ funcnames[vecindex( funcnames, funcname )-1 ] ];
            }
        }
    }
}

int main( int argc, char **arg ){
    ifstream fin( split( arg[1], "." )[0], ios::in | ios::binary );
    string funcname, data;
    vector<string> vec;
    map<string, string> func;
    map <string, string> strvall;
    map <string, int> intvall;
    int hex, loopj = 0;

    char buf[16];
    while(!fin.eof()) {
        fin.read(buf,sizeof(16));
        string data2( buf, 4 );
        data += data2;
    }
    vec = split( data, "3b" );
    for ( int i = 0; i < vec.size(); i++ ) {
        vec[i] = vec[i] + "3b";
        if ( vec[i].find("3a") != string::npos ) {
            funcname = split( vec[i], "28" )[0];
            func[funcname] += split( vec[i], "3a" )[1];
        }
        else 
        if ( vec[i] != "3b" ) {
            func[funcname] += vec[i];
        }
    }
    scop[funcname] = strvall;
    scopint[funcname] = intvall;
    VM( func, "6d61696e", loopj );
    return 0;
}