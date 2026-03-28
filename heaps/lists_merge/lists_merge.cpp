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

ListNode *mergeSortedLists(vector<ListNode *> &lists)
{ // LeetCode Q.23.
    // Min heap. Format: {value, its linked list idx}.
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;

    vector<ListNode *> listsNodes;
    for (int idx = 0; idx < lists.size(); idx++)
    {
        if (lists[idx] != nullptr)
            minHeap.push({lists[idx]->val, idx});

        listsNodes.push_back(lists[idx]);
    }

    vector<int> sortedValues;

    while (!minHeap.empty())
    {
        auto [value, listIdx] = minHeap.top();
        sortedValues.push_back(value);
        minHeap.pop();

        if (listsNodes[listIdx]->next != nullptr)
        {
            listsNodes[listIdx] = listsNodes[listIdx]->next;
            minHeap.push({listsNodes[listIdx]->val, listIdx});
        }
    }

    if (sortedValues.empty())
        return nullptr;

    ListNode *sortedList = new ListNode(sortedValues[0]);
    ListNode *currentNode = sortedList;

    for (size_t idx = 1; idx < sortedValues.size(); idx++)
    {
        currentNode->next = new ListNode(sortedValues[idx]);
        currentNode = currentNode->next;
    }

    return sortedList;
}
