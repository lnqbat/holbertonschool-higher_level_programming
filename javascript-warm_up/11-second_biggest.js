#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
const uni = [...new Set(args)];
uni.sort((a, b) => b - a);

if (uni.length <= 1) {
  console.log(0);
} else {
  console.log(uni[1]);
}
