#include <vector>
using namespace std;

int count_min_swaps(vector<int> &row) // LeetCode Q.765.
{
    vector<int> people2seats(row.size(), 0);
    vector<vector<int>> seats2people(row.size() / 2, vector<int>());

    for (int idx = 0; idx < row.size(); idx++)
    {
        int seat = idx / 2, person = row[idx];
        people2seats[person] = seat;
        seats2people[seat].push_back(person);
    }

    int min_swaps = 0;

    for (auto person : row)
    {
        int couple = person;
        if (person % 2 == 0)
            couple++; // Person is even: couple must + 1.
        else
            couple--; // Person is odd: couple must - 1.

        if (people2seats[person] != people2seats[couple])
        { // Must swap.
            min_swaps++;

            int seat_1 = people2seats[person], other_seat_1_person = person;

            for (auto member : seats2people[seat_1])
            {
                if (member != person)
                    other_seat_1_person = member;
            }

            int seat_2 = people2seats[couple], other_seat_2_person = couple;

            for (auto member : seats2people[seat_2])
            {
                if (member != couple)
                    other_seat_2_person = member;
            }

            people2seats[couple] = seat_1;
            people2seats[other_seat_1_person] = seat_2;

            seats2people[seat_1] = {person, couple};
            seats2people[seat_2] = {other_seat_1_person, other_seat_2_person};
        }
    }

    return min_swaps;
}
