#include "Lexer.h"

Lexer::Lexer() {}

Lexer::~Lexer() {}

void Lexer::get_lexem(string text) {
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

