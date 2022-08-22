let tavo = "pavarde"

function doSomething(vardas, pavarde="(pavarde nenurodyta)"){
    console.log(doSomethingAgain())
    console.log("Labas "+vardas+" "+pavarde)
}

function doSomethingAgain(){
    console.log("Doing somethign again")
    console.log(tavo)
}


elem.onclick = function() {
    alert('Thank you');
};

elem2.addEventListener("mouseover", doSomethingAgain);
