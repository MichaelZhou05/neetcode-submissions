class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map1 = new HashMap<>();
    
        for(String str1 : strs){
            int [] hashTable = new int[26];
            for(char c: str1.toCharArray()){
                hashTable[(int) c - (int)'a'] ++;
            }
            String hashTableString = Arrays.toString(hashTable);
            if(!map1.containsKey(hashTableString)){
                map1.put(hashTableString, new ArrayList<String>());
            }
            map1.get(hashTableString).add(str1);
        }
        
        return new ArrayList<>(map1.values());
        
    }
}
