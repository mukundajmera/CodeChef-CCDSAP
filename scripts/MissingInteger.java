import java.util.*;

class Solution {
    public int solution(int[] A) {
        // write your code in Java SE 8
        int value = 1,diff = 0;
        Arrays.sort(A);
        //check for the length negative
        if(A[A.length-1] <= 0){
            return value;
        }
        for(int i = 1;i<A.length;i++){
            diff = A[i] - A[i-1];
            if(A[i] > 0 && diff <= 1){
                value = A[i];
            }else{
                value = A[i-1]+1;
                return value;
            }    
        }
        return value + 1;
    }
}

//another way work for negative and rest with value counter
// Arrays.sort(A);
//    int value = 1;

//    for (int i : A) {
//      if (i == value) {
//        value++;
//      }
//    }

//    return value;