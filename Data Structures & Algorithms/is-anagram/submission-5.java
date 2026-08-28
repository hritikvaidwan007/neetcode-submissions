class Solution {
    public boolean isAnagram(String s, String t) {

        // s.length()
        // s.toCharArray()
        // map1.getOrDefault(c,0) + 1
        // map1.equals(map2)
        // map1.put(c, value)

        // Edge case
        if(s.length() != t.length()) {
            return false;
        }

        // Create first hasmao
        HashMap<Character, Integer> map1 = new HashMap<>();
        for(char c : s.toCharArray()) {
            int value1 = map1.getOrDefault(c,0) + 1;
            map1.put(c, value1);
        }

        // create second hashmap
        HashMap<Character, Integer> map2 = new HashMap<>();
        for(char c : t.toCharArray()) {
            int value2 = map2.getOrDefault(c, 0) + 1;
            map2.put(c, value2);
        }

        // compare both
        if (map1.equals(map2)) {
            return true;
        }

        return false;
    }
}
