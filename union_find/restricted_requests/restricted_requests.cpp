#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

class RestrictedFriendRequests
{ // LeetCode Q.2076.
private:
    // Each person's restricted people.
    unordered_map<int, unordered_set<int>> forbidden;
    vector<int> parents;

    int find_parent(int person)
    {
        if (parents[person] == person)
        {
            return person;
        }
        return find_parent(parents[person]);
    }

    void union_people(int person_1, int person_2)
    {
        int parent_1 = find_parent(min(person_1, person_2));
        int parent_2 = find_parent(max(person_1, person_2));
        if (parent_1 != parent_2)
        {
            parents[parent_2] = parent_1;
            // Must merge parent 2's restricted people into parent 1's.
            forbidden[parent_1].insert(
                forbidden[parent_2].begin(), forbidden[parent_2].end());
            forbidden.erase(parent_2); // Clear unused memory.
        }
    }

public:
    vector<bool> process_requests(int n, vector<vector<int>> &restrictions, vector<vector<int>> &requests)
    {
        for (int person = 0; person < n; person++)
        {
            parents.push_back(person); // Initialize each person's parent as self.
            forbidden[person] = {};    // Initialize empty set.
        }

        for (auto restriction : restrictions)
        {
            forbidden[restriction[0]].insert(restriction[1]);
            forbidden[restriction[1]].insert(restriction[0]);
        }

        vector<bool> requests_results;
        for (auto request : requests)
        {
            int parent_1 = find_parent(request[0]);
            int parent_2 = find_parent(request[1]);
            bool request_success = true; // Default to True.

            for (auto forbidden_person : forbidden[parent_1])
            { // Test parent 1.
                if (find_parent(forbidden_person) == parent_2)
                {
                    request_success = false;
                    break;
                }
            }
            if (request_success)
            { // Test parent 2.
                for (auto forbidden_person : forbidden[parent_2])
                {
                    if (find_parent(forbidden_person) == parent_1)
                    {
                        request_success = false;
                        break;
                    }
                }
            }

            requests_results.push_back(request_success);
            if (request_success)
            {
                union_people(parent_1, parent_2);
            }
        }

        return requests_results;
    }
};