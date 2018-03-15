/**
    Given two strings check
    if one is th permutation
    of the other.
**/

import java.util.HashMap;

public class checkPermutationsBetter {

    public static void main(String[] args)
    {
        System.out.println(isPermutation("ilyass", "iyasls"));
        System.out.println(isPermutation("google", "ogggle"));
    }

    public static boolean isPermutation(String str1, String str2) {

        // Check if length differs
        if (str1.length() != str2.length()) {
            return false;
        }

        // Create a counter for str1
        int[] letters = new int[128];
        char[] str1_char_array = str1.toCharArray();
        for (char c: str1_char_array) {
            letters[c]++;
        }

        // Check if permutation
        for (int x = 0; x < str2.length(); x++) {
            int index = (int) str2.charAt(x);
            letters[index]--;
            if (letters[index] < 0) {
                return false;
            }
        }

        return true;

    }

}
