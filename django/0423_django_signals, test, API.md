# Django_Signals

1. `app`에 `signals.py`를 생성

   ```python
   from django.db.models.signals import post_save
   from django.dispatch import receiver
   from django.conf import settings
   
   from .models import Profile
   
   
   # 저장한 이후에 함수가 처리한다.
   @receiver(post_save, sender=settings.AUTH_USER_MODEL)       
   # post_save = save한 이후, sender = 유저
   def create_user_profile(instance, created, **kwards):       
   # created : boolean (생성과 수정을 구분)
       if created:
           Profile.objects.get_or_create(user=instance)        
   # 어떠한 상황에 어떤 인자들을 받는지 확인
   # settings.AUTH_USER_MODEL 이거는 models.py랑 signals.py
   # models폼에서 .save()를 하는 순간 신호발생해서 함수발생
           
   ```



2. `apps.py`

   ```python
   from django.apps import AppConfig
   
   class UsersConfig(AppConfig):
       name = 'users'
       def ready(self):
           from .signals import create_user_profile
   ```



# Django_Test

1. pip install django_test_plus

   ```
   git clone https://lab.ssafy.com/edutak/django_test.git
   ```


2. boards -> tests.py

   ```python
   from test_plus.test import TestCase
   from django.conf import settings
   
   class SettingsTest(TestCase):
       # 1. settings 값 확인
       def test_01_settings_locale(self):
           self.assertEqual(settings.USER_I18N, True)
   ```

3. `test.py`

```python
from test_plus.test import TestCase
from django.conf import settings


class SettingsTest(TestCase):
    # 1. settings 값 확인
    def test_01_settings_locale(self):
        self.assertEqual(settings.USE_I18N, True)       
        self.assertEqual(settings.TIME_ZONE, 'Asia/Seoul')
        
        
from .models import Board
from .forms import BoardForm
class BoardModelTest(TestCase):
    def test_01_model(self):
        board = Board.objects.create(   title='테스트', 
                                        content='내용', 
                                        user_id=1 )
        self.assertEqual(str(board), f'Board{board.pk}')
        
    def test_02_modelform_with_data(self):
        data = {'title': 'test', 'content': 'test'}
        self.assertEqual(BoardForm(data).is_valid(), True)
        
    def test_03_modelform_without_title(self):
        data = {'content': 'test' }
        self.assertEqual(BoardForm(data).is_valid(), False)
    
    def test_04_modelform_without_title(self):
        data = {'title': 'test' }
        self.assertEqual(BoardForm(data).is_valid(), False)
      
        
# BoardForm이 있는지 Test
class BoardViewCreateTest(TestCase):  # 필요한 걸 불러오는지, 저장이 되는지
    def setUp(self):
        # given
        user = self.make_user(username='test', password='xptmxmqht!')
        
    def test_01_get(self):
        # when
        # self.make_user(username='test', password='xptmxmqht!')   # 로그인, 로그인하지않은 상태면 302 에러코드 출력
        with self.login(username='test', password='xptmxmqht!'):
            response = self.get_check_200('boards:create')            
            # HTTP 상태코드 200 ok를 받을수 있냐 없냐!
            # self.assertEqual(response, '<form')                     
            # form 형식이 있는지
            # then
            self.assertIsInstance(response.context['form'], BoardForm)  
            # 302 : 로그인을 안한 상태를 말한다.
          	# key가 'form'인 딕셔너리의 value가 BoardForm인지!
                                        
    def test_02_login_required(self):
        self.assertLoginRequired('boards:create')
        
    def test_03_post_redirect_302(self):
        # given -> 사용자가 작성한 글이 request.POST로 넘어온다
        data = {'title': '제목 작성', 'content':'냉무'}
        
        # when -> 
        with self.login(username='test', password='xptmxmqht!'):
            self.post('boards:create', data=data)
            # then
            self.response_302()
            

class BoardViewDetailTest(TestCase):
    def setUp(self):
        self.user = self.make_user(username='test', password='xptmxmqht!')
        self.board = Board.objects.create(
                            title = '제목',
                            content = '내용',
                            user = self.user
                            )
    
    def test_01_get(self): 
        # when then
        self.get_check_200('boards:detail', board_pk = self.board.pk)
        
    def test_02_contain_board_title_content(self):
        # when
        self.get_check_200('boards:detail', board_pk = self.board.pk)
        # then
        self.assertResponseContains(self.board.title)
        self.assertResponseContains(self.board.content)
        
    def test_03_template(self):
        # when
        response = self.get_check_200('boards:detail', board_pk = self.board.pk)
        # then
        self.assertTemplateUsed(response, 'boards/detail.html')
    
    
class BoardViewIndexTest(TestCase):
    def setUp(self):
        # given
        self.user = self.make_user(username='test', password='xptmxmqht!')
        self.board = Board.objects.create(
                            title = '제목',
                            content = '내용',
                            user = self.user
                            )

    def test_01_boards_queryset(self):
        Board.objects.create(
                            title = '제목1',
                            content = '내용1',
                            user = self.user
                            )
        boards = Board.objects.order_by('-pk')
        response = self.get_check_200('boards:index')
        self.assertQuerysetEqual(response.context['boards'], map(repr, boards))
        
    def test_02_template(self):
        # when
        response = self.get_check_200('boards:index')
        # then
        self.assertTemplateUsed(response,'boards/index.html')
        
class BoardViewDeleteTest(TestCase):
    def setUp(self):
    # given
        self.user = self.make_user(username='test', password='xptmxmqht!')
        self.board = Board.objects.create(
                    title = '제목',
                    content = '내용',
                    user = self.user
                    )
    
    def test_01_get_405(self):
        # when
        with self.login(username='test', password="xptmxmqht!"):
            self.get('boards:delete', board_pk=self.board.pk)
            self.response_405()
        
    def test_02_post_302(self):
        # when
        with self.login(username='test', password="xptmxmqht!"):
            self.post('boards:delete', board_pk=self.board.pk)
            self.response_302()
        
    def test_03_delete(self):
        # when
        boards_count = Board.objects.count()
        with self.login(username='test', password="xptmxmqht!"):
            self.post('boards:delete', board_pk=self.board.pk)
            self.assertEqual(Board.objects.count(), boards_count-1)


class BoardViewUpdateTest(TestCase):
    def setUp(self):
    # given
        self.user = self.make_user(username='test', password='xptmxmqht!')
        self.board = Board.objects.create(
                                    title = '제목',
                                    content = '내용',
                                    user = self.user
                                    )
    
    def test_01_boardform_instance(self):
        with self.login(username='test', password='xptmxmqht!'):
            response = self.get_check_200('boards:update', board_pk=self.board.pk)
            self.assertEqual(response.context['form'].instance.pk, self.board.pk)
 
```





