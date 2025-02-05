import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int totalAmount = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());
        int sum = 0;

        for(int i = 0; i < n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int amount = Integer.parseInt(st.nextToken());
            int num = Integer.parseInt(st.nextToken());

            sum += amount * num;
        }
        if(sum == totalAmount){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
    }
}