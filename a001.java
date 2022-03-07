import java.util.Scanner;

public class a001 {
    public static void main(String[]arg)
    {
        String a;
        try (Scanner scanner = new Scanner(System.in)) {
            a = scanner.nextLine();
        }
        System.out.println("hello, "+a);
    }
}
