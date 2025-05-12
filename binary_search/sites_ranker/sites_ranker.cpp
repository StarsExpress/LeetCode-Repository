#include <deque>
#include <string>
using namespace std;

class SitesRanker
{ // LeetCode Q.2102.
private:
    // Sorted in acending score and name. Format: {negative score, name}.
    deque<pair<int, string>> locations_scores;
    int query_calls = 0;

    static bool comparator(const pair<int, string> &a, const pair<int, string> &b)
    {
        if (a.first != b.first)
            return a.first < b.first;
        return a.second < b.second;
    }

public:
    SitesRanker() {}

    void add_site(string name, int score)
    {
        auto idx = upper_bound(
            locations_scores.begin(), locations_scores.end(),
            make_pair(-score, name), comparator);
        locations_scores.insert(idx, {-score, name});
    }

    string get_site()
    {
        query_calls++;
        return locations_scores[query_calls - 1].second;
    }
};