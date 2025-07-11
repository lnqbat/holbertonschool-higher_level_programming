#!/usr/bin/node
const { argv } = require('node:process');

const res = argv.reduce(
  (acc, num) => {
    if (num > acc[0]) {
      acc[1] = acc[0];
      acc[0] = num;
    } else if (num > acc[1] && num < acc[0]) {
      acc[1] = num;
    }
    return acc;
  },
  [0, 0]
);
console.log(res[1]);
