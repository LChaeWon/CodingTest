import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    int h = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());
    int t = Integer.parseInt(br.readLine());

    br.close();

    m += t;

    h += m/60;
    m %= 60;

    h %= 24;

    System.out.println(h + " " + m);
}
}