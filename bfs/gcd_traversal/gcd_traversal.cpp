#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>
using namespace std;

class GCDTraversal
{ // LeetCode Q.2709.
private:
    unordered_map<int, unordered_set<int>> graph;

    vector<int> find_distinct_primes(int num)
    {
        unordered_set<int> primes;
        while (num % 2 == 0)
        {
            num /= 2;
            if (graph.find(2) == graph.end())
                graph[2] = {};

            if (primes.find(2) == primes.end())
                primes.insert(2);
        }

        for (int divisor = 3; divisor * divisor <= num; divisor += 2)
            while (num % divisor == 0)
            {
                num /= divisor;
                if (graph.find(divisor) == graph.end())
                    graph[divisor] = {};

                if (primes.find(divisor) == primes.end())
                    primes.insert(divisor);
            }

        if (num > 2)
        { // If original num itself is a prime.
            if (graph.find(num) == graph.end())
                graph[num] = {};

            if (primes.find(num) == primes.end())
                primes.insert(num);
        }

        return vector<int>(primes.begin(), primes.end());
    }

public:
    bool verify_traversal(vector<int> &nums)
    {
        if (nums.size() == 1) // Base case.
            return true;

        queue<int> queue;
        for (auto num : nums)
        {
            if (num == 1) // Base case: GCD of any num and 1 doesn't exceed 1.
                return false;

            vector<int> primes = find_distinct_primes(num);
            if (queue.size() == 0) // Prepare any prime into queue as BFS start.
                queue.push(primes[0]);

            for (int idx = 0; idx < primes.size() - 1; idx++)
            {
                graph[primes[idx]].insert(primes[idx + 1]);
                graph[primes[idx + 1]].insert(primes[idx]);
            }
        }

        unordered_set<int> visited_primes;
        while (!queue.empty())
        {
            int prime = queue.front();
            visited_primes.insert(prime);
            queue.pop();

            for (auto neighbor_prime : graph[prime])
            {
                if (visited_primes.find(neighbor_prime) == visited_primes.end())
                    queue.push(neighbor_prime);
            }
        }

        if (visited_primes.size() < graph.size())
            return false;
        return true;
    }
};