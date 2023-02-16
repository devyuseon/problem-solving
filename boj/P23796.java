import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class P23796 {

    public static long[][] matrix;

    public static void main(String[] args) throws IOException {
        Main.solution();
    }

    public static void L() {
        for (int i = 0; i < 8; i++) {
            ArrayDeque<Long> q = new ArrayDeque<>();
            boolean flag = false; // 바로 앞 전이 합쳐졌나?
            for (int j = 0; j < 8; j++) {
                if (matrix[i][j] == 0) continue;
                if (!q.isEmpty()) {
                    if (!flag && matrix[i][j] == q.peekLast()) {
                        q.addLast(q.pollLast() * 2);
                        flag = true;
                    } else {
                        q.addLast(matrix[i][j]);
                        flag = false;
                    }
                } else {
                    q.addLast(matrix[i][j]);
                }
            }
            for (int j = 0; j < 8; j++) {
                if (!q.isEmpty()) {
                    matrix[i][j] = q.pollFirst();
                } else {
                    matrix[i][j] = 0;
                }
            }
        }
    }

    public static void R() {
        for (int i = 0; i < 8; i++) {
            ArrayDeque<Long> q = new ArrayDeque<>();
            boolean flag = false; // 바로 앞 전이 합쳐졌나?
            for (int j = 7; j > -1; j--) {
                if (matrix[i][j] == 0) continue;
                if (!q.isEmpty()) {
                    if (!flag && matrix[i][j] == q.peekLast()) {
                        q.addLast(q.pollLast() * 2);
                        flag = true;
                    } else {
                        q.addLast(matrix[i][j]);
                        flag = false;
                    }
                } else {
                    q.addLast(matrix[i][j]);
                }
            }
            for (int j = 7; j > -1; j--) {
                if (!q.isEmpty()) {
                    matrix[i][j] = q.pollFirst();
                } else {
                    matrix[i][j] = 0;
                }
            }
        }
    }

    public static void U() {
        for (int j = 0; j < 8; j++) {
            ArrayDeque<Long> q = new ArrayDeque<>();
            boolean flag = false; // 바로 앞 전이 합쳐졌나?
            for (int i = 0; i < 8; i++) {
                if (matrix[i][j] == 0) continue;
                if (!q.isEmpty()) {
                    if (!flag && matrix[i][j] == q.peekLast()) {
                        q.addLast(q.pollLast() * 2);
                        flag = true;
                    } else {
                        q.addLast(matrix[i][j]);
                        flag = false;
                    }
                } else {
                    q.addLast(matrix[i][j]);
                }
            }

            for (int i = 0; i < 8; i++) {
                if (!q.isEmpty()) {
                    matrix[i][j] = q.pollFirst();
                } else {
                    matrix[i][j] = 0;
                }
            }
        }
    }

    public static void D() {
        for (int j = 0; j < 8; j++) {
            ArrayDeque<Long> q = new ArrayDeque<>();
            boolean flag = false; // 바로 앞 전이 합쳐졌나?
            for (int i = 7; i > -1; i--) {
                if (matrix[i][j] == 0) continue;
                if (!q.isEmpty()) {
                    if (!flag && matrix[i][j] == q.peekLast()) {
                        q.addLast(q.pollLast() * 2);
                        flag = true;
                    } else {
                        q.addLast(matrix[i][j]);
                        flag = false;
                    }
                } else {
                    q.addLast(matrix[i][j]);
                }
            }
            for (int i = 7; i > -1; i--) {
                if (!q.isEmpty()) {
                    matrix[i][j] = q.pollFirst();
                } else {
                    matrix[i][j] = 0;
                }
            }
        }
    }

    public static void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        matrix = new long[8][8];

        for (int i = 0; i < 8; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 8; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        String cmd = br.readLine();

        if (cmd.equals("L")) L();
        if (cmd.equals("R")) R();
        if (cmd.equals("U")) U();
        if (cmd.equals("D")) D();

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                sb.append(matrix[i][j]).append(" ");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }

}