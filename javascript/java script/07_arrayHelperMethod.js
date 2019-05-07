// 1. 배열 반복하면서 출력
const avengers = ['캡틴아메리카', '토르', '헐크', '아이언맨', '블랙위도우', '호크아이']
avengers.forEach(heroName => console.log(heroName))
avengers.forEach(function (heroName, index, array) {
    console.log(heroName, index)
})
// 2. map
const numbers = [1, 2, 3]
const strNumbers = numbers.map(number => String(number))
console.log(strNumbers)
const squreNumbers = numbers.map(number => number*number)
const squreNumbers2 = numbers.map(function(number){
    return number*number
})
console.log(squreNumbers)
console.log(squreNumbers2)
// 'velocity' * 'time' 배열로 출력
const seulgi = [
    {'velocity': 40, 'time': 50},
    {'velocity': 100, 'time': 60},
    {'velocity': 20, 'time': 100},
]
// 방법 1
const distances = seulgi.map(obj => obj.velocity * obj.time)
console.log(distances)

// 방법 2
const distances2 = seulgi.map(function(obj){
    return obj.velocity * obj.time
})
console.log(distances2)

// 3. filter
// 짝수만 
const nums = [1, 5, 6, 8]
const evenNums = nums.filter(num => num%2 === 0)
// const evenNums = nums.filter(function(num){
//     return num%2 === 0
// })
console.log(evenNums) 
// 카페인이 아닌것만
const drinks = [
    {type: 'caffeine', name: 'cold brew'},
    {type: 'caffeine', name: 'green tea'},
    {type: 'juice', name: 'orange'},
    {type: 'juice', name: 'mango'},
]
const noncaffeine = drinks.filter(obj => obj.type !== 'caffeine')
                        .map(obj => obj.name)
console.log(noncaffeine)

// 4. reduce
const reduceNum = [1, 5, 6]
const reduceResult = reduceNum.reduce((result, num) => {
    console.log(result)
    return result + num*10
}, 0)
console.log(reduceResult)

// 5. find
const dc = ['슈퍼맨', '배트맨', '조커']
const badguy = dc.find(name => name === '조커')
console.log(badguy)
