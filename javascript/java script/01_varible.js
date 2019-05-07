// alert('자바스크립트, 안녕!')
/*
console.log('안녕?')
console.log('잘가')
*/
document.write('<h1>ssafy 최고</h1>')
    

// 변수 hoisting
// 자바스크립트에서 모든 선언과 관련된 (변수, 함수 등) 문장은 호이스팅 된다.
// 변수 1) 선언단계 2) 초기화 단계 3) 할당 단계를 거치게 된다.
console.log(name)   // undefined
var name = '승만'
console.log(PhoneNumber) // PhoneNumber is not defined error(Reference Error)
 
// let(값을 바꿀수있다), const(값을 바꿀수없다) 키워드 (ES6+)
// var : 재선언 가능
var a = 3
console.log(a)
var a = 5
console.log(a)
   
let b = 5
let b = 3 // 에러 발생

// 0,1,2
// =====================
// 3
for (var i = 0; i<3;i++){
    console.log(i)
}
console.log('====================')
console.log(i)

// 0,1,2
// =====================
// error
for (let j = 0; j<3;j++){
    console.log(j)
}
console.log('====================')
console.log(j)
