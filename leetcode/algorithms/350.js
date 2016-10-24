'use strict';

var intersect = function(nums1, nums2) {
    var res = [];
    nums1.sort(function(x, y) {return x - y;});
    nums2.sort(function(x, y) {return x - y;});
    while( nums1[0] !== undefined && nums2[0] !== undefined ) {
        var to_be_shifted1 = nums1[0];
        var to_be_shifted2 = nums2[0];
        if (to_be_shifted1 === to_be_shifted2) {
            // if (res.indexOf(to_be_shifted1) == -1) {
	        res.push(to_be_shifted1);
            // }
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

console.log(intersect([1, 2, 2, 1], [2, 2]));
