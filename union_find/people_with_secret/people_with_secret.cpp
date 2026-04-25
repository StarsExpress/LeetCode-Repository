#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
using namespace std;

class PeopleWithSecret
{ // LeetCode Q.2092.
private:
    unordered_set<int> secretSet;
    unordered_map<int, int> parents;

    int findParent(int person)
    {
        if (person == parents[person])
            return person;

        return findParent(parents[person]);
    }

    void unionPeople(int personOne, int personTwo)
    {
        int parentOne = findParent(personOne);
        int parentTwo = findParent(personTwo);

        if (secretSet.find(parentOne) != secretSet.end())
            parents[parentTwo] = parentOne;

        else
            parents[parentOne] = parentTwo;
    }

public:
    vector<int> findAwarePeople(int n, vector<vector<int>> &meetings, int firstPerson)
    {
        secretSet = {0, firstPerson};

        sort(
            meetings.begin(), meetings.end(),
            [](const vector<int> &a, const vector<int> &b)
            {
                return a[2] > b[2]; // Sort by decending meeting time at idx 2.
            });

        while (!meetings.empty())
        {
            int meetingTime = meetings.back()[2]; // Current meeting time.

            while (!meetings.empty() && meetings.back()[2] == meetingTime)
            {
                for (auto person : {meetings.back()[0], meetings.back()[1]})
                {
                    if (parents.find(person) == parents.end())
                        parents[person] = person;
                }

                unionPeople(meetings.back()[0], meetings.back()[1]);
                meetings.pop_back(); // A lot faster than erase.
            }

            for (const auto &pair : parents)
            {
                if (secretSet.find(findParent(pair.second)) != secretSet.end())
                    secretSet.insert(pair.first); // Knows secret at this meeting time.
            }

            parents.clear(); // Reset for the next meeting time.
        }

        return vector<int>(secretSet.begin(), secretSet.end()); // Must return vector.
    }
};