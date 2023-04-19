import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class LC17 {
    public List<String> letterCombinationsAttempt(String digits) {
        // TKE am bad
        HashMap<Character, ArrayList<Character>> map = new HashMap<>();
        ArrayList<String> res = new ArrayList<>();
        map.put('2', new ArrayList<Character>(Arrays.asList('a', 'b', 'c')));
        map.put('3', new ArrayList<Character>(Arrays.asList('d', 'e', 'f')));
        map.put('4', new ArrayList<Character>(Arrays.asList('g', 'h', 'i')));
        map.put('5', new ArrayList<Character>(Arrays.asList('j', 'k', 'l')));
        map.put('6', new ArrayList<Character>(Arrays.asList('m', 'n', 'o')));
        map.put('7', new ArrayList<Character>(Arrays.asList('p', 'q', 'r', 's')));
        map.put('8', new ArrayList<Character>(Arrays.asList('t', 'u', 'v')));
        map.put('9', new ArrayList<Character>(Arrays.asList('w', 'x', 'y', 'z')));
        res.add("");
        for (int i = 0; i < digits.length(); i++) {
            Character curr = digits.charAt(i);
            List<Character> add = map.get(curr);

            for (int j = 0; j < res.size(); j++) {
                String s = res.get(j);
                for (Character c : add) {
                    String newString = c + s;
                    res.add(newString);
                }
                // definitely TLE because of the remove
                res.remove(j);
            }
        }
        return res;
    }

    // just because you can use a hashmap does not mean you should oops
    // use array indexing to avoid needing hashmap, starts at 1
    // this approach goes one by one through the digits string (backtrack) Instead of starting with all say 3 characters at the arr index,
    // we start with one string and tack onto it
    String[] arr = new String[]{"", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        List<String> list = new ArrayList<>();
        if (digits.length() == 0) return list;
        StringBuilder sb = new StringBuilder();
        backtrack(list, digits, sb, 0);
        return list;
    }

    private void backtrack(List<String> list, String str, StringBuilder sb, int index) {
        // when we have reached a string of the correct size, add it to the list (passed as our res)
        if (sb.length() == str.length()) {
            list.add(sb.toString());
            return;
        } else {
            // quick conversion to int, current index in the digits string
            int val = str.charAt(index) - '0';
            // for every string in the current index append to string builder, and recurse (backtrack)
            for (int i = 0; i < arr[val - 1].length(); i++) {
                sb.append(arr[val - 1].charAt(i));
                // increase the index so you add onto this string
                backtrack(list, str, sb, index + 1);
                // delete here to make sure that you are resetting the string for the next iteration of the loop
                sb.deleteCharAt(sb.length() - 1);
            }
        }
    }

}