# API_ Django_CRUD

## postman 검색 후 실행, Params는 유저, Body는 admin(내가) 설정해준다.

```
C - POST
R - GET
U - PUT
D - DELETE
--------------------------------------------------------------
Example)
목록 - musics/	GET
C - musics/		 POST
R - musics/{music_pk}	GET
U - musics/{music_pk}	PUT
D - musics/{music_pk}	DELETE
```



pip install

```
djangorestframework
django-rest-swagger

'''
docstring
'''
```



### Serializer는 queryset과 모델 인스턴스와 같은 복잡한 데이터를 JSON, XML 등의 다른 유형으로 쉽게 변환한다.

1. `Serializers.py`

   ```python
   from rest_framework import serializers
   from .models import Music, Artist, Comment
   
   class MusicSerializer(serializers.ModelSerializer):
       class Meta:
           model = Music
           fields = ['id', 'title', 'artist']
   
   class ArtistSerializer(serializers.ModelSerializer):
       music_count = serializers.IntegerField(source='music_set.count')
       class Meta:
           model = Artist
           fields = '__all__'
           
   class ArtistDetailSerializer(serializers.ModelSerializer):
       musics = MusicSerializer(source='music_set', many=True, read_only=True)
       class Meta:
           model = Artist
           fields = '__all__'
           
   class CommentSerializer(serializers.ModelSerializer):
       class Meta:
           model = Comment
           fields = ['content']
   ```

   * form형식 대신 Serializer

2. `settings.py`

   ```python
   INSTALLED_APPS = [
       'rest_framework',
       'rest_framework_swagger',
       'musics',
   ]
   ```



3. `views.py`

   ```python
   from django.shortcuts import render, get_object_or_404
   from rest_framework.decorators import api_view
   from rest_framework.response import Response
   
   from .models import Music, Artist, Comment
   from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer
   # Create your views here.
   
   @api_view(['GET'])
   def music_list(request):
       '''
       음악 정보 출력
       '''
       musics = Music.objects.all()
       serializer = MusicSerializer(musics, many=True)
       return Response(serializer.data)
   
   @api_view(['GET'])
   def music_detail(request, music_pk):
       '''
       음악 상세 보기
       '''
       music = get_object_or_404(Music, pk=music_pk)
       serializer = MusicSerializer(music)
       return Response(serializer.data)
       
   @api_view(['GET'])
   def artist_list(reqeust):
       '''
       Artist 정보 출력
       '''
       artists = Artist.objects.all()
       serializer = ArtistSerializer(artists, many=True, read_only=True)
       return Response(serializer.data)
       
   @api_view(['GET'])
   def artist_detail(reqeust, artist_pk):
       '''
       Artist 상세 보기
       '''
       artist = get_object_or_404(Artist, pk=artist_pk)
       serializer = ArtistDetailSerializer(artist)
       return Response(serializer.data)
   
   @api_view(['POST'])    
   def comment_create(request, music_pk):
       '''
       comment 달기
       '''
       music = get_object_or_404(Music, pk=music_pk)
       serializer = CommentSerializer(data=request.data)
       if serializer.is_valid(raise_exception=True):
           serializer.save(music = music)
           return Response(serializer.data)
           
   @api_view(['DELETE', 'PUT'])
   def comment_update_delete(request, music_pk, comment_pk):
       '''
       comment 수정 및 삭제
       ''' 
       comment = get_object_or_404(Comment, pk=comment_pk)
       if request.method == 'PUT':
           music = get_object_or_404(Music, pk=music_pk)
           serializer = CommentSerializer(data=request.data, instance=comment)
           if serializer.is_valid(raise_exception=True):
               serializer.save()
               return Response({'message': '성공적으로 수정되었습니다.'})
       else:
           comment.delete()
           return Response({'message': f'음악{music_pk}의 댓글이 삭제되었습니다.'})
       
       
   ```

   1. docstring

      ```python
      '''
      docstring
      '''
      
      /api/v1/docs/에서 각 함수별로 멘트
      ```


   2. message

      ```python
      return Response({'message': '성공적으로 수정되었습니다.'})
      
      # 요청받은 곳에 message 전송
      ```

   3. 기타

      ```python
      is_valid(raise_exception=True):
      # 기존에는 에러발생 시 응답상태코드 = 5xx
      # raise_exception=True를 추가하면 에러발생 시 HTTP 400 Bad request
      
      serializer = ArtistSerializer(artists, many=True, read_only=True)
      # 생성이나 수정이 아닌 read만 (출력만 할 때 사용)
      ```


