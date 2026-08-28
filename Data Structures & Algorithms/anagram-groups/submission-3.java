class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        // str1.toCharArray()
        // Arrays.sort(chars1)
        // map.containsKey(key)
        // map1.putIfAbsent
        // res.get(sortedS).add(s)
        // map1.values()

        // Input: strs = ["act","pots","tops","cat","stop","hat"]
        // Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]


        Map<String, List<String>> map1 = new HashMap<>();

        for(String s : strs) {
            // just because sorting is only allowed in array
            char[] charArray = s.toCharArray(); // str to Array
            Arrays.sort(charArray); // sort array
            String sortedS = new String(charArray); // array to str

            map1.putIfAbsent(sortedS, new ArrayList<>());
            map1.get(sortedS).add(s); // ["act", "cat"].add("tac");
        }

        // map1
        // {
        //     "act": ["cat", "act"],
        //     "opst": ["pots", "stop"]
        // }

        return new ArrayList<>(map1.values()); 
        // pitfall remember: .values() returns a collection, not a list
        // so we converted Collection<List<String>> to ArrayList<List<String>>
        // returns [["cat", "act"], ["pots", "stop"]]
        
    }
}
