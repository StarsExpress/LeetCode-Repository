#include <vector>
#include <deque>
using namespace std;

vector<double> compute_collision_times(vector<vector<int>> &cars) // LeetCode Q.1776.
{
    vector<double> collision_times(cars.size(), -1); // Default to -1: no collisions.
    deque<pair<int, int>> stack;                     // Format: {position, speed}.

    for (int idx = cars.size() - 1; idx >= 0; idx--) // From rightmost car to leftmost car.
    {
        int position = cars[idx][0], speed = cars[idx][1];
        while (!stack.empty() && stack.back().second >= speed)
        {
            stack.pop_back();
        }

        while (stack.size() >= 2)
        {
            auto [front_car_position, front_car_speed] = stack.back();
            auto [front_front_car_position, front_front_car_speed] = stack[stack.size() - 2];

            double current_car_crash_time = (front_car_position - position);
            current_car_crash_time /= (speed - front_car_speed);

            double front_car_crash_time = (front_front_car_position - front_car_position);
            front_car_crash_time /= (front_car_speed - front_front_car_speed);

            if (current_car_crash_time <= front_car_crash_time)
            {
                break; // Current car and its left cars might crash stack's last car.
            }
            else
            { // Current car and its left cars can't crash stack's last car.
                stack.pop_back();
            }
        }

        if (!stack.empty() && speed > stack.back().second)
        {
            auto [front_car_position, front_car_speed] = stack.back();
            double current_car_crash_time = (front_car_position - position);
            current_car_crash_time /= (speed - front_car_speed);
            collision_times[idx] = current_car_crash_time;
        }

        stack.push_back({position, speed});
    }

    return collision_times;
}
