import java.io.*;
import java.util.StringTokenizer;

public class Main{
public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int test = Integer.parseInt(br.readLine());
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    for(int i = 1; i < test + 1; i++){
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int sum = Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken());
        bw.write("Case #" + i + ": " + sum);
        bw.newLine();
    }
    br.close();
    bw.flush();
    bw.close();
}
}
