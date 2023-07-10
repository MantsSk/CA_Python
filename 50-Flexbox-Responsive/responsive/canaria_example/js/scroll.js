const htmlTag = document.querySelector('html');
const bodyTag = document.querySelector('body');
const myNav = document.querySelector('nav');
const myElem = document.querySelector('nav li a');

let scrolled = () => {
    let dec = scrollY/ (bodyTag.scrollHeight - innerHeight);
    return Math.floor(dec * 100);
}

addEventListener('scroll', () => {
    myNav.style.setProperty('background', scrolled() > 1 ? "#f7ececfa" : "white");
})