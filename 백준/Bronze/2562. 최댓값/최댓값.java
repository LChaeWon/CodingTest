import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[9];
        int a = 0;
        int b = 0;
        for(int i = 0; i < 9; i++){
            arr[i] = Integer.parseInt(br.readLine());
            if(arr[i] > a) {
                a = arr[i];
                b = i + 1;
            }
        }
        System.out.println(a);
        System.out.println(b);
    }
}