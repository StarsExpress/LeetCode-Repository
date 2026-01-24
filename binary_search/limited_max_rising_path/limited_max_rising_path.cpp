#include <vector>
#include <algorithm>
using namespace std;

int count_max_path_length(vector<vector<int>> &coordinates, int k) // LeetCode Q.3288.
{
    vector<int> k_point = coordinates[k];
    sort(
        coordinates.begin(), coordinates.end(),
        [](const vector<int> &a, const vector<int> &b)
        {
            if (a[0] != b[0])
                return a[0] < b[0];
            return a[1] > b[1];
        });

    vector<int> left_y, right_y;
    for (auto coordinate : coordinates)
    {
        int x = coordinate[0], y = coordinate[1];

        if (x < k_point[0] && y < k_point[1])
        {
            int idx = lower_bound(left_y.begin(), left_y.end(), y) - left_y.begin();

            if (idx == left_y.size())
                left_y.push_back(y);
            else
                left_y[idx] = y;
        }

        if (x > k_point[0] && y > k_point[1])
        {
            int idx = lower_bound(right_y.begin(), right_y.end(), y) - right_y.begin();

            if (idx == right_y.size())
                right_y.push_back(y);
            else
                right_y[idx] = y;
        }
    }

    return left_y.size() + 1 + right_y.size();
}
