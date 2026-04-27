#include <vector>
#include <stack>
#include <queue>
using namespace std;

class DinnerPlatesStacks
{ // LeetCode Q.1172.
private:
    int max_capacity;
    vector<stack<int>> plates_stacks;

    // Min heap of indices of stacks that aren't full yet.
    priority_queue<int, vector<int>, greater<int>> free_stacks_heap;

public:
    DinnerPlatesStacks(int capacity)
    {
        max_capacity = capacity;
    }

    void push(int plate)
    {
        if (!free_stacks_heap.empty())
        {
            auto free_stack_idx = free_stacks_heap.top();
            if (free_stack_idx < plates_stacks.size())
            {
                plates_stacks[free_stack_idx].push(plate);
                if (plates_stacks[free_stack_idx].size() == max_capacity)
                {
                    free_stacks_heap.pop();
                }
                return;
            }

            free_stacks_heap = {}; // Reset: all free stacks exist no more.
        }

        if (plates_stacks.empty())
        { // No stacks at all.
            plates_stacks.push_back({});
        }
        if (plates_stacks.back().size() == max_capacity)
        { // Rightmost stack is full.
            plates_stacks.push_back({});
        }
        plates_stacks.back().push(plate);
    }

    int pop()
    {
        if (plates_stacks.empty())
        {
            return -1;
        }

        int plate = plates_stacks.back().top();
        plates_stacks.back().pop();
        while (!plates_stacks.empty() && plates_stacks.back().empty())
        {
            plates_stacks.pop_back(); // Drop empty rightmost stacks.
        }

        return plate;
    }

    int pop_specific_stack(int index)
    {
        if (index >= plates_stacks.size())
        {
            return -1;
        }
        if (plates_stacks[index].empty())
        {
            return -1;
        }

        if (index == plates_stacks.size() - 1)
        {
            return pop();
        }

        // Becomes not full after this pop: enter heap.
        if (plates_stacks[index].size() == max_capacity)
        {
            free_stacks_heap.push(index);
        }

        int plate = plates_stacks[index].top();
        plates_stacks[index].pop();
        return plate;
    }
};