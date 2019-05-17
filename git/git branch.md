# git branch
1. fast-forwarding

2. merge commit ()

3. merge conflict (master와 다른 branch 사이 같은 파일 수정 - 충돌발생)



branch 만들면서 이동

```bash
$ git checkout -b 브랜치명
```

> 두 개 합친거
>
> git branch 브랜치명
>
> git checkout 브랜치명



master와  branch 사이 차이 

```bash
$ git diff manuck
```



master에 붙이기(병합)

```bash
$ git merge manuck
```



branch 지우기

```bash
$ git branch -d manuck
```





서로 같은파일 다르게 수정했을때



충돌

```
CONFLICT (content): Merge conflict in godTakki.txt
Automatic merge failed; fix conflicts and then commit the result.
```

파일 내부

```
<<<<<<< HEAD
zxczczczx
=======
gggg
>>>>>>> jeong
```

visual studio code 로 들어가면 코드 선택 가능