import java.util.Random;
public class homework_1{
    public static void main(String[] args){
        for(int b=0;b<4;b++)
        {
            if(b == 0){
                System.out.println("第一週");
                System.out.println(" ");
            }
            if(b == 1){
                System.out.println("第二週");
                System.out.println(" ");

            }
            if(b == 2){
                System.out.println("第三週");
                System.out.println(" ");

            }
            if(b == 3){
                System.out.println("第四週");
                System.out.println(" ");

            }
            for(int a=0;a<8;a++)
            {
                Random num = new Random();
                int[] x = new int[4];
                for(int i=0; i<4;i++){
                    x[i]=num.nextInt(99)+1;                    for(int j=0;j<i;j++){
                        if(x[j]==x[i]){
                            x[i] = num.nextInt(5)+1;
                            j=0;
                        }
                        else j++;
                    }
                    System.out.print(""+x[i]+"\t");
                }

                if(a == 0){
                    System.out.print("國旅券");
                }
                if(a == 1){
                    System.out.print("i原券");
                }
                if(a == 2){
                    System.out.print("農遊券");
                }
                if(a == 3){
                    System.out.print("數位藝fun券");
                }
                if(a == 4){
                    System.out.print("紙本藝fun券");
                }
                if(a == 5){
                    System.out.print("動滋券");
                }
                if(a == 6){
                    System.out.print("客庄券");
                }
                if(a == 7){
                    System.out.print("地方創生券");
                }
                System.out.println(" ");
            System.out.println();
            }
        }
    }
}