#include <vector>
#include <numeric>
using namespace std;

vector<int> replace_non_coprimes(vector<int> &nums)
{ // LeetCode Q.2197.
    vector<int> non_corime_nums;
    for (auto num : nums)
    {
        while (!non_corime_nums.empty())
        {
            int greatest_common_divisor = gcd(num, non_corime_nums.back());
            if (greatest_common_divisor == 1)
            {
                break;
            }
            num *= non_corime_nums.back() / greatest_common_divisor;
            non_corime_nums.pop_back();
        }
        non_corime_nums.push_back(num);
    }
    return non_corime_nums;
}
