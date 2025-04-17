#include <vector>
#include <queue>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode *merge_sorted_lists(vector<ListNode *> &lists)
{ // LeetCode Q.23.
    // Min heap. Format: {value, its linked list idx}.
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> min_heap;

    vector<ListNode *> lists_nodes;
    for (int idx = 0; idx < lists.size(); idx++)
    {
        if (lists[idx] != nullptr)
        {
            min_heap.push({lists[idx]->val, idx});
        }

        lists_nodes.push_back(lists[idx]);
    }

    vector<int> sorted_values;
    while (!min_heap.empty())
    {
        auto [value, list_idx] = min_heap.top();
        sorted_values.push_back(value);
        min_heap.pop();
        if (lists_nodes[list_idx]->next != nullptr)
        {
            lists_nodes[list_idx] = lists_nodes[list_idx]->next;
            min_heap.push({lists_nodes[list_idx]->val, list_idx});
        }
    }

    if (sorted_values.empty())
        return nullptr;

    ListNode *sorted_list = new ListNode(sorted_values[0]);
    ListNode *current_node = sorted_list;
    for (size_t idx = 1; idx < sorted_values.size(); idx++)
    {
        current_node->next = new ListNode(sorted_values[idx]);
        current_node = current_node->next;
    }
    return sorted_list;
}
