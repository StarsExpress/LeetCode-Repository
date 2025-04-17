#include <vector>
#include <deque>
#include <string>
using namespace std;

class TextEditor
{ // LeetCode Q.2296.
private:
    vector<char> cursor_left_chars; // Stack based. Chars at cursor's left.
    deque<char> cursor_right_chars; // Queue based. Chars at cursor's right.

public:
    TextEditor() {}

    void add_text(string text)
    {
        for (auto character : text)
            cursor_left_chars.push_back(character);
    }

    int delete_text(int k)
    {
        int total_left_chars = cursor_left_chars.size();
        int total_deletions = min(k, total_left_chars);
        for (int deletions = total_deletions; deletions > 0; deletions--)
            cursor_left_chars.pop_back();
        return total_deletions;
    }

    string move_cursor_left(int k)
    {
        while (k > 0 && !cursor_left_chars.empty())
        {
            cursor_right_chars.push_front(cursor_left_chars.back());
            cursor_left_chars.pop_back();
            k -= 1;
        }

        int total_left_chars = cursor_left_chars.size();
        int str_min_idx = max(total_left_chars - 10, 0);
        string cursor_left_string = "";
        for (int idx = str_min_idx; idx < total_left_chars; idx++)
            cursor_left_string += cursor_left_chars[idx];
        return cursor_left_string;
    }

    string move_cursor_right(int k)
    {
        while (k > 0 && !cursor_right_chars.empty())
        {
            cursor_left_chars.push_back(cursor_right_chars.front());
            cursor_right_chars.pop_front();
            k -= 1;
        }

        int total_left_chars = cursor_left_chars.size();
        int str_min_idx = max(total_left_chars - 10, 0);
        string cursor_left_string = "";
        for (int idx = str_min_idx; idx < total_left_chars; idx++)
            cursor_left_string += cursor_left_chars[idx];
        return cursor_left_string;
    }
};