#include <bitset>
#include <unordered_map>
#include <string>
using namespace std;

class NonB2BOnesCounter
{ // LeetCode Q.600.
private:
    // Base case: num = 0 or 1.
    unordered_map<int, int> non_b2b_ones_counts = {{0, 1}, {1, 2}};

public:
    int count_non_b2b_ones(int num)
    {
        if (non_b2b_ones_counts.find(num) != non_b2b_ones_counts.end())
        {
            return non_b2b_ones_counts[num];
        }

        bitset<32> num_bin_set(num);
        string num_bin_str = num_bin_set.to_string();

        size_t first_1_idx = num_bin_str.find('1');
        size_t second_1_idx = string::npos;
        second_1_idx = num_bin_str.find('1', first_1_idx + 1);

        int query_num = pow(2, num_bin_str.length() - 1 - first_1_idx) - 1;
        non_b2b_ones_counts[num] = count_non_b2b_ones(query_num);

        if (second_1_idx == string::npos) // Num has just one 1 bit.
        {
            non_b2b_ones_counts[num] += 1; // Min num at num's bin level.
            return non_b2b_ones_counts[num];
        }

        if (first_1_idx + 1 == second_1_idx)
        { // Must reduce 1 level.
            query_num = pow(2, num_bin_str.length() - 1 - second_1_idx) - 1;
        }
        else
        {
            query_num = stoi(num_bin_str.substr(second_1_idx), nullptr, 2);
        }

        non_b2b_ones_counts[num] += count_non_b2b_ones(query_num);
        return non_b2b_ones_counts[num];
    }
};
