class Solution {
    public int solution(int X, int[] A) {
        // write your code in Java SE 8
        int flag = -1;
        for(int i = 0;i<A.length;i++){
            if(A[i] == X){
                flag = i;
            }
        }
        return flag;
    }
}
