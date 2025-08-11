var find_shortest_subarray_length = function (nums, k) { // LeetCode Q.862.
    let queue = []; // Format: [idx, prefix sum].
    let queue_front_idx = 0; // Locates the current front element.
    let prefix_sum = 0, min_len = nums.length + 1;

    for (const [idx, num] of nums.entries()) {
        prefix_sum += num;
        while (queue_front_idx < queue.length) {
            const [past_idx, past_prefix_sum] = queue.at(queue_front_idx);
            if (prefix_sum - past_prefix_sum < k) {
                break;
            }

            let subarray_len = idx - past_idx;
            if (subarray_len < min_len)
                min_len = subarray_len;
            queue_front_idx++;
        }

        while (queue.length > queue_front_idx && queue.at(-1)[1] >= prefix_sum)
            queue.pop();

        if (prefix_sum >= k && idx + 1 < min_len)
            min_len = idx + 1;

        queue.push([idx, prefix_sum]);
    }

    return (min_len === nums.length + 1) ? -1 : min_len;
};