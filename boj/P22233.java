import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class P22233 {

    public int n;
    public int m;

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        StringBuilder sb = new StringBuilder();

        HashSet<String> hashSet = new HashSet<>();

        for (int i = 0; i < n; i++) {
            hashSet.add(br.readLine());
        }

        for (int i = 0; i < m; i++) {
            String[] written = br.readLine().split(",");
            for (String s: written) {
                hashSet.remove(s);
            }
            sb.append(String.valueOf(hashSet.size()) + '\n');
        }

        System.out.println(sb.toString().trim());
    }
}