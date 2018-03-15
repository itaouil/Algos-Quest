/**
    Is the string made
    up of only unique
    characters.

    Assumptions:
        - String is in ASCII format
        - ASCII made of 128 chars (possibly 256 if extended)
**/

public class isUnique {

    public static void main(String[] args)
    {
        System.out.println(isUnique("uniqe"));
        System.out.println(isUnique("ilyass"));
        System.out.println(isUnique("google"));
    }

    public static boolean isUnique(String string) {

        // Check if string exceeds
        // possible chars
        if (string.length() > 128) {
            return false;
        }

        // Boolean array
        boolean[] bool_array = new boolean[128];

        // Check if unique
        for (int i = 0; i < string.length(); i++) {

            // Get ASCII index
            int ascii_index = string.charAt(i);

            // Not unique
            if (bool_array[ascii_index]) {
                return false;
            }

            else {
                bool_array[ascii_index] = true;
            }
        }

        return true;
    }
}
