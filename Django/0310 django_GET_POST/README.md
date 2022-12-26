#### Django_POST_GET

##### GET

* 특정 리소스를 가져오도록 요청할 때 사용
* 반드시 데이터를 가져올 때만 사용해야함
* DB에 변화를 주지 않음
* CRUD에서 R 역할 담당

##### POST

* 서버를 데이터로 전송할 때 사용
* 리소스를 생성/변경하기 위해 데이터를 HTTP body에 담아 전송
* 서버에 변경사항을 만듦
*  CRUD에서 C/U/D 역할을 담당



##### CSRF

* 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법
* Django는 CSRF에 대항하여 middleware와 template tag 제공
* Security Token 사용방식
  * 사용자 데이터에 임의의 난수 부여 및 전달, 이후 서버 요청시마다 token 값이 유효한지 검증
  * POST, PATCH, DELETE 등에 적용

`{% csrf_token %}`

* CSRF 보호에 사용
* input type이 hidden으로 작성되며 value는 django에서 생성한 hash 값으로 설정됨
* 해당 태그가 없다면 403 forbidden 응답

```django

{% extends 'base.html' %} {% block content %}
<h1 class="text-center">CREATE</h1>
<form action="{% url 'articles:create' %}" method="POST">  <==  ****POST로 변경****
  {% csrf_token %}
  <label for="title">Title : </label>
  <input type="text" name="title" /><br />
  <label for="content">Content : </label>
  <textarea name="content" cols="30" rows="10"></textarea><br />
  <input type="submit" />
</form>
{% endblock content %}
```

```python
def create(request):
    title = request.POST.get('title')		# POST로 받아온다
    content = request.POST.get('content')	# POST로 받아온다
    article = Article(title=title, content=content)
    article.save()
    return redirect('articles:detail', article.pk)
```



##### `redirect()`

* 새 URL로 요청을 다시 보냄

* 인자에 따라 HttpResponseRedirect를 반환

* 브라우저는 현재 경로에 따라 전체 URL 자체를 재구성

  ```python
  from django.shortcuts import render, redirect # <== redirect 추가
  def create(request):
      title = request.POST.get('title')
      content = request.POST.get('content')
  
      article = Article(title=title, content=content)
      article.save()
      return redirect('articles:detail', article.pk)	# return redirect
  ```



##### DETAIL

```python
def detail(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)
```

```django
{% extends 'base.html' %} 
{% block content %}
<h1 class="text-center">{{ article.pk }}'s DETAIL</h1>
<p>제목 : {{ article.title }}</p>
<p>내용 : {{ article.content }}</p>
<p>생성일 : {{ article.created_at }}</p>
<p>수정일 : {{ article.updated_at }}</p>
<hr />
<a href="{% url 'articles:index' %}" class="btn btn-primary"> [BACK] </a>
{% endblock content %}
```



##### DELETE

```python
# apps/urls.py
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    # path('<str:title>/', views.detail, name='detail'),
    path('delete/<int:pk>/', views.delete, name='delete'), # path 추가
    
]
```

```python
# apps/views.py
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```

근데 이러면 모든 유저가 url로 내 정보들 삭제가 가능해짐

그래서 조건을 건다

```python
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else: # GET
        return redirect('articles:detail', article.pk)
```



##### UPDATE

```python
# apps/urls.py
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('update/<int:pk>/', views.update, name = 'update'),
```

```python
# apps/views.py
def edit(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)


def update(request,pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)
```

```django
# edit.html
{% extends 'base.html' %} {% block content %}
<h1>{{ article.pk }}'s EDIT</h1>
<form action="{% url 'articles:update' article.pk %}" method="POST">
  {% csrf_token %}
  <label for="title">Title : </label>
  <input type="text" name="title" value="{{ article.title }}" /><br />
  <label for="content">Content : </label>
  <textarea name="content" cols="30" rows="10">{{ article.content }}</textarea
  ><br />
  <input type="submit" />
</form>
<a href="{% url 'articles:index' %}" class="btn btn-primary"> [BACK] </a>
{% endblock content %}
```

