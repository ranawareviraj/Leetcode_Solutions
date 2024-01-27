class Solution {
    public boolean backspaceCompare(String s, String t) {
        return typedString(s).equals(typedString(t));
    }

    private String typedString(String str){
        StringBuilder stack = new StringBuilder();

        for(int i = 0; i < str.length(); i++){
            char ch = str.charAt(i);
            if(ch != '#'){
                stack.append(ch);
            } else if (stack.length() > 0){
                stack.deleteCharAt(stack.length() - 1);
            }
        }
        return stack.toString();
    }
}