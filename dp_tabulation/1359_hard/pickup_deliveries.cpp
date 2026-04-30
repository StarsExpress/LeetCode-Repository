#include <cmath>
using namespace std;

int countValidSequences(int totalOrders) // LeetCode Q.1359.
{
    long long modulo = pow(10, 9) + 7; // Long long prevents overflow.

    // Base case when n is 1: pickup 1 followed by delivery 1.
    long long validSequences = 1;

    for (int prevOrderNum = 1; prevOrderNum <= totalOrders - 1; prevOrderNum++)
    {
        int spotsCount = 2 * prevOrderNum + 1;

        // Sum from 1 to spots count.
        int multiple = spotsCount * (spotsCount + 1) / 2;

        validSequences *= multiple;
        validSequences %= modulo;
    }

    return validSequences;
}
