import java.util.*;

public class baek2884 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int H = sc.nextInt();
        int M = sc.nextInt();

        sc.close();

        if (M < 45) {
            if (H == 0) {
                H = 23;
                M = 60 - (45 -M);
            } else {
                H = H - 1;
                M = 60 - (45 -M);
            }

        } else {
            M = M - 45;
        }

        System.out.println(H + " " + M);
    }
    
}
