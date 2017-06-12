#include <iostream>
#include <stdlib.h>
 
using namespace std;
 
int main()
{
    const string training_data = "training_data.zip";
    const string syscmd = "zipinfo -1 " + training_data;
    // print zip information
    system(syscmd.c_str());

    return 0;
}