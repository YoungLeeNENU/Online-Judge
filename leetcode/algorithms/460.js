/**
 * @fileOverview LFU Cache O(1)
 * @name 460.js
 * @author Young Lee <youngleemails@gmail.com>
 * @license MIT
 */
'use strict';

/**
 * @param {number} capacity
 */
var LFUCache = function(capacity) {
	if (this instanceof LFUCache) {
		this.capacity = capacity;
		this.pool = {};
		this.frequency = [];
	} else {
		return new LFUCache(capacity);
	}
};

/**
 * @param {number} key use cache item
 * @return {number}
 */
LFUCache.prototype.get = function(key) {
	var context = this;
	if (context.pool[key] !== undefined) {
		var feq = 0;
		context.frequency.filter(function (x, i) {
			if (x && x.indexOf(key) !== -1) {
				feq = i;
			}
		});
		var evicted = context.frequency[feq].filter(function (x) {
			return x != key;
		});
		if (Array.isArray(evicted) && evicted.length === 0) {
			evicted = undefined;
		}
		context.frequency[feq] = evicted;
		if (context.frequency[feq + 1] && Array.isArray(context.frequency[feq + 1])) {
			// Silence
		} else {
			context.frequency[feq + 1] = [];
		}
		context.frequency[feq + 1].push(key); // Push to the last position of the array
		return context.pool[key];
	}
	return -1;					// Not Found
};

/**
 * @param {number} key
 * @param {number} value
 * @return {void}
 */
LFUCache.prototype.put = function(key, value) {
	var context = this;
	if (context.capacity > 0) {
	    if (context.pool[key] === undefined) { // insert
		    if (Object.keys(context.pool).length >= context.capacity) {
		        var indexes = [];
		        var shrinked_freq = context.frequency.filter(function (x, i) {
		        	if (x !== undefined) {
		        		indexes.push(i);
		        		return x;
		        	}
		        });
		        var to_be_evicted = shrinked_freq[0][0];
		        delete context.pool[to_be_evicted];
		        var evicted = context.frequency[indexes[0]].filter(function (x) {
		        	return x != to_be_evicted;
    	    	});
		        if (Array.isArray(evicted) && evicted.length === 0) {
		    	    context.frequency[indexes[0]] = undefined;
		        }
		        context.frequency[indexes[0]] = evicted;
		    }
	    }
		context.pool[key] = value; // Caching
		if (context.frequency[0] && Array.isArray(context.frequency[0])) {
			// Silence
		} else {
			context.frequency[0] = [];
		}
        context.frequency[0] = context.frequency[0].filter(function (x, i) {
	        return x !== key;
        });
        context.frequency[0].push(key);
	} else {
		return ;
	}
};

LFUCache.createNew = function (capacity) {
	if (this instanceof LFUCache) {
		this.capacity = capacity;
		this.pool = {};
		this.frequency = [];
	} else {
		return new LFUCache(capacity);
	}
};

/**
 * Check the cache status
 */
LFUCache.prototype.checkFrequency = function () {
	return this.frequency;
};

LFUCache.prototype.checkPool = function () {
	return this.pool;
};

LFUCache.prototype.reset = function () {
	this.pool = {};
	this.frequency = [];
	return;
};

// Your LFUCache object will be instantiated and called as such:
var obj = Object.create(LFUCache).createNew(10);
// obj.put(2, 1);
// obj.checkPool();
// obj.checkFrequency();
// obj.put(1, 1);
// obj.checkPool();
// obj.checkFrequency();
// obj.put(2, 3);
// obj.checkPool();
// obj.checkFrequency();
// obj.put(4, 1);
// obj.checkPool();
// obj.checkFrequency();
// obj.get(1);
// obj.checkPool();
// obj.checkFrequency();
// obj.get(2);
// obj.checkPool();
// obj.checkFrequency();

obj.put([10,13]);
obj.put([3,17]);
obj.put([6,11]);
obj.put([10,5]);
obj.put([9,10]);
obj.get([13]);
obj.put([2,19]);
obj.get([2]);
obj.get([3]);
obj.put([5,25]);
obj.get();
obj.put();
obj.put();
obj.put();
obj.get();
obj.put();
obj.get();
obj.get();
obj.get();
obj.get();
obj.put();
obj.put();
obj.get();
obj.get();
obj.get();
obj.put();
obj.put();
obj.get();
obj.put();
obj.get();
obj.put();
obj.get();
obj.get();
obj.get();
obj.put();
obj.put();
obj.put();
obj.get();
obj.put();
obj.get();
obj.get();
obj.put();
obj.put();
obj.get();
obj.put();
obj.put();
obj.put();
obj.put();
obj.get();
obj.put();
obj.put();
obj.get();
obj.put();
obj.put();
obj.get();
obj.put();
obj.put();
obj.put();
obj.put();
obj.put();
obj.get();
obj.put();
obj.put();
obj.get();
obj.put();
obj.get();
obj.get();
obj.get();
obj.put();
obj.get();
obj.get();
obj.put();
obj.put();
obj.put();
obj.put();
obj.get();
obj.put();
obj.put();
obj.put();
obj.put();
obj.get();
obj.get();
obj.get();
obj.put();
obj.put();
obj.put();
obj.get();
obj.put();
obj.put();
obj.put();
obj.get();
obj.put();
obj.put();
obj.put();
obj.get();
obj.get();
obj.get();
obj.put();
obj.put();
obj.put();
obj.put();
obj.get();
obj.put();
obj.put();
obj.put();
obj.put();
obj.put();
obj.put();
obj.put();

[[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
