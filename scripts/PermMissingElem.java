import java.util.*;

class Solution {
    public int solution(int[] A) {
        // write your code in Java SE 8
        long n = A.length + 1;
        long total = (n * (n + 1))/2;
        for(long i : A){
            total -= i;
        }
        return ((int)total);
    }
}
