// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int N) {
        // write your code in Java SE 8
        int value = 0,count = 0,digit = 0;
        if(N == 0){
            return 1;
        }
        String s = String.valueOf(N);
        int [] arr = new int[s.length()];
        while(N > 0){
            digit = N % 10;
            arr[count++] = digit;
            N = N / 10;
        }
        //sorting
        Arrays.sort(arr);
        //counting
        value = 1;
        for(int i = 1;i<s.length();i++){
            if(arr[i] != arr[i-1]){
                value += 1;
            } 
        }
        return value;
    }
}
