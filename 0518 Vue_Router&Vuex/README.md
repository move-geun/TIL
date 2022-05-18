### Vue Router & Vuex

---

`npm install` == `pip install -r requirement`



 ### Vue router

src/api/drf.js

```javascript
const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const ARTICLES = 'articles/'
const COMMENTS = 'comments/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },
  articles: {
    articles: () => HOST + ARTICLES,
    article: articlePk => HOST + ARTICLES + `${articlePk}/`,
    likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
    comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) =>
      HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
  },
}

```



#### 404 page

1. Vue Router에 등록되지 않은 routes일 경우

   ex) /no-such-routes

   vue router는 routes 배열에서 순차적으로 URL을 검색

   등록되지 않은 모든(*)  URL은 /404로 redirection

   브라우저에서 NotFound404 컴포넌트 확인

   ```javascript
   import Vue from 'vue'
   import VueRouter from 'vue-router'
   
   import ArticleListView from '@/views/ArticleListView.vue'
   import ArticleDetailView from '@/views/ArticleDetailView.vue'
   import ArticleNewView from '@/views/ArticleNewView'
   import ArticleEditView from '@/views/ArticleEditView'
   
   import LoginView from '@/views/LoginView.vue'
   import LogoutView from '@/views/LogoutView.vue'
   import SignupView from '@/views/SignupView.vue'
   import ProfileView from '@/views/ProfileView.vue'
   import NotFound404 from '../views/NotFound404.vue'
   
   Vue.use(VueRouter)
   
   const routes = [
     /*
     accounts
       /login => LoginView
       /logout => LogoutView
       /signup => SignupView
       /profile/:username => ProfileView
     
     articles
       / => ArticleListView
       /articles/new => ArticleNewView
       /articles/:articlePk => ArticleDetailView
       /articles/:articlePk/edit => ArticleEditView
       /404 => NotFound404
       * => /404
     */
   {
     path: '/login',
     name: 'login',
     conpinent: LoginView,
   },
   {
     path: '/logout',
     name: 'logout',
     conpinent: LogoutView,
   },
   {
     path: '/signup',
     name: 'signup',
     conpinent: SignupView,
   },
   {
     path: '/profile/:username', //profile/neo
     name: 'profile',
     conpinent: ProfileView,
   },
   {
     path: '/',  // Home
     name: 'articles',
     conpinent: ArticleListView,
   },
   {
     path: '/artilces/new',
     name: 'articleNew',
     conpinent: ArticleNewView,
   },
   {
     path: '/articles/:articlePk',
     name: 'article',
     conpinent: ArticleDetailView,
   },
   {
     path: '/articles/:articlePk/edit',
     name: 'articleEdit',
     conpinent: ArticleEditView,
   },
   {
     path: '/404',
     name: 'NotFound404',
     conpinent: NotFound404,
   },
   {
     path: '*',  // route에 없는 다른 모든 것들은
     redirect: '/404', // 404로 연결시킨다
   },
   ]
   ```

   

2. Vue Router에는 등록되어 있지만, 서버에서 해당 리소스를 찾을 수 없는 경우

   ex) /articles/9874561

#### Navigation Guard



---

### Vuex 

#### Vuex modules & namespace

