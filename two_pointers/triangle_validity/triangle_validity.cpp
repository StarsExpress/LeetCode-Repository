#include <vector>
using namespace std;

int count_valid_triangles(vector<int> &edges)
{ // LeetCode Q.611.
    sort(edges.begin(), edges.end());

    int triangles = 0, min_edge_2_idx = 1;
    for (int edge_3_idx = 2; edge_3_idx < edges.size(); edge_3_idx++)
    {
        int edge_3_len = edges[edge_3_idx];
        while (edges[min_edge_2_idx - 1] + edges[min_edge_2_idx] <= edge_3_len)
        {
            min_edge_2_idx++;
            if (min_edge_2_idx >= edge_3_idx)
            {
                break;
            }
        }

        int min_edge_1_idx = min_edge_2_idx - 1;
        for (int edge_2_idx = min_edge_2_idx; edge_2_idx < edge_3_idx; edge_2_idx++)
        {
            int edge_2_len = edges[edge_2_idx];
            while (min_edge_1_idx > 0)
            {
                if (edges[min_edge_1_idx - 1] + edge_2_len <= edge_3_len)
                {
                    break;
                }
                min_edge_1_idx--;
            }

            triangles += edge_2_idx - min_edge_1_idx;
        }
    }

    return triangles;
}
