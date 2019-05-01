# Javascript event

1. 키보드 누르면

   ```javascript
   let y = 0
   let x = 0
   // 무엇을
   const dinoImage = document.querySelector('#dino')
   // 언제
   dinoImage.addEventListener('click', function(e){
   	// 무엇을
   	console.log(e)
   	// alert('크앙!')
   	const bgDiv = document.querySelector('.bg')
   	bgDiv.append('크앙')
   })
   		
   document.addEventListener('keydown', function(e){
   	console.log(e)
   	if (e.keyCode === 38){
   		console.log('위로가')
   		y -= 30
   		dinoImage.style.marginTop = `${y}px`
   		}
   	else if (e.keyCode === 37){
   		console.log('왼쪽')
   		x -= 30
   		dinoImage.style.marginLeft = `${x}px`
           }
   	else if (e.keyCode === 39){
   		console.log('오른쪽')
   		x += 30
   		dinoImage.style.marginLeft = `${x}px`
   		}
   	else if (e.keyCode === 40){
   		console.log('아래')
   		y += 30
   		dinoImage.style.marginTop = `${y}px`
   		}
   })
   ```

2. 복사 금지

   ```javascript
   document.addEventListener('copy', function(e){
           console.log(e)
           e.preventDefault()
           alert('철컹철컹 합니다. 복사하면 ㅡㅡ')
       })
   ```

3. 멍멍이 vs 키티 (버튼클릭시 이벤트 발생)

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>Document</title>
       <style>
           img {
               width: 300px;
               height: 300px;
           }
       </style>
   </head>
   <body>
       <h1>댕댕이 vs 키티</h1>
       <button id="dog">멍멍이 내놔</button>
       <button id="cat">애용이</button>
       <div id="animals"></div>
   
       <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
       <script>
           const getDogImage = function() {
                axios.get('https://dog.ceo/api/breeds/image/random')
               .then(response => response.data.message)
               .then(url => {
                   const imageTag = document.createElement('img')
                   imageTag.src = url
                   const animal = document.querySelector('#animals')
                   animal.append(imageTag)
               })
           }
           const getCatImage = function() {
                axios.get('https://api.thecatapi.com/v1/images/search')
               .then(response => response.data[0].url)
               .then(url => {
                   const imageTag = document.createElement('img')
                   imageTag.src = url
                   const animal = document.querySelector('#animals')
                   animal.append(imageTag)
               })
           }
           const dogbutton = document.querySelector('#dog')
           dogbutton.addEventListener('click', getDogImage)
           const catbutton = document.querySelector('#cat')
           catbutton.addEventListener('click', getCatImage)
       </script>
   </body>
   </html>
   ```

   



