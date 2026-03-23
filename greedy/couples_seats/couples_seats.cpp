#include <vector>
using namespace std;

int countMinSwaps(vector<int> &row) // LeetCode Q.765.
{
    vector<int> people2Seats(row.size(), 0);
    vector<vector<int>> seats2People(row.size() / 2, vector<int>());

    for (int idx = 0; idx < row.size(); idx++)
    {
        int seat = idx / 2, person = row[idx];
        people2Seats[person] = seat;
        seats2People[seat].push_back(person);
    }

    int minSwaps = 0;

    for (auto person : row)
    {
        int couple = person;

        if (person % 2 == 0)
            couple++; // Person is even: couple must + 1.

        else
            couple--; // Person is odd: couple must - 1.

        if (people2Seats[person] != people2Seats[couple])
        { // Must swap.
            minSwaps++;

            int seat_1 = people2Seats[person], otherSeat1Person = person;

            for (auto member : seats2People[seat_1])
            {
                if (member != person)
                    otherSeat1Person = member;
            }

            int seat_2 = people2Seats[couple], otherSeat2Person = couple;

            for (auto member : seats2People[seat_2])
            {
                if (member != couple)
                    otherSeat2Person = member;
            }

            people2Seats[couple] = seat_1;
            people2Seats[otherSeat1Person] = seat_2;

            seats2People[seat_1] = {person, couple};
            seats2People[seat_2] = {otherSeat1Person, otherSeat2Person};
        }
    }

    return minSwaps;
}
