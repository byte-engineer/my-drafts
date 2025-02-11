
// Draft/tricks.cpp
// This file explains an important tric

#include <iostream>

void swapVar()                                             // this function will swap a variables values.
{
    int a = 0;
    int b = 9;

    // Using standard library.
    std::swap(a, b);

    // Using tempruary variable.
    int temp;
    temp = a;
    a = b;
    b = temp;

    // Oprators method we will use bit-wise XOR (^).
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;
}


void wideChars() {
    // We Have to insert an "L" in front of the wide string.   
    // This method is used to deal with Wide chars like emojies.
    // We use wcout to print wide chars.
    std::wcout << L"😊" << "\n";
}


// Timer class.
#include <chrono>
using namespace std::chrono_literals;
class Timer
{
public:
    std::chrono::time_point<std::chrono::steady_clock> start;
    Timer()
    {
        start = std::chrono::high_resolution_clock::now();
    }

    ~Timer()
    {
        std::chrono::time_point<std::chrono::steady_clock> end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
        std::cout << duration.count() << "ms" << std::endl;

    }
};








int main() 
{
    swapVar();
    wideChars();
    Timer timer;
}