/** 
 * @param {number} key 
 * @param {number} value
 */
class Node {
    constructor(key, value) {
        this.key = key, this.value = value;
        this.prev = null, this.next = null;
    }
}


/**
 * @param {number} capacity
 */
var LRUCache = function (capacity) { // LeetCode Q.146.
    this.capacity = capacity;
    this.cache = new Map();

    this.head = new Node(-1, -1), this.tail = new Node(-1, -1);
    this.head.next = this.tail, this.tail.prev = this.head;

    /**
    * @param {Node} node
    */
    this.add = function (node) {
        let next_node = this.head.next;
        node.prev = this.head;
        this.head.next = node;

        node.next = next_node;
        next_node.prev = node;
    }

    /**
    * @param {Node} node
    */
    this.remove = function (node) {
        let prev_node = node.prev;
        let next_node = node.next;
        prev_node.next = next_node;
        next_node.prev = prev_node;
    }
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function (key) {
    if (!this.cache.has(key))
        return -1;

    let node = this.cache.get(key);
    this.remove(node);

    this.add(node);
    this.cache.set(key, node); // Node property has changed.
    return this.cache.get(key).value;
};

/** 
 * @param {number} key 
 * @param {number} value
 */
LRUCache.prototype.put = function (key, value) {
    if (!this.cache.has(key)) // New key coming.
    {
        if (this.cache.size == this.capacity) // Capacity is full.
        {
            let removed_key = this.tail.prev.key;
            this.cache.delete(removed_key);
            this.remove(this.tail.prev);
        }
    }
    else // Remove already existing node from current spot.
    {
        this.remove(this.cache.get(key));
    }

    let node = new Node(key, value);
    this.add(node);
    this.cache.set(key, node);
};