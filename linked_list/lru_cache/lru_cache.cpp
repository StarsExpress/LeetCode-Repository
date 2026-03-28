#include <unordered_map>
using namespace std;

struct Node
{
    int key, value;
    Node *prev;
    Node *next;

    Node(int key, int value) : key(key), value(value), prev(nullptr), next(nullptr) {}
};

class LRUCache // LeetCode Q.146.
{
private:
    int maxCapacity = 1; // Default value.
    unordered_map<int, Node *> cache;

    Node *head = new Node(-1, -1); // Initiate head and tail.
    Node *tail = new Node(-1, -1); // Don't connect them now.

    void add(Node *node)
    {
        Node *next_node = head->next;
        node->prev = head;
        head->next = node;

        node->next = next_node;
        next_node->prev = node;
    }

    void remove(Node *node)
    {
        Node *prev_node = node->prev;
        Node *next_node = node->next;
        prev_node->next = next_node;
        next_node->prev = prev_node;
    }

public:
    LRUCache(int capacity)
    {
        maxCapacity = capacity;
        head->next = tail; // Connect head and tail upon initialization.
        tail->prev = head;
    }

    int get(int key)
    {
        if (cache.find(key) == cache.end())
            return -1;

        Node *node = cache[key];
        remove(node);

        add(node);
        cache[key] = node; // Node property has changed.
        return cache[key]->value;
    }

    void put(int key, int value)
    {
        if (cache.find(key) == cache.end()) // New key coming.
        {
            if (cache.size() == maxCapacity) // Capacity is full.
            {
                int removed_key = tail->prev->key;
                cache.erase(removed_key);
                remove(tail->prev);
            }
        }
        else // Remove already existing node from current spot.
            remove(cache[key]);

        Node *node = new Node(key, value);
        add(node);
        cache[key] = node;
    }
};
