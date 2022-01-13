public class Test1{
    static int c = 100;
    public static void main(String[]args){
        System.out.println("Hello主程式");
        B obj3 = new B();
        A obj1 = new A();
    }
    static{System.out.println("主類別初始區塊");}
}

class A{
    A(){System.out.println("A建構子");}
    static{System.out.println("A初始區塊");}
}
class B{
    static{System.out.println("B初始區塊");}
}