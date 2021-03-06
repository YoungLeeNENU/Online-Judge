'use strict';

var union = function(nums1, nums2) {
    var res = [],
        size = nums1.length > nums2.length ? nums1.length : nums2.length;
    nums1.sort(function(x, y) {return x - y;});
    nums2.sort(function(x, y) {return x - y;});
    for (var i = 0; i < size; i++) {
        var shifted1 = nums1.shift();
        var shifted2 = nums2.shift();
        if (shifted1) {
            if (res.indexOf(shifted1) == -1) {
                res.push(shifted1);
            }
        }
        if (shifted2) {
            if (res.indexOf(shifted2) == -1) {
                res.push(shifted2);
            }
        }
    }
    return res;
};

var intersection = function(nums1, nums2) {
    var res = [];
    nums1.sort(function(x, y) {return x - y;});
    nums2.sort(function(x, y) {return x - y;});
    while( nums1[0] !== undefined && nums2[0] !== undefined ) {
        var to_be_shifted1 = nums1[0];
        var to_be_shifted2 = nums2[0];
        if (to_be_shifted1 === to_be_shifted2) {
            if (res.indexOf(to_be_shifted1) == -1) {
	            res.push(to_be_shifted1);
            }
            nums1.shift();
            nums2.shift();
        } else if (to_be_shifted1 < to_be_shifted2) {
            nums1.shift();
        } else if (to_be_shifted1 > to_be_shifted2) {
            nums2.shift();
        }
    }
    return res;
};

console.log(intersection([1, 2, 2, 1], [2, 2]));
