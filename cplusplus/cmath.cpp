#include <iostream>



#define _USE_MATH_DEFINES                       // Must be defined before cmath.
#include <cmath>                                // All so called math.hpp

double result;

int main()
{
    // absulot value.
    result = std::abs(-1);

    // devsion remainder.
    result = std::fmod(11, 5);

    // return e^x.
    result = std::exp(1);

    // returns the natural logarithm (base e) of x.
    result = std::log(4);

    // returns the base-10 logarithm of x.
    result = std::log10(1000);

    // square root.
    result = std::sqrt(16);

    // returns x raised to the power y (x^y).
    result = std::pow(2, 8);

    // trignometeric functions.
    result = std::sin(30);

    // round to nearest integer.
    result = std::round(5.5);   // ==> 6

    // ceil.
    result = std::ceil(2.5);    // ==> 3

    // floor.
    result = std::floor(2.5);   // ==> 2


    return 0;
}