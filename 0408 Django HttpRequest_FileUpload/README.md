### Django http request, image upload

---

### Handling HTTP request

Django에서 HTTP 요청 처리방법

1. Django shortcut functions

   * django.shorcuts 패키지는 개발에 도움 될 수 있는 여러 함수와 클래스 제공

   * `render()`

   * `redirect()`

   * `get_list_or_404()`

     ```python
     get_list_or_404
     
     def index(request):
         # API로 서버를 쓸 때 사용
         articles = get_list_or_404(Article)
         pass
     
     ```

     

   * `get_object_or_404()`

     * 모델 manager인 objects에서 get()을 호출하지만,  해당 객체가 없을 경우 DoesNotExist 예외 대신 Http 404를 raise
     * `get()`의 경우 조건에 맞는 데이터가 없을 경우 예외를 발생시킴
       * 코드 실행 단계에서 발생한 예외 및 에러에 대해서 error 500(서버가 처리방법을 모르는 상태)로 인식함
     * 상황에 따라 적절한 예외처리를 하고, 클라이언트에게 올바른 에러 상황을 전달하는 것 또한 중요한 개발 요소 중 하나

     ```python
     get_object_or_404
     
     def detail(request, pk):
         # article = Article.objects.get(pk=pk)
         # article 정의 방법이 달라짐
         article = get_object_or_404(Article, pk=pk)
         context = {
             'article' : article,
         }
     	return render(request, 'articles/detail.html', context)
     
     
     def delete(request, pk):
         article = get_object_or_404(Article, pk=pk)
         pass
     
     
     def update(request, pk):
         article = get_object_or_404(Article, pk=pk)
         pass
     ```



2. View decorater

   * 어떤 함수에 기능을 추가하고 싶을 떄, 해당 함수를 수정하지 않고 기능을 연장해주는 함수

   * 즉, 원본 함수를 수정하지 않으면서 추가 기능만을 구현 할 때 사용

   * Allowed HTTP methods

     * 요청 메서드에 따라 view 함수에 대한 엑세스를 제한

     * 요청이 조건을 충족시키지 못하면 HttpResponseNotAllowed을 return

       (405 Method Not Allowed)

     * `require_http_methods()`

       * view 함수가 특정한 method 요청에 대해서만 허용하도록 하는 데코레이터

         ```python
         from django.views.decoraters.http import reqire_http_methods
         
         # 데코레이터를 통해 GET과 POST만 허용되게 만들어줌
         # 이외의 경우 405 응답 return
         @require_http_methods(['GET', 'POST'])
         def create(request):
         
             if request.method == 'POST':
                 form = ArticleForm(request.POST)
                 if form.is_valid():
                     article = form.save()
                     return redirect('articles:detail', article.pk)
             # 데코레이터를 주기 전엔 POST가 아닌 모든 method에 적용됨
             # 데코레이터를 준 이후엔 GET만
             else:
                 form = ArticleForm()
             
             context = {
                 'form': form,
             }
             return render(request, 'articles/create.html', context)
         
         # update에도 적용~
         @require_http_methods(['GET', 'POST'])
         def update(request, pk):
             pass
         
         ```

         

     * `require_POST()`

       * view 함수가 POST method 요청만 승인하도록 하는 데코레이터

         ```python
         from django.views.decoraters.http import reqire_POST
         
         @require_POST
         def delete(request, pk):
             article = get_object_or_404(Article, pk=pk)
             # 데코를 통해 POST만 들어오게 되니까 if문 생략 가능 and 인덴트 맞추기
             # if request.method=='POST':
             article.delete()
             return redirect('articles:index')
         	# 얘도 생략 가능	
             # return redirect('articles:detail', article.pk)
         ```

     * `require_safe()`

       * view 함수가 GET 및 HEAD method만 허용하도록 요구하는 데코레이터

       * django는 require_GET 대신 require_safe 사용을 권장

         ```python
         from django.views.decoraters.http import reqire_safe
         
         @require_safe
         def index(request):
             pass
         
         @require_safe
         def detail(request, pk):
             pass
         
         ```

---

### Media files

* 미디어 파일
* 사용자가 웹에서 업로드하는 정적 파일(user-uploaded)
* 유저가 업로드 한 모든 정적 파일

#### Model field

`FileField()`

* 파일 업로드에 사용하는 모델 필드

* 2개의 선택 인자를 가지고 있음 

