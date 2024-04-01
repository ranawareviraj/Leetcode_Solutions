class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> charMap = Map.of('{', '}', '[', ']', '(', ')');
        Stack<Character> stack = new Stack<>();

        for (char ch : s.toCharArray()) {
            if (charMap.containsKey(ch)) {
                stack.push(ch);
            } else if (stack.isEmpty() || (charMap.get(stack.pop()) != ch)) {
                return false;
            }
        }

        return stack.isEmpty();
    }
}