import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        double scores[] = new double[N];
        double max = 0;
        for(int i = 0; i < N; i++){
            int a = Integer.parseInt(st.nextToken());
            scores[i] = a;
            if(a > max) max = a;
        }

        double sum = 0;
        for(int j = 0; j < N; j++){
            scores[j] = scores[j] / max * 100;
            sum += scores[j];
        }
        System.out.println(sum / N);
    }
}