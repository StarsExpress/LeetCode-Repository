#include <vector>
#include <unordered_set>
#include <unordered_map>
using namespace std;

class PeopleWithSecret
{ // LeetCode Q.2092.
private:
    unordered_set<int> secret_set;
    unordered_map<int, int> parents;

    int find_parent(int person)
    {
        if (person == parents[person])
        {
            return person;
        }
        return find_parent(parents[person]);
    }

    void union_people(int person_1, int person_2)
    {
        int parent_1 = find_parent(person_1);
        int parent_2 = find_parent(person_2);
        if (secret_set.find(parent_1) != secret_set.end())
        {
            parents[parent_2] = parent_1;
        }
        else
        {
            parents[parent_1] = parent_2;
        }
    }

public:
    vector<int> find_aware_people(int n, vector<vector<int>> &meetings, int first_person)
    {
        secret_set = {0, first_person};

        sort(
            meetings.begin(), meetings.end(),
            [](const vector<int> &a, const vector<int> &b)
            {
                return a[2] > b[2]; // Sort by decending meeting time at idx 2.
            });

        while (!meetings.empty())
        {
            int meeting_time = meetings.back()[2]; // Current meeting time.
            while (!meetings.empty() && meetings.back()[2] == meeting_time)
            {
                for (auto person : {meetings.back()[0], meetings.back()[1]})
                {
                    if (parents.find(person) == parents.end())
                    {
                        parents[person] = person;
                    }
                }
                union_people(meetings.back()[0], meetings.back()[1]);
                meetings.pop_back(); // A lot faster than erase.
            }

            for (const auto &pair : parents)
            {
                if (secret_set.find(find_parent(pair.second)) != secret_set.end())
                {
                    secret_set.insert(pair.first); // Knows secret at this meeting time.
                }
            }
            parents.clear(); // Reset for the next meeting time.
        }

        return vector<int>(secret_set.begin(), secret_set.end()); // Must return vector.
    }
};