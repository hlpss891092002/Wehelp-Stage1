let hamburgerIcon = document.querySelector(".hamburger-icon");
let hamburgerList = document.querySelector(".hamburger-list");
let closeIcon = document.querySelector(".close-icon");

hamburgerIcon.addEventListener('click', function(event) {
  hamburgerList.style.display = 'flex'
})
closeIcon.addEventListener('click', function(event){
  hamburgerList.style.display = 'none'
})