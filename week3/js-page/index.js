let hamburgerIcon = document.querySelector(".hamburger-icon");
let hamburgerList = document.querySelector(".hamburger-list");
let closeIcon = document.querySelector(".close-icon");
let boxContainer = document.querySelector(".box-container")
let smallBoxContainer = document.querySelector(".small-box-container");
let bigBoxContainer = document.querySelector(".big-box-container");
let windowWidth1200 = window.matchMedia("(max-width: 1200px)");
let moreButton = document.querySelector(".more-info") ;
let rawData=[];
let count = 0;
let bigBoxStart = 3;
let loadAmount = 10;
// 開啟/關閉側邊攔
hamburgerIcon.addEventListener('click', function(event) {
  hamburgerList.className="hamburger-list-display";
});
closeIcon.addEventListener('click', function(event){
  hamburgerList.className="hamburger-list";
});


// 連線資料
fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1")
.then((response)=>{
  return response.json();
}).then((data)=>{
  let results = data.data.results;
  function renderSmallBoxData (){
    for( let i = 0; i < 3; i++) {
    let title = results[i].stitle;
    let imgSrc = results[i].filelist.toLowerCase();
    let firstImg = imgSrc.slice(0,imgSrc.indexOf("jpg")+3)
    let smallBox = document.createElement("div");//創造小箱子
    smallBox.className = `small-box sb-${i}`;
    let smallImg = document.createElement("img");//創造圖片
    smallImg.className="small-img";
    smallImg.src=`${firstImg}`;
    smallImg.alt = "small-image";
    let smallTitle = document.createElement('p');//創造文字框
    smallTitle.className="small-title";
    smallTitle.textContent=`${title}`;
    smallBox.appendChild(smallImg);//推smallBox
    smallBox.appendChild(smallTitle); 
    smallBoxContainer.appendChild(smallBox);//嘉進container
    };
  };
  
  function renderBigBoxData(start, amount){
    for( let i = start; i < start + amount; i++) {
    let title = results[i].stitle;
    let imgSrc = results[i].filelist.toLowerCase();
    let firstImg = imgSrc.slice(0,imgSrc.indexOf("jpg")+3)
    let bigBox = document.createElement("div");//創造小箱子
    bigBox.className = `big-box bg-${count}`;
    bigBox.style.backgroundImage=`url(${firstImg})`
    let bigTitle = document.createElement('p');//創造文字框
    bigTitle.textContent=`${title}`;
    bigTitle.className="big-title";
    let star = document.createElement('img');
    star.src="./icon/star.png";
    star.className="star";
    bigBox.appendChild(star);
    bigBox.appendChild(bigTitle); //推bigBox
    bigBoxContainer.appendChild(bigBox);//嘉進container
    count+=1;
    };
    bigBoxStart = start + amount;
    changeLastBoxSize();
  };
  function clearBigBoxGridCss(){
    AllBigBox = document.querySelectorAll(".big-box");
    for( box of AllBigBox ){
      box.style.gridColumnEnd="auto";
      box.style.gridColumnStart="auto";
    };
  };
  function changeLastBoxSize(){ 
    if(window.innerWidth <= 1200 && count % 4 ===2 ){
      let last1 = document.querySelector(`.bg-${count-2}`);
      let last2 = document.querySelector(`.bg-${count-1}`);
      last1.style.gridColumnStart = "1";
      last1.style.gridColumnEnd = "3";
      last2.style.gridColumnStart = "3";
      last2.style.gridColumnEnd = "5";
    }else if(window.innerWidth <= 1200 && count % 4 ===3 ){
      let last1 = document.querySelector(`.bg-${count-1}`);
      last1.style.gridColumnStart = "3";
      last1.style.gridColumnEnd = "5";
    }
  }
  function clearLastBoxGrid(){ 
    if(window.innerWidth >= 1200 && count % 4 ===2 ){
      let last1 = document.querySelector(`.bg-${count-2}`);
      let last2 = document.querySelector(`.bg-${count-1}`);
      last1.style.gridColumnStart = "auto";
      last1.style.gridColumnEnd = "auto";
      last2.style.gridColumnStart = "auto";
      last2.style.gridColumnEnd = "auto";
    }else if(window.innerWidth >= 1200 && count % 4 ===3 ){
      let last1 = document.querySelector(`.bg-${count-1}`);
      last1.style.gridColumnStart = "auto";
      last1.style.gridColumnEnd = "auto";
    }
  }

  renderSmallBoxData();
  renderBigBoxData(bigBoxStart,loadAmount);
  

  // more 監聽器+計算剩餘數據數
  moreButton.addEventListener("click",(event)=>{
    clearBigBoxGridCss();
    renderBigBoxData(bigBoxStart,loadAmount);
    let remain = (results.length)-bigBoxStart;
    if(remain < loadAmount && remain > 0){
      loadAmount = remain;
    }else if (remain === 0){
      moreButton.style.display="none";
      let loadOver = document.createElement("div");
      loadOver.className="load-over";
      let loadOverContent = document.createElement("p");
      loadOverContent.className="load-over-content";
      loadOverContent.textContent="All data are loaded";
      loadOver.appendChild(loadOverContent);
      boxContainer.appendChild(loadOver);
    };

}); 
  window.addEventListener("resize", (event) => {
    if( window.innerWidth <= 1200) {
      changeLastBoxSize()
    }else{
      clearLastBoxGrid()
    }
  })
})

