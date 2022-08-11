let sliderImages = document.getElementsByClassName('slide');
//let arrowLeft = document.getElementById('arrow-left');
//let arrowRight = document.getElementById('arrow-right');
current = 0;
timeoutHandle = 0;

startSlide();
showAutoSlides();


function reset(){
    for (let i = 0; i < sliderImages.length; i++) {
        sliderImages[i].style.display = "none";
    }
}

function startSlide(){
    reset();
    sliderImages[0].style.display = "block";
}

function slideLeft(){
    reset();
    sliderImages[current-1].style.display = 'block';
    current--;
}

function slideRight(){
    reset();
    sliderImages[current+1].style.display = 'block';
    current++;
}
/*
arrowLeft.addEventListener('click', function(){
    clearTimeout(timeoutHandle);
    if (current === 0)
    {
        current = sliderImages.length;
    }
    slideLeft();
    showAutoSlides();
});

arrowRight.addEventListener('click', function(){
    clearTimeout(timeoutHandle);
    if (current === sliderImages.length - 1)
    {
        current = -1;
    }
    slideRight();
    showAutoSlides();
});
*/
function showAutoSlides() {
    timeoutHandle = setTimeout(function(){
        if (current === sliderImages.length - 1)
        {
            current = -1;
        }
        slideRight();
        showAutoSlides();
    }, 7000);
}
