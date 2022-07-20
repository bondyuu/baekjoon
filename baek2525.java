import java.util.Scanner;

public class baek2525 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int H = sc.nextInt();
        int M = sc.nextInt();
        int A = sc.nextInt();

        int plusH = A / 60;
        int plusM = A % 60;

        if (M + plusM >= 60){
            M = M + plusM - 60;

            if (H + plusH + 1>= 24) {
                H = H + plusH + 1 - 24;
                
            } else {
                H = H + plusH + 1;
            }
        } else {
            M = M + plusM;

            if (H + plusH >= 24) {
                H = H + plusH - 24;
                
            } else {
                H = H + plusH;
            }
        }

        System.out.println(H + " " + M);
    }
    
}
