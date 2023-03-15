#!/usr/bin/node

//import the "process" module
const process = require("process");
//the calue of the first argument passed
const first_arg = Number(process.argv[2]);

if (typeof(first_arg) == "number") {
    console.log(`My number: ${first_arg}`)
}
else {
    console.log("Not a number");
}
