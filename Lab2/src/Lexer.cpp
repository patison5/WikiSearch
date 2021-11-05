#include "Lexer.h"

Lexer::Lexer() {}

Lexer::~Lexer() {}

list<char *> Lexer::get_lexem(string text) {
    char text_arr[text.length() + 1];
    strcpy(text_arr, text.c_str());
    char * lexem = strtok (text_arr," ,.-?");

    list<char *> result;

    while (lexem != NULL)                         // пока есть лексемы
    {
        cout << lexem  << " - ";
        lexem = strtok (NULL, " ,.-?");
        result.push_back(lexem);
    }
    cout << endl;
    return result;
}

