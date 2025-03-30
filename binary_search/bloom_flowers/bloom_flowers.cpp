#include <vector>
#include <unordered_map>
using namespace std;

vector<int> count_bloom_flowers(vector<vector<int>> &flowers, vector<int> &people)
{ // LeetCode Q.2251.
    // Bloom counts keys: bloom time.
    // Fade counts keys: original fade time + 1 as fade time is inclusive.
    unordered_map<int, int> bloom_counts, fade_counts;

    for (auto flower : flowers)
    {
        int bloom_time = flower[0];
        if (bloom_counts.find(bloom_time) == bloom_counts.end())
        {
            bloom_counts[bloom_time] = 0;
        }
        bloom_counts[bloom_time] += 1;

        int fade_time = flower[1] + 1;
        if (fade_counts.find(fade_time) == fade_counts.end())
        {
            fade_counts[fade_time] = 0;
        }
        fade_counts[fade_time] += 1;
    }

    vector<int> bloom_times(bloom_counts.size());
    transform(
        bloom_counts.begin(), bloom_counts.end(), bloom_times.begin(),
        [](const auto &pair)
        { return pair.first; });
    sort(bloom_times.begin(), bloom_times.end());

    vector<int> fade_times(fade_counts.size());
    transform(
        fade_counts.begin(), fade_counts.end(), fade_times.begin(),
        [](const auto &pair)
        { return pair.first; });
    sort(fade_times.begin(), fade_times.end());

    vector<int> bloom_prefix_counts, fade_prefix_counts;

    for (auto bloom_time : bloom_times)
    {
        if (bloom_prefix_counts.empty())
        {
            bloom_prefix_counts.push_back(0);
        }
        else
        {
            bloom_prefix_counts.push_back(bloom_prefix_counts.back());
        }

        bloom_prefix_counts.back() += bloom_counts[bloom_time];
    }

    for (auto fade_time : fade_times)
    {
        if (fade_prefix_counts.empty())
        {
            fade_prefix_counts.push_back(0);
        }
        else
        {
            fade_prefix_counts.push_back(fade_prefix_counts.back());
        }
        fade_prefix_counts.back() += fade_counts[fade_time];
    }

    vector<int> full_bloom_flowers(people.size(), 0);
    for (int idx = 0; idx < people.size(); idx++)
    {
        int time = people[idx];

        // Idx of the 1st bloom time > visit time.
        int bloom_idx = upper_bound(bloom_times.begin(), bloom_times.end(), time) - bloom_times.begin();
        if (bloom_idx > 0)
        {
            full_bloom_flowers[idx] += bloom_prefix_counts[bloom_idx - 1];

            // Idx of the 1st incremented fade time > visit time.
            int fade_idx = upper_bound(fade_times.begin(), fade_times.end(), time) - fade_times.begin();
            if (fade_idx > 0)
            {
                full_bloom_flowers[idx] -= fade_prefix_counts[fade_idx - 1];
            }
        }
    }

    return full_bloom_flowers;
}
