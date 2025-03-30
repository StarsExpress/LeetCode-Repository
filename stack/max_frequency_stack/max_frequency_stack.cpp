#include <unordered_map>
#include <stack>
#include <vector>
using namespace std;

class MaxFrequencyStack
{ // LeetCode Q.895.
private:
    unordered_map<int, int> values2freqs;
    // Each idx contains stack of values with frequency of idx + 1.
    vector<stack<int>> freqs2stacks;

public:
    MaxFrequencyStack() {}

    void push(int value)
    {
        values2freqs[value]++;
        if (values2freqs[value] > freqs2stacks.size())
        { // Need to add another stack for current frequency.
            freqs2stacks.push_back({});
        }
        freqs2stacks[values2freqs[value] - 1].push(value);
    }

    int pop()
    {
        int most_freq_value = freqs2stacks.back().top();
        values2freqs[most_freq_value]--;

        freqs2stacks.back().pop();
        if (freqs2stacks.back().empty())
        {
            freqs2stacks.pop_back();
        }

        return most_freq_value;
    }
};