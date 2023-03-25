import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] nums = new String[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            nums[i] = st.nextToken();
        }

        Arrays.sort(nums, (o1, o2) -> (o2  + o1).compareTo(o1 + o2));
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            sb.append(nums[i]);
        }
        
        if (sb.toString().startsWith("0")) {
            System.out.println("0");
        } else {
            System.out.println(sb);  
        }        
    }
}
