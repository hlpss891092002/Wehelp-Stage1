const apiMemberForm = document.getElementById("api-member-form")
const apiMemberInput = document.getElementById("api-member-input")
const apiMemberBtn = document.getElementById("api-member-btn")
const updateForm = document.getElementById("update-form")
const updateNameInput = document.getElementById("update-name-input")
const updateNameBtn = document.getElementById("update-name-btn")
const memberWelcome = document.getElementById("member-welcome")

apiMemberBtn.addEventListener("click",(e)=>{
  e.preventDefault()
  let inputValue = apiMemberInput.value
  fetch(`/api/member?username=${inputValue}`)
    .then((response)=> {
      return response.json();
    })
    .then((response) =>{
      let memberData = response.data
      console.log(memberData)
      const memberDataDiv = document.getElementById("member-data-div")
      if(!memberDataDiv){
        let memberDataDiv = document.createElement("div")
        memberDataDiv.setAttribute("id", "member-data-div")
        let memberInfo = document.createElement("p")
        memberInfo.className="member-data-text"
        if(memberData===null){
          memberInfo.innerText="查無此人"
        }else{
          memberInfo.innerText=`${memberData.name} (${memberData.username})`
        }
        memberDataDiv.appendChild(memberInfo)
        apiMemberForm.appendChild(memberDataDiv)
      }else{
        const memberDataText = document.querySelector(".member-data-text")
        if(memberData===null){
          memberDataText.innerText="查無此人"
        }else{
          memberDataText.innerText=`${memberData.name} (${memberData.username})`
        }
      }
      apiMemberInput.value = ""
    })
    .catch((error) => {
      console.log("error");
    })
    a 
})



updateNameBtn.addEventListener("click",(e)=>{
    e.preventDefault()
    console.log(updateNameInput.value)
    if(updateNameInput.value !== ""){
      fetch(`/api/member`,{
        method: "PATCH",
        body:JSON.stringify({
          "name": `${updateNameInput.value}`
        }),
        headers: {
          'Content-type': 'application/json',
        },
      })
      .then(response => response.json())
      .then(response => {
        let updateTextBlock = document.querySelector(".update-text")
        if(response.ok){
          if(!updateTextBlock){
            createUpdateBlock("更新成功")
            updateWelcomeName(updateNameInput.value)
            updateNameInput.value = ""
          }else{
            updateTextBlock.innerText = "更新成功"
            updateWelcomeName(updateNameInput.value)
            updateNameInput.value = ""
          }
          
        }else{
          if(!updateTextBlock){
            createUpdateBlock("更新失敗")
            updateNameInput.value = ""
          }else{
            updateTextBlock.innerText = "更新失敗"
            updateNameInput.value = ""
          }
        } 
      })
      

    }
    
})

function updateWelcomeName (updateName){
  memberWelcome.innerText=`${updateName}，歡迎登入系統`
}

function createUpdateBlock(updateInfo){
  let updateDiv = document.createElement("div")
  updateDiv.className = "update-info"
  let updateText =document.createElement("p")
  updateText.className = "update-text"
  updateText.innerText = `${updateInfo}`
  updateDiv.appendChild(updateText)
  updateForm.appendChild(updateDiv)
}