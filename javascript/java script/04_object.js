// 자바스크립트 데이터타입 - 원시타입(primitive type)
// Boolean(true, false), null, undefined, number, string

// 자바스크립트 object 표기법
let seungman = {
    name : 'seungman',
    age : 26,
    number : '010-1111-1111'
}
console.log(seungman.name) // 'seungman'
console.log(seungman.age) // 26
console.log(typeof seungman) // object
console.log(typeof [1,2,3]) // object

// ES6+ 추가 오브젝트 표현법
// 변수를 그대로 넣으면, 변수면: 값
let name = 'sungmin'
let stuffs = ['텀블러', '안경']
let sungmin = {
    name,
    stuffs
}
// json <-> object
let jsonData = JSON.stringify(sungmin)
let jsonParse = JSON.parse(jsonData)