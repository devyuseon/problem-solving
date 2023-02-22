import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class P1005 {

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        while (t > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            int[] times = new int[n + 1];
            int[] timeSum = new int[n + 1];
            int[] inputs = new int[n + 1];
            HashMap<Integer, ArrayList<Integer>> graph = new HashMap<>();

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                times[i + 1] = Integer.parseInt(st.nextToken());
            }
            for (int i = 0; i < k; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                if (!graph.containsKey(x)) graph.put(x, new ArrayList<>());
                graph.get(x).add(y);
                inputs[y]++;
            }
            int w = Integer.parseInt(br.readLine());

            ArrayDeque<Integer> q = new ArrayDeque<>();
            for (int i = 1; i < n + 1; i++) {
                if (inputs[i] == 0) {
                    q.addLast(i);
                    timeSum[i] = times[i];
                }
            }

            while (!q.isEmpty()) {
                Integer now = q.pollFirst();

                if (now == w) {
                    break;
                }

                if (!graph.containsKey(now)) continue;
                for (Integer next : graph.get(now)) {
                    inputs[next]--;

                    // 선행노드 + 현재노드시간 최대인것으로 갱신함
                    timeSum[next] = Math.max(timeSum[next], timeSum[now] + times[next]);

                    if (inputs[next] == 0) {
                        q.addLast(next);
                    }
                }
            }

            System.out.println(timeSum[w]);

            t--;
        }
    }
}