class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        int rows = matrix.length;
        int columns = matrix[0].length;
        int up = 0;
        int left = 0;
        int right = columns - 1;
        int down = rows - 1;

        while (result.size() < rows * columns) {
            // Traverse left to right
            for(int col = left; col <= right; col++){
                result.add(matrix[up][col]);
            }  

            // Traverse top to bottom
            for(int row = up + 1; row <= down; row++){
                result.add(matrix[row][right]);
            }

            // If we are not on the same row that has traversed before
            if(up != down){
                // Traverse from right to left.
                for(int col = right - 1; col >= left; col--){
                    result.add(matrix[down][col]);
                }
            }

            // If we are not on the same column that has traversed before
            if(right != left){
                // Traverse from bottom to top.
                for(int row = down - 1; row > up; row--){
                    result.add(matrix[row][left]);
                }
            }

            up += 1;
            down -= 1;
            left += 1;
            right -= 1;
        }

        return result;
    }   
}