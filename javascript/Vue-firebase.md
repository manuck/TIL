# Vue-firebase

[firebase](https://firebase.google.com/?gclid=CjwKCAjw2cTmBRAVEiwA8YMgzfkQDiatbDbUi7CoEBFKWGHvEBSNchPKOwVpICHsuErWNjU3Ox1M_BoCct0QAvD_BwE) 홈페이지 



### 1. todofire.html

1. CDN 설정 (head에)

   ```html
   <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
   <!-- Firebase -->
   <script src="https://gstatic.com/firebasejs/5.9.1/firebase.js"></script>
   <!-- VueFire -->
   <script src="https://unpkg.com/vuefire/dist/vuefire.js"></script>
   <script>
       // Initialize Firebase
       // TODO: Replace with your project's customized code snippet
       const config = {
         apiKey: "AIzaSyAaiy19QqIyj0-aar-ocO7oR3wYfsBZgns",
         databaseURL: "https://vue-project-sm.firebaseio.com/",
         projectId: "vue-project-sm",
       };
       firebase.initializeApp(config);
       const db = firebase.database()
   </script>
   ```

   

2. @change 추가

   ```html
   <input type="checkbox" v-model="todo.completed" @change="updateTodo(todo)">
   ```

3. app 에 firebase 추가

   ```javascript
   firebase: {
   	todoList: db.ref('todoList')
   },
   ```

4. `app`에 `addNewTodo` 수정

   ```javascript
   addNewTodo: function(){
   	// this : vue 오브젝트(app)
   	// this.todoLis : data의 todoList
       if (this.newTodo) {
       	this.$firebaseRefs.todoList.push({
           	// this.newTodo : data의 newTodo (사용자가 입력을 한 값)
               id: Date.now(),
               content: this.newTodo,
               completed: false
           })
           this.newTodo = ''
       }
   },
   ```

5. `app`에 `deleteTodo` 수정

   ```javascript
   deleteTodo: function(todo) {
   	//this.todoList.splice(this.todoList.indexOf(todo), 1)
       this.$firebaseRefs.todoList.child(todo['.key']).remove()
   },
   ```

6. `app`에 `updateTodo` 추가

   ```javascript
   updateTodo: function(todo) {
   	const copy = {...todo}
       delete copy['.key']
       this.$firebaseRefs.todoList.child(todo['.key']).set(copy)
   },
   ```

   





### 2. chat.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <!-- Firebase -->
    <script src="https://gstatic.com/firebasejs/5.9.1/firebase.js"></script>
    <!-- VueFire -->
    <script src="https://unpkg.com/vuefire/dist/vuefire.js"></script>
    <script src="https://cdn.firebase.com/libs/firebaseui/3.6.0/firebaseui.js"></script>
    <link type="text/css" rel="stylesheet" href="https://cdn.firebase.com/libs/firebaseui/3.6.0/firebaseui.css" />
    <script>
        // Initialize Firebase
        // TODO: Replace with your project's customized code snippet
        const config = {
            apiKey: "AIzaSyAaiy19QqIyj0-aar-ocO7oR3wYfsBZgns",
            databaseURL: "https://vue-project-sm.firebaseio.com/",
            projectId: "vue-project-sm",
        };
        firebase.initializeApp(config);
        const db = firebase.database()
        const auth = firebase.auth()
        const ui = new firebaseui.auth.AuthUI(auth)
        ui.start('#firebaseui-auth-container')
    </script>
    <style>
        .chat-container {
            width: 650px;
            margin: auto;
        }
        .chat {
            width: 161px;
            height: 80px;
            padding: 10px;
            border: 1px solid seashell;
            background-color: darkorange;
            color: white;
            opacity: 0.7;
            border-radius: 10px;
        }
        .my-chat {
            margin-left : auto;
            background-color: green;
            color: white;
            border-radius: 10px;
        }
        input {
            margin: 10px;
            width: 100px;
            border-radius: 5px;
        }
    </style>
</head>

<body>
    <div id="app">
        <div class="chat-container" v-if="currentUser.uid">
            <button @click="logout">로그아웃</button>
                <div v-for="message in messages" :class="{'chat':true, 'my-chat':currentUser.username === message.username}">
                    <b>{{ message.username }}</b> : {{message.content}}
                </div>
            <input type="text" v-model="newContent" v-on:keyup.enter="createMessage"><br>
        </div>
        <div v-else>
            <div id="firebaseui-auth-container"></div>
        </div>
    </div>

    <script>
        const app = new Vue({
            el: '#app',
            data: {
                newContent: '',
                // messages: [
                //     { 'username': '승만', 'content': '배부르다.' },
                //     { 'username': '심심이', 'content': '졸리다.' }

                // ],
                currentUser: {
                    uid: '',
                    email: '',
                    username: ''
                }
            },
            firebase: {
                messages: db.ref('messages')
            },
            // 실제로 실행됨(마운트됨)과 동시에 실행되는 함수
            mounted: function () {
                auth.onAuthStateChanged((user) => {
                    if (user) {
                        this.currentUser.uid = user.uid
                        this.currentUser.email = user.email
                        this.currentUser.username = user.displayName
                    }
                    this.initUI()
                })
            },
            methods: {
                createMessage: function () {
                    if (this.newContent) {
                        this.$firebaseRefs.messages.push({
                            username: this.currentUser.username,
                            content: this.newContent,
                        })
                        this.newContent = ''
                    }
                },
                initUI: function () {
                    ui.start('#firebaseui-auth-container', {
                        signInoptions: [
                            firebase.auth.EmailAuthProvider.PROVIDER_ID
                        ],
                        callbacks: {
                            signInSuccessWithAuthResult: (authResult, redirectUrl) => {
                                this.currentUser.uid = authResult.user.uid
                                this.currentUser.email = authResult.user.email
                                this.currentUser.username = authResult.user.displayName
                                return false
                            }
                        }
                    })
                },
                logout: function() {
                    this.currentUser = {
                        uid: '',
                        email: '',
                        displayName: ''
                    }
                    auth.signOut()
                }
            }
        })

    </script>
</body>

</html>
```

