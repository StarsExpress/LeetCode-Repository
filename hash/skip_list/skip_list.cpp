#include <unordered_map>
using namespace std;

class Skiplist
{ // LeetCode Q.1206.
private:
    unordered_map<int, int> numsCounts;

public:
    Skiplist() {}

    bool search(int target)
    {
        if (numsCounts.find(target) == numsCounts.end())
            return false;

        if (numsCounts[target] == 0)
            return false;

        return true;
    }

    void add(int num)
    {
        numsCounts[num]++;
    }

    bool erase(int num)
    {
        numsCounts[num]--;
        if (numsCounts[num] == -1) // Num isn't in skiplist.
        {
            numsCounts[num]++; // Back to 0.
            return false;
        }
        return true;
    }
};