#include <string>
#include <unordered_map>
using namespace std;

string find_min_substring(string mother_str, string target_str)
{ // LeetCode Q.76.
    int total_uncovered_chars = target_str.size();
    unordered_map<char, int> chars2counts;
    for (int idx = 0; idx < target_str.size(); idx++)
        chars2counts[target_str[idx]]++;

    string min_substring = "";
    int substring_start_idx = -1, min_len = numeric_limits<int>::max();

    int left_idx = 0;
    for (int right_idx = 0; right_idx < mother_str.size(); right_idx++)
    {
        char right_char = mother_str[right_idx];
        if (chars2counts.find(right_char) != chars2counts.end())
        {
            if (chars2counts[right_char] > 0)
                total_uncovered_chars--;
            chars2counts[right_char]--;

            while (total_uncovered_chars == 0)
            {
                int substring_len = right_idx + 1 - left_idx;
                if (substring_len < min_len)
                {
                    min_len = substring_len, substring_start_idx = left_idx;
                }

                if (chars2counts.find(mother_str[left_idx]) != chars2counts.end())
                {
                    if (chars2counts[mother_str[left_idx]] == 0)
                    {
                        break;
                    }
                    chars2counts[mother_str[left_idx]]++;
                }
                left_idx++;
            }
        }
    }

    if (substring_start_idx != -1)
        min_substring += mother_str.substr(substring_start_idx, min_len);
    return min_substring;
}
