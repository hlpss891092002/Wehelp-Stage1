let hamburgerIcon = document.querySelector(".hamburger-icon");
let hamburgerList = document.querySelector(".hamburger-list");
let closeIcon = document.querySelector(".close-icon");
let smBOx= document.querySelectorAll(".sm-box")
hamburgerIcon.addEventListener('click', function(event) {
  hamburgerList.style.display = 'flex';
})
closeIcon.addEventListener('click', function(event){
  hamburgerList.style.display = 'none';
})
fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1")
.then(function(response){
    return response.json();})
.then((function(data){
  results = data.data.results;//台北市景點文字資料
  let divList=[];
  let sm1 = document.querySelectorAll(".sm-1");
  let sm2 = document.querySelectorAll(".sm-2");
  let sm3 = document.querySelectorAll(".sm-3");
  let bg1 = document.querySelectorAll(".bg-1");
  let bg2 = document.querySelectorAll(".bg-2");
  let bg3 = document.querySelectorAll(".bg-3");
  let bg4 = document.querySelectorAll(".bg-4");
  let bg5 = document.querySelectorAll(".bg-5");
  let bg6 = document.querySelectorAll(".bg-6");
  let bg7 = document.querySelectorAll(".bg-7");
  let bg8 = document.querySelectorAll(".bg-8");
  let bg9 = document.querySelectorAll(".bg-9");
  let bg10 = document.querySelectorAll(".bg-10");
  divList.push(sm1,sm2,sm3,bg1,bg2,bg3,bg4,bg5,bg6,bg7,bg8,bg9,bg10);
  // 
  for(let i=0; i < 3; i++){
    renderSMImg(divList[i],i);
    renderSMPromotion(divList[i],i)
  };
  function renderSMImg(divs, num){
    let img = results[num].filelist.toLowerCase().slice(0,results[num].filelist.toLowerCase().indexOf("jpg")+3);
    for (div of divs){
      let image = div.querySelector(".sm-img");
      image.src = img;
    };
  };
  function renderSMPromotion(divs, num){
    let title = results[num].stitle;
    for (div of divs){
      let promotion = div.querySelector("p");
      promotion.textContent = title;
    };
  };
  // render大方塊資料
  for(let i = 3; i < 14;i++){
    renderBGBackgroundImgAndTitle(divList[i],i);
  };
  function renderBGBackgroundImgAndTitle(divs,num){
    let img = results[num].filelist.toLowerCase().slice(0,results[num].filelist.toLowerCase().indexOf("jpg")+3);
    let title = results[num].stitle;
      for( div of divs){
        div.style.backgroundImage= `url("${img}")`;
        div.style.bcakgroundSize="100%";
        let p = div.querySelector("p");
        p.textContent = `${title}`;
        p.style.display = "-webkit-box";
        p.style.webkitBoxOrient = "vertical";
        p.style.webkitLineClamp = "1";
        p.style.wordWrap ="normal";

      };
    };
}));
