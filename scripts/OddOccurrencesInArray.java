import java.util.*;

class Solution {
    public int solution(int[] A) {
        // write your code in Java SE 8
        Arrays.sort(A);
        int value = 0;
        for(int i =0 ;i< A.length;){
            if(i == A.length -1){
                value = A[i];
                break;
            }
            if(A[i] == A[i+1]){
                i += 2;
            }else{
                value = A[i];
                break;
            }    
        }
        return value;
    }
}
