// When the user scrolls the page, execute myFunction
window.onscroll = function() {checkStick()}

// Get the navbar
const navbar = document.getElementById("navbar")
const mobile = document.getElementById("mobile_navbar")
const logo = document.getElementById("logo_big")
const logo_big = document.getElementById("logo_holder")
const logo_small = document.getElementById("logo_small")
const header = document.getElementById("header")
const title = document.getElementById("title")

// Get the offset position of the navbar
const sticky_title = title.offsetTop-12;
const sticky_logo = logo.offsetTop-4;
const sticky_nav = navbar.offsetTop-78;
const sticky_mobile = mobile.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function checkStick() {
  if (window.pageYOffset >= sticky_title) {
    title.classList.add("sticky_title")
    header.classList.add("sticky_padding")
  } else {
    title.classList.remove("sticky_title")
    header.classList.remove("sticky_padding")
  }

  if (window.pageYOffset >= sticky_logo) {
    logo.classList.add("sticky")
    navbar.classList.add("sticky_nav")
  } else {
    logo.classList.remove("sticky")
    navbar.classList.remove("sticky_nav")
  }


  if (sticky_mobile) {
    if (window.pageYOffset >= sticky_mobile) {
      mobile.classList.add("sticky_mobile")
    } else {
      mobile.classList.remove("sticky_mobile")
    }
  }
}
