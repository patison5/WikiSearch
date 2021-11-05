#!/bin/bash

BLUE='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

clear

printf "${BLUE}Starting IS Lab2${NC}\n"
printf "${BLUE}Starting compiling .h and .cpp...${NC}\n"

if cd src/ && g++-11 -I ../include/ -c *.cpp; then

    cd ..

    printf "${GREEN}Finish compiling${NC}\n"
    printf "${BLUE}Build starting...${NC}\n"

    if g++-11 -I ./include main.cpp ./src/*.o -o main; then

        printf "${GREEN}Build finished${NC}\n"
        printf "${BLUE}Running project..${NC}\n\n"

        start=$(date +%s.%N)

        if time ./main; then
            dur=$(echo "$(date +%s.%N) - $start" | bc)
        else
            printf "${RED}\n\nFailed running project.${NC}"
        fi

        rm ./src/*.o
    else
        printf "${GREEN}Finish compiling${NC}\n"
        printf "${RED}\n\nFailed building project.${NC}"
    fi

else 

    printf "${RED}\n\nFailed compiling project.${NC}"

fi

printf "\n${NC}Execution time: %.6f seconds\n\n${NC}" $dur