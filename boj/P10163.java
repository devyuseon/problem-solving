import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P10163 {

    public int n;
    public int m;

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        int[][] matrix = new int[1001][1001];

        for (int i = 1; i < n + 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());

            for (int p = 0; p < w; p++) {
                for (int q = 0; q < h; q++) {
                    matrix[x + p][y + q] = i;
                }
            }
        }

        int[] res = new int[n + 1];
        for (int i = 0; i < 1001; i++) {
            for (int j = 0; j < 1001; j++) {
                res[matrix[i][j]] += 1;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < n + 1; i++) {
            sb.append(String.valueOf(res[i]) + '\n');
        }

        System.out.println(sb);
    }
}