var modal;
var slideIndex = 0;
var slideshowTimer;

function openModal(id) //id that you get from DOM
{
    modal = document.getElementById(id);
    modal.style.display = "block";

    clearTimeout(slideshowTimer);
    showSlides();
}

function showSlides() {
    var slides = modal.getElementsByClassName("mySlides");
    var dots = modal.getElementsByClassName("dot");

    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
    }
    for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace("active", "");
    }

    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}    
    slides[slideIndex-1].style.display = "block";  
    dots[slideIndex-1].className += " active";
    slideshowTimer = setTimeout(showSlides, 4000); // Change image every 2 seconds
}

function closeModal(id)
{
    modal = document.getElementById(id);
    modal.style.display = "none";
}

window.addEventListener("click", outsideClick);

function outsideClick(e)
{   
        if(e.target == modal)
        {
            modal.style.display = 'none';
        }
}




