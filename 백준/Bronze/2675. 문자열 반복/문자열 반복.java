import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        for(int i = 0; i < a; i++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");

            int b = Integer.parseInt(st.nextToken());
            String s = st.nextToken();

            for(int j = 0; j < s.length(); j++){
                for(int z = 0; z < b; z++){
                System.out.print(s.charAt(j));
                }
            }
            System.out.println();
        }
    }
}