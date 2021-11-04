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

using namespace std;

using json = nlohmann::json;
using filesystem::recursive_directory_iterator;

namespace fs = filesystem;

static string CORPUS_PATH = "/mnt/d/Github/WikiSearch/habr/clean/json/";  //D:/Github/WikiSearch/habr/clean/json

int main()
{
    JSONReader jsr(CORPUS_PATH);
    Lexer lexer;
    json data;

    for (const auto& file : fs::recursive_directory_iterator(CORPUS_PATH)) {
        string file_name = file.path().filename().string();
        data = jsr.get_json(file_name);

        string title = data["title"];
        string body = data["body"];

        lexer.get_lexem(title);
        lexer.get_lexem(body);
    }

    return 0;
}

//  cd src/ && g++-11 -I ../include/ -c *.cpp && cd .. && g++-11 -I ./include main.cpp ./src/*.o -o main && ./main