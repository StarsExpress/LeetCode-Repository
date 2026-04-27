#include <string>
#include <stack>
using namespace std;

int count_longest_valid_length(string s) // LeetCode Q.32.
{
    stack<int> open_parentheses; // Indices of open parentheses.
    // Format: {open idx, close idx, parentheses len}.
    stack<tuple<int, int, int>> complete_parentheses;

    int longest_valid_len = 0;
    for (int idx = 0; idx < s.length(); idx++)
    {
        if (s[idx] == '(')
        {
            open_parentheses.push(idx);
            continue;
        }

        if (!open_parentheses.empty())
        {
            int open_idx = open_parentheses.top(), length = 2;
            open_parentheses.pop();

            if (!complete_parentheses.empty())
            {
                auto [prev_open_idx, prev_close_idx, prev_len] = complete_parentheses.top();
                if (open_idx < prev_open_idx && prev_close_idx < idx)
                {
                    length += prev_len;
                    complete_parentheses.pop();
                }
            }

            if (!complete_parentheses.empty())
            {
                auto [prev_open_idx, prev_close_idx, prev_len] = complete_parentheses.top();
                if (prev_close_idx + 1 == open_idx)
                {
                    open_idx = prev_open_idx;
                    length += prev_len;
                    complete_parentheses.pop();
                }
            }

            if (length > longest_valid_len)
            {
                longest_valid_len = length;
            }
            complete_parentheses.push({open_idx, idx, length});
        }
    }

    return longest_valid_len;
}
