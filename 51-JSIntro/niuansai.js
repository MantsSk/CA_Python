a = 5
b = "5"

if (a === b) {
	console.log("Lygu")
}

// ----------------------------------- scopes example 

// js example
var x = 300

if (true) {
    var x = 200
    console.log(x)
}

console.log(x)

// python example

// x = 300

// if True:
//     x = 200
//     print(x)

// print(x)