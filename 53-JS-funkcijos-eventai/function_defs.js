let doSomethingAgain = function(){
    console.log("You have to change me")
}

function sumFunction(){
    console.log(1+2);
}

function doSomething(vardas, pavarde="(pavarde nenurodyta)"){
    //doSomethingAgain = sumFunction;
    console.log(((x=1,y=2) => x+y)())
    console.log("Labas "+concatenateName(vardas, pavarde))
    console.log("Lietuvos prezidentas siuo metu yra "+concatenateName("gitanas", "nauseda"))
    function concatenateName(name, surname){
        return name+" "+surname
    }
}

let myVar = doSomething;

const sqrt = (x) => {x*x; console.log(x*x);}
