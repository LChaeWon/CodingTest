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

        int[] arr = new int[N];
        int[] temp = new int[N];

        for(int i = 0; i < N; i++){
            arr[i] = i + 1;
            temp[i] = i + 1;
        }

        for(int j = 0; j < M; j++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = b;
            for(int k = a-1; k < b; k++){
                arr[k] = temp[c-1];
                --c;
            }
            temp = arr.clone();

        }
        for (int z = 0; z < N; z++) {
            System.out.print(arr[z] + " ");
        }
    }
}