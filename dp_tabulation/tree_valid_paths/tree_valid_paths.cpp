#include <vector>
#include <unordered_map>
using namespace std;

class ValidPathsCounter
{
private:
    long long pathsCount = 0;

    unordered_map<int, vector<int>> tree;
    vector<int> visited;

    bool verifyPrime(int num)
    {
        if (num <= 1)
            return false; // Sanity check.

        int currentPrime = 2, primeUsage = 0;

        while (num > 1)
        {
            if (num % currentPrime == 0)
            {
                num /= currentPrime;
                primeUsage++;

                if (primeUsage == 2)
                    return false;
                continue;
            }

            if (currentPrime == 2)
                currentPrime++;
            else
                currentPrime += 2;

            // Threshold: square root of num.
            if (currentPrime > pow(num, 0.5))
                currentPrime = num;
        }

        return true;
    }

    pair<long long, long long> dfsValidPaths(int node)
    {
        visited[node]++; // From 0 to 1: visited.

        long long noPrimeNodes = 0, onePrimeNodes = 0;

        bool nodeIsPrime = verifyPrime(node);

        if (nodeIsPrime)
            onePrimeNodes++;
        else
            noPrimeNodes++;

        for (auto child : tree[node])
        {
            if (visited[child] == 0)
            {
                auto [childNoPrimeNodes, childOnePrimeNodes] = dfsValidPaths(child);

                pathsCount += childNoPrimeNodes * onePrimeNodes;

                if (nodeIsPrime)
                    onePrimeNodes += childNoPrimeNodes;

                else
                {
                    pathsCount += childOnePrimeNodes * noPrimeNodes;

                    noPrimeNodes += childNoPrimeNodes;

                    onePrimeNodes += childOnePrimeNodes;
                }
            }
        }

        return {noPrimeNodes, onePrimeNodes};
    }

public:
    long long countPaths(int n, vector<vector<int>> &edges)
    {
        for (auto edge : edges)
        {
            int node_1 = edge[0], node_2 = edge[1];

            if (tree.find(node_1) == tree.end())
                tree[node_1] = {};
            tree[node_1].push_back(node_2);

            if (tree.find(node_2) == tree.end())
                tree[node_2] = {};
            tree[node_2].push_back(node_1);
        }

        // Make n + 1 spots: map idx and node num w/o - 1 adjustment.
        visited.assign(n + 1, 0); // Default to all not visited yet.

        dfsValidPaths(1); // Always start from node labeled 1.
        return pathsCount;
    }
};