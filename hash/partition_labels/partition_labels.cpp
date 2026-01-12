#include <unordered_map>
#include <vector>
#include <string>
using namespace std;

vector<int> partition_labels(string s) // LeetCode Q.763.
{
    unordered_map<char, int> chars2orders;
    vector<pair<int, int>> indices_pairs; // Same char's 1st and last indices pair.

    for (int idx = 0; idx < s.size(); idx++)
    {
        char character = s[idx];
        if (chars2orders.find(character) == chars2orders.end())
        {
            chars2orders[character] = chars2orders.size() + 1;
            indices_pairs.push_back({idx, idx});
        }

        int order = chars2orders[character];
        indices_pairs[order - 1].second = idx;
    }

    vector<int> partition_sizes;

    int current_size = 0;
    int current_right_idx = -1;

    for (auto [first_idx, last_idx] : indices_pairs)
    {
        if (current_right_idx < first_idx) // Start a new partition.
        {
            if (current_size > 0) // Store the latest partition.
                partition_sizes.push_back(current_size);

            current_size = last_idx + 1 - first_idx;
            current_right_idx = last_idx;
            continue;
        }

        if (last_idx > current_right_idx) // Current partition extends.
        {
            current_size += last_idx - current_right_idx;
            current_right_idx = last_idx;
        }
    }

    if (current_size > 0) // Last remaining partition.
        partition_sizes.push_back(current_size);

    return partition_sizes;
}
