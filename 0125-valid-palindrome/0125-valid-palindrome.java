class Solution {
    public boolean isPalindrome(String s) {
       int left = 0;
       int right = s.length() - 1;
       s = s.toLowerCase();

        while(left < right){
            if(!Character.isLetterOrDigit(s.charAt(left))){
                left += 1;
                continue;
            }

            if(!Character.isLetterOrDigit(s.charAt(right))){
                right -= 1;
                continue;
            }

            if(s.charAt(left) != s.charAt(right)){
                return false;
            }

            left += 1;
            right -= 1;
        }

        return true;
    }
}