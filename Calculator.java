/**
 * 
 */
package calculator;
import java.util.Scanner;
/**
 * 
 */
public class Calc1 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		double n1;
		double n2;
		double op;
		
		System.out.println("Enter 2 numbers and an operator");
		System.out.println("Please enter a number");
		n1 = scan.nextDouble();
		System.out.println("Please enter a second number");
		n2 = scan.nextDouble();
		System.out.println("Please choose one of the below numbers: \n 1) Addition. \n 2) Subtraction. \n 3) Multiplication. \n 4) Division.");
		op = scan.nextDouble();
		if (op == 1) {
			System.out.println(n1 +" + " + n2 + " = " + (n1 + n2));				
		} else if (op == 2) {
			System.out.println(n1 +" - " + n2 + " = " + (n1 - n2));
		} else if (op == 3) {
			System.out.println(n1 +" * " + n2 + " = " + (n1 * n2));
		} else if (op == 4) {
			System.out.println(n1 +" / " + n2 + " = " + (n1 / n2));
		} else {
			System.out.println("Sorry, the choice " + op + " isn't recognised.");
		}

	}

}