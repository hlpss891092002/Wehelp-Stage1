const agreeBox = document.querySelector(".agree-box")
const loginBtn = document.querySelector(".login-btn")
const squareSubmit = document.querySelector(".square-btn")
const squareInput = document.querySelector(".square-input")

loginBtn.addEventListener("click",(e)=>{
  // 
  if(agreeBox.checked === false){
    alert("Please check the checkbox first")
    e.preventDefault()
  }
  // else{
  //   location.href="/signin"
  // }
})


squareSubmit.addEventListener("click",(e)=>{
  if(!Number.isInteger(squareInput.value)){
    alert("Please enter a positive number")
    e.preventDefault()
  }
  
})