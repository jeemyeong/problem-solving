import java.util.Arrays;


import java.util.ArrayList;
class Advertisement {
	public static void main(String[] args) {
		Advertisement ad = new Advertisement();
		String sentence = "AxAxAxAoBoBoB";
		String ret = ad.solution(sentence);
		System.out.println(ret);
	}
	public String solution(String sentence) {
		String answer = "";
		int[] count = new int[(int)'z' - (int)'a'];
		ArrayList<String> words = new ArrayList<String>();
		int length = sentence.length();
		for (int i = 0; i < length; i++) {
				char cur = sentence.charAt(i);
				if (isLowerCase(cur)) {
						count[getIndexFromAlphabet(cur)]++;
				}
		}
		char innerChar = '\0';
		char outerChar = '\0';
		int beginIndex = 0;
		int endIndex = 0;
		int sizeOfUpperCase = 0;
		for (int i = 0; i < length; i++) {
				char cur = sentence.charAt(i);
				if (isUpperCase(cur)) {
					sizeOfUpperCase ++;
					if(innerChar == '\0' && outerChar == '\0' && (i != beginIndex && i != endIndex )) {
						words.add(""+ cur);
					}
					continue;
				}
				if (count[getIndexFromAlphabet(cur)] != 0 && count[getIndexFromAlphabet(cur)] != 2) {
					if (innerChar != cur) {
						innerChar = cur;
						beginIndex = i-1;
						endIndex = i+1;
					} else {
						endIndex = i+1;
					}
					if (i+2 < length && sentence.charAt(i+2) != cur) {
						words.add(sentence.substring(beginIndex, endIndex+1).replaceAll(""+innerChar, ""));
						innerChar = '\0';
					}
				} else if (count[getIndexFromAlphabet(cur)] == 2) {
					if (outerChar != '\0' && outerChar != cur) {
						continue;
					}
					if (outerChar != cur) {
						outerChar = cur;
						beginIndex = i+1;
						endIndex = i+1;
					} else {
						endIndex = i-1;
						words.add(sentence.substring(beginIndex, endIndex+1).replaceAll(""+outerChar, ""));
						outerChar = '\0';
					}
				}
		}
		int sizeOfUpperCaseInOutput = 0;
		for (int i = 0; i < words.size(); i++) {
			answer += words.get(i);
			sizeOfUpperCaseInOutput += words.get(i).length();
			if (i != words.size()-1) {
				answer += " ";
			}
		}
		if (sizeOfUpperCaseInOutput != sizeOfUpperCase) {
			return "invalid";
		}
		return answer;
	}
	boolean isLowerCase(char ch) {
		return ch >= 'a' && ch <= 'z';
	}
	
	boolean isUpperCase(char ch) {
		return ch >= 'A' && ch <= 'Z';
	}
	int getIndexFromAlphabet(char ch) {
		return (int)ch - (int)'a';
	}
}