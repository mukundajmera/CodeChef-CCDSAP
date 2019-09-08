class Solution {
    public int solution(int N) {
        // write your code in Java SE 8
        int gap = 0,max = 0;
        String bin = String.valueOf(Integer.toBinaryString(N));
        //System.out.println(bin);
        for(int i = 0;i < bin.length();i++){
            if(bin.charAt(i) == '1'){
            if(gap > max){
            max = gap;
            }
            gap = 0;
            }
            else{
                gap += 1;
            }
            //System.out.println(bin.charAt(i)+" "+gap);
        }
        return max;
    }
}
