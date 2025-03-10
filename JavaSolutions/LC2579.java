class Solution {
    public long coloredCells(int n) {
        // 1 + 4 + 8 + 12 + 16
        // 4, 12, 24, 40, 60, 84
        // the below sequence is just the sum of consecutive elements starting from 1
        // 1, 3, 6, 10, 15, 21

        // iterative
        // long res = 1
        // long add = 4;
        // for (int i = 1; i < n; i ++){
        //     res += add;
        //     add += 4;
        // }
        
        // formula
        // force long multiplication and division by using L
        // use the formula for n consecutive elements starting from 1 up to n - 1
        return 1L + (4L * (n - 1L) * n) / 2L;
    }
}