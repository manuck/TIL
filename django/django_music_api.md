# django|music_api

1. project 생성

   ```bash
   $ djangot-admin startproject music_api
   $ cd music_api
   ```

2. app 생성

   ```bash
   $ python manage.py startapp musics
   ```

3. pip install 하기

   ```bash
   $ pip install djangorestframework
   $ pip install django-rest-swagger
   ```

4. `settings.py` 설정

   ```python
   INSTALLED_APPS = [
       'rest_framework',
       'rest_framework_swagger',
       'musics',
   ]
   ```

5. `urls.py` 설정

   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('api/v1/', include('musics.urls')),
   ]
   ```

6. `musics` app에서 `models.py` 설정

   ```python
   from django.db import models
   
   class Artist(models.Model):
       name = models.TextField()
       
       def __str__(self):
           return self.name
           
   class Music(models.Model):
       title = models.TextField()
       artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
       
       def __str__(self):
           return self.title
   
   class Comment(models.Model):
       content = models.TextField()
       music = models.ForeignKey(Music, on_delete=models.CASCADE)
   ```

7. migration 하기, 슈퍼유저 생성

   ```bash
   $ python manage.py makemigrations
   $ python manage.py migrate
   $ python manage.py createsuperuser
   ```

8. `musics`app에서 `admin.py` 설정

   ```python
   from django.contrib import admin
   from .models import Artist, Music, Comment
   
   admin.site.register(Artist)
   admin.site.register(Music)
   admin.site.register(Comment)
   ```

9. `urls.py` 생성

   ```python
   from django.urls import path
   from rest_framework_swagger.views import get_swagger_view
   from . import views
   
   urlpatterns = [
       path('docs/', get_swagger_view(title='음악 정보 API')),
       path('musics/', views.music_list),
       path('musics/<int:music_pk>/', views.music_detail),
       path('artist/', views.artist_list),
       path('artist/<int:artist_pk>/', views.artist_detail),
       path('musics/<int:music_pk>/comments/', views.comment_create),
       path('musics/<int:music_pk>/comments/<int:comment_pk>/', views.comment_update_delete),
   ]
   ```

10. `apps.py` 설정

    ```python
    from django.apps import AppConfig
    
    class MusicsConfig(AppConfig):
        name = 'musics'
    ```

11. `serializers.py` 생성

    ```python
    from rest_framework import serializers
    
    from .models import Music, Artist, Comment
    
    class MusicSerializer(serializers.ModelSerializer):
        class Meta:
            model = Music
            fields = ['id', 'title', 'artist']
    
    
    class ArtistSerializer(serializers.ModelSerializer):
        music_count = serializers.IntegerField(source='music_set.count', read_only=True)
        class Meta:
            model = Artist
            fields = '__all__'
        
    
    class ArtistDetailSerializer(serializers.ModelSerializer):
        musics = MusicSerializer(source='music_set', many=True)
        class Meta:
            model = Artist
            fields = '__all__'
    
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ['id', 'content']
    ```

12. `veiws.py` 설정

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
    def artist_list(request):
        '''
        아티스트 정보
        '''
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    def artist_detail(request, artist_pk):
        artist = get_object_or_404(Artist, pk=artist_pk)
        serializer = ArtistDetailSerializer(artist)
        return Response(serializer.data)    
    
    @api_view(['POST'])
    def comment_create(request, music_pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(music_id=music_pk)
            return Response(serializer.data)
            
    @api_view(['DELETE', 'PUT'])
    def comment_update_delete(request, music_pk ,comment_pk):
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.method == 'PUT':
            serializer = CommentSerializer(data=request.data, instance=comment)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'message': '성공적으로 수정되었습니다.'})
        else:
            comment.delete()
            return Response({'message': f'음악 {music_pk}의 댓글이 삭제되었습니다.'})
    ```

    