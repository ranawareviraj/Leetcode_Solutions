import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int hIndex(int[] citations) {
        // Sorting the array in descending order
        Arrays.sort(citations);

        // Finding the hIndex
        int n = citations.length;
        for (int i = 0; i < n; i++) {
            int hIndex = n - i;
            if (citations[i] >= hIndex) {
                return hIndex;
            }
        }

        return 0;
    }
}
