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

    int findParent(int person)
    {
        if (parents[person] == person)
            return person;

        return findParent(parents[person]);
    }

    void unionPeople(int personOne, int personTwo)
    {
        int parentOne = findParent(min(personOne, personTwo));
        int parentTwo = findParent(max(personOne, personTwo));

        if (parentOne != parentTwo)
        {
            parents[parentTwo] = parentOne;

            // Must merge parent 2's restricted people into parent 1's.
            forbidden[parentOne].insert(
                forbidden[parentTwo].begin(), forbidden[parentTwo].end());

            forbidden.erase(parentTwo); // Clear unused memory.
        }
    }

public:
    vector<bool> processRequests(int n, vector<vector<int>> &restrictions, vector<vector<int>> &requests)
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

        vector<bool> requestsResults;

        for (auto request : requests)
        {
            int parentOne = findParent(request[0]);
            int parentTwo = findParent(request[1]);
            bool requestSuccess = true; // Default to True.

            for (auto forbidden_person : forbidden[parentOne]) // Test parent 1.
            {
                if (findParent(forbidden_person) == parentTwo)
                {
                    requestSuccess = false;
                    break;
                }
            }

            if (requestSuccess) // Test parent 2.
            {
                for (auto forbidden_person : forbidden[parentTwo])
                {
                    if (findParent(forbidden_person) == parentOne)
                    {
                        requestSuccess = false;
                        break;
                    }
                }
            }

            requestsResults.push_back(requestSuccess);
            if (requestSuccess)
                unionPeople(parentOne, parentTwo);
        }

        return requestsResults;
    }
};