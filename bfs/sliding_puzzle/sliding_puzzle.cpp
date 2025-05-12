#include <vector>
#include <string>
#include <unordered_set>
#include <queue>
using namespace std;

int sliding_puzzle(vector<vector<int>> &board)
{
    // LeetCode Q.773.
    string init_state = ""; // Vectorize board w.r.t. rows into string.
    for (int row_idx = 0; row_idx < 2; row_idx++)
        for (int col_idx = 0; col_idx < 3; col_idx++)
            init_state += to_string(board[row_idx][col_idx]);

    // Format: vectorize board w.r.t. rows into string.
    unordered_set<string> visited_states;

    queue<pair<string, int>> queue; // Format: {current state, moves}.
    queue.push({"123450", 0});      // Start from the solved state.
    while (!queue.empty())
    {
        auto [state, moves] = queue.front();
        if (state == init_state)
            return moves;

        moves++;
        visited_states.insert(state);
        queue.pop();

        for (int idx = 0; idx < 6; idx++)
            if (state[idx] == '0')
            { // Locate the idx containing '0'.
                if (idx % 3 != 2)
                {
                    swap(state[idx], state[idx + 1]);
                    if (visited_states.find(state) == visited_states.end())
                        queue.push({state, moves});

                    swap(state[idx], state[idx + 1]); // Swap back.
                }

                if (idx % 3 != 0)
                {
                    swap(state[idx], state[idx - 1]);
                    if (visited_states.find(state) == visited_states.end())
                        queue.push({state, moves});

                    swap(state[idx], state[idx - 1]); // Swap back.
                }

                if (idx < 3)
                {
                    swap(state[idx], state[idx + 3]);
                    if (visited_states.find(state) == visited_states.end())
                        queue.push({state, moves});

                    swap(state[idx], state[idx + 3]); // Swap back.
                }

                if (idx >= 3)
                {
                    swap(state[idx], state[idx - 3]);
                    if (visited_states.find(state) == visited_states.end())
                        queue.push({state, moves});

                    swap(state[idx], state[idx - 3]); // Swap back.
                }
                break;
            }
    }

    return -1; // Can't be solved.
}
