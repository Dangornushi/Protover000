#include "main.hpp"

int main( int argc, char **arg ) {

    string comp = "./proc ";
    string pyt = "./compile ";
    string name = arg[1] ;

    comp = comp + arg[1] ;
    pyt = pyt + name ;

    //system(pyt.c_str());
    string inpfilename = arg[1], data;
    ifstream ifs ( inpfilename+"s" ) ;
    ofstream ofs ( split( inpfilename, "." )[0]+".way" ) ;

    while ( getline( ifs, data ) ) {
        ofs << data << endl;
    }
    
    name = split( comp, " " )[1];
    string funcs;
    stringstream ss, ss2;
    ifstream ifs2( split( name, "." )[0]+".way", ios::in );
    ofstream ofs2 ( split( name, "." )[0], ios::out|ios::binary );
    int fc = 0;
    vector<string> impv;

    while ( getline( ifs2, data ) ) {
        if ( data.find( "call" ) != string::npos ) {
            funcs+=split( split( data, "call " )[1], "[" )[0];
        }
        if ( data.find( ":" ) != string::npos ) {
            funcs = replace( funcs, split( data, "(" )[0] );
        }
        for ( int i = 0; i < data.size();i++ ) {
            string data2 = data.substr( i, data.size()-(data.size()-1) );
            for (const auto &item : data2) {
                ss << hex << int(item);
            }
        }
    }

    ofs2 << ss.str() << flush;
    ofs2.close();
    ifs2.close();
    //system(comp.c_str());

    return 0;
}
