class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> map1 = new HashMap<>();

        for(char c : s.toCharArray()) {
            int value1 = map1.getOrDefault(c,0) + 1;
            map1.put(c, value1);
        }

        HashMap<Character, Integer> map2 = new HashMap<>();

        for(char c : t.toCharArray()) {
            int value2 = map2.getOrDefault(c, 0) + 1;
            map2.put(c, value2);
        }

        if (map1.equals(map2)) {
            return true;
        }

        return false;
    }
}
