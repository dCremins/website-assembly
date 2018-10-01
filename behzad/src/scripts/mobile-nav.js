const hamburger = document.getElementById('mobile_button')
let mobileActive = false

hamburger.addEventListener('click', toggleMobile)

function toggleMobile() {
  console.log(mobileActive)
  if (mobileActive) {
    mobileActive = false
    hamburger.classList.remove('is-active')
  } else {
    mobileActive = true
    hamburger.classList.add('is-active')
  }
}
