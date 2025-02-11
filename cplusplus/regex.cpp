// Draft/regex.cpp

#include <iostream>
#include <regex>
#include <string>

int main() { 

    // Specfying the targeted test and the pattren.
    std::string text = "12345";                            // Ordinary string for testing.
    std::regex pattern("\\d+");                            // Pattern for one or more digits.

    // Regex Operations.
    std::regex_match(text, pattern);                       // check the entire string matchs the patten.


    std::cout << "Done!" << "\n";
}