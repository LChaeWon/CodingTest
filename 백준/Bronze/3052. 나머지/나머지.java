import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i = 0; i < 10; i++){
            int a =  Integer.parseInt(br.readLine()) % 42;
            if(!arr.contains(a))
                arr.add(a);

        }
        System.out.println(arr.size());
    }
}