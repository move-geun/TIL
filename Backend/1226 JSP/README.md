# JSP 활용하여 BBS 만들기



## 1. JSP란?

* JSP 란 JavaServer Pages 의 약자이며 HTML 코드에 JAVA 코드를 넣어 **동적**웹페이지를 생성하는 웹어플리케이션 도구 (Java 언어를 기반으로 하는 Server Side 스크립트 언어) 

* JSP는 기존의 단순한 html을 서비스하던 웹서버의 기능을 보다 발전시켜 웹 기반의 프로그램을 할 수 있도록 만든 것
* 서블릿을 기반으로 하고 있으며 서블릿의 프로그램적인 요소를 발전시켜 사용자가 보다 쉽게 다룰 수 있도록 만든 스크립트 기반의 프로그램

 

![img](https://blog.kakaocdn.net/dn/0CaN9/btqEiMKbAQf/zcJr0xohg1aV228f2wtzq0/img.jpg)



JSP 가 실행되면 자바 서블릿(Servlet) 으로 변환되며 웹 어플리케이션 서버에서 동작되면서 필요한 기능을 수행, 생성된 데이터를 웹페이지와 함께 클라이언트로 응답한다.

 



# 2. Tomcat

아파치 소프트웨어 재단의 웹 어플리케이션 서버로, 자바 서블릿을 실행시키고 JSP 코드가 포함되어 있는 웹 페이지를 만들어준다.

Tomcat은 WAS로 Web Application Server라고 한다.



**웹서버 Web Server** 

: 정적인 데이터 처리하는 서버.

단순 이미지나 html파일과 같은 리소스만을 제공하는 서버는 웹서버만 사용하여 빠르고 안정적이게 활용.



**와스 WAS** 

: 동적인 데이터 처리하는 서버.



DB로 연결되어 데이터를 주고받거나 자바등을 통해 데이터 조작이 필요한 경우에는 WAS를 활용.


