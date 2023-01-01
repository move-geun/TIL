<%--
  Created by IntelliJ IDEA.
  User: ehdrms
  Date: 2022-12-28
  Time: 오후 4:27
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="user.UserDAO" %>
<%@ page import="java.io.PrintWriter" %>
<jsp:useBean id="user" class="user.User" scope="page" />
<jsp:setProperty name="user" property="userID" />
<jsp:setProperty name="user" property="userPassword" />
<html>
<head>
  <title>JSP 게시판 웹 사이트</title>
</head>
<body>
<%
  UserDAO userDAO = new UserDAO();
  int result = userDAO.login(user.getUserID(), user.getUserPassword());
  if(result == 1){
    PrintWriter script = response.getWriter();
    script.println("<script>");
    script.println("location.href='main.jsp'");
    script.println("</script>");
  } else if(result == 0){
  PrintWriter script = response.getWriter();
  script.println("<script>");
  script.println("alret('비밀번호가 틀립니다')");
  script.println("history.back()");
  script.println("</script>");
}else if(result == -1) {
    PrintWriter script = response.getWriter();
    script.println("<script>");
    script.println("alret('존재하지 않는 아이디입니다')");
    script.println("history.back()");
    script.println("</script>");
  }else if(result == -2){
    PrintWriter script = response.getWriter();
    script.println("<script>");
    script.println("alret('데이터베이스 오류가 발생했습니다')");
    script.println("history.back()");
    script.println("</script>");
  }
%>
</body>
</html>
