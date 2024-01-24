import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static String[] commands = {" ", "+", "-"};

    public static ArrayList<String> results;

    public static void dfs(int cur, int end, StringBuilder sb) {
        if (cur > end) {
            results.add(sb.toString());
            return;
        }

        for (int i = 0; i < 3; i++) {
            String command = commands[i];
            sb.append(command).append(cur);
            dfs(cur + 1, end, sb);
            sb.delete(sb.length() - 2, sb.length());
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            int n = Integer.parseInt(br.readLine());
            results = new ArrayList<>();
            dfs(2, n, new StringBuilder().append("1"));
            for (String result : results) {
                String _result = result.replaceAll(" ", "");
                String[] plusSplit = _result.split("\\+");
                int sum = 0;
                for (String token : plusSplit) {
                    String[] minusSplit = token.split("-");
                    if (minusSplit.length == 1) {
                        sum += Integer.parseInt(minusSplit[0]);
                    } else {
                        int tmp = Integer.parseInt(minusSplit[0]);
                        for (int j = 1; j < minusSplit.length; j++) {
                            tmp -= Integer.parseInt(minusSplit[j]);
                        }
                        sum += tmp;
                    }
                }

                if (sum == 0) {
                    sb.append(result).append("\n");
                }
            }

            if (i != N - 1) {
                sb.append("\n");
            }
        }

        System.out.print(sb);
    }
}