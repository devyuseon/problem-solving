import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P15657 {

    public int n, m;
    public int[] nums;
    public int[] res;
    public StringBuilder sb = new StringBuilder();
    public int[] visited;

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void dfs(int cnt, int start) {
        if (cnt == m) {
            for (int n : res) {
                sb.append(n).append(" ");
            }
            sb.append("\n");
        } else {
            for (int i = start; i < n; i++) {
                res[cnt] = nums[i];
                dfs(cnt + 1, i);
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
        dfs(0, 0);
        System.out.println(sb);
    }
}