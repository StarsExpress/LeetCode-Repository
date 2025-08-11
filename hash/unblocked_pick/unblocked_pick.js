/**
 * @param {number} n
 * @param {number[]} blocklist
 */
var UnBlockedPick = function (n, blocklist) {
    this.replacements_table = new Map(); // Attach class-wide variables to this.
    for (const blocked_num of blocklist)
        this.replacements_table.set(blocked_num, -1);

    this.total_candidates = n - blocklist.length;
    let replacement_num = this.total_candidates;

    for (const blocked_num of blocklist) {
        if (blocked_num < this.total_candidates) {
            while (this.replacements_table.has(replacement_num))
                replacement_num++;

            this.replacements_table[blocked_num] = replacement_num;
            replacement_num++;
        }
    }
};

/**
 * @return {number}
 */
UnBlockedPick.prototype.pick = function () { // LeetCode Q.710.
    let picked_num = Math.floor(Math.random() * this.total_candidates);
    if (this.replacements_table.has(picked_num))
        picked_num = this.replacements_table[picked_num];
    return picked_num;
};