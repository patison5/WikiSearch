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

void JSONReader::get_lexem(string text) {
    char text_arr[text.length() + 1];
    strcpy(text_arr, text.c_str());
    char * lexem = strtok (text_arr," ,.-?");

    while (lexem != NULL)                         // пока есть лексемы
    {
        cout << lexem  << " - ";
        lexem = strtok (NULL, " ,.-?");
    }

    cout << endl;
}