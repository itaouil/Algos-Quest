/**
    Given two strings check
    if one is th permutation
    of the other.
**/

import java.util.HashMap;

public class checkPermutation {

    public static void main(String[] args)
    {
        System.out.println(isPermutation("ilyass", "iyasls"));
        System.out.println(isUnique("google", "ooggle"));
    }

    public static boolean isPermutation(String str1, String str2) {

        // Check if length differs
        if (str1.length() != str2.length()) {
            return false;
        }

        // Create a counter for str1
        final Counter<Char> cnt = new Counter<>();
        for (int x = 0; x < str1.length(); x++) {
            cnt.add(str1.charAt(x));
        }

        // Check if permutation
        for (int x = 0; x < str2.length(); x++) {
            int woops = str2.charAt(x);
            boolean isPresent = cnt.containsKey(woops);
            int val = cnt.getValue(woops);

            if (isPresent && val != 0) {
                cnt.put(woops, cnt.get(woops) - 1);
            }
            else {
                return false;
            }
        }

        return true;

    }

}

// Counter method (Python like version)
public class Counter<T> {

    final Map<T, Integer> counter = new HashMap<>();

    // Add new item using merge
    public void add(T t) {
        counter.merge(t, 1, Integer::sum);
    }

    // Return number of counts
    public int count(T t) {
        return counter.getOrDefault(t, 0);
    }

}
