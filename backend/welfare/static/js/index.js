const hamburger = document.querySelector('.hamburger')
const logo = document.querySelector('.logo')
const menu = document.querySelector('.menu')

hamburger.addEventListener('click',function () {
    this.classList.toggle('is-active');
    logo.classList.toggle('is-active');
    menu.classList.toggle('is-active');
    
})