import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.StringTokenizer;

public class P1167 {

    public static HashMap<Integer, ArrayList<int[]>> graph;
    public static int v;
    public static int max, node;

    public static void main(String[] args) throws IOException {
        Main.solution();
    }

    public static void dfs(int start) {
        ArrayDeque<int[]> s = new ArrayDeque<>();
        s.addLast(new int[]{start, 0}); // 정점, cost
        int[] visited = new int[v + 1];

        while (!s.isEmpty()) {
            int[] now = s.pollLast();
            visited[now[0]] = 1;
            if (max < now[1]) {
                node = now[0];
                max = now[1];
            }
            for (int[] next : graph.get(now[0])) {
                if (visited[next[0]] == 0) {
                    s.addLast(new int[]{next[0], now[1] + next[1]});
                }
            }
        }
    }

    public static void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        v = Integer.parseInt(br.readLine());

        graph = new HashMap<>();
        for (int i = 0; i < v; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken()); // 정점 번호
            if (!graph.containsKey(s)) {
                graph.put(s, new ArrayList<>());
            }
            while (true) {
                String tmp = st.nextToken();
                if (tmp.equals("-1")) {
                    break;
                }
                int e = Integer.parseInt(tmp);
                int c = Integer.parseInt(st.nextToken());
                graph.get(s).add(new int[]{e, c}); // 도착점, 비용
            }

        }

        dfs(1);
        dfs(node);

        System.out.println(max);
    }

}