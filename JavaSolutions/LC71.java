import java.util.ArrayList;

public class LC71 {
    public String simplifyPath(String path) {
        ArrayList<String> words = new ArrayList<>();
        StringBuilder progress = new StringBuilder();
        boolean prevSlash = false;
        for (int i = 0; i < path.length(); i++) {
            if (path.charAt(i) == '/') {
                if (!prevSlash || i == path.length() - 1) {
                    String curr = progress.toString();
                    if (curr.equals("..")) {
                        words.remove(words.size() - 1);
                    } else if (curr.equals(".")) {

                    } else if (!curr.equals("")) {
                        words.add(curr);
                    }
                    progress.delete(0, progress.length());
                    continue;
                }
            }
            if (i == path.length() - 1) {
                progress.append(path.charAt(i));
                String curr = progress.toString();
                if (curr.equals("..")) {
                    words.remove(words.size() - 1);
                } else if (curr.equals(".")) {

                } else if (!curr.equals("")) {
                    words.add(curr);
                }
                progress.delete(0, progress.length());
                continue;
            }
            if (path.charAt(i) == '/') {
                prevSlash = true;
            } else {
                prevSlash = false;
            }
            progress.append(path.charAt(i));
        }
        for (String w : words) {
            progress.append('/');
            progress.append(w);
        }

        if (progress.isEmpty()) {
            return "/";
        }

        return progress.toString();
    }

    public static void main(String[] args) {
        LC71 test = new LC71();
//        System.out.println(test.simplifyPath("///home//foo/../"));
//        System.out.println(test.simplifyPath("//../"));
//        System.out.println(test.simplifyPath("//../pop/.."));
//        System.out.println(test.simplifyPath("//../pop/../wew////wewq/wq"));
        System.out.println(test.simplifyPath("/a//b////c/d//././/.."));

    }
}

// this solution was really difficult to code honestly. Probably took me an hour longer than it should have
// it works pretty fast, but there are nuances in logic that make it error prone
// the gist is to track all the words between pairs of / /
// if the word is a . or a .. do something special
// then concat together using string builder


// the less dumb solution uses string split and then puts the words in a stack
// in the dot case, don't add to string, in dot dot case, pop, then use a string builder to append the / in between words

