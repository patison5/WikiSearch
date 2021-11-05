#include <iostream>
#include <vector>
#include <string>
#include <filesystem>
#include <fstream>
#include <fcntl.h>
#include <cstring>

#include "json.hpp"

#include "JSONReader.h"
#include "Lexer.h"
#include "BooleanSearch.h"

using namespace std;

using json = nlohmann::json;
using filesystem::recursive_directory_iterator;

namespace fs = filesystem;

static string CORPUS_PATH = "/mnt/d/Github/WikiSearch/habr/clean/json/";  //D:/Github/WikiSearch/habr/clean/json

int main()
{
    JSONReader jsr(CORPUS_PATH);
    Lexer lexer;
    BooleanSearch boolean_search;

    json data;

    for (const auto& file : fs::recursive_directory_iterator(CORPUS_PATH)) {
        string file_name = file.path().filename().string();
        data = jsr.get_json(file_name);


        string title = data["title"];
        string body = data["body"];

        cout << title << endl;

        list<string> title_lexems = lexer.get_lexem(title);
        list<string> boty_lexems = lexer.get_lexem(body);

        for (list<string>::iterator it = title_lexems.begin(); it != title_lexems.end(); ++it){
            cout << (*it) << ", ";
        }
        
        cout << endl;
    }

    return 0;
}