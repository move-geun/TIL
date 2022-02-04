### HTML 

###  Inline / Block

* 한 줄 띄우기가 자동으로 되는지

---

#### 텍스트 :: Inline 요소

* `<a href="link">__</a>`
* `<b>__</b>`
* `<strong>__</strong>`
* `<u>__</u>`
* `<i>__</i>`
* `<img src="link, path"`: 상대경로

---

#### 그룹 :: Block 요소

* `<p>__</p>`

  * ```html
    <p>
        안녕하세요 뭅근입니다. 
    </p><br><span>내일 모레 또 쉬어요.</span>
    ```

* `<hr>` : 디바이더

##### 리스트

* `<ol>__</ol>` : 순서가 있는 리스트
* `<ul>__</ul>` : 순서가 없는 리스트
  * `<li>_자식태그_</li>`
* `<div>__</div>`

---

#### 테이블

```html
<table>
    
    <thead>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Major</th>
        </tr>
    </thead>
    
    <tbody>
        <tr>
            <td>1</td>
            <td>지은</td>
            <td>베트남어</td>
        </tr>
        <tr>
            <td>2</td>
            <td>상현</td>
            <td>치치어</td>
        </tr>
    </tbody>
    
    <tfoot>
        <tr>
            <td>총계</td>
            <td colspan="2">2명</td>
        </tr>
    </tfoot>
    <caption>반짝이는 우리!</caption>
</table>
```

---

#### form

`<form>`은 정보(데이터)를 서버에 제출하기 위한 영역

`<form>`의 기본 속성

* action : form을 처리할 서버의 URL
* method : form을 제출할 때 사용할 HTTP 메서드(GET 혹은 POST)
* enctype : method가 post인 경우 데이터 유형

---

#### input

다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨

`<input>`의 기본 속성

* name : form control에 적용되는 이름(이름/값 페어로 전송됨)
* value : form control에 적용되는 값(이름/값 페어로 전송됨)
* required, readonly, autofocus, autocompltet, disabled 등

```html
<form action="/search" method="GET">
    <input type="text" name="q">
</form>
```

##### input label

label을 클릭하여 input 자체의 초점을 맞추거나 활성화 가능

* 사용자는 선택할 수 있는 영역이 늘어나 웹/모바일 환경에서 편하게 사용 가능

* label과 input 입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label을 읽어 쉽게 내용확인을 가능

* `<input>`에 id 속성을, `<label>`에는 for 속성을 활용하여 상호 연관을 시킴

  ```html
  <label for="agreement">개인정보 수집에 동의합니다.</label>
  <input type="checkbox" name="agreement" id="agreement">
  ```

---

### CSS

#### 결합자(div > ul > li > a > span)

* 자손 결합자(selectorA 하위 모든 selectorB 요소)

```css
div span{
	color : red,
}
```

```html
<div>
    <span>이건 빨강입니다.</span>
    <p>
        이건 빨강이 아닙니다.
    </p>
    <p>
        <span>이건 빨강입니다.</span>
    </p>
</div>
```

* 자식 결합자(selectorA 바로 아래의 selectorB 요소)

```css
div > span{
    color : red;
}
```

```html
<div>
    <span>이건 빨강입니다.</span>
    <p>
        이건 빨강이 아닙니다.
    </p>
    <p>
        <span>이건 빨강입니다.</span>
    </p>
</div>
```

* 일반 형제 결합자(selectorA의 형제 요소 중 뒤에 위치하는 selectorB 요소를 모두 선택)

```css
p ~ span{
    color : red;
}
```

```html
<span>p태그의 앞에 있기 때문에 이건 빨강이 아닙니다.</span>
<p>
    여기 문단이 있습니다.
</p>
<b>여기 문단이 있습니다.</b>
<span>p태그와 형제이기 때문에 이건 빨강입니다!</span>
<b>더 많은 코드가 있습니다.</b>
<span>이것도 p태그와 형제이기 때문에 빨강입니다!</span>
```

* 인접형제 결합자(selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택)

```css
p + span{
    color : red;
}
```

```html
<span>p태그의 앞에 있기 때문에 이건 빨강이 아닙니다.</span>
<p>
    여기 문단이 있습니다.
</p>
<span>p태그와 형제이기 때문에 이건 빨강입니다!</span>
<b>더 많은 코드가 있습니다.</b>
<span>이것도 p태그와 형제이기 때문에 빨강입니다!</span>
```

