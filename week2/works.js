//  --------------------task1-------------------
 function findAndPrint(messages, currentStation){
 // your code here
  const stationInfo = [
    {"name": "Songshan", "line": "G", "codeNumber":0 },
    {"name": "Nanjing Sanmin", "line": "G", "codeNumber":1 },
    {"name": "Taipei Arena", "line": "G", "codeNumber":2 },
    {"name": "Nanjing Fuxing", "line": "G", "codeNumber":3 },
    {"name": "Songjiang Nanjing", "line": "G", "codeNumber":4 },
    {"name": "Zhongshan", "line": "G", "codeNumber":5 },
    {"name": "Beimen", "line": "G", "codeNumber":6 },
    {"name": "Ximen", "line": "G", "codeNumber":7 },
    {"name": "Xiaonanmen", "line": "G", "codeNumber":8 },
    {"name": "Chiang Kai-Shek Memorial Hal", "line": "G", "codeNumber": 9},
    {"name": "Guting", "line": "G", "codeNumber": 10},
    {"name": "Taipower Building", "line": "G", "codeNumber": 11},
    {"name": "Gongguan", "line": "G", "codeNumber": 12},
    {"name": "Wanlong", "line": "G", "codeNumber": 13},
    {"name": "Jingmei", "line": "G", "codeNumber": 14},
    {"name": "Dapinglin", "line": "G", "codeNumber": 15},
    {"name": "Qizhang", "line": "G", "codeNumber": 16},
    {"name": "Xiaobitan", "line": "G-A", "codeNumber": 1},
    {"name": "Xindian City Hall", "line": "G", "codeNumber": 17},
    {"name": "Xindian", "line": "G", "codeNumber": 18} 
  ];
  let currentStationLine = "";
  let currentStationCode = 0;
  let messagesPerson = "";
  let closest = 19;

  function renderCurrentStationData (){
    for (info of stationInfo){
        if(info.name === currentStation){
          currentStationCode = info.codeNumber;
          currentStationLine = info.line;
        };
    }

  }
  function compareCode (currentStation){
      let result = 0;
    for( info of stationInfo){
      for(j in messages){
        if(messages[j].includes(info.name)){
          if(currentStationLine !== info.line){
            result = 1 + Math.abs(16-currentStationCode);
            if(closest > result){
              closest = result;
              messagesPerson = j;
            };
          }else if ( currentStationLine == info.line){
            result = Math.abs(info.codeNumber - currentStationCode)
              if(closest > result){
              closest = result;
              messagesPerson = j;
            };
          };
        };
      };
    };
  };
  renderCurrentStationData();
  compareCode();
  console.log(messagesPerson);
 }

 const messages={
 "Bob":"I'm at Ximen MRT station.",
 "Mary":"I have a drink near Jingmei MRT station.",
 "Copper":"I just saw a concert at Taipei Arena.",
 "Leslie":"I'm at home near Xiaobitan station.",
 "Vivian":"I'm at Xindian station waiting for you."
 };
 findAndPrint(messages, "Wanlong"); // print Mary
 findAndPrint(messages, "Songshan"); // print Copper
 findAndPrint(messages, "Qizhang"); // print Leslie
 findAndPrint(messages, "Ximen"); // print Bob
 findAndPrint(messages, "Xindian City Hall"); // print Vivian

 
 // --------------------task2-------------------
  const consultants=[
 {"name":"John", "rate":4.5, "price":1000},
 {"name":"Bob", "rate":3, "price":1200},
 {"name":"Jenny", "rate":3.8, "price":800}
 ];
 // your code here, maybe
 let consultantsList = [...consultants];
 function book(consultants, hour, duration, criteria){
 // your code here
 
 let availableList = [];
 
 function inSertOccupyTime(){
    for( i of consultantsList){
      if(!i.occupiedTime){
        i.occupiedTime = [];
      };
    };
 };
function getAvailableList(){
  let orderPeriod = [];
  for(let j = hour; j < hour + duration; j++ ){
    orderPeriod.push(j);
  };
  consultantsList.forEach((ele)=>{
    function check(item){
      return !ele.occupiedTime.includes(item);
    };
    if(orderPeriod.every(check)){
      availableList.push(ele);
    }else{
      return
    };
  })

};
function selectConsultant (){
  let result = 0;
  let selectConsultantName = "";
  if(criteria === "price"){
     result = 10000;
      for (i of availableList){
        if(i[criteria] < result){
          result =  i[criteria];
          selectConsultantName = i.name;
        };
      };
  }else if(criteria === "rate") {
    result = 0;
      for (i of availableList){
        if(i[criteria] > result ){
          result =  i[criteria];
          selectConsultantName = i.name;
        };
      };
  };
  return selectConsultantName;
}; 
function orderHour (name){
  if(availableList.length === 0){
    console.log("No service");
  }else{
    for( i of consultantsList){
      if(i.name === name){
        for(let j = hour; j <hour + duration; j++ ){
          i.occupiedTime.push(j);
        };
      };
    };
    console.log(name);
  }

}

 inSertOccupyTime();
 getAvailableList();
 let theChosenOne = selectConsultant();
 orderHour(theChosenOne);
 };

 book(consultants, 15, 1, "price"); // Jenny
 book(consultants, 11, 2, "price"); // Jenny
 book(consultants, 10, 2, "price"); // John
 book(consultants, 20, 2, "rate"); // John
 book(consultants, 11, 1, "rate"); // Bob
 book(consultants, 11, 2, "rate"); // No Service
 book(consultants, 14, 3, "price"); // John

// --------------------task3-------------------
 function func(...data){
 // your code here
 let nameList = [...data];
let sameLetter = [];
let differName = [];
let midNameArray = sliceWords();

function sliceWords(){
   let  midNameArray1 =nameList.map((ele)=>{
    if(ele.length < 3){
      return [...ele.slice(1,2)];
    }else{
      return [...ele.slice(1,ele.length-1)];
    }
 })
    return(midNameArray1);
};

function figureOutSame(){
 for(let i = 0; i < midNameArray.length; i++){
  for(let j = midNameArray.length-1; j>= 0 ; j--){
    if(i === j ){
      continue;
    }
      for(letter of midNameArray[i]){   
      if(midNameArray[j].includes(letter)){
        sameLetter.push(nameList[j]);
      };
    } ;
  };
 };
};

function printResult(){
 for(names of nameList){
    if(!sameLetter.includes(names)){
      differName.push(names);
    };
  } ;
  if(differName.length === 0){
    console.log("沒有");
  }else{
    console.log(...differName);
  };

};
figureOutSame();
printResult();

};

func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安

// --------------------task4-------------------
function getNumber(index){
 // your code here
 let array =[];
 let num = 0;
 for(let i = 0; i <= index+1; i++){
    if(i === 0){
      num += 0;
      array.push(num);
    }else if(i % 3 === 1){
      num += 4;
      array.push(num);
    }else if(i % 3 === 2){
      num += 4;
      array.push(num);  
    }else if(i % 3 === 0){
      num -= 1;
      array.push(num);
    };
  };
  console.log(array[index]);
 };

 getNumber(1); // print 4
 getNumber(5); // print 15
 getNumber(10); // print 25
 getNumber(30); // print 70

//  --------------------task5-------------------
function find(spaces, stat, n){
 // your code here
 let min = n;
 let carNum = -1;
 for(let i = 0; i < spaces.length; i++){
  let menus = spaces[i] - n;
  if(menus < n && menus >= 0 && stat[i] === 1){
     min = menus;
     carNum = i;
  }
 }
 console.log(carNum);
}
 find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2); // print 5
 find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print-1
 find([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2