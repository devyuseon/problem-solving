import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class P15654 {

    public int n, m;
    public int[] nums;
    public int[] res;
    public StringBuilder sb = new StringBuilder();
    public int[] visited;

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void dfs(int cnt) {
        if (cnt == m) {
            for (int n : res) {
                sb.append(n).append(" ");
            }
            sb.append("\n");
        } else {
            for (int i = 0; i < n; i++) {
                if (visited[i] == 0) {
                    visited[i] = 1;
                    res[cnt] = nums[i];
                    dfs(cnt + 1);
                    visited[i] = 0;
                }
            }
        }
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        nums = new int[n];
        visited = new int[n];
        res = new int[m];

        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(nums);
        dfs(0);
        System.out.println(sb);
    }
}