import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        int[] arr = new int[26];
        for(int i=0;i<arr.length;i++){
            arr[i] = -1;
        }

        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        for(int j = 97; j < 123; j++){
            for(int i = 0; i < s.length(); i++) {
                int a = s.charAt(i);
                if (j == a) {
                    arr[j-97] = i;
                    break;
                }
            }
        }
        for(int k = 0; k < arr.length; k++){
            System.out.print(arr[k] + " ");
        }
    }
}