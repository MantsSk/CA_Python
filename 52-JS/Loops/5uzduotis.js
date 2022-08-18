const hours = 480
let lessonLength = 4
let days = hours/lessonLength

const courseDateList = []

// const cancelledDates = [
//     new Date("2022-05-04")
// ]

let lessonDate = new Date("2022-04-28")
let tempHours = 0

while(courseDateList.length < days) {
    let weekDay = lessonDate.getDay()
  
    if (weekDay == 1 || weekDay == 2  || weekDay == 3 || weekDay == 4) {
        courseDateList.push(new Date(lessonDate))
        lessonDate.setDate(lessonDate.getDate() + 1)
    }
    else {
        lessonDate.setDate(lessonDate.getDate() + 3)
    }
}   

for(let day of courseDateList)  {
  console.log(day)
}  