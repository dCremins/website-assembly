const hamburger = document.getElementById('mobile_button')
let mobileActive = false

hamburger.addEventListener('click', toggleMobile())

toggleMobile() {
  if (mobileActive) {
    mobileActive = true
    hamburger.classList.add('is-active')
  } else {
    mobileActive = false
    hamburger.classList.remove('is-active')
  }
}
