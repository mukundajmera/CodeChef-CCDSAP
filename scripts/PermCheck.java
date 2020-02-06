import java.util.*;

class Solution {
    public int solution(int[] A) {
        // write your code in Java SE 8
        Arrays.sort(A);
        int flag = 1;
        if(A[0] != 1){
            flag = 0;
            return flag;
        }
        for(int i  = 0;i< A.length-1;i++){
            if(A[i+1] != A[i]+1 ){
                flag = 0;
            }
        }
        return flag;
    }
}
