#include "JSONReader.h"

JSONReader::JSONReader(string path) {
    this -> path = path;
}

JSONReader::~JSONReader() {}

json JSONReader::get_json(string file) {
    ifstream i(this -> path + "/" + file);
    json j;
    i >> j;
    i.close();
    return j;
}