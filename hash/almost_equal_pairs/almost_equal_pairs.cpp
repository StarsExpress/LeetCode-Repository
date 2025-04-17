#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <deque>
using namespace std;

int count_almost_equal_pairs(vector<int> &nums)
{ // LeetCode Q.3267.
    // Each num's transformed nums set.
    unordered_map<int, unordered_set<int>> new_nums_table;
    unordered_map<int, double> old_nums2counts, new_nums2counts;

    deque<int> queue;
    unordered_set<int> new_nums;
    for (auto num : nums)
    {
        old_nums2counts[num]++;

        if (new_nums_table.find(num) == new_nums_table.end())
        {
            queue.push_back(num);

            int rounds = 2;
            while (rounds > 0)
            {
                int transformations = queue.size();
                while (transformations > 0)
                {
                    int new_num = queue.front();
                    queue.pop_front();
                    string new_num_str = to_string(new_num);
                    int new_num_len = new_num_str.length();

                    for (int back_idx = 0; back_idx < new_num_len - 1; back_idx++)
                    {
                        for (int front_idx = back_idx + 1; front_idx < new_num_len; front_idx++)
                        {
                            swap(new_num_str[back_idx], new_num_str[front_idx]);

                            new_num = stoi(new_num_str);
                            if (new_num != num && new_nums.find(new_num) == new_nums.end())
                            {
                                new_nums.insert(new_num); // Only take real new nums.
                                queue.push_back(new_num);
                            }

                            swap(new_num_str[back_idx], new_num_str[front_idx]);
                        }
                    }

                    transformations--;
                }
                rounds--;
            }

            new_nums_table[num] = new_nums;
            queue.clear(); // Reset for future usage.
            new_nums.clear();
        }

        int num_len = to_string(num).length();
        for (auto new_num : new_nums_table[num])
        {
            new_nums2counts[new_num]++;
            if (to_string(new_num).length() == num_len)
                new_nums2counts[new_num] -= 0.5;
        }
    }

    double almost_equal_pairs = 0.0;
    for (auto &pair : old_nums2counts)
        almost_equal_pairs += pair.second * (pair.second - 1) / 2;

    for (auto num : nums)
        almost_equal_pairs += new_nums2counts[num];

    return int(almost_equal_pairs); // Return int form.
}
