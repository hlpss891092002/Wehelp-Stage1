const agreeBox = document.querySelector(".agree-box")
const loginBtn = document.querySelector(".login-btn")
const signOut = document.querySelector("#sign-out")

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

signOut.submit()