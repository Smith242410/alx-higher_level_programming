#!/usr/bin/node

//import the "process" module
const process = require("process");

if (process.argv.length > 2) {
    console.log("Argument found");
}
else {
    console.log("Argument not found")
}
