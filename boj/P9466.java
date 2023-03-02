import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P9466 {

    public static int[] visited;
    public static int[] finished;
    public static int[] choice;
    public static int cnt;

    public static void dfs(int v) {
        visited[v] = 1; // 방문

        int next = choice[v];
        if (visited[next] == 0) dfs(next);
        else if (finished[next] == 0) {
            // 방문 했음에도 안끝남 == 사이클
            // 사이클 돌면서 사이클 노드 개수 카운트
            int tmp = next;
            while (true) {
                cnt++;
                tmp = choice[tmp];
                if (tmp == next) break;
            }
        }
        // dfs가 끝난 노드 체크
        finished[v] = 1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            // 입력
            int n = Integer.parseInt(br.readLine());
            choice = new int[n + 1];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 1; j < n + 1; j++) {
                choice[j] = Integer.parseInt(st.nextToken());
            }
            visited = new int[n + 1];
            finished = new int[n + 1];
            cnt = 0;
            for (int j = 1; j < n + 1; j++) {
                if (visited[j] == 0) dfs(j);
            }
            sb.append(n - cnt).append("\n");
        }
        System.out.println(sb);
    }
}