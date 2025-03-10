const toggleButton = document.getElementById('toggle-btn')
const sidebar = document.getElementById('sidebar')
const sidediv = document.getElementById('sidediv')
const toggleBtn_map = document.getElementById('toggle-btn-map')


function toggleSidebar(){
  sidebar.classList.toggle('close')
  toggleButton.classList.toggle('rotate')

  closeAllSubMenus()
}

function toggleSidediv(){
  sidebar.classList.toggle('close')
  toggleBtn_map.classList.toggle('rotate')

}

function toggleSubMenu(button){

  if(!button.nextElementSibling.classList.contains('show')){
    closeAllSubMenus()
  }

  button.nextElementSibling.classList.toggle('show')
  button.classList.toggle('rotate')

  if(sidebar.classList.contains('close')){
    sidebar.classList.toggle('close')
    toggleButton.classList.toggle('rotate')
  }
}

function closeAllSubMenus(){
  Array.from(sidebar.getElementsByClassName('show')).forEach(ul => {
    ul.classList.remove('show')
    ul.previousElementSibling.classList.remove('rotate')
  })
}