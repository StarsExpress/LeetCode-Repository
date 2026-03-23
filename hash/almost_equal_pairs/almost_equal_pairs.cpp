#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <deque>
using namespace std;

int countAlmostEqualPairs(vector<int> &nums)
{ // LeetCode Q.3267.
    // Each num's transformed nums set.
    unordered_map<int, unordered_set<int>> newNumsTable;
    unordered_map<int, double> oldNums2Counts, newNums2Counts;

    deque<int> queue;
    unordered_set<int> newNums;

    for (auto num : nums)
    {
        oldNums2Counts[num]++;

        if (newNumsTable.find(num) == newNumsTable.end())
        {
            queue.push_back(num);

            int rounds = 2;
            while (rounds > 0)
            {
                int transformations = queue.size();

                while (transformations > 0)
                {
                    int newNum = queue.front();
                    queue.pop_front();

                    string newNumStr = to_string(newNum);
                    int newNumLen = newNumStr.length();

                    for (int back_idx = 0; back_idx < newNumLen - 1; back_idx++)
                    {
                        for (int front_idx = back_idx + 1; front_idx < newNumLen; front_idx++)
                        {
                            swap(newNumStr[back_idx], newNumStr[front_idx]);

                            newNum = stoi(newNumStr);
                            if (newNum != num && newNums.find(newNum) == newNums.end())
                            {
                                newNums.insert(newNum); // Only take real new nums.
                                queue.push_back(newNum);
                            }

                            swap(newNumStr[back_idx], newNumStr[front_idx]);
                        }
                    }

                    transformations--;
                }

                rounds--;
            }

            newNumsTable[num] = newNums;
            queue.clear(); // Reset for future usage.
            newNums.clear();
        }

        int numLen = to_string(num).length();

        for (auto newNum : newNumsTable[num])
        {
            newNums2Counts[newNum]++;
            if (to_string(newNum).length() == numLen)
                newNums2Counts[newNum] -= 0.5;
        }
    }

    double almost_equal_pairs = 0.0;
    for (auto &pair : oldNums2Counts)
        almost_equal_pairs += pair.second * (pair.second - 1) / 2;

    for (auto num : nums)
        almost_equal_pairs += newNums2Counts[num];

    return int(almost_equal_pairs); // Return int form.
}
