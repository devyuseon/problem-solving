import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int res = 0;
            int divided = n / 3;
            for (int j = 0; j <= divided; j++) {
                int rest = n - j * 3;
                res += rest / 2 + 1;
            }
            sb.append(res).append("\n");
        }
        System.out.print(sb);
    }
}