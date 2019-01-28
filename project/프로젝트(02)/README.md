# README

---

# WEB

---

## 1. 영화 추천 사이트를 위한 레이아웃 구성(1)

```html
<link href="https://fonts.googleapis.com/css?family=Nanum+Pen+Script" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Indie+Flower" rel="stylesheet">
```

위와 같은 코드를 통해 2개의 폰트를 이용하여 구성하였다.

> 당신에게 어울리는 영화를 추천해드립니다.

위 글에서 배경 이미지가 어두운 이미지여서 텍스트를 흰색으로 적용

```html
class="text-white"
```

---

## 2. 영화 추천 사이트를 위한 영화 리스트 구성(2)

카드에 효과를 주기 위해 shadow를 사용하였다.

```html
class = "shadow p-3 mb-5"
```



---

## 3. 영화 상세 보기

이미지를 클리하면 modal 이 뜨는데 modal에 예고편을 추가했다.

```html
<div class="embed-responsive embed-responsive-16by9">
                    <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/Zy2Ht5gehsQ" allowfullscreen></iframe>
</div>
```

