package user;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class UserDAO {
    private Connection conn;
    private PreparedStatement pstmt;
    private ResultSet rs;

    public UserDAO() {
        try {
            String dbURL = "jdbc:mariadb://localhost:3306/BBS";
            String dbID = "root";
            String dbPassword = "1234";
            Class.forName("com.mariadb.jdbc.Driver");
            conn = DriverManager.getConnection(dbURL, dbID, dbPassword);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public int login(String userID, String userPassword) {
        // 로그인 시 pstmt에 정해진 SQL 문장을 넣어 실행시킴
        String SQL = "SELECT userPassword FROM USER WHERE userID = ?";
        try {
            pstmt = conn.prepareStatement(SQL);
            // 보안문제로 설정한 SQL문에 userID를 넣는 과정
            pstmt.setString(1, userID);
            // pstmt 실행
            rs = pstmt.executeQuery();
            if (rs.next()) {
                if(rs.getString(1).equals(userPassword))
                    return 1;  // 로그인 성공
                else
                    return 0;  // 비밀번호 불일치
            }
            return -1; // 아이디 없음
        } catch (Exception e) {
            e.printStackTrace();
        }
        return -2; // 데이터베이스 오류
    }
}
