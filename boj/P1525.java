import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.StringTokenizer;

class Point {
    public int idx;
    public int cnt;
    public String str;

    public Point(int idx, int cnt, String str) {
        this.idx = idx;
        this.cnt = cnt;
        this.str = str;
    }
}

public class P1525 {

    public static HashSet<String> visited = new HashSet<>();
    public static ArrayDeque<Point> q = new ArrayDeque<>();
    public static final String ANS = "123456780";

    public static void main(String[] args) throws IOException {
        Main.solution();
    }

    public static String toVisitedString(int idx, String str) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 9; i++) {
            if (i == idx) sb.append("0");
            else if (str.charAt(i) == '0') sb.append(str.charAt(idx));
            else sb.append(str.charAt(i));
        }
        return sb.toString();
    }

    public static int bfs() {
        while(!q.isEmpty()) {
            Point now = q.pollFirst();
            int[] d;
            if (now.idx % 3 == 2) d = new int[]{-3, 3, -1};
            else if (now.idx % 3 == 0) d = new int[]{-3, 3, 1};
            else d = new int[]{3, -3, 1, -1};

            for (int i = 0; i < d.length; i++) {
                int next = now.idx + d[i];
                if (0 <= next && next < 9) {
                    String check = toVisitedString(next, now.str);
                    if (visited.contains(check)) continue;
                    if (check.equals(ANS)) return now.cnt + 1;
                    visited.add(check);
                    q.addLast(new Point(next, now.cnt + 1, check));
                }
            }
        }

        return -1;
    }

    public static void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int p = 0;
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < 3; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++) {
                int tmp = Integer.parseInt(st.nextToken());
                sb.append(tmp);
                if (tmp == 0) {
                    p = 3 * i + j;
                }
            }
        }

        if (sb.toString().equals(ANS)) {
            System.out.println(0);
            System.exit(0);
        }
        visited.add(sb.toString());
        q.addLast(new Point(p, 0, sb.toString()));
        System.out.println(bfs());
    }

}