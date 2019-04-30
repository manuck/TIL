# Javascript

### 1.varible
```javascript
document.write('<h1>ssafy 최고</h1>')
```



변수 hoisting

자바스크립트에서 모든 선언과 관련된 (변수, 함수 등) 문장은 호이스팅 된다.

변수 1) 선언단계 2) 초기화 단계 3) 할당 단계를 거치게 된다.

```javascript
console.log(name)   // undefined
var name = '승만'
console.log(PhoneNumber) // PhoneNumber is not defined error(Reference Error)
```



let : 값을 바꿀 수 있다. (재선언, 재할당 가능)

const : 값을 바꿀 수 없다. (재할당 불가능)

var : 재선언 가능

```javascript
var a = 3
console.log(a)
var a = 5
console.log(a)
// 3 
// 5
```

```javascript
let b = 5
let b = 3 // 에러 발생
b = 3 // 가능
```



반복문을 통한 예시

1. var

   ```javascript
   for (var i = 0; i<3;i++){
       console.log(i)
   }
   console.log('====================')
   console.log(i)
   // 0,1,2
   // =====================
   // 3
   ```

2. let

   ```javascript
   for (let j = 0; j<3;j++){
       console.log(j)
   }
   console.log('====================')
   console.log(j)
   // 0,1,2
   // =====================
   // error
   ```



### 2.if

```javascript
const firstName = 'happy'
const lastName = 'hacking'
const name = firstName + lastName
// document.write('<h1>' + name + '</h1>')
// ES6+ : Template literal(템플릿 문자열)
document.write(`<h1>${name}</h1>`)  // ~쪽의 ` 
```



자바스크립트에서는 `===`이 비교 연산자이다. (python에서의 `==`)

`===` : 일치함을 비교 (값, 타입) [반대:`!==`]

`==` : 동등함을 비교(값) - 타입이 암묵적 변환 [반대:`!=`]

ex) 123 == '123' : true

```javascript
let userName = prompt('너 누구냐?')
let message
// document.write(message)
    
if (userName === '성민'){
    message = `<h1>${userName}이는 나가있어.</h1>`
} else if (userName === '슬기'){
    message = `<h1>${userName}는 일하자!</h1>`
} else {
    message = `<h1>${userName}은 수업듣자</h1>`
}
document.write(message)
```



### 3.loop

1. while

   ```javascript
   let i = 0
   while (i<10) {
       console.log(i)
       i++
   }    
   ```

2. for

   ```javascript
   for (let j=0; j < 10; j++) {
       console.log(j)
   }
   ```

3. for of : 배열 반복문

   ```javascript
   let mtArray = [1, 2, 3]
   for (let k of mtArray) {
       console.log(k)
   }
   ```

   

### 4.object

자바스크립트 object 표기법

```javascript
let seungman = {
    name : 'seungman',
    age : 26,
    number : '010-1111-1111'
}
console.log(seungman.name) // 'seungman'
console.log(seungman.age) // 26
console.log(typeof seungman) // object
console.log(typeof [1,2,3]) // object
```



ES6+ 추가 오브젝트 표현법

```javascript
// 변수를 그대로 넣으면, 변수면: 값
let name = 'sungmin'
let stuffs = ['텀블러', '안경']
let sungmin = {
    name,
    stuffs
}
// json <-> object
```



### 5.function

1. 함수 선언식

   ```javascript
   function add(num1, num2) {
       return num1 + num2
   }
   console.log(add(1, 3))
   ```

2. 함수 표현식

   ```javascript
   let add2 = function (num1, num2) {
       return num1 + num2
   }
   console.log(add2(1, 3))
   ```

3. ES6+ Arrow Function

   ```javascript
   let sub = (num1, num2) => {
       return num1-num2
   }
   ```

   1) 인자가 하나인 경우, () 생략 가능

      단순 리턴인 경우, {} 및 리턴 키워드 생략 가능

   ```javascript
   let greeting = name => `${name}, 안녕!`
   console.log(greeting('성민'))
   let mul = (num1, num2) => (num1*num2)
   console.log(mul(5,6))
   ```

   2) 인자가 없는 경우에는 () 작성

   ```javascript
   let hello = () => 'hello, world!'
   console.log(hello)
   ```

   3) object 리턴 시 반드시 {} 묶어서 작성

   ```javascript
   let me = (name, age) => ({name, age})
   console.log(me('hi', 3))
   ```

   4) 만약, default args (기본인자)

   ```javascript
   let bonjour = (name='동명') => `${name}, bonjour`
   ```

4. 익명 함수

   ```javascript
   (function (num) {return num*num})
   ```

5. 즉시 실행 함수 (익명함수 + 호출) - IIFE (Immediately Invoked Function Expression)

   ```javascript
   (num => num*num)(5)
   ```





### 6.callback 함수

```javascript
// 배열을 받아서 다 더해주는 함수를 작성 해주세요.
// numberAddEach(numbers)
const numberAddEach = numbers => {
    let sum = 0
    for (const number of numbers){
        sum += number
    }
    return sum
}
console.log(numberAddEach([1,2,3])) // 6

// 배열을 받아서 다 빼주는 함수를 작성 해주세요.
const numberSubEach = numbers => {
    let sum = 0
    for (const number of numbers){
        sum -= number
    }
    return sum
}
console.log(numberSubEach([1,2,3])) // -6

// 배열을 받아서 다 곱해주는 함수를 작성 해주세요.
const numberMulEach = numbers => {
    let sum = 1
    for (const number of numbers){
        sum *= number
    }
    return sum
}
console.log(numberMulEach([1,2,3])) // 6
/* 위에까지 보노보노 */
const numberEach = (numbers, calc) => {
    let result
    for (const number of numbers) {
        result = calc(number, result)
    }
    return result
}

const addEach = (number, result=0) => result + number
const subEach = (number, result=0) => result - number
const mulEach = (number, result=1) => result * number
// 콜백
console.log(numberEach([10,20,30], addEach))
console.log(numberEach([10,20,30], subEach))
console.log(numberEach([10,20,30], mulEach))
/* 익명함수 + 콜백 */
console.log(numberEach([10,20,30], (number, result=0) => result + number))
console.log(numberEach([10,20,30], function(number, result=0){
    return result + number
}))
```









