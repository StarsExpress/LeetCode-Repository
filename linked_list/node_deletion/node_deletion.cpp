#include <iostream>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

void delete_node(ListNode *node) // LeetCode Q.237.
{
    node->val = node->next->val;
    node->next = node->next->next;
}
