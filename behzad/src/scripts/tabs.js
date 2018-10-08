let act_con = 'itre'

const itre = document.getElementById('tab_1')
const civil = document.getElementById('tab_2')
const former = document.getElementById('tab_3')

const itre_staff = document.getElementById('itre_staff')
const civil_staff = document.getElementById('civil_staff')
const former_staff = document.getElementById('former_staff')


itre ? itre.addEventListener('click', () => toggleTabContent('itre') ) : ''
civil ? civil.addEventListener('click', () => toggleTabContent('civil') ) : ''
former ? former.addEventListener('click', () => toggleTabContent('former') ) : ''

function toggleTabContent(clicked) {
  if (clicked === act_con) {
    return
  } else {
    switch(act_con) {
      case 'itre':
        itre.classList.remove("active_tab")
        itre_staff.classList.remove("active_content")
        break
      case 'civil':
        civil.classList.remove("active_tab")
        civil_staff.classList.remove("active_content")
        break
      case 'former':
        former.classList.remove("active_tab")
        former_staff.classList.remove("active_content")
        break
      default:
        break
    }
    switch(clicked) {
      case 'itre':
        itre.classList.add("active_tab")
        itre_staff.classList.add("active_content")
        break
      case 'civil':
        civil.classList.add("active_tab")
        civil_staff.classList.add("active_content")
        break
      case 'former':
        former.classList.add("active_tab")
        former_staff.classList.add("active_content")
        break
      default:
        break
    }
  }
  act_con = clicked
  return
}
