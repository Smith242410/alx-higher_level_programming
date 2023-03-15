#!/usr/bin/node

//import the "process" module
const process = require("process");

const str = `${process.argv[2]} is ${process.argv[3]}`;

console.log(str);
