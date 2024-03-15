class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m - 1, p2 = n - 1;
        int resultLength = m + n;

        for (int writer = resultLength - 1; writer >= 0 ; writer--) {
            if(p2 >= 0 && p1 >= 0){
                nums1[writer] = (nums1[p1] > nums2[p2]) ? nums1[p1--] : nums2[p2--];
            } else if(p1 >= 0){
                nums1[writer] = nums1[p1--];
            } else{
                nums1[writer] = nums2[p2--];
            }
        }
    }
}