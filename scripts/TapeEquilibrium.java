class Solution {
    public int solution(int[] A) {
        // write your code in Java SE 8
        int min = Integer.MAX_VALUE;
        int left = A[0],right = 0;
        
        for(int i = 1;i<A.length;i++){
            right += A[i];
        }
        
        for(int i = 1;i<A.length;i++){
            min = Math.min(min,Math.abs(left - right));
            left += A[i];
            right -= A[i];
        }
    return min;
    }
}
