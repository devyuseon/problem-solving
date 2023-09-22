import java.util.*;

class Solution {
        public int YEAR = 28 * 12;
    public int MONTH = 28;
    public int[] solution(String today, String[] terms, String[] privacies) {
        ArrayList<Integer> answers = new ArrayList<>();
        int todayInt = parseDateToInt(today);
        HashMap<String, Integer> rules = new HashMap<>();
        for (String term : terms) {
            String[] splited = term.split(" ");
            rules.put(splited[0], Integer.parseInt(splited[1]) * MONTH);
        }
        int idx = 1;
        for (String privacy : privacies) {
            String[] splited = privacy.split(" ");
            int day = parseDateToInt(splited[0]);
            int dayEnd = day + rules.get(splited[1]);
            if (todayInt > dayEnd || todayInt == dayEnd) {
                answers.add(idx);
            }
            idx++;
        }

        int[] result = new int[answers.size()];
        for (int i = 0; i < answers.size(); i++) {
            result[i] = answers.get(i);
        }

        return result;
    }
    
    public int parseDateToInt(String date) {
        String[] daySplit = date.split("\\.");
        int year = Integer.parseInt(daySplit[0]);
        int month = Integer.parseInt(daySplit[1].charAt(0) == '0' ? String.valueOf(daySplit[1].charAt(1)) : daySplit[1]);
        int day = Integer.parseInt(daySplit[2].charAt(0) == '0' ? String.valueOf(daySplit[2].charAt(1)) : daySplit[2]);
        return year * YEAR + month * MONTH + day;
    }
}