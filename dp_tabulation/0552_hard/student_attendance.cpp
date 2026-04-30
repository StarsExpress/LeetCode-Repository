#include <vector>
#include <cmath>
using namespace std;

int countPossibilities(int recordLen) // LeetCode Q.552.
{
    long long modulo = pow(10, 9) + 7; // Long long prevents overflow.

    // Possible suffixes: "a", "p", "l", "ll".
    long long oneAbsenceSuffixA = 1;
    long long oneAbsenceSuffixP = 0, oneAbsenceSuffixL = 0, oneAbsenceSuffixLL = 0;

    // Possible suffixes: "p", "l", "ll".
    long long noAbsenceSuffixP = 1, noAbsenceSuffixL = 1;
    long long noAbsenceSuffixLL = 0;

    // Helper variables: help each day's branch counts update values.
    long long newOneAbsenceSuffixA = 0, newOneAbsenceSuffixP = 0;
    long long newOneAbsenceSuffixL = 0, newOneAbsenceSuffixLL = 0;

    long long newNoAbsenceSuffixP = 0;
    long long newNoAbsenceSuffixL = 0, newNoAbsenceSuffixLL = 0;

    for (int day = 2; day <= recordLen; day++)
    {
        // Update counts of those w/ one absence suffix "a".
        newOneAbsenceSuffixA = (noAbsenceSuffixL + noAbsenceSuffixLL + noAbsenceSuffixP) % modulo;

        // Update counts of those w/ one absence suffix "p".
        newOneAbsenceSuffixP = (oneAbsenceSuffixL + oneAbsenceSuffixLL + oneAbsenceSuffixA + oneAbsenceSuffixP) % modulo;

        // Update counts of those w/ 1 absence and suffix "l".
        newOneAbsenceSuffixL = (oneAbsenceSuffixA + oneAbsenceSuffixP) % modulo;

        // Update counts of those w/ 1 absence and suffix "ll".
        newOneAbsenceSuffixLL = oneAbsenceSuffixL;

        // Update counts of those w/o absence and has suffix "l" or "ll".
        newNoAbsenceSuffixL = noAbsenceSuffixP;
        newNoAbsenceSuffixLL = noAbsenceSuffixL;

        // Update counts of those w/o absence and has suffix "p".
        newNoAbsenceSuffixP = (noAbsenceSuffixP + noAbsenceSuffixL + noAbsenceSuffixLL) % modulo;

        // Transit updated counts.
        oneAbsenceSuffixA = newOneAbsenceSuffixA;
        oneAbsenceSuffixP = newOneAbsenceSuffixP;
        oneAbsenceSuffixL = newOneAbsenceSuffixL;
        oneAbsenceSuffixLL = newOneAbsenceSuffixLL;

        noAbsenceSuffixP = newNoAbsenceSuffixP;
        noAbsenceSuffixL = newNoAbsenceSuffixL;
        noAbsenceSuffixLL = newNoAbsenceSuffixLL;

        // Reset helper variables for next day's usage.
        newOneAbsenceSuffixA = 0, newOneAbsenceSuffixP = 0;
        newOneAbsenceSuffixL = 0, newOneAbsenceSuffixLL = 0;
        newNoAbsenceSuffixP = 0, newNoAbsenceSuffixL = 0, newNoAbsenceSuffixLL = 0;
    }

    long long validCombinations = (oneAbsenceSuffixA + oneAbsenceSuffixP + oneAbsenceSuffixL + oneAbsenceSuffixLL) % modulo;

    validCombinations += (noAbsenceSuffixP + noAbsenceSuffixL + noAbsenceSuffixLL) % modulo;

    return validCombinations % modulo;
}
