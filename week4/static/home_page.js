const agreeBox = document.querySelector(".agree-box")
const loginBtn = document.querySelector(".login-btn")


loginBtn.addEventListener("click",(e)=>{
  e.preventDefault()
  if(agreeBox.checked === false){
    alert("Please check the checkbox first")
  }else{
    location.href="/login"
  }
})
