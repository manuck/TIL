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