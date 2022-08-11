var y = document.getElementById("list-nav"); 

function switchNavMode()
{
    if (y.style.display === "flex") {
    y.style.display = "none";
    } else {
    y.style.display = "flex";
    console.log("no");
    }
}