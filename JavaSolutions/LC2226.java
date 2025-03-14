class Solution {
    public boolean check(int number, int[] candies, long k){
        // we can always distribute 0 candies 
        if (number == 0){
            return true;
        }
        // System.out.println(number);
        long piles = 0;
        for (int i = 0; i < candies.length; i ++){
            int amt = candies[i] / number;
            // System.out.println(amt);
            piles += amt;
        }
        // System.out.println("---");
        return piles >= k;
    }
    public int maximumCandies(int[] candies, long k) {
        int max = 0;
        for (int i = 0; i < candies.length; i++){
            max = Math.max(candies[i], max);
        }
        int start = 0;
        int end = max;
        while (start <= end){
            int middle = start + (end - start) / 2;
            // System.out.println(middle);
            if (check(middle, candies, k)){
                start = middle + 1;
            }else{
                end = middle - 1;
            }
        }
        if (start > 0){
            return start - 1;
        }
        return start;
    }
}

// simple binary search on the solution
// binary search finds the lowest value where the check fails
// return that value - 1, or return 0 which is the floor 