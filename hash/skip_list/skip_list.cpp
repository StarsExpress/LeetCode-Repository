#include <unordered_map>
using namespace std;

class Skiplist
{ // LeetCode Q.1206.
private:
    unordered_map<int, int> nums2counts;

public:
    Skiplist() {}

    bool search(int target)
    {
        if (nums2counts.find(target) == nums2counts.end())
        {
            return false;
        }
        if (nums2counts[target] == 0)
        {
            return false;
        }
        return true;
    }

    void add(int num)
    {
        nums2counts[num]++;
    }

    bool erase(int num)
    {
        nums2counts[num]--;
        if (nums2counts[num] == -1)
        {                       // Num isn't in skiplist.
            nums2counts[num]++; // Back to 0.
            return false;
        }
        return true;
    }
};