/**
 * @param {number[]} nums
 * @return {number[]}
 */
var find_lonely_integers = function (nums) { // LeetCode Q.2150.
    let nums2counts = new Map();
    for (num of nums) {
        if (!nums2counts.has(num))
            nums2counts.set(num, 0);
        nums2counts.set(num, nums2counts.get(num) + 1);

    }
    let lonely_nums = [];
    for (num of nums) {
        if (nums2counts.get(num) == 1) {
            if (!nums2counts.has(num - 1) && !nums2counts.has(num + 1))
                lonely_nums.push(num);
        }
    }

    return lonely_nums;
};