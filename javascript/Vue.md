# Vue

### 1.basic

```html
<div id= "app">
        <button v-on:click="plus">count증가!</button>
        {{ message }} - {{ count }}
    </div>

	<!-- https://kr.vuejs.org/v2/guide/index.html 여기서 가져요기(아래 코드)-->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        const app = new Vue ({
            // element: 실제 vue와 연결 할 element
            el: '#app',
            // app (vue 인스턴스)의 속성을 가지게 된다.
            data: {
                message: 'Hello, Vue!',
                count: 0
            },
            methods: {
                plus: function(){
                    // arrow function : lexicial this
                    this.count ++
                }
            }
        })
    </script>
```



### 2.todo

```html
<div id="app">
        <!-- v-model : data의 newTodo 값이 사용자가 입력하는 값으로 변경됨. -->
        <input type="text" v-model="newTodo" v-on:keyup.enter="addNewTodo"><br>
        {{newTodo}}
        <button v-on:click="allCompleted">All completed</button>
        <ul>
            <!-- v-for가 우선, v-if가 나중 -->
            <li v-for="todo in todoList" v-if="!todo.completed">
                {{ todo.content }} <button v-on:click="check(todo)">완료</button>
            </li>
            <li v-else><del>{{todo.content}}</del>의 completed가 트루인것이에요 <button v-on:click="check(todo)">취소</button></li>
        </ul>
    </div>


    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        const app = new Vue({
            el: '#app',
            data: {
                newTodo: '',
                todoList: [
                    {
                        content: '쉬는 시간 공부하기',
                        completed: true
                    },
                    {
                        content: '전골먹기',
                        completed: false
                    },
                    {
                        content: '약속의 2시',
                        completed: false
                    },
                    {
                        content: '중청사기',
                        completed: false
                    }
                ]
            },
            methods: {
                check: function(todo){
                    todo.completed = !todo.completed
                },
                // check: function(todo){
                //     todo.completed = true
                // },
                // notcheck: function(todo){
                //     todo.completed = false
                // }
                addNewTodo: function(){
                    // this : vue 오브젝트(app)
                    // this.todoLis : data의 todoList
                    if (this.newTodo) {
                        this.todoList.push({
                            // this.newTodo : data의 newTodo (사용자가 입력을 한 값)
                            content: this.newTodo,
                            completed: false
                        })
                        this.newTodo = ''
                    }
                },
                allCompleted: function(){
                    this.todoList.forEach(function(todo){
                        todo.completed = true
                    })
                    // this.todoList.forEach(todo => {
                    //     if(!todo.completed){
                    //         this.check(todo)
                    //     }
                    // })
                }
            }
        })
    </script>
```



### 3.dogVue

```html
<div id="app">
        <h1>댕댕이 {{ dogCount }}마리</h1>
        <button v-on:click="getDogImage">댕댕이</button>
        <img v-for="image in images" v-bind:src="image">
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <script>
        const getDogImage = function() {
            axios.get('https://dog.ceo/api/breeds/image/random')
            .then(response =>{
                this.images.push(response.data.message)
                this.dogCount += 1  
            })
        }
        const app = new Vue({
            el: '#app',
            data: {
                images: [],
                dogCount: 0
            },
            methods: {
                getDogImage
            }
        })
    </script>
```

