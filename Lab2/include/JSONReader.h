#ifndef __JSONREADER_H
#define __JSONREADER_H

#include <iostream>
#include <fstream>
#include <cstring>

#include "../json.hpp"

using namespace std;
using json = nlohmann::json;

class JSONReader
{
    public:
        int k = 12;
        JSONReader(string path);
        ~JSONReader();
        json get_json(string file);

    protected:

    private:
        string path;
};

#endif // __JSONREADER_H
