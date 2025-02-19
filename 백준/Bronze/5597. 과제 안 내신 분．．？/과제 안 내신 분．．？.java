import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] num = new int[30];
        ArrayList arr = new ArrayList();
        for(int i = 0; i < 28; i++){
            int a = Integer.parseInt(br.readLine());
            num[a-1] = a;
        }
        for(int j = 0; j < 30; j++){
            if(num[j] == 0){
                arr.add(j+1);
            }
        }
        System.out.println(arr.get(0));
        System.out.println(arr.get(1));
    }
}