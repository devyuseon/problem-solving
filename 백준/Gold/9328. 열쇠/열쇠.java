import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

class Point {
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public String toString() {
        return "Point{" +
                "x=" + x +
                ", y=" + y +
                '}';
    }
}

public class Main {

    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws Exception {
        int t = read();
        StringBuilder sb = new StringBuilder();

        for (int tt = 0; tt < t; tt++) {
            int h = read();
            int w = read();
            char[][] matrix = new char[h + 2][w + 2];
            int key = 0;

            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    matrix[i + 1][j + 1] = (char) System.in.read();
                }
                System.in.read();
            }

            int tmp;
            while((tmp = System.in.read()) > 32) {
                if(tmp != '0') key |= 1 << (tmp - 'a');
            }

            ArrayDeque<Point> dq = new ArrayDeque<>();
            ArrayDeque<Point> doors = new ArrayDeque<>();
            boolean[][] visited = new boolean[h + 2][w + 2];
            visited[0][0] = true;
            dq.addLast(new Point(0, 0));
            int cnt = 0;

            while (!dq.isEmpty()) {
                Point cur = dq.pollFirst();

                for (int i = 0; i < 4; i++) {
                    int nx = cur.x + dx[i];
                    int ny = cur.y + dy[i];

                    if (nx < 0 || nx > h + 1 || ny < 0 || ny > w + 1) continue;
                    if (visited[nx][ny]) continue;
                    if (matrix[nx][ny] == '*') continue;

                    // 열쇠일경우
                    if ('a' <= matrix[nx][ny] && matrix[nx][ny] <= 'z') {
                        key |= 1 << (matrix[nx][ny] - 'a'); // 열쇠 줍기
                        for (Point door: doors) {
                            // 지금 주운 열쇠로 문을 열 수 있음
                            if (Character.toLowerCase(matrix[door.x][door.y]) == matrix[nx][ny]) {
                                if (!visited[door.x][door.y]) {
                                    matrix[door.x][door.y] = '.';
                                    visited[door.x][door.y] = true;
                                    // 큐에 넣어서 탐색
                                    dq.addLast(new Point(door.x, door.y));
                                }

                            }
                        }

                    }

                    // 문일 경우
                    if ('A' <= matrix[nx][ny] && matrix[nx][ny] <= 'Z') {
                        char c = Character.toLowerCase(matrix[nx][ny]);
                        if ((key & (1 << c - 'a')) > 0) {
                            matrix[nx][ny] = '.';
                        } else {
                            // 문을 열지 못했을 경우 따로 저장
                            doors.addLast(new Point(nx, ny));
                            continue;
                        }
                    }

                    if (matrix[nx][ny] == '$') cnt++; // 문서 훔치기

                    dq.addLast(new Point(nx, ny));
                    visited[nx][ny] = true;
                }
            }

            sb.append(cnt).append("\n");
        }

        System.out.println(sb);
    }

    static int read() throws Exception{
        int c, n = System.in.read() & 15;
        while((c = System.in.read()) > 32) n = (n<<3) + (n<<1) + (c & 15);
        return n;
    }
}