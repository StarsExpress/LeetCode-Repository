var find_second_next_greater = function (nums) { // LeetCode Q.2454.
    let second_next_greater = Array(nums.length).fill(-1);
    let stack_1 = [], stack_2 = [], transporter = []; // Format: [idx, num].

    for (const [idx, num] of nums.entries()) {
        while (stack_2.length > 0 && num > stack_2.at(-1)[1]) {
            let past_idx = stack_2.pop()[0];
            second_next_greater[past_idx] = num;
        }

        while (stack_1.length > 0 && num > stack_1.at(-1)[1])
            transporter.push(stack_1.pop()); // Stack 1 to transporter.
        stack_1.push([idx, num]); // Now current num can enter stack 1.

        while (transporter.length > 0)
            stack_2.push(transporter.pop()); // Transporter to stack 2.
    }

    return second_next_greater;
};