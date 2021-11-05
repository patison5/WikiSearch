#include "Lexer.h"

Lexer::Lexer() {}

Lexer::~Lexer() {}

list<string> Lexer::get_lexem(string text) {
    char text_arr[text.length() + 1];
    strcpy(text_arr, text.c_str());
    char * lexem = strtok (text_arr," ,.-?");

    list<string> result;

    while (lexem != NULL)                         // пока есть лексемы
    {
        string str = lexem;
        lexem = strtok (NULL, " ,.-?!");
        result.push_back(str);
    }
    return result;
}

