class Solution {
    public boolean checkPowersOfThree(int n) {
        // 3 ** 14
        while (n > 0){
            int remainder = n % 3;
            if (remainder == 2){
                return false;
            }
            n = n / 3;
        }
        return true;

    }
}

// This is a good reminder for how to get the binary representation of a number:
// It follows a similar approach where we just concatenate the remainder after dividing by 2 (in reverse)

// This sol is more intuitive:
// we just subtract the current power up to 2 times. If we need to subtract it twice, then there is a 2 in the ternary representation
// in that case, return false. 

// class Solution {

//     public boolean checkPowersOfThree(int n) {
//         int power = 0;

//         // Find the largest power that is smaller or equal to n
//         while (Math.pow(3, power) <= n) {
//             power++;
//         }

//         while (n > 0) {
//             // Subtract current power from n
//             if (n >= Math.pow(3, power)) {
//                 n -= (int) Math.pow(3, power);
//             }
//             // We cannot use the same power twice
//             if (n >= Math.pow(3, power)) {
//                 return false;
//             }
//             // Move to the next lower power
//             power--;
//         }

//         // n has reached 0
//         return true;
//     }
// }