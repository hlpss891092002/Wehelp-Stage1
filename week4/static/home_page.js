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
  let squareValue = Number(squareInput.value) 
  if(!Number.isInteger(squareValue)){
    alert("Please enter a positive number")
    e.preventDefault()
  }else{
    e.preventDefault()
    location.href=`/square/${squareValue}`
  }

})