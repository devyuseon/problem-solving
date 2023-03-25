import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {

    public static int[][] board;

    public static void backTracking(int r, int c) {
        if (c == 9) {
            backTracking(r + 1, 0);
            return;
        }

        if (r == 9) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    sb.append(board[i][j]);
                }
                sb.append("\n");
            }
            System.out.println(sb);
            System.exit(0);
        }

        if (board[r][c] == 0) {
            for (int i = 1; i <= 9; i++) {
                if (isPossible(r, c, i)) {
                    board[r][c] = i;
                    backTracking(r, c + 1);
                }
            }
            board[r][c] = 0;
            return;
        }

        backTracking(r, c + 1);
    }

    public static boolean isPossible(int r, int c, int n) {
        for (int i = 0; i < 9; i++) {
            if (board[r][i] == n) return false;
        }

        for (int i = 0; i < 9; i++) {
            if (board[i][c] == n) return false;
        }

        // 시작 위치
        int row = (r / 3) * 3;
        int col = (c / 3) * 3;

        for (int i = row; i < row + 3; i++) {
            for (int j = col; j < col + 3; j++) {
                if (board[i][j] == n) return false;
            }
        }

        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        board = new int[9][9];

        for (int i = 0; i < 9; i++) {
            String tmp = br.readLine();
            for (int j = 0; j < 9; j++) {
                board[i][j] = tmp.charAt(j) - '0';
            }
        }

        backTracking(0, 0);
    }
}