let sliderImagesEnt = document.getElementsByClassName('image-container');
let sliderImagesEntMobile = document.getElementsByClassName('mobile-image-container');
let arrowLeftEnt = document.getElementById('prev-arrow');
let arrowRightEnt = document.getElementById('next-arrow');
let arrowLeftEntMobile = document.getElementById('prev-arrow-mobile');
let arrowRightEntMobile = document.getElementById('next-arrow-mobile');
let entTexts = document.getElementsByClassName('ent-info-item');
currentEnt = 0;
timeoutHandleEnt = 0;

startSlideEnt();
showAutoSlidesEnt();


function resetEnt(){
    for (let i = 0; i < sliderImagesEnt.length; i++) {
        sliderImagesEnt[i].style.display = "none";
        sliderImagesEntMobile[i].style.display = "none";
    }
}

function startSlideEnt(){
    resetEnt();
    sliderImagesEnt[currentEnt].style.display = "block";
    sliderImagesEntMobile[currentEnt].style.display = "block";
    checkEnt(currentEnt);
}

function slideLeftEnt(){
    resetEnt();
    sliderImagesEnt[currentEnt-1].style.display = 'block';
    sliderImagesEntMobile[currentEnt-1].style.display = 'block';
    checkEnt(currentEnt-1);
    currentEnt--;
}

function slideRightEnt(){
    resetEnt();
    sliderImagesEnt[currentEnt+1].style.display = 'block';
    sliderImagesEntMobile[currentEnt+1].style.display = 'block';
    checkEnt(currentEnt+1);
    currentEnt++;
}

arrowLeftEntMobile.addEventListener('click', function(){
    clearTimeout(timeoutHandleEnt);
    if (currentEnt === 0)
    {
        currentEnt = sliderImagesEnt.length;
    }
    slideLeftEnt();
    showAutoSlidesEnt();
});

arrowRightEntMobile.addEventListener('click', function(){
    clearTimeout(timeoutHandleEnt);
    if (currentEnt === sliderImagesEnt.length - 1)
    {
        currentEnt = -1;
    }
    slideRightEnt();
    showAutoSlidesEnt();
});


arrowLeftEnt.addEventListener('click', function(){
    clearTimeout(timeoutHandleEnt);
    if (currentEnt === 0)
    {
        currentEnt = sliderImagesEnt.length;
    }
    slideLeftEnt();
    showAutoSlidesEnt();
});

arrowRightEnt.addEventListener('click', function(){
    clearTimeout(timeoutHandleEnt);
    if (currentEnt === sliderImagesEnt.length - 1)
    {
        currentEnt = -1;
    }
    slideRightEnt();
    showAutoSlidesEnt();
});

function showAutoSlidesEnt() {
    timeoutHandleEnt = setTimeout(function(){
        if (currentEnt === sliderImagesEnt.length - 1)
        {
            currentEnt = -1;
        }
        slideRightEnt();
        showAutoSlidesEnt();
    }, 7000);
}

function checkEnt(i) {
    if (i<2){
        for(i=0; i<entTexts.length;i++)
        {
            entTexts[i].className = entTexts[5].className.replace(" activeitem", "");
        }
        entTexts[0].className += " activeitem";
    }
    else if (i<4){
        for(i=0; i<entTexts.length;i++)
        {
            entTexts[i].className = entTexts[5].className.replace(" activeitem", "");
        }
        entTexts[1].className += " activeitem";
    }
    else if (i<6){
        for(i=0; i<entTexts.length;i++)
        {
            entTexts[i].className = entTexts[5].className.replace(" activeitem", "");
        }
        entTexts[2].className += " activeitem";
    }
    else if (i<8){
        for(i=0; i<entTexts.length;i++)
        {
            entTexts[i].className = entTexts[5].className.replace(" activeitem", "");
        }
        entTexts[3].className += " activeitem";
    }
    else if (i<10){
        for(i=0; i<entTexts.length;i++)
        {
            entTexts[i].className = entTexts[5].className.replace(" activeitem", "");
        }
        entTexts[4].className += " activeitem";
    }
    else {
        for(i=0; i<entTexts.length;i++)
        {
            entTexts[i].className = entTexts[5].className.replace(" activeitem", "");
        }
        entTexts[5].className += " activeitem";
    }
}
