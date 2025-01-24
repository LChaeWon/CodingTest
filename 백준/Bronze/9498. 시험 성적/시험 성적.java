import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        if(a > 89) System.out.println("A");
        else if(a > 79) System.out.println("B");
        else if(a > 69) System.out.println("C");
        else if(a > 59) System.out.println("D");
        else System.out.println("F");

    }
}