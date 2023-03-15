#!/usr/bin/node

//import tge "process" module
const process = require("process");

if (process.argv[2] == undefined) {
    console.log("Argument not found");
}
else {
    console.log(process.argv[2]);
}
