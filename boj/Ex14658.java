import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class Pair {
    int x, y;

    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
public class Main {

    static int n, m, l, k;
    static List<Pair> stars;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        stars = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            stars.add(new Pair(x, y));
        }

        int res = 0;
        for (Pair p: stars) {
            for (Pair q: stars) {
                res = Math.max(res, boundCount(p.x, q.y));
            }
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.valueOf(k - res));
        bw.close();
        //System.out.println(k - res);
    }

    private static int boundCount(int i, int j) {
        int cnt = 0;
        for (Pair p: stars) {
            int x = p.x; int y = p.y;
            if (i <= x && x <= i + l && j <= y && y <= j + l) cnt++;
        }
        return cnt;
    }
}