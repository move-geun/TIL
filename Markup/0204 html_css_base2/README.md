### Html

* html : 문서의 최상위 요소
* head : 문서 메타데이터 요소
  * 문서 제목, 인코딩, 스타일, 외부파일 로딩
  * 브라우저에 잘 나타나지 않음
* body : 문서 본문 (실제 화면과 관련된 내용)
* DOM 트리 구조
  * 텍스트 파일인 html 문서를 브라우저에 렌더링하기 위한 구조
    * html 문서에 대한 모델을 구성함
    * html 문서 내의 각 요소에 접근/수정에 필요한 프로퍼티와 메소드 제공
* `<form>`
  * 정보(데이터)를 서버에 제출하기 위한 영역
  * `action` : form을 처리할 서버의 URL
  * `method`: form을 제출할 때 사용할 HTTP 메서드(GET or POST)
  * `enctype` : method가 post인 경우 데이터 유형

### CSS

* css는 상속을 통해 부모 요소의 속성을 자식에게 상속하지만
* 상속이 되는 것과 안되는 것이 있다
  * 상속 되는 것
    * Text 관련 요소(font,color)
  * 상속 되지 않는 것
    * box model 관련 요소
    * position 관련 요소

