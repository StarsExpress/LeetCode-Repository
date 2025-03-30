#include <vector>
using namespace std;

int find_max_score(vector<int> &nums_1, vector<int> &nums_2)
{ // LeetCode Q.1537.
    // Only use modulo on max score. Can't use modulo on partial sums.
    long long max_score = 0, modulo = pow(10, 9) + 7;

    int idx_1 = 0, idx_2 = 0;
    long long sum_1 = nums_1[0], sum_2 = nums_2[0];

    while (idx_1 < nums_1.size() && idx_2 < nums_2.size())
    {
        while (nums_1[idx_1] < nums_2[idx_2])
        {
            if (idx_1 == nums_1.size() - 1)
            {
                break;
            }
            idx_1++;
            sum_1 += nums_1[idx_1];
        }
        if (nums_1[idx_1] < nums_2[idx_2])
        {
            break; // Num 1 can't catch up with num 2.
        }

        while (nums_2[idx_2] < nums_1[idx_1])
        {
            if (idx_2 == nums_2.size() - 1)
            {
                break;
            }
            idx_2++;
            sum_2 += nums_2[idx_2];
        }
        if (nums_2[idx_2] < nums_1[idx_1])
        {
            break; // Num 2 can't catch up with num 1.
        }

        if (nums_1[idx_1] == nums_2[idx_2])
        {
            max_score += max(sum_1, sum_2);
            max_score %= modulo;

            sum_1 = 0; // Reset sum 1.
            idx_1++;
            if (idx_1 < nums_1.size())
            {
                sum_1 += nums_1[idx_1];
            }

            sum_2 = 0; // Reset sum 2.
            idx_2++;
            if (idx_2 < nums_2.size())
            {
                sum_2 += nums_2[idx_2];
            }
        }
    }

    while (idx_1 < nums_1.size() - 1)
    { // Sum the rest of nums 1.
        idx_1++;
        sum_1 += nums_1[idx_1];
    }

    while (idx_2 < nums_2.size() - 1)
    { // Sum the rest of nums 2.
        idx_2++;
        sum_2 += nums_2[idx_2];
    }

    max_score += max(sum_1, sum_2);
    return max_score % modulo;
}
