import java.util.*;

public class baek11022 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        
        for(int i=0;i<A;i++) {
            int B = sc.nextInt();
            int C = sc.nextInt();   

            System.out.println("Case #"+(i+1)+": "+B+" + "+C+" = "+(B+C));
        }
        sc.close();         
    }
}