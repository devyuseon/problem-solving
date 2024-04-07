import java.util.*;

class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = {};
        int n = arr1.length;
        int m = arr1[0].length;
        int p = arr2[0].length;
        
        // System.out.println(n);
        // System.out.println(m);
        answer = new int[n][p];
        
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < p; k++) {
                for (int j = 0; j < m; j++) {
                    answer[i][k] += arr1[i][j] * arr2[j][k];
                }
            }
        }
        
        return answer;
    }
}