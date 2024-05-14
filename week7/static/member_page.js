const apiMemberForm = document.getElementById("api-member-form")
const apiMemberInput = document.getElementById("api-member-input")
const apiMemberBtn = document.getElementById("api-member-btn")


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
      console.log(memberDataDiv)
      
      if(!memberDataDiv){
        console.log(memberData === "null")
        let memberDataDiv = document.createElement("div")
        memberDataDiv.setAttribute("id", "member-data-div")
        let memberInfo = document.createElement("p")
        memberInfo.className="member-data-text"
        if(memberData==="null"){
          memberInfo.innerText="查無此人"
        }else{
          memberInfo.innerText=`${memberData.name} (${memberData.username})`
        }
        memberDataDiv.appendChild(memberInfo)
        apiMemberForm.appendChild(memberDataDiv)
      }else{
        console.log(memberData === "null")
        const memberDataText = document.querySelector(".member-data-text")
        if(memberData==="null"){
          memberDataText.innerText="查無此人"
        }else{
          memberDataText.innerText=`${memberData.name} (${memberData.username})`
        }
      }
    })
    .catch((error) => {
      console.log("error")
    }) 
})
