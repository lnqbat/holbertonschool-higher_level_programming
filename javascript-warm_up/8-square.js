#!/usr/bin/node
const size = parseInt(process.argv[2]);
let line = '';
let j;
let i;

if (isNaN(size)) {
  console.log('Missing size');
} else if (size > 0) {
  for (j = 0; j < size; j++) {
    line += 'X';
  }
  for (i = 0; i < size; i++) {
    console.log(line);
  }
}
