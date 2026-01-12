
var Skiplist = function () { // LeetCode Q.1206.
    this.nums2counts = new Map();
};

/** 
 * @param {number} target
 * @return {boolean}
 */
Skiplist.prototype.search = function (target) {
    if (this.nums2counts.has(target) && this.nums2counts.get(target) > 0)
        return true;
    return false;
};

/** 
 * @param {number} num
 * @return {void}
 */
Skiplist.prototype.add = function (num) {
    if (!this.nums2counts.has(num))
        this.nums2counts.set(num, 0);
    this.nums2counts.set(num, this.nums2counts.get(num) + 1);
};

/** 
 * @param {number} num
 * @return {boolean}
 */
Skiplist.prototype.erase = function (num) {
    if (this.nums2counts.has(num) && this.nums2counts.get(num) > 0) {
        this.nums2counts.set(num, this.nums2counts.get(num) - 1);
        return true;
    }
    return false;
};