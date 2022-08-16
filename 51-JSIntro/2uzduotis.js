function main() {
    var hour = 1
    // Your code goes here
    if (hour < 12) {
        console.log(`${hour} AM`);
    }
    else if (hour < 24) {
        console.log(`${hour} AM`)
    }
    else {
    	console.log("No hour like this")
    }
}

main()