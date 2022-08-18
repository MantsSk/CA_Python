const hours = 480
let lessonLength = 4
let days = hours/lessonLength

const courseDateList = []

const cancelledDatesString = [
    "2022-05-03", "2022-05-04", "2022-08-18",
    "2022-05-10", "2022-05-11", "2022-08-25"
]

let lessonDate = new Date("2022-04-28")
let tempHours = 0

while(courseDateList.length < days) {
    let weekDay = lessonDate.getDay()
    let lessonDateString = lessonDate.toISOString().split('T')[0]
    
    if (weekDay == 1 || weekDay == 2  || weekDay == 3 || weekDay == 4) {
        if (cancelledDatesString.includes(lessonDateString)) {
            lessonDate.setDate(lessonDate.getDate() + 1)
        }
        else {
            courseDateList.push(new Date(lessonDate))
            lessonDate.setDate(lessonDate.getDate() + 1)
        }
    }
    else {
        lessonDate.setDate(lessonDate.getDate() + 3)
    }
}   

for(let day of courseDateList)  {
  console.log(day)
  console.log(day.toISOString().split('T')[0])
}  