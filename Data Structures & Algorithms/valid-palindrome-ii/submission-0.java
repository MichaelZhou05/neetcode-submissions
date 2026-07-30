class Solution {
    public boolean validPalindrome(String s) {
        int l=0,r=s.length()-1;
        
        char [] stringArray = s.toCharArray();
        
        int diffCounter = 0;
        while(l<r){
            if(stringArray[l] == stringArray[r]){
                l++;
                r--;
                continue;
            }
            
            diffCounter++;
            if(stringArray[l+1] == stringArray[r]){
                l++;
            }else if(stringArray[l] ==  stringArray[r-1]){
                r--;
            }else{
                return false;
            }
        }
        
        return diffCounter<=1;
    }
}