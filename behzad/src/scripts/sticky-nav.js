// When the user scrolls the page, execute myFunction
window.onscroll = function() {checkStick()}

// Get the navbar
const navbar = document.getElementById("navbar")
const logo = document.getElementById("logo_big")
const logo_big = document.getElementById("logo_holder")
const logo_small = document.getElementById("logo_small")
const header = document.getElementById("header")
const title = document.getElementById("title")

// Get the offset position of the navbar
const sticky_title = title.offsetTop-12;
const sticky_logo = logo.offsetTop-5;
const sticky_nav = navbar.offsetTop-49;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function checkStick() {
  if (window.pageYOffset >= sticky_title) {
    title.classList.add("sticky_title")
    header.setAttribute('style', 'padding-top:55px;')
  } else {
    title.classList.remove("sticky_title")
    header.removeAttribute('style', 'padding-top:55px;')
  }

  if (window.pageYOffset >= sticky_logo) {
    logo_small.classList.add("sticky")
    logo_small.setAttribute('style', 'display:block;width:200px;')
  } else {
    logo_small.classList.remove("sticky")
    logo_small.removeAttribute('style', 'display:block;width:200px;')
  }

  if (window.pageYOffset >= sticky_nav) {
    navbar.classList.add("sticky_nav")
  } else {
    navbar.classList.remove("sticky_nav")
  }
}
