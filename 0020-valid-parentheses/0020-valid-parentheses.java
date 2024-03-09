class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> map = new HashMap<>();
        map.put('{','}');
        map.put('[',']');
        map.put('(',')');

        for(char ch : s.toCharArray()){
            if(map.containsKey(ch)){
                stack.push(ch);
            } else{
                if(stack.isEmpty()){
                    return false;
                }

                char top = stack.pop();
                if(map.get(top) != ch){
                    return false;
                }
            }
        }
        
        return stack.isEmpty();
    }
}