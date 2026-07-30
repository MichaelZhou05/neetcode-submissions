class Solution {
    public boolean isAnagram(String s, String t) {
        int[] sChars = new int[26];


        for(char ch : s.toCharArray()){
            sChars[(int) ch - (int)'a'] = sChars[(int) ch - (int)'a'] +1;
        }

        for(char ch : t.toCharArray()){
            sChars[(int) ch - (int)'a'] = sChars[(int) ch - (int)'a'] -1;
        }

        for(int val : sChars){
            if(val != 0){return false;}
        }
        return true;
    }

}
