import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int N = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        ArrayList<Integer> list = new ArrayList<>();
        StringTokenizer st1 = new StringTokenizer(br.readLine()," ");
        for(int i=0; i<N; i++){
            int a = Integer.parseInt(st1.nextToken());
            if(a < X){
                list.add(a);
            }
        }
        for(int b: list){
            System.out.print(b + " ");
        }
    }
}