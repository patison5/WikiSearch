#ifndef __LEXER_H
#define __LEXER_H

#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

class Lexer
{
    public:
        Lexer();
        ~Lexer();

        void get_lexem(string text);

    protected:

    private:
};

#endif // __LEXER_H
