# Vue-django

django에서 `music_api` 프로젝트 활용
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>

<body>
    <div id="app">
        <ul>
            <li v-for="music in musics">
                <h2>{{ music.artist_name}}: {{ music.title }}</h2>
                <input v-model="music.newComment" v-on:keyup.enter="creatComment(music)">
                <ul>
                    <li v-for="comment in music.comment_set">{{ comment.content }}</li>
                </ul>
                <hr>
            </li>
        </ul>
    </div>

    <script>
        const app = new Vue({
            el: '#app',
            data: {
                musics: []
            },
            mounted: function () {
                this.getMusics()
            },
            methods: {
                getMusics: function () {
                    // axios를 통한 요청은 promise 객체를 리턴
                    axios.get('http://django-intro-manuck.c9users.io:8080/api/v1/musics/')
                        // resolve 되면, (성공하면) => then으로 처리
                        .then(response => response.data)
                        .then(musics => {
                            this.musics = musics.map((music) => {
                                return {...music, newComment: ''}
                            })
                        })
                        // reject 되면, (실패하면) => catch에서 처리
                        .catch(error => {
                            console.log(error)
                        })
                },
                creatComment: function(music) {
                    const data = {content: music.newComment}
                    axios.post(`http://django-intro-manuck.c9users.io:8080/api/v1/musics/${music.id}/comments/`, data)
                        .then(response => {
                            music.comment_set.push(response.data)
                            music.newComment = ''
                            console.log(response)
                        })
                        .catch( error => console.log(error))
                }
                
            }
        })
    </script>
</body>

</html>
```



django에서 `install`

```bash
$ pip install django-cors-headers
```



`settings.py` 수정

```python
# INSTALLED_APP 추가
INSTALLED_APPS = [
    'corsheaders',
    'musics',
]

# MIDDLEWARE 추가 
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]


CORS_ORIGIN_ALLOW_ALL = True

# 만약에, 특정한 오리진만 허용하려면
# CORS_ORIGIN_WHITELIST =[
#     'localhost:8080',
#     'naver.com'
#     ]
```

