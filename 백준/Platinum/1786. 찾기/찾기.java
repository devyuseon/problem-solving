import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] txt = br.readLine().toCharArray();
        char[] pat = br.readLine().toCharArray();
        int t = txt.length;
        int p = pat.length;
        StringBuilder sb = new StringBuilder();
        int cnt = 0;

        // LPS 만들기
        int[] lps = new int[p];
        int len = 0;
        int i = 1;
        while (i < p) {
            if (pat[i] == pat[len]) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }

        // KMP 알고리즘
        i = 0; // index of T
        int j = 0; // index of P
        while (i < t) {
            if (pat[j] == txt[i]) {
                i++;
                j++;
                // 패턴 찾음
                if (j == p) {
                    sb.append(i - j + 1).append(" ");
                    cnt++;
                    j = lps[j - 1];
                }
            } else {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }

        System.out.println(cnt);
        System.out.println(sb);
    }
}