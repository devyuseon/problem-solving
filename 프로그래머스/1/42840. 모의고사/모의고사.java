import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        ArrayList<Integer> results = new ArrayList<>();
        int[] pattern1 = {1, 2, 3, 4, 5};
        int[] pattern2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] pattern3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int score1 = 0;
        int score2 = 0;
        int score3 = 0;
        
        int p1 = 0;
        int p2 = 0;
        int p3 = 0;
        
        int l1 = pattern1.length;
        int l2 = pattern2.length;
        int l3 = pattern3.length;
        
        for (int a : answers) {
            if (pattern1[p1++] == a) score1++;
            if (pattern2[p2++] == a) score2++;
            if (pattern3[p3++] == a) score3++;
            if (p1 == l1) p1 = 0;
            if (p2 == l2) p2 = 0;
            if (p3 == l3) p3 = 0;
        }
        
        int max = score1;
        if (max < score2) max = score2;
        if (max < score3) max = score3;
        
        if (score1 == max) results.add(1);
        if (score2 == max) results.add(2);
        if (score3 == max) results.add(3);
        
        return results.stream().mapToInt(Integer::intValue).toArray();
    }
}