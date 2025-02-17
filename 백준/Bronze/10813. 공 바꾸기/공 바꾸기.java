import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] bucket = new int[N];
        for(int i = 0; i < N; i++){
            bucket[i] = i+1;
        }
        for(int j = 0; j < M; j++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = bucket[a-1];
            bucket[a-1] = bucket[b-1];
            bucket[b-1] = c;
        }
        for(int k = 0; k < N; k++){
            System.out.print(bucket[k] + " ");
        }
    }
}