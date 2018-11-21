// When the user scrolls the page, execute myFunction
window.onscroll = function() {checkStick()}

// Get the navbar
const navbar = document.getElementById("navbar")
const mobile = document.getElementById("mobile_navbar")
const logo = document.getElementById("logo_big")
const logo_big = document.getElementById("logo_holder")
const logo_icon = document.getElementById("logo_icon")
const logo_small = document.getElementById("logo_small")
const header = document.getElementById("header")
const title = document.getElementById("title")

// Get the offset position of the navbar
const sticky_title = title.offsetTop-12;
const sticky_logo = logo.offsetTop-24;
const sticky_icon = logo_big.offsetTop-105;
const sticky_nav = navbar.offsetTop-78;
const sticky_mobile = mobile.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function checkStick() {
  console.log('widow: ', window.pageYOffset)
  console.log('title: ', sticky_title)
  console.log('logo: ', sticky_logo)
  if (window.pageYOffset >= sticky_title) {
    title.classList.add("sticky_title")
    header.classList.add("sticky_padding")
  } else {
    title.classList.remove("sticky_title")
    header.classList.remove("sticky_padding")
  }

  if (window.pageYOffset >= sticky_logo) {
    navbar.classList.add("sticky_nav")
  } else {
    navbar.classList.remove("sticky_nav")
      logo.classList.remove("sticky")
      logo_icon.classList.remove("sticky_fixed")
      logo_icon.classList.remove("sticky_little")
  }

  if (window.pageYOffset >= sticky_icon) {
    logo.classList.add("sticky")
    logo_icon.classList.add("sticky_fixed")
    logo_icon.classList.add("sticky_little")
  } else {
  }

  if (sticky_mobile) {
    if (window.pageYOffset >= sticky_mobile) {
      mobile.classList.add("sticky_mobile")
    } else {
      mobile.classList.remove("sticky_mobile")
    }
  }
}
