class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if( !(str1+str2).equals(str2+str1)){ return "";}
        
        int str1Length = str1.length();
        int str2Length = str2.length();
        int gcd = str2Length;
        
        
        int i = 1;
        while(str1Length%gcd != 0){
            i++;
            gcd = str2Length/i;
        }
        
        return str1.substring(0,gcd);
    }
}