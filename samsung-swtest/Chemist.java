/*
You should use the statndard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful. 
*/

import java.util.Scanner;
import java.util.TreeSet;
import java.util.Set;
import java.util.Arrays;

/*
   As the name of the class should be Solution , using Solution.java as the filename is recommended.
   In any case, you can execute your program by running 'java Solution' command.
 */
class Chemist {
    static Set<String> symbolsSet = new TreeSet<String>();
	public static void main(String args[]) throws Exception	{
        String[] syombolsArray = {"H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al",
        "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe",
        "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr",
        "Y","Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb",
        "Te", "I", "Xe", "Cs", "Ba", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au",
        "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Rf", "Db", "Sg",
        "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Fl", "Lv", "La", "Ce", "Pr", "Nd",
        "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Ac",
        "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md",
        "No", "Lr"};
        for (String symbols : syombolsArray) {
            symbolsSet.add(symbols.toLowerCase());
        }
		Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        sc.nextLine();
		for(int test_case = 0; test_case < T; test_case++) {
            String str = sc.next();
            sc.nextLine();
            String ret = solve(str);
            System.out.println("Case #"+(test_case+1));
			System.out.println(ret);
		}
    }
    public static String solve(String str) {
        int length = str.length();
        int[] dp = new int[length+1];
        int MAX_INT = 2000000000;
        dp[0] = 1;
        for (int j = 1; j <= length; j++) {
            dp[j] = MAX_INT;
            for (int i = 1; i <= 2; i++) {
                if ((j-i) < 0){
                    continue;
                }
                if (symbolsSet.contains(str.substring(j-i, j))) {
                    dp[j] = Math.min(dp[j], dp[j-i]+1);
                }
            }
        }
        if (dp[length] == MAX_INT) {
            return "NO";
        }
        return "YES";
    }
}