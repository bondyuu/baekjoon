import java.util.Scanner;

public class baek2739 {

	public static void main(String[] args) {
		int num;
		
		Scanner sc = new Scanner(System.in);
		
		num = sc.nextInt();
		
		sc.close();
		
		
		for (int i = 1; i < 10; i++) {
			System.out.println(num+" * "+i+" = "+(num*i));
		}

	}

}