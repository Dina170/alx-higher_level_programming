#!/usr/bin/node

const len = process.argv.length;

if (len <= 3) {
  console.log(0);
} else {
  const nums = process.argv.slice(2).map(function (n) {
    return parseInt(n);
  }).sort((a, b) => a - b);
  console.log(nums[nums.length - 2]);
}
