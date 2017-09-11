import java.util.Arrays;
class Advertisement {
    public static void main(String[] args) {
        Advertisement ad = new Advertisement();
        String sentence = "SpIpGpOpNpGJqOqA";
        String ret = ad.solution(sentence);
        System.out.println(ret);

    }
    public String solution(String sentence) {
        String answer = "";
        int[] count = new int[(int)'z' - (int)'a'];
        int length = sentence.length();
        for (int i = 0; i < length; i++) {
            char cur = sentence.charAt(i);
            if (isLowerCase(cur)) {
                count[(int)cur - (int)'a']++;
            } else if (isUpperCase(cur)) {
                answer += cur;
            }
        }
        System.out.println(Arrays.toString(count));
        return answer;
    }
    boolean isLowerCase(char ch) {
        return ch >= 'a' && ch <= 'z';
    }
    
    boolean isUpperCase(char ch) {
        return ch >= 'A' && ch <= 'Z';
    }
  }