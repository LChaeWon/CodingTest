import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();

        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();

        for(int i=0; i < 3; i++){
            sb1.append(a.charAt(2-i));
            sb2.append(b.charAt(2-i));
        }
        if(Integer.parseInt(String.valueOf(sb1)) > Integer.parseInt(String.valueOf(sb2)))
        {System.out.print(sb1);}
        else {System.out.print(sb2);}

    }
}