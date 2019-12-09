import java.util.*;

class Solution {
    public int[] solution(int N, int[] A) {
        // write your code in Java SE 8
        int [] arr = new int[N];
        int max = 0,count = 0;
        for(int i = 0;i<A.length;i++){
            if(A[i] <= N){
                arr[A[i]-1] += 1;
                max = Math.max(arr[A[i]-1],max);
            }
            else if(A[i] > N){
                Arrays.fill(arr,max);
            }
        }
        //add max counter to array
        return arr;
    }
}
