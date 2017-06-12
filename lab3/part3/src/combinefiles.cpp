#include <iostream>
#include <stdlib.h>
 
using namespace std;
const string training_data = "training_data.zip";

// print zip information without deflating
int printzipinfo(){
const string syscmd = "unzip -n -l " + training_data;
system(syscmd.c_str());
return 0;
}

// int normalize(){
//     system("cat * > ../final.txt"); 
//     return 0;
// }

// int aggregate(){
//     system("cd ./tmp"); // cd into tmp directory 
//     normalize();
//     return 0;
// }

// unzip files from zip and deflate in the tmp directory
int deflate(){
    // const string syscmd = "unzip -n -j -d ./tmp " + training_data;
    system("unzip -n -j -d ./tmp training_data.zip && cd ./tmp && cat * > final.txt"); 
    // aggregate();
    return 0;
}



int main()  
{
    // printzipinfo(); // print zip information without deflating

    deflate(); // unzip files from zip and deflate in the tmp directory
    
    // system("rm -v !(\"final.txt\")"); // remove residuals after aggregation

    return 0;
}

// unzip -j filename.zip
// cat * > output.txt
// unzip -n -j -d ./finno training_data.zip && cd ./finno && cat * > final.txt
//unzip -n -j -d ./finno training_data.zip && cd ./finno && cat * > final.txt && rm -v !("final.txt")
