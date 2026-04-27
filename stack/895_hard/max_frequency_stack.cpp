#include <unordered_map>
#include <stack>
#include <vector>
using namespace std;

class MaxFrequencyStack // LeetCode Q.895.
{
private:
    // Each idx contains stack of values with frequency = idx + 1.
    vector<stack<int>> frequencyStack;

    unordered_map<int, int> valuesFrequencies;

public:
    MaxFrequencyStack() {}

    void push(int value)
    {
        valuesFrequencies[value]++;
        int frequency = valuesFrequencies[value];

        // Need to add another stack for current frequency.
        if (frequency > frequencyStack.size())
            frequencyStack.push_back({});

        frequencyStack[frequency - 1].push(value);
    }

    int pop()
    {
        int mostFreqValue = frequencyStack.back().top();
        valuesFrequencies[mostFreqValue]--;

        frequencyStack.back().pop();
        if (frequencyStack.back().empty())
            frequencyStack.pop_back();

        return mostFreqValue;
    }
};