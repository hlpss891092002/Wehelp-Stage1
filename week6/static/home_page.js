const signinUsername = document.querySelector(".signin-username")
const signinPassword = document.querySelector(".signin-password")
const loginBtn = document.querySelector(".login-btn")
const signupBtn= document.querySelector(".signup-btn")
const signupName =document.querySelector(".signup-name-input")
const signupUsername =document.querySelector(".signup-username-input")
const signupPassword =document.querySelector(".signup-password-input")

loginBtn.addEventListener("click",(e)=>{
  // 
  if(signinUsername.value === "" || signinPassword.value === ""){
    e.preventDefault()
  }

})

signupBtn.addEventListener("click",(e)=>{
  // 
  if (signupName.value ==="" ||  signupUsername.value ==="" || signupPassword.value === ""){
    e.preventDefault()
  }
  
 
})
