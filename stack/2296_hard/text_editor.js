const TRACE_LIMIT = 10; // Number of chars to trace to the cursor left.

var TextEditor = function () {
    this.cursor_left = []; // Stack.
    this.cursor_right = []; // Reverse queue: queue's head is actually at idx -1.
};

/** 
 * @param {string} text
 * @return {void}
 */
TextEditor.prototype.addText = function (text) {
    for (const char of text)
        this.cursor_left.push(char);
};

/** 
 * @param {number} k
 * @return {number}
 */
TextEditor.prototype.deleteText = function (k) {
    let deletions = 0;
    while (Math.min(this.cursor_left.length, k) > 0) {
        this.cursor_left.pop();
        deletions++;
        k--;
    }

    return deletions;
};

/** 
 * @param {number} k
 * @return {string}
 */
TextEditor.prototype.cursorLeft = function (k) {
    while (Math.min(this.cursor_left.length, k) > 0) {
        this.cursor_right.push(this.cursor_left.pop());
        k--;
    }

    let cursor_left_str = "";
    let start_idx = -Math.min(this.cursor_left.length, TRACE_LIMIT);
    for (idx = start_idx; idx <= -1; idx++)
        cursor_left_str += this.cursor_left.at(idx);

    return cursor_left_str;
};

/** 
 * @param {number} k
 * @return {string}
 */
TextEditor.prototype.cursorRight = function (k) {
    while (Math.min(this.cursor_right.length, k) > 0) {
        this.cursor_left.push(this.cursor_right.pop());
        k--;
    }

    let cursor_left_str = "";
    let start_idx = -Math.min(this.cursor_left.length, TRACE_LIMIT);
    for (idx = start_idx; idx <= -1; idx++)
        cursor_left_str += this.cursor_left.at(idx);

    return cursor_left_str;
};