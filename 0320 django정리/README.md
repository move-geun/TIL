### 일단 만들기

1.  시작 

   `django-admin startproject <프로젝트이름>`

2.  settings.py 변경

   ```python
   
   INSTALLED_APPS = [
       'articles',				# 앱 추가
       'django_extensions',	# shell_plus 위해서 추가
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   ]
   
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [BASE_DIR, 'templates'],		# BASE_DIR 경로 설정
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   
   LANGUAGE_CODE = 'en-us'				# ko-kr
   
   TIME_ZONE = 'UTC'					# Asia/Seoul
   
   USE_I18N = True						# 국제화 설정 True여야함
   	
   USE_TZ = True						# 현지화 설정 True여야함
   
   
   ```

3.  앱 생성 

   `python manange.py startapp <앱이름>`

4. 앱, 프로젝트와 같은 위치에 `templates`  폴더 생성, `base.html` 생성

   ```django
     <body>
       <div class="container mt-2">
           {% block content %}
           {% endblock content %}
         </div>
     </body>
   ```

5.  앱 내에 `templates`/`앱이름`/`~.html` 파일 생성

   ```django
   {% extends 'base.html' %} 			
   {% block content %}
   
   <a href="{% url 'articles:create' %}">NEW</a>			# url 위치로 이동시킨다
   
   {% for article in articles %}
   <h2 class="mt-2">제목 : {{ article.title }}</h2>			# 값 꺼낼때는 %%없음
   <h3>내용 : {{ article.content }}</h3>
   <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>	# 특정위치일 경우 pk 같이전달
   <hr />
   {% endfor %} 
   
   {% endblock content %}
   
   ```

6.  `projects`/`urls.py`에 경로 생성

   ```python
   from django.contrib import admin
   from django.urls import path,include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('articles.urls')),		# 앱.urls를 통째로 받아오겠다
       ]
   ```

7.  `app`/`urls.py` 생성

   ```python
   from django.urls import path
   from . import views				# 현재 위치에서 views를 가져온다
   
   
   app_name = 'articles'			# 이름 공간 지정
   
   urlpatterns = [
       path('', views.index, name='index' ),
       path('create/', views.create, name='create'),
       path('<int:pk>/', views.detail, name='detail'),
       path('edit/<int:pk>/', views.edit, name='edit'),
       path('update/<int:pk>/', views.update, name='update'),
       path('delete/<int:pk>/', views.delete, name='delete'),
   ]
   ```

8. `app`/`views.py` 

   ```python
   from django.shortcuts import render, redirect
   from .models import Article 			# from 위치 잘 잡기
   
   
   def detail(request,pk):					# pk 값이 일치하는 article을 가져와라
       article = Article.objects.get(pk=pk)
       context = {
           'article' : article,
       }
       return render(request, 'articles/detail.html', context)	# 화면을 띄워줌
   
   
   def update(request,pk):						# pk 값이 일치하는 애 가져오고, 그 request 
       article = Article.objects.get(pk=pk)	# POST에서 'title'에 해당하는 값을 가져와라
       article.title = request.POST.get('title')
       article.content = request.POST.get('content')
       article.save()							# 그리고 저장도 해줘야겠지?
       return redirect('articles:detail', article.pk)	# redirect로 연결, 특정 위치가 있으니
   													# pk 값을 전달해줌
   
   def delete(request,pk):	
       article = Article.objects.get(pk=pk)
       if request.method == 'POST':			# 주소링크로만 삭제되면 안되니까 POST일 경우만
           article.delete()					# 삭제하자~
           return redirect('articles:index')	
       else:
           return redirect('articles:detail',article.pk)
   ```

   ```python
   내림차순
   articles = Article.objcets.order_by(-pk)
   articles = Article.objects.all()[::-1]
   ```

9. `app`/`models.py`

   ```python
   from django.db import models
   
   # Create your models here.
   class Article(models.Model):
       title = models.CharField(max_length=10)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)	# 생성 시간 자동 입력
       updated_at = models.DateTimeField(auto_now=True)		# 
   ```

   ```shell
   $ python manage.py makemigrations
   $ python manage.py migrate
   
   
   필수는 아닌데 찝어줬음
   sql 볼 수 있는 명령어
   $ python manage.py sqlmigrate articles 0001
   
   
   $ python manage.py shell_plus
   'django_extensions', <-- 이것을 settings.py에 INSTALLED_APPS 에 추가해준다.
   ```

   ```shell
      # article 생성
      # 1.
       article = Article()
       article.title = title
       article.content = content
       article.save()
   
       # 2.
       article = Article(title=title, content=content)
       article.save()
   
       # 3.
       Article.objects.create(title=title, content=content)
   ```

   

10. `app`/`admin.py`

    ```python
    from django.contrib import admin
    from .models import Article
    
    class ArticleAdmin(admin.ModelAdmin):
        list_display = ('pk', 'title', 'content', 'created_at', 'updated_at')
    
    admin.site.register(Article, ArticleAdmin) 
    # Article만 주어질 경우 admin 페이지에서 Article과 각 목록의 제목만 나타남
    # ArticleAdmin 함께 주어질 경우 list 형태로 보이게 된다
    
    ```

    ```shell
    $ python manage.py createsuperuser
    name : 아이디이름
    email : 이메일@
    비밀번호 : 
    비밀번호 확인
    성공적으로 만들어졌습니다.
    ```

11. 시간표시

    ```django
    
    시간표시 - 년도 월 일 (Mon) AM/PM
    <!-- 2020년 02월 02일 (Sun) PM 02:02 -->
    {{ today|date:"Y년 m월 d일 (D) A h:i" }}
    ```

---

### ORM

- Object Relational Mapping
  - 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에(Django-SQL)데이터를 변환하는 프로그래밍 기술
  - OOP프로그래밍에서 RDBMS를 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

- RDBMS의 개념적 정의
  - Relational Database Management System
  - 관계형 모델을 기반으로 하는 데이터베이스 관리시스템
- RDBMS를 기반으로 한 DB Engine 의 종류
  - MySQL
  - SQLite
  - PostgreSQL
  - ORACLE
  - MS SQL

---

### 에러 종류

- forbiden 에러
  - 403 에러
  - 모델값이 제대로 전달안됐을때 
  - 데이터 문제
- 404 는 URL 문제
  - 해당 url을 찾지 못했음
- http status code
  - 에러 떳을 때 알려주는 노란색 코드창
- operation error
  - migrate를 하지않아서 혹은 table이 잘못되서
  - 명령어로 처리할 수 있는게 아니라, 테이블을 수정해야함

---

### MTV

- Django는 **MTV 디자인 패턴**으로 이루어진 Web Framework 이다 . 여기서 MTV 는 무엇의
  약자이며 각각 MVC 디자인 패턴과 어떻게 매칭이 되며 각 키워드가 django 에서 하는
  역할을 간략히 서술하시오.
- **MTV : Model Template View** // 장고에서 사용
- MVC : Model View Controller // 스프링에서 사용
- Model : **Model**
  - 응용프로그램의 **데이터 구조**를 정의하고 **데이터베이스의 기록을 관리**(추가, 수정, 삭제)
- View : **Template**
  - 파일의 구조나 **레이아웃**을 정의
  - 실제 내용을 **보여주는 데** 사용(presentation)
  - 장고는 Temlplates폴더에 html들이 있다.
- Controller : **View**
  - HTTP 요청을 수신하고 HTTP 응답을 반환
  - Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
  - template에게 응답의 서식 설정을 맡김
  - 요청에 따라 로직을 수행하며, 결과를 템플릿으로 렌더링하여 응답한다.