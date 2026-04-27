#include <string>
#include <queue>
#include <unordered_map>
using namespace std;

string reorganizeString(string originalString) // LeetCode Q.767.
{
    unordered_map<char, int> charsCounts;

    for (char character : originalString)
        charsCounts[character]++;

    priority_queue<pair<int, char>> maxHeap; // Format: {count, char}.

    for (const auto &[character, count] : charsCounts)
        maxHeap.push({count, character});

    string reshapedString = "";

    while (maxHeap.size() > 1)
    {
        auto [topOneCount, topOneChar] = maxHeap.top();
        maxHeap.pop();

        auto [topTwoCount, topTwoChar] = maxHeap.top();
        maxHeap.pop();

        reshapedString += topOneChar;
        reshapedString += topTwoChar;

        if (topOneCount > 1)
            maxHeap.push({topOneCount - 1, topOneChar});

        if (topTwoCount > 1)
            maxHeap.push({topTwoCount - 1, topTwoChar});
    }

    if (!maxHeap.empty())
    {
        if (maxHeap.top().first > 1)
            return "";

        reshapedString += maxHeap.top().second;
    }

    return reshapedString;
}
