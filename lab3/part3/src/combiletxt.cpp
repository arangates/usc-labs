#include <fstream>
#include <sstream>
#include <string>
using namespace std;
int main()
{
    ofstream out("outputfile.txt");
    string line;
    for (int i=1; i<5; i++) {
        stringstream filename;
        filename << i << ".txt";
        ifstream in( filename.str().c_str() );
        while (getline(in, line)) {
            out << line << "\n";
        }
    }
    return 0;
}