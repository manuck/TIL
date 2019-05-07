const firstName = 'happy'
const lastName = 'hacking'
const name = firstName + lastName
// document.write('<h1>' + name + '</h1>')
// ES6+ : Template literal(템플릿 문자열)
document.write(`<h1>${name}</h1>`)  // ~쪽의 ` 

let userName = prompt('너 누구냐?')
let message
// document.write(message)
    
// 자바스크립트에서는 ===이 비교 연산자이다. (python에서의 ==)
// === : 일치함을 비교(값, 타입)
// == : 동등함을 비교(값) : 타입이 암묵적 변환
// 123 == '123' : true
// !==
// !=
if (userName === '성민'){
    message = `<h1>${userName}이는 나가있어.</h1>`
} else if (userName === '슬기'){
    message = `<h1>${userName}는 일하자!</h1>`
} else {
    message = `<h1>${userName}은 수업듣자</h1>`
}
document.write(message)