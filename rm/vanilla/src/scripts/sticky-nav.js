// When the user scrolls the page, execute myFunction
window.onscroll = function() {checkStick()}



// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function checkStick() {
  // Get the navbar
  let logo = document.getElementById("logo_big")
  let logo_big = document.getElementById("logo_holder")
  let logo_icon = document.getElementById("logo_icon")
  let header = document.getElementById("header")
  let title = document.getElementById("title")
  let nav = document.getElementById("nav_bar")

  // Get the offset position of the navbar
console.log(window.pageYOffset, ' vs ', nav.offsetTop)
  if (window.pageYOffset > title.offsetTop) {
    title.classList.add("sticky_title")
    header.classList.add("sticky_padding")
    logo.classList.add("sticky")
    logo_icon.classList.add("sticky_fixed")
    logo_icon.classList.add("sticky_little")
  } else {
    title.classList.remove("sticky_title")
    header.classList.remove("sticky_padding")
    logo.classList.remove("sticky")
    logo_icon.classList.remove("sticky_fixed")
    logo_icon.classList.remove("sticky_little")
  }
  if (window.pageYOffset > (nav.offsetTop-50)) {
    nav.classList.add("sticky_bar")
  } else {
    nav.classList.remove("sticky_bar")
  }
}
