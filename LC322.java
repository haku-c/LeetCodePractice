import java.util.Arrays;
import java.util.Collections;

public class LC322 {
    public int coinChange(int[] coins, int amount) {
        if (amount == 0) {
            return 0;
        }
        int count = 0;
        Arrays.sort(coins);
        if (amount / coins[coins.length - 1] == 0) {
            return -1;
        }
        for (int i = coins.length - 1; i > 0; i--) {
            int c = coins[i];
            int num = amount / c;
            count += num;
            amount = amount % c;
        }
        System.out.println(count);
        return count;
    }
}