* `upload to` 

  * 업로드 디렉토리와 파일 이름을 설정하는 두 가지 방법 제공
    * 문자열 값이나 경로 지정
    * 함수 호출

  `upload_to` = 'images/'

  * 실제 이미지가 저장되는 경로를 지정

  ```python
  # upload_to 문자열 값이나 경로 지정하는 방법
  # models.py
  
  class MyModel(models.Model):
      # MEDIA_ROOT/uploads/ 경로로 파일 업로드
      upload = models.FileField(upload_to='uploads/')
      # or
      # MEDIA_ROOT/uploads/2021/01/01/ 경로로 파일 업로드
      upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
  ```

  ```python
  # upload_to 함수 호출 방식
  # models.py
  
  def articles_image_path(instance, filename):
      # `MEDIA_ROOT/image_<pk>/` 경로에 <filename>` 이름으로 업로드
      return f'image_{instance.pk}/{filename}`
  
  class Article(models.Model):
      image = models.ImageField(upload_to=articles_image_path)
  ```

  

  `blank=True`

  * 이미지 필드에 빈 값(빈 문자열)이 허용되도록 설정(이미지를 선택적으로 업로드 할 수 있도록)

  * 기본값 = False

  * True인 경우 필드를 비워 둘 수 있고, DB에는 ``(빈 문자열)이 저장됨

  * 유효성 검사에서 사용됨(is_valid)

    * 모델 필드에 blank=True를 작성하면 form 유효성 검사에서 빈 값을 입력할 수 있음

      

  `null`

  * 기본값 = False
  * True인 경우 django는 빈 값에 대해 DB에 NULL로 저장
  * [주의]
    * CharField, TextFiled와 같은 문자열 기반 필드에는 사용하는 것을 피해야 함
    * 문자열 기반 필드에 True 설정시 '데이터 없음'에 [ 빈 문자열과 NULL 두 가지 가능한 값이 있음을 의미하게 됨
    * 대부분의 경우 '데이터 없음'에 대해 두 개의 가능한 값을 갖는 것은 중복되는 것이며, django는 Null이 아닌 빈 문자열을 사용하는 것이 규칙

  ```python
  # blanck & null 비교
  # models.py
  
  class Person(models.Model):
      name = models.CharField(max_length=10)
      
      # null=True 금지
      bio = models.TextField(max_length=50, blank=True)
      
      # null, blank 모두 설정 가능 -> 문자열 기반 필드가 아니기 때문
      birth_date = models.DateField(null=True, blank=True)
  ```

* ※ 문자열 기반 및 비문자열 기반 필드 모두에 대해 null option은 DB에만 영향을 끼치므로, form에서 빈 값을 허용하려면 blank=True를 설정해야 함



* `storage`

---

#### Image Upload

* `ImageField()`

  * 이미지 업로드에 사용하는 모델 필드

    ```python
    from django.db import models
    
    # 모델에 이미지 추가해주기.
    class Article(models.Model):
        title = models.CharField(max_length=20)
        content = models.TextField()
        # 모델에 이미지 추가~
        image = models.ImageField(upload_to='images/', blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    
        def __str__(self):
            return self.title
    ```

  * FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용가능하며, 더해서 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사함

  * ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성되며, max_length 인자를 사용하여 최대 길이를 변경 할 수 있음

  * [주의]  사용하려면 반드시  `Pillow`라이브러리가 필요

  * ##### 사용하기 위한 단계(실제 적용)

    1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정

       ```python
       # settings.py
       
       # 사용자가 업로드 한 파일을 보관한 디렉토리의 절대 경로
       # 장고는 파일의 경로를 데이터 베이스에 저장한다
       MEDIA_ROOT = BASE_DIR/ 'media'
       
       # MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL
       # 업로드 된 파일의 주소를 만들어주는 역할
       # 비어있지 않은 값으로 설정한다면 반드시 slash(/)로 끝나야함
       MEDIA_URL = '/media/'
       ```

    2. upload_to 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT의 하위 경로를 지정

    3. 업로드 된 파일의 경로는 django가 제공하는 `url` 속성을 통해 얻을 수 있음

       ```python
       # project/urls.py
       from django.contrib import admin
       from django.urls import path, include
       # import 추가하기
       from django.conf import settings
       from django.conf.urls.static import static
       
       urlpatterns = [
           path('admin/', admin.site.urls),
           path('articles/', include('articles.urls')),
       ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
       
       ```

    4. html 조정

       ```django
       # create.html form에 이미지 넣는다고 장고한테 말해주기
       
       {% extends 'base.html' %} 
       
       {% block content %}
       <p class="fs-1 fw-bold">CREATE</p>
       <form action="{% url 'articles:create' %}" method="POST"
             # 인코딩타입 추가해주기
             enctype="multipart/form-data">
         {% csrf_token %} {{ form.as_p }}
         <input type="submit" value="CREATE" />
       </form>
       <hr />
       <a href=" {% url 'articles:index' %} ">BACK</a>
       {% endblock content %}
       ```

    5. view 함수 조정

       ```python
       # views.py
       
       def create(request):
       
           if request.method == 'POST':
               # POST에는 title과 content 등이 저장되어있음
       		# file은 request.FILES에 저장되어 있어서 추가해줘야 한다
               form = ArticleForm(request.POST, request.FILES)
               if form.is_valid():
                   article = form.save()
                   return redirect('articles:detail', article.pk)
           else:
               form = ArticleForm()
           
           context = {
               'form': form,
           }
           return render(request, 'articles/create.html', context)
       ```

    6.  출력되게 설정

       ```django
       # detail.html
       
       {% extends 'base.html' %} 
       {% block content %}
       <p class="fw-bold fs-1">Detail</p>
       
       # 이미지 여기에 넣기~
       # 이미지가 있다면 출력하고 없다면 안 나오게 if로 감싸주기
       {% if article.image %}
       <img src="{{ article.image.url }}" alt="{{ article.image }}">
       {% endif %}
       
       <p class="fw-bold fs-2">{{ article.title }}</p>
       <p>{{ article.content }}</p>
       <p>작성일: {{ article.created_at }}</p>
       <p>수정일: {{ article.updated_at }}</p>
       <p></p>
       <p></p>
       <a href=" {% url 'articles:index' %}">BACK</a>
       {% endblock content %}
       ```

  ##### 이미지 수정하기

  * 이미지는 바이너리 데이터이기 때문에 수정 불가능, 그렇기 때문에 덮어씌우는 형태로 수정함

    ```django
    # update.html
    
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>UPDATE</h1>
      <hr>
      <form action="{% url 'articles:update' article.pk %}" method="POST"
          # 인코딩타입 추가해주기
          enctype="multipart/form-data">>
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
      </form>
      <a href="{% url 'articles:detail' article.pk %}">back</a>
    {% endblock content %}
    ```

    ```python
    # views.py update 함수 수정
    
    def update(request, pk):
        article = Article.objects.get(pk=pk)
        if request.method == 'POST':
            # files 추가해주기
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                article = form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'articles/update.html', context)
    
    ```

---

#### Image Resizing

업로드 될 때 이미지 자체를 resizing 하는 것

`django-imagekit` 라이브러리 활용

1.  이미지 킷 설치

   ```shell
   pip install Pillow
   pip install django-imagekit
   ```

2.  settings.py에 추가

   ```python
   # settings.py 
   
   INSTALLED_APPS = [
       'imagekit',
       'articles',
       'django_extensions',
   ]
   ```

3.  두 가지 방법이 있다

   3-1.  원본 이미지를 재가공하여 저장(원본 X, 썸네일O)

   ```python
   # models.py
   
   from django.db import models
   # import 추가해주고
   from imagekit.models import ProcessedImageField
   from imagekit.processors import Thumbnail
   
   class Article(models.Model):
       title = models.CharField(max_length=20)
       content = models.TextField()
   
    	# image = models.ImageField(upload_to='images/', blank=True)
       # imagekit을 활용해서 img 등록해줄거야~
       image = ProcessedImageField(
           blank=True,
           upload_to='thumbnails/',
           processors=[Tumbnail(200, 300)],
           format='JPEG',
           options={'quality': 90})
       
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   
       def __str__(self):
           return self.title
   ```

   ```shell
   # 모델 초기화
   python manage.py makemigrations
   python manage.py migrate
   ```

   3-2. 원본 O, 썸네일 O

   ```python
   # models.py
   
   from django.db import models
   # import 더욱 추가해주고
   from imagekit.models import ProcessedImageField, ImageSpecField
   from imagekit.processors import Thumbnail
   
   class Article(models.Model):
       title = models.CharField(max_length=20)
       content = models.TextField()
       # imagekit을 활용해서 img 등록해줄거야~
       # 원본도 저장하니까 image도 살려준다
    	image = models.ImageField(upload_to='images/', blank=True)
       image_thmbnail = ImageSpecField(
           blank=True,
           source='image', # 원본 ImageField명
           processors=[Tumbnail(200, 300)],
           format='JPEG',
           options={'quality': 90})
       
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   
       def __str__(self):
           return self.title
   ```

   