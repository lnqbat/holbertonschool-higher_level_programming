#!/usr/bin/node
const { argv } = require('node:process');

function fact (n) {
  let res = 1;
  for (let i = 1; i <= n; i++) {
    res *= i;
  }
  return res;
}
console.log(fact(argv[2]));
