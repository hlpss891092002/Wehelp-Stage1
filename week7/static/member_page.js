const apiMemberForm = document.getElementById("api-member-form")
const apiMemberInput = document.getElementById("api-member-input")
const apiMemberBtn = document.getElementById("api-member-btn")
const messageList = document.querySelector(".messages-list")
const updateForm = document.getElementById("update-form")
const updateNameInput = document.getElementById("update-name-input")
const updateNameBtn = document.getElementById("update-name-btn")
const memberWelcome = document.getElementById("member-welcome")
const loadMessageBtn = document.querySelector(".load-message-btn")
const messageInputBtn = document.querySelector(".message-input-btn")


let messages = null
let messageAmount = 0
function createMessage (id, message){
  let messageBlock = document.createElement("div")
  messageBlock.className="message"
  let messageForm = document.createElement("form")
  messageForm.setAttribute("method", "post")
  messageForm.setAttribute("action", "/deleteMessage")
  messageForm.className = "message-form"
  let messageSpan = document.createElement("span")
  messageSpan.className = "message-text"
  messageSpan.innerText = `${message.name} : ${message.content}`
  let messageId = document.createElement("input")
  messageId.setAttribute("type", "hidden")
  messageId.setAttribute("name", "message_id")
  messageId.setAttribute("value", `${message.message_id}`)
  let messageDelete = document.createElement("input")
  messageDelete.setAttribute("type", "submit")
  messageDelete.setAttribute("value", "x")
  messageForm.appendChild(messageSpan)
  messageForm.appendChild(messageId)
  if(id === message.member_id){
    messageForm.appendChild(messageDelete)
  }
  messageBlock.appendChild(messageForm)
  messageList.appendChild(messageBlock)
  // console.log(messageList)
}

function loadMessages(){
  fetch("/api/message")
  .then((response)=>{
    return response.json()
  })
  .then((response)=>{
    messages = response
    // console.log(messages.messages)
    for (let i = 0; i < 5; i++){
      id = messages.id
      message = messages.messages[i]
      createMessage(id, message )
      messageAmount += 1
      console.log(messageAmount)
    }
})
}

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

function deleteOldMessages(){
  let messagesList = document.querySelectorAll(".message")
  for (message of  messagesList){
    message.remove()
  }
}

loadMessages()


messageInputBtn.addEventListener("click", (e)=>{
  e.preventDefault()
})



apiMemberBtn.addEventListener("click",(e)=>{
  e.preventDefault()
  let inputValue = apiMemberInput.value
  if (inputValue !== ""){
      fetch(`/api/member?username=${inputValue}`)
    .then((response)=> {
      return response.json();
    })
    .then((response) =>{
      let memberData = response.data
      // console.log(memberData)
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
  }
})

updateNameBtn.addEventListener("click",(e)=>{
    e.preventDefault()
    // console.log(updateNameInput.value)
    const messageForm = document.querySelector(".message-form")
    console.log(messageForm)
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
            messageAmount = 0
            deleteOldMessages()
            loadMessages()
          }else{
            updateTextBlock.innerText = "更新成功"
            updateWelcomeName(updateNameInput.value)
            updateNameInput.value = ""
            messageAmount = 0
            deleteOldMessages()
            loadMessages()
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

loadMessageBtn.addEventListener("click", (e)=>{
  e.preventDefault()
  let starNum = messageAmount
  let menus = messages.messages.length - starNum 
  if (menus >= 5){
    for (let i = starNum ; i < starNum + 5; i++){
      id = messages.id
      message = messages.messages[i]
      createMessage(id, message )
      messageAmount += 1
      // console.log(messageAmount)
    }
  }else{
      for (let i = starNum ; i < menus + 5; i++){
      id = messages.id
      message = messages.messages[i]
      createMessage(id, message )
      messageAmount += 1
      // console.log(messageAmount)
    }
  }

})
