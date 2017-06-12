#include "src/libzippp.h"
using namespace libzippp;

ZipArchive zf("training_data.zip");
zf.open(ZipArchive::READ_ONLY);

vector<ZipEntry> entries = zf.getEntries();
vector<ZipEntry>::iterator it;
for(it=entries.begin() ; it!=entries.end(); ++it) {
  ZipEntry entry = *it;
  string name = entry.getName();
  int size = entry.getSize();

  //the length of binaryData will be size
  void* binaryData = entry.readAsBinary();

  //the length of textData will be size
  string textData = entry.readAsText();

  //...
}

zf.close();