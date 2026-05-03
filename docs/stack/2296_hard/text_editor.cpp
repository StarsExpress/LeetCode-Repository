#include <vector>
#include <deque>
#include <string>
using namespace std;

class TextEditor // LeetCode Q.2296.
{
private:
    deque<char> cursorLeftSide, cursorRightSide;

    string sliceCursorLeftTail()
    {
        string text = "";

        int startIdx = 0;
        if (cursorLeftSide.size() > 10)
            startIdx += cursorLeftSide.size() - 10;

        for (int idx = startIdx; idx < cursorLeftSide.size(); idx++)
            text += cursorLeftSide[idx];

        return text;
    }

public:
    TextEditor() {}

    void addText(string text)
    {
        for (auto letter : text)
            cursorLeftSide.push_back(letter);
    }

    int deleteText(int k)
    {
        int deletionsCount = cursorLeftSide.size();
        if (k < deletionsCount)
            deletionsCount = k;

        while (k > 0 && !cursorLeftSide.empty())
        {
            cursorLeftSide.pop_back();
            k--;
        }

        return deletionsCount;
    }

    string cursorLeft(int k)
    {
        while (k > 0 && !cursorLeftSide.empty())
        {
            char letter = cursorLeftSide.back();
            cursorRightSide.push_front(letter);
            cursorLeftSide.pop_back();
            k--;
        }

        return sliceCursorLeftTail();
    }

    string cursorRight(int k)
    {
        while (k > 0 && !cursorRightSide.empty())
        {
            char letter = cursorRightSide.front();
            cursorLeftSide.push_back(letter);
            cursorRightSide.pop_front();
            k--;
        }

        return sliceCursorLeftTail();
    }
};