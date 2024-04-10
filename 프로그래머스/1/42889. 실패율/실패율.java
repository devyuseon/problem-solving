import java.util.*;

class Solution {

    public int[] solution(int N, int[] stages) {
        int[] answer = {};
        HashMap<Integer, Double> percentage = new HashMap<>();
        
        for (int n = 1; n < N + 1; n++) {
            int same = 0;
            int low = 0;
            
            for (int s : stages) {
                // 이하인것의 개수 세기
                // 미만인것의 개수 세기 
                if (s == n) same++;
                if (s < n) low++;
            }
            
            if ((stages.length - low) == 0) {
                percentage.put(n, 0.0);
            } else {
                percentage.put(n, (double) same / (stages.length - low));
            }   
        }
        
        return percentage.entrySet().stream()
            .sorted((o1, o2) -> Double.compare(o2.getValue(), o1.getValue()))
            .mapToInt(HashMap.Entry::getKey)
            .toArray();
    }
}